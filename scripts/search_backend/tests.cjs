// this_file: scripts/search_backend/tests.cjs
const test=require("node:test"), assert=require("node:assert/strict"), fs=require("node:fs"), os=require("node:os"), path=require("node:path");
const vm=require("node:vm");
const {execFileSync}=require("node:child_process"),{Search}=require("./engine.cjs");
const {candidates,hydrate,validateManifest,decodeRouting,readVarint,encodeTerms}=require("./router.cjs"),{QueryRunner}=require("./query.cjs");
const dir=fs.mkdtempSync(path.join(os.tmpdir(),"complete-search-test-"));
const config={lang:["en"],separator:"[\\s\\-]+",pipeline:["trimmer"],fields:{title:{boost:1000},text:{boost:1},tags:{boost:1000000}}};
const corpus={config,docs:[{location:"a.html",title:"Alpha",text:"Signal resize",boost:100},
 {location:"a.html#close",title:"Alpha.close",text:"Close Signal",tags:["fly.Alpha.close"]},
 {location:"b.html",title:"Beta",text:"Signal other"},
 {location:"b.html#resize",title:"Beta.resize",text:"Resize widget",tags:["fly.Beta.resize"]}]};
const input=path.join(dir,"input.json");fs.writeFileSync(input,JSON.stringify(corpus));
execFileSync(process.execPath,[path.join(__dirname,"build.cjs"),input,dir,"150"]);
const manifest=validateManifest(JSON.parse(fs.readFileSync(path.join(dir,"manifest.json"))));
const encodedTerms=JSON.parse(fs.readFileSync(path.join(dir,"terms.json"))), bytes=fs.readFileSync(path.join(dir,"postings.bin"));
const routing=decodeRouting(manifest,encodedTerms,bytes), terms=routing.terms, original=new Search({...JSON.parse(JSON.stringify(corpus)),options:{suggest:true}});
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
 assert.throws(()=>decodeRouting(manifest,encodedTerms,bytes.subarray(0,-1)),/varint/);
 assert.throws(()=>decodeRouting(manifest,encodeTerms([...terms].reverse()),bytes),/terms/);
 assert.throws(()=>decodeRouting(manifest,encodedTerms,Buffer.concat([bytes,Buffer.of(0)])),/Trailing/);
 assert.throws(()=>validateManifest({...manifest,rows:manifest.rows+1}),/count/);
 assert.throws(()=>validateManifest({...manifest,shards:[{...manifest.shards[0],start:5}]}),/range/);
 assert.throws(()=>decodeRouting({...manifest,rows:1},encodeTerms([terms[0]]),Buffer.of(2,0,1)),/terms|count/);
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
test("shard deadline fails fast, then doubles per Retry up to the startup cap",async()=>{
 const {shardDeadline}=require("./query.cjs");
 assert.deepEqual([0,1,2,3,4,5,9].map(shardDeadline),[1800,3600,7200,14400,28800,30000,30000]);
 const previous=global.fetch;
 global.fetch=(url,{signal})=>new Promise((resolve,reject)=>{
  const timer=setTimeout(()=>resolve(new Response(fs.readFileSync(path.join(dir,path.basename(url.pathname))))),60);
  signal.addEventListener("abort",()=>{clearTimeout(timer);reject(signal.reason);},{once:true});
 });
 const runner=new QueryRunner(manifest,routing,{suggest:false},new URL("http://fixture.test/search/complete/"),()=>{});
 await assert.rejects(runner.execute("Signal",new AbortController().signal,()=>true,"default",10),/TimeoutError|timed out|aborted/i);
 assert.deepEqual(locations(await runner.execute("Signal",new AbortController().signal,()=>true,"reload",1000)),locations(original.search("Signal")));
 global.fetch=previous;
});
process.on("exit",()=>fs.rmSync(dir,{recursive:true,force:true}));

