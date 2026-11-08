// this_file: scripts/archive_search/tests-ui.cjs
const test=require("node:test"),assert=require("node:assert/strict"),fs=require("node:fs"),path=require("node:path"),zlib=require("node:zlib"),crypto=require("node:crypto"),cp=require("node:child_process");
const ROOT=__dirname,SITE=path.resolve(ROOT,"../.."),TMP=path.join(SITE,".build/archive-ui-tests"),MODULES=path.join(SITE,".build/archive-compiler/node_modules");
const sha=b=>crypto.createHash("sha256").update(b).digest("hex");
const fixture=name=>JSON.parse(zlib.gunzipSync(fs.readFileSync(path.join(ROOT,"fixtures",`ui-${name}.json.gz`))));
const esbuild=require(path.join(MODULES,"esbuild")),{compile,verify}=require("./compile-ui.cjs");
const TEMPLATE="ui/src/templates/assets/javascripts/templates/search/index.tsx";
const CONTENT="ui/src/templates/assets/javascripts/components/content/_/index.ts";
let contentRuntime;
const VISIBILITY="ui/src/templates/assets/javascripts/browser/element/visibility/index.ts",visibilityContexts=[],visibilityCompiled=new Map();
const archivedHTML=cp.execFileSync("tar",["-xOf",path.join(SITE,"archive/fontlab7-site.tar.gz"),"pythonqt/index.html"],{maxBuffer:2*1024*1024}).toString();
const config=JSON.parse(archivedHTML.match(/<script[^>]*id="__config"[^>]*>(.*?)<\/script>/s)[1]);
config.base="https://example.test/fontlab-python-docs/archive/fontlab7/pythonqt/";
fs.mkdirSync(TMP,{recursive:true});
const instrumented=[];
async function renderer(){
 const plugins=process.env.ARCHIVE_UI_COVERAGE?[{name:"whole-search-template",setup(build){build.onLoad({filter:/templates\/search\/index\.tsx$/},args=>{
  const source=fs.readFileSync(args.path,"utf8");
  const instrumenter=require(path.join(MODULES,"istanbul-lib-instrument")).createInstrumenter({parserPlugins:["typescript","jsx"],esModules:true,produceSourceMap:true});
  const contents=instrumenter.instrumentSync(source,args.path);instrumented.push({path:TEMPLATE,sha256:sha(source),map:instrumenter.lastSourceMap()});return{contents,loader:"tsx"};
 });}}]:[];
 const result=await esbuild.build({absWorkingDir:ROOT,stdin:{contents:`export {renderSearchResultItem} from './${TEMPLATE}'; export {configuration} from './ui/src/templates/assets/javascripts/_';`,resolveDir:ROOT,sourcefile:"test-ui-entry.ts",loader:"ts"},outfile:path.join(TMP,"renderer.js"),tsconfig:path.join(ROOT,"ui/tsconfig.json"),bundle:true,format:"iife",platform:"browser",target:"es2015",globalName:"Renderer",nodePaths:[MODULES],write:false,plugins});
 return result.outputFiles[0].text;
}
function marked(value){let text="",marks=[],cursor=0;for(const match of value.matchAll(/<mark>(.*?)<\/mark>/gs)){text+=value.slice(cursor,match.index);marks.push({text:match[1],offset:text.length});text+=match[1];cursor=match.index+match[0].length;}text+=value.slice(cursor);return{text,marks};}
function expected(group,features=[]){
 const parent=group.find(doc=>!new URL(doc.location,config.base).hash),sections=group.filter(doc=>doc!==parent),threshold=group[0].score;
 const teasers=sections.filter(doc=>doc.score>=threshold).length;
 return [parent,...sections].map((doc,i)=>{
  const hasTeaser=i>0 || (group[0]===parent && teasers===0),fields=[doc.title,...(hasTeaser?[doc.text]:[]),...(doc.tags||[])];let text="",marks=[];
  for(const field of fields){const p=marked(field);marks.push(...p.marks.map(m=>({...m,offset:m.offset+text.length})));text+=p.text;}
  const missing=Object.keys(doc.terms).filter(key=>!doc.terms[key]);if(hasTeaser&&missing.length)text+=config.translations['search.result.term.missing']+': '+missing.join(' ');
  const url=new URL(doc.location,config.base);if(features.includes('search.highlight'))url.searchParams.set('h',Object.keys(doc.terms).filter(key=>doc.terms[key]).join(' '));
  return{text,marks,score:doc.score.toFixed(2),url:String(url)};
 });
}
let browser,page,source;
test.before(async()=>{
 const driver=cp.execFileSync('uv',['run','--no-sync','python','-c','from pathlib import Path; import playwright; print(Path(playwright.__file__).parent / "driver/package")'],{cwd:SITE}).toString().trim();
 const {chromium}=require(driver);browser=await chromium.launch({headless:true});page=await browser.newPage();await page.route("**/*",route=>route.abort());page.on("pageerror",error=>console.error("Renderer page error:",error.message));source=await renderer();
 await page.setContent(archivedHTML.replace(/<script\b[\s\S]*?<\/script>/gi, "").replace(/<link\b[^>]*>/gi, "") + `<script id="__config" type="application/json">${JSON.stringify(config)}</script><main id="results"></main>`);await page.addScriptTag({content:source});
});
test.after(async()=>{
 if(page&&process.env.ARCHIVE_UI_COVERAGE){const coverage=await page.evaluate(()=>globalThis.__coverage__);fs.writeFileSync(path.join(TMP,'template-coverage.json'),JSON.stringify({coverage,instrumented},null,2));}
 if(contentRuntime&&process.env.ARCHIVE_UI_COVERAGE)fs.writeFileSync(path.join(TMP,'content-coverage.json'),JSON.stringify({coverage:contentRuntime.context.__coverage__,instrumented:contentRuntime.instrumented},null,2));
 if(process.env.ARCHIVE_UI_COVERAGE&&visibilityContexts.length){const coverage=require(path.join(MODULES,'istanbul-lib-coverage')).createCoverageMap({});for(const context of visibilityContexts)if(context.__coverage__)coverage.merge(context.__coverage__);fs.writeFileSync(path.join(TMP,'visibility-coverage.json'),JSON.stringify({coverage:coverage.toJSON(),instrumented:visibilityCompiled.get(false).instrumented},null,2));}
 if(browser)await browser.close();
});
async function render(groups,features=[],tags){return page.evaluate(({groups,features,tags})=>{
 const cfg=Renderer.configuration();cfg.features=features;cfg.tags=tags;const root=document.querySelector('#results');root.replaceChildren();
 const results=[];for(const group of groups){const item=Renderer.renderSearchResultItem(group);root.appendChild(item);results.push({articles:[...item.querySelectorAll('article')].map(article=>{
  const text=article.textContent,marks=[...article.querySelectorAll('mark')].map(mark=>{const walker=document.createTreeWalker(article,NodeFilter.SHOW_TEXT);let node,offset=0;while(node=walker.nextNode()){if(mark.contains(node))break;offset+=node.textContent.length;}return{text:mark.textContent,offset};});
  return{text,marks,score:article.dataset.mdScore,url:article.parentElement.href,unexpected:[...article.querySelectorAll('*')].filter(el=>!['DIV','H1','H2','MARK','NAV','SPAN','P','DEL'].includes(el.tagName)).map(el=>el.tagName),nested:article.querySelectorAll('mark mark').length};}),more:[...item.querySelectorAll('summary')].map(el=>el.textContent),tagClasses:[...item.querySelectorAll('.md-tag')].map(el=>el.className)});}return results;
 },{groups,features,tags});}

