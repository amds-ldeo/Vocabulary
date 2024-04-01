"""
Provides a convenience wrapper for vocabularies expressed in SKOS rdf.

Part of the iSamples project.
"""
import dataclasses
import logging
import typing
import rdflib
import rdflib.namespace
import rdflib.plugins.sparql
import sqlalchemy
import logging
import logging.config

STORE_IDENTIFIER = "https://w3id.org/isample/vocabulary"
NS = {
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "obo": "http://purl.obolibrary.org/obo/",
    "geosciml": "http://resource.geosciml.org/classifier/cgi/lithology",
}
def getLogger():
    return logging.getLogger("navocab")

L = getLogger()

def skosT(term):
    return rdflib.URIRef(f"{NS['skos']}{term}")


def rdfT(term):
    return rdflib.URIRef(f"{NS['rdf']}{term}")


def rdfsT(term):
    return rdflib.URIRef(f"{NS['rdfs']}{term}")


@dataclasses.dataclass
class VocabularyConcept:
    uri: str
    name: str
    label: list[str]
    definition: str
    broader: list[str]
    narrower: list[str]
    vocabulary: str


@dataclasses.dataclass
class Vocabulary:
    uri: str
    label: str
    description: str
    extends: typing.Optional[str] = None


class VocabularyStore:
    _PFX = f"""
PREFIX skos: <{NS['skos']}>
PREFIX owl: <{NS['owl']}>
PREFIX rdf: <{NS['rdf']}>
PREFIX rdfs: <{NS['rdfs']}>
"""
    DEFAULT_FORMAT = "text/turtle"
    DEFAULT_STORE = "sqlite://"

    def __init__(
        self,
        storage_uri=DEFAULT_STORE,
        store_identifier=STORE_IDENTIFIER,
        purge_existing=False,
#        purge_existing=True  # change to true to get rid of previous loads
        ):
        self.origin = None
        self.storage_uri = storage_uri
        self.store_identifier = store_identifier
        self._g = None
        self._terms = {}
        self._litfts = ""
        self._literals = ""
        self._initialize_store(purge=purge_existing)

    def __len__(self):
        return len(self._g)

    def purge_store(self):
        """Clears out the Sqlite cache."""
        # added by SMR to enable purge
        L.debug("purge_store: purging %s", self.store_identifier)
        graph.destroy(self.storage_uri)

    def _initialize_store(self, purge=False):
        """Sets up the rdf store using an Sqlite cache."""
#        L = getLogger()
        L.debug("initialize SQLAlchemy datastore. purge:%s",purge)
        L.debug("initialize datastore %s", self.store_identifier)
        graph = rdflib.ConjunctiveGraph("SQLAlchemy", identifier=self.store_identifier)

        if purge:
            L.debug("navocab init: purging %s", self.store_identifier)
            graph.destroy(self.storage_uri)
        
        graph.open(self.storage_uri, create=True)
        ident = graph.store._interned_id
        # sqlite specific:
        # Generate a full text search index of the literal statements
        # Triggers are used to keep the FTS up to date with changes to the literal table.
        self._literals = f"{ident}_literal_statements"
        self._litfts = f"{ident}_fts"
        sql = f"""CREATE VIRTUAL TABLE IF NOT EXISTS {self._litfts} 
        USING fts5 (object, content={self._literals}, tokenize='porter unicode61');"""
        graph.store.engine.execute(sql)
        sql = f"""CREATE TRIGGER IF NOT EXISTS fts_insert AFTER INSERT ON {self._literals}
        BEGIN
            INSERT INTO {self._litfts} (rowid,object) VALUES (new.rowid, new.object);
        END;"""
        graph.store.engine.execute(sql)

        sql = f"""CREATE TRIGGER IF NOT EXISTS fts_delete AFTER DELETE ON {self._literals}
        BEGIN
            INSERT INTO {self._litfts} ({self._litfts}, rowid, object) VALUES ('delete', old.rowid, old.object);
        END;"""
        graph.store.engine.execute(sql)

        sql = f"""CREATE TRIGGER IF NOT EXISTS fts_update AFTER UPDATE ON {self._literals}
        BEGIN
            INSERT INTO {self._litfts} ({self._litfts}, rowid, object) VALUES ('delete', old.rowid, old.object);
            INSERT INTO {self._litfts} (rowid, object) VALUES (new.rowid, new.object);
        END;
        """
        graph.store.engine.execute(sql)
        self._g = graph

    def load(
        self,
        source: str,
        voc_uri: str,
        format: str = DEFAULT_FORMAT,
        bindings: typing.Optional[dict] = None,
    ):
        g_loaded = self._g.parse(source, format=format)
