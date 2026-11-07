// this_file: scripts/archive_search/tests.cjs
const test = require("node:test"), assert = require("node:assert/strict");
const fs = require("node:fs"), path = require("node:path"), vm = require("node:vm");
const zlib = require("node:zlib"), crypto = require("node:crypto"), cp = require("node:child_process");
const ROOT = __dirname, SITE = path.resolve(ROOT,"../.."), TMP = path.join(SITE,".build/archive-tests");
const MODULES = path.join(SITE,".build/archive-compiler/node_modules");
const sha = bytes => crypto.createHash("sha256").update(bytes).digest("hex");
const json = value => JSON.stringify(value, (_,v) => typeof v === "number" && !Number.isFinite(v) ? {$number:String(v)} : v);
const plain = value => JSON.parse(json(value));
const fixture = name => JSON.parse(zlib.gunzipSync(fs.readFileSync(path.join(ROOT,"fixtures",name+".json.gz"))));
const receipt = JSON.parse(fs.readFileSync(path.join(ROOT,"dist/receipt.json")));
const worker = process.env.ARCHIVE_SEARCH_RED_WORKER || path.join(ROOT,"dist",receipt.worker);
const index = JSON.parse(cp.execFileSync("tar",["-xOf",path.join(SITE,"archive/fontlab7-site.tar.gz"),"pythonqt/search/search_index.json"],{maxBuffer:16*1024*1024}));
const synthetic = ["run","running","runner","needle","needles","agree","agreed","agre","quartz"].map(x=>({location:x+".html",title:x,text:x,tags:[]}));
const extended = [...synthetic,{location:"parent.html",title:"Parent <em>heading</em>",text:"unrelated",tags:["sample"]},
  {location:"parent.html#one",title:"Running &amp; callable",text:"<p>Needles available <code>agree</code> running running.</p>",tags:["running","available"]},
  {location:"unicode.html",title:"café naïve 中文",text:"Żółć café a+b foo:bar a_b run-running available callable",tags:["café"]}];
const cohorts = {synthetic,extended,needle:[{location:"fixture.html",title:"Mechanical archive fixture",text:"Archive verification needle example.",tags:[]}],
  "no-needle":[{location:"fixture.html",title:"Mechanical archive fixture",text:"Archive verification quartz example.",tags:[]}],corpus:index.docs,
  empty:[], stopword:[{location:"stop.html",title:"the",text:"the a an",tags:[]}]};

async function probe(file, docs, queries, suggest) {
  let listener; const messages=[], warnings=[];
  const context = {URL,TextEncoder,TextDecoder,setTimeout,clearTimeout,
    console:{warn(...args){warnings.push(args.map(x=>typeof x === "object" ? {name:x.name,message:x.message}:x));}},
    addEventListener(name,fn){assert.equal(name,"message");listener=fn;},postMessage(message){messages.push(plain(structuredClone(message)));}};
  for (const name of ["importScripts","fetch","XMLHttpRequest","WebSocket"])
    context[name]=()=>{throw Error("NETWORK_DENIED");};
  context.self=context;
  vm.runInNewContext(fs.readFileSync(file,"utf8"),context,{filename:file,timeout:5000});
  const before=sha(JSON.stringify(docs)), payload=structuredClone({type:0,data:{config:index.config,options:{suggest},docs}});
  await listener({data:payload}); assert.equal(sha(JSON.stringify(docs)),before,"caller docs mutated");
  const ready=messages.at(-1), results=[];
  for (const query of queries) {warnings.length=0;await listener({data:{type:2,data:query}});results.push({query,message:messages.at(-1),warnings:structuredClone(warnings)});}
  let invalid;try{await listener({data:{type:99}});}catch(error){invalid={name:error.name,message:error.message};}
  return {ready,invalid,results,after:sha(JSON.stringify(payload.data.docs))};
}

