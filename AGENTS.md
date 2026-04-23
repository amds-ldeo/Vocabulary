# AGENTS.md

Short operational guide for maintainers and coding agents working on this repo. See [`README.md`](README.md) for the user-facing overview.

## What this repo is

A multi-subdirectory SKOS vocabulary repo adapted from [`isamplesorg/vocabularyTemplate`](https://github.com/isamplesorg/vocabularyTemplate). Pipeline: SKOS Turtle (`<subdir>/*.ttl`) → SQLite (`tools/vocab.py` / navocab) → Markdown (`tools/vocab2mdCacheV2.py`) → HTML (Quarto) → deployed to `gh-pages:/docs/<subdir>/` via [JamesIves/github-pages-deploy-action](https://github.com/JamesIves/github-pages-deploy-action).

Unlike the upstream template (which assumes a single `vocabulary/` folder), this repo runs one workflow per subdirectory and passes the target directory through the `vocabdir` input on [`action.yml`](action.yml). Docs landing page lives at [`docs/readme.md`](docs/readme.md) and is deployed by a dedicated [`publish_landing_page.yml`](.github/workflows/publish_landing_page.yml) with `clean: false` so per-subdir content isn't wiped.

Live site: <https://amds-ldeo.github.io/Vocabulary/>.

## Vocabularies

| Subdir | Slug (no ext) | ConceptScheme CURIE | Notes |
|---|---|---|---|
| `geochemistry` | `GeochemAnalyticalMethod` | `meth:method` | `meth:` = `<https://w3id.org/geochem/1.0/analyticalmethod/>` |
| `geochemistry` | `onegctechniquesastromatv4` | `meth:method` | `meth:` = `<https://w3id.org/geochem/1.1/analyticalmethod/>` (added at top of file) |
| `ETmaterials` | `ExtraterrestrialMaterialsMindat` | `etma:cscheme` | — |
| `instrumentAll` | `Instruments` | `sdndev:current` | anchored at `sdnc:ICAT03`/`ICAT04`/`ICAT05` |
| `instrumentAll` | `NumericModel` | `sdndev:current` | `skos:hasTopConcept sdnc:ICAT08` added locally (see `skos:historyNote`) |
| `instrumentAll` | `Parameters` | `edmedscheme:current` | anchored at `edct:D0100001..005` |
| `instrumentAll` | `PositioningSystem` | `sdndev:current` | anchored at `sdnc:ICAT06` |
| `instrumentAll` | `SampleCollection` | `sdndev:current` | anchored at `sdnc:ICAT01` |
| `instrumentAll` | `SamplePreparation` | `sdndev:current` | anchored at `sdnc:ICAT02` |
| `instrumentAll` | `SeismicSource` | `sdndev:current` | anchored at `sdnc:ICAT07` |
| `instruments` | `mmisw-models` | `mmiscm:ontology` | flat vocab; items typed `:ModelName` (subclass of `skos:Concept`) — relies on local `getVocabRoot` flat+subclass fallback |

`sdndev:` = `<http://vocab.nerc.ac.uk/scheme/SDNDEV/>`, `edmedscheme:` = `<http://vocab.nerc.ac.uk/scheme/EDMED_DCAT_THEMES/>`, `mmiscm:` = `<http://w3id.org/def/mmisw/models/>`. All three were added as `@prefix` declarations at the top of the relevant ttl files so the CURIEs pass through `inputvocaburi`.

`instruments/gcmd-instrument.ttl` is intentionally excluded from the pipeline.

## Adding a new vocabulary

1. Drop the `.ttl` under the appropriate subdirectory (`geochemistry/`, `ETmaterials/`, etc.), or create a new subdir if it's a new topic.
2. Verify the file declares a `skos:ConceptScheme` and either (a) has `skos:hasTopConcept`/`skos:topConceptOf` assertions pointing to real tree roots, or (b) is a flat list (`getVocabRoot` will fall back).
3. Identify the `@prefix` that resolves the scheme URI as a CURIE; add one if missing (a `@prefix` line in the ttl header is a harmless binding, not a semantic change).
4. Add the slug + CURIE to the corresponding `.github/workflows/process_<subdir>_vocab.yml` (`inputttl` and `inputvocaburi` are pipe-delimited, same order).
5. Add a link in [`docs/readme.md`](docs/readme.md).
6. If it's in a new subdir: create a new workflow file (copy one of the existing ones, adjust `vocabdir`, `inputttl`, `inputvocaburi`, target folder), and add `COPY ./<subdir> ./<subdir>` to the [`Dockerfile`](Dockerfile) so the source is available in the container.
7. Verify locally with Option-A (below). On GitHub, dispatch the workflow via the Actions tab.

## Local verification (Option A — no Docker)

Fast feedback loop. Exercises every pure-Python fix but not the Dockerfile or the JamesIves deploy step.

```bash
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r tools/requirements.txt

# Replace V (slug without .ttl) and U (ConceptScheme CURIE), per the table above.
# Run each vocab in its own cache for isolation.
V=GeochemAnalyticalMethod
U=meth:method
SUBDIR=geochemistry
mkdir -p testoutput/local_run
rm -f cache/vocabularies.db
.venv/Scripts/python.exe tools/vocab.py --verbosity ERROR -s cache/vocabularies.db load "$SUBDIR/$V.ttl" "$U"
PYTHONIOENCODING=utf-8 .venv/Scripts/python.exe tools/vocab2mdCacheV2.py cache/vocabularies.db "$U" > "testoutput/local_run/$V.md"
quarto render "testoutput/local_run/$V.md" -t html
```

`PYTHONIOENCODING=utf-8` is a Windows-only workaround (cp1252 stdout can't encode e.g. `≥`). The Ubuntu runner uses UTF-8 by default.

**Expected stderr:** one `pkg_resources is deprecated` warning from `rdflib_sqlalchemy` — mitigated but not eliminated by the `setuptools<81` pin. Anything else probably matters.

**Sanity check:** `grep -c "^## " testoutput/local_run/$V.md` — should be ≥ 1 (number of top-level concept-scheme sections). Empty output means `getVocabRoot` returned nothing.

## Docker verification (Option B — matches the deployed action)

```bash
docker build -t astromat-vocab .
# Example: run the geochemistry workflow's action step locally
docker run --rm \
  -e INPUT_ACTION=docs \
  -e INPUT_PATH=/app \
  -e INPUT_VOCABDIR=geochemistry \
  -e INPUT_INPUTTTL='GeochemAnalyticalMethod|onegctechniquesastromatv4' \
  -e INPUT_INPUTVOCABURI='meth:method|meth:method' \
  -v "/$(pwd)/docs://app/docs" \
  astromat-vocab
```

The `//` prefix on the volume path is a Git-Bash-on-Windows workaround; drop it on Linux/macOS. Output is root-owned (the container runs as root); the actual workflow [`sudo chown`s `docs/`](.github/workflows/process_geochemistry_vocab.yml) before staging.

## Divergences from upstream `vocabularyTemplate`

The [2026-04-23 upstream PR](https://github.com/isamplesorg/vocabularyTemplate/pull/3) back-ported most generally-applicable fixes; the items below are Astromat-specific and intentionally not in the template:

1. **Multi-subdirectory layout.** `Dockerfile` COPYs each vocab subdir (`./geochemistry`, `./ETmaterials`, `./instrumentAll`, `./instruments`) instead of a single `./vocabulary`. New subdirs need a matching `COPY` line.
2. **`cache/` is gitignored and not committed.** `Dockerfile` has no `COPY ./cache ./cache`; `_reset_cache_db` in `github_action_main.py` creates the directory inside the container at runtime. The upstream template still commits `cache/` back to main after each run (stale DB from the previous run gets COPY'd at build time) — we don't.
3. **`.dockerignore` with `.github` exception.** Excludes `**/html`, `**/archive`, spreadsheets, PDFs, etc. from the build context. Do **not** add `.github` to the ignore list — `Dockerfile` needs to COPY `.github/actions/github_action_main.py`.
4. **Per-subdir workflow files** (one per subdirectory) rather than one `process_vocab.yml`. The `vocabdir` input (which we also contributed to the upstream template in PR #3) selects the target at dispatch time.
5. **Landing-page workflow** [`publish_landing_page.yml`](.github/workflows/publish_landing_page.yml) with `clean: false` — owns `docs/readme.md` on `gh-pages` without wiping per-subdir content deployed by the other workflows.
6. **`root`-owned output handling.** Each per-subdir workflow runs `sudo chown -R` over `docs/` before its own staging step (the action container runs as root, the runner steps as the non-root runner user).

## Things not to touch

- `.claude/` — Claude Code session/agent state. Excluded from git and Docker.
- `.idea/` and `*.project` — JetBrains / Eclipse IDE state if they appear in the working tree; pre-existing and not yours to commit.
- Files tagged `-SMR-Samsung.*` or similar host-tagged names — owner's local experiments on another machine.
- Pre-existing staged/pending deletions and untracked files you didn't introduce — leave for the owner to commit separately (see `feedback_do_not_stage_in_progress` memory entry).

## Known gaps

- `<http://w3id.org/def/mmisw/models/ontology>` in `instruments/mmisw-models.ttl` has no `skos:prefLabel`, so the generated landing-page title for that vocab is the fallback "ConceptScheme" rather than something descriptive. Cosmetic only; fix by adding one line to the scheme block.
- The Windows cp1252 stdout encoding trips the local Option-A `vocab2mdCacheV2.py` on files containing characters like `≥`. Workaround is `PYTHONIOENCODING=utf-8`. Not a problem on the Linux runner.