#        L = getLogger()
        L.info("Navocab.load.source: %s", source)

        test = self._g.namespace_manager.namespaces()
        for prefix, ns_url in test:
            L.debug(f"load prefix binding: {prefix}: {ns_url}")
            self._g.bind(prefix, ns_url)

        if bindings is not None:
            for k, v in bindings.items():
                L.debug("binding item k: %", k)
                L.debug("binding item v: %", v)
                self._g.bind(k, v)
        # Figure the broader concept vocabularies.
        # First check for extension_vocab rdfs:subPropertyOf extended_vocab
        # if not present, then compute and add it for later use.
        # What vocabulary did we just load?
        
        loaded_vocabulary = self._g.namespace_manager.expand_curie(voc_uri)
        L.debug(f"Test Loaded_vocabulary: {loaded_vocabulary}")

        if loaded_vocabulary is not None:
            L.info("Loaded vocabulary %s", loaded_vocabulary)
            q = (
                VocabularyStore._PFX
                + """SELECT ?extended
            WHERE {
                ?vocabulary rdfs:subPropertyOf ?extended .
            }"""
            )
            qres = self._g.query(q, initBindings={"vocabulary": loaded_vocabulary})
            _extended_vocab = self._result_single_value(qres, abbreviate=False)
            if _extended_vocab is not None:
                L.info("subPropertyOf Extends: %s", _extended_vocab)
                return
            # The extended vocabulary is not specified
            # Figure it by examining the broader concepts for each
            # concept in the loaded vocabulary
            q = (
                VocabularyStore._PFX
                + """SELECT ?s
            WHERE {
                ?child rdf:type skos:Concept .
                ?child skos:broader ?s .
                ?child skos:inScheme ?voc .
            }"""
            )
            qres = g_loaded.query(q,initBindings={"voc": loaded_vocabulary} )
            broader_concepts = self._one_res(qres)
            vocabs = set()
            for c in broader_concepts:
                concept = self.concept(str(c))
                if concept.vocabulary is not None:
                    vocabs.add(concept.vocabulary)
            for vocab in vocabs:
                if str(vocab) != str(loaded_vocabulary):
                    L.info("broader concept Extends: %s", vocab)
                    self._g.add((rdflib.URIRef(loaded_vocabulary), rdfsT("subPropertyOf"), rdflib.URIRef(vocab)))
                    self._g.commit()
            return
        L.warning("Loaded vocabulary does not specify skos:ConceptScheme")


    def expand_name(self, n: typing.Optional[str]) -> typing.Optional[str]:
        L.debug(f"expand name: {n}")
        if n is None:
            return n
        try:
            return self._g.namespace_manager.expand_curie(n)
        except (ValueError, TypeError):
            pass
        return n

    def compact_name(self, n:typing.Optional[str]) -> typing.Optional[str]:
        L.debug(f"compact name: {n}")
        if n is None:
            return n
        try:
            return rdflib.URIRef(n).n3(self._g.namespace_manager)
        except (ValueError, TypeError):
            pass
        return n

    def _one_res(self, rows, abbreviate=False) -> list[str]:
        res = []
        for r in rows:
            if abbreviate:
                res.append(self.compact_name(r[0]))
            else:
                res.append(r[0])
        return res

    def _result_single_value(self, rows, abbreviate=False) -> typing.Any:
#        L = getLogger()
        L.debug(f"result_single_value-count rows in query result: {len(rows)}")
        for r in rows:
            L.debug(f"VocabularyStore-result single value row: {self.compact_name(r[0])}")
        for r in rows:
            if abbreviate:
                return self.compact_name(r[0])
            return r[0]
        return None


    def namespaces(self) -> list[str, rdflib.URIRef]:
        return [n for n in self._g.namespace_manager.namespaces()]