test('full real immutable messages render every article with complete text and ordered UTF16 marks',async()=>{
 const evidence=[];
 for(const name of ['old-callable','candidate-callable','old-available','candidate-available']){
  const row=fixture(name),before=sha(JSON.stringify(row)),groups=row.message.data.items,actual=await render(groups);
  if(process.env.ARCHIVE_UI_RED_EVIDENCE)fs.writeFileSync(process.env.ARCHIVE_UI_RED_EVIDENCE,JSON.stringify({fixture:name,inputLength:groups[0][0].text.length,articles:actual.map(g=>g.articles.map(a=>({sha256:sha(a.text),length:a.text.length,unexpected:a.unexpected.length,marks:a.marks.map(m=>({...m,context:a.text.slice(Math.max(0,m.offset-100),m.offset+100)}))})))},null,2));
  for(let g=0;g<groups.length;g++){
   const want=expected(groups[g]);assert.equal(actual[g].articles.length,want.length);
   for(let i=0;i<want.length;i++){const got=actual[g].articles[i];assert.deepEqual(got.unexpected,[],`${name}/${g}/${i}: accidental representation elements`);assert.equal(got.nested,0);assert.deepEqual({text:got.text,marks:got.marks,score:got.score,url:got.url},want[i],`${name}/${g}/${i}: complete article`);}
  }
  assert.equal(sha(JSON.stringify(row)),before,'fixture message mutated');
  if(name.includes('callable')){
   const a=actual[0].articles[1];assert.equal(groups[0][0].text.length,769106);assert.deepEqual(a.marks.map(m=>m.offset),[766828,766904]);assert.equal(a.marks.length,2);
   assert.ok(a.text.slice(a.marks[0].offset-40,a.marks[0].offset+8).includes('Connects the signal to the Python callable'));
   assert.ok(a.text.slice(a.marks[1].offset-50,a.marks[1].offset+8).includes('Disconnects the signal from the given Python callable'));
   assert.ok(!a.text.includes('callablecallable'));
  }
  evidence.push({fixture:name,sha256:before,groups:groups.length,articles:actual.reduce((n,g)=>n+g.articles.length,0),complete_text:true,all_ordered_marks:true});
 }
 fs.writeFileSync(path.join(TMP,'complete-real-oracles.json'),JSON.stringify(evidence,null,2));
});

test('whole renderer preserves parent, thresholds, More, tags, terms, empty text and URL branches',async()=>{
 const doc=(location,score,title='Title <mark>café</mark> & "quoted" <unbound x> <=y',text='Teaser <built-in method> <class A> <==> 中文 <mark>Żółć</mark>',tags)=>({location,score,title,text,tags,terms:{'yes & <term>':true,'missing & <term>':false,second:false}});
 const p=()=>doc('page.html',10),s=(id,score=10)=>doc(`page.html#${id}`,score);
 const cases=[[p()],[p(),s('best')],[p(),s('one',5)],[p(),s('one',5),s('two',4)],[s('first',20),p(),s('lower',10)],[doc('empty.html',0,'','',[])],[doc('tag.html',0,'<mark>title</mark>','',['<mark>red</mark> & <tag>','plain'])]];
 for(const features of [[],['search.highlight']]){
  const got=await render(cases,features,{'plain':'custom'});
  for(let g=0;g<cases.length;g++)for(let i=0;i<got[g].articles.length;i++){
   const a=got[g].articles[i];assert.deepEqual({text:a.text,marks:a.marks,score:a.score,url:a.url},expected(cases[g],features)[i]);assert.deepEqual(a.unexpected,[]);assert.equal(a.nested,0);
  }
  assert.deepEqual(got[0].more,[]);assert.deepEqual(got[1].more,[]);assert.deepEqual(got[2].more,[config.translations['search.result.more.one']]);assert.deepEqual(got[3].more,[config.translations['search.result.more.other'].replace('#','2')]);
  assert.deepEqual(got[6].tagClasses,['md-tag md-tag-icon','md-tag md-tag-icon md-tag--custom']);
 }
 await render([[doc('no-tags.html',0,'title','text',['tag'])]],[],undefined);
 await assert.rejects(render([[]]));await assert.rejects(render([[doc('http://[',0)]]));
 await assert.rejects(render([[{...p(),tags:'bad'}]]));
});

test('unchanged upstream rich synthetic renderer remains a distinct control',async()=>{
 const stock=esbuild.buildSync({absWorkingDir:ROOT,stdin:{contents:"export {renderSearchResultItem} from './ui/provenance/upstream-javascripts/templates/search/index.tsx';",resolveDir:ROOT,sourcefile:"stock-control.ts",loader:"ts"},outfile:path.join(TMP,'stock-control.js'),tsconfig:path.join(ROOT,'ui/tsconfig.json'),bundle:true,format:'iife',platform:'browser',target:'es2015',globalName:'StockRenderer',nodePaths:[MODULES],write:false});
 await page.addScriptTag({content:stock.outputFiles[0].text});
 const value=await page.evaluate(()=>{const item=StockRenderer.renderSearchResultItem([{location:'rich.html',title:'<em>Rich heading</em>',text:'<p>Actual <code>rich</code> markup</p>',score:1,terms:{rich:true},tags:['<strong>tag</strong>']}]);return{title:item.querySelector('em').textContent,code:item.querySelector('code').textContent,tag:item.querySelector('strong').textContent};});
 assert.deepEqual(value,{title:'Rich heading',code:'rich',tag:'tag'});
});

