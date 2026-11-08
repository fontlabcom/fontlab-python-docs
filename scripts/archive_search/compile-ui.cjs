// this_file: scripts/archive_search/compile-ui.cjs
// Maintainer-only compiler. Site builds validate and copy the committed UI assets.
const fs = require("node:fs"), path = require("node:path"), crypto = require("node:crypto");
const ROOT = __dirname, MODULES = path.resolve(ROOT, "../../.build/archive-compiler/node_modules");
const digest = bytes => crypto.createHash("sha256").update(bytes).digest("hex");
const safe = name => typeof name === "string" && !path.isAbsolute(name) && !name.split(/[\\/]/).includes("..") && !name.includes("\\");

function verify(root = ROOT, modules = MODULES) {
  const inventory = JSON.parse(fs.readFileSync(path.join(root, "ui-sources.json")));
  const lock = JSON.parse(fs.readFileSync(path.join(root, "package-lock.json")));
  for (const row of inventory.files) {
    if (!safe(row.path)) throw Error("Unsafe UI preferred-source path");
    const bytes = fs.readFileSync(path.join(root, row.path));
    if (bytes.length !== row.bytes || digest(bytes) !== row.sha256)
      throw Error(`UI preferred-source identity differs: ${row.path}`);
  }
  for (const row of inventory.dependencies) {
    if (!safe(row.path)) throw Error("Unsafe UI dependency path");
    const bytes = fs.readFileSync(path.join(modules, row.path));
    if (bytes.length !== row.bytes || digest(bytes) !== row.sha256)
      throw Error(`UI dependency identity differs: ${row.path}`);
  }
  for (const [name, identity] of Object.entries(inventory.packages)) {
    const installed = JSON.parse(fs.readFileSync(path.join(modules, name, "package.json")));
    const locked = lock.packages[`node_modules/${name}`];
    if (installed.version !== identity.version || locked.version !== identity.version || locked.integrity !== identity.integrity)
      throw Error(`Locked UI package differs: ${name}`);
  }
  return inventory;
}

function compile({root = ROOT, modules = MODULES, output = path.join(root, "ui-dist"), compiler} = {}) {
  const inventory = verify(root, modules);
  compiler ||= require(path.join(modules, "esbuild"));
  if (compiler.version !== "0.25.12") throw Error("Pinned esbuild 0.25.12 is required");
  const result = compiler.buildSync({absWorkingDir: root,
    entryPoints: ["ui/src/templates/assets/javascripts/bundle.ts"], outfile: "ui-dist/bundle.js",
    tsconfig: path.join(root, "ui/tsconfig.json"), bundle: true, minify: true, format: "iife",
    platform: "browser", target: "es2015", jsxFactory: "h", legalComments: "inline",
    sourcemap: true, sourcesContent: true, metafile: true, write: false,
    loader: {".css": "text"}, nodePaths: [modules], logLevel: "silent"});
  const mapFile = result.outputFiles.find(file => file.path.endsWith(".map"));
  const jsFile = result.outputFiles.find(file => file.path.endsWith(".js"));
  if (!mapFile || !jsFile || result.outputFiles.length !== 2) throw Error("Unexpected UI compiler outputs");
  const mapping = JSON.parse(mapFile.text);
  if (!mapping.mappings || !mapping.sourcesContent || mapping.sources.length !== mapping.sourcesContent.length)
    throw Error("Incomplete UI source map");
  // Normalize only truthful source names; require every mapped string to equal its resolved file.
  mapping.sources = mapping.sources.map((name, i) => {
    const resolved = path.resolve(root, "ui-dist", name);
    let canonical;
    if (resolved.startsWith(path.join(root, "ui/src") + path.sep)) canonical = "materialx/" + path.relative(path.join(root, "ui/src"), resolved);
    else if (resolved.startsWith(modules + path.sep)) canonical = "node_modules/" + path.relative(modules, resolved);
    else throw Error("Unexpected UI mapped source path");
    canonical = canonical.split(path.sep).join("/");
    if (!safe(canonical) || fs.readFileSync(resolved, "utf8") !== mapping.sourcesContent[i]) throw Error("UI mapped source differs");
    return canonical;
  });
  const entries = Object.entries(result.metafile.outputs);
  if (entries.filter(([, value]) => value.entryPoint).length !== 1 || entries.some(([, value]) => value.imports.length))
    throw Error("Unexpected UI runtime import or entrypoint");
  for (const [name, input] of Object.entries(result.metafile.inputs)) {
    const resolved = path.resolve(root, name);
    if (!resolved.startsWith(path.join(root, "ui/src") + path.sep) && !resolved.startsWith(modules + path.sep))
      throw Error("Unexpected UI resolved input");
    for (const edge of input.imports)
      if (!edge.external && !Object.hasOwn(result.metafile.inputs, edge.path)) throw Error("Unresolved UI import");
  }
  const map = Buffer.from(JSON.stringify(mapping) + "\n"), mapName = `bundle.${digest(map)}.js.map`;
  if (!jsFile.text.endsWith("//# sourceMappingURL=bundle.js.map\n")) throw Error("Unexpected UI source-map trailer");
  const bundle = Buffer.from(jsFile.text.replace("sourceMappingURL=bundle.js.map", `sourceMappingURL=${mapName}`));
  const bundleName = `bundle.${digest(bundle)}.js`, notice = fs.readFileSync(path.join(root, "ui/NOTICE.txt"));
  const outputs = {[bundleName]: bundle, [mapName]: map, "NOTICE.txt": notice};
  const receipt = {schema_version: 1, compiler: "esbuild0.25.12", target: "es2015", bundle: bundleName, map: mapName,
    sources_sha256: digest(fs.readFileSync(path.join(root, "ui-sources.json"))), original: inventory.original,
    files: Object.fromEntries(Object.entries(outputs).map(([name, bytes]) => [name, {sha256:digest(bytes), bytes:bytes.length}]))};
  fs.mkdirSync(output, {recursive:true});
  for (const [name, bytes] of Object.entries(outputs)) fs.writeFileSync(path.join(output, name), bytes);
  fs.writeFileSync(path.join(output, "receipt.json"), JSON.stringify(receipt, null, 2) + "\n");
  // Maintainer resolution evidence is source-bearing, outside the four published assets.
  fs.writeFileSync(path.join(output, "metafile.json"), JSON.stringify(result.metafile, null, 2) + "\n");
  return receipt;
}
if (require.main === module) compile();
module.exports = {compile, verify};
