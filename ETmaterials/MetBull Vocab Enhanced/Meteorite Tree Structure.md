# Meteorite Classification Structure Comparison

**Total Meteorites: 86,190**

All three structures include ungrouped meteorite reclassifications:
- Chondrite-ung (23) + Chondrite-uncl (74) → Chondrite (97 moved)
- Achondrite-ung (175) + Enst achon-ung (8) → Achondrite (183 moved)
- Achondrite-prim-ung (12) → Primitive achondrite (12 moved)
- **Total reclassified: 292 meteorites**
- **Remaining Ungrouped: 1,864** (primarily Stone-uncl: 1,385)

---

## Structure 1: Current Classification

**Hierarchy:** Type → Class → Clan → Group → Subgroup

**Additional Labels:** Parent Body (for filtering/searching)

```
All Meteorites (86,190)
│
├── Type: Chondrite (70,919)
│   ├── Class: Ordinary Chondrite (66,383)
│   │   ├── Group: H (29,754)
│   │   ├── Group: L (27,756)
│   │   ├── Group: LL (8,514)
│   │   ├── Group: L/LL (160)
│   │   ├── Group: OC (102)
│   │   ├── Group: H/L (63)
│   │   ├── Group: LL/L (30)
│   │   └── Group: L/H (4)
│   │
│   ├── Class: Carbonaceous Chondrite (3,726)
│   │   ├── Clan: CM-CO (1,570)
│   │   │   ├── Group: CO (792)
│   │   │   └── Group: CM (778)
│   │   ├── Clan: CV-CK (1,406)
│   │   │   ├── Group: CV (786)
│   │   │   └── Group: CK (620)
│   │   ├── Clan: CR (400)
│   │   │   ├── Group: CR (218)
│   │   │   ├── Group: CH (29)
│   │   │   └── Group: CB (26)
│   │   ├── Group: R (350) [no clan]
│   │   ├── Group: C3 (50) [no clan]
│   │   ├── Group: C2 (32) [no clan]
│   │   ├── Group: C-ung (13) [no clan]
│   │   ├── Group: CI (10) [no clan]
│   │   ├── Group: CL (7) [no clan]
│   │   ├── Group: C1 (5) [no clan]
│   │   ├── Group: K (4) [no clan]
│   │   ├── Group: C4 (3) [no clan]
│   │   ├── Group: C6 (2) [no clan]
│   │   └── Group: C5/6 (1) [no clan]
│   │
│   └── Class: Enstatite Chondrite (713)
│       ├── Group: E (247)
│       ├── Group: EL (241)
│       └── Group: EH (225)
│
├── Type: Achondrite (6,656)
│   ├── Clan: Vesta [Parent Body: Vesta] (3,313)
│   │   ├── Group: Eucrite (2,087)
│   │   ├── Group: Diogenite (720)
│   │   └── Group: Howardite (506)
│   │
│   ├── Clan: Lunar [Parent Body: Moon] (804)
│   │   └── Group: Lunar (804)
│   │
│   ├── Clan: Martian [Parent Body: Mars] (419)
│   │   ├── Group: Shergottite (357)
│   │   ├── Group: Nakhlite (34)
│   │   ├── Group: Martian (24)
│   │   ├── Group: Chassignite (3)
│   │   └── Group: OPX (1)
│   │
│   ├── Group: Mesosiderite (394) [no clan] [Material: stony-iron]
│   ├── Group: IIIAB (369) [no clan] [Material: iron]
│   ├── Group: IAB (308) [no clan] [Material: iron]
│   ├── Group: Pallasite (214) [no clan] [Material: stony-iron]
│   ├── Group: IIAB (155) [no clan] [Material: iron]
│   ├── Group: Aubrite (96) [no clan] [Material: stony]
│   ├── Group: IVA (94) [no clan] [Material: iron]
│   ├── Group: IAB complex (84) [no clan] [Material: iron]
│   ├── Group: IID (31) [no clan] [Material: iron]
│   ├── Group: IIE (27) [no clan] [Material: iron]
│   ├── Group: Angrite (24) [no clan] [Material: stony]
│   ├── Group: IIIE (22) [no clan] [Material: iron]
│   ├── Group: IVB (20) [no clan] [Material: iron]
│   ├── Group: IC (16) [no clan] [Material: iron]
│   ├── Group: IID (11) [no clan] [Material: iron]
│   ├── Group: IIIF (9) [no clan] [Material: iron]
│   ├── Group: IIC (8) [no clan] [Material: iron]
│   ├── Group: IIF (8) [no clan] [Material: iron]
│   ├── Group: IIG (6) [no clan] [Material: iron]
│   └── Group: IIC (2) [no clan] [Material: iron]
│
├── Type: Primitive achondrite (1,180)
│   ├── Clan: ACA-LOD [Parent Body: ACA-LOD parent] (209)
│   │   ├── Group: Lodranite (101)
│   │   ├── Group: Acapulcoite (96)
│   │   └── Group: ACA/LOD (12)
│   │
│   ├── Group: Ureilite (766) [no clan] [Parent Body: Ureilite parent]
│   ├── Group: Winonaite (105) [no clan] [Parent Body: IAB/Winonaite parent]
│   ├── Group: Brachinite (73) [no clan]
│   └── Group: Enst achon (16) [no clan]
│
├── Type: Ungrouped (1,864)
│   ├── Stone-uncl (1,385) [Material: stony]
│   ├── Iron, ungrouped (160) [Material: iron]
│   ├── Doubtful meteorite (116) [Material: unknown]
│   ├── Iron (106) [Material: iron]
│   ├── Doubtful stone (46) [Material: unknown]
│   ├── Doubtful Iron (24) [Material: unknown]
│   ├── Discredited (14) [Material: unknown]
│   ├── Stony iron (4) [Material: stony-iron]
│   ├── Doubtful OC (3) [Material: unknown]
│   ├── Iron? (2) [Material: iron]
│   ├── Doubtful achondrite (1) [Material: unknown]
│   ├── Doubtful pallasite (1) [Material: unknown]
│   ├── Doubtful eucrite (1) [Material: unknown]
│   └── Doubtful chondrite (1) [Material: unknown]
│
├── Type: Unknown (5,482)
│   ├── Unknown (4,984)
│   ├── Terrestrial rock (228)
│   ├── Impact Crater (190)
│   ├── Pseudometeorite (71)
│   ├── Chondrite-fusion crust (4)
│   ├── Fusion crust (4)
│   └── Impact melt breccia (1)
│
└── Type: Relict meteorite (89)
    ├── Relict OC (65) [Material: stony]
    ├── Relict iron (21) [Material: iron]
    ├── Relict H (1) [Material: stony]
    ├── Relict ureilite (1) [Material: stony]
    └── Relict meteorite (1) [Material: unknown]
```

