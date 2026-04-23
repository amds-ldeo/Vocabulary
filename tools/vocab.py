"""

"""

import dataclasses
import json
import logging
import logging.config
import sys
import click
#import yaml
from rdflib import URIRef
from rdflib.store import Store

import navocab

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s %(name)s:%(levelname)s: %(message)s",
            "dateformat": "%Y-%m-%dT%H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "standard",
            "stream": "ext://sys.stderr",
        },
    },
    "loggers": {
        "": {
            "handlers": [
                "console",
            ],
            "level": "INFO",
            "propogate": False,
        },
    },
}

LOG_LEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "WARN": logging.WARNING,
    "ERROR": logging.ERROR,
    "FATAL": logging.CRITICAL,
    "CRITICAL": logging.CRITICAL,
}

# CURRENT_ISAMPLES_VOCABULARIES = [
#     "https://raw.githubusercontent.com/isamplesorg/metadata/develop/src/vocabularies/sampledFeature.ttl",
#     "https://raw.githubusercontent.com/isamplesorg/metadata/develop/src/vocabularies/materialType.ttl",
#     "https://raw.githubusercontent.com/isamplesorg/metadata/develop/src/vocabularies/materialSampleType.ttl",
#     "https://raw.githubusercontent.com/isamplesorg/metadata/develop/src/vocabularies/mineralGroup.ttl",
#     "https://raw.githubusercontent.com/isamplesorg/metadata/develop/src/vocabularies/iSamplesGeoMaterials.ttl",
#     "https://raw.githubusercontent.com/isamplesorg/metadata/develop/src/vocabularies/rockSedimentExtension.ttl",
#     "https://raw.githubusercontent.com/isamplesorg/metadata/develop/src/vocabularies/OpenContextMaterial.ttl",
# ]
CURRENT_ISAMPLES_VOCABULARIES = [
    # "https://raw.githubusercontent.com/isamplesorg/metadata_profile_earth_science/main/vocabulary/earthenv_material_extension_mineral_group.ttl",
    # "https://raw.githubusercontent.com/isamplesorg/metadata_profile_earth_science/main/vocabulary/earthenv_material_extension_rock_sediment.ttl",
    # "https://raw.githubusercontent.com/isamplesorg/metadata_profile_earth_science/main/vocabulary/earthenv_sampled_feature_role.ttl",
    # "https://raw.githubusercontent.com/isamplesorg/metadata_profile_earth_science/main/vocabulary/earthenv_specimen_type.ttl"
]

def getLogger():
    return logging.getLogger("navocab")


def getDefaultVocabulary(vs, abbreviate=False):
    L = getLogger()
    vocabs = vs.vocabulary_list(abbreviate=abbreviate)
    vocabulary = vocabs[0]
    if len(vocabs) > 1:
        L.warning("More than one vocabulary in store. Using: %s", vocabulary)
    return vocabulary


@click.group()
@click.pass_context
@click.option("-s", "--store", default="vocabularies.db", help="SQLite db for vocabularies" )
@click.option("--verbosity", default="INFO", help="Logging level")
def main(ctx, store, verbosity) -> int:
    verbosity = verbosity.upper()
    logging_config["loggers"][""]["level"] = verbosity
    logging.config.dictConfig(logging_config)
    L = getLogger()
    ctx.ensure_object(dict)
    store_uri = f"sqlite:///{store}"
    L.debug("Using store at: %s", store_uri)
    ctx.obj["store"] = navocab.VocabularyStore(storage_uri=store_uri, purge_existing=False)
    return 0

@main.command("purgeStore")
@click.pass_context
def purgeStore(ctx):
    _s = ctx.obj["store"]
    _s.purge_store()

@main.command("load")
@click.pass_context
@click.argument("inputf")
@click.argument("voc_uri")
def load(ctx, inputf, voc_uri):
    """Load RDF from the provided local or remote URI."""
    import warnings
    L = getLogger()
    _s = ctx.obj["store"]
#
    L.debug(f"input file to load: {inputf}")
#    if inputf =="known":
#        uris = CURRENT_ISAMPLES_VOCABULARIES
#    for aninputf in uris:
    L.info("Loading URI: %s", inputf)
    # stifle cascade of warnings from sqlalchemy about 
    # 'caught a TypeError, retrying call to <class 'rdflib_sqlalchemy.store.SQLAlchemy'>.bind without override'
    _s.load(inputf,voc_uri)
    L.info("Graph now has %s statements.", len(_s._g))


