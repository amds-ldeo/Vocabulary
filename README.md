# Astromat Vocabulary

Workspace for developing and maintaining SKOS vocabularies that support interoperable sample-based analytical data from astromaterials. This README is the `master`-branch source reference; generated HTML views are published on the `gh-pages` branch and served at **<https://amds-ldeo.github.io/Vocabulary/>** (landing page: [`docs/readme.md`](docs/readme.md)).

## Pipeline

This repo descends from [`isamplesorg/vocabularyTemplate`](https://github.com/isamplesorg/vocabularyTemplate). SKOS Turtle files under per-topic subdirectories are processed by a Docker-based GitHub Action (Turtle → SQLite via `tools/vocab.py` → Markdown via `tools/vocab2mdCacheV2.py` → HTML via Quarto) and deployed to `gh-pages:/docs/<subdir>/`. One workflow per subdirectory:

| Workflow | Source folder | Deploys to |
|---|---|---|
| [`process_geochemistry_vocab.yml`](.github/workflows/process_geochemistry_vocab.yml) | `geochemistry/` | `gh-pages:/docs/geochemistry/` |
| [`process_etmaterials_vocab.yml`](.github/workflows/process_etmaterials_vocab.yml) | `ETmaterials/` | `gh-pages:/docs/ETmaterials/` |
| [`process_instrumentall_vocab.yml`](.github/workflows/process_instrumentall_vocab.yml) | `instrumentAll/` | `gh-pages:/docs/instrumentAll/` |
| [`process_instruments_vocab.yml`](.github/workflows/process_instruments_vocab.yml) | `instruments/` | `gh-pages:/docs/instruments/` |
| [`publish_landing_page.yml`](.github/workflows/publish_landing_page.yml) | `docs/readme.md` | `gh-pages:/docs/readme.md` |

All vocabulary workflows are manually dispatched (`workflow_dispatch`). The landing-page workflow runs automatically when `docs/readme.md` changes on `master`.

See [`AGENTS.md`](AGENTS.md) for maintainer/contributor/agent notes — adding a new vocabulary, running the pipeline locally without Docker, per-subdirectory caveats, and divergences from the upstream template.

## Geochemistry

Vocabularies for analytical techniques in geochemistry and cosmochemistry.

### Geochemical analytical methods

Vocabulary of analytical techniques for analyzing Earth, astronomic, and planetary materials.

- [HTML view](https://amds-ldeo.github.io/Vocabulary/geochemistry/GeochemAnalyticalMethod.html)
- [ARDC Research Vocabularies Australia landing page](https://vocabs.ardc.edu.au/viewById/650)
- [SKOS Turtle source](https://github.com/amds-ldeo/Vocabulary/blob/master/geochemistry/GeochemAnalyticalMethod.ttl)

### OneGeochemistry analytical techniques (Astromat v4)

- [HTML view](https://amds-ldeo.github.io/Vocabulary/geochemistry/onegctechniquesastromatv4.html)
- [SKOS Turtle source](https://github.com/amds-ldeo/Vocabulary/blob/master/geochemistry/onegctechniquesastromatv4.ttl)

Earlier drafts (`GeoXAnalyticalTechnique.ttl`, `AnalyticalTechnique.ttl`, PoolParty v2/v3) are preserved under [`geochemistry/archive/`](geochemistry/archive).

## Extraterrestrial materials (`ETmaterials/`)

Vocabulary to classify types of meteorites and other extraterrestrial materials. Classes based on Meteorite Bulletin (MetBull) categories extracted into Mindat, extended with Apollo lunar materials and links to subsuming terrestrial material classes.

- [HTML view](https://amds-ldeo.github.io/Vocabulary/ETmaterials/ExtraterrestrialMaterialsMindat.html)
- [SKOS Turtle source](https://github.com/amds-ldeo/Vocabulary/blob/master/ETmaterials/ExtraterrestrialMaterialsMindat.ttl)

## Instruments, parameters, and sampling (`instrumentAll/`, `instruments/`)

Concept schemes compiled from SeaDataNet/NETMAR/NERC vocabularies (SDN device categories L22, SDN keyword types L19, SDN keyword categories L21, EDMED DCAT themes D01). Each ttl is rendered by anchoring the concept tree at the scheme whose `skos:hasTopConcept` entries align with the file's `skos:broader`/`narrower` roots (`SDNDEV/current` for most; `EDMED_DCAT_THEMES/current` for `Parameters`).

- Measurement instruments — [HTML view](https://amds-ldeo.github.io/Vocabulary/instrumentAll/Instruments.html) · [source](https://github.com/amds-ldeo/Vocabulary/blob/master/instrumentAll/Instruments.ttl)
- Numeric models — [HTML view](https://amds-ldeo.github.io/Vocabulary/instrumentAll/NumericModel.html) · [source](https://github.com/amds-ldeo/Vocabulary/blob/master/instrumentAll/NumericModel.ttl)
- Parameters — [HTML view](https://amds-ldeo.github.io/Vocabulary/instrumentAll/Parameters.html) · [source](https://github.com/amds-ldeo/Vocabulary/blob/master/instrumentAll/Parameters.ttl)
- Positioning systems — [HTML view](https://amds-ldeo.github.io/Vocabulary/instrumentAll/PositioningSystem.html) · [source](https://github.com/amds-ldeo/Vocabulary/blob/master/instrumentAll/PositioningSystem.ttl)
- Sample collection instruments — [HTML view](https://amds-ldeo.github.io/Vocabulary/instrumentAll/SampleCollection.html) · [source](https://github.com/amds-ldeo/Vocabulary/blob/master/instrumentAll/SampleCollection.ttl)
- Sample preparation instruments — [HTML view](https://amds-ldeo.github.io/Vocabulary/instrumentAll/SamplePreparation.html) · [source](https://github.com/amds-ldeo/Vocabulary/blob/master/instrumentAll/SamplePreparation.ttl)
- Seismic sources — [HTML view](https://amds-ldeo.github.io/Vocabulary/instrumentAll/SeismicSource.html) · [source](https://github.com/amds-ldeo/Vocabulary/blob/master/instrumentAll/SeismicSource.ttl)
- MMISW instrument models — [HTML view](https://amds-ldeo.github.io/Vocabulary/instruments/mmisw-models.html) · [source](https://github.com/amds-ldeo/Vocabulary/blob/master/instruments/mmisw-models.ttl)

## Related vocabularies (external)

- [Minerals vocabulary](https://geosamples.github.io/vocabularies/mineralSKOS.html) (hosted in `GeoSamples/vocabularies`).

## Contributing

See [`AGENTS.md`](AGENTS.md) for operational detail: how to add a vocabulary, how to verify changes locally without Docker, and what files not to touch. Pull requests against `master`; vocabulary workflows must be re-dispatched after merge to refresh the published HTML.
