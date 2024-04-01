import os
import pytest
from tools import navocab


@pytest.fixture()
def test_01():
    source = "data/test_01.ttl"
    dest = "data/test.db"
    v = navocab.Vocabulary(storage_uri=f"sqlite:///{dest}")
    v.load(source)
    yield v
    os.unlink(dest)


def test_load():
    NS = {
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "owl": "http://www.w3.org/2002/07/owl#",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "obo": "http://purl.obolibrary.org/obo/",
        "geosciml": "http://resource.geosciml.org/classifier/cgi/lithology",
    }

    source = "data/test_01.ttl"
    dest = "data/test.db"
    v = navocab.Vocabulary(storage_uri=f"sqlite:///{dest}")
    v.load(source, bindings=NS)
    assert len(v) == 33
    # Loading the same content again should not add any statements
    v.load(source, bindings=NS)
    assert len(v) == 33
    os.unlink(dest)


def test_vocabularies(test_01):
    vocabs = test_01.vocabulary_list(abbreviate=False)
    assert len(vocabs) == 1
    assert str(vocabs[0]) == "https://w3id.org/isample/vocabulary/test/1/testvocabulary"
    vocabs = test_01.vocabulary_list(abbreviate=True)
    assert len(vocabs) == 1
    assert str(vocabs[0]) == "test1:testvocabulary"


def test_root(test_01):
    vocab = "https://w3id.org/isample/vocabulary/test/1/testvocabulary"
    roots = test_01.getVocabRoot(vocab)
    assert len(roots) == 1
    assert str(roots[0]) == "https://w3id.org/isample/vocabulary/test/1/rootterm"


def test_concepts(test_01):
    vocab = "https://w3id.org/isample/vocabulary/test/1/testvocabulary"
    concepts = test_01.concepts(vocab)
    assert len(concepts) == 5
    concepts = test_01.concepts()
    assert len(concepts) == 6


def test_narrower(test_01):
    root = "https://w3id.org/isample/vocabulary/test/1/rootterm"
    vocab = "https://w3id.org/isample/vocabulary/test/1/testvocabulary"
    ns = test_01.narrower(root)
    assert len(ns) == 3
    ns = test_01.narrower(root, vocab)
    assert len(ns) == 2


def test_broader(test_01):
    root = "https://w3id.org/isample/vocabulary/test/1/rootterm"
    term = "https://w3id.org/isample/vocabulary/test/1/level1b"
    ns = test_01.broader(term)
    assert len(ns) == 1
    assert str(ns[0]) == root
    ns = test_01.broader(root)
    assert len(ns) == 0


def test_match(test_01):
    res = test_01.match("foobar")
    assert len(res) == 0
    res = test_01.match("once removed")
    assert len(res) == 2
    res = test_01.match("once OR twice")
    assert len(res) == 4