@main.command("namespaces")
@click.pass_context
@click.option(
    "-b",
    "--bind",
    default=None,
    help="Bind new prefix to namespace, like: 'eg=https://example.com/'",
)
def namespaces(ctx, bind):
    """List available namespaces and their prefixes."""
    L = getLogger()
    _s = ctx.obj["store"]
    if bind is not None:
        p_uri = bind.split("=", 1)
        if len(p_uri) < 2:
            L.error("namespace.bind: Insufficient parameters: %s", bind)
            L.info("namespace.bind: Format the bind request like 'prefix=namspace'")
            return
        _s.bind(p_uri[0].strip(), p_uri[1].strip())
    for prefix, uri in _s.namespaces():
        print(f"{prefix} = {str(uri)}")


@main.command("vocabs")
@click.pass_context
@click.option(
    "-f", "--full-uri", is_flag=True, help="Show expanded URIs instead of prefixed"
)
@click.option(
    "-r","--roots-only", is_flag=True, help="List only the root vocabulary URIs"
)
def vocabularies(ctx, full_uri, roots_only):
    """List the vocabulary URIs in the store."""
    _s = ctx.obj["store"]

    vocabs = list(_s.vocabularies(abbreviate=(not full_uri)))
    roots = []
    for v in vocabs:
        if v.extends is None:
            roots.append(v)

    for r in roots:
        if roots_only:
            print(r.uri)
        else:
            print(f"{r.label} ({r.uri})")
            for v in vocabs:
                if v.extends == r.uri:
                    print(f"  --extend--> {v.label} ({v.uri})")

@main.command("concepts")
@click.option(
    "-v",
    "--vocabulary",
    default=None,
    help="URI of vocabulary, 'default' to load first available.",
)
@click.option(
    "-f", "--full-uri", is_flag=True, help="Show expanded URIs instead of prefixed"
)
@click.option(
    "-e","--extensions", is_flag=True, help="Include registered vocabulary extensions"
)
@click.pass_context
def concepts(ctx, vocabulary, full_uri, extensions):
    """List the skos:Concept entities in the selected vocabulary."""
    L = getLogger()
    _s = ctx.obj["store"]
    if vocabulary == "default":
        vocabulary = getDefaultVocabulary(_s, abbreviate=False)
        L.info("Loaded default vocabulary: %s", vocabulary)
    concepts = _s.concepts(vocabulary, abbreviate=(not full_uri))
    for c in concepts:
        print(f"{c}")


@main.command("roots")
@click.pass_context
@click.option(
    "-f", "--full-uri", is_flag=True, help="Show expanded URIs instead of prefixed"
)
def vocabulary_root(ctx, full_uri):
    """Retrieve the vocabulary root term(s)."""
    _s = ctx.obj["store"]
    vocabs = _s.vocabulary_list(abbreviate=(not full_uri))
    for vocab in vocabs:
        roots = _s.getVocabRoot(vocab, abbreviate=(not full_uri))
        if len(roots) > 0:
            print(f"{vocab}")
            for root in roots:
                print(f"  {str(root)}")
            print()


@main.command("broader")
@click.option(
    "-v",
    "--vocabulary",
    default=None,
    help="URI of vocabulary, 'default' to load first available.",
)
@click.option("-d", "--depth", default=-1, help="Depth to traverse (default=all)")
@click.argument("concept")
@click.option(
    "-f", "--full-uri", is_flag=True, help="Show expanded URIs instead of prefixed"
)
@click.pass_context
def broader(ctx, vocabulary, concept, depth, full_uri):
    """Perform a depth first traversal of the vocabulary starting from CONCEPT."""

    def _broader(s, v, c, indent=0, level=0, max=100):
        ns = s.broader(c, v, abbreviate=(not full_uri))
        for n in ns:
            print(f"{indent*' '}{n}")
            if level < max:
                _broader(s, v, n, indent=indent + 2, level=level + 1, max=max)

    L = getLogger()
    _s = ctx.obj["store"]
    if vocabulary == "default":
        vocabulary = getDefaultVocabulary(_s, abbreviate=(not full_uri))
        L.info("Loaded default vocabulary: %s", vocabulary)
    if depth < 1:
        depth = 100
    _broader(_s, vocabulary, concept, max=depth)


@main.command("narrower")
@click.option(
    "-v",
    "--vocabulary",
    default=None,
    help="URI of vocabulary, 'default' to load first available.",
)
@click.option("-d", "--depth", default=-1, help="Depth to traverse (default=all)")
@click.argument("concept")
@click.option(
    "-f", "--full-uri", is_flag=True, help="Show expanded URIs instead of prefixed"
)
@click.option(
    "-e", "--extensions", is_flag=True, help="Traverse vocabulary extensions"
)
@click.pass_context
def narrower(ctx, vocabulary, concept, depth, full_uri, extensions):
    """Perform a depth first traversal of the vocabulary starting from CONCEPT.

    If CONCEPT = "root", all terms starting from the vocabulary root concept
    are retrieved.
    Uses the default vocabulary if none specified.
    """

    def _narrower(s, v, c, indent=0, level=0, max=100):
        ns = s.narrower(c, v, abbreviate=(not full_uri))
        for n in ns:
            print(f"{indent*' '}{n}")
            if level < max:
                _narrower(s, v, n, indent=indent + 2, level=level + 1, max=max)

    L = getLogger()
    _s = ctx.obj["store"]
    if vocabulary == "default":
        vocabulary = getDefaultVocabulary(_s, abbreviate=(not full_uri))
        L.info("Loaded default vocabulary: %s", vocabulary)
    if concept == "root":
        concept = str(_s.getVocabRoot(vocabulary)[0])
        L.info("Using %s as root concept", concept)
    if depth < 1:
        depth = 100
    if extensions:
        vocabulary = None
    _narrower(_s, vocabulary, concept, max=depth)

