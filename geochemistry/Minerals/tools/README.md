
# Vocabulary Tools

## Installation

1. Create a python virtual environment using python3.8 or later.
2. Install the dependencies using `pip install -r requirements.txt`.

The tools can be run like:
```
python vocab.py
```

## vocab2md

Generates markdown from a SKOS vocabulary file.


## navocab

`vocab` implements tooling for navigating SKOS vocabulary definitions used in the iSamples project.

### Install

Checkout this repository:

```
git clone https://github.com/isamplesorg/navocab.git
```

Then run poetry install:

```
cd navocab
poetry install
```

### Operation

```
$ navocab --help
Usage: navocab [OPTIONS] COMMAND [ARGS]...

Options:
  -s, --store TEXT  SQLite db for vocabularies
  --verbosity TEXT  Logging level
  --help            Show this message and exit.

Commands:
  broader     Perform a depth first traversal of the vocabulary starting...
  concept     Print out a concept in JSON format.
  concepts    List the skos:Concept entities in the selected vocabulary.
  load        Load RDF from the provided local or remote URI.
  match       Perform a full text search against literal values in the...
  namespaces  List available namespaces and their prefixes.
  narrower    Perform a depth first traversal of the vocabulary starting...
  roots       Retrieve the vocabulary root term(s).
  vocabs      List the vocabulary URIs in the store.
```

#### `load` 

`navocab` keeps loaded vocabularies in an sqlite cache. To load a vocabulary, provide the local or remote address of the vocabulary turtle file. The default database name is `vocabularies.db` in the current directory.

```
navocab load https://raw.githubusercontent.com/isamplesorg/metadata/develop/src/vocabularies/sampledFeature.ttl
...
2022-10-07 10:58:30,435 navocab:INFO: Graph now has 180 statements.
```

Note: load currently issues a bunch of `SQLAlchemy.bind()` warnings. This is due to a pending update in one of the rdflib libraries.

To load all the current (2022-10-07) vocabularies and extensions:

```
navocab load known
...
2022-10-07 11:25:56,212 navocab:INFO: Graph now has 1414 statements.
```

#### Navigating

To list the available vocabularies (namespace abbreviations can be listed with the `namespaces` operation):
```
$ navocab vocabs
sf:sampledfeaturevocabulary
mat:materialsvocabulary
spec:specimentypevocabulary
ming:mineralgroupvocabulary
gmat:geomaterialsvocabulary
```

Or with full namespaces:
```
navocab vocabs -f
https://w3id.org/isample/vocabulary/sampledfeature/0.9/sampledfeaturevocabulary
https://w3id.org/isample/vocabulary/material/0.9/materialsvocabulary
https://w3id.org/isample/vocabulary/specimentype/0.9/specimentypevocabulary
https://w3id.org/isample/vocabulary/mingroup/0.9/mineralgroupvocabulary
https://w3id.org/isample/vocabulary/geomaterial/0.9/geomaterialsvocabulary
```

The vocabulary root terms:
```
$ navocab roots
sf:sampledfeaturevocabulary
  sf:anysampledfeature

mat:materialsvocabulary
  mat:material

spec:specimentypevocabulary
  spec:physicalspecimen

ming:mineralgroupvocabulary
  No root terms in this vocabulary.

gmat:geomaterialsvocabulary
  No root terms in this vocabulary.
```

Narrower terms of `spec:physicalspecimen`:

```
$ navocab narrower spec:physicalspecimen
spec:anyaggregation
  spec:anthropogenicaggregation
  spec:biomeaggregation
    spec:bundlebiomeaggregation
    spec:slurrybiomeaggregation
  spec:genericaggregation
spec:artifact
spec:biologicalspecimen
  spec:biomeaggregation
    spec:bundlebiomeaggregation
    spec:slurrybiomeaggregation
  spec:organismpart
  spec:organismproduct
  spec:wholeorganism
spec:fluidincontainer
spec:fossil
spec:othersolidobject
spec:researchproduct
  spec:analyticalpreparation
  spec:experimentalproduct
```

Finding concepts (`-c` to just list the concepts uri): 
```
navocab match oxide -c
ming:oxidemineral
ocmat:faience
mat:liquidwater
mat:anyanthropogenicmaterial
```

Matching strings in specific predicate:
```
navocab match oxide -c -p skos:prefLabel
ming:oxidemineral
```

Full results:
```
navocab match oxide -p skos:prefLabel
{
  "uri": "https://w3id.org/isample/vocabulary/mingroup/0.9/oxidemineral",
  "name": "oxidemineral",
  "label": [
    "Mineral-Oxide"
  ],
  "definition": "Includes class oxides, hydroxides, and arsenties. Oxides are 
minerals in which the oxide anion is bonded to one or more metal alloys. The 
hydroxide-bearing minerals are typically included in the oxide class. Arsenite 
minerals are very rare oxygen-bearing arsenic minerals.",
  "broader": [
    "https://w3id.org/isample/vocabulary/material/0.9/mineral"
  ],
  "narrower": []
}
```