async function until(condition) {
 const deadline=Date.now()+1000;
 while(!condition()) {if(Date.now()>deadline)throw Error("Timed out waiting for fixture state");await new Promise(resolve=>setTimeout(resolve,5));}
}
test("persisted page restoration reopens/reconciles retry channel through repeated transitions",async()=>{
 const channels=[];
 class TrackedChannel extends BroadcastChannel {constructor(name){super(name);channels.push(this);}}
 const events=new Map(), config={textContent:'{"search":"unused"}'}, meta={},list={},output={dataset:{},prepend(panel){this.panel=panel;},querySelector(selector){return selector.includes("__list")?list:meta;}};
 const document={currentScript:{dataset:{worker:"assets/javascripts/workers/complete-search.js"}},
  getElementById(){return config;},querySelector(){return output;},createElement(){return {dataset:{},style:{},children:[],setAttribute(){},append(...children){this.children.push(...children);}};}};
 let reloads=0;
 try {vm.runInNewContext(fs.readFileSync(path.resolve(__dirname,"../../overrides/assets/javascripts/complete-search-ui.js"),"utf8"),{
  document,URL,crypto,BroadcastChannel:TrackedChannel,setTimeout,clearTimeout,location:{href:"http://fixture.test/prefix/",reload(){reloads++;}},
  addEventListener(name,fn,options){if(!events.has(name))events.set(name,[]);events.get(name).push({fn,once:options?.once});}
 });} catch(error) {for(const channel of channels)channel.close();throw error;}
 const peer=new BroadcastChannel(new URL(JSON.parse(config.textContent).search).searchParams.get("channel")), received=[];
 let current={state:"error",phase:"query"};peer.onmessage=({data})=>{received.push(data);if(data.type==="status")peer.postMessage(current);};
 const dispatch=(name,event)=>{for(const listener of events.get(name)||[]){listener.fn(event);if(listener.once)events.set(name,events.get(name).filter(x=>x!==listener));}};
 const retry=output.panel.children[1];
 try {
  peer.postMessage(current);await until(()=>output.dataset.completeSearchState==="error");
  assert(events.has("pageshow"),"Persisted restoration needs an explicit pageshow listener");
  for(let i=0;i<2;i++) {
   dispatch("pagehide",{persisted:true});current={state:"error",phase:"query"};peer.postMessage(current);
   dispatch("pageshow",{persisted:true});await until(()=>received.filter(x=>x.type==="status").length===i+1);
   await until(()=>output.panel.hidden===false && retry.disabled===false);
   assert.doesNotThrow(()=>retry.onclick(),"Retry must never use a closed channel");
   await until(()=>received.filter(x=>x.type==="retry").length===i+1);
   current={state:"ready"};peer.postMessage(current);await until(()=>output.panel.hidden && !meta.hidden && !list.hidden);
  }
  current={state:"error",phase:"query"};peer.postMessage(current);await until(()=>!output.panel.hidden);
  assert.equal(reloads,0,"Persisted restoration cannot be replaced by an automatic reload");
 } finally {dispatch("pagehide",{persisted:false});peer.close();for(const channel of channels)channel.close();}
});
test("actual compiled worker returns ordinary empty results for original parser errors only",async()=>{
 const messages=[], states=[], handlers=new Map(), channels=[], name=`parse-${crypto.randomUUID()}`;
 class TrackedChannel extends BroadcastChannel {constructor(name){super(name);channels.push(this);}}
 const peer=new BroadcastChannel(name);peer.onmessage=({data})=>states.push(data);
 let missing=false;
 const source=fs.readFileSync(path.resolve(__dirname,"../../overrides/assets/javascripts/workers/complete-search.js"),"utf8");
 try {vm.runInNewContext(source,{URL,BroadcastChannel:TrackedChannel,crypto,AbortController,AbortSignal,TransformStream,DecompressionStream,
  Uint8Array,Uint32Array,TextDecoder,setTimeout,clearTimeout,console,
  location:{href:`http://fixture.test/prefix/assets/javascripts/workers/complete-search.js?channel=${name}`},
  addEventListener(type,handler){handlers.set(type,handler);},postMessage(message){messages.push(message);},
  fetch:async url=>missing&&url.pathname.includes("rows-")?new Response("missing",{status:404}):new Response(fs.readFileSync(path.join(dir,path.basename(url.pathname))))});
 } catch(error) {peer.close();for(const channel of channels)channel.close();throw error;}
 const setupBytes=fs.readFileSync(path.join(dir,"manifest.json"));
 const spec={file:"manifest.json",raw:setupBytes.length,gzip:fs.statSync(path.join(dir,"manifest.json.gz")).size,sha256:require("node:crypto").createHash("sha256").update(setupBytes).digest("hex")};
 const message=data=>handlers.get("message")({data});
 try {
  message({type:0,data:{config:{complete:{manifest:spec}},docs:[],options:{suggest:false}}});await until(()=>messages.some(x=>x.type===1));
  for(const value of ["Signal~x","Signal^foo","title:Signal~x"]) {
   const before=messages.length, stateBefore=states.length;message({type:2,data:value});
   await until(()=>messages.length>before && states.slice(stateBefore).some(x=>x.state==="ready"||x.state==="error"));
   assert.equal(JSON.stringify(messages.at(-1)),JSON.stringify({type:3,data:{items:[]}}));
   assert(!states.slice(stateBefore).some(x=>x.state==="error"),"Invalid query syntax is not a transport outage");
  }
  missing=true;const before=states.length;message({type:2,data:"Signal"});
  await until(()=>states.slice(before).some(x=>x.state==="error"));
  assert(states.slice(before).some(x=>x.message?.includes("404")),"Network failures must remain unavailable");
  const restored=states.length;peer.postMessage({type:"status"});
  await until(()=>states.length>restored);
  assert(states.slice(restored).some(x=>x.state==="error" && x.message?.includes("404")),"Restored pages must receive the actual worker's current failure status");
 } finally {peer.close();for(const channel of channels)channel.close();}
});
test("lunr TokenSet keys stay distinct when a digit label meets a node id (lunr 2.3.9 defect)",()=>{
 // Unpatched lunr keys both nodes as "01234": minimisation merged them and the full
 // index lost words (issue 106, final-6). Keys must encode label, id and a terminator.
 const TokenSet=original.index.tokenSet.constructor, node=id=>Object.assign(new TokenSet(),{id});
 const a=new TokenSet(), b=new TokenSet();
 a.edges={"1":node(234)};
 b.edges={"1":node(2),"3":node(4)};
 assert.notEqual(a.toString(),b.toString());
});
test("every shipped lunr copy carries the TokenSet key patch exactly once",()=>{
 const root=path.resolve(__dirname,"../..");
 for(const file of ["scripts/search_backend/engine.cjs","scripts/search_backend/router.cjs","scripts/search_backend/query.cjs",
  "overrides/assets/javascripts/workers/complete-search.js"]){
  const source=fs.readFileSync(path.join(root,file),"utf8");
  assert.equal(source.split("str + label + node.id;").length-1,0,file+": unpatched lunr TokenSet key");
  assert.equal(source.split('str + label + node.id + ";";').length-1,1,file+": patched lunr TokenSet key");
 }
});
test("routing vocabulary is front-coded and decodes to the exact sorted terms",()=>{
 // R041 initial payload: the global vocabulary is the largest initial asset (issue 106).
 assert.equal(encodedTerms.format,"front-coded-1");
 assert.deepEqual(encodeTerms(terms),encodedTerms);
 const words=["","a","ab","abc","abd","b","b.c","b.cd","\u00e9t\u00e9"];
 assert.deepEqual(decodeRouting({...manifest,tokens:words.length,rows:1,shards:[]},encodeTerms(words),Buffer.from(words.map(()=>0))).terms,words);
});
test("malformed front-coded vocabularies fail before READY",()=>{
 const one={...manifest,tokens:2,rows:1,shards:[]},empty=Buffer.of(0,0),good=encodeTerms(["ab","ac"]);
 for(const bad of [["ab","ac"],{...good,format:"plain"},{...good,prefix:[0]},{...good,prefix:[0,3]},
   {...good,prefix:[0,-1]},{...good,prefix:[0,1.5]},{...good,suffix:["ab",7]},{...good,prefix:[0,0],suffix:["ab","ac"]},
   {...good,prefix:[1,1]}])
  assert.throws(()=>decodeRouting(one,bad,empty),/terms/,JSON.stringify(bad));
});
test("search UI starts on plain-http pages, where crypto.randomUUID is unavailable",()=>{
 // Browsers expose randomUUID only in secure contexts; getRandomValues works everywhere.
 const source=fs.readFileSync(path.resolve(__dirname,"../../overrides/assets/javascripts/complete-search-ui.js"),"utf8");
 const element={textContent:JSON.stringify({search:"assets/javascripts/workers/search.js"})};
 const context={URL,location:{href:"http://code.example/docs/"},
  crypto:{getRandomValues:array=>require("node:crypto").webcrypto.getRandomValues(array)},
  document:{currentScript:{dataset:{worker:"assets/javascripts/workers/complete-search.js"}},
   getElementById:()=>element,querySelector:()=>null}};
 vm.runInNewContext(source,context);
 const search=new URL(JSON.parse(element.textContent).search);
 assert.match(search.searchParams.get("channel"),/^complete-search-[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/);
});
