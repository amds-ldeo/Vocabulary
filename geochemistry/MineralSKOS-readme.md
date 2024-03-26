#  Mineral concept vocabulary

mineralSKOS.ttl contains a SKOS concept scheme for mineral species. The original version of this vocabulary is the GSO-Geologic-Mineral module in the GSO vocabulary (Brodaric and Richard, 2021). This vocabulary is implemented as an OWL ontology, with classes defined in the framework of the GSO ontology. This module was compiled by scraping Wikipedia in October, 2020, and merging with a data dump from the RRUFF databasee in 2019-05. Properties associated with mineral species gathered in this initial scrape include:

- chemistryelements -- RRUFF, pipe-delimited ("|") list of elements present in the mineral formula, using standard element abbreviations.
- crystalsystem -- RRUFF, crystal system for the mineral.
- handbookofmineralogyurl -- Wikipedia; link to web page for mineral in Handbook of Mineralogy web site.
- imachemistry -- RRUFF, html-encoded chemical formula, using e.g. <sub></sub> to represent subscripts.
- imanumber -- RRUFF, International Mineralogical Association registration number for the mineral
- imastatus -- RRUFF, International Mineralogical Association status: {Approved, Grandfathered, Pending publicationon, Questionable mineral species, Redefined, Renamed }
- iupacchemname -- wikipedia, included in rdfs comment.
- mindatid --  extract from mindaturl, prefix 'min-' and integer id value.
- mindaturl -- wikipedia, URL to get MinDat landing web page for the mineral.
- rruffchemistry -- RRUFF
- rruffids -- RRUFF, a list of identifiers for specimens with analytical data in the RRUFF database
- rruffnamehtml -- RRUFF. The name of the mineral URL-encoded to display non-base ASCII characters
- rruffnameplain -- RRUFF.  Name of the mineral with ASCII characters substituted for special characters
- statusnotes -- RRUFF. Typical a citation for an original publication about the mineral, with some other notes about name updates etc. 
- strunzcodeV10 -- wikipedia, extracted from skos:definition in wikipedia dump.
- strunzlabel --  correlate code to strunz classification
- webmineralurl -- wikipedia
- wikipediadate -- wikipedia, date in the skos definition.
- Structuralgroup -- RRUFF field, not sure where this classification is defined
- fleischersgroup -- RRUFF, group classifcation from Black, M.E. "Fleischer's Glossary of Mineral Species", not sure which edition (2014? or 2018?)

A flat list of several thousand mineral species is not particularly useful. An initial attempt to introduce some hierarchy and organization by manually adding a few mineral group classes in the mineral module during GSO development, e.g. for feldspar, mica, apatite, and clay minerals. It was clear that this could not scale, and the effor was tabled for the version one release of GSO. 

In the intervening years, MinDat has implemented a publicly accessible API (see https://api.mindat.org/schema/redoc/), and assigned identifiers to the registered items in their database. This has enable a more automated process to generate a hierarchical SKOS based vocabulary, using the mineral groups defined in MinDat, and the assignment of mineral to classes in the Strunz-mindat (2024) Classification. "This classification is based on the Nickel-Strunz 9th Edition (2001), expanded on by Jim Ferraiolo and others, and now extended and maintained by mindat.org" (https://www.mindat.org/strunz.php). 

The MinDat database was queried to extract all the mineral groups defined there (entrytype = 5), and then queried for all the mineral species with links to a group if they are associated with one; these are represented using skos:broader links.  A vocabulary of the Strunz classes was established with identifiers for each Strunz Class. Minerals that are not members of a group are linked to the  Strunz class with skos:broader. A group is assigned to the most specific Strunz class that includes all members of the group. Some groups include minerals from different Strunz classes, in which case skos:broader triples link the mineral to the group and its specific Strunz class. Note that the vocabulary hasn't been reviewed to check that all these links were created. 

The long-form identifiers for the minerals were calculated and used to generate MinDatURIs, linked to the mineral skos concept with skos:exactMatch.  ExactMatch triples also link mineral classes to the mineral vocabulary developed by the Geological Survey of Queensland (see https://github.com/geological-survey-of-queensland/vocabularies/blob/master/vocabularies-gsq/minerals.ttl).  

Locality counts were calculated by summing localities for all minerals in each group.  Note that because more that one mineral in a group might occur at a locality, a locality might be counted more than once in the context of a group.  The normalizedcount property was calculated for some groups; a python code used the API to gather all the localities in a list,remove duplicate values in the list ('list(set(localities))' function) and count the unique values. Comparing the normalizedcount values to the localitycount values gives an indication of typical locality duplication for groups. 

After processing and cleaning the vocabulary 5165 mineral classes are included in the vocabulary, 602 groups (including a few solid-solution series labeled as groups here...), and 437 Strunz classes. 

Properties added during the 2024 updates to the vocabular are:

- gcmin:localitycount -- count of localities reported for all minerals in a group or Strunz clast; count might include duplicate localities
- skos:exactMatch -- URI for corresponding MinDat Mineral or Geological Survey or Queensland mineral.  The Mindat URIs resolve to the html landing page for the mineral.
- gcmin:normalizedcount -- count of localities reported for minerals in a group, with duplicate localities removed. 
- schema:additionalType -- simple field to distinguish mineral groups from Strunz Classes. Mineral 'species' do not have an additionalType property. 

# Why?

This vocabulary brings information from various sources together, most prominently the MinDat database. The number of mineral species defined there is far too large to generate useful mineral pick lists for populating rock descriptions. The intention here is to provide a SKOS vocabulary with sufficient additional properties sufficient to filter the 5165 mineral classes to generate a skos collection with the minerals needed for a particular application.   Next steps in this process would be to generate SKOS collections for common rock-forming minerals (perhaps based on Deer, Howie and Zussman), minerals common in porphyry copper deposits, minerals found in meteorites,  minerals associated with different metamorphic facies or grades, etc. 

# References
H. Strunz and E.H. Nickel. Strunz Mineralogical Tables, 9th Edition. Berlin and Stuttgart (E. Schweizerbart’sche Verlagsbuchhandlung). 2001, 870 pp. Price €148.00 (US$142.00). ISBN 3 510 65188 X.