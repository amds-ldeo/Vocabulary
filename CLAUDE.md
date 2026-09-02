# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A vocabulary workspace, not an application. The authoritative content is a set of SKOS
concept schemes serialized as Turtle (`.ttl`), grouped into per-topic source directories:

| Directory       | Contents |
|-----------------|----------|
| `geochemistry/` | Analytical technique/method vocabularies (`GeochemAnalyticalMethod.ttl`, `onegctechniquesastromatv4.ttl`) |
| `ETmaterials/`  | Meteorite / extraterrestrial material classes (`ExtraterrestrialMaterialsMindat.ttl`) |
| `instrumentAll/`| Seven NERC/SeaDataNet-derived schemes (Instruments, NumericModel, Parameters, PositioningSystem, SampleCollection, SamplePreparation, SeismicSource) |
| `instruments/`  | MMISW instrument models, GCMD instruments |

Everything else is machinery that turns those `.ttl` files into published HTML.
`*/archive/` holds superseded drafts and legacy Quarto output — read-only history, do not
regenerate or "fix" it.

## The publishing pipeline

One composite Docker action (`action.yml` + `Dockerfile`) is invoked by several GitHub
workflows. Chain of control:

1. `.github/workflows/process_<subdir>_vocab.yml` calls `uses: ./` with inputs
   `vocabdir`, `inputttl` (pipe-delimited ttl basenames, no extension), and
   `inputvocaburi` (pipe-delimited ConceptScheme CURIEs, **same count and order**).
2. `Dockerfile` builds an image with `tools/` plus the four vocabulary source
   directories, installs `tools/requirements.txt` and Quarto, and runs
   `.github/actions/github_action_main.py`.
3. For each ttl file, `github_action_main.py`:
   deletes `cache/vocabularies.db` → `tools/vocab.py load <ttl> <curie>` (parses Turtle
   into an rdflib-sqlalchemy SQLite store) → `tools/vocab2mdCacheV2.py <db> <curie>`
   (SPARQL over the store, emits Quarto-flavored Markdown to stdout, redirected to
   `docs/<name>.md`) → `quarto render` to HTML.
4. The workflow re-owns `docs/` (the container writes as root), moves the outputs into
   `staged_docs/<subdir>/`, and deploys to the **`gh-pages`** branch under
   `docs/<subdir>/` via `JamesIves/github-pages-deploy-action`.

`process_all_vocabularies.yml` chains all four via `needs:` — deliberately **sequential**,
because the deploy action force-pushes `gh-pages` and parallel jobs would race. Preserve
that chaining when adding a new subdirectory workflow.

`publish_landing_page.yml` owns only `docs/readme.md` and deploys with `clean: false`, so
it does not wipe the per-subdirectory HTML. On `master`, `docs/` contains only that landing
page; generated HTML exists solely on `gh-pages`.

All `process_*` workflows are `workflow_dispatch` + `workflow_call` — manual only.

## Key invariants

- **The CURIE must resolve from the ttl file's own `@prefix` declarations.**
  `vocab2mdCacheV2.main` calls `store.expand_name(vocabulary)`, which expands against the
  namespace manager populated when that file was loaded. `meth:method`, `etma:cscheme`,
  `sdndev:current`, `edmedscheme:current`, `mmiscm:ontology` are the CURIEs in use.
- **One vocabulary per cache DB.** `_reset_cache_db()` deletes the SQLite file before each
  load; navocab's purge path is unreliable. If you load locally without deleting first,
  concepts from an earlier vocabulary leak into the next one's output.
- **Multiple `skos:ConceptScheme` declarations per file are normal** (external NERC schemes
  plus in-house ones). The scheme to pass is the one whose `skos:hasTopConcept` entries are
  actually anchored in that file's own `skos:broader`/`narrower` graph — `SDNDEV/current`
  for six `instrumentAll` files, `EDMED_DCAT_THEMES/current` for `Parameters.ttl`.
- **`getVocabRoot` fallback chain** (`tools/vocab2mdCacheV2.py:129`): `skos:topConceptOf`
  or `skos:hasTopConcept` first; failing that, every `skos:inScheme` concept as a flat root,
  accepting both `rdf:type skos:Concept` and subclass typing (`?C rdfs:subClassOf
  skos:Concept`). That subclass branch is what makes `mmisw-models.ttl` (items typed
  `:ModelName`) render at all. `getNarrower` similarly falls back to an unscoped query when
  concepts omit `skos:inScheme`.
- **Non-base-ASCII characters in a ttl file break the conversion.** This is a long-standing
  failure mode; the GitHub Pages step is even stricter than the Python. Check for them
  first when a build fails on an edited vocabulary.

## Local runs

`tools/runVocabTools.py` is a stale IDE-driver copy with hardcoded iSamples paths — do not
use it as-is. Reproduce the pipeline stage by stage instead (Windows, from the repo root):

```bash
python -m venv .venv && .venv/Scripts/python.exe -m pip install -r tools/requirements.txt
```

Then, per vocabulary — delete the cache DB, load, generate, render:

```bash
rm -f cache/vocabularies.db && .venv/Scripts/python.exe tools/vocab.py --verbosity ERROR -s cache/vocabularies.db load "geochemistry/GeochemAnalyticalMethod.ttl" "meth:method"
```

```bash
PYTHONIOENCODING=utf-8 .venv/Scripts/python.exe tools/vocab2mdCacheV2.py cache/vocabularies.db "meth:method" > testoutput/local_run/GeochemAnalyticalMethod.md
```

```bash
quarto render testoutput/local_run/GeochemAnalyticalMethod.md -t html
```

`PYTHONIOENCODING=utf-8` matters on Windows — the Markdown goes to stdout and the default
console encoding mangles it. `cache/`, `.venv/`, and `testoutput/local_run/` are gitignored;
put scratch output in `testoutput/local_run/`, never in `docs/`.

`tools/vocab.py` is also a standalone `click` CLI (`vocabs`, `roots`, `concepts`, `narrower`,
`match`, `namespaces`) — useful for inspecting a loaded store when diagnosing why a
vocabulary renders empty or with the wrong roots. See `tools/README.md` for examples.

## Editing conventions

- `tools/vocab.py`, `tools/vocab2mdCacheV2.py`, `tools/navocab/`, and `tools/requirements.txt`
  are vendored from the iSamples `metadata_profile_earth_science` repo. Changes made here
  (the `getVocabRoot`/`getNarrower` fallbacks) are local divergences — note them when
  touching that code, since a naive re-vendor would drop them.
- Adding a vocabulary: put the ttl in the appropriate subdirectory, then extend that
  subdirectory's workflow's `inputttl`/`inputvocaburi` (both lists, matching order) and its
  staging `for` loop, and add the entry to `docs/readme.md`. A new subdirectory also needs a
  `COPY` line in the `Dockerfile` and a `needs:`-chained job in `process_all_vocabularies.yml`.
- `.dockerignore` deliberately excludes archives, spreadsheets, PDFs, and legacy HTML to
  keep the image small; if a new source file is not landing in the container, check it.
