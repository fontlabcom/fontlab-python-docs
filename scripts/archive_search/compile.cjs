// this_file: scripts/archive_search/compile.cjs
// Explicit maintainer build. Ordinary site builds verify and copy committed assets.
const fs = require("node:fs"), path = require("node:path"), crypto = require("node:crypto");
const ROOT = __dirname;
const MODULES = path.resolve(ROOT, "../../.build/archive-compiler/node_modules");
const digest = bytes => crypto.createHash("sha256").update(bytes).digest("hex");

function verify(root = ROOT, modules = MODULES) {
  const inventory = JSON.parse(fs.readFileSync(path.join(root, "sources.json")));
  for (const row of inventory.files) {
    const bytes = fs.readFileSync(path.join(root, row.path));
    if (bytes.length !== row.bytes || digest(bytes) !== row.sha256)
      throw Error(`Archive preferred-source identity differs: ${row.path}`);
  }
  const lunr = fs.readFileSync(path.join(modules, "lunr/lunr.js"));
  const original = fs.readFileSync(path.join(root, "provenance/baseline/node_modules/lunr/lunr.js"));
  const lock = JSON.parse(fs.readFileSync(path.join(root, "package-lock.json")));
  const expected = JSON.parse(fs.readFileSync(path.join(root, "provenance/lunr-bindings.json")));
  if (!lunr.equals(original) || lock.packages["node_modules/lunr"].integrity !== expected.integrity ||
      lock.packages["node_modules/lunr"].version !== "2.3.9")
    throw Error("Locked official Lunr dependency differs");
  return inventory;
}

function compile({ root = ROOT, modules = MODULES, output = path.join(root, "dist"), compiler } = {}) {
  const inventory = verify(root, modules);
  compiler ||= require(path.join(modules, "esbuild"));
  if (compiler.version !== "0.25.12") throw Error("Pinned esbuild 0.25.12 is required");
  const result = compiler.buildSync({absWorkingDir:root,
    entryPoints:["src/templates/assets/javascripts/integrations/search/worker/main/index.ts"],
    outfile:"dist/search.js", bundle:true, minify:true, format:"iife", platform:"browser",
    target:"es2020", sourcemap:true, sourcesContent:true, legalComments:"eof",
    nodePaths:[modules], metafile:true, write:false, logLevel:"silent"});
  const map = result.outputFiles.find(file => file.path.endsWith(".map")).contents;
  const mapName = `search.${digest(map)}.js.map`;
  const source = result.outputFiles.find(file => file.path.endsWith(".js")).text;
  if (!source.endsWith("//# sourceMappingURL=search.js.map\n"))
    throw Error("Unexpected compiler source-map trailer");
  const worker = Buffer.from(source.replace("sourceMappingURL=search.js.map", `sourceMappingURL=${mapName}`));
  const workerName = `search.${digest(worker)}.js`;
  const notices = Buffer.concat([Buffer.from("Archived PythonQt search derivative. MaterialX and Lunr MIT notices follow.\n\n"),
    fs.readFileSync(path.join(root,"LICENSE.MaterialX")), Buffer.from("\n"), fs.readFileSync(path.join(root,"LICENSE.Lunr"))]);
  const outputs = {[workerName]:worker, [mapName]:map, "NOTICE.txt":notices};
  const receipt = {schema_version:1, compiler:"esbuild0.25.12", lunr:"2.3.9",
    worker:workerName, map:mapName, sources_sha256:digest(fs.readFileSync(path.join(root,"sources.json"))),
    original:inventory.original, config:inventory.config,
    files:Object.fromEntries(Object.entries(outputs).map(([name,bytes]) => [name,{sha256:digest(bytes),bytes:bytes.length}]))};
  fs.mkdirSync(output,{recursive:true});
  for (const [name,bytes] of Object.entries(outputs)) fs.writeFileSync(path.join(output,name),bytes);
  fs.writeFileSync(path.join(output,"receipt.json"),JSON.stringify(receipt,null,2)+"\n");
  fs.writeFileSync(path.join(output,"metafile.json"),JSON.stringify(result.metafile,null,2)+"\n");
  return receipt;
}

if (require.main === module) compile();
module.exports = {compile,verify};