#    def bind(self, prefix: str, uri: str, override: bool = True):
#        self._g.namespace_manager.bind(prefix, uri, override=override)
    def bind(self, prefix: str, uri: str, replace: bool = True):
        self._g.namespace_manager.bind(prefix, uri, replace=replace)

    def query(self, q, **bindings):
        sparql = rdflib.plugins.sparql.prepareQuery(
                VocabularyStore._PFX + q)
        qres = self._g.query(sparql, initBindings=bindings)
        return qres

    def vocabulary_list(self, abbreviate: bool = True) -> list[str]:
        """List the vocabularies in the provided graph"""
        q = (
            VocabularyStore._PFX
            + """SELECT ?s
        WHERE {
            ?s rdf:type skos:ConceptScheme .
        }"""
        )
        qres = self._g.query(q)
        return self._one_res(qres, abbreviate=abbreviate)

    def vocabularies(self, abbreviate:bool=True)->list[Vocabulary]:
        q = (
            VocabularyStore._PFX
            + """SELECT ?vocabulary ?label ?description ?extends
        WHERE {
            ?vocabulary rdf:type skos:ConceptScheme .
            ?vocabulary rdfs:label ?label .
            OPTIONAL {?vocabulary skos:definition ?description .} .
            OPTIONAL {?vocabulary rdfs:subPropertyOf ?extends .} .
        }"""
        )
        qres = self._g.query(q)
        for row in qres:
            _ext = row[3]
            if _ext is not None:
                if abbreviate:
                    _ext = self.compact_name(_ext)
            yield(Vocabulary(
                uri=str(self.compact_name(row[0]) if abbreviate else row[0]),
                label=str(row[1]),
                description=str(row[2]),
                extends=str(_ext) if _ext is not None else None
            ))


    def getVocabRoot(self, v: str, abbreviate: bool = False) -> list[str]:
        """Get top concept of the specific vocabulary.

        v is the URI of the vocabulary
        """
        try:
            v = self._g.namespace_manager.expand_curie(v)
        except (ValueError, TypeError):
            pass
        q = rdflib.plugins.sparql.prepareQuery(
            VocabularyStore._PFX
            + """SELECT ?s
        WHERE {
            ?s skos:topConceptOf ?vocabulary .
        }"""
        )
        qres = self._g.query(q, initBindings={"vocabulary": v})
        return self._one_res(qres, abbreviate=abbreviate)

    def concepts(
        self,
        v: typing.Optional[str] = None,
        abbreviate: bool = False
    ) -> list[str]:
        """List the concept URIs in the specific vocabulary.

        Returns a list of the skos:Concept instances in the specified vocabulary
        as it exists in the current graph store.
        """
        try:
            v = self._g.namespace_manager.expand_curie(v)
        except (ValueError, TypeError):
            pass

        if v is None:
            q = (
                VocabularyStore._PFX
                + """SELECT ?s
            WHERE {
                ?s rdf:type skos:Concept .
            }"""
            )
            qres = self._g.query(q)
        else:
            q = (
                VocabularyStore._PFX
                + """SELECT ?s
                WHERE {
                    ?s skos:inScheme ?vocabulary .
                    ?s rdf:type skos:Concept .
                }"""
            )
            qres = self._g.query(q, initBindings={"vocabulary": v})
        return self._one_res(qres, abbreviate=abbreviate)

    def objects(self, subject: str, predicate: str) -> list[str]:
        q = rdflib.plugins.sparql.prepareQuery(
            VocabularyStore._PFX
            + """SELECT ?o
        WHERE {
            ?subject ?predicate ?o .
        }"""
        )
        qres = self._g.query(
            q, initBindings={"subject": subject, "predicate": predicate}
        )
        res = []
        for row in qres:
            v = row[0]
            v = str(v).strip()
            if len(v) > 0:
                res.append(v)
        return res

    def broader(self, concept: str, v: typing.Optional[str] = None, abbreviate: bool = False) -> list[str]:
        concept = self.expand_name(concept)
        if v is None:
            q = rdflib.plugins.sparql.prepareQuery(
                VocabularyStore._PFX
                + """SELECT ?s
            WHERE {
                ?child skos:broader ?s .
            }"""
            )
            qres = self._g.query(q, initBindings={"child": concept})
        else:
            v = self.expand_name(v)
            q = rdflib.plugins.sparql.prepareQuery(
                VocabularyStore._PFX
                + """SELECT ?s
            WHERE {
                ?s skos:inScheme ?vocabulary .
                ?child skos:broader ?s .
            }"""
            )
            qres = self._g.query(q, initBindings={"vocabulary": v, "child": concept})
        res = []
        # Should only ever be a single broader term in a well constructed taxonomy,
        # but who knows how well these things are constructed?
        return self._one_res(qres, abbreviate=abbreviate)

    def narrower(
        self, concept: str, v: typing.Optional[str] = None, abbreviate: bool = False
    ) -> list[str]:
        concept = self.expand_name(concept)
        if v is None:
            q = rdflib.plugins.sparql.prepareQuery(
                VocabularyStore._PFX
                + """SELECT ?s
            WHERE {
                ?s skos:broader ?parent .
            }"""
            )
            qres = self._g.query(q, initBindings={"parent": concept})
        else:
            v = self.expand_name(v)
            q = rdflib.plugins.sparql.prepareQuery(
                VocabularyStore._PFX
                + """SELECT ?s
            WHERE {
                ?s skos:inScheme ?vocabulary .
                ?s skos:broader ?parent .
            }"""
            )
            qres = self._g.query(q, initBindings={"vocabulary": v, "parent": concept})
        return self._one_res(qres, abbreviate=abbreviate)

    def vocab_tree(self, v: str):
        """
        Get the list of vocabularies progressively broader than vocabulary v.

        This is a bit messy. The approach is to get a concept of v,
        then for each broader concept, add its vocab to the list.

        """
        def _broader(v, c, level=0, max=100):
            ns = self.broader(c, v, False)
            for n in ns:
                yield(self.concept(n))
                if level < max:
                    _broader(v, n, level=level + 1, max=max)

        # Maximum number of concept hierarchies to examine
        MAX_TO_CHECK = 5
        vocab = str(self.expand_name(v))
        n_checked = 0
        vocabs = [vocab, ]
        for _concept in self.concepts(vocab):
            for _c in _broader(None, _concept, level=0, max=100):
                if _c.vocabulary is not None:
                    _vocab = str(_c.vocabulary)
                    if _vocab not in vocabs:
                        vocabs.append(_vocab)
            n_checked += 1
            if n_checked > MAX_TO_CHECK:
                break
        vocabs.reverse()
        return vocabs


    def concept(self, term: str):
        term = self.expand_name(term)
        if "#" in term:
            ab = term.split("#")
        else:
            ab = term.split("/")
        name = ab[-1]
        # _v = self.objects(term, skosT("inScheme"))[0]
        _v = None
        labels = self.objects(term, skosT("prefLabel"))
        labels += self.objects(term, skosT("label"))
        tmp = self.objects(term, skosT("definition"))
        definition = "\n".join(tmp)
        broader = self.objects(term, skosT("broader"))
        narrower = self.narrower(term, _v)
        vocabulary = self.objects(term, skosT("inScheme"))
        if len(vocabulary) >0:
            vocabulary = vocabulary[0]
        else:
            vocabulary = None
        return VocabularyConcept(
            uri=str(term),
            name=name,
            label=labels,
            definition=definition.strip(),
            broader=broader,
            narrower=narrower,
            vocabulary = vocabulary
        )

    def match(
        self, q, predicate=None, abbreviate: bool = False
    ) -> list[tuple[rdflib.URIRef, rdflib.URIRef, str, float]]:
        """
        Return a list of subject,predicate,object,rank that match the provided FTS query.

        Rank is the sqlite FTS rank property, https://www.sqlite.org/fts5.html#the_bm25_function
        and indicates the relevance of the result to the query. Lower values (i.e. more negative)
        indicate higher relevance.
        """
        where_clause = f"{self._litfts} MATCH :query"
        if predicate is not None:
            predicate = self.expand_name(predicate)
            where_clause = f"a.predicate = :predicate AND {where_clause}"
        sql = sqlalchemy.text(
            f"""SELECT a.subject, a.predicate, a.object, b.rank FROM {self._literals} AS a
            INNER JOIN {self._litfts} AS b on a.rowid=b.rowid 
            WHERE {where_clause} ORDER BY rank;"""
        )
        rows = self._g.store.engine.execute(sql, {"query": q, "predicate": predicate})
        result = []
        for row in rows:
            if abbreviate:
                result.append((
                    rdflib.URIRef(row[0]).n3(self._g.namespace_manager),
                    rdflib.URIRef(row[1]).n3(self._g.namespace_manager),
                    str(row[2]),
                    row[3]
                ))
            else:
                result.append(
                    (rdflib.URIRef(row[0]), rdflib.URIRef(row[1]), str(row[2]), row[3])
                )
        return result

    def resolve(self, uri: str):
        """
        WIP
        Lookup the specified uri.
        If not present in the graph try and retrieve from uri as URL.
        """
        # look for the object with iri in the current graph first
        res = []
        for t in self._g.predicate_objects(rdflib.URIRef(uri)):
            res.append(t)
        if len(res) > 0:
            return res
        g = rdflib.ConjunctiveGraph()
        self._g += g.parse(uri)
        for t in self._g.predicate_objects(rdflib.URIRef(uri)):
            res.append(t)
        return res

    def asDict(self, _index=0):
        """Dict representation of self that can be serialized to linkml yaml for an enum.

        """
        _name = self.vocabulary_list(abbreviate=False)[_index]
        res = {
            _name:{
                "description":"",
                "permissable_values": []
            }
        }
        qres = self.query("SELECT ?o WHERE {?subject ?predicate ?o.}", subject=_name, predicate="skos:definition")
        L.debug(f"Dict representation of self: %", qres)
        res[_name]["description"] = self._one_res(qres)
        return res