**Key Features:**
- Traditional scientific structure
- Irons and stony-irons grouped under Achondrite
- Parent Body information in Clan or as label
- Most similar to current literature

**Issues:**
- Mixes materials (iron, stony, stony-iron) under Achondrite Type
- Visually chondrite-heavy (82% of all meteorites)

---

## Structure 2: Option B Classification

**Hierarchy:** Type → Class → Clan → Group → Subgroup

**Additional Labels:** Parent Body, Clan (for filtering/searching)

```
All Meteorites (86,190)
│
├── Type: Chondrite (70,919)
│   ├── Class: Ordinary Chondrite (66,383)
│   │   ├── Group: H (29,754)
│   │   ├── Group: L (27,756)
│   │   ├── Group: LL (8,514)
│   │   ├── Group: L/LL (160)
│   │   ├── Group: OC (102)
│   │   ├── Group: H/L (63)
│   │   ├── Group: LL/L (30)
│   │   └── Group: L/H (4)
│   │
│   ├── Class: Carbonaceous Chondrite (3,726)
│   │   ├── Clan: CM-CO (1,570)
│   │   │   ├── Group: CO (792)
│   │   │   └── Group: CM (778)
│   │   ├── Clan: CV-CK (1,406)
│   │   │   ├── Group: CV (786)
│   │   │   └── Group: CK (620)
│   │   ├── Clan: CR (400)
│   │   │   ├── Group: CR (218)
│   │   │   ├── Group: CH (29)
│   │   │   └── Group: CB (26)
│   │   └── [Groups without clan: R, C3, C2, C-ung, CI, CL, C1, K, etc.]
│   │
│   └── Class: Enstatite Chondrite (713)
│       ├── Group: E (247)
│       ├── Group: EL (241)
│       └── Group: EH (225)
│
├── Type: Achondrite (5,501) [stony differentiated only]
│   ├── Clan: Vesta [Parent Body: Vesta] (3,313)
│   │   ├── Group: Eucrite (2,087)
│   │   ├── Group: Diogenite (720)
│   │   └── Group: Howardite (506)
│   │
│   ├── Clan: Lunar [Parent Body: Moon] (804)
│   │   └── Group: Lunar (804)
│   │
│   ├── Clan: Martian [Parent Body: Mars] (419)
│   │   ├── Group: Shergottite (357)
│   │   ├── Group: Nakhlite (34)
│   │   ├── Group: Martian (24)
│   │   ├── Group: Chassignite (3)
│   │   └── Group: OPX (1)
│   │
│   ├── Group: Aubrite (96) [no clan]
│   ├── Group: Angrite (24) [no clan]
│   └── Group: Enst achon (13) [no clan]
│
├── Type: Primitive achondrite (1,180) [stony primitive only]
│   ├── Clan: ACA-LOD [Parent Body: ACA-LOD parent] (209)
│   │   ├── Group: Lodranite (101)
│   │   ├── Group: Acapulcoite (96)
│   │   └── Group: ACA/LOD (12)
│   │
│   ├── Group: Ureilite (766) [no clan] [Parent Body: Ureilite parent]
│   ├── Group: Winonaite (105) [no clan] [Parent Body: IAB/Winonaite parent]
│   └── Group: Brachinite (73) [no clan]
│
├── Type: Iron meteorite (1,442)
│   ├── Primitive/Non-magmatic (392)
│   │   ├── Group: IAB (308) [Parent Body: IAB/Winonaite parent]
│   │   └── Group: IAB complex (84) [Parent Body: IAB/Winonaite parent]
│   │
│   ├── Differentiated/Magmatic (761)
│   │   ├── Group: IIIAB (369)
│   │   ├── Group: IIAB (155)
│   │   ├── Group: IVA (94)
│   │   ├── Group: IID (31)
│   │   ├── Group: IIE (27)
│   │   ├── Group: IIIE (22)
│   │   ├── Group: IVB (20)
│   │   ├── Group: IC (16)
│   │   ├── Group: IIIF (9)
│   │   ├── Group: IIC (8)
│   │   ├── Group: IIF (8)
│   │   └── Group: IIG (6)
│   │
│   └── Ungrouped iron (289)
│       ├── Iron, ungrouped (160)
│       ├── Iron (106)
│       ├── Iron? (2)
│       └── [Relict iron: 21 - moved to Relict type]
│
├── Type: Stony-iron meteorite (612)
│   ├── Differentiated (608)
│   │   ├── Group: Mesosiderite (394)
│   │   └── Group: Pallasite (214)
│   │
│   └── Ungrouped stony-iron (4)
│       └── Stony iron (4)
│
├── Type: Ungrouped (1,385) [stony only]
│   └── Stone-uncl (1,385)
│
├── Type: Unknown (5,482)
│   ├── Unknown (4,984)
│   ├── Terrestrial rock (228)
│   ├── Impact Crater (190)
│   ├── Pseudometeorite (71)
│   ├── Doubtful meteorite (116)
│   ├── Doubtful stone (46)
│   ├── Doubtful Iron (24)
│   ├── Discredited (14)
│   ├── Chondrite-fusion crust (4)
│   ├── Fusion crust (4)
│   ├── Doubtful OC (3)
│   ├── Impact melt breccia (1)
│   ├── Doubtful achondrite (1)
│   ├── Doubtful pallasite (1)
│   ├── Doubtful eucrite (1)
│   └── Doubtful chondrite (1)
│
└── Type: Relict meteorite (89)
    ├── Relict OC (65) [Material: stony]
    ├── Relict iron (21) [Material: iron]
    ├── Relict H (1) [Material: stony]
    ├── Relict ureilite (1) [Material: stony]
    └── Relict meteorite (1) [Material: unknown]
```

