// this_file: scripts/search_backend/worker.js
import {fetchChecked,parseJSON,validateManifest,decodeRouting} from "./validation.js";
import {QueryRunner} from "./query.js";
const base=new URL("../../../search/complete/",location.href);
const channelName=new URL(location.href).searchParams.get("channel");
const channel=channelName ? new BroadcastChannel(channelName) : null;
let setupData, runner, setupPromise=Promise.resolve(), queue=Promise.resolve(), generation=0, latest="", ready=false;
let active=new AbortController(), startup=new AbortController();
const state=data=>channel?.postMessage(data);
async function setup(retry=false) {
  ready=false;runner=undefined;startup.abort();startup=new AbortController();
  const signal=AbortSignal.any([startup.signal,AbortSignal.timeout(30000)]);
  state({state:"loading"});
  try {
    const cache=retry ? "reload" : "default";
    const manifest=validateManifest(parseJSON(await fetchChecked(setupData.config.complete.manifest,base,signal,cache)));
    const [terms,postings]=await Promise.all([fetchChecked(manifest.terms,base,signal,cache),fetchChecked(manifest.postings,base,signal,cache)]);
    const routing=decodeRouting(manifest,parseJSON(terms),postings);
    runner=new QueryRunner(manifest,routing,setupData.options,base,metrics=>state({state:"metrics",metrics}));
    ready=true;postMessage({type:1});state({state:"ready"});return true;
  } catch(error) {
    if(!signal.aborted || !startup.signal.aborted)state({state:"error",phase:"startup",message:String(error)});
    return false;
  }
}
function submit(value,retry=false) {
  latest=value;const id=++generation;active.abort();active=new AbortController();const signal=active.signal;
  queue=queue.then(async()=>{
    await setupPromise;
    if(id!==generation||!ready)return;
    state({state:"query"});
    try {
      const result=await runner.execute(value,signal,()=>id===generation,retry ? "reload" : "default");
      if(result&&id===generation) {postMessage({type:3,data:result});state({state:"ready"});}
    } catch(error) {
      if(id!==generation)return;
      active.abort();postMessage({type:3,data:{items:[]}});
      state({state:"error",phase:"query",message:String(error)});
    }
  }).catch(error=>state({state:"error",message:String(error)}));
}
addEventListener("message",({data})=>{
  if(data.type===0) {setupData=data.data;setupPromise=setup();}
  if(data.type===2&&typeof data.data==="string")submit(data.data);
});
if(channel)channel.onmessage=({data})=>{
  if(data?.type!=="retry"||!setupData)return;
  if(!ready)setupPromise=setup(true);
  submit(latest,true);
};
