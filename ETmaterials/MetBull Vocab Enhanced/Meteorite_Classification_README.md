# Meteorite Classification Database: Material-First Hierarchy v1.0

**Version:** 1.0  
**Last Updated:** April 14, 2026  
**Database File:** `Meteorite_Classification_MaterialFirst v1.0.csv`  
**Prepared by:** Ruolin Deng  
**Total Meteorites:** 85,701

---

## Table of Contents

1. [Overview](#overview)
2. [Database Structure](#database-structure)
3. [Column Descriptions](#column-descriptions)
4. [Classification Parameters](#classification-parameters)
5. [Data Quality & Curation](#data-quality--curation)
6. [Technical Notes](#technical-notes)
7. [References & Resources](#references--resources)
8. [Version History](#version-history)


---

## Overview

This database contains a hierarchical classification of 85,701 meteorites from the Meteorite Bulletin Database (MetBull).

### a. Key Features

- **4-level hierarchical structure**: Material → Type → (Class →) Group → Subgroup
- **Genetic relationships preserved** via Parent Body and Clan labels
- **Human-readable explanations** for all classification suffixes and abbreviations
- **Meteorite exclusive**: Non-meteorite entries (pseudometeorites, impact craters, terrestrial rocks) removed from original MetBull glossary

---


## Database Structure

### a. File Format
- **Format:** CSV (comma-separated values)
- **Encoding:** UTF-8
- **Total Rows:** 85,701 (excluding header)
- **Total Columns:** 21

### b. Hierarchical Levels

```
Material (Level 0)
  ├─ Type (Level 1)
     ├─ Class (Level 2) [when applicable]
        ├─ Group (Level 3)
           └─ Subgroup (Level 4) = recclass (recclass is the recommended classification by MetBull)

Labels (non-hierarchical, searchable):
  • Clan
  • Parent_Body
```

---

## Column Descriptions

### a. Column Order Reference

```
1.  name
2.  id
3.  recclass
4.  Material          ← Hierarchy Level 0
5.  Type              ← Hierarchy Level 1
6.  Class             ← Hierarchy Level 2 (when applicable)
7.  Group             ← Hierarchy Level 3
8.  Subgroup          ← Hierarchy Level 4 (= recclass)
9.  Classification_Details  ← Explanations
10. Clan              ← Label (searchable, not hierarchical)
11. Parent_Body       ← Label (searchable, not hierarchical)
12. fall
13. year
14. reclat
15. reclong
16. mass
17. geolocation
18. nametype
19. recclass_orig
20. GeoLocation
```

---

### a. Core Identification Columns (from original MetBull)

| Column | Description | Example | Data Type |
|--------|-------------|---------|-----------|
| `name` | Official meteorite name from MetBull | "Allende" | String |
| `id` | Unique MetBull identifier | "2" | Integer |
| `recclass` | Original MetBull classification code | "CV3" | String |

### b. Hierarchical Classification Columns (New)

| Column | Level | Description | Example | Required |
|--------|-------|-------------|---------|----------|
| `Material` | 0 | Physical composition category | "Stony" | Yes |
| `Type` | 1 | Formation/differentiation classification | "Chondrite" | Yes |
| `Class` | 2 | Chemical/compositional grouping | "Carbonaceous Chondrite" | No* |
| `Group` | 3 | Specific meteorite group | "CV" | No* |
| `Subgroup` | 4 | Detailed classification (same as recclass) | "CV3" | Yes |

*Only populated when scientifically applicable. 70,468 out of the total of 85,701 meteorites have "Class"; 78,501 out of the total of 85,701 meteorites have "Group".

### c. Label Columns (Non-Hierarchical) (New)

| Column | Description | Example | Purpose |
|--------|-------------|---------|---------|
| `Clan` | Genetic groupings of related chondrite groups | "CV-CK" | Searchable relationships |
| `Parent_Body` | Source body (when known) | "Vesta", "Mars", "Moon" | Genetic relationships |

Note: These two can potentially be combined to reduce sparcity of the dataset.

### d. Explanation Column (New)

| Column | Description | Example |
|--------|-------------|---------|
| `Classification_Details` | Human-readable explanations of suffixes, petrologic types, and abbreviations | "petrologic type 3 (unequilibrated, least metamorphosed)" |

### e. Physical & Discovery Metadata (from original MetBull)

| Column | Description | Data Type | Values |
|--------|-------------|-----------|--------|
| `fall` | Observed fall or later find | String | "Fell", "Found" |
| `year` | Year of fall or discovery | String/Integer | "1969", "~1920 a" |
| `reclat` | Recovery latitude | Float | -33.166 |
| `reclong` | Recovery longitude | Float | -64.95 |
| `mass` | Mass in grams | Float | 100.5 |
| `geolocation` | Coordinate string | String | "(-33.166, -64.95)" |

### f. Legacy Metadata (from original MetBull)

| Column | Description |
|--------|-------------|
| `nametype` | Classification of name type |
| `recclass_orig` | Original recclass before any modifications |
| `GeoLocation` | Original geolocation field |

---

## Classification Parameters

### a. Material

| Material | Count | Percentage | Description |
|----------|-------|------------|-------------|
| **Stony** | 78,446 | 91.5% | Silicate-dominated meteorites |
| **Iron** | 1,442 | 1.7% | Iron-nickel metal dominated |
| **Stony-iron** | 612 | 0.7% | Mixed silicate and metal |
| **Unknown** | 5,201 | 6.1% | Unclassified or uncertain material |

### b. Type (14 total)

| Type | Count | Material | Description |
|------|-------|----------|-------------|
| **Chondrite** | 70,919 | stony | Primitive, unmelted meteorites with chondrules |
| **Achondrite** | 4,895 | stony | Differentiated stony meteorites (no chondrules) |
| **Primitive achondrite** | 1,180 | stony | Partially melted/residual meteorites |
| **Ungrouped stony** | 1,385 | stony | Stony meteorites that don't fit existing groups |
| **Relict stony** | 67 | stony | Fragmented/altered stony meteorites |
| **Differentiated iron** | 761 | iron | Iron meteorites from differentiated parent bodies |
| **Primitive iron** | 392 | iron | IAB complex (primitive iron with silicates) |
| **Ungrouped iron** | 268 | iron | Iron meteorites that don't fit existing groups |
| **Doubtful/Discredited** | 207 | Unknown | Uncertain authenticity |
| **Relict iron** | 21 | iron | Fragmented/altered iron meteorites |
| **Differentiated stony-iron** | 608 | stony-iron | Pallasites and mesosiderites |
| **Ungrouped stony-iron** | 4 | stony-iron | Unclassified stony-irons |
| **Relict unknown** | 1 | Unknown | Fragmented meteorite of unknown type |
| **Unknown** | 4,993 | Unknown | Unclassified specimens |

### c. Class (3 total)

**Class** only applies to a subset of chondrites (carbonaceous chondrites, ordinary chondrites, and enstatite chondrites, but not Group R or Group K chondrites), which covers 70,468 out of a total of 85,701 meteorites in the list.

### d. Group (61 total)

**Group** applies to all meteorites that have been properly classified to the group level, which include a total of 78,501 meteorites out of a total of 85,701 meteorites in the list.

### e. Subgroup
**Subgroup** is the same as **recclass** in the original MetBull glossary and is the lowest layer of classification.

### f. Explanatory Notes

The `Classification_Details` column provides human-readable explanations for:

### I. Petrologic Types (Metamorphic Grade)

| Type | Meaning | Explanation |
|------|---------|-------------|
| **1** | CI-like | Heavily aqueously altered |
| **2** | Aqueously altered | Significant water alteration |
| **3** | Unequilibrated | Least metamorphosed; primitive |
| **4** | Slightly metamorphosed | Beginning equilibration |
| **5** | Moderately metamorphosed | Well-equilibrated |
| **6** | Highly metamorphosed | Extensive recrystallization |
| **7** | Very highly metamorphosed | Near melting point |

**Subtypes:** Decimal values (e.g., 3.0, 3.1, ... 3.9) provide finer gradations within type 3.

### II. IAB Iron Subgroups (Chemical Classification)

| Code | Meaning | Gold (Au) | Nickel (Ni) |
|------|---------|-----------|-------------|
| **MG** | Main Group | - | - |
| **sLL** | Subgroup | Low | Low |
| **sLM** | Subgroup | Low | Medium |
| **sLH** | Subgroup | Low | High |
| **sHL** | Subgroup | High | Low |
| **sHH** | Subgroup | High | High |

### III. Breccia Types (Texture)

| Code | Meaning |
|------|---------|
| **pmict** | Polymict breccia (fragments from different sources) |
| **mmict** | Monomict breccia (fragments from same source) |
| **br** | Brecciated |
| **unbr** | Unbrecciated |
| **melt breccia** | Impact melt breccia |
| **melt rock** | Impact melt rock |
| **imp melt** | Impact melt |

### IV. Pallasite Groups

| Code | Meaning | Count |
|------|---------|-------|
| **PMG** | Main group pallasite (most common pallasites) | 77 |
| **PES** | Eagle Station group (rare, iron-rich olivine, different parent body) | 7 |

### V. Lunar Rock Types

| Abbreviation | Full Name | Description |
|--------------|-----------|-------------|
| **bas** | Basalt | Volcanic rock from lunar maria |
| **anorth** | Anorthosite | Plagioclase-rich highland rock |
| **troct** | Troctolite | Olivine-plagioclase rock |
| **nori** | Norite | Pyroxene-plagioclase rock |
| **gabbr** | Gabbro | Pyroxene-plagioclase intrusive rock |
| **feldsp** | Feldspathic | Feldspar-rich |

### VI. CV Chondrite Subtypes

| Code | Meaning | Characteristics |
|------|---------|-----------------|
| **CVox** | Oxidized CV | Higher magnetite, lower metal |
| **CVoxA** | Oxidized Allende-like | More metamorphosed, less hydrated |
| **CVoxB** | Oxidized Bali-like | More hydrated, contains pure fayalite |
| **CVred** | Reduced CV | Higher metal, lower magnetite; different parent body |

### VII. Mesosiderite Subtypes

| Type | Description |
|------|-------------|
| **A, A1-A4** | Metal-poor variants |
| **B, B1-B4** | Metal-rich variants |
| **C, C2-C3** | Intermediate metal content |

### VIII. Classification Status

| Code | Meaning |
|------|---------|
| **an** | Anomalous (fits group but differs significantly) |
| **ung** | Ungrouped (doesn't fit existing schemes) |
| **uncl** | Unclassified (not yet fully classified) |
| **prim** | Primitive |

---

## Data Quality & Curation

### a. Removed Entries (489 total)

The following non-meteorite entries were removed from the original MetBull dataset:

| Category | Count | Description |
|----------|-------|-------------|
| **Impact Crater** | 190 | Geographic locations, not specimens |
| **Terrestrial rock** | 228 | Confirmed Earth rocks |
| **Pseudometeorite** | 71 | Terrestrial rocks mistaken for meteorites |

### b. Data Quality Notes

- **Classification_Details coverage:** 100% of meteorites (all meteorites now have explanations or are simple enough not to need them)
- **Uncertain classifications:** Petrologic types with "(?)notation (e.g., H(5?), LL6(?)) are preserved and explained
- **Completeness:** Material and Type fields are populated for all meteorites; Class is only populated when scientifically applicable

---

## Technical Notes

### a. For Database Implementation

1. **Primary Key:** Use `id` (MetBull unique identifier)
2. **Indexes:** Recommended on `Material`, `Type`, `Group`, `Parent_Body`, `Clan` for fast filtering
3. **Full-Text Search:** Index `Classification_Details` for detailed suffix/explanation searches
4. **Hierarchical Queries:** Use Material → Type → Class → Group → Subgroup for drill-down interfaces

### b. For Web Interface Design

**Recommended Filtering UI:**

1. **Level 0:** Material dropdown (4 options: stony, iron, stony-iron, Unknown)
2. **Level 1:** Type dropdown (populated based on selected Material)
3. **Level 2:** Class dropdown (only shown when applicable)
4. **Level 3:** Group dropdown
5. **Facet Filters:** Parent Body, Clan (independent of hierarchy)
6. **Search Bar:** Free-text search across all classification parameters (`Material`, `Type`, `Group`, `Parent_Body`, `Clan`)

**Tree View:** Display hierarchical counts:
```
Stony (78,446)
├─ Chondrite (70,919)
│  ├─ Ordinary Chondrite (66,383)
│  │  ├─ H (24,163)
│  │  ├─ L (23,547)
│  │  └─ LL (18,673)
│  ├─ Carbonaceous Chondrite (3,372)
│  └─ Enstatite Chondrite (713)
...
```

## References & Resources

1. **Meteorite Bulletin Database:** https://www.lpi.usra.edu/meteor/metbull.php
2. **Weisberg et al. (2006):** "Systematics and Evaluation of Meteorite Classification" - authoritative classification scheme
3. **Scientific Classifications:**
   - IAB/IIE iron distinction: Modern classification (non-magmatic term deprecated)
   - R and K chondrites: Separate groups (Weisberg et al. 2006)
   - CV subtypes: Bonal et al. (2020) oxidized/reduced classification
   - Pallasite PMG/PES: Wasson & Choi (2003)

---

## Version History

**Version 1.0 (April 14, 2026)**
- Initial release
- 85,701 meteorites from MetBull (February 2026 export)
- Material-First hierarchy implemented
- All non-meteorite entries removed
- Classification_Details explanations added for all suffixes

---
