// this_file: scripts/search_backend/tests.cjs
const test=require("node:test"), assert=require("node:assert/strict"), fs=require("node:fs"), os=require("node:os"), path=require("node:path");
const {execFileSync}=require("node:child_process"),{Search}=require("./engine.cjs");
const {candidates,hydrate,validateManifest,decodeRouting,readVarint}=require("./router.cjs"),{QueryRunner}=require("./query.cjs");
const dir=fs.mkdtempSync(path.join(os.tmpdir(),"complete-search-test-"));
const config={lang:["en"],separator:"[\\s\\-]+",pipeline:["trimmer"],fields:{title:{boost:1000},text:{boost:1},tags:{boost:1000000}}};
const corpus={config,docs:[{location:"a.html",title:"Alpha",text:"Signal resize",boost:100},
 {location:"a.html#close",title:"Alpha.close",text:"Close Signal",tags:["fly.Alpha.close"]},
 {location:"b.html",title:"Beta",text:"Signal other"},
 {location:"b.html#resize",title:"Beta.resize",text:"Resize widget",tags:["fly.Beta.resize"]}]};
const input=path.join(dir,"input.json");fs.writeFileSync(input,JSON.stringify(corpus));
execFileSync(process.execPath,[path.join(__dirname,"build.cjs"),input,dir,"150"]);
const manifest=validateManifest(JSON.parse(fs.readFileSync(path.join(dir,"manifest.json"))));
const terms=JSON.parse(fs.readFileSync(path.join(dir,"terms.json"))), bytes=fs.readFileSync(path.join(dir,"postings.bin"));
const routing=decodeRouting(manifest,terms,bytes), original=new Search({...JSON.parse(JSON.stringify(corpus)),options:{suggest:true}});
const locations = result => [...new Set(result.items.flatMap(g=>g.map(x=>x.location)))].sort();
test("qualified/unqualified/multi-term selection retains cross-namespace rows",()=>{
 assert.deepEqual(candidates("Alpha.close",manifest,routing).selected,[0]);
 assert.deepEqual(candidates("Signal",manifest,routing).selected,[0,1]);
 assert.deepEqual(candidates("Alpha.close Beta.resize",manifest,routing).selected,[0,1]);
});
for(const value of ["Signal","Alp","resize","+Signal -other","title:Alpha","tags:fly.Alpha.close",'"Signal"',"Sinal~1","*ignal","Sig*al","-other"])
 test(`original complete engine result set and suggestions: ${value}`,()=>{
  const selection=candidates(value,manifest,routing),groups=[],suggest=new Set();
  for(const id of selection.selected) {
   const spec=manifest.shards[id],rows=hydrate(JSON.parse(fs.readFileSync(path.join(dir,spec.file))),spec,selection.docs);
   const result=new Search({config,docs:rows,options:{suggest:true}}).search(value);
   groups.push(...result.items);for(const item of result.suggest)suggest.add(item);
  }
  assert.deepEqual(locations({items:groups}),locations(original.search(value)));
  if(value==="Alp")assert(suggest.size>0);
 });
test("malformed metadata and varints fail before READY",()=>{
 for(const broken of [Uint8Array.of(128),Uint8Array.of(128,0),Uint8Array.of(255,255,255,255,16),Uint8Array.of(128,128,128,128,128,0)])
  assert.throws(()=>readVarint(broken,{at:0}),/varint/);
 assert.throws(()=>decodeRouting(manifest,terms,bytes.subarray(0,-1)),/varint/);
 assert.throws(()=>decodeRouting(manifest,[...terms].reverse(),bytes),/terms/);
 assert.throws(()=>decodeRouting(manifest,terms,Buffer.concat([bytes,Buffer.of(0)])),/Trailing/);
 assert.throws(()=>validateManifest({...manifest,rows:manifest.rows+1}),/count/);
 assert.throws(()=>validateManifest({...manifest,shards:[{...manifest.shards[0],start:5}]}),/range/);
 assert.throws(()=>decodeRouting({...manifest,rows:1},[terms[0]],Buffer.of(2,0,1)),/terms|count/);
});
test("every encoded posting list equals the unchanged engine field references",()=>{
 const expected=new Map();
 for(const spec of manifest.shards) {
  const rows=JSON.parse(fs.readFileSync(path.join(dir,spec.file))),ids=new Map(rows.map((row,i)=>[row.location,spec.start+i]));
  const engine=new Search({config,docs:rows,options:{suggest:false}});
  for(const [term,posting] of Object.entries(engine.index.invertedIndex)) {
   if(!expected.has(term))expected.set(term,new Set());
   for(const field of engine.index.fields)for(const ref of Object.keys(posting[field]))expected.get(term).add(ids.get(ref));
  }
 }
 assert.equal(expected.size,terms.length);
 for(const [i,term] of terms.entries()) {
  const pointer={at:routing.offsets[i]},count=readVarint(bytes,pointer),actual=[];let row=0;
  for(let j=0;j<count;j++){row+=readVarint(bytes,pointer);actual.push(row);}
  assert.deepEqual(actual,[...expected.get(term)].sort((a,b)=>a-b),`Every posting for ${term}`);
 }
});
test("missing/corrupt/delayed fetch emits no partial data; cancellation releases buffers",async()=>{
 const previous=global.fetch;let metrics;
 global.fetch=async url=>new Response(fs.readFileSync(path.join(dir,path.basename(url.pathname))));
 const runner=new QueryRunner(manifest,routing,{suggest:true},new URL("http://fixture.test/prefix/search/complete/"),m=>metrics=m);
 assert.deepEqual(locations(await runner.execute("Signal",new AbortController().signal,()=>true)),locations(original.search("Signal")));
 assert(metrics.peakLiveBytes>0 && metrics.cacheBytes>0 && metrics.liveBytes===0);
 runner.cache.clear();runner.cacheBytes=0;
 global.fetch=async()=>new Response("not found",{status:404});
 await assert.rejects(runner.execute("Signal",new AbortController().signal,()=>true),/404/);
 global.fetch=async()=>new Response("[]");
 await assert.rejects(runner.execute("Signal",new AbortController().signal,()=>true));
 global.fetch=(url,{signal})=>new Promise((resolve,reject)=>signal.addEventListener("abort",()=>reject(signal.reason),{once:true}));
 const control=new AbortController();const pending=runner.execute("Signal",control.signal,()=>!control.signal.aborted);control.abort();
 await assert.rejects(pending);assert.equal(metrics.liveBytes,0);
 global.fetch=previous;
});
process.on("exit",()=>fs.rmSync(dir,{recursive:true,force:true}));
