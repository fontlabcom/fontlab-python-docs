// this_file: tests/search_complete_consumer.cjs
// Read-only full-corpus gate. Inputs are an original index, generated complete directory and query fixture.
const fs=require("node:fs"),path=require("node:path"),{Search}=require("../scripts/search_backend/engine.cjs");
const {candidates,hydrate,validateManifest,decodeRouting}=require("../scripts/search_backend/router.cjs");
const [input,directory,fixture,output]=process.argv.slice(2);
const corpus=JSON.parse(fs.readFileSync(input)), manifest=validateManifest(JSON.parse(fs.readFileSync(path.join(directory,"manifest.json"))));
const routing=decodeRouting(manifest,JSON.parse(fs.readFileSync(path.join(directory,"terms.json"))),fs.readFileSync(path.join(directory,"postings.bin")));
const named=JSON.parse(fs.readFileSync(fixture));
const queries={...named,resize:null,"resize Signal":null,'"Signal"':null,"title:Signal":null,"+Signal -resize":null,
 "tags:fly.fl":null,"Sinal~1":null,"*ignal":null,"Sig*al":null,"-resize":null};
const started=performance.now(), original=new Search({...corpus,options:{suggest:true}}),report={rows:corpus.docs.length,index_ms:performance.now()-started,queries:[]};
function locations(result) {return [...new Set(result.items.flatMap(g=>g.map(x=>x.location)))].sort();}
for(const [query,target] of Object.entries(queries)) {
 const t=performance.now(),selection=candidates(query,manifest,routing),groups=[],suggest=new Set();
 for(const id of selection.selected) {
  const spec=manifest.shards[id],rows=hydrate(JSON.parse(fs.readFileSync(path.join(directory,spec.file))),spec,selection.docs);
  const result=new Search({config:manifest.config,docs:rows,options:{suggest:true}}).search(query);
  groups.push(...result.items);for(const suggestion of result.suggest)suggest.add(suggestion);
 }
 groups.sort((a,b)=>b[0].score-a[0].score);
 const expected=locations(original.search(query)),actual=locations({items:groups}),top=groups.slice(0,20).flatMap(g=>g.map(x=>x.location));
 const item={query,ms:performance.now()-t,selected:selection.selected.length,results:actual.length,
  equal:JSON.stringify(actual)===JSON.stringify(expected),target_first20:target===null||top.some(x=>x.includes(target)),suggestions:[...suggest]};
 report.queries.push(item);console.log(JSON.stringify({...item,suggestions:item.suggestions.length}));
 if(!item.equal||!item.target_first20)process.exitCode=1;
}
fs.writeFileSync(output,JSON.stringify(report,null,2)+"\n");
