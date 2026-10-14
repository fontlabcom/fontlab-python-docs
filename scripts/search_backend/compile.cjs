// this_file: scripts/search_backend/compile.cjs
// Explicit maintainer command. Ordinary documentation builds use committed bundles offline.
const path = require("node:path"), fs = require("node:fs"), crypto = require("node:crypto");
const esbuild = require(path.resolve(__dirname,"../../.build/search-compiler/node_modules/esbuild"));
if (esbuild.version !== "0.25.12") throw Error("Pinned esbuild 0.25.12 is required");
const root = path.resolve(__dirname, "../..");
const provenance = JSON.parse(fs.readFileSync(path.join(__dirname,"source-provenance.json")));
for (const source of provenance.sources)
  if (crypto.createHash("sha256").update(fs.readFileSync(path.join(__dirname,source.vendored))).digest("hex") !== source.sha256)
    throw Error(`Vendored original source drift: ${source.source}`);
const materialLicense = fs.readFileSync(path.join(__dirname,"vendor/src/templates/assets/javascripts/integrations/search/_/index.ts"),"utf8").split("*/")[0]+"*/";
const lunrLicense = fs.readFileSync(path.join(__dirname,"vendor/lunr.js"),"utf8").split("*/")[0]+"*/";
for (const [entry, outfile, platform, format] of [
  ["engine.ts", "scripts/search_backend/engine.cjs", "node", "cjs"],
  ["worker.js", "overrides/assets/javascripts/workers/complete-search.js", "browser", "iife"],
  ["router.js", "scripts/search_backend/router.cjs", "node", "cjs"],
  ["query.js", "scripts/search_backend/query.cjs", "node", "cjs"],
]) esbuild.buildSync({entryPoints:[path.join(__dirname, entry)], outfile:path.join(root,outfile), bundle:true, platform, format,
  legalComments:"inline", banner:{js:`// this_file: ${outfile}\n// Generated with esbuild 0.25.12; retained MIT engine headers below.\n${materialLicense}\n${lunrLicense}`}});
const files = {};
for (const file of ["engine.cjs", "router.cjs", "query.cjs", "../../overrides/assets/javascripts/workers/complete-search.js"])
  files[file] = crypto.createHash("sha256").update(fs.readFileSync(path.join(__dirname,file))).digest("hex");
fs.writeFileSync(path.join(__dirname,"bundles.json"),JSON.stringify({esbuild:"0.25.12",files},null,2)+"\n");
