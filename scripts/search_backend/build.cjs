// this_file: scripts/search_backend/build.cjs
// Extract complete postings from the pinned original engine, preserving raw rows before mutation.
const fs = require("node:fs"), path = require("node:path"), crypto = require("node:crypto"), zlib = require("node:zlib");
const {Search} = require("./engine.cjs");
const [input, directory, target] = process.argv.slice(2);
const corpus = JSON.parse(fs.readFileSync(input)), groups = new Map(), termDocs = new Map();
if (!Array.isArray(corpus.config.lang) || corpus.config.lang.length !== 1 || corpus.config.lang[0] !== "en") throw Error("Complete search currently supports the pinned English engine only; language assets must be provisioned explicitly");
for (const row of corpus.docs) {
  const page = row.location.split("#")[0];
  if (!groups.has(page)) groups.set(page, []);
  groups.get(page).push(row);
}
const shards = []; let current = [], size = 0;
for (const rows of groups.values()) {
  const bytes = Buffer.byteLength(JSON.stringify(rows));
  if (size && size + bytes > Number(target)) {shards.push(current); current = []; size = 0;}
  current.push(...rows); size += bytes;
}
if (current.length) shards.push(current);
const hash = data => crypto.createHash("sha256").update(data).digest("hex");
function write(file, data) {
  const gzip = zlib.gzipSync(data, {level:9});
  fs.writeFileSync(path.join(directory,file),data);
  fs.writeFileSync(path.join(directory,file+".gz"),gzip);
  return {file, raw:data.length, gzip:gzip.length, sha256:hash(data)};
}
const manifest = {version:1, engine:"materialx-10.1.5/lunr-2.3.9", config:corpus.config, rows:corpus.docs.length,
  input_sha256:hash(fs.readFileSync(input)), input_raw:fs.statSync(input).size,
  input_gzip:zlib.gzipSync(fs.readFileSync(input),{level:9}).length, tokens:0, shards:[]};
let start = 0;
for (const [id, docs] of shards.entries()) {
  const raw = Buffer.from(JSON.stringify(docs));
  manifest.shards.push({id, start, rows:docs.length, ...write(`rows-${hash(raw)}.json`,raw)});
  const ids = new Map(docs.map((row, i) => [row.location,start+i]));
  const search = new Search({config:corpus.config, docs, options:{suggest:false}});
  for (const [term, posting] of Object.entries(search.index.invertedIndex)) {
    if (!termDocs.has(term)) termDocs.set(term,new Set());
    for (const field of search.index.fields)
      for (const location of Object.keys(posting[field])) termDocs.get(term).add(ids.get(location));
  }
  start += docs.length;
}
const entries = [...termDocs].sort((a,b) => a[0] < b[0] ? -1 : a[0] > b[0] ? 1 : 0), bytes = [];
function put(value) {while (value>127) {bytes.push((value&127)|128);value=Math.floor(value/128);} bytes.push(value);}
for (const [, ids] of entries) {
  const sorted = [...ids].sort((a,b)=>a-b); put(sorted.length); let last = 0;
  for (const id of sorted) {put(id-last);last=id;}
}
manifest.tokens = entries.length;
manifest.terms = write("terms.json",Buffer.from(JSON.stringify(entries.map(([term])=>term))));
manifest.postings = write("postings.bin",Buffer.from(bytes));
write("manifest.json",Buffer.from(JSON.stringify(manifest)));
console.log(JSON.stringify({rows:manifest.rows,shards:shards.length,tokens:entries.length}));