**Key Features:**
- Separates Iron and Stony-iron as distinct Types
- Achondrite = stony differentiated only
- IAB irons classified as "Primitive" under Iron Type
- Addresses concern about mixing irons with achondrites

**Advantages:**
- Clearer separation by material type
- IAB/Winonaite genetic relationship preserved via Parent Body label
- More balanced top-level structure

**Issues:**
- More Types (8 vs 6) = deeper initial branching
- "Primitive iron" vs "Primitive achondrite" may seem redundant

---

## Structure 3: Material-First Classification

**Hierarchy:** Material → Type → Class → Group → Subgroup

**Additional Labels:** Parent Body, Clan (for filtering/searching, NOT hierarchy)

```
All Meteorites (86,190)
│
├── Material: Stony (78,542)
│   │
│   ├── Type: Chondrite (70,919)
│   │   ├── Class: Ordinary Chondrite (66,383)
│   │   │   ├── Group: H (29,754)
│   │   │   ├── Group: L (27,756)
│   │   │   ├── Group: LL (8,514)
│   │   │   ├── Group: L/LL (160)
│   │   │   ├── Group: OC (102)
│   │   │   ├── Group: H/L (63)
│   │   │   ├── Group: LL/L (30)
│   │   │   └── Group: L/H (4)
│   │   │
│   │   ├── Class: Carbonaceous Chondrite (3,726)
│   │   │   ├── Group: CO (792) [Clan: CM-CO]
│   │   │   ├── Group: CM (778) [Clan: CM-CO]
│   │   │   ├── Group: CV (786) [Clan: CV-CK]
│   │   │   ├── Group: CK (620) [Clan: CV-CK]
│   │   │   ├── Group: R (350)
│   │   │   ├── Group: CR (218) [Clan: CR]
│   │   │   ├── Group: C3 (50)
│   │   │   ├── Group: C2 (32)
│   │   │   ├── Group: CH (29) [Clan: CR]
│   │   │   ├── Group: CB (26) [Clan: CR]
│   │   │   ├── Group: C-ung (13)
│   │   │   ├── Group: CI (10)
│   │   │   ├── Group: CL (7)
│   │   │   ├── Group: C1 (5)
│   │   │   ├── Group: K (4)
│   │   │   ├── Group: C4 (3)
│   │   │   ├── Group: C6 (2)
│   │   │   └── Group: C5/6 (1)
│   │   │
│   │   └── Class: Enstatite Chondrite (713)
│   │       ├── Group: E (247)
│   │       ├── Group: EL (241)
│   │       └── Group: EH (225)
│   │
│   ├── Type: Achondrite (5,501)
│   │   ├── Group: Eucrite (2,087) [Parent Body: Vesta]
│   │   ├── Group: Lunar (804) [Parent Body: Moon]
│   │   ├── Group: Diogenite (720) [Parent Body: Vesta]
│   │   ├── Group: Howardite (506) [Parent Body: Vesta]
│   │   ├── Group: Shergottite (357) [Parent Body: Mars]
│   │   ├── Group: Aubrite (96)
│   │   ├── Group: Nakhlite (34) [Parent Body: Mars]
│   │   ├── Group: Martian (24) [Parent Body: Mars]
│   │   ├── Group: Angrite (24)
│   │   ├── Group: Enst achon (13)
│   │   ├── Group: Chassignite (3) [Parent Body: Mars]
│   │   └── Group: OPX (1) [Parent Body: Mars]
│   │
│   ├── Type: Primitive achondrite (1,180)
│   │   ├── Group: Ureilite (766) [Parent Body: Ureilite parent]
│   │   ├── Group: Winonaite (105) [Parent Body: IAB/Winonaite parent] [Clan: ACA-LOD]
│   │   ├── Group: Lodranite (101) [Clan: ACA-LOD]
│   │   ├── Group: Acapulcoite (96) [Clan: ACA-LOD]
│   │   ├── Group: Brachinite (73)
│   │   └── Group: ACA/LOD (12) [Clan: ACA-LOD]
│   │
│   ├── Type: Ungrouped stony (1,385)
│   │   └── Stone-uncl (1,385)
│   │
│   └── Type: Relict meteorite (67)
│       ├── Relict OC (65)
│       ├── Relict H (1)
│       └── Relict ureilite (1)
│
├── Material: Iron (1,442)
│   │
│   ├── Type: Primitive iron (392)
│   │   ├── Group: IAB (308) [Parent Body: IAB/Winonaite parent]
│   │   └── Group: IAB complex (84) [Parent Body: IAB/Winonaite parent]
│   │
│   ├── Type: Differentiated/Magmatic iron (761)
│   │   ├── Group: IIIAB (369)
│   │   ├── Group: IIAB (155)
│   │   ├── Group: IVA (94)
│   │   ├── Group: IID (31)
│   │   ├── Group: IIE (27)
│   │   ├── Group: IIIE (22)
│   │   ├── Group: IVB (20)
│   │   ├── Group: IC (16)
│   │   ├── Group: IIIF (9)
│   │   ├── Group: IIC (8)
│   │   ├── Group: IIF (8)
│   │   └── Group: IIG (6)
│   │
│   ├── Type: Ungrouped iron (268)
│   │   ├── Iron, ungrouped (160)
│   │   ├── Iron (106)
│   │   └── Iron? (2)
│   │
│   └── Type: Relict iron (21)
│       └── Relict iron (21)
│
├── Material: Stony-iron (612)
│   │
│   ├── Type: Differentiated stony-iron (608)
│   │   ├── Group: Mesosiderite (394)
│   │   └── Group: Pallasite (214)
│   │
│   ├── Type: Ungrouped stony-iron (4)
│   │   └── Stony iron (4)
│   │
│   └── Type: Relict stony-iron (0)
│
└── Material: Unknown (5,594)
    │
    ├── Type: Unknown (5,482)
    │   ├── Unknown (4,984)
    │   ├── Terrestrial rock (228)
    │   ├── Impact Crater (190)
    │   ├── Pseudometeorite (71)
    │   ├── Chondrite-fusion crust (4)
    │   ├── Fusion crust (4)
    │   └── Impact melt breccia (1)
    │
    ├── Type: Doubtful/Discredited (207)
    │   ├── Doubtful meteorite (116)
    │   ├── Doubtful stone (46)
    │   ├── Doubtful Iron (24)
    │   ├── Discredited (14)
    │   ├── Doubtful OC (3)
    │   ├── Doubtful achondrite (1)
    │   ├── Doubtful pallasite (1)
    │   ├── Doubtful eucrite (1)
    │   └── Doubtful chondrite (1)
    │
    └── Type: Relict unknown (1)
        └── Relict meteorite (1)
```

