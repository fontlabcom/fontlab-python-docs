// this_file: scripts/search_backend/engine.ts
// Engine sources are unchanged MaterialX 10.1.5 / Lunr 2.3.9; see source-provenance.json.
import lunr from "./vendor/lunr.js";
import { Search } from "./vendor/src/templates/assets/javascripts/integrations/search/_";
import { transformSearchQuery } from "./vendor/src/templates/assets/javascripts/integrations/search/query";
(globalThis as any).lunr = lunr;
export { lunr, Search, transformSearchQuery };
