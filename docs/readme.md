# Astromat Vocabulary

Workspace for developing and maintaining vocabularies that support interoperable sample-based analytical data from astromaterials. Generated HTML views are published from the authoritative SKOS Turtle sources under the [master branch](https://github.com/amds-ldeo/Vocabulary).

## Geochemistry

Vocabularies for analytical techniques in geochemistry and cosmochemistry.

### Geochemical analytical methods

- [HTML view](geochemistry/GeochemAnalyticalMethod.html)
- [SKOS Turtle source](https://github.com/amds-ldeo/Vocabulary/blob/master/geochemistry/GeochemAnalyticalMethod.ttl)
- [ARDC Research Vocabularies Australia landing page](https://vocabs.ardc.edu.au/viewById/650)

### OneGeochemistry analytical techniques (Astromat v4)

- [HTML view](geochemistry/onegctechniquesastromatv4.html)
- [SKOS Turtle source](https://github.com/amds-ldeo/Vocabulary/blob/master/geochemistry/onegctechniquesastromatv4.ttl)

## Extraterrestrial materials

Vocabulary to classify types of meteorites and other extraterrestrial materials. Derived from Meteorite Bulletin classes (via Mindat), extended with lunar materials from Apollo return samples and links to subsuming terrestrial material classes.

### Extraterrestrial materials (Mindat)

- [HTML view](ETmaterials/ExtraterrestrialMaterialsMindat.html)
- [SKOS Turtle source](https://github.com/amds-ldeo/Vocabulary/blob/master/ETmaterials/ExtraterrestrialMaterialsMindat.ttl)

## Instruments and related vocabularies

Concept schemes describing instrument and sample-handling categories: `Instruments`, `NumericModel`, `Parameters`, `PositioningSystem`, `SampleCollection`, `SamplePreparation`, `SeismicSource`, and `mmisw-models`.

- _HTML views — pending. The `instrumentAll/*.ttl` files declare multiple ConceptSchemes per file (mix of external NERC schemes and several in-house schemes) and need a per-file "primary scheme" decision before they can be processed. `instruments/mmisw-models.ttl` needs its items retyped as `skos:Concept` before HTML generation can produce non-empty output._
- [SKOS Turtle sources (instrumentAll)](https://github.com/amds-ldeo/Vocabulary/tree/master/instrumentAll)
- [SKOS Turtle source (mmisw-models)](https://github.com/amds-ldeo/Vocabulary/blob/master/instruments/mmisw-models.ttl)

## Related

- [Minerals vocabulary](https://geosamples.github.io/vocabularies/mineralSKOS.html) (hosted in `GeoSamples/vocabularies`)