@main.command("uijson")
@click.argument("vocabulary")
@click.option(
    "-e", "--extensions", is_flag=True, help="Traverse vocabulary extensions"
)
@click.pass_context
def uijson(ctx, vocabulary, extensions):
    """Render VOCABULARY as JSON suitable for inclusion in iSamples WebUI.
    """
    def _narrower(s, v, c, indent=0, level=0, max=100):
        ns = s.narrower(c, v, abbreviate=False)
        for n in ns:
            entry = _json_for_uri_ref(n, s)
            if level < max:
                for nn in _narrower(s, v, n, indent=indent + 2, level=level + 1, max=max):
                    entry["children"].append(nn)
            yield entry

    def _json_for_uri_ref(n: URIRef, s: Store):
        _c = s.concept(n)
        # TODO: use provided lang instead of assuming everything is @en
        entry = {
            "concept": str(n),
            "label": {
                "en": _c.label[0] if len(_c.label) > 0 else str(s.compact_name(n))
            },
            "children": []
        }
        return entry

    def _convert_to_ui_format(entry: dict) -> dict:
        child_dict = {
            "label": entry["label"]
        }
        ui_dict = {
            entry["concept"]: child_dict
        }
        children = []
        for child in entry["children"]:
            children.append(_convert_to_ui_format(child))
        child_dict["children"] = children
        return ui_dict

    L = getLogger()
    _s = ctx.obj["store"]
    if vocabulary == "default":
        vocabulary = getDefaultVocabulary(_s, abbreviate=False)
        L.debug("Loaded default vocabulary: %s", vocabulary)
    concept = str(_s.getVocabRoot(vocabulary)[0])
    L.debug("Using %s as root concept", concept)
    if extensions:
        vocabulary = None
    result = []
    for n in _narrower(_s, vocabulary, concept):
        result.append(n)
    root_entry = _json_for_uri_ref(URIRef(concept), _s)
    for child in result:
        root_entry["children"].append(child)

    # Note that due to the way the RDF queries are structured, if we construct the dictionaries in the format
    # the UI expects while we are iterating, the RDF query blows up.  So, keep it in one format while iterating and
    # convert when done.
    root_entry = _convert_to_ui_format(root_entry)
    print(json.dumps(root_entry, indent=2))


@main.command("concept")
@click.argument("concept")
@click.pass_context
def get_concept(ctx, concept):
    """Print out a concept in JSON format."""
    _s = ctx.obj["store"]
    c = _s.concept(concept)
    print(json.dumps(dataclasses.asdict(c), indent=2))


@main.command("match")
@click.argument("query")
@click.option("-c", "--concepts-only", is_flag=True, help="Show only the concept URIs")
@click.option(
    "-p", "--predicate", default=None, help="Match only on objects of this predicate"
)
@click.pass_context
@click.option(
    "-f", "--full-uri", is_flag=True, help="Show expanded URIs instead of prefixed"
)
def matchconcepts(ctx, query, concepts_only, predicate, full_uri):
    """Perform a full text search against literal values in the store.

    QUERY is an sqlite fts match expression
    """
    L = getLogger()
    _s = ctx.obj["store"]
    results = _s.match(query, predicate=predicate, abbreviate=(not full_uri))
    if len(results) < 1:
        L.warning("No matches")
        return
    concepts = []
    # results are ordered by relevance
    for result in results:
        concept = str(result[0])
        if concept not in concepts:
            concepts.append(concept)
    for concept in concepts:
        if concepts_only:
            print(concept)
        else:
            vt = _s.concept(concept)
            print(json.dumps(dataclasses.asdict(vt), indent=2))
            print()


@main.command("yaml")
@click.option(
    "-v",
    "--vocabulary",
    default="default",
    help="URI of vocabulary, 'default' to load first available.",
)
@click.pass_context
def toYaml(ctx, vocabulary):
    L = getLogger()
    _s = ctx.obj["store"]
    if vocabulary == "default":
        vocabulary = getDefaultVocabulary(_s, abbreviate=True)
        L.info("Loaded default vocabulary: %s", vocabulary)
    res = _s.asDict()
    print(yaml.dump(res))

if __name__ == "__main__":
    sys.exit(main())
