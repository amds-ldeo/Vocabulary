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

Concept schemes describing instrument, sampling, and parameter categories compiled from the SeaDataNet/NETMAR/NERC thesauri (SDN devices L22, SDN keyword types L19, SDN keyword categories L21, EDMED DCAT themes D01, etc.). Each file's HTML is rendered by anchoring the tree at the scheme whose `skos:hasTopConcept` entries line up with the file's actual `skos:broader`/`narrower` roots — `SDNDEV/current` for six of the seven, `EDMED_DCAT_THEMES/current` for `Parameters`.

### Measurement instruments

- [HTML view](instrumentAll/Instruments.html)
- [SKOS Turtle source](https://github.com/amds-ldeo/Vocabulary/blob/master/instrumentAll/Instruments.ttl)

### Numeric models

- [HTML view](instrumentAll/NumericModel.html)
- [SKOS Turtle source](https://github.com/amds-ldeo/Vocabulary/blob/master/instrumentAll/NumericModel.ttl)

### Parameters

- [HTML view](instrumentAll/Parameters.html)
- [SKOS Turtle source](https://github.com/amds-ldeo/Vocabulary/blob/master/instrumentAll/Parameters.ttl)

### Positioning systems

- [HTML view](instrumentAll/PositioningSystem.html)
- [SKOS Turtle source](https://github.com/amds-ldeo/Vocabulary/blob/master/instrumentAll/PositioningSystem.ttl)

### Sample collection instruments

- [HTML view](instrumentAll/SampleCollection.html)
- [SKOS Turtle source](https://github.com/amds-ldeo/Vocabulary/blob/master/instrumentAll/SampleCollection.ttl)

### Sample preparation instruments

- [HTML view](instrumentAll/SamplePreparation.html)
- [SKOS Turtle source](https://github.com/amds-ldeo/Vocabulary/blob/master/instrumentAll/SamplePreparation.ttl)

### Seismic sources

- [HTML view](instrumentAll/SeismicSource.html)
- [SKOS Turtle source](https://github.com/amds-ldeo/Vocabulary/blob/master/instrumentAll/SeismicSource.ttl)

### MMISW instrument models

- [HTML view](instruments/mmisw-models.html)
- [SKOS Turtle source](https://github.com/amds-ldeo/Vocabulary/blob/master/instruments/mmisw-models.ttl)

## Related

- [Minerals vocabulary](https://geosamples.github.io/vocabularies/mineralSKOS.html) (hosted in `GeoSamples/vocabularies`)