**Key Features:**
- Material (observable property) as Level 0
- Most balanced tree structure (4 main branches vs 6-8)
- IAB irons stay with other irons but labeled as "Primitive"
- Parent Body and Clan preserved as searchable/filterable labels (not hierarchy)
- Ungrouped categorized by material type

**Advantages:**
- ✅ Most intuitive for public/educational use
- ✅ Clearest visual balance in tree
- ✅ Material separation makes searching easier
- ✅ IAB/Winonaite connection preserved via Parent Body label
- ✅ Handles ungrouped meteorites more logically

**Considerations:**
- Non-standard in scientific literature
- Adds one more hierarchy level (Material)
- Separates genetically related objects (IAB vs Winonaite) into different Material branches
  (but connection preserved via Parent Body label)

---

## Summary Comparison

| Feature | Current | Option B | Material-First |
|---------|---------|----------|----------------|
| **Top Level** | Type (6) | Type (8) | Material (4) |
| **Visual Balance** | Chondrite-heavy | More balanced | Most balanced |
| **Iron Classification** | Under Achondrite | Separate Type | Under Iron Material |
| **IAB Placement** | Achondrite Type | Primitive Iron Type | Primitive Iron Type |
| **Parent Body Info** | Clan (hierarchy) | Clan or label | Label only |
| **Genetic Relationships** | In hierarchy | In hierarchy | Via labels |
| **Public Clarity** | Good | Good | Excellent |
| **Scientific Standard** | Yes | Modified | Non-standard |
| **Database Searchability** | Good | Good | Excellent |
| **Tree Depth** | 5 levels | 5 levels | 6 levels |

---

## Recommendations by Use Case

**For Research Database (primary users = scientists):**
→ **Structure 1 (Current)** or **Structure 2 (Option B)**

**For Educational Website (primary users = students/public):**
→ **Structure 3 (Material-First)**

**For Mixed Audience (researchers + public):**
→ **Structure 2 (Option B)** - best compromise

---

*All structures include the same reclassifications and data. The choice depends on your primary audience and educational goals.*
