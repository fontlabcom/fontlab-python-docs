// this_file: scripts/search_backend/validation.js
// Check durable metadata before allocating router tables or announcing READY.
export function integer(value, label, max = 10000000) {
  if (!Number.isSafeInteger(value) || value < 0 || value > max) throw Error(`Invalid ${label}`);
  return value;
}
export function descriptor(spec) {
  if (!spec || !/^(manifest\.json|terms\.json|postings\.bin|rows-[a-f0-9]{64}\.json)$/.test(spec.file) ||
      !/^[a-f0-9]{64}$/.test(spec.sha256)) throw Error("Invalid search asset descriptor");
  integer(spec.raw,"asset size",128*1024*1024); integer(spec.gzip,"encoded asset size",128*1024*1024);
  return spec;
}
export function validateManifest(manifest) {
  if (!manifest || manifest.version !== 1 || manifest.engine !== "materialx-10.1.5/lunr-2.3.9" ||
      !/^[a-f0-9]{64}$/.test(manifest.input_sha256)) throw Error("Invalid complete search manifest");
  integer(manifest.rows,"row count"); integer(manifest.tokens,"token count",4000000);
  const config = manifest.config;
  if (!config || !Array.isArray(config.lang) || config.lang.length !== 1 || config.lang[0] !== "en" || !Array.isArray(config.pipeline) ||
      config.pipeline.some(x => !["trimmer","stemmer","stopWordFilter"].includes(x)) ||
      typeof config.separator !== "string" || config.separator.length > 1024 || !config.fields ||
      Object.keys(config.fields).some(x => !["title","text","tags"].includes(x))) throw Error("Unsupported search configuration");
  new RegExp(config.separator);
  descriptor(manifest.terms); descriptor(manifest.postings);
  if (manifest.terms.file !== "terms.json" || manifest.postings.file !== "postings.bin" ||
      !Array.isArray(manifest.shards) || manifest.shards.length > 100000) throw Error("Invalid search manifest assets");
  let rows = 0;
  for (const [id, shard] of manifest.shards.entries()) {
    descriptor(shard); integer(shard.rows,"shard rows");
    if (shard.id !== id || shard.start !== rows || shard.rows === 0 ||
        shard.file !== `rows-${shard.sha256}.json`) throw Error("Invalid shard range");
    rows += shard.rows;
  }
  if (rows !== manifest.rows) throw Error("Invalid aggregate row count");
  return manifest;
}
export function readVarint(bytes, pointer) {
  let value = 0, factor = 1;
  for (let length = 0; length < 5; length++, factor *= 128) {
    if (pointer.at >= bytes.length) throw Error("Truncated search varint");
    const byte = bytes[pointer.at++];
    value += (byte & 127) * factor;
    if (!(byte & 128)) {
      if ((length && byte === 0) || value > 0xffffffff) throw Error("Overlong search varint");
      return value;
    }
  }
  throw Error("Overlong search varint");
}
export function decodeRouting(manifest, terms, postings) {
  if (!Array.isArray(terms) || terms.length !== manifest.tokens ||
      terms.some((term,i) => typeof term !== "string" || (i && terms[i-1] >= term))) throw Error("Invalid sorted search terms");
  const offsets = new Uint32Array(terms.length), pointer = {at:0};
  for (let i = 0; i < terms.length; i++) {
    offsets[i] = pointer.at;
    const count = readVarint(postings,pointer);
    if (count > manifest.rows) throw Error("Invalid posting count");
    let row = 0;
    for (let j = 0; j < count; j++) {
      const delta = readVarint(postings,pointer); row += delta;
      if ((j && delta === 0) || row >= manifest.rows) throw Error("Invalid posting row range");
    }
  }
  if (pointer.at !== postings.length) throw Error("Trailing search postings");
  const docShard = new Uint32Array(manifest.rows);
  for (const shard of manifest.shards) docShard.fill(shard.id,shard.start,shard.start+shard.rows);
  return {terms, postings, offsets, docShard};
}
export async function fetchChecked(spec, base, signal, cache = "default") {
  descriptor(spec);
  const response = await fetch(new URL(spec.file+".gz",base),{signal,cache});
  if (!response.ok) throw Error(`${spec.file}: HTTP ${response.status}`);
  // Static hosts need not negotiate Content-Encoding for binary assets. Explicit
  // gzip files guarantee transfer sizes; Fetch first handles any HTTP encoding.
  let encodedBytes = 0;
  const bounded = new TransformStream({transform(chunk,controller) {
    encodedBytes += chunk.length;
    if (encodedBytes > spec.gzip) throw Error(`${spec.file}: invalid encoded size`);
    controller.enqueue(chunk);
  }});
  const stream = response.body.pipeThrough(bounded).pipeThrough(new DecompressionStream("gzip"));
  const reader = stream.getReader(), chunks = []; let length = 0;
  try {
    for (;;) {
      const {done,value} = await reader.read(); if (done) break;
      length += value.length;
      if (length > spec.raw) throw Error(`${spec.file}: invalid size`);
      chunks.push(value);
    }
  } finally { await reader.cancel(); }
  if (encodedBytes !== spec.gzip || length !== spec.raw) throw Error(`${spec.file}: truncated asset`);
  const bytes = new Uint8Array(length); let at = 0;
  for (const chunk of chunks) {bytes.set(chunk,at);at+=chunk.length;}
  const hash = [...new Uint8Array(await crypto.subtle.digest("SHA-256",bytes))].map(x=>x.toString(16).padStart(2,"0")).join("");
  if (hash !== spec.sha256) throw Error(`${spec.file}: invalid hash`);
  return bytes;
}
export function parseJSON(bytes) { return JSON.parse(new TextDecoder("utf-8",{fatal:true}).decode(bytes)); }
