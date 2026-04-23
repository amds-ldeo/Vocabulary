---
comment: | 
  WARNING: This file is generated. Any edits will be lost!
format:
  html:
    ascii: true
    toc: true
    toc-depth: 4
    number-sections: true
    anchor-sections: false
    number-depth: 8
execute:
  echo: false
---

[]{#SeaDataNetDeviceThesaurus}

# **Concept scheme:** SeaDataNet Device Thesaurus

no modified date

subtitle: 

Namespace: 
[`http://vocab.nerc.ac.uk/scheme/SDNDEV/current`](http://vocab.nerc.ac.uk/scheme/SDNDEV/current)

**History**

* 2026-04-23 SMR: added skos:hasTopConcept sdnc:ICAT08 so that the vocabularyTemplate-based HTML generation can anchor the broader/narrower tree at the numeric-model category root. The base SDNDEV scheme as distributed by NERC does not list ICAT08 as a top concept; this local NumericModel.ttl export extends it solely for documentation-rendering purposes.

- [Numerical model](#icat08)
    - [Global models](#mod01)
    - [Regional models](#mod02)
    - [Atmosphere models](#mod03)
    - [Ocean models](#mod04)
    - [Coupled models](#mod05)
    - [Meteorological models](#mod06)
    - [Physical oceanographic models](#mod07)
    - [Biological and biogeochemical models](#mod08)

**Concepts**

[]{#icat08}

##  Numerical model
- Categories used in the SeaDataNet project to classify algorithmic
predications that produce datasets.
- **Alternate labels:**
SeaDataNet numerical model categories, 
numerical models, 
- Concept URI: http://vocab.nerc.ac.uk/collection/L21/current/ICAT08


[]{#mod01}

###  Global models
- Child of:
 [`ICAT08`](#ICAT08)
- Numerical models that make predictions over the whole globe.
- Concept URI: http://vocab.nerc.ac.uk/collection/L05/current/MOD01


[]{#mod02}

###  Regional models
- Child of:
 [`ICAT08`](#ICAT08)
- Numerical models that make predictions within a limited geographic
area.
- Concept URI: http://vocab.nerc.ac.uk/collection/L05/current/MOD02


[]{#mod03}

###  Atmosphere models
- Child of:
 [`ICAT08`](#ICAT08)
- Numerical models the make predictions in the atmosphere assuming
that it is a closed system that doesn't interact with the hydrosphere.
- Concept URI: http://vocab.nerc.ac.uk/collection/L05/current/MOD03


[]{#mod04}

###  Ocean models
- Child of:
 [`ICAT08`](#ICAT08)
- Numerical models the make predictions in the hydrosphere assuming
that it is a closed system that doesn't interact with the atmosphere.
- Concept URI: http://vocab.nerc.ac.uk/collection/L05/current/MOD04


[]{#mod05}

###  Coupled models
- Child of:
 [`ICAT08`](#ICAT08)
- Numerical models that make predictions in both the atmosphere and
the hydrosphere by considering both spheres as a single system.
- Concept URI: http://vocab.nerc.ac.uk/collection/L05/current/MOD05


[]{#mod06}

###  Meteorological models
- Child of:
 [`ICAT08`](#ICAT08)
- Numerical models that make predictions of weather parameters such as
air temperature, pressure, humidity and winds.
- Concept URI: http://vocab.nerc.ac.uk/collection/L05/current/MOD06


[]{#mod07}

###  Physical oceanographic models
- Child of:
 [`ICAT08`](#ICAT08)
- Numerical models that make predictions of physical oceanographic
parameters such as water body temperature, salinity, currents and
waves.
- Concept URI: http://vocab.nerc.ac.uk/collection/L05/current/MOD07


[]{#mod08}

###  Biological and biogeochemical models
- Child of:
 [`ICAT08`](#ICAT08)
- Numerical models that make predictions of biological parameters,
including ecosystem models.
- Concept URI: http://vocab.nerc.ac.uk/collection/L05/current/MOD08



