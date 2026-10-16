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
// lunr 2.3.9 keys TokenSet nodes as label+id with no terminator, so a digit label
// next to an id collides ("1"+234 vs "1"+2,"3"+4) and minimisation merges distinct
// nodes; large indexes then lose words and Index.query throws. The vendored source
// stays byte-exact; this one line is rewritten while bundling (issue 106, final-6).
const LUNR_PATCH = {from: "    str = str + label + node.id\n", to: "    str = str + label + node.id + \";\"\n"};
const lunrPatch = {name: "lunr-tokenset-key", setup(build) {
  build.onLoad({filter: /vendor[\\/]lunr\.js$/}, ({path: file}) => {
    const source = fs.readFileSync(file, "utf8");
    if (source.split(LUNR_PATCH.from).length !== 2) throw Error("lunr TokenSet key patch must match exactly once");
    return {contents: source.replace(LUNR_PATCH.from, LUNR_PATCH.to), loader: "js"};
  });
}};
(async () => {
for (const [entry, outfile, platform, format] of [
  ["engine.ts", "scripts/search_backend/engine.cjs", "node", "cjs"],
  ["worker.js", "overrides/assets/javascripts/workers/complete-search.js", "browser", "iife"],
  ["router.js", "scripts/search_backend/router.cjs", "node", "cjs"],
  ["query.js", "scripts/search_backend/query.cjs", "node", "cjs"],
]) await esbuild.build({entryPoints:[path.join(__dirname, entry)], outfile:path.join(root,outfile), bundle:true, platform, format, plugins:[lunrPatch],
  legalComments:"inline", banner:{js:`// this_file: ${outfile}\n// Generated with esbuild 0.25.12; retained MIT engine headers below.\n${materialLicense}\n${lunrLicense}`}});
const files = {};
for (const file of ["engine.cjs", "router.cjs", "query.cjs", "../../overrides/assets/javascripts/workers/complete-search.js"])
  files[file] = crypto.createHash("sha256").update(fs.readFileSync(path.join(__dirname,file))).digest("hex");
fs.writeFileSync(path.join(__dirname,"bundles.json"),JSON.stringify({esbuild:"0.25.12",files,
  patches:{"vendor/lunr.js":LUNR_PATCH}},null,2)+"\n");
})().catch(error => { console.error(error); process.exitCode = 1; });