test('compiler reproduces exact committed assets and every original mapped path except three scoped modules',()=>{
 const a=compile({output:path.join(TMP,'compile-one')}),b=compile({output:path.join(TMP,'compile-two')});assert.deepEqual(a,b);
 const committed=JSON.parse(fs.readFileSync(path.join(ROOT,'ui-dist/receipt.json')));assert.deepEqual(a,committed);
 for(const name of [...Object.keys(a.files),'receipt.json'])assert.deepEqual(fs.readFileSync(path.join(TMP,'compile-one',name)),fs.readFileSync(path.join(TMP,'compile-two',name)));
 const original=JSON.parse(fs.readFileSync(path.join(ROOT,'ui/provenance/original/bundle.1a8646e9.min.js.map'))),mapping=JSON.parse(fs.readFileSync(path.join(TMP,'compile-one',a.map)));
 assert.equal(mapping.sources.length,211);let changed=0;
 for(let i=0;i<original.sources.length;i++){
  const normalized=original.sources[i].replace(/^.*?(node_modules\/|src\/)/,'$1').replace(/^src\//,'materialx/');const j=mapping.sources.indexOf(normalized);assert.notEqual(j,-1,normalized);
  if(normalized.endsWith('/templates/search/index.tsx')||normalized.endsWith('/components/content/_/index.ts')||normalized.endsWith('/browser/element/visibility/index.ts')){assert.notEqual(mapping.sourcesContent[j],original.sourcesContent[i]);changed++;}else assert.equal(mapping.sourcesContent[j],original.sourcesContent[i],normalized);
 }
 assert.equal(changed,3);assert.ok(!mapping.sources.some(name=>name.startsWith('/')||name.includes('..')||name.includes('Falstaff')||name.includes('config-stub')));
 const meta=JSON.parse(fs.readFileSync(path.join(TMP,'compile-one/metafile.json')));assert.equal(Object.keys(meta.inputs).length,341);assert.ok(!JSON.stringify(meta).includes('config-stub'));
});

test('frozen Mermaid browser targets reproduce exact mapped CSS from preferred source',async()=>{
 const inventory=JSON.parse(fs.readFileSync(path.join(ROOT,'ui-sources.json'))),css=inventory.css;
 const saved=process.env.BROWSERSLIST;process.env.BROWSERSLIST=JSON.parse(fs.readFileSync(path.join(ROOT,css.targets))).join(',');
 try{const postcss=require(path.join(MODULES,'postcss')),cssnano=require(path.join(MODULES,'cssnano'));const output=await postcss([cssnano()]).process(fs.readFileSync(path.join(ROOT,css.preferred),'utf8'),{from:undefined});assert.equal(sha(output.css),css.sha256);assert.equal(output.css,fs.readFileSync(path.join(ROOT,css.minified),'utf8'));}finally{if(saved===undefined)delete process.env.BROWSERSLIST;else process.env.BROWSERSLIST=saved;}
});

test('compiler preflight rejects corrupt sources, dependencies, locks and unsafe inventory before writes',()=>{
 const own=path.join(TMP,'failure-root');fs.cpSync(ROOT,own,{recursive:true,filter:p=>!p.includes('/fixtures/')&&!p.includes('/ui-dist/')});
 const inventoryPath=path.join(own,'ui-sources.json'),inventory=fs.readFileSync(inventoryPath),data=JSON.parse(inventory);
 const fail=()=>{const out=path.join(TMP,'must-not-exist');assert.throws(()=>compile({root:own,modules:MODULES,output:out}));assert.ok(!fs.existsSync(out));};
 const original=fs.readFileSync(path.join(own,TEMPLATE));fs.appendFileSync(path.join(own,TEMPLATE),'corrupt');fail();fs.writeFileSync(path.join(own,TEMPLATE),original);
 for(const key of ['files','dependencies']){const d=JSON.parse(inventory);d[key][0].path='../outside';fs.writeFileSync(inventoryPath,JSON.stringify(d));fail();}
 let d=JSON.parse(inventory);d.dependencies[0].sha256='bad';fs.writeFileSync(inventoryPath,JSON.stringify(d));fail();
 d=JSON.parse(inventory);d.packages.tslib.version='2.9.1';fs.writeFileSync(inventoryPath,JSON.stringify(d));fail();fs.writeFileSync(inventoryPath,inventory);
 assert.throws(()=>compile({root:own,compiler:{version:'wrong'},output:path.join(TMP,'wrong-compiler')}),/Pinned/);
 const real=esbuild.buildSync;const compiler={version:'0.25.12',buildSync(options){const result=real(options);result.outputFiles=result.outputFiles.filter(f=>!f.path.endsWith('.map'));return result;}};
 assert.throws(()=>compile({compiler,output:path.join(TMP,'missing-map')}),/outputs/);
 for(const problem of ['mappings','sourcesContent','source-path','source-content','runtime-import','extra-entrypoint','outside-input','unresolved-edge','trailer']){
  const corrupt={version:'0.25.12',buildSync(options){const result=real(options),map=result.outputFiles.find(f=>f.path.endsWith('.map')),js=result.outputFiles.find(f=>f.path.endsWith('.js'));let mapping=JSON.parse(map.text);
   if(problem==='mappings')mapping.mappings='';
   if(problem==='sourcesContent')delete mapping.sourcesContent;
   if(problem==='source-path')mapping.sources[0]='/unowned/source.ts';
   if(problem==='source-content')mapping.sourcesContent[0]+='wrong';
   if(['mappings','sourcesContent','source-path','source-content'].includes(problem)){result.outputFiles=result.outputFiles.map(f=>f===map?{path:f.path,contents:Buffer.from(JSON.stringify(mapping)),text:JSON.stringify(mapping)}:f);}
   if(problem==='runtime-import')Object.values(result.metafile.outputs)[0].imports.push({path:'external.js',kind:'import-statement',external:true});
   if(problem==='extra-entrypoint')Object.values(result.metafile.outputs)[0].entryPoint='extra.ts';
   if(problem==='outside-input')result.metafile.inputs['/unowned/source.ts']={bytes:0,imports:[]};
   if(problem==='unresolved-edge')Object.values(result.metafile.inputs)[0].imports.push({path:'missing.ts',kind:'import-statement',external:false});
   if(problem==='trailer')result.outputFiles=result.outputFiles.map(f=>f===js?{path:f.path,contents:Buffer.from(js.text+'wrong'),text:js.text+'wrong'}:f);
   return result;
  }};
  assert.throws(()=>compile({compiler:corrupt,output:path.join(TMP,'corrupt-'+problem)}),undefined,problem);
  assert.ok(!fs.existsSync(path.join(TMP,'corrupt-'+problem)));
 }

});

// The entire preferred module is compiled here; only its component dependencies are unit doubles.
async function contentModule(original=false){
 const filename=original?CONTENT.replace('ui/src/templates/assets/javascripts/','ui/provenance/upstream-javascripts/'):CONTENT,instrumented=[];
 const plugins=[{name:'content-unit-dependencies',setup(build){
  build.onResolve({filter:/^rxjs$/},()=>({path:path.join(MODULES,'rxjs'),external:true}));
  build.onResolve({filter:/^(~\/|\.\.\/)/},args=>({path:args.path,namespace:'content-double'}));
  build.onLoad({filter:/.*/,namespace:'content-double'},()=>({contents:[
   'export const feature=name=>globalThis.contentTest.features.includes(name);',
   'export const getElements=(selector,el)=>globalThis.contentTest.getElements(selector,el);',
   'export const renderTooltip2=(...nodes)=>globalThis.contentTest.renderTooltip2(nodes);',
   ...['mountAnnotationBlock','mountCodeBlock','mountLink','mountMermaid','mountDataTable','mountDetails','mountContentTabs','mountInlineTooltip2','mountTooltip2'].map(name=>`export const ${name}=(...args)=>globalThis.contentTest.factory("${name}",...args);`)
  ].join('\n'),loader:'js'}));
  if(!original&&process.env.ARCHIVE_UI_COVERAGE)build.onLoad({filter:/components\/content\/_\/index\.ts$/},args=>{
   const source=fs.readFileSync(args.path,'utf8'),instrumenter=require(path.join(MODULES,'istanbul-lib-instrument')).createInstrumenter({parserPlugins:['typescript'],esModules:true,produceSourceMap:true});
   const contents=instrumenter.instrumentSync(source,args.path);instrumented.push({path:CONTENT,sha256:sha(source),map:instrumenter.lastSourceMap()});return{contents,loader:'ts'};
  });
 }}];
 const result=await esbuild.build({absWorkingDir:ROOT,entryPoints:[filename],outfile:path.join(TMP,'content-unit.cjs'),tsconfig:path.join(ROOT,'ui/tsconfig.json'),bundle:true,format:'cjs',platform:'node',target:'es2015',write:false,plugins});
 const context={require,URL,module:{exports:{}},contentTest:null};context.exports=context.module.exports;
 require('node:vm').runInNewContext(result.outputFiles[0].text,context,{filename:'whole-content-unit.cjs'});
 return{mount:context.module.exports.mountContent,context,instrumented};
}
const selectors=['.annotate:not(.highlight)','pre:not(.mermaid) > code','a','pre.mermaid','table:not([class])','details','[data-tabs]','[title]:not([data-preview])','.footnote-ref'];
const factories=['mountAnnotationBlock','mountCodeBlock','mountLink','mountMermaid','mountDataTable','mountDetails','mountContentTabs','mountInlineTooltip2','mountTooltip2'];
const rxjs=require(path.join(MODULES,'rxjs'));
function contentState(runtime,groups={},features=[]){
 const state={features,calls:[],selected:[],el:{article:true},dependencies:{sitemap$:rxjs.EMPTY,viewport$:rxjs.EMPTY,target$:rxjs.EMPTY,print$:rxjs.EMPTY},
  getElements(selector,el){assert.equal(el,state.el);state.selected.push(selector);return groups[selector]||[];},
  factory(name,child,options){state.calls.push({name,child,options});return child.stream||rxjs.EMPTY;},
  renderTooltip2(){throw Error('Unexpected tooltip rendering');}};
 runtime.context.contentTest=state;return state;
}

test('whole content initializer handles source-bound 140171 article anchors without a function-argument overflow',async()=>{
 const html=cp.execFileSync('tar',['-xOf',path.join(SITE,'archive/fontlab7-site.tar.gz'),'pythonqt/PythonQt.QtGui.html'],{maxBuffer:80*1024*1024}).toString();
 const article=html.match(/<article\b[\s\S]*?<\/article>/)[0],count=[...article.matchAll(/<a\b/g)].length;assert.equal(count,140171);
 const runtime=await contentModule(!!process.env.ARCHIVE_CONTENT_RED);if(!process.env.ARCHIVE_CONTENT_RED)contentRuntime=runtime;
 let subscribed=0,completed=0,cleaned=0,next=0;const stream=new rxjs.Observable(observer=>{subscribed++;observer.next('link');observer.complete();return()=>cleaned++;});
 const state=contentState(runtime,{a:Array.from({length:count},(_,id)=>({id,stream}))});
 const observable=runtime.mount(state.el,state.dependencies);observable.subscribe({next:value=>{assert.equal(value,'link');next++;},complete:()=>completed++});
 assert.equal(state.calls.length,count);assert.deepEqual(state.selected,selectors);assert.ok(state.calls.every((call,i)=>call.name==='mountLink'&&call.child.id===i&&call.options===state.dependencies));
 assert.deepEqual({subscribed,next,completed,cleaned},{subscribed:count,next:count,completed:1,cleaned:count});
 fs.writeFileSync(path.join(TMP,'whole-content-large-proof.json'),JSON.stringify({whole_module:CONTENT,source_sha256:sha(fs.readFileSync(path.join(ROOT,CONTENT))),article_sha256:sha(article),lexical_article_anchors:count,subscribed,next,completed,cleaned},null,2));
});

test('whole original content module reproduces the bound large argument RangeError',async()=>{
 const runtime=await contentModule(true),state=contentState(runtime,{a:Array.from({length:140171},()=>({stream:rxjs.EMPTY}))});
 assert.throws(()=>runtime.mount(state.el,state.dependencies),/Maximum call stack size exceeded/);assert.equal(state.calls.length,140171);
});

test('whole content module preserves zero/one identities and synchronous completion before cleanup',async()=>{
 const runtime=contentRuntime||await contentModule();contentRuntime=runtime;
 let state=contentState(runtime);assert.equal(runtime.mount(state.el,state.dependencies),rxjs.EMPTY);
 const trace=[],stream=new rxjs.Observable(observer=>{trace.push('subscribe');observer.next('one');observer.complete();return()=>trace.push('cleanup');});
 state=contentState(runtime,{a:[{stream}]});const actual=runtime.mount(state.el,state.dependencies);assert.equal(actual,stream);
 actual.subscribe({next:value=>trace.push('next:'+value),complete:()=>trace.push('complete')});assert.deepEqual(trace,['subscribe','next:one','complete','cleanup']);
});

test('whole content module preserves every selector, feature, factory order and dependency',async()=>{
 const runtime=contentRuntime||await contentModule();contentRuntime=runtime;
 for(const features of [[],['content.tooltips','content.footnote.tooltips']]){
  const groups=Object.fromEntries(selectors.map((selector,id)=>[selector,[{id}]])),state=contentState(runtime,groups,features);
  runtime.mount(state.el,state.dependencies).subscribe();assert.deepEqual(state.selected,selectors);
  const count=features.length?9:7;assert.deepEqual(state.calls.map(call=>call.name),factories.slice(0,count));
  for(const [i,call] of state.calls.entries()){
   assert.equal(call.child,groups[selectors[i]][0]);const options=call.options;
   if(i===2)assert.equal(options,state.dependencies);
   else if([0,1,5].includes(i)){assert.deepEqual(Object.keys(options),['target$','print$']);assert.equal(options.target$,state.dependencies.target$);assert.equal(options.print$,state.dependencies.print$);}
   else if(i===6){assert.deepEqual(Object.keys(options),['viewport$','target$']);assert.equal(options.viewport$,state.dependencies.viewport$);assert.equal(options.target$,state.dependencies.target$);}
   else if(i===7){assert.deepEqual(Object.keys(options),['viewport$']);assert.equal(options.viewport$,state.dependencies.viewport$);}
   else if(i===8){assert.deepEqual(Object.keys(options),['content$','viewport$']);assert.equal(options.viewport$,state.dependencies.viewport$);assert.ok(options.content$ instanceof rxjs.Observable);}
   else assert.equal(options,undefined);
  }
 }
});

test('whole content module retains multi-source sync/async/error/completion and unsubscribe ordering',async()=>{
 const runtime=contentRuntime||await contentModule();contentRuntime=runtime;
 async function scenario(mount,kind){
  const trace=[],observers=[];let subscription;
  const sources=['a','b'].map(name=>new rxjs.Observable(observer=>{trace.push('subscribe:'+name);observers.push(observer);if(kind==='sync'){observer.next(name);observer.complete();}if(kind==='error'&&name==='a')observer.error(Error('same failure'));return()=>trace.push('cleanup:'+name);}));
  const stream=mount(sources);subscription=stream.subscribe({next:value=>trace.push('next:'+value),error:error=>trace.push('error:'+error.message),complete:()=>trace.push('complete')});
  if(kind==='async'){await new Promise(resolve=>setImmediate(resolve));observers[1].next('b');observers[0].next('a');observers[0].complete();assert.ok(!trace.includes('complete'));observers[1].complete();}
  if(kind==='cancel'){observers[0].next('a');subscription.unsubscribe();observers[1].next('late');observers[1].complete();}
  return trace;
 }
 for(const kind of ['sync','async','error','cancel']){
  const expected=await scenario(sources=>rxjs.merge(...sources),kind),actual=await scenario(sources=>{const state=contentState(runtime,{a:sources.map(stream=>({stream}))});return runtime.mount(state.el,state.dependencies);},kind);assert.deepEqual(actual,expected,kind);
 }
 const failure=Error('factory failure'),state=contentState(runtime,{a:[{}]});state.factory=()=>{throw failure;};assert.throws(()=>runtime.mount(state.el,state.dependencies),error=>error===failure);
});

test('whole content footnote callback preserves node construction, next/append order and disposal',async()=>{
 const runtime=contentRuntime||await contentModule();contentRuntime=runtime;const trace=[],children=[{id:1},{id:2}],node={remove(){trace.push('remove');}},footnote={href:'https://example.test/page.html#note'};
 const state=contentState(runtime,{'.footnote-ref':[footnote]},['content.footnote.tooltips']);
 runtime.context.document={getElementById(id){assert.equal(id,'note');return{cloneNode(deep){assert.equal(deep,true);return{children};}};},body:{append(value){assert.equal(value,node);trace.push('append');}}};
 state.renderTooltip2=nodes=>{assert.equal(nodes.length,children.length);assert.ok(nodes.every((node,i)=>node===children[i]));trace.push('render');return node;};
 runtime.mount(state.el,state.dependencies);const content=state.calls[0].options.content$;
 const subscription=content.subscribe({next:value=>{assert.equal(value,node);trace.push('next');}});assert.deepEqual(trace,['render','next','append']);subscription.unsubscribe();assert.deepEqual(trace,['render','next','append','remove']);
 runtime.context.document.getElementById=()=>null;let error;content.subscribe({error:value=>error=value});assert.match(error.message,/cloneNode/);assert.equal(trace.filter(x=>x==='remove').length,1);
});

// Compile the entire real visibility module; only its separate browser measurements are controlled.
async function visibilityModule(original=false){
 if(visibilityCompiled.has(original))return visibilityCompiled.get(original);
 const filename=original?VISIBILITY.replace('ui/src/templates/assets/javascripts/','ui/provenance/upstream-javascripts/'):VISIBILITY,instrumented=[];
 const result=await esbuild.build({absWorkingDir:ROOT,entryPoints:[filename],outfile:path.join(TMP,'whole-visibility.cjs'),tsconfig:path.join(ROOT,'ui/tsconfig.json'),bundle:true,format:'cjs',platform:'node',target:'es2015',treeShaking:false,sourcemap:'external',sourcesContent:true,write:false,plugins:[{name:'visibility-browser-measurements',setup(build){
  build.onResolve({filter:/^rxjs$/},()=>({path:path.join(MODULES,'rxjs'),external:true}));
  build.onResolve({filter:/^~\/browser$/},()=>({path:'boundary-measurements',namespace:'visibility-unit'}));
  build.onLoad({filter:/.*/,namespace:'visibility-unit'},()=>({contents:['getElementContentSize','getElementSize','watchElementContentOffset'].map(name=>`export const ${name}=(...args)=>globalThis.visibilityTest.boundary.${name}(...args);`).join('\n'),loader:'js'}));
  if(!original&&process.env.ARCHIVE_UI_COVERAGE)build.onLoad({filter:/element\/visibility\/index\.ts$/},args=>{
   const source=fs.readFileSync(args.path,'utf8'),instrumenter=require(path.join(MODULES,'istanbul-lib-instrument')).createInstrumenter({parserPlugins:['typescript'],esModules:true,produceSourceMap:true});
   const contents=instrumenter.instrumentSync(source,args.path);instrumented.push({path:VISIBILITY,sha256:sha(source),map:instrumenter.lastSourceMap()});return{contents,loader:'ts'};
  });
 }}]});
 const value={code:result.outputFiles.find(file=>file.path.endsWith('.cjs')).text,instrumented,source:fs.readFileSync(path.join(ROOT,filename),'utf8')};
 const mapping=JSON.parse(result.outputFiles.find(file=>file.path.endsWith('.map')).text);assert.ok(mapping.sources.some(name=>name.endsWith('/element/visibility/index.ts')));
 if(!process.env.ARCHIVE_UI_COVERAGE||original)assert.ok(mapping.sourcesContent.includes(value.source));
 visibilityCompiled.set(original,value);return value;
}
async function visibilityRuntime(original=false,failure={}){
 const compiled=await visibilityModule(original),events=[],observers=[],subscriptions=[],maps=[],channels=[],channelSeen=new Set();let reads=0,attempts=0,mapGets=0,scans=0;
 class TargetMap extends Map{
  constructor(...args){super(...args);maps.push(this);}
  get(key){mapGets++;return super.get(key);}
  set(key,value){if(!channelSeen.has(value)){channelSeen.add(value);channels.push(value);}return super.set(key,value);}
  entries(){scans++;return super.entries();}keys(){scans++;return super.keys();}values(){scans++;return super.values();}
  forEach(...args){scans++;return super.forEach(...args);}[Symbol.iterator](){scans++;return super[Symbol.iterator]();}
 }
 class Observer{
  constructor(callback,options){attempts++;events.push(['construct',options.threshold]);if(failure.construct){failure.construct--;throw Error('controlled construct failure');}this.callback=callback;this.observed=new Set();observers.push(this);}
  observe(el){events.push(['observe',el.id]);if(failure.observe===el.id)throw Error('controlled observe failure');this.observed.add(el);if(failure.onObserve)failure.onObserve(el);}
  unobserve(el){events.push(['unobserve',el.id]);if(failure.onUnobserve)failure.onUnobserve(el);if(failure.unobserve===el.id)throw Error('controlled unobserve failure');this.observed.delete(el);}
  disconnect(){events.push(['disconnect']);this.observed.clear();}
 }
 const context={require,module:{exports:{}},IntersectionObserver:Observer,Map:TargetMap,visibilityTest:{boundary:{}}};context.exports=context.module.exports;
 require('node:vm').runInNewContext(compiled.code,context,{filename:'whole-visibility.cjs'});if(!original)visibilityContexts.push(context);
 const api=context.module.exports;assert.deepEqual(Object.keys(api).sort(),['watchElementBoundary','watchElementVisibility']);
 const entry=(el,value)=>({get target(){reads++;return el;},isIntersecting:value});
 const emit=entries=>{assert.equal(observers.length,1);observers[0].callback(entries);};
 const subscribe=(el,label,hook)=>{const sub=api.watchElementVisibility(el).subscribe({next:value=>{events.push(['next',label,value]);if(hook)hook(value);},error:error=>events.push(['error',label,error.name,error.message]),complete:()=>events.push(['complete',label])});subscriptions.push(sub);return sub;};
 return{api,context,events,observers,subscriptions,maps,channels,entry,emit,subscribe,get reads(){return reads;},get attempts(){return attempts;},get mapGets(){return mapGets;},get scans(){return scans;}};
}

async function visibilityScenarios(original){
 const scenarios=[];let active;
 const runtime=async failure=>active=await visibilityRuntime(original,failure);
 const record=(name,value)=>scenarios.push({name,...value,closed_subscriptions:active.subscriptions.map(sub=>sub.closed),observed_targets:active.observers.map(observer=>[...observer.observed].map(el=>el.id))});
 {const r=await runtime();assert.equal(r.observers.length,0);record('zero_subscriptions',{observers:0,events:r.events});}
 for(const n of [1,2,64,128]){
  const r=await runtime(),els=Array.from({length:n},(_,i)=>({id:'e'+i})),subs=els.map(el=>r.subscribe(el,el.id));
  r.emit([]);assert.equal(r.reads,0);assert.equal(r.events.filter(e=>e[0]==='next').length,0);
  r.emit(els.map(el=>r.entry(el,false)));assert.equal(r.reads,original?n*n:n);assert.deepEqual(r.events.filter(e=>e[0]==='next'),els.map(el=>['next',el.id,false]));
  for(const sub of subs)sub.unsubscribe();assert.equal(r.events.filter(e=>e[0]==='unobserve').length,n);assert.equal(r.events.filter(e=>e[0]==='disconnect').length,0);
  record('false_batch_'+n,{n,target_reads:r.reads,expected:original?n*n:n,empty_batch_reads:0,events:r.events});
 }
 {const r=await runtime(),a={id:'a'},b={id:'b'},sa=r.subscribe(a,'a'),sb=r.subscribe(b,'b');
  r.emit([r.entry(a,false),r.entry(b,true),r.entry(a,true),r.entry(a,false)]);
  assert.deepEqual(r.events.filter(e=>e[0]==='next'),[['next','a',false],['next','b',true],['next','a',true],['next','a',false]]);
  sa.unsubscribe();sb.unsubscribe();assert.equal(r.reads,original?8:4);record('ordered_true_false',{target_reads:r.reads,events:r.events});
 }
 {const r=await runtime(),a={id:'a'},s1=r.subscribe(a,'first'),s2=r.subscribe(a,'second');r.emit([r.entry(a,false)]);s1.unsubscribe();
  assert.equal(r.observers[0].observed.has(a),false);r.emit([r.entry(a,true)]);s2.unsubscribe();
  assert.deepEqual(r.events.filter(e=>e[0]==='next'),[['next','first',false],['next','second',false],['next','second',true]]);
  assert.equal(r.reads,original?3:2);record('duplicate_subscriptions_queued_delivery',{note:'Second callback explicitly represents an already-queued entry, not a claim that native observer schedules after unobserve',target_reads:r.reads,events:r.events});
 }
 {const r=await runtime(),a={id:'a'},b={id:'b'};let sa,sb;sa=r.subscribe(a,'a',()=>{sb.unsubscribe();sa.unsubscribe();});sb=r.subscribe(b,'b');
  r.emit([r.entry(a,true),r.entry(b,false)]);assert.deepEqual(r.events.filter(e=>e[0]==='next'),[['next','a',true]]);assert.equal(r.reads,original?1:2);record('unsubscribe_during_delivery',{target_reads:r.reads,events:r.events});
 }
 {const r=await runtime(),a={id:'a'},b={id:'b'},sa=r.subscribe(a,'a');r.emit([r.entry(a,true)]);const sb=r.subscribe(b,'late-b');
  assert.deepEqual(r.events.filter(e=>e[0]==='next'),[['next','a',true]]);r.emit([r.entry(b,false)]);sa.unsubscribe();sb.unsubscribe();const before=r.events.length,sa2=r.subscribe(a,'again-a');
  assert.equal(r.observers.length,1);assert.ok(!r.events.slice(before).some(e=>e[0]==='next'));r.emit([r.entry(a,false)]);sa2.unsubscribe();assert.equal(r.events.filter(e=>e[0]==='disconnect').length,0);
  record('late_and_resubscribe',{target_reads:r.reads,observer_instances:r.observers.length,events:r.events});
 }
 {const r=await runtime(),a={id:'a'},b={id:'b'};let late;const sa=r.subscribe(a,'a',()=>{late=r.subscribe(b,'late-b');});r.emit([r.entry(a,true),r.entry(b,false)]);sa.unsubscribe();late.unsubscribe();
  assert.deepEqual(r.events.filter(e=>e[0]==='next'),[['next','a',true],['next','late-b',false]]);record('subscribe_during_batch',{target_reads:r.reads,events:r.events});
 }
 {const r=await runtime(),a={id:'a'},b={id:'b'};let nested=false;const sa=r.subscribe(a,'a-first',()=>{if(!nested){nested=true;r.emit([r.entry(b,false)]);}}),sa2=r.subscribe(a,'a-second'),sb=r.subscribe(b,'b');
  r.emit([r.entry(a,true)]);assert.deepEqual(r.events.filter(e=>e[0]==='next'),[['next','a-first',true],['next','b',false],['next','a-second',true]]);assert.equal(r.reads,original?6:2);sa.unsubscribe();sa2.unsubscribe();sb.unsubscribe();record('reentrant_callback',{target_reads:r.reads,events:r.events});
 }
 {const r=await runtime({construct:1}),a={id:'a'};const first=r.subscribe(a,'failed'),next=r.subscribe(a,'retry');assert.equal(first.closed,true);assert.equal(r.attempts,2);assert.equal(r.observers.length,1);r.emit([r.entry(a,false)]);next.unsubscribe();assert.equal(r.events.filter(e=>e[0]==='error').length,1);record('constructor_error_then_retry',{attempts:r.attempts,events:r.events});}
 {const r=await runtime({observe:'bad'}),bad={id:'bad'},good={id:'good'};const failed=r.subscribe(bad,'bad'),next=r.subscribe(good,'good');assert.equal(failed.closed,true);r.emit([r.entry(good,true)]);next.unsubscribe();assert.ok(!r.events.some(e=>e[0]==='unobserve'&&e[1]==='bad'));record('observe_error_then_other_target',{events:r.events});}
 {const r=await runtime({unobserve:'bad'}),bad={id:'bad'},sub=r.subscribe(bad,'bad');let caught;try{sub.unsubscribe();}catch(error){caught={name:error.name,message:error.message,errors:error.errors.map(e=>({name:e.name,message:e.message}))};}assert.equal(caught.name,'UnsubscriptionError');assert.equal(caught.errors[0].message,'controlled unobserve failure');assert.equal(sub.closed,true);record('unobserve_error',{caught,events:r.events});}
 assert.equal(scenarios.length,14);return scenarios;
}

test('whole visibility dispatch work is linear in entries plus matching deliveries',async()=>{
 const rows=[];
 for(const n of [128,1,2,64]){
  const r=await visibilityRuntime(!!process.env.ARCHIVE_VISIBILITY_RED),elements=Array.from({length:n},(_,i)=>({id:'e'+i})),subs=elements.map(el=>r.subscribe(el,el.id));
  const beforeGets=r.mapGets,beforeReads=r.reads;r.emit(elements.map(el=>r.entry(el,false)));const targetReads=r.reads-beforeReads,mapGets=r.mapGets-beforeGets,delivered=r.events.filter(event=>event[0]==='next').length,work=targetReads+mapGets+delivered;
  assert.ok(work<=3*n,`${n} entries: actual target reads+map lookups+deliveries=${work}; expected <=${3*n}`);
  assert.equal(targetReads,n);assert.equal(mapGets,n);assert.equal(delivered,n);assert.equal(r.scans,0);rows.push({n,target_reads:targetReads,map_gets:mapGets,deliveries:delivered,global_map_scans:r.scans,work});
  subs.forEach(sub=>sub.unsubscribe());assert.equal(r.maps[0].size,0);
 }
 fs.writeFileSync(path.join(TMP,'visibility-linear-work.json'),JSON.stringify(rows,null,2));
});

test('whole visibility module preserves all fourteen original value lifecycle and error scenarios',async()=>{
 const old=await visibilityScenarios(true),current=await visibilityScenarios(false);
 const values=row=>{const{target_reads,expected,...unchanged}=row;return unchanged;};
 assert.deepEqual(current.map(values),old.map(values));
 fs.writeFileSync(path.join(TMP,'visibility-fourteen-scenarios.json'),JSON.stringify({old,current},null,2));
});

test('whole visibility module preserves unknown repeated same-target late-reentrant and returned-observable reuse',async()=>{
 async function scenario(original){
  const r=await visibilityRuntime(original),a={id:'a'},unknown={id:'unknown'};let late,nested=false;
  const observable=r.api.watchElementVisibility(a),first=observable.subscribe(value=>{r.events.push(['first',value]);if(!nested){nested=true;late=r.subscribe(a,'late');r.emit([r.entry(a,false)]);}});
  r.emit([r.entry(unknown,true),r.entry(a,true),r.entry(a,true)]);first.unsubscribe();late.unsubscribe();
  const again=observable.subscribe(value=>r.events.push(['again',value]));r.emit([r.entry(a,false)]);again.unsubscribe();
  if(!original)assert.equal(r.maps[0].size,0);return{events:r.events,closed:[first.closed,late.closed,again.closed],observers:r.observers.length};
 }
 assert.deepEqual(await scenario(false),await scenario(true));
});

test('whole visibility observes before subscription and releases bookkeeping even on unobserve error',async()=>{
 for(const original of [true,false]){
  let r;const a={id:'a'},failure={onObserve:()=>{if(r)r.emit([r.entry(a,true)]);}};r=await visibilityRuntime(original,failure);
  const sub=r.subscribe(a,'a');assert.ok(!r.events.some(event=>event[0]==='next'));r.emit([r.entry(a,false)]);sub.unsubscribe();if(!original)assert.equal(r.maps[0].size,0);
  const bad=await visibilityRuntime(original,{unobserve:'a'}),s=bad.subscribe(a,'bad');assert.throws(()=>s.unsubscribe(),error=>error.name==='UnsubscriptionError'&&error.errors[0].message==='controlled unobserve failure');assert.equal(s.closed,true);if(!original){assert.equal(bad.maps[0].size,0);assert.equal(bad.channels[0].observed,false);}
 }
});

test('whole visibility nested teardown cannot remove a newer same-target channel',async()=>{
 async function scenario(original){
  let r,b,c,nested=false;const a={id:'a'},failure={onUnobserve:()=>{if(!nested){nested=true;b.unsubscribe();c=r.subscribe(a,'C');}}};r=await visibilityRuntime(original,failure);
  const first=r.subscribe(a,'A');b=r.subscribe(a,'B');first.unsubscribe();r.emit([r.entry(a,true)]);
  assert.deepEqual(r.events.filter(event=>event[0]==='next'),[['next','C',true]]);if(!original){assert.equal(r.maps[0].size,1);assert.equal(r.channels.length,2);}
  c.unsubscribe();if(!original)assert.equal(r.maps[0].size,0);return{events:r.events,closed:[first.closed,b.closed,c.closed]};
 }
 assert.deepEqual(await scenario(false),await scenario(true));
});

test('whole visibility retains take1 done completion closed subscriptions and async consumer errors',async()=>{
 async function scenario(original){
  const r=await visibilityRuntime(original),a={id:'a'},done=new rxjs.Subject(),events=[],previous=rxjs.config.onUnhandledError;
  try{
   rxjs.config.onUnhandledError=error=>events.push(['reported',error.message]);
   const first=r.api.watchElementVisibility(a).pipe(rxjs.filter(Boolean),rxjs.take(1)).subscribe({next:value=>events.push(['first',value]),complete:()=>events.push(['first-complete'])});
   const until=r.api.watchElementVisibility(a).pipe(rxjs.takeUntil(done)).subscribe({next:value=>events.push(['until',value]),complete:()=>events.push(['until-complete'])});
   const bad=r.api.watchElementVisibility(a).subscribe(()=>{throw Error('consumer failure');});
   r.emit([r.entry(a,false),r.entry(a,true)]);done.next(true);assert.equal(first.closed,true);assert.equal(until.closed,true);assert.equal(bad.closed,false);
   await new Promise(resolve=>setTimeout(resolve,0));bad.unsubscribe();const closed=new rxjs.Subscriber();closed.unsubscribe();r.api.watchElementVisibility(a).subscribe(closed);
   if(!original)assert.equal(r.maps[0].size,0);return{events,observer:r.events,closed:[first.closed,until.closed,bad.closed]};
  }finally{rxjs.config.onUnhandledError=previous;}
 }
 assert.deepEqual(await scenario(false),await scenario(true));
});

test('whole visibility boundary export retains thresholds distinct values errors and completion',async()=>{
 const r=await visibilityRuntime(),el={id:'boundary'},offsets=new rxjs.Subject(),values=[];
 r.context.visibilityTest.boundary={watchElementContentOffset:target=>{assert.equal(target,el);return offsets;},getElementSize:target=>{assert.equal(target,el);return{height:20};},getElementContentSize:target=>{assert.equal(target,el);return{height:100};}};
 const sub=r.api.watchElementBoundary(el).subscribe({next:value=>values.push(value),complete:()=>values.push('complete')});
 for(const y of [0,63,64,65,0])offsets.next({y});offsets.complete();assert.deepEqual(values,[false,true,false,'complete']);assert.equal(sub.closed,true);
 const errors=new rxjs.Subject();r.context.visibilityTest.boundary.watchElementContentOffset=()=>errors;let caught;r.api.watchElementBoundary(el,0).subscribe({error:error=>caught=error});const failure=Error('offset failure');errors.error(failure);assert.equal(caught,failure);assert.equal(r.maps[0].size,0);
});

// Use exact AST slices from the four unchanged callers, never copied visibility pipelines.
const callerBindings=[];
async function callerPipeline(relative,name,mode,runtime,state){
 const source=fs.readFileSync(path.join(ROOT,'ui/src/templates/assets/javascripts',relative),'utf8'),parser=require(path.join(MODULES,'@babel/parser'));
 const ast=parser.parse(source,{sourceType:'module',plugins:['typescript']}),nodes=[];
 function visit(value){if(!value||typeof value!=='object')return;if(Array.isArray(value)){value.forEach(visit);return;}if(value.type)nodes.push(value);Object.values(value).forEach(visit);}
 visit(ast);const fn=nodes.find(node=>node.type==='FunctionDeclaration'&&node.id.name===name);assert.ok(fn);
 const text=node=>source.slice(node.start,node.end),rxImport=ast.program.body.find(node=>node.type==='ImportDeclaration'&&node.source.value==='rxjs');let contents=source,selected=[{start:0,end:source.length}];
 if(mode!=='ellipsis'){
  const body=fn.body.body,inner=nodes.find(node=>node.type==='ArrowFunctionExpression'&&node.body.type==='BlockStatement'&&text(node).includes('const push$')&&node.start>fn.start&&node.end<fn.end);
  if(mode==='code'){
   const branch=body.find(node=>node.type==='IfStatement'&&text(node.test).includes('content.lazy')),fallback=body.at(-1);assert.ok(branch&&fallback.type==='ReturnStatement');selected=[branch,fallback];
   contents=text(rxImport)+'\nconst feature=globalThis.callerTest.feature;const watchElementVisibility=globalThis.callerTest.watchElementVisibility;export function run(el,factory$){'+selected.map(text).join('\n')+'}';
  }else{
   assert.ok(inner);const statements=inner.body.body,push=statements.find(node=>node.type==='VariableDeclaration'&&node.declarations[0].id.name==='push$'),done=statements.find(node=>node.type==='VariableDeclaration'&&node.declarations[0].id.name==='done$'),pipeline=statements.find(node=>node.type==='ExpressionStatement'&&text(node).includes('watchElementVisibility('));assert.ok(push&&done&&pipeline);selected=[push,done,pipeline];
   contents=text(rxImport)+'\nconst {watchElementVisibility,watchElementSize,getElementOffset,getElementSize,getElementContentOffset}=globalThis.callerTest;export function run(el,container){'+selected.map(text).join('\n')+';return push$;}';
  }
 }
 callerBindings.push({path:relative,sha256:sha(source),mode,slices:selected.map(node=>({start:node.start,end:node.end,sha256:sha(source.slice(node.start,node.end))}))});
 const result=await esbuild.build({absWorkingDir:ROOT,stdin:{contents,loader:'ts',resolveDir:ROOT,sourcefile:relative},outfile:path.join(TMP,'caller-unit.cjs'),tsconfig:path.join(ROOT,'ui/tsconfig.json'),bundle:true,format:'cjs',platform:'node',target:'es2015',write:false,plugins:[{name:'caller-controlled-dependencies',setup(build){
  build.onResolve({filter:/^rxjs$/},()=>({path:path.join(MODULES,'rxjs'),external:true}));build.onResolve({filter:/^~\//},args=>({path:args.path,namespace:'caller-unit'}));
  build.onLoad({filter:/.*/,namespace:'caller-unit'},()=>({contents:['feature','getElements','watchElementVisibility','mountInlineTooltip2'].map(name=>`export const ${name}=(...args)=>globalThis.callerTest.${name}(...args);`).join('\n'),loader:'js'}));
 }}]});
 const context={require,module:{exports:{}},callerTest:{...state,watchElementVisibility:runtime.api.watchElementVisibility}};context.exports=context.module.exports;
 require('node:vm').runInNewContext(result.outputFiles[0].text,context,{filename:'actual-caller-pipeline.cjs'});return context.module.exports;
}

test('actual source ellipsis pipeline waits for first true cancels on document and retains optional tooltip cleanup',async()=>{
 async function scenario(original,tooltips){
  const r=await visibilityRuntime(original),events=[],document$=new rxjs.ReplaySubject(1),viewport$=rxjs.NEVER,host={id:'host',removeAttribute(name){events.push(['remove',name]);delete this[name];}},visible={id:'visible',offsetWidth:1,scrollWidth:2,innerText:'Caption',closest:()=>host},pending={id:'pending'};let elements=[visible,pending];
  const state={feature:name=>tooltips&&name==='content.tooltips',getElements:selector=>selector==='.md-ellipsis'?elements:[],mountInlineTooltip2:(el,dependencies)=>{assert.equal(el,host);assert.equal(dependencies.viewport$,viewport$);return new rxjs.Observable(()=>{events.push(['tooltip']);return()=>events.push(['tooltip-cleanup']);});}};
  const api=await callerPipeline('patches/ellipsis/index.ts','patchEllipsis','ellipsis',r,state);document$.next('first');api.patchEllipsis({document$,viewport$});
  r.emit([r.entry(visible,false),r.entry(pending,false)]);assert.equal(host.title,undefined);r.emit([r.entry(visible,true),r.entry(visible,false)]);assert.equal(host.title,'Caption');
  elements=[];document$.next('second');document$.complete();assert.equal(host.title,tooltips?undefined:'Caption');if(!original)assert.equal(r.maps[0].size,0);
  return{events,observer:r.events,title:host.title??null};
 }
 for(const tooltips of [false,true])assert.deepEqual(await scenario(false,tooltips),await scenario(true,tooltips));
});

test('actual source annotation pipeline toggles every visibility value and retires on real done construction',async()=>{
 async function scenario(original){
  const r=await visibilityRuntime(original),events=[],el={id:'annotation',toggleAttribute:(name,value)=>events.push([name,value])};
  const api=await callerPipeline('components/content/annotation/_/index.ts','mountAnnotation','annotation',r,{}),push=api.run(el,{});
  r.emit([r.entry(el,false),r.entry(el,true),r.entry(el,true)]);push.next({active:false});assert.equal(r.events.filter(event=>event[0]==='unobserve').length,0);push.complete();r.emit([r.entry(el,false)]);
  assert.deepEqual(events,[['data-md-visible',false],['data-md-visible',true],['data-md-visible',true]]);assert.equal(r.events.filter(event=>event[0]==='unobserve').length,1);if(!original)assert.equal(r.maps[0].size,0);return{events,observer:r.events};
 }
 assert.deepEqual(await scenario(false),await scenario(true));
});

test('actual source code lazy branch waits for first true switches factory and preserves ungated identity and cancellation',async()=>{
 async function scenario(original,lazy,cancel){
  const r=await visibilityRuntime(original),el={id:'code'},events=[],factorySource=new rxjs.Subject(),factory=rxjs.defer(()=>{events.push('factory');return factorySource;});
  const api=await callerPipeline('components/content/code/_/index.ts','mountCodeBlock','code',r,{feature:name=>lazy&&name==='content.lazy'}),actual=api.run(el,factory);if(!lazy)assert.equal(actual,factory);
  const sub=actual.subscribe({next:value=>events.push(value),complete:()=>events.push('complete')});
  if(lazy){r.emit([r.entry(el,false)]);assert.deepEqual(events,[]);if(!cancel)r.emit([r.entry(el,true),r.entry(el,false)]);}
  if(cancel)sub.unsubscribe();else{factorySource.next('rendered');factorySource.complete();}
  assert.deepEqual(events,cancel?[]:['factory','rendered','complete']);assert.equal(sub.closed,true);if(!original)assert.equal(r.maps[0].size,0);return{events,observer:r.events};
 }
 for(const [lazy,cancel] of [[false,false],[true,false],[true,true]])assert.deepEqual(await scenario(false,lazy,cancel),await scenario(true,lazy,cancel));
});

test('actual source tabs pipeline waits for all inputs audits state size and visibility and cleans on done',async()=>{
 async function scenario(original){
  const r=await visibilityRuntime(original),events=[],size=new rxjs.Subject(),el={id:'tabs',style:{setProperty:(...args)=>events.push(['set',...args]),removeProperty:name=>events.push(['remove',name])}},container={scrollTo:options=>events.push(['scroll',options.left,options.behavior])};
  const api=await callerPipeline('components/content/tabs/index.ts','mountContentTabs','tabs',r,{watchElementSize:target=>{assert.equal(target,el);return size;},getElementOffset:active=>active.offset,getElementSize:active=>active.size,getElementContentOffset:target=>{assert.equal(target,container);return{x:0};}});
  const scheduler=new (require(path.join(MODULES,'rxjs/testing')).TestScheduler)(()=>{});
  scheduler.run(()=>{
   const push=api.run(el,container);push.next({active:{offset:{x:40},size:{width:10}}});size.next({width:20});assert.deepEqual(events,[]);r.emit([r.entry(el,false)]);assert.deepEqual(events,[]);
   scheduler.schedule(()=>{assert.deepEqual(events,[['set','--md-indicator-x','40px'],['set','--md-indicator-width','10px'],['scroll',24,'smooth']]);push.next({active:{offset:{x:5},size:{width:8}}});size.next({width:100});r.emit([r.entry(el,true)]);},2);
   scheduler.schedule(()=>push.complete(),5);
  });
  assert.deepEqual(events,[['set','--md-indicator-x','40px'],['set','--md-indicator-width','10px'],['scroll',24,'smooth'],['set','--md-indicator-x','5px'],['set','--md-indicator-width','8px'],['remove','--md-indicator-x'],['remove','--md-indicator-width']]);
  assert.equal(r.events.filter(event=>event[0]==='unobserve').length,1);if(!original)assert.equal(r.maps[0].size,0);return{events,observer:r.events};
 }
 assert.deepEqual(await scenario(false),await scenario(true));fs.writeFileSync(path.join(TMP,'four-caller-source-bindings.json'),JSON.stringify(callerBindings,null,2));
});