fs.mkdirSync(TMP,{recursive:true});
const esbuild=require(path.join(MODULES,"esbuild"));
const unitFile=path.join(TMP,"units.cjs");
const instrumented=[];
const coveragePlugins=process.env.ARCHIVE_SEARCH_COVERAGE ? [{name:"whole-module-coverage",setup(build){
  build.onLoad({filter:/\.ts$/},args=>{
    const relative=path.relative(ROOT,args.path).split(path.sep).join("/");
    const mandatory=["src/templates/assets/javascripts/integrations/search/_/index.ts","src/templates/assets/javascripts/integrations/search/query/_/index.ts","src/templates/assets/javascripts/integrations/search/query/transform/index.ts","src/templates/assets/javascripts/integrations/search/literal.ts"];
    if(!mandatory.includes(relative)) return;
    const source=fs.readFileSync(args.path,"utf8");
    const instrumenter=require(path.join(MODULES,"istanbul-lib-instrument")).createInstrumenter({parserPlugins:["typescript"],esModules:true,produceSourceMap:true});
    const contents=instrumenter.instrumentSync(source,args.path);
    instrumented.push({path:relative,sha256:sha(source),map:instrumenter.lastSourceMap()});
    return {contents,loader:"ts"};
  });
}}] : [];
(async()=>{
await esbuild.build({absWorkingDir:ROOT,stdin:{contents:
  `export {Search} from './src/templates/assets/javascripts/integrations/search/_';
   export * from './src/templates/assets/javascripts/integrations/search/literal';
   export * from './src/templates/assets/javascripts/integrations/search/query/_';
   export {transform} from './src/templates/assets/javascripts/integrations/search/query/transform';`,
  resolveDir:ROOT,sourcefile:"test-entry.ts",loader:"ts"},outfile:unitFile,bundle:true,format:"cjs",platform:"node",target:"es2020",sourcemap:true,nodePaths:[MODULES],plugins:coveragePlugins});
global.lunr=require(path.join(MODULES,"lunr"));
const unit=require(unitFile);
const makeSearch = (docs=extended,suggest=false) => new unit.Search({config:structuredClone(index.config),docs:structuredClone(docs),options:{suggest}});

test("ordinary callable completion repairs the stock omission and highlights QPen available",async()=>{
  const actual=await probe(worker,index.docs,["callable","available"],false);
  const call=actual.results[0].message.data.items.flat(),available=actual.results[1].message.data.items.flat();
  assert.equal(call.length,2);assert.equal(actual.results[0].message.data.items.length,1);
  assert.ok(call.some(item=>JSON.stringify(item).includes("<mark>callable</mark>")));
  assert.equal(available.length,475);
  assert.ok(available.some(item=>item.location === "PythonQt.QtGui.html#help_200" && item.text.includes("QPen.help") && JSON.stringify(item).includes("<mark>available</mark>")));
});

test("pure-negative queries repair NaN to exact finite zero without changing mixed scores",async()=>{
  const actual=await probe(worker,extended,["-run","-run +agree","-run needle","-run running"],false);
  assert.ok(actual.results[0].message.data.items.flat().length>0);
  for(const item of actual.results[0].message.data.items.flat()) assert.equal(item.score,0);
  assert.ok(actual.results[1].message.data.items.flat().some(item=>item.score>0));
  assert.ok(actual.results[2].message.data.items.flat().some(item=>item.score>0));
  assert.deepEqual(actual.results[3].message.data.items,[],"original required/prohibited constraints still exclude run/running");
});

test("all 312 frozen candidate-negation messages, warnings and setup identities stay exact",async()=>{
  const frozen=fixture("candidate-negation-results");let count=0;
  for(const run of frozen.runs){
    const actual=await probe(worker,cohorts[run.cohort],run.next.results.map(row=>row.query),run.suggest);
    assert.deepEqual(actual.results,run.next.results,`${run.cohort}/${run.suggest}`);
    assert.deepEqual(actual.ready,run.next.ready);assert.deepEqual(actual.invalid,run.next.invalid);
    assert.equal(actual.after,run.next.worker_docs_after_setup_sha256);count+=actual.results.length;
  }
  assert.equal(count,312);
});

test("stock 312 witnesses and 206 explicit/non-completed messages retain full lineage",async()=>{
  const frozen=fixture("baseline-results");let count=0;
  for(const run of frozen.runs){
    const actual=await probe(path.join(ROOT,"provenance/original/search.2c215733.min.js"),cohorts[run.cohort],run.old.results.map(row=>row.query),run.suggest);
    assert.deepEqual(actual.results,run.old.results);count+=actual.results.length;
  }
  assert.equal(count,312);
  const candidate=fixture("candidate-results"),fixed=fixture("candidate-negation-results");let explicit=0;
  const annotation=new Map(fixture("adapter-checks").annotations.map(row=>[row.query,row.completed]));
  for(let i=0;i<candidate.runs.length;i++) for(let j=0;j<candidate.runs[i].next.results.length;j++){
    const a=candidate.runs[i],b=fixed.runs[i],old=a.old.results[j],next=a.next.results[j];
    if((annotation.has(old.query)&&annotation.get(old.query).length===0)||["+callable","+available","title:available","+available -help"].includes(old.query)){
      assert.deepEqual(next,old);
      const expected=structuredClone(old), state={negated:false};
      try { unit.parseSearchQuery(unit.transformSearchQuery(old.query),state); } catch(error) { assert.ok(old.warnings.length,"the frozen worker reports invalid queries"); }
      if(state.negated) for(const item of expected.message.data.items.flat()) if(item.score?.$number==="NaN") item.score=0;
      assert.deepEqual(b.next.results[j],expected);explicit++;
    }
  }
  assert.equal(explicit,206);
});

test("all 90 focused negative messages preserve exclusions/grouping and exact corrected scores",async()=>{
  let count=0,changes=0;
  for(const run of fixture("negative-probe")){
    const actual=await probe(worker,cohorts[run.name],run.fixed.results.map(row=>row.query),run.suggest);
    assert.deepEqual(actual.results,run.fixed.results);
    changes+=run.changes;count+=actual.results.length;
    for(const row of run.exact.results) for(const item of row.message.data.items.flat())
      if(item.score?.$number==="NaN") assert.ok(run.fixed.results.find(other=>other.query===row.query).message.data.items.flat().some(other=>other.location===item.location&&other.score===0));
  }
  assert.equal(count,90);assert.equal(changes,230);
});

test("complete transform/parser helper and all 66 frozen completion annotations",()=>{
  const frozen=fixture("adapter-checks");
  for(const row of frozen.annotations){let completed=[];assert.equal(unit.transformSearchQuery(row.query,completed),row.transformed);assert.deepEqual(completed,row.completed);}
  assert.equal(frozen.annotations.length,66);
  const baselineFile=path.join(TMP,"baseline-transform.cjs");
  esbuild.buildSync({entryPoints:[path.join(ROOT,"provenance/baseline/src/templates/assets/javascripts/integrations/search/query/transform/index.ts")],outfile:baselineFile,bundle:true,format:"cjs",platform:"node"});
  const baseline=require(baselineFile).transform;
  assert.equal(baseline(' "run running" ',word=>[word,word]),"* * +run +run +running +running");
  assert.equal(unit.transform(' "run running" ',word=>[word,word]),baseline(' "run running" ',word=>[word,word]));
  assert.equal(unit.transform("run"),"run*");
  const state={negated:false};const clauses=unit.parseSearchQuery("-run",state);assert.equal(state.negated,true);assert.equal(clauses.length,1);
  unit.parseSearchQuery("*ning run*",state);assert.equal(state.negated,false);
  assert.deepEqual(plain(unit.getSearchQueryTerms([{term:"run"},{term:"absent"},{term:"the"}],["running"])),{run:true,absent:false});
  assert.throws(()=>unit.parseSearchQuery("title:"),/expecting term/);
});

test("reserved namespaces, extra escapes and malformed query controls retain frozen messages",()=>{
  const search=makeSearch(extended,true),frozen=fixture("adapter-checks");
  for(const row of frozen.extraResults){
    const expected=structuredClone(row.next);
    if(row.query==="-the") for(const item of expected.value.items.flat()) if(item.score?.$number==="NaN") item.score=0;
    let actual;try{actual={value:search.search(row.query)};}catch(error){actual={error:{name:error.name,message:error.message}};}
    assert.deepEqual(plain(actual),expected,row.query);
  }
  for(const row of frozen.expansions)assert.deepEqual(plain(search.index.tokenSet.intersect(lunr.TokenSet.fromString(row.term)).toArray()),row.next);
});

test("initialization and runtime shape guards fail clearly without global interception",()=>{
  const config=structuredClone(index.config);
  for(const [name,value] of [["separator","different"],["lang",["de"]],["fields",{}]])
    assert.throws(()=>unit.guard({...config,[name]:value},[]),/Unsupported archived search identity/);
  const version=lunr.version;lunr.version="different";assert.throws(()=>unit.guard(config,[]),/Unsupported/);lunr.version=version;
  assert.throws(()=>makeSearch([{location:"reserved",title:"\uE000marker",text:""}]),/Reserved literal namespace/);
  assert.throws(()=>unit.install({invertedIndex:{},tokenSet:{edges:{}}}),/Unsupported locked TokenSet shape/);
  assert.throws(()=>unit.install({invertedIndex:{},tokenSet:{intersect(){}}}),/Unsupported locked TokenSet shape/);
  const original=lunr.TokenSet.fromString;lunr.TokenSet.fromString=()=>({edges:{}});
  assert.throws(()=>unit.install({invertedIndex:{},tokenSet:{edges:{},intersect(){}}}),/Unsupported locked TokenSet shape/);lunr.TokenSet.fromString=original;
  const originalQuery=lunr.Index.prototype.query;const a=makeSearch(),b=makeSearch();assert.equal(lunr.Index.prototype.query,originalQuery);
  assert.deepEqual(plain(a.search("running")),plain(b.search("running")));
  assert.throws(()=>a.literalSearch("title:",[]),/expecting term/);
  assert.ok(b.search("running").items.length);
});

test("complete Search handles absent fields, parents, duplicate positions and missing references",()=>{
  const search=makeSearch([{location:"one.html",title:"Running",text:"running running",tags:["running"]},{location:"one.html#part",title:"Child",text:"running"},{location:"empty.html",title:"",text:""}],true);
  assert.deepEqual(plain(search.search(" ")),{items:[]});
  for(const q of ["running","+running","-quartz","child","中文","run quartz"]){
    const result=search.search(q);assert.ok(!json(result).includes("<mark><mark>"));assert.ok(!json(result).includes("archive_literal_"));
  }
  const absent=makeSearch([{location:"absent.html",title:"Running"}]);assert.ok(absent.search("running").items.length);
  absent.literalSearch=()=>[{ref:"unknown",score:1,matchData:{metadata:{}}}];assert.deepEqual(plain(absent.search("running")),{items:[]});
  const clear=makeSearch([{location:"clear.html",title:"Running",text:"running"}]);
  const wrapped=clear.literalSearch;clear.literalSearch=(query,terms)=>{const found=wrapped(query,terms);clear.map.delete("clear.html");return found;};
  assert.deepEqual(plain(clear.search("running")),{items:[]});
});

test("locked compiler, preferred sources, maps and independent builds remain deterministic",()=>{
  const {compile,verify}=require("./compile.cjs");verify();
  const first=compile({output:path.join(TMP,"first")}),second=compile({output:path.join(TMP,"second")});assert.deepEqual(first,second);
  for(const name of [...Object.keys(first.files),"receipt.json","metafile.json"]){assert.ok(fs.readFileSync(path.join(TMP,"first",name)).equals(fs.readFileSync(path.join(TMP,"second",name))));assert.ok(fs.readFileSync(path.join(TMP,"first",name)).equals(fs.readFileSync(path.join(ROOT,"dist",name))));}
  assert.equal(first.worker,`search.${sha(fs.readFileSync(path.join(ROOT,"dist",first.worker)))}.js`);
  assert.equal(first.map,`search.${sha(fs.readFileSync(path.join(ROOT,"dist",first.map)))}.js.map`);
  const map=JSON.parse(fs.readFileSync(path.join(ROOT,"dist",first.map)));assert.ok(map.mappings.length);
  for(let i=0;i<map.sources.length;i++)assert.equal(fs.readFileSync(path.resolve(ROOT,"dist",map.sources[i]),"utf8"),map.sourcesContent[i]);
  assert.throws(()=>compile({compiler:{version:"wrong"}}),/Pinned esbuild/);
  const broken=path.join(TMP,"broken");fs.cpSync(ROOT,broken,{recursive:true});
  fs.appendFileSync(path.join(broken,"src/templates/assets/javascripts/integrations/search/literal.ts"),"\n");
  assert.throws(()=>verify(broken),/preferred-source identity differs/);
  fs.copyFileSync(path.join(ROOT,"src/templates/assets/javascripts/integrations/search/literal.ts"),path.join(broken,"src/templates/assets/javascripts/integrations/search/literal.ts"));
  const lock=JSON.parse(fs.readFileSync(path.join(broken,"package-lock.json")));lock.packages["node_modules/lunr"].integrity="wrong";fs.writeFileSync(path.join(broken,"package-lock.json"),JSON.stringify(lock));
  assert.throws(()=>verify(broken),/Locked official Lunr dependency differs/);
  assert.throws(()=>compile({compiler:{version:"0.25.12",buildSync(){return {outputFiles:[{path:"search.js.map",contents:Buffer.from("{}")} ,{path:"search.js",text:"missing trailer"}]};}}}),/source-map trailer/);
});

if(process.env.ARCHIVE_SEARCH_COVERAGE) test.after(()=>{
  fs.writeFileSync(path.join(TMP,"istanbul.json"),JSON.stringify(global.__coverage__,null,2)+"\n");
  fs.writeFileSync(path.join(TMP,"instrumented-sources.json"),JSON.stringify(instrumented,null,2)+"\n");
  const rows=Object.entries(global.__coverage__).map(([file,c])=>{
    const statements=Object.values(c.s),branches=Object.values(c.b).flat();
    const covered=statements.filter(Boolean).length+branches.filter(Boolean).length;
    return {file,statements:[statements.filter(Boolean).length,statements.length],branches:[branches.filter(Boolean).length,branches.length],combined:covered/(statements.length+branches.length)};
  });
  fs.writeFileSync(path.join(TMP,"coverage-summary.json"),JSON.stringify(rows,null,2)+"\n");
  assert.equal(rows.length,4);
  for(const row of rows) assert.ok(row.branches[1]>0 && row.combined>=0.8,JSON.stringify(row));
});

})().catch(error=>{console.error(error);process.exitCode=1;});
