# How to build and publish the vocabulary HTML

Notes by Stephen M. Richard. Original SKOS-to-HTML tooling by Dave Vieglais for the
iSamples project (https://github.com/isamplesorg/isamplesorg.github.io), supported by
NSF award 2004815.

The authoritative vocabularies are the SKOS Turtle files on the `master` branch, under
`geochemistry/`, `ETmaterials/`, `instrumentAll/`, and `instruments/`. Edit those. The
HTML views are generated artifacts and live only on the `gh-pages` branch, under
`docs/<subdirectory>/`; never edit them by hand.

## The normal path: run the GitHub Action

Publishing is done entirely by GitHub Actions — there is nothing to install locally.

1. Commit and push your edited `.ttl` file to `master`.
2. Go to the repository's **Actions** tab.
3. Pick the workflow for the subdirectory you changed — *Process geochemistry
   vocabularies*, *Process ETmaterials vocabularies*, *Process instrumentAll
   vocabularies*, or *Process instruments vocabularies* — and press **Run workflow**.
   To rebuild everything after a wide change, run *Process all vocabularies* instead;
   it runs the four in sequence.
4. When the run finishes, the regenerated HTML is on `gh-pages` and visible at
   `https://amds-ldeo.github.io/Vocabulary/docs/<subdirectory>/<name>.html`.

The landing page (`docs/readme.md`) publishes itself: the *Publish landing page*
workflow runs automatically whenever that file changes on `master`.

### What the workflow actually does

The workflow calls the repository's own composite action (`action.yml`), which builds
the `Dockerfile` image and runs `.github/actions/github_action_main.py`. For each
vocabulary that script deletes the SQLite cache, loads the Turtle file into it with
`tools/vocab.py`, generates Quarto-flavored Markdown with `tools/vocab2mdCacheV2.py`,
and renders HTML with Quarto. The workflow then stages the output and deploys it to
`gh-pages`.

### Adding or changing a vocabulary in a workflow

Each workflow names its files in two pipe-delimited inputs that must have the same
number of entries in the same order:

- `inputttl` — Turtle file basenames, no `.ttl` extension, located in `vocabdir`.
- `inputvocaburi` — the `skos:ConceptScheme` URI for each file, written as a CURIE.

The CURIE has to be resolvable from the `@prefix` declarations inside that same Turtle
file. A file commonly declares more than one concept scheme (imported NERC schemes
alongside the in-house one); the correct choice is the scheme whose `skos:hasTopConcept`
entries are anchored in that file's own `skos:broader`/`narrower` hierarchy. Getting
this wrong produces an empty or near-empty HTML page rather than an error.

Also update the staging step's file list in the same workflow, and add the new entry to
`docs/readme.md`.

## Running it locally to debug

Useful when a vocabulary renders empty, with the wrong roots, or not at all. Requires
Python 3.8+ and a local [Quarto](https://quarto.org/docs/get-started/) install.

Set up once, from the repository root:

```bash
python -m venv .venv && .venv/Scripts/python.exe -m pip install -r tools/requirements.txt
```

Then, for each vocabulary, delete the cache database and load the Turtle file:

```bash
rm -f cache/vocabularies.db && .venv/Scripts/python.exe tools/vocab.py --verbosity ERROR -s cache/vocabularies.db load "geochemistry/GeochemAnalyticalMethod.ttl" "meth:method"
```

Generate the Markdown:

```bash
PYTHONIOENCODING=utf-8 .venv/Scripts/python.exe tools/vocab2mdCacheV2.py cache/vocabularies.db "meth:method" > testoutput/local_run/GeochemAnalyticalMethod.md
```

Render it:

```bash
quarto render testoutput/local_run/GeochemAnalyticalMethod.md -t html
```

`cache/`, `.venv/`, and `testoutput/local_run/` are gitignored. Put scratch output in
`testoutput/local_run/` — not in `docs/`, which is reserved for the published landing page.

`tools/vocab.py` is also a standalone command-line tool for inspecting a loaded
vocabulary (`vocabs`, `roots`, `concepts`, `narrower`, `match`, `namespaces`). Running
`roots` against the cache is the quickest way to find out why a page came out empty.
See `tools/README.md` for examples.

## Things that bite

- **Delete the cache database between vocabularies.** If you skip it, concepts from the
  previously loaded vocabulary leak into the next one's output. The GitHub Action does
  this automatically; local runs do not.
- **Non-base-ASCII characters in a Turtle file break the conversion.** This has been a
  persistent failure mode. Check for them first when a build fails on a file you just
  edited; the GitHub Pages step is even less tolerant of them than the Python is.
- **On Windows, set `PYTHONIOENCODING=utf-8`** when generating Markdown. The tool writes
  to stdout, and the default console encoding will mangle the output.
