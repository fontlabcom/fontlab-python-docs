// this_file: scripts/search_backend/query.js
import {Search} from "./engine.ts";
import {candidates, hydrate} from "./router.js";
import {fetchChecked, parseJSON} from "./validation.js";
const CACHE_LIMIT = 3*1024*1024;
export const SHARD_DEADLINE_MS=1800, MAX_SHARD_DEADLINE_MS=30000;
// A new query fails fast; each consecutive Retry doubles the per-shard deadline
// (capped like startup) so a slow but live host can still complete.
export const shardDeadline=attempt=>Math.min(MAX_SHARD_DEADLINE_MS,SHARD_DEADLINE_MS*2**attempt);
// Cache owns original bytes only. Query-specific indexes never persist between queries.
export class QueryRunner {
  constructor(manifest,routing,options,base,notify) {
    Object.assign(this,{manifest,routing,options,base,notify});
    this.cache=new Map();this.cacheBytes=0;this.liveBytes=0;this.peakLiveBytes=0;this.peakCacheBytes=0;
  }
  remember(id,bytes) {
    if (this.cache.has(id)) return;
    while(this.cache.size && this.cacheBytes+bytes.length>CACHE_LIMIT) {
      const key=this.cache.keys().next().value;this.cacheBytes-=this.cache.get(key).length;this.cache.delete(key);
    }
    this.cache.set(id,bytes);this.cacheBytes+=bytes.length;this.peakCacheBytes=Math.max(this.peakCacheBytes,this.cacheBytes);
  }
  async execute(value,signal,current,fetchCache="default",deadline=SHARD_DEADLINE_MS) {
    const {selected,docs}=candidates(value,this.manifest,this.routing), pending=new Map(), groups=[], suggestions=new Set();
    let scheduledWindowBound=0;
    const take = async id => {
      const spec=this.manifest.shards[id], cached=this.cache.get(id);
      const bytes=cached || await fetchChecked(spec,this.base,AbortSignal.any([signal,AbortSignal.timeout(deadline)]),fetchCache);
      this.liveBytes+=bytes.length;this.peakLiveBytes=Math.max(this.peakLiveBytes,this.liveBytes);
      return bytes;
    };
    try {
      for(let i=0;i<selected.length;i++) {
        if(!current())return null;
        const window=selected.slice(i,i+3);
        scheduledWindowBound=Math.max(scheduledWindowBound,window.reduce((n,id)=>n+this.manifest.shards[id].raw,0));
        for(const id of window) if(!pending.has(id)) pending.set(id,take(id).then(bytes=>({bytes}),error=>({error})));
        const id=selected[i], entry=await pending.get(id);pending.delete(id);
        if(entry.error)throw entry.error;
        try {
          if(!current())return null;
          const rows=hydrate(parseJSON(entry.bytes),this.manifest.shards[id],docs);
          const result=new Search({config:this.manifest.config,docs:rows,options:this.options}).search(value);
          groups.push(...result.items);
          for(const suggestion of result.suggest || [])suggestions.add(suggestion);
          this.remember(id,entry.bytes);
        } finally {this.liveBytes-=entry.bytes.length;}
      }
      if(!current())return null;
      groups.sort((a,b)=>b[0].score-a[0].score);
      return {items:groups,...this.options.suggest && {suggest:[...suggestions]}};
    } finally {
      // Already prefetched responses must be released on failure/cancellation too.
      for(const promise of pending.values()) {const entry=await promise;if(entry.bytes)this.liveBytes-=entry.bytes.length;}
      this.notify({cacheBytes:this.cacheBytes,peakCacheBytes:this.peakCacheBytes,liveBytes:this.liveBytes,
        peakLiveBytes:this.peakLiveBytes,scheduledWindowBound});
    }
  }
}
