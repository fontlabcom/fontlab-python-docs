// this_file: scripts/search_backend/verify.cjs
// Offline complete metadata verification uses the same decoder as the browser worker.
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const {validateManifest,decodeRouting}=require("./router.cjs");
const directory=process.argv[2],manifest=validateManifest(JSON.parse(fs.readFileSync(path.join(directory,"manifest.json"))));
function read(spec) {
 const bytes=fs.readFileSync(path.join(directory,spec.file));
 if(bytes.length!==spec.raw || crypto.createHash("sha256").update(bytes).digest("hex")!==spec.sha256)throw Error("Invalid metadata hash/size");
 return bytes;
}
decodeRouting(manifest,JSON.parse(read(manifest.terms)),read(manifest.postings));
console.log(JSON.stringify({rows:manifest.rows,tokens:manifest.tokens,checked:true}));
