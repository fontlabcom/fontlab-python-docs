// this_file: scripts/search_backend/router.js
import {lunr, transformSearchQuery} from "./engine.ts";
import {readVarint} from "./validation.js";
export {validateManifest, decodeRouting, readVarint, fetchChecked} from "./validation.js";
// Routing is only a safe superset. The original engine evaluates every field/operator.
export function candidates(value, manifest, routing) {
  lunr.tokenizer.separator = new RegExp(manifest.config.separator);
  const transformed = transformSearchQuery(value), query = new lunr.Query(["title","text","tags"]);
  if (!transformed) return {selected:[], docs:new Set()};
  new lunr.QueryParser(transformed,query).parse();
  const all = () => ({selected:manifest.shards.map(x=>x.id),docs:null});
  // A nontrivial search pipeline can rewrite query terms. Conservatively hydrate all rows.
  if (manifest.config.pipeline.some(x=>x!=="trimmer") || /\p{sc=Han}/u.test(value) ||
      query.clauses.every(c=>c.presence===lunr.Query.presence.PROHIBITED)) return all();
  const ids = new Set(), docs = new Set();
  for (const clause of query.clauses) {
    if (clause.presence===lunr.Query.presence.PROHIBITED) continue;
    if (clause.editDistance || clause.term.slice(0,-1).includes("*")) return all();
    const prefix = clause.term.endsWith("*") ? clause.term.slice(0,-1) : null;
    const term = prefix ?? clause.term, terms = routing.terms;
    let lo=0, hi=terms.length;
    while(lo<hi) {const mid=(lo+hi)>>>1;if(terms[mid]<term)lo=mid+1;else hi=mid;}
    for(let i=lo;i<terms.length&&(prefix!==null?terms[i].startsWith(prefix):terms[i]===term);i++) {
      const pointer={at:routing.offsets[i]}, count=readVarint(routing.postings,pointer);let doc=0;
      for(let j=0;j<count;j++) {doc+=readVarint(routing.postings,pointer);docs.add(doc);ids.add(routing.docShard[doc]);}
    }
  }
  return {selected:[...ids].sort((a,b)=>a-b),docs};
}
export function hydrate(rows, spec, wanted) {
  if (!Array.isArray(rows) || rows.length !== spec.rows || rows.some(x=>!x || typeof x.location!=="string"))
    throw Error("Invalid search shard rows");
  if (!wanted) return rows;
  const pages = new Set();
  rows.forEach((row,i)=>{if(wanted.has(spec.start+i))pages.add(row.location.split("#")[0]);});
  return rows.filter((row,i)=>wanted.has(spec.start+i)||pages.has(row.location));
}
