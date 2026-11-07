// this_file: scripts/archive_search/src/templates/assets/javascripts/integrations/search/literal.ts
// Literal completion adapter for the hash-locked archived Lunr 2.3.9 engine.
export const namespace = "\uE000"
export const alias = (field: string) => `archive_literal_${field}`

export function guard(config: any, docs: any[]) {
  const expected = {"indexing":"full","lang":["en"],"min_search_length":3,"prebuild_index":false,"separator":"[\\s\\-\\.]+","pipeline":["stemmer","stopWordFilter","trimmer"],"fields":{"title":{"boost":1000.0},"text":{"boost":1.0},"tags":{"boost":1000000.0}}}
  if (lunr.version !== "2.3.9" || JSON.stringify(config) !== JSON.stringify(expected))
    throw new Error("Unsupported archived search identity")
  if (docs.some(doc => JSON.stringify(doc).includes(namespace)))
    throw new Error("Reserved literal namespace in corpus")
}

function literalStemmer(token: any) {
  return token.metadata.fields.some((field: string) => field.startsWith("archive_literal_"))
    ? token : lunr.stemmer(token)
}
function namespaceLiteral(token: any) {
  return token.metadata.fields.some((field: string) => field.startsWith("archive_literal_"))
    ? token.update((value: string) => namespace + value) : token
}


export function configure(builder: any, tokenize: any, field: any, fields: any) {
  lunr.Pipeline.registerFunction(literalStemmer, "archiveLiteralStemmer")
  lunr.Pipeline.registerFunction(namespaceLiteral, "archiveLiteralNamespace")
  builder.tokenizer = (value: any, metadata: any) => tokenize(value).map((token: any) => {
    token.metadata.fields = [...metadata.fields]
    return token
  })
  builder.pipeline.before(lunr.stemmer, literalStemmer)
  builder.pipeline.remove(lunr.stemmer)
  builder.pipeline.add(namespaceLiteral)
  for (const [name, spec] of Object.entries(fields))
    builder.field(alias(name), { ...spec as object, extractor: field(name) })
}

export function install(index: any) {
  const words = Object.keys(index.invertedIndex).sort()
  const original = lunr.TokenSet.fromArray(words.filter(word => !word.startsWith(namespace)))
  const literal = lunr.TokenSet.fromArray(words.filter(word => word.startsWith(namespace)))
  const full = index.tokenSet
  if (typeof full.intersect !== "function" || !full.edges ||
      !lunr.TokenSet.fromString(namespace + "x*").edges[namespace])
    throw new Error("Unsupported locked TokenSet shape")
  // One index, two vocabulary tries. No duplicate postings, vectors or parser.
  let allowLiteral = false
  full.intersect = (query: any) => {
    const keys = Object.keys(query.edges)
    const route = allowLiteral && keys.length === 1 && keys[0] === namespace ? literal : original
    return route.intersect(query)
  }
  return (query: string, literals: string[]) => {
    const parsed = new lunr.Query(["title", "text", "tags"])
    new lunr.QueryParser(query, parsed).parse()
    allowLiteral = !query.includes(namespace)
    try {
      const results = index.query((builder: any) => {
        for (const clause of parsed.clauses) builder.clause(clause)
        if (allowLiteral) for (const term of literals) {
          const raw = new lunr.Query(["title", "text", "tags"])
          new lunr.QueryParser(term + "*", raw).parse()
          for (const clause of raw.clauses)
            builder.clause({ ...clause, term: namespace + clause.term,
              fields: clause.fields.map(alias), usePipeline: false })
        }
      })
      if (literals.length && allowLiteral) for (const result of results) normalize(result.matchData.metadata)
      return results
    } finally { allowLiteral = false }
  }
}

function normalize(metadata: any) {
  for (const term of Object.keys(metadata)) {
    if (!term.startsWith(namespace)) continue
    const clean = term.slice(namespace.length)
    metadata[clean] ||= Object.create(null)
    for (const [name, data] of Object.entries(metadata[term]) as any) {
      const field = name.slice("archive_literal_".length)
      metadata[clean][field] ||= { position: [] }
      metadata[clean][field].position = [...new Set([
        ...metadata[clean][field].position, ...data.position
      ])]
    }
    delete metadata[term]
  }
}
