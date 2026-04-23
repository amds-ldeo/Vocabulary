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

[]{#W3CDCATThemesfortheSeaDataNetEDMEDCatalogue}

# **Concept scheme:** W3C DCAT Themes for the SeaDataNet EDMED Catalogue

no modified date

subtitle: 

Namespace: 
[`http://vocab.nerc.ac.uk/scheme/EDMED_DCAT_THEMES/current`](http://vocab.nerc.ac.uk/scheme/EDMED_DCAT_THEMES/current)

**History**


- [Parameters](#d0100001)
    - [Microzooplankton taxonomy-related biosurface area per unit volume of the water column](#a999)
    - [Phytoplankton taxonomic surface area in water bodies](#aatx)
    - [Concentration of alkanamines (amines) in the water column](#aawc)
    - [Suspended particulate material aggregates](#abag)
    - [Quality control flags](#acfl)
    - [Macroalgae and seagrass taxonomy-related counts](#acnt)
    - [Active seismic refraction](#acsr)
    - [Reference numbers](#acyc)
    - [Vertical spatial coordinates](#ahgt)
    - [Horizontal spatial co-ordinates](#alat)
    - [Alkalinity, acidity and pH of the water column](#alky)
    - [Ammonium and ammonia concentration parameters in water bodies](#amon)
    - [Nitrification and denitrification rates in water bodies](#amox)
    - [Regenerated production in water bodies](#amup)
    - [Horizontal platform movement](#apda)
    - [Vertical platform movement](#apza)
    - [Acoustic backscatter in the water column](#asam)
    - [Sea level](#aslv)
        - [Sea level expressed as pressure](#prex)
    - [Atmospheric emissions](#atem)
    - [Concentration of adenylates in the water column](#atpx)
    - [Atmospheric visibility and transparency](#atvs)
    - [Date and time](#aymd)
    - [Bacteria in biota](#babi)
    - [Bacteria taxonomy-related biomass expressed as carbon per unit volume of the water column](#batc)
    - [Bacteria environmental parameters](#batt)
    - [Bacteria taxonomic abundance in water bodies](#batx)
    - [Bacteria taxonomic abundance in sediment](#bauc)
    - [Concentration of polycyclic aromatic hydrocarbons (PAHs) in biota](#bcah)
    - [Metal concentrations in biota](#bcmt)
    - [Concentration of other organic contaminants in biota](#bcoc)
    - [Concentration of other substances in biota](#bcos)
    - [Concentration of polychlorobiphenyls (PCBs) in biota](#bcpb)
    - [Biodiversity indices](#bdrv)
    - [Bacteria taxonomy-related ash-free dry weight biomass in sediment](#bdwc)
    - [Zooplankton and zoobenthos morphological parameters](#blen)
    - [Bioluminescence parameters](#blum)
    - [Bacteria non taxonomy-related biomass expressed as carbon per unit volume of the water column](#bntc)
    - [Bacteria generic abundance in water bodies](#bntx)
    - [Bacteria generic abundance in sediment](#bnuc)
    - [Bacteria non taxonomy-related biomass expressed as protein per unit volume of the water column](#bpbp)
    - [SeaDataNet biological format biotic parameters](#bprp)
    - [Radioactivity in biota](#brad)
    - [Bird counts](#brda)
    - [Bird taxonomy-related abundance per unit area of surface](#brdd)
    - [Concentration of alkenones and alkenoates in the water column](#cakn)
    - [Air pressure](#caph)
    - [Carotenoid and flavenoid pigment concentrations in water bodies](#caro)
    - [Carotenoid pigment concentrations in sediment](#cars)
    - [Concentration of carbohydrates, phenols, alkanols (alcohols), ethers, aldehydes and ketones in sediment](#casd)
        - [Concentration of alkanols (alcohols), phenols and ethers in sediment](#ca11)
    - [Phytoplankton taxonomic biomass in water bodies](#catx)
    - [Bacteria morphology and physiology](#cbcc)
    - [Carbon concentrations in sediment](#cbsd)
    - [Carbon concentrations in suspended particulate material](#cbsp)
    - [Carbonate chemistry in sediment pore waters](#ccpw)
    - [Metal uptake rates in the water column](#cdru)
    - [Air temperature](#cdta)
    - [Cetacean behaviour](#cebh)
    - [Cetacean mortality](#cemo)
    - [Cetacean morphology and physiology](#cemp)
    - [Cetacean abundance](#ceta)
    - [Contaminant fluxes between the terrestrial and marine environment](#cftm)
    - [Cloud cover height and extent](#chex)
    - [Atmospheric humidity](#chum)
    - [Mineralogical composition](#clay)
    - [Cloud type](#clty)
    - [Concentration of inorganic halogens in sediment pore waters](#clxx)
    - [Variable fluorescence parameters](#cmfl)
    - [Electrical conductivity of the water column](#cndc)
    - [Phytoplankton generic biomass in water bodies](#cntx)
    - [Terrestrial mapping](#coas)
    - [Colloidal organic carbon concentration in the water column](#cocc)
    - [Coastal geomorphology](#coge)
    - [Unclassified pigment concentrations in sediment](#cpcn)
    - [Precipitation and evaporation](#cprp)
    - [Chlorophyll pigment concentrations in sediment](#cpsd)
    - [Chlorophyll pigment concentrations in water bodies](#cpwc)
    - [Snow and ice mass, thickness and extent](#crys)
    - [Organic sulphur compound dynamics in the water column](#csde)
    - [Solar Radiation](#cslr)
    - [Plankton biomass expressed as carbon per unit volume of the water column](#cyeu)
    - [Microphytobenthos abundance](#d000)
    - [Concentration of alkanes in the water column](#dalk)
    - [Geological sample density](#dbdx)
    - [Other halocarbon concentrations in water bodies](#dcmx)
    - [Other physical and chemical properties of suspended particulate material](#dens)
    - [Dissolved oxygen parameters for sediments](#dgpw)
    - [Organosulphur and organoselenium species concentration parameters in water bodies](#dmst)
    - [Dissolved organic carbon concentration in the water column](#docc)
    - [Dissolved organic carbon uptake and production in the water column](#docu)
    - [Dissolved oxygen parameters in the water column](#doxy)
    - [Depositional environment](#dpev)
    - [Zooplankton and zoobenthos development stage parameters](#dvlp)
    - [Engineering parameters](#engp)
    - [Wind strength and direction](#ewsb)
    - [Light extinction and diffusion coefficients](#exco)
    - [Excretion rate parameters in the water column](#excr)
    - [Water body lipid concentrations](#f001)
    - [Fauna abundance per unit area of the bed](#fabd)
    - [Fish taxonomy-related abundance per unit area of the bed](#fbab)
    - [Fish taxonomy-related ash-free dry weight biomass per unit area of the bed](#fbaf)
    - [Fish taxonomy-related counts](#fcnt)
    - [Zooplankton feeding](#fcrt)
    - [Fish non taxonomy-related abundance per unit volume of the water column](#fntx)
    - [Seal abundance](#foca)
    - [Chlorofluorocarbon concentrations in the water column](#fr11)
    - [Raw fluorometer output](#fvlt)
    - [Oxygen production and respiration in the water column](#goxp)
    - [Pollution events](#gp001)
    - [Bird reproduction](#gp004)
    - [Bioassay and contaminant biological impact](#gp010)
    - [Macroalgae and seagrass infection and damage](#gp012)
    - [Cetacean reproduction](#gp018)
    - [Seal reproduction](#gp025)
    - [Reptile disease and parasites](#gp067)
    - [Reptile abundance](#gp068)
    - [Reptile reproduction](#gp069)
    - [Zooplankton wet weight biomass](#gp079)
    - [Fishery characterisation](#gp087)
        - [Fishing by-catch](#gp080)
    - [Bird behaviour](#gp088)
    - [Zooplankton gut pigments](#gpig)
    - [Gravity](#grav)
    - [Bacterial growth](#gref)
    - [Zooplankton growth rates](#grzo)
    - [Geotechnics](#gtch)
    - [Groundwater amount](#gwam)
    - [Groundwater chemistry](#gwch)
    - [Wave direction](#gwdr)
    - [Amino acids in sediment](#haac)
    - [Platform or instrument orientation](#head)
    - [Wave height estimates](#heav)
    - [Dissolved noble gas concentration parameters in the water column](#hexc)
    - [Concentration of inorganic halogens in water bodies](#hlwc)
    - [Concentration of organic matter in water bodies](#hmsb)
    - [Hazards to navigation](#hznv)
    - [Ice age](#iage)
    - [Insect and earthworm taxonomy-related ash-free dry weight biomass per unit area of the littoral zone](#ialz)
    - [Insecta taxonomy-related abundance per unit volume of the water column](#iatx)
    - [Ice motion and related parameters](#icem)
    - [Snow and ice chemistry](#ichm)
    - [Industrial discharges](#idis)
    - [Insect and earthworm taxonomy-related abundance per unit area of the littoral zone](#inlz)
    - [Snow and ice physical properties and characteristics](#iphy)
    - [Stable isotopes in biota](#irbo)
    - [Stable isotopes in speleothems](#irsp)
    - [Insect and earthworm taxonomy-related abundance per unit area of the bed](#iwab)
    - [Insect and earthworm taxonomy-related ash-free dry weight biomass per unit area of the bed](#iwdx)
    - [Other wave statistics](#krts)
    - [Raw current meter output parameters](#lerr)
    - [Lagrangian currents and transport rates in the water column](#lgcr)
    - [Biota lipid concentrations](#libi)
    - [Lithology](#lith)
    - [Litter abundance and type](#litt)
    - [Land surface temperature](#lsst)
    - [Land vegetation](#lveg)
    - [Raw light meter output](#lvlt)
    - [Terrestrial water content](#lwet)
    - [Long-wave radiation](#lwrd)
    - [Microzooplankton taxonomy-related biomass expressed as carbon per unit volume of the water column](#matc)
    - [Microzooplankton taxonomic abundance in water bodies](#matx)
    - [Bathymetry and Elevation](#mban)
    - [Trace metalloid concentrations in biota](#mdbo)
    - [Trace metalloid concentrations in sediment pore water](#mdpw)
    - [Trace metalloid concentrations in sediment](#mdsd)
    - [Suspended particulate material setting velocity parameters](#mdsv)
    - [Dissolved trace metalloid and inorganic selenium concentrations in water bodies](#mdwd)
    - [Particulate trace metalloid and inorganic selenium concentrations in water bodies](#mdwp)
    - [Zooplankton egg hatch proportion](#meph)
    - [Zoobenthos generic abundance](#mfab)
    - [Zoobenthos taxonomy-related ash-free dry weight biomass per unit area of the littoral zone](#mfaz)
    - [Zoobenthos taxonomy-related abundance per unit area of the littoral zone](#mflz)
    - [Zoobenthos non taxonomy-related wet weight biomass per unit area of the bed](#mfww)
    - [Magnetics](#mman)
    - [Man-made structures](#mmst)
    - [Moored instrument depth](#mpmn)
    - [Zooplankton reproduction rate parameters](#msep)
    - [Metal concentrations in the cryosphere](#mtic)
    - [Metal concentrations in sediment pore waters](#mtpw)
    - [Metal concentrations in sediment](#mtsd)
    - [Colloidal metal concentrations in the water column](#mtwc)
    - [Dissolved metal concentrations in the water column](#mtwd)
    - [Total metal concentrations in water bodies](#mtwt)
    - [Microzooplankton non taxonomy-related biomass expressed as carbon per unit volume of the water column](#mzbc)
    - [Microzooplankton generic abundance in water bodies](#mzbn)
    - [Microzooplankton grazing](#mzct)
    - [Acoustic noise in the water column](#noys)
    - [Nutrient concentrations in sediment pore waters](#ntpw)
    - [Nitrate concentration parameters in the water column](#ntra)
        - [Nitrate+nitrite concentration parameters in the water column](#ntrz)
    - [Nitrite concentration parameters in the water column](#ntri)
    - [Nitrogen concentrations in suspended particulate material](#ntsp)
    - [New production in water bodies](#ntup)
    - [Raw in-situ nutrient analyser output](#nutv)
    - [Dissolved organic carbon concentrations in sediment pore waters](#ocpw)
    - [Dissolved concentration parameters for other gases in sediment pore waters](#ogpw)
    - [Concentration of other hydrocarbons in the water column](#ohwc)
    - [Organometallic species concentration parameters in biota](#ombi)
    - [Other meteorological measurements](#omet)
    - [Organometallic and organometalloid species concentration parameters in sediments](#ompw)
    - [Organometallic and organometalloid species concentration parameters in water bodies](#omwc)
    - [Optical backscatter](#opbs)
    - [Concentration of silicon species in suspended particulate material](#opcn)
    - [Raw oxygen sensor output](#oxyc)
    - [Phytoplankton taxonomic abundance in water bodies](#patx)
    - [Concentration of polycyclic aromatic hydrocarbons (PAHs) in suspended particulate material](#pcah)
    - [Concentration of polycyclic aromatic hydrocarbons (PAHs) in the water column](#pchw)
    - [Palaeoclimatic indicators and parameters](#pclm)
    - [Concentration of other organic contaminants in suspended particulate material](#pcoc)
    - [Pesticide concentrations in biota](#pebi)
    - [Pesticide concentrations in sediment](#pesd)
    - [Pesticide concentrations in water bodies](#pewb)
    - [Phosphate concentration parameters in the water column](#phos)
    - [Phaeopigment concentrations in sediment](#phsd)
    - [Pharmaceutical concentrations in water bodies](#phwb)
    - [Phaeopigment concentrations in the water column](#phwc)
    - [Phycobolin pigment concentrations in the water column](#phyc)
    - [Phytoplankton growth](#phyg)
    - [Phytoplankton generic abundance in water bodies](#pntx)
    - [Light absorption in the water column](#ppab)
    - [Concentration of polychlorobiphenyls (PCBs) in suspended particulate material](#ppcb)
    - [Primary production in the water column](#pprd)
    - [Concentration of polychlorobiphenyls (PCBs) in the water column](#ppwc)
    - [Salinity of the water column](#psal)
    - [Concentration of phycotoxins in biota](#ptox)
    - [Macroalgae generic abundance in water bodies](#pu02)
    - [Phosphorus concentrations in sediment](#pxsd)
    - [Phosphorus concentrations in suspended particulate material](#pxsp)
    - [Plankton abundance per unit volume of the water column](#pytt)
    - [Quantity of material dumped](#qdmd)
    - [Ocean colour and earth-leaving visible waveband spectral radiation](#r410)
    - [Rock age](#rage)
    - [Rock alteration](#ralt)
    - [Molecular biology parameters](#rbhy)
    - [Radar backscatter](#rbsc)
    - [Horizontal velocity of the water column (currents)](#rfvl)
    - [Inorganic chemical composition of sediment or rocks](#rmin)
    - [Redox potential in sediment](#rpot)
    - [River flow and discharge](#rvds)
    - [Shellfish abundance and biomass in water bodies](#sabb)
    - [Concentration of aliphatic hydrocarbons in sediment samples](#salk)
    - [Nutrient fluxes between the bed and the water column](#samo)
    - [Shellfish morphology, age and physiology](#satm)
    - [Concentration of polycyclic aromatic hydrocarbons (PAHs) in sediment samples](#scah)
    - [Metal fluxes between the bed and the water column](#scdo)
    - [Concentration of other organic contaminants in sediment samples](#scoc)
    - [Dissolved concentration parameters for other gases in the water column](#scox)
    - [Concentrations of biopolymers in sediment](#sdna)
    - [Seal behaviour](#sebh)
    - [Secchi disk depth](#secc)
    - [Seal mortality](#semo)
    - [Seal morphology and physiology](#semp)
    - [Hydrolytic activity in sediment](#shta)
    - [Density of the water column](#sigt)
    - [Stable isotopes in sediment pore waters](#sipw)
    - [Concentration of silicon species in the water column](#sixx)
    - [Speleothem age](#spag)
    - [Concentration of polychlorobiphenyls (PCBs) in sediment samples](#spcb)
    - [Suspended particulate material grain size parameters](#spgs)
    - [Concentration of inorganic sulphur species in sediment pore water](#spht)
    - [Concentration of proteins in sediment](#spro)
    - [Concentration of inorganic sulphur species in the water column](#spwc)
    - [Two-dimensional seismic reflection](#sr2d)
    - [Three-dimensional seismic reflection](#sr3d)
    - [Geological sample radioactivity](#srad)
    - [Shellfish reproduction](#srep)
    - [Seismic reflection](#srfl)
        - [Two-dimensional seismic reflection](#sr2d)
        - [Three-dimensional seismic reflection](#sr3d)
    - [Seismic refraction](#srfr)
    - [Side-scan sonar](#sscn)
        - [Long/short range side scan sonar](#g24)
    - [Temperature of geological units](#stmp)
        - [Rock temperature](#rtmp)
    - [Concentration of organic matter in sediments](#stom)
    - [Concentration of adenylates in sediment](#tadn)
    - [Raw temperature and/or salinity instrument output](#tcnt)
    - [Dissolved inorganic nitrogen concentration in the water column](#tdin)
    - [Dissolved total and organic nitrogen concentrations in the water column](#tdnt)
    - [Dissolved total or organic phosphorus concentration in the water column](#tdpx)
    - [Dissolved amino acid concentrations in the water column](#tfaa)
    - [Metadata parameters](#tmes)
    - [Dissolved inorganic carbon production and respiration in the water column](#tnrp)
    - [Concentration of carbohydrates, phenols, alkanols (alcohols), aldehydes and ketones in water bodies](#toch)
    - [Transport activity](#tran)
    - [Concentration of inorganic sulphur species in sediment](#tris)
    - [Concentration of suspended particulate material in the water column](#tsed)
    - [Raw suspended particulate material concentration sensor output](#tvlt)
    - [Bacterial production in the water column](#upth)
    - [Ultra-violet (UV) radiation](#uvrd)
    - [Microzooplankton taxonomy-related biovolume per unit volume of the water column](#v999)
    - [Phytoplankton taxonomic volume in water bodies](#vatx)
    - [Virus abundance in water bodies](#viru)
    - [Visible waveband radiance and irradiance measurements in the atmosphere](#vsra)
    - [Water body redox potential](#wbrx)
    - [Concentration of other organic contaminants in the water column](#wcoc)
    - [Concentration of proteins in the water column](#wpro)
    - [Water quality bioindicators](#wqbi)
    - [Radioactivity in water bodies](#wrad)
    - [Stable isotopes in water bodies](#wstb)
    - [Wind stress and shear](#wstr)
    - [Spectral wave data parameters](#wvsp)
    - [Wave height and period statistics](#wvst)
    - [Geological sample magnetic, electrical and acoustic properties](#xmgs)
    - [Raw X-Ray fluorometer (XRF) output from sediment samples](#xrfc)
    - [Zoobenthos dry weight biomass](#zadx)
    - [Zooplankton taxonomy-related biomass expressed as protein per unit volume of the water column](#zatp)
    - [Zooplankton taxonomy-related abundance per unit volume of the water column](#zatx)
    - [Zoobenthos taxonomic abundance](#zbtx)
    - [Zooplankton chemical composition](#zcmp)
    - [Zooplankton taxonomy-related biomass expressed as carbon per unit volume of the water column](#zctc)
    - [Zooplankton taxonomy-related biomass expressed as nitrogen per unit volume of the water column](#zctn)
    - [Zooplankton and zoobenthos physiological condition parameters](#zfit)
    - [Metal ligand parameters in the water column](#znlg)
    - [Zoobenthos taxonomy-related counts](#zoob)
    - [Zooplankton biovolume](#zv00)
    - [Zoobenthos taxonomy-related wet weight biomass per unit area of the bed](#zwtx)
    - [Unspecified](#zzzz)

- [d0100002](#d0100002)

- [d0100003](#d0100003)

- [d0100004](#d0100004)

- [d0100005](#d0100005)

**Concepts**

[]{#d0100001}

##  Parameters
- Measurement phenomena for use in dataset discovery metadata.
- Concept URI: http://vocab.nerc.ac.uk/collection/D01/current/D0100001


[]{#a999}

###  Microzooplankton taxonomy-related biosurface area per unit volume of the water column
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Microzooplankton surface area per unit volume of the water column
parameters presented at the level of taxa that may be mapped to
entities in a standard taxonomy registry such as WoRMS or ITIS.  These
may be at any taxonomic level from sub-species upwards.
- **Alternate labels:**
WC_TaxMicrozooSurfArea, 
WC_TaxMicrozooSurfArea, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/A999


[]{#aatx}

###  Phytoplankton taxonomic surface area in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Any parameterisation of cell surface area of free-floating
autotrophic biological entities designated by taxonomic names (e.g.
species, genus, family) in any body of fresh or salt water.
- **Alternate labels:**
PhytoTaxaAreaWater, 
PhytoTaxaAreaWater, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/AATX


[]{#aawc}

###  Concentration of alkanamines (amines) in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`C050`](#C050)
- Alkanamine concentrations in all phases of the water column
- **Alternate labels:**
WC_Amines, 
WC_Amines, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/AAWC


[]{#abag}

###  Suspended particulate material aggregates
- Child of:
 [`D0100001`](#D0100001)
 [`G015`](#G015)
- Parameters relating to the abundance, size and morphology of
particle aggregates in the SPM
- **Alternate labels:**
SPM_aggreg, 
SPM_aggreg, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/ABAG


[]{#acfl}

###  Quality control flags
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`Z005`](#Z005)
-
- **Alternate labels:**
QC_Flag, 
QC_Flag, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/ACFL


[]{#acnt}

###  Macroalgae and seagrass taxonomy-related counts
- Child of:
 [`D0100001`](#D0100001)
- Macroalgae (Rhodophycota, Chromphycota, Chlorophycota) and seagrass
(Charophyta, Anthophyta) count parameters presented at the level of
taxa at any level from sub-species upwards. Count includes
presence/absence indicators.
- **Alternate labels:**
Macroalgae+Seagrass_taxa_count, 
Macroalgae+Seagrass_taxa_count, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/ACNT


[]{#acsr}

###  Active seismic refraction
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`G012`](#G012)
 [`GPYS`](#GPYS)
- Parameters quantifying the magnitude of earth movements resulting
from artificial sources (such as explosions) far away from the
measurement site.
- **Alternate labels:**
ActSeisRefrac, 
ActSeisRefrac, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/ACSR


[]{#acyc}

###  Reference numbers
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`Z005`](#Z005)
- Data record, event, sample or measurement reference numbers
- **Alternate labels:**
Refno, 
Refno, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/ACYC


[]{#ahgt}

###  Vertical spatial coordinates
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`Z005`](#Z005)
- All vertical spatial parameters including depth, height and pressure
when used as an independent variable.
- **Alternate labels:**
Vert_spac_coord, 
Vert_spac_coord, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/AHGT


[]{#alat}

###  Horizontal spatial co-ordinates
- Child of:
 [`D0100001`](#D0100001)
 [`Z005`](#Z005)
- All forms of horizontal spatial coordinates such as lat/lon and grid
references
- **Alternate labels:**
Horiz_spat_coord, 
Horiz_spat_coord, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/ALAT


[]{#alky}

###  Alkalinity, acidity and pH of the water column
- Child of:
 [`D0100001`](#D0100001)
 [`C010`](#C010)
- Parameters quantifying the hydrogen ion concentration in water
bodies
- **Alternate labels:**
WC_Alk+Ac+pH, 
WC_Alk+Ac+pH, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/ALKY


[]{#amon}

###  Ammonium and ammonia concentration parameters in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`C005`](#C005)
 [`C040`](#C040)
- Ammonium and ammonia concentration parameters (including statistical
parameters such as standard deviation) in any body of fresh or salt
water.
- **Alternate labels:**
WC_NH4, 
WC_NH4, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/AMON


[]{#amox}

###  Nitrification and denitrification rates in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C005`](#C005)
 [`C040`](#C040)
 [`O010`](#O010)
- Parameters quantifying rates associated with nitrification
(oxidation of reduced nitrogen such as ammonium) and denitrification
(conversion of nitrate into gaseous compounds such as nitric oxide,
nitrous oxide and molecular nitrogen) processes in the water column of
any body of fresh or salt water.
- **Alternate labels:**
WC_Nitrif_Denitr, 
WC_Nitrif_Denitr, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/AMOX


[]{#amup}

###  Regenerated production in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C040`](#C040)
 [`O010`](#O010)
- Parameters quantifying the uptake rate of nitrogen from excretion
products (ammonium and urea) by flora and fauna living in any body of
salt or fresh water
- **Alternate labels:**
Reg_prod, 
Reg_prod, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/AMUP


[]{#apda}

###  Horizontal platform movement
- Child of:
 [`D0100001`](#D0100001)
 [`Z005`](#Z005)
- All parameters relating to horizontal platform travel, including
distance run
- **Alternate labels:**
Horiz_Plat_Vel, 
Horiz_Plat_Vel, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/APDA


[]{#apza}

###  Vertical platform movement
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`Z005`](#Z005)
- Parameters quantifying the upward and downward motion of objects
mounting sensors or collecting samples.
- **Alternate labels:**
VertPlatVelocity, 
VertPlatVelocity, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/APZA


[]{#asam}

###  Acoustic backscatter in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`D005`](#D005)
 [`watercolumnproperties`](#watercolumnproperties)
- Includes all parameters covering the strength of acoustic signal
return, including absolute measurements of returning signal strength
as well as parameters expressed as backscatter (the proportion of
transmitted signal returned)
- **Alternate labels:**
Acc_bksctr, 
Acc_bksctr, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/ASAM


[]{#aslv}

###  Sea level
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Measurements and predictions of the displacement of the water column
surface from a fixed, stable reference
- **Alternate labels:**
Sea_Level, 
Sea_Level, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/ASLV


[]{#prex}

####  Sea level expressed as pressure
- Child of:
 [`005`](#005)
 [`ASLV`](#ASLV)
- Measurements of the displacement of the water column surface from a
fixed, stable reference expressed as either total pressure or sea
pressure
- **Alternate labels:**
SeaLvl_Press, 
SeaLvl_Press, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/PREX


[]{#atem}

###  Atmospheric emissions
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`H001`](#H001)
 [`O005`](#O005)
- Parameters quantifying and describing the release of substances into
the atmosphere as a result of human activity
- **Alternate labels:**
AtmosEmiss, 
AtmosEmiss, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/ATEM


[]{#atpx}

###  Concentration of adenylates in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`C050`](#C050)
- Concentrations of adenylates (ADP, ATP etc) in all phases of the
water column
- **Alternate labels:**
Aden_WC, 
Aden_WC, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/ATPX


[]{#atvs}

###  Atmospheric visibility and transparency
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Parameters relating to atmospheric clarity, such as optical
transmittance/attenuance, and resultant visibility
- **Alternate labels:**
AtmosVis, 
AtmosVis, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/ATVS


[]{#aymd}

###  Date and time
- Child of:
 [`D0100001`](#D0100001)
 [`Z005`](#Z005)
- All date and time parameters
- **Alternate labels:**
Date + Time, 
Date + Time, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/AYMD


[]{#babi}

###  Bacteria in biota
- Child of:
 [`D0100001`](#D0100001)
 [`B005`](#B005)
 [`B007`](#B007)
 [`H001`](#H001)
- Parameters relating to the abundance and nature of bacteria (Kingdom
Monera) infecting other biota.
- **Alternate labels:**
Bact_Biota, 
Bact_Biota, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/BABI


[]{#batc}

###  Bacteria taxonomy-related biomass expressed as carbon per unit volume of the water column
- Child of:
 [`D0100001`](#D0100001)
 [`B005`](#B005)
- Bacteria carbon biomass parameters presented at the level of taxa
that may be mapped to entities in a standard taxonomy registry such as
WoRMS or ITIS.  These may be at any taxonomic level from sub-species
upwards.  Bacteria are defined as all taxa that fall into Kingdom
Monera in the ITIS taxonomy, which includes cyanobacteria.
- **Alternate labels:**
WC_TaxBacteriaCarbBiomass, 
WC_TaxBacteriaCarbBiomass, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/BATC


[]{#batt}

###  Bacteria environmental parameters
- Child of:
 [`D0100001`](#D0100001)
 [`B005`](#B005)
-
- **Alternate labels:**
BactEnvironParm, 
BactEnvironParm, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/BATT


[]{#batx}

###  Bacteria taxonomic abundance in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`B005`](#B005)
- Any enumeration of bacteria (Kingdom Monera so includes
cyanobacteria) designated by taxonomic names (e.g. species, genus,
family) in any body of fresh or salt water.
- **Alternate labels:**
BactTaxaAbundWater, 
BactTaxaAbundWater, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/BATX


[]{#bauc}

###  Bacteria taxonomic abundance in sediment
- Child of:
 [`D0100001`](#D0100001)
 [`B005`](#B005)
- Any enumeration of bacteria (Kingdom Monera so includes
cyanobacteria) designated by taxonomic names (e.g. species, genus,
family) in any soil or sediment.
- **Alternate labels:**
BactTaxaAbundSed, 
BactTaxaAbundSed, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/BAUC


[]{#bcah}

###  Concentration of polycyclic aromatic hydrocarbons (PAHs) in biota
- Child of:
 [`D0100001`](#D0100001)
 [`C025`](#C025)
 [`C055`](#C055)
 [`H001`](#H001)
- PAH concentrations in either whole organisms or their constituent
parts
- **Alternate labels:**
Biota_PAH, 
Biota_PAH, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/BCAH


[]{#bcmt}

###  Metal concentrations in biota
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C035`](#C035)
 [`H001`](#H001)
- Metal concentrations in either whole organisms or their constituent
parts.
- **Alternate labels:**
Met_Biota, 
Met_Biota, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/BCMT


[]{#bcoc}

###  Concentration of other organic contaminants in biota
- Child of:
 [`D0100001`](#D0100001)
 [`C055`](#C055)
 [`H001`](#H001)
- Concentration parameters for carbon compounds regarded as
environmentally harmful in either whole organisms or their constituent
parts that are not included in other categories
- **Alternate labels:**
Biota_Orgcontam, 
Biota_Orgcontam, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/BCOC


[]{#bcos}

###  Concentration of other substances in biota
- Child of:
 [`D0100001`](#D0100001)
- 'Other'  (than metals or organic contaminants) substance
concentrations in either whole organisms or their constituent parts.
This is a 'bucket' grouping that may be reclassified as the dictionary
developes.
- **Alternate labels:**
Biota_Other_Subst, 
Biota_Other_Subst, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/BCOS


[]{#bcpb}

###  Concentration of polychlorobiphenyls (PCBs) in biota
- Child of:
 [`D0100001`](#D0100001)
 [`C055`](#C055)
 [`H001`](#H001)
- PCB concentrations in either whole organisms or their constituent
parts
- **Alternate labels:**
Biota_PCB, 
Biota_PCB, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/BCPB


[]{#bdrv}

###  Biodiversity indices
- Child of:
 [`D0100001`](#D0100001)
- Parameters describing the variety of entity types encountered in a
population of living organisms
- **Alternate labels:**
Biodiversity, 
Biodiversity, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/BDRV


[]{#bdwc}

###  Bacteria taxonomy-related ash-free dry weight biomass in sediment
- Child of:
 [`D0100001`](#D0100001)
 [`B005`](#B005)
- Bacteria ash-free dry weight biomass in sediment parameters
presented at the level of taxa that may be mapped to entities in a
standard taxonomy registry such as WoRMS or ITIS.  The taxa may be at
any taxonomic level from sub-species upwards.  Bacteria are defined as
all taxa that fall into Kingdom Monera in the ITIS taxonomy, which
includes cyanobacteria.
- **Alternate labels:**
Sed_TaxBacteriaAFDW, 
Sed_TaxBacteriaAFDW, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/BDWC


[]{#blen}

###  Zooplankton and zoobenthos morphological parameters
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B027`](#B027)
 [`B045`](#B045)
- Morphological parameters of zooplankton and zoobenthos (essentially
any animal except for insects, earthworms or fish), such as size,
shape and weight.  Benthic and planktonic animals have not been
seggregated because there is a degree of overlap (eg shrimps).
- **Alternate labels:**
Animal_morph, 
Animal_morph, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/BLEN


[]{#blum}

###  Bioluminescence parameters
- Child of:
 [`D0100001`](#D0100001)
 [`B027`](#B027)
 [`D015`](#D015)
- Parameters describing the nature and intensity of light generated by
biological activity in the water column.
- **Alternate labels:**
Biolum, 
Biolum, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/BLUM


[]{#bntc}

###  Bacteria non taxonomy-related biomass expressed as carbon per unit volume of the water column
- Child of:
 [`D0100001`](#D0100001)
 [`B005`](#B005)
- Basically any bacteria carbon biomass parameters that aren't
included in parameter group BATC because they cannot be mapped to
specific taxa in a standard taxonomy registry such as WoRMS or ITIS.
Bacteria are defined as Kingdom Monera, which includes cyanobacteria.
- **Alternate labels:**
WC_NontaxBacteriaCarbBiomass, 
WC_NontaxBacteriaCarbBiomass, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/BNTC


[]{#bntx}

###  Bacteria generic abundance in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`B005`](#B005)
- Any enumeration of bacteria (Kingdom Monera so includes
cyanobacteria) designated by terms other than taxonomic names (e.g.
total) in any body of fresh or salt water.
- **Alternate labels:**
BactGenAbundWater, 
BactGenAbundWater, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/BNTX


[]{#bnuc}

###  Bacteria generic abundance in sediment
- Child of:
 [`D0100001`](#D0100001)
 [`B005`](#B005)
- Any enumeration of bacteria (Kingdom Monera so includes
cyanobacteria) designated by terms other than taxonomic names (e.g.
total) in any soil or sediment.
- **Alternate labels:**
BactGenAbundSed, 
BactGenAbundSed, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/BNUC


[]{#bpbp}

###  Bacteria non taxonomy-related biomass expressed as protein per unit volume of the water column
- Child of:
 [`D0100001`](#D0100001)
 [`B005`](#B005)
-
- **Alternate labels:**
BactPopBiomProt, 
BactPopBiomProt, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/BPBP


[]{#bprp}

###  SeaDataNet biological format biotic parameters
- Child of:
 [`D0100001`](#D0100001)
 [`B027`](#B027)
- Parameters that quantify any attribute of a biological entity
specified elsewhere in the data model and therefore do not map to the
existing biologically classified P02 categories. This concept is used
as a temporary grouping of parameter codes created for the SeaDataNet
biological standard format.
- **Alternate labels:**
SDN_BioFormatCodes, 
SDN_BioFormatCodes, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/BPRP


[]{#brad}

###  Radioactivity in biota
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B007`](#B007)
 [`C030`](#C030)
- All parameters associated with radioactivity in either whole
organisms or their constituent parts
- **Alternate labels:**
Biota_RadAct, 
Biota_RadAct, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/BRAD


[]{#brda}

###  Bird counts
- Child of:
 [`B25`](#B25)
 [`D0100001`](#D0100001)
- Parameters quantifying the number of birds (Class Aves) in a survey
but not expressed per unit area. Includes presence/absence indicators.
- **Alternate labels:**
Bird_count, 
Bird_count, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/BRDA


[]{#brdd}

###  Bird taxonomy-related abundance per unit area of surface
- Child of:
 [`B25`](#B25)
 [`D0100001`](#D0100001)
- Bird (Class Aves) abundance per unit area (of land or sea) presented
at the level of taxa that may be mapped to entities in a standard
taxonomy registry such as WoRMS or ITIS.These may be at any taxonomic
level from sub-species upwards.
- **Alternate labels:**
Bird_taxa_abund, 
Bird_taxa_abund, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/BRDD


[]{#cakn}

###  Concentration of alkenones and alkenoates in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`C050`](#C050)
- Concentrations of alkenones (unsaturated aliphatic ketones) and
alkenoates (carboxylic acid esters) in all phases of the water column.
- **Alternate labels:**
Akenone+alkenoate_WC, 
Akenone+alkenoate_WC, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CAKN


[]{#caph}

###  Air pressure
- Child of:
 [`D0100001`](#D0100001)
- Measurements of air pressure as the dependent variable (ie excluding
air pressure measured to specify the z co-ordinate of a balloon or
sonde), including derived parameters such as tendency (rate of change)
and related parameters such as air density.
- **Alternate labels:**
Air_Press, 
Air_Press, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CAPH


[]{#caro}

###  Carotenoid and flavenoid pigment concentrations in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B035`](#B035)
-
- **Alternate labels:**
WC_CarotFlavPig, 
WC_CarotFlavPig, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CARO


[]{#cars}

###  Carotenoid pigment concentrations in sediment
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B035`](#B035)
 [`sedimentorganicchemistry`](#sedimentorganicchemistry)
- Sediment includes anything collected by a grab or corer, including
the fluff layer from the top of the consolidated sediment
- **Alternate labels:**
Sed_CarotPig, 
Sed_CarotPig, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CARS


[]{#casd}

###  Concentration of carbohydrates, phenols, alkanols (alcohols), ethers, aldehydes and ketones in sediment
- Child of:
 [`D0100001`](#D0100001)
 [`C050`](#C050)
 [`sedimentorganicchemistry`](#sedimentorganicchemistry)
- Concentrations of carbohydrates, phenols, alkanols (alcohols),
ethers,aldehydes and simple (non-alkenone) ketones in unlithified
sediment (material collected by a corer including fluff).
- **Alternate labels:**
CarbPhenolAlkanolEtherAldKetSed, 
CarbPhenolAlkanolEtherAldKetSed, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CASD


[]{#ca11}

####  Concentration of alkanols (alcohols), phenols and ethers in sediment
- Child of:
 [`D0100001`](#D0100001)
 [`CASD`](#CASD)
- Concentration of alkanols, phenols and ethers per unit mass or unit
volume of sediment (material collected by a corer including fluff)
- **Alternate labels:**
Sed_Alkanol+Phenol+Ethers
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CA11


[]{#catx}

###  Phytoplankton taxonomic biomass in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Any parameterisation of biomass (e.g. wet weight, dry weight,
carbon, nitrogen etc.) of free-floating autotrophic biological
entities identified by their taxonomic names (e.g. family, genus,
species) in any body of fresh or salt water.
- **Alternate labels:**
PhytoTaxaBiomWater, 
PhytoTaxaBiomWater, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CATX


[]{#cbcc}

###  Bacteria morphology and physiology
- Child of:
 [`D0100001`](#D0100001)
 [`B005`](#B005)
- Parameters describing the size, shape or physiological activity of
bacteria, defined as Kingdom Monera (includes cyanobacteria).
Includes parameters both parameters mapped to taxa and those mapped to
non-taxonomic groupings.
- **Alternate labels:**
Bacteria_morph+physio, 
Bacteria_morph+physio, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CBCC


[]{#cbsd}

###  Carbon concentrations in sediment
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C005`](#C005)
 [`sedimentchemistry`](#sedimentchemistry)
- Concentrations of total, organic and inorganic carbon per unit
weight of sediment.  Sediment is understood to be the solid phase of
the bed, including the recently settled material sometimes known as
fluff collected from the bed surface.
- **Alternate labels:**
Sed_Carb, 
Sed_Carb, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CBSD


[]{#cbsp}

###  Carbon concentrations in suspended particulate material
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C005`](#C005)
 [`G015`](#G015)
- Concentrations of total, organic and inorganic carbon per unit
weight of suspended particulate material collected by water column
filtration, centrifugation or sediment trapping.
- **Alternate labels:**
SPM_C, 
SPM_C, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CBSP


[]{#ccpw}

###  Carbonate chemistry in sediment pore waters
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C010`](#C010)
 [`G050`](#G050)
- Carbonate system parameters (DIC/TCO2, pH, alkalinity, pCO2) in
sediment pore waters
- **Alternate labels:**
SedPoreWat_CarbChem, 
SedPoreWat_CarbChem, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CCPW


[]{#cdru}

###  Metal uptake rates in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`O010`](#O010)
- Parameters relating to the uptake rates of metals from the dissolved
phase into the particulate phase
- **Alternate labels:**
WC_MetalUptake, 
WC_MetalUptake, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CDRU


[]{#cdta}

###  Air temperature
- Child of:
 [`D0100001`](#D0100001)
- Parameters quantifying the degree of hotness of the atmosphere.
Specifically excludes indirect measurements of other parameters such
as wet bulb temperatures.
- **Alternate labels:**
Air_temp, 
Air_temp, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CDTA


[]{#cebh}

###  Cetacean behaviour
- Child of:
 [`D0100001`](#D0100001)
 [`B015`](#B015)
- Parameters describing the actions or reactions of cetaceans (Order
Cetacea), usually in response to the environment. Includes both
parameters mapped to taxa and those mapped to non-taxonomic groupings.
- **Alternate labels:**
Cetac_Behav, 
Cetac_Behav, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CEBH


[]{#cemo}

###  Cetacean mortality
- Child of:
 [`D0100001`](#D0100001)
 [`B015`](#B015)
- Parameters describing the causes and rate of mortality in cetaceans
(Order Cetacea). Includes both parameters mapped to taxa and those
mapped to non-taxonomic groupings.
- **Alternate labels:**
Cetac_Mort, 
Cetac_Mort, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CEMO


[]{#cemp}

###  Cetacean morphology and physiology
- Child of:
 [`D0100001`](#D0100001)
 [`B015`](#B015)
- Parameters describing the size, shape or physiological activity
including disease and parasite infection status of cetaceans (Order
Cetacea). Includes both parameters mapped to taxa and those mapped to
non-taxonomic groupings.
- **Alternate labels:**
Cetac_Morph_Phys, 
Cetac_Morph_Phys, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CEMP


[]{#ceta}

###  Cetacean abundance
- Child of:
 [`D0100001`](#D0100001)
 [`B015`](#B015)
- Parameters that specify the number of specified members of Order
Cetacea present at a particular time and location, including
presence/absence indicators.
- **Alternate labels:**
Cetac_abund, 
Cetac_abund, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CETA


[]{#cftm}

###  Contaminant fluxes between the terrestrial and marine environment
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`H001`](#H001)
 [`O005`](#O005)
- Parameters quanitifying the transfer of substances considered
harmful from land to sea, including river discharge rates of
contaminant species (but not freshwater discharge rates).
- **Alternate labels:**
ContamFlux, 
ContamFlux, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CFTM


[]{#chex}

###  Cloud cover height and extent
- Child of:
 [`D0100001`](#D0100001)
- Parameters describing the horizontal and vertical extent of cloud
cover
- **Alternate labels:**
Atm_CloudCover, 
Atm_CloudCover, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CHEX


[]{#chum}

###  Atmospheric humidity
- Child of:
 [`D0100001`](#D0100001)
- Parameters that either quantify the water content of moist air or
are specifically used in its determination (eg wet bulb air
temperature)
- **Alternate labels:**
Humidity, 
Humidity, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CHUM


[]{#clay}

###  Mineralogical composition
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`G045`](#G045)
- Parameters describing or quantifying the mineralogical composition
of rocks and unlithified sediments.
- **Alternate labels:**
Min_comp, 
Min_comp, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CLAY


[]{#clty}

###  Cloud type
- Child of:
 [`D0100001`](#D0100001)
- Parameters that classify cloud cover into types such as cumulus and
cirrus.
- **Alternate labels:**
Atm_CloudType, 
Atm_CloudType, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CLTY


[]{#clxx}

###  Concentration of inorganic halogens in sediment pore waters
- Child of:
 [`D0100001`](#D0100001)
 [`C045`](#C045)
- Concentrations of halogens as elements or their inorganic compounds
in all phases of sediment pore water
- **Alternate labels:**
SedPoreWater_Halogen, 
SedPoreWater_Halogen, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CLXX


[]{#cmfl}

###  Variable fluorescence parameters
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`O010`](#O010)
- Parameters measured by variable fluorescence instruments such as
pump and probe and fast repetition rate fluorometers
- **Alternate labels:**
Var_fluor, 
Var_fluor, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CMFL


[]{#cndc}

###  Electrical conductivity of the water column
- Child of:
 [`D0100001`](#D0100001)
 [`D025`](#D025)
- Parameters quantifying the flow of electrical current through or the
electrical resistance of a body of water at any point between the bed
and the atmosphere
- **Alternate labels:**
WC_Cond, 
WC_Cond, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CNDC


[]{#cntx}

###  Phytoplankton generic biomass in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Any parameterisation of biomass (e.g. wet weight, dry weight,
carbon, nitrogen etc.) of free-floating autotrophic biological
entities designated by terms other than taxonomic names (e.g.
microphytoplankton, ciliate, flagellate) in any body of fresh or salt
water.
- **Alternate labels:**
PhytoGenBiomWater, 
PhytoGenBiomWater, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CNTX


[]{#coas}

###  Terrestrial mapping
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`T001`](#T001)
- Parameters relating to the mapping of terrestrial features,
including coastlines
- **Alternate labels:**
Land_map, 
Land_map, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/COAS


[]{#cocc}

###  Colloidal organic carbon concentration in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`C005`](#C005)
- Colloidal organic carbon per unit volume of the water column.
- **Alternate labels:**
Colloid_OrgC, 
Colloid_OrgC, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/COCC


[]{#coge}

###  Coastal geomorphology
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`T001`](#T001)
- All parameters associated with coastal landforms such as beaches and
dunes including morphology, evolution and associated transport
phenomena
- **Alternate labels:**
Coast_Geomorph, 
Coast_Geomorph, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/COGE


[]{#cpcn}

###  Unclassified pigment concentrations in sediment
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B035`](#B035)
 [`sedimentproperties`](#sedimentproperties)
- Includes all pigments that cannot be explicitly classified as
chlorophylls, phaeopigments or carotenoids (usually groups of
pigments). Sediment includes anything collected by a grab or corer,
including the fluff layer from the top of the consolidated sediment.
- **Alternate labels:**
Sed_Pigments, 
Sed_Pigments, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CPCN


[]{#cprp}

###  Precipitation and evaporation
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Parameters relating to all kinds of precipitation (rain, snow, etc.)
and water loss from the surface of the Earth
- **Alternate labels:**
Precip+Evap, 
Precip+Evap, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CPRP


[]{#cpsd}

###  Chlorophyll pigment concentrations in sediment
- Child of:
 [`D0100001`](#D0100001)
 [`B035`](#B035)
 [`sedimentorganicchemistry`](#sedimentorganicchemistry)
- Includes all variants of chlorophyll.  Sediment includes anything
collected by a grab or corer, including the fluff layer from the top
of the consolidated sediment
- **Alternate labels:**
Sed_ChlPigs, 
Sed_ChlPigs, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CPSD


[]{#cpwc}

###  Chlorophyll pigment concentrations in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`B035`](#B035)
- Includes all variants of chlorophyll expressed in terms of per unit
volume, per unit area of any body of fresh or salt water, or as a
relative colour index (e.g. PCI). Does not include data expressed per
unit mass of SPM.
- **Alternate labels:**
WC_ChlPigs, 
WC_ChlPigs, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CPWC


[]{#crys}

###  Snow and ice mass, thickness and extent
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Measurements of quantity (mass), thickness and spatial extent of
snow and ice
- **Alternate labels:**
SnowIce_Amount, 
SnowIce_Amount, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CRYS


[]{#csde}

###  Organic sulphur compound dynamics in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`O010`](#O010)
- Parameters relating to the rates of creation and consumption of
organic sulphur compounds (such as DMS and carbonyl sulphide) in the
water column
- **Alternate labels:**
WC_OrgSulphDyn, 
WC_OrgSulphDyn, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CSDE


[]{#cslr}

###  Solar Radiation
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Parameters quantifying the irradiance of the sun impinging on the
Earth's surface in the visible and infra-red waveband, generally
accepted as wavelengths between 300 and 3000 nm
- **Alternate labels:**
Sol_Rad, 
Sol_Rad, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CSLR


[]{#cyeu}

###  Plankton biomass expressed as carbon per unit volume of the water column
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Used for plankton carbon biomass parameters where no differentiation
between phytoplankton, microzooplankton or zooplankton is possible
- **Alternate labels:**
WC_PlanktonCarbBiomass, 
WC_PlanktonCarbBiomass, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/CYEU


[]{#d000}

###  Microphytobenthos abundance
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Any quantification of the number (e.g. count, abundance) of
microalgae present on hard substrate or soft sediment at the bottom of
any body of fresh or salt water.
- **Alternate labels:**
Sed_MicroPhytoAbund, 
Sed_MicroPhytoAbund, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/D000


[]{#dalk}

###  Concentration of alkanes in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`C025`](#C025)
- Alkane concentration parameters (including saturation of gaseous
species) in all phases of the water column.  Does not include
parameters expressed per unit weight of SPM.
- **Alternate labels:**
WC_alkane, 
WC_alkane, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/DALK


[]{#dbdx}

###  Geological sample density
- Child of:
 [`D0100001`](#D0100001)
 [`G040`](#G040)
- Parameters that describe the the mass per unit volume of any samples
of rock or unlithified sediment.
- **Alternate labels:**
GeoSampDens, 
GeoSampDens, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/DBDX


[]{#dcmx}

###  Other halocarbon concentrations in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C020`](#C020)
- Concentrations of volatile halocarbons (compounds comprising carbon
atoms covalently bonded to fluorine, chlorine, bromine or iodine
atoms) other than tracers (i.e. freons/chlorofluorocarbons) and
contaminants in any body of fresh or salt water.
- **Alternate labels:**
Haloc_WC, 
Haloc_WC, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/DCMX


[]{#dens}

###  Other physical and chemical properties of suspended particulate material
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`G015`](#G015)
- Parameters that do not easily fit into any of the other SPM data
categories.
- **Alternate labels:**
SPM_Properties, 
SPM_Properties, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/DENS


[]{#dgpw}

###  Dissolved oxygen parameters for sediments
- Child of:
 [`D0100001`](#D0100001)
 [`C015`](#C015)
 [`G050`](#G050)
- All parameters (including concentration, saturation, turnover and
fluxes) for dissolved oxygen in sediment and sediment pore waters.
- **Alternate labels:**
Sed_O2, 
Sed_O2, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/DGPW


[]{#dmst}

###  Organosulphur and organoselenium species concentration parameters in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C050`](#C050)
- All organosulphur and organoselenium compound concentration
parameters (including saturations for gaseous species) in all phases
of any body of fresh or salt water.
- **Alternate labels:**
WC_OrgS, 
WC_OrgS, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/DMST


[]{#docc}

###  Dissolved organic carbon concentration in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`C005`](#C005)
- DOC per unit volume of the water column.  Note that this includes
some parameters that are strictly defined as total carbon, because the
water was unfiltered on the assumption that POC was negligible.
- **Alternate labels:**
DOC, 
DOC, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/DOCC


[]{#docu}

###  Dissolved organic carbon uptake and production in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`O010`](#O010)
- Any parameter relating to the rate of DOC concentration change in
the water column
- **Alternate labels:**
DOC_dyn_WC, 
DOC_dyn_WC, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/DOCU


[]{#doxy}

###  Dissolved oxygen parameters in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`C015`](#C015)
- All dissolved oxygen parameters (including saturation and
utilisation) for the water column
- **Alternate labels:**
WC_O2, 
WC_O2, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/DOXY


[]{#dpev}

###  Depositional environment
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`GSED`](#GSED)
- Parameters characterising the environment in which sediments were
deposited either by observation or interpretation of sedimentary rocks
and unlithified sediments.
- **Alternate labels:**
Dep_env, 
Dep_env, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/DPEV


[]{#dvlp}

###  Zooplankton and zoobenthos development stage parameters
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B027`](#B027)
 [`B045`](#B045)
- Development stage parameters (such as proportion but excluding
abundance or biomass) of zooplankton and zoobenthos. Benthic and
planktonic animals have not been seggregated because there is a degree
of overlap (eg shrimps).
- **Alternate labels:**
Animal_devlopment, 
Animal_devlopment, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/DVLP


[]{#engp}

###  Engineering parameters
- Child of:
 [`D0100001`](#D0100001)
 [`Z005`](#Z005)
- Technical parameters that provide information on how well an
instrument or data acquisition system is working
- **Alternate labels:**
Engineer, 
Engineer, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/ENGP


[]{#ewsb}

###  Wind strength and direction
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Parameters quantifying the extent or direction of atmospheric
movement. Obvious examples are wind velocity, windspeed and wind
direction, but can also include derived parameters such as force,
energy, power and power density.
- **Alternate labels:**
WindStrenDir, 
WindStrenDir, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/EWSB


[]{#exco}

###  Light extinction and diffusion coefficients
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`D015`](#D015)
- Parameters relating to the extent of light penetration into the
water column
- **Alternate labels:**
Extco, 
Extco, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/EXCO


[]{#excr}

###  Excretion rate parameters in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`B027`](#B027)
 [`O010`](#O010)
- Includes all parameters relating to all mechanisms of waste release
except respiration.
- **Alternate labels:**
WC_Excretion, 
WC_Excretion, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/EXCR


[]{#f001}

###  Water body lipid concentrations
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Lipids are defined as small water-insoluble biomolecules including
fats, fatty acids, esters, sterols, isoprenoid compounds, etc..  Water
body includes any body of fresh or salt water. As lipids are insoluble
in water the concencentrations are associated with the particulate
phase.
- **Alternate labels:**
WC_Lipids, 
WC_Lipids, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/F001


[]{#fabd}

###  Fauna abundance per unit area of the bed
- Child of:
 [`D0100001`](#D0100001)
- Any fauna (class Animalia) abundance per unit are of sea, river or
lake bed.  Broad group overlapping a number of more specific groups
that should be used preferentially, but this group is provided as an
alternative to one-to-many mappings.
- **Alternate labels:**
Faun_abuns_bed, 
Faun_abuns_bed, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/FABD


[]{#fbab}

###  Fish taxonomy-related abundance per unit area of the bed
- Child of:
 [`D0100001`](#D0100001)
- Fish (Osteichthyes, Agnatha and Chondrichthyes) abundance per unit
area of bed (sea, river, lake etc.) parameters presented at the level
of taxa that may be mapped to entities in a standard taxonomy registry
such as WoRMS or ITIS.  Includes animals normally considered as
planktonic if they have been returned from sediment samples.
- **Alternate labels:**
Fish_tax_aubund_bed, 
Fish_tax_aubund_bed, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/FBAB


[]{#fbaf}

###  Fish taxonomy-related ash-free dry weight biomass per unit area of the bed
- Child of:
 [`D0100001`](#D0100001)
- Fish (Osteichthyes, Agnatha and Chondrichthyes) ash-free dry weight
biomass per unit area of bed (sea, river, lake etc.) parameters
presented at the level of taxa that may be mapped to entities in a
standard taxonomy registry such as WoRMS or ITIS.  Includes animals
normally considered as planktonic if they have been returned from
sediment samples.
- **Alternate labels:**
Fish_tax_afdw_biomass, 
Fish_tax_afdw_biomass, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/FBAF


[]{#fcnt}

###  Fish taxonomy-related counts
- Child of:
 [`D0100001`](#D0100001)
- Fish (Osteichthyes, Agnatha and Chrondrichthyes) count parameters
presented at the level of taxa that may be mapped to entities in a
standard taxonomy registry such as WoRMS or ITIS.  These may be at any
taxonomic level from sub-species upwards. Count includes
presence/absence indicators.
- **Alternate labels:**
Fish_taxa_count, 
Fish_taxa_count, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/FCNT


[]{#fcrt}

###  Zooplankton feeding
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B045`](#B045)
 [`O010`](#O010)
- Parameters quantifying the ingestion of food by zooplankton
(mesozooplankton and larger but excluding fish) in terms of identified
biota or chemical species and the effects of nutrition on life
processes such as physiology and reproduction.
- **Alternate labels:**
Zoopl_feeding, 
Zoopl_feeding, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/FCRT


[]{#fntx}

###  Fish non taxonomy-related abundance per unit volume of the water column
- Child of:
 [`D0100001`](#D0100001)
- Fish (Osteichthyes, Agnatha and Chrondrichthyes) abundance per unit
volume parameters not included under FATX.  Most commonly used for the
generic term 'fish' that maps to multiple taxa.
- **Alternate labels:**
Fish_nontaxa_abund, 
Fish_nontaxa_abund, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/FNTX


[]{#foca}

###  Seal abundance
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B015`](#B015)
- Parameters related to the distribution of true seals (Phocidae),
eared seals (Otariidae) and walruses (Odobenidae)at a particular time
and location, including presence/absence indicators.
- **Alternate labels:**
Seal_Abund, 
Seal_Abund, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/FOCA


[]{#fr11}

###  Chlorofluorocarbon concentrations in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`C020`](#C020)
- Concentrations of chlorofluorocarbons (also known as freons or CFCs)
in sny body of water
- **Alternate labels:**
WC_Freon, 
WC_Freon, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/FR11


[]{#fvlt}

###  Raw fluorometer output
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B035`](#B035)
- Output as logged from any type fluorometer.
- **Alternate labels:**
RawFluorometerOutput, 
RawFluorometerOutput, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/FVLT


[]{#goxp}

###  Oxygen production and respiration in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`O010`](#O010)
- Parameters related to the rates of oxygen production and consumption
- **Alternate labels:**
WC_O2Prod+Resp, 
WC_O2Prod+Resp, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/GOXP


[]{#gp001}

###  Pollution events
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`H001`](#H001)
- Parameters quantifying the accidental spillage of liquid or dry
pollutants from vessels or marine industries. Parameters may include
quantities of pollutant, areas affected and event duration.
- **Alternate labels:**
PollutEvnt, 
PollutEvnt, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/GP001


[]{#gp004}

###  Bird reproduction
- Child of:
 [`B25`](#B25)
 [`D0100001`](#D0100001)
- Parameters related to the reproduction of birds (Class Aves)
- **Alternate labels:**
BirdRepr, 
BirdRepr, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/GP004


[]{#gp010}

###  Bioassay and contaminant biological impact
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B060`](#B060)
- Parameters describing the effects of substances on living organisms.
- **Alternate labels:**
BiolImpact, 
BiolImpact, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/GP010


[]{#gp012}

###  Macroalgae and seagrass infection and damage
- Child of:
 [`D0100001`](#D0100001)
 [`B055`](#B055)
 [`B060`](#B060)
- Parameters relating to diseases and parasites of macroalgae
(Rhodophycota, Chromphycota, Chlorophycota)  and seagrass (Charophyta,
Anthophyta) and damage to seagrass beds
- **Alternate labels:**
AlgaeDis, 
AlgaeDis, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/GP012


[]{#gp018}

###  Cetacean reproduction
- Child of:
 [`D0100001`](#D0100001)
 [`B015`](#B015)
- Parameters related to the reproduction of cetaceans (Order Cetacea)
- **Alternate labels:**
CetacRepr, 
CetacRepr, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/GP018


[]{#gp025}

###  Seal reproduction
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B015`](#B015)
- Parameters related to the reproduction of true seals (Phocidae),
eared seals (Otariidae) and walruses (Odobenidae).
- **Alternate labels:**
SealRepr, 
SealRepr, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/GP025


[]{#gp067}

###  Reptile disease and parasites
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B015`](#B015)
 [`B060`](#B060)
- Parameters relating to diseases and parasites of reptiles (Class
Reptilia)
- **Alternate labels:**
ReptDis, 
ReptDis, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/GP067


[]{#gp068}

###  Reptile abundance
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B015`](#B015)
- Parameters related to the abundance of reptiles (Class Reptilia)
- **Alternate labels:**
ReptAbund, 
ReptAbund, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/GP068


[]{#gp069}

###  Reptile reproduction
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B015`](#B015)
- Parameters related to the reproduction of reptiles (Class Reptilia)
- **Alternate labels:**
ReptRepr, 
ReptRepr, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/GP069


[]{#gp079}

###  Zooplankton wet weight biomass
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B045`](#B045)
- Zooplankton (mesozooplankton and larger, exclusing fish, mammals,
reptiles and insects) biomass determined by weighing unprocessed catch
samples.
- **Alternate labels:**
ZooplWWBiom, 
ZooplWWBiom, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/GP079


[]{#gp087}

###  Fishery characterisation
- Child of:
 [`D0100001`](#D0100001)
 [`H004`](#H004)
- Parameters describing the extent, intensity, timing and method of
fisheries
- **Alternate labels:**
Fisheries, 
Fisheries, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/GP087


[]{#gp080}

####  Fishing by-catch
- Child of:
 [`GP087`](#GP087)
 [`H004`](#H004)
- Parameters quantifying the capture of non-target species during
commercial and non-commercial fishing trips
- **Alternate labels:**
ByCatch, 
ByCatch, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/GP080


[]{#gp088}

###  Bird behaviour
- Child of:
 [`B25`](#B25)
 [`D0100001`](#D0100001)
- Parameters describing the actions or reactions of birds (Class
Aves), usually in response to the environment. Includes both
parameters mapped to taxa and those mapped to non-taxonomic groupings.
- **Alternate labels:**
BirdBehav, 
BirdBehav, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/GP088


[]{#gpig}

###  Zooplankton gut pigments
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B035`](#B035)
 [`B045`](#B045)
- Parameters identifying or quantifying zooplankton gut pigments
- **Alternate labels:**
GutPig, 
GutPig, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/GPIG


[]{#grav}

###  Gravity
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`G005`](#G005)
 [`GPYS`](#GPYS)
- Parameters relating to the measurement of the Earth's gravity field
- **Alternate labels:**
Gravity, 
Gravity, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/GRAV


[]{#gref}

###  Bacterial growth
- Child of:
 [`D0100001`](#D0100001)
 [`B005`](#B005)
 [`O010`](#O010)
-
- **Alternate labels:**
Bact_Growth, 
Bact_Growth, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/GREF


[]{#grzo}

###  Zooplankton growth rates
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B045`](#B045)
 [`O010`](#O010)
- Parameters pertaining to zooplankton growth rates including
biochemical proxies such as AARS activity
- **Alternate labels:**
ZooplGrowthRate, 
ZooplGrowthRate, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/GRZO


[]{#gtch}

###  Geotechnics
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`H002`](#H002)
- Parameters quantifying the properties of rocks and sediments that
are relevance to engineering such as physical strength and load-
bearing capacity.  Includes the disciplines of rock mechanics and soil
mechanics.
- **Alternate labels:**
GeoTech, 
GeoTech, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/GTCH


[]{#gwam}

###  Groundwater amount
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`T001`](#T001)
- Parameters quantifying the amount of groundwater in a given system
such as aquifer water level and rate of flow of water through rock
formations.
- **Alternate labels:**
GwaterAmt, 
GwaterAmt, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/GWAM


[]{#gwch}

###  Groundwater chemistry
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`T001`](#T001)
- Parameters quantifying the chemistry of terrestrial groundwater
bodies such as aquifers and waters percolating through rock
formations.
- **Alternate labels:**
GwaterChem, 
GwaterChem, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/GWCH


[]{#gwdr}

###  Wave direction
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`D034`](#D034)
- Direct measurements (including visual estimates) plus statistically
derived parameters
- **Alternate labels:**
WaveDir, 
WaveDir, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/GWDR


[]{#haac}

###  Amino acids in sediment
- Child of:
 [`D0100001`](#D0100001)
 [`C003`](#C003)
 [`sedimentorganicchemistry`](#sedimentorganicchemistry)
- Parameters quantifying the amount of organic compounds containing
both a carboxyl group and an amino group in unlithified seabed
material.
- **Alternate labels:**
Sed_AminoAcids, 
Sed_AminoAcids, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/HAAC


[]{#head}

###  Platform or instrument orientation
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`Z005`](#Z005)
- Parameters that describe the displacement of platforms or
instruments in space relative to various origins
- **Alternate labels:**
PlatOrientation, 
PlatOrientation, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/HEAD


[]{#heav}

###  Wave height estimates
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`D034`](#D034)
- Measurements of wave height that are not based on the statistical
analysis of wave records, such as heave, surface roughness and visual
height estimates
- **Alternate labels:**
WaveHeight, 
WaveHeight, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/HEAV


[]{#hexc}

###  Dissolved noble gas concentration parameters in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`C015`](#C015)
- All concentration parameters including saturations and statistics
such as standard deviations
- **Alternate labels:**
WC_NobleGas, 
WC_NobleGas, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/HEXC


[]{#hlwc}

###  Concentration of inorganic halogens in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`C045`](#C045)
- Concentrations of halogens as elements or their inorganic compounds
in all phases of any body of fresh or salt water
- **Alternate labels:**
WC_Halogen, 
WC_Halogen, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/HLWC


[]{#hmsb}

###  Concentration of organic matter in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`C050`](#C050)
- Concentration (not 380nm light absorption) parameters for dissolved
or total organic matter (includes humics, yellow matter, Gelbstoff) in
any body of salt or fresh water.
- **Alternate labels:**
Org_Mat_Water, 
Org_Mat_Water, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/HMSB


[]{#hznv}

###  Hazards to navigation
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`H002`](#H002)
 [`H016`](#H016)
- Parameters describing the location, nature and extent of objects
that pose a threat to travel on the water column such as wrecks and
obstructions
- **Alternate labels:**
HazNav, 
HazNav, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/HZNV


[]{#iage}

###  Ice age
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Measured or stratigraphically estimated age of ice
- **Alternate labels:**
Age_Ice, 
Age_Ice, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/IAGE


[]{#ialz}

###  Insect and earthworm taxonomy-related ash-free dry weight biomass per unit area of the littoral zone
- Child of:
 [`D0100001`](#D0100001)
- Insect (Class Insecta) and earthworm (Subclass Oligochaeta) ash-free
dry weight biomass per unit area of the littoral zone (between spring
tide high and low water) parameters.
- **Alternate labels:**
Littoral_TaxInsectWormAFDW, 
Littoral_TaxInsectWormAFDW, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/IALZ


[]{#iatx}

###  Insecta taxonomy-related abundance per unit volume of the water column
- Child of:
 [`D0100001`](#D0100001)
 [`B045`](#B045)
- Insecta abundance parameters presented at the level of taxa that may
be mapped to entities in a standard taxonomy registry such as WoRMS or
ITIS.  These may be at any taxonomic level from sub-species upwards.
- **Alternate labels:**
Insect_taxa_abund, 
Insect_taxa_abund, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/IATX


[]{#icem}

###  Ice motion and related parameters
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Parameters specifying the speed and direction of sea or land ice and
the stresses associated with this motion.
- **Alternate labels:**
Ice_motion, 
Ice_motion, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/ICEM


[]{#ichm}

###  Snow and ice chemistry
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Parameters related to the chemical composition of any kind of water
sample that was frozen solid at the time of sampling or measurement
- **Alternate labels:**
SnowIce_Chem, 
SnowIce_Chem, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/ICHM


[]{#idis}

###  Industrial discharges
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`H001`](#H001)
- Parameters that quantify and specify material output into the
environment as a result of industrial activity
- **Alternate labels:**
IndDisch, 
IndDisch, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/IDIS


[]{#inlz}

###  Insect and earthworm taxonomy-related abundance per unit area of the littoral zone
- Child of:
 [`D0100001`](#D0100001)
- Insect (Class Insecta) and earthworm (Subclass Oligochaeta)
abundance per unit area of the littoral zone (between spring tide high
and low water) parameters.
- **Alternate labels:**
InsWorm_Tax_Litabund, 
InsWorm_Tax_Litabund, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/INLZ


[]{#iphy}

###  Snow and ice physical properties and characteristics
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Parameters related to physical properties (e.g. colour, density, in-
situ temperature) or characteristics (e.g. sea ice type) of any kind
of water sample that was in its solid state at the time of sampling or
measurement
- **Alternate labels:**
SnowIce_PhysChar, 
SnowIce_PhysChar, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/IPHY


[]{#irbo}

###  Stable isotopes in biota
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B007`](#B007)
 [`C030`](#C030)
- Stable isotope parameters (concentrations, ratios and enrichments)
from measurements on living (at the time of sampling) organisms or
parts thereof.
- **Alternate labels:**
Iso_Biota, 
Iso_Biota, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/IRBO


[]{#irsp}

###  Stable isotopes in speleothems
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`G035`](#G035)
- Stable isotope parameters (concentrations, ratios and enrichments)
in secondary mineral deposits in caves. This includes stalactites,
stalagmites, flowstone, and crystal growths.
- **Alternate labels:**
Iso_Speleo, 
Iso_Speleo, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/IRSP


[]{#iwab}

###  Insect and earthworm taxonomy-related abundance per unit area of the bed
- Child of:
 [`D0100001`](#D0100001)
- Insect (Class Insecta) and earthworm (Subclass Oligochaeta)
abundance per unit area of bed (sea, river, lake etc.) parameters
presented at the level of taxa that may be mapped to entities in a
standard taxonomy registry such as WoRMS or ITIS.  Includes animals
normally considered as planktonic if they have been returned from
sediment samples. This parameter group has been implemented to
separate predominantly freshwater taxa from predominantly marine taxa.
- **Alternate labels:**
InsWorm_tax_abund_bed, 
InsWorm_tax_abund_bed, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/IWAB


[]{#iwdx}

###  Insect and earthworm taxonomy-related ash-free dry weight biomass per unit area of the bed
- Child of:
 [`D0100001`](#D0100001)
- Insect (Class Insecta) and earthworm (Subclass Oligochaeta) ash-free
dry weight biomass per unit area of bed (sea, river, lake etc.)
parameters presented at the level of taxa that may be mapped to
entities in a standard taxonomy registry such as WoRMS or ITIS.
Includes animals normally considered as planktonic if they have been
returned from sediment samples. This parameter group has been
implemented to separate predominantly freshwater taxa from
predominantly marine taxa.
- **Alternate labels:**
InsWorm_tax_afdw_biomass, 
InsWorm_tax_afdw_biomass, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/IWDX


[]{#krts}

###  Other wave statistics
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`D034`](#D034)
- Statistical parameters derived from wave data expressing wave
properties other than height, period and direction
- **Alternate labels:**
Oth_WaveStat, 
Oth_WaveStat, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/KRTS


[]{#lerr}

###  Raw current meter output parameters
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Parameters as logged by measuring devices, including raw
counts/voltages and ADCP relative velocities
- **Alternate labels:**
Raw_CM_Parm, 
Raw_CM_Parm, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/LERR


[]{#lgcr}

###  Lagrangian currents and transport rates in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Parameters expressing the mean nett transport rates within the water
column like Lagrangian currents. Note this is an unintentional
duplicate of VDFC.
- **Alternate labels:**
Lagran_Currents_WC, 
Lagran_Currents_WC, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/LGCR


[]{#libi}

###  Biota lipid concentrations
- Child of:
 [`D0100001`](#D0100001)
 [`B007`](#B007)
- Lipids are defined as small water-insoluble biomolecules including
fats, fatty acids, esters, sterols, isoprenoid compounds, etc..  Biota
includes any type of sample originating from a living organism.
- **Alternate labels:**
Lipid_Biota, 
Lipid_Biota, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/LIBI


[]{#lith}

###  Lithology
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`G045`](#G045)
- Parameters describing rocks on the basis of physical characteristics
such as colour, structure, mineralogy and grain size
- **Alternate labels:**
Lithology, 
Lithology, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/LITH


[]{#litt}

###  Litter abundance and type
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`H001`](#H001)
- Parameters describing the abundance and nature of material classed
as refuse introduced to the environment by activities of man that are
not covered by the more specific P02 terms for micro-litter (UMLS and
UMLW), beach litter (BLIT) or seafloor litter (SLIT).
- **Alternate labels:**
Litter, 
Litter, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/LITT


[]{#lsst}

###  Land surface temperature
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`T001`](#T001)
- Parameters relating to land surface temperature including fire and
other hot spot location
- **Alternate labels:**
LandTemp, 
LandTemp, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/LSST


[]{#lveg}

###  Land vegetation
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`T001`](#T001)
- Parameters relating to land (including marshes and the intertidal
zone) vegetation
- **Alternate labels:**
LandVeg, 
LandVeg, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/LVEG


[]{#lvlt}

###  Raw light meter output
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`D015`](#D015)
-
- **Alternate labels:**
RawLightOutput, 
RawLightOutput, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/LVLT


[]{#lwet}

###  Terrestrial water content
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`T001`](#T001)
- Parameters relating to the water held by land masses such as soil
and vegetation moisture content
- **Alternate labels:**
LandWet, 
LandWet, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/LWET


[]{#lwrd}

###  Long-wave radiation
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
-
- **Alternate labels:**
LWRad, 
LWRad, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/LWRD


[]{#matc}

###  Microzooplankton taxonomy-related biomass expressed as carbon per unit volume of the water column
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Microzooplankton carbon biomass parameters presented at the level of
taxa that may be mapped to entities in a standard taxonomy registry
such as WoRMS or ITIS.  These may be at any taxonomic level from sub-
species upwards., but exclude morphological classifications such as
'heterotrophic flagellate'.
- **Alternate labels:**
Microzoo_taxa_C_biomass, 
Microzoo_taxa_C_biomass, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/MATC


[]{#matx}

###  Microzooplankton taxonomic abundance in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Any enumeration (e.g. count, number per litre) of microzooplankton
(free swimming heterotrophic organisms smaller than 200um) designated
by taxonomic names (e.g. species, genus or family) in any fresh or
salt water body.
- **Alternate labels:**
MicrozooTaxaAbundWater, 
MicrozooTaxaAbundWater, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/MATX


[]{#mban}

###  Bathymetry and Elevation
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Depth of the water column or elevation of land surface relative to
sea surface, geoid or other datum
- **Alternate labels:**
Bath_Elev, 
Bath_Elev, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/MBAN


[]{#mdbo}

###  Trace metalloid concentrations in biota
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C035`](#C035)
 [`H001`](#H001)
- Concentration parameters for trace metalloid elements in either
whole organisms or their constituent parts. Trace metalloids are
considered as B, Ge, As, Sb, Te and Po (but not Si which is classed
separately because of its major role in environmental chemistry)
- **Alternate labels:**
Metoid_Biota, 
Metoid_Biota, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/MDBO


[]{#mdpw}

###  Trace metalloid concentrations in sediment pore water
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C035`](#C035)
 [`G050`](#G050)
- Concentration parameters for trace metalloid elements in water
occupying the space between sediment grains. Trace metalloids are
considered as B, Ge, As, Sb, Te and Po (but not Si which is classed
separately because of its major role in environmental chemistry)
- **Alternate labels:**
Metoid_SedPW, 
Metoid_SedPW, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/MDPW


[]{#mdsd}

###  Trace metalloid concentrations in sediment
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`sedimentinorganicchemistry`](#sedimentinorganicchemistry)
- Concentration parameters for metalloid elements in sediment.
Sediment is understood to be the solid phase of the bed, including the
recently settled material sometimes known as fluff collected from the
bed surface. Metalloids are considered as B, Ge, As, Sb, Te and Po
(but not Si which is classed separately because of its major role in
environmental chemistry)
- **Alternate labels:**
Metoid_Sed, 
Metoid_Sed, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/MDSD


[]{#mdsv}

###  Suspended particulate material setting velocity parameters
- Child of:
 [`D0100001`](#D0100001)
 [`G015`](#G015)
-
- **Alternate labels:**
SPM_SettVeloc, 
SPM_SettVeloc, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/MDSV


[]{#mdwd}

###  Dissolved trace metalloid and inorganic selenium concentrations in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`C035`](#C035)
- Concentration parameters for trace metalloid elements and non-
organic selenium species in the dissolved phase of any body of fresh
or salt water. This may include a contribution from the particulate
phase if this has not been totally removed by filtration and the
metalloid in question is reactive (ie detected as if it were
dissolved) to the analytical technique used. Trace metalloids are
considered as B, Ge, As, Sb, Te, and Po (but not Si which is classed
separately because of its major role in environmental chemistry).
- **Alternate labels:**
Metoid_WC_Diss, 
Metoid_WC_Diss, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/MDWD


[]{#mdwp}

###  Particulate trace metalloid and inorganic selenium concentrations in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C035`](#C035)
 [`G015`](#G015)
- Concentration parameters for trace metalloid elements and inorganic
selenium species in the particulate phase of any body of fresh or salt
water collected by fitration, centrifugation or sediment trapping.
Trace metalloids are considered as B, Ge, As, Sb, Te and Po (but not
Si which is classed separately because of its major role in
environmental chemistry).
- **Alternate labels:**
Metoid_WC_Part, 
Metoid_WC_Part, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/MDWP


[]{#meph}

###  Zooplankton egg hatch proportion
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B045`](#B045)
-
- **Alternate labels:**
MesozooEggHatch, 
MesozooEggHatch, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/MEPH


[]{#mfab}

###  Zoobenthos generic abundance
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Any enumeration (e.g. count, number per square metre) of animals
living on or near the seabed designated by terms other than taxonomic
names (e.g. total).
- **Alternate labels:**
ZoobenthGenAbund, 
ZoobenthGenAbund, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/MFAB


[]{#mfaz}

###  Zoobenthos taxonomy-related ash-free dry weight biomass per unit area of the littoral zone
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Any zoobenthos ash-free dry weight biomass per unit area of the
littoral zone (between spring tide high and low water) parameters that
are not fish or terrestrial animals (insecta/oligochaeta)
- **Alternate labels:**
Littoral_TaxZoobenthAFDW, 
Littoral_TaxZoobenthAFDW, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/MFAZ


[]{#mflz}

###  Zoobenthos taxonomy-related abundance per unit area of the littoral zone
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Any zoobenthos abundance per unit area of the littoral zone (between
spring tide high and low water) parameters that are not fish or
terrestrial animals (insecta/oligochaeta)
- **Alternate labels:**
Zoobenth_Tax_Litabund, 
Zoobenth_Tax_Litabund, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/MFLZ


[]{#mfww}

###  Zoobenthos non taxonomy-related wet weight biomass per unit area of the bed
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Any zoobenthos wet weight biomass per unit area of the seabed
parameters that are not included in parameter group ZWTX.
- **Alternate labels:**
ZoobenthNontaxWetWtBiomass, 
ZoobenthNontaxWetWtBiomass, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/MFWW


[]{#mman}

###  Magnetics
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`G005`](#G005)
 [`GPYS`](#GPYS)
- Parameterisations of the intensity and inclination of Earth's
magnetic field
- **Alternate labels:**
Magnetics, 
Magnetics, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/MMAN


[]{#mmst}

###  Man-made structures
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`H002`](#H002)
- Parameters relating to human built structures on the coast or
offshore and their impact on the environment.
- **Alternate labels:**
Structures, 
Structures, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/MMST


[]{#mpmn}

###  Moored instrument depth
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`Z005`](#Z005)
- Parameters expressing depth (possibly as pressure) of an instrument
on a suspended underwater mooring.  These are primarily collected to
monitor mooring performance by quantifying knock-down and should not
be regarded as instrument z co-ordinates (accurate calibration is
rare) or as sea level measurements.
- **Alternate labels:**
Depth, 
Depth, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/MPMN


[]{#msep}

###  Zooplankton reproduction rate parameters
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B045`](#B045)
 [`O010`](#O010)
- All parameters related to zooplankton reproduction rates
- **Alternate labels:**
ZooplanktonRepoduction, 
ZooplanktonRepoduction, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/MSEP


[]{#mtic}

###  Metal concentrations in the cryosphere
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C035`](#C035)
- Concentration parameters for metallic elements in ice and snow
- **Alternate labels:**
Met_Ice, 
Met_Ice, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/MTIC


[]{#mtpw}

###  Metal concentrations in sediment pore waters
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C035`](#C035)
 [`G050`](#G050)
- Concentrations of metal elements in sediment pore waters
- **Alternate labels:**
Met_SedPW, 
Met_SedPW, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/MTPW


[]{#mtsd}

###  Metal concentrations in sediment
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C035`](#C035)
 [`sedimentinorganicchemistry`](#sedimentinorganicchemistry)
- Concentrations of metal elements per unit weight of sediment.
Sediment is understood to be the solid phase of the bed, including the
recently settled material sometimes known as fluff collected from the
bed surface.
- **Alternate labels:**
Met_Sed, 
Met_Sed, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/MTSD


[]{#mtwc}

###  Colloidal metal concentrations in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`C035`](#C035)
- Concentrations of metal elements in the colloidal phase of the water
column. Usually the dissolved concentration difference between
conventionally filtered water and ultra-filtered water.
- **Alternate labels:**
Met_WC_Coll, 
Met_WC_Coll, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/MTWC


[]{#mtwd}

###  Dissolved metal concentrations in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`C035`](#C035)
- Concentrations of metal elements in the dissolved phase of the water
column.  This may include a contribution from the particulate phase if
this has not been totally removed by filtration and the metal in
question is reactive (ie detected as if it were dissolved) to the
analytical technique used.
- **Alternate labels:**
Met_WC_Diss, 
Met_WC_Diss, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/MTWD


[]{#mtwt}

###  Total metal concentrations in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C035`](#C035)
- Concentration parameters for metal elements in the combined
dissolved and particulate phases of any body of fresh or salt water.
- **Alternate labels:**
Met_WC_Tot, 
Met_WC_Tot, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/MTWT


[]{#mzbc}

###  Microzooplankton non taxonomy-related biomass expressed as carbon per unit volume of the water column
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Basically, any microzooplankton carbon biomass measurement that
isn't included in parameter group MATC.  May include data integrations
such as 'total microzooplankton'.
- **Alternate labels:**
WC_NontaxMicrozooCarbBiomass, 
WC_NontaxMicrozooCarbBiomass, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/MZBC


[]{#mzbn}

###  Microzooplankton generic abundance in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Any enumeration (e.g. count, number per litre) of microzooplankton
(free swimming heterotrophic organisms smaller than 200um) designated
by terms other than taxonomic names (e.g. total) in any fresh or salt
water body.
- **Alternate labels:**
MicrozooGenAbundWater, 
MicrozooGenAbundWater, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/MZBN


[]{#mzct}

###  Microzooplankton grazing
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`O010`](#O010)
- Parameters that express the consumption of the phytoplankton
population by the microzooplankton.  Generally the results of dilution
experiments on water samples screened through a 200-micron mesh.
- **Alternate labels:**
WC_MicrozooGraz, 
WC_MicrozooGraz, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/MZCT


[]{#noys}

###  Acoustic noise in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`D005`](#D005)
-
- **Alternate labels:**
Noise, 
Noise, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/NOYS


[]{#ntpw}

###  Nutrient concentrations in sediment pore waters
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C040`](#C040)
 [`G050`](#G050)
- Nutrient (nitrate, nitrite, ammonium, phosphate, silicate and urea)
concentrations in sediment pore waters
- **Alternate labels:**
SedPoreWat_Nuts, 
SedPoreWat_Nuts, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/NTPW


[]{#ntra}

###  Nitrate concentration parameters in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C005`](#C005)
 [`C040`](#C040)
- Nitrate concentration parameters (including statistical parameters
such as standard deviation) in the water column. Includes
nitrate+nitrite, which is often loosely referred to as nitrate.
- **Alternate labels:**
WC_NO3, 
WC_NO3, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/NTRA


[]{#ntrz}

####  Nitrate+nitrite concentration parameters in the water column
- Child of:
 [`NTRA`](#NTRA)
- Deprecated term from a misguided attempt to distinguish between NO3
and NO3+NO2 for discovery. Use parameter group NTRA instead
- **Alternate labels:**
WC_NO3+NO2, 
WC_NO3+NO2, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/NTRZ


[]{#ntri}

###  Nitrite concentration parameters in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C005`](#C005)
 [`C040`](#C040)
- Nitrite concentration parameters (including statistical parameters
such as standard deviation) in the water column
- **Alternate labels:**
WC_NO2, 
WC_NO2, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/NTRI


[]{#ntsp}

###  Nitrogen concentrations in suspended particulate material
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C005`](#C005)
 [`G015`](#G015)
- Concentrations of total, organic and inorganic nitrogen per unit
weight of suspended particulate material collected by water column
filtration, centrifugation or sediment trapping.  Note that it is
common practice to assume all nitrogen in SPM is organic.
- **Alternate labels:**
SPM_Nitrogen, 
SPM_Nitrogen, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/NTSP


[]{#ntup}

###  New production in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C040`](#C040)
 [`O010`](#O010)
- Parameters quantifying the uptake rate of nitrate or gaseous
nitrogen by flora and fauna living in any body of salt or fresh water
- **Alternate labels:**
New_prod, 
New_prod, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/NTUP


[]{#nutv}

###  Raw in-situ nutrient analyser output
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C040`](#C040)
- Direct output parameters from spectophotometric or chemical in-situ
nutrient analysers
- **Alternate labels:**
Raw_Nuts, 
Raw_Nuts, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/NUTV


[]{#ocpw}

###  Dissolved organic carbon concentrations in sediment pore waters
- Child of:
 [`D0100001`](#D0100001)
 [`C005`](#C005)
 [`G050`](#G050)
- Concentrations of dissolved organic carbon in sediment pore waters
- **Alternate labels:**
SedPoreWat_DOC, 
SedPoreWat_DOC, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/OCPW


[]{#ogpw}

###  Dissolved concentration parameters for other gases in sediment pore waters
- Child of:
 [`D0100001`](#D0100001)
 [`C015`](#C015)
- All concentration parameters for inorganic dissolved gases other
than oxygen and the noble gases in sediment pore water samples
- **Alternate labels:**
SedPoreWater_Gases, 
SedPoreWater_Gases, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/OGPW


[]{#ohwc}

###  Concentration of other hydrocarbons in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`C025`](#C025)
- 'Other' (not alkanes, alkenes, alkynes or PAHs) hydrocarbon
concentration parameters (including saturation of gaseous species) in
all phases of the water column.  Does not include parameters expressed
per unit weight of SPM.
- **Alternate labels:**
WC_UnclassHydrocarb, 
WC_UnclassHydrocarb, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/OHWC


[]{#ombi}

###  Organometallic species concentration parameters in biota
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C035`](#C035)
 [`C050`](#C050)
 [`C055`](#C055)
 [`H001`](#H001)
- All measurements of the quantity or mass of any organometallic
compound in any living organisms or their component parts
- **Alternate labels:**
Biota_OrganoMet, 
Biota_OrganoMet, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/OMBI


[]{#omet}

###  Other meteorological measurements
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Bucket group for parameters that cannot be classified elsewhere
- **Alternate labels:**
UnclassMet, 
UnclassMet, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/OMET


[]{#ompw}

###  Organometallic and organometalloid species concentration parameters in sediments
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C035`](#C035)
 [`C050`](#C050)
 [`C055`](#C055)
 [`G050`](#G050)
 [`H001`](#H001)
 [`sedimentorganicchemistry`](#sedimentorganicchemistry)
- All organometallic and orgamometalloid compound concentration
parameters (including saturations for gaseous species) in all phases
of sediments (including pore waters)
- **Alternate labels:**
Sed_OrganoMet, 
Sed_OrganoMet, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/OMPW


[]{#omwc}

###  Organometallic and organometalloid species concentration parameters in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C035`](#C035)
 [`C050`](#C050)
 [`C055`](#C055)
 [`H001`](#H001)
- All organometallic and organometalloid compound concentration
parameters (including saturations for gaseous species) in all phases
of any body of fresh or salt water.
- **Alternate labels:**
Water_OrganoMet, 
Water_OrganoMet, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/OMWC


[]{#opbs}

###  Optical backscatter
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`D015`](#D015)
- Includes all parameters covering the strength of electromagnetic
radiation signal return, including absolute measurements of returning
signal strength as well as parameters expressed as backscatter (the
proportion of transmitted signal returned)
- **Alternate labels:**
OptBS, 
OptBS, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/OPBS


[]{#opcn}

###  Concentration of silicon species in suspended particulate material
- Child of:
 [`D0100001`](#D0100001)
 [`C045`](#C045)
 [`G015`](#G015)
- Concentration parameters for silicon species (including opal) in SPM
(material gathered by filtration or sediment trapping). Only includes
parameters expressed per unit mass of SPM and not per unit volume of
the water column
- **Alternate labels:**
SPM_SiSpecies, 
SPM_SiSpecies, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/OPCN


[]{#oxyc}

###  Raw oxygen sensor output
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C015`](#C015)
- Raw parameters (usually membrane current and temperature) from
dissolved oxygen sensors
- **Alternate labels:**
RawO2Output, 
RawO2Output, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/OXYC


[]{#patx}

###  Phytoplankton taxonomic abundance in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Any enumeration (e.g. count, abundance) of free-floating autotrophic
biological entities designated by taxonomic names (e.g. species,
genus, family) in any body of fresh or salt water.
- **Alternate labels:**
PhytoTaxaAbundWater, 
PhytoTaxaAbundWater, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/PATX


[]{#pcah}

###  Concentration of polycyclic aromatic hydrocarbons (PAHs) in suspended particulate material
- Child of:
 [`D0100001`](#D0100001)
 [`C025`](#C025)
 [`C055`](#C055)
 [`G015`](#G015)
 [`H001`](#H001)
- PAH concentrations in suspended particulate material, regarded as
anything sampled by a water bottle, SAP, sediment trap etc.  This
group is for SPM composition measurements (concentration per unit
weight) and NOT concentrations per unit volume of the water column in
the particulate phase.
- **Alternate labels:**
SPM_PAH, 
SPM_PAH, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/PCAH


[]{#pchw}

###  Concentration of polycyclic aromatic hydrocarbons (PAHs) in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`C025`](#C025)
 [`C055`](#C055)
 [`H001`](#H001)
- PAH concentrations in all phases of the water column. This group
includes concentrations per unit volume of the water column in the
particulate phase, but not concentrations per unit wieght of SPM.
- **Alternate labels:**
WC_PAH, 
WC_PAH, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/PCHW


[]{#pclm}

###  Palaeoclimatic indicators and parameters
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`H003`](#H003)
- Parameterisations that describe climatic conditions in the past.
Includes climate indices, climate indicators and indirect measurements
of climate-related phenomena such as sea level and water table depth.
- **Alternate labels:**
PalaeoInd, 
PalaeoInd, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/PCLM


[]{#pcoc}

###  Concentration of other organic contaminants in suspended particulate material
- Child of:
 [`D0100001`](#D0100001)
 [`C055`](#C055)
 [`G015`](#G015)
 [`H001`](#H001)
- 'Other' organic contaminant (substances regarded as harmful other
than PCBs and PAHs) concentrations in suspended particulate material,
regarded as anything sampled by a water bottle, SAP, sediment trap
etc.  This group is for SPM composition measurements (concentration
per unit weight) and NOT concentrations per unit volume of the water
column in the particulate phase.
- **Alternate labels:**
SPM_Orgcontam, 
SPM_Orgcontam, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/PCOC


[]{#pebi}

###  Pesticide concentrations in biota
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C055`](#C055)
 [`H001`](#H001)
- Concentration parameters for substances synthesised by man to kill
other life forms in either whole organisms or their constituent parts.
- **Alternate labels:**
Pesticide_Biota, 
Pesticide_Biota, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/PEBI


[]{#pesd}

###  Pesticide concentrations in sediment
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C055`](#C055)
 [`H001`](#H001)
 [`sedimentorganicchemistry`](#sedimentorganicchemistry)
- Concentration parameters for substances synthesised by man to kill
other life forms in sediment, which is considered to be anything from
the bed sampled by a grab or corer, including 'fluff'.
- **Alternate labels:**
Pesticide_Sediment, 
Pesticide_Sediment, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/PESD


[]{#pewb}

###  Pesticide concentrations in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C055`](#C055)
 [`H001`](#H001)
- Concentration parameters for substances synthesised by man to kill
other life forms in either solution or suspension (i.e.includes
measurements in both the dissolved and particulate phases) in any body
of salt or fresh water.
- **Alternate labels:**
Pesticide_WaterBody, 
Pesticide_WaterBody, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/PEWB


[]{#phos}

###  Phosphate concentration parameters in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C005`](#C005)
 [`C040`](#C040)
- Phosphate  concentration parameters (including statistical
parameters such as standard deviation) in the water column
- **Alternate labels:**
WC_PO4, 
WC_PO4, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/PHOS


[]{#phsd}

###  Phaeopigment concentrations in sediment
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B035`](#B035)
 [`sedimentorganicchemistry`](#sedimentorganicchemistry)
- Includes all variants of phaeopigment (chlorophyll degradation
products). Sediment is defined as any solids collected by a corer,
including fluff..
- **Alternate labels:**
Sed_PhaeoPigs, 
Sed_PhaeoPigs, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/PHSD


[]{#phwb}

###  Pharmaceutical concentrations in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C055`](#C055)
 [`H001`](#H001)
- Concentration parameters for substances synthesised by man to modify
bodily function or diagnose, cure, mitigate, treat, or prevent disease
in either solution or suspension (i.e.includes measurements in both
the dissolved and particulate phases) in any body of salt or fresh
water.
- **Alternate labels:**
Pharm_WaterBody, 
Pharm_WaterBody, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/PHWB


[]{#phwc}

###  Phaeopigment concentrations in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B035`](#B035)
- Includes all variants of phaeopigment (chlorophyll degradation
products) expressed in terms of per unit volume or unit area of the
water column.  Does not include data expressed per unit mass of SPM.
- **Alternate labels:**
WC_PhaeoPigs, 
WC_PhaeoPigs, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/PHWC


[]{#phyc}

###  Phycobolin pigment concentrations in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B035`](#B035)
- Concentration of phycobolin group pigments such as phycocyanin and
phycoerythrin in the water column
- **Alternate labels:**
WC_PhycobolPig, 
WC_PhycobolPig, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/PHYC


[]{#phyg}

###  Phytoplankton growth
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`O010`](#O010)
-
- **Alternate labels:**
Phyt_Growth, 
Phyt_Growth, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/PHYG


[]{#pntx}

###  Phytoplankton generic abundance in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Any enumeration (e.g. count, abundance) of free-floating autotrophic
biological entities designated by terms other than taxonomic names
(e.g. microphytoplankton, ciliate, flagellate) in any body of fresh or
salt water.
- **Alternate labels:**
PhytoGenAbundWater, 
PhytoGenAbundWater, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/PNTX


[]{#ppab}

###  Light absorption in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`D015`](#D015)
- Water column spectral absorption parameters
- **Alternate labels:**
WC_LightAbsorb, 
WC_LightAbsorb, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/PPAB


[]{#ppcb}

###  Concentration of polychlorobiphenyls (PCBs) in suspended particulate material
- Child of:
 [`D0100001`](#D0100001)
 [`C055`](#C055)
 [`G015`](#G015)
 [`H001`](#H001)
- PCB concentrations in suspended particulate material, regarded as
anything sampled by a water bottle, SAP, sediment trap etc.  This
group is for SPM composition measurements (concentration per unit
weight) and NOT concentrations per unit volume of the water column in
the particulate phase.
- **Alternate labels:**
SPM_PCB, 
SPM_PCB, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/PPCB


[]{#pprd}

###  Primary production in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`O010`](#O010)
- Parameters associated with the quantification of primary production.
This is defined as the fixation of carbon dioxide into either organic
or inorganic carbon by living entities and so includes photosynthesis
and calcification.
- **Alternate labels:**
WC_PrimaryProd, 
WC_PrimaryProd, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/PPRD


[]{#ppwc}

###  Concentration of polychlorobiphenyls (PCBs) in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`C055`](#C055)
 [`H001`](#H001)
- PCB concentrations in all phases of the water column. This group
excludes SPM composition measurements (concentration per unit weight).
- **Alternate labels:**
WC_PCB, 
WC_PCB, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/PPWC


[]{#psal}

###  Salinity of the water column
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`D025`](#D025)
- Parameters quantifying the concentration of sodium chloride in any
body of water at any point between the bed and the atmosphere
- **Alternate labels:**
WC_Sal, 
WC_Sal, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/PSAL


[]{#ptox}

###  Concentration of phycotoxins in biota
- Child of:
 [`D0100001`](#D0100001)
- Parameters associated with the concentration of algae-generated
toxins in either whole organisms or their constituent parts
- **Alternate labels:**
Phycotox_biota, 
Phycotox_biota, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/PTOX


[]{#pu02}

###  Macroalgae generic abundance in water bodies
- Child of:
 [`D0100001`](#D0100001)
- Any enumeration (e.g. count, number per litre) of macroalgae
(seaweeds) designated by terms other than taxonomic names (e.g. total)
in any fresh or salt water body.
- **Alternate labels:**
MacAlgaeGenAbundWater, 
MacAlgaeGenAbundWater, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/PU02


[]{#pxsd}

###  Phosphorus concentrations in sediment
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`sedimentchemistry`](#sedimentchemistry)
- Concentrations of total, organic and inorganic phosphorus per unit
weight of sediment.  Sediment is understood to be the solid phase of
the bed, including the recently settled material sometimes known as
fluff collected from the bed surface.
- **Alternate labels:**
Sed_Phosphorus, 
Sed_Phosphorus, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/PXSD


[]{#pxsp}

###  Phosphorus concentrations in suspended particulate material
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C005`](#C005)
 [`G015`](#G015)
- Concentrations of total, organic and inorganic phosphorus per unit
weight of suspended particulate material collected by water column
filtration, centrifugation or sediment trapping.
- **Alternate labels:**
SPM_Phosphorus, 
SPM_Phosphorus, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/PXSP


[]{#pytt}

###  Plankton abundance per unit volume of the water column
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Used for plankton abundance parameters where no differentiation
between phytoplankton, microzooplankton or zooplankton is possible
- **Alternate labels:**
WC_PlanktonAbund, 
WC_PlanktonAbund, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/PYTT


[]{#qdmd}

###  Quantity of material dumped
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`H001`](#H001)
- Parameters quantifying the amount of liquids (e.g. ship's ballast)
or solids (e.g. dredge spoil) deposited into the water column as a
result of man's activities
- **Alternate labels:**
Amount_dumped, 
Amount_dumped, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/QDMD


[]{#r410}

###  Ocean colour and earth-leaving visible waveband spectral radiation
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`D015`](#D015)
- Parameters associated with the measurement of ocean colour,
including visible waveband satellite spectral radiometer measurements,
their calibration measurements (spectral water-leaving radiance and
reflectance) and chart colour estimates.
- **Alternate labels:**
Ocean_clr, 
Ocean_clr, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/R410


[]{#rage}

###  Rock age
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`G030`](#G030)
- Measured or stratigraphically estimated ages of lithified sediments,
igneous rock or metamorphic rock.
- **Alternate labels:**
RockAge, 
RockAge, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/RAGE


[]{#ralt}

###  Rock alteration
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`G060`](#G060)
- Parameters describing aspects of a geologic unit that are the result
of bulk chemical, mineralogical or physical changes related to change
in the physical or chemical environment.  Includes weathering,
supergene alteration, hydrothermal alteration and metasomatic effects
not considered metamorphic.
- **Alternate labels:**
RockAlt, 
RockAlt, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/RALT


[]{#rbhy}

###  Molecular biology parameters
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B027`](#B027)
- Any parameters relating to molecular biology or genetics
- **Alternate labels:**
MolecularBiol, 
MolecularBiol, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/RBHY


[]{#rbsc}

###  Radar backscatter
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`D034`](#D034)
- Includes all parameters covering the strength of emitted microwave
radiation return, including absolute measurements of returning signal
strength as well as parameters expressed as backscatter (the
proportion of transmitted signal returned)
- **Alternate labels:**
RadarBScatter, 
RadarBScatter, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/RBSC


[]{#rfvl}

###  Horizontal velocity of the water column (currents)
- Child of:
 [`D0100001`](#D0100001)
- Parameters expressing the velocity (including scalar speeds and
directions) of water column horizontal movement, commonly termed
Eulerian currents
- **Alternate labels:**
Horiz_Currents_WC, 
Horiz_Currents_WC, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/RFVL


[]{#rmin}

###  Inorganic chemical composition of sediment or rocks
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C045`](#C045)
 [`G035`](#G035)
- Parameters specifying the proportions of inorganic components
(major/minor/trace elements, trace metals etc.) in sediment or rock
samples.  Major elements includes the H2O+ and H2O- parameters
reported by convention in oxide weight per cent geochemical major
element analyses.
- **Alternate labels:**
InorgChemRockSed, 
InorgChemRockSed, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/RMIN


[]{#rpot}

###  Redox potential in sediment
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C045`](#C045)
 [`sedimentchemistry`](#sedimentchemistry)
-
- **Alternate labels:**
Sed_RedoxPot, 
Sed_RedoxPot, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/RPOT


[]{#rvds}

###  River flow and discharge
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`H001`](#H001)
 [`O005`](#O005)
- Parameters related to the volume of water passing through a point in
a river system per unit time, including the rates of freshwater,
dissolved material and particulate load discharge from a river into
the sea.
- **Alternate labels:**
Riv_flow_discharge, 
Riv_flow_discharge, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/RVDS


[]{#sabb}

###  Shellfish abundance and biomass in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`H004`](#H004)
- Parameters that quantify the numbers or amount of living material of
shellfish (molluscs - including cephalopods - and crustaceans of
interest to fisheries research and commercial fisheries) in any body
of fresh or salt water.
- **Alternate labels:**
Sfish_AbundBiom, 
Sfish_AbundBiom, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SABB


[]{#salk}

###  Concentration of aliphatic hydrocarbons in sediment samples
- Child of:
 [`D0100001`](#D0100001)
 [`C025`](#C025)
 [`sedimentorganicchemistry`](#sedimentorganicchemistry)
- Aliphatic hydrocarbon (alkane, alkene, alkyne, polycyclic aliphatics
like hopane, terpenes etc.)  concentrations in sediment, which is
considered to be anything from the bed sampled by a grab or corer,
including 'fluff'
- **Alternate labels:**
Sed_AliphaticHC, 
Sed_AliphaticHC, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SALK


[]{#samo}

###  Nutrient fluxes between the bed and the water column
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C040`](#C040)
 [`O005`](#O005)
- Parameters quantifying the exchange of nutrients between the bed (ie
the sediment) and the water column sometimes termed benthic fluxes
- **Alternate labels:**
WCBed_NutFlux, 
WCBed_NutFlux, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SAMO


[]{#satm}

###  Shellfish morphology, age and physiology
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B027`](#B027)
 [`H004`](#H004)
- Parameters that quantify the size, shape, age and life processes
(including mortality) of shellfish (molluscs - including cephalopods -
and crustaceans of interest to fisheries research and commercial
fisheries).
- **Alternate labels:**
Sfish_MorphAgePhys, 
Sfish_MorphAgePhys, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SATM


[]{#scah}

###  Concentration of polycyclic aromatic hydrocarbons (PAHs) in sediment samples
- Child of:
 [`D0100001`](#D0100001)
 [`C025`](#C025)
 [`C055`](#C055)
 [`H001`](#H001)
 [`sedimentorganicchemistry`](#sedimentorganicchemistry)
- PAH concentrations in sediment, which is considered to be anything
from the bed sampled by a grab or corer, including 'fluff'
- **Alternate labels:**
Sed_PAH, 
Sed_PAH, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SCAH


[]{#scdo}

###  Metal fluxes between the bed and the water column
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`O005`](#O005)
- Parameters quantifying the exchange of metalsbetween the bed (ie the
sediment) and the water column sometimes termed benthic fluxes
- **Alternate labels:**
WCBed_MetalFlux, 
WCBed_MetalFlux, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SCDO


[]{#scoc}

###  Concentration of other organic contaminants in sediment samples
- Child of:
 [`D0100001`](#D0100001)
 [`C055`](#C055)
 [`H001`](#H001)
 [`sedimentorganicchemistry`](#sedimentorganicchemistry)
- Concentration parameters for carbon compounds regarded as
environmentally harmful in sediment, which is considered to be
anything from the bed sampled by a grab or corer, including 'fluff'
that are not included in other specific categories
- **Alternate labels:**
Sed_Orgcontam, 
Sed_Orgcontam, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SCOC


[]{#scox}

###  Dissolved concentration parameters for other gases in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`C015`](#C015)
- All concentration parameters for inorganic dissolved gases other
than oxygen and the noble gases in the water column
- **Alternate labels:**
OthGas_WC, 
OthGas_WC, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SCOX


[]{#sdna}

###  Concentrations of biopolymers in sediment
- Child of:
 [`D0100001`](#D0100001)
 [`C050`](#C050)
 [`sedimentorganicchemistry`](#sedimentorganicchemistry)
- Parameters quantifying the amount of naturally-produced organic
(molecules containing carbon) compounds that are built from multiple
instances of structural units (monomers) that are covalently-bonded to
produce larger structures in any sediment (material collected by a
corer including fluff). Includes polynucleotides (RNA and DNA),
polypeptides and polysaccharides (e.g. cellulose).
- **Alternate labels:**
Biolpoly_sed, 
Biolpoly_sed, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SDNA


[]{#sebh}

###  Seal behaviour
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B015`](#B015)
- Parameters describing the actions or reactions, usually in response
to the environment, of true seals (Phocidae), eared seals (Otariidae)
and walruses (Odobenidae).
- **Alternate labels:**
Seal_Behav, 
Seal_Behav, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SEBH


[]{#secc}

###  Secchi disk depth
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`D015`](#D015)
- Measurements of optical visibility in the water column
- **Alternate labels:**
Secchi, 
Secchi, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SECC


[]{#semo}

###  Seal mortality
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B015`](#B015)
- Parameters describing the causes and rate of mortality of true seals
(Phocidae), eared seals (Otariidae) and walruses (Odobenidae).
- **Alternate labels:**
Seal_Mort, 
Seal_Mort, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SEMO


[]{#semp}

###  Seal morphology and physiology
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B015`](#B015)
- Parameters describing the size, shape or physiological activity
including disease and parasite infection status of true seals
(Phocidae), eared seals (Otariidae) and walruses (Odobenidae).
- **Alternate labels:**
Seal_Morph_Phys, 
Seal_Morph_Phys, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SEMP


[]{#shta}

###  Hydrolytic activity in sediment
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`O010`](#O010)
 [`sedimentchemistry`](#sedimentchemistry)
-
- **Alternate labels:**
Sed_HydrolAct, 
Sed_HydrolAct, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SHTA


[]{#sigt}

###  Density of the water column
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`D020`](#D020)
- Absolute determinations of water column density plus parameters
(generally expressed as density anomaly) derived from temperature and
salinity
- **Alternate labels:**
WC_Dens, 
WC_Dens, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SIGT


[]{#sipw}

###  Stable isotopes in sediment pore waters
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C030`](#C030)
 [`G050`](#G050)
- Stable isotope parameters (concentrations, ratios and enrichments)
in either the solute or solvent phase of sediment pore waters.
- **Alternate labels:**
Iso_SedPoreWater, 
Iso_SedPoreWater, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SIPW


[]{#sixx}

###  Concentration of silicon species in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`C045`](#C045)
- Concentration parameters for silicon species (including opal) in all
phases of the water column
- **Alternate labels:**
WC_SiSpecies, 
WC_SiSpecies, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SIXX


[]{#spag}

###  Speleothem age
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`G030`](#G030)
- Measured or stratigraphically estimated ages of secondary mineral
deposits in caves. This includes stalactites, stalagmites, flowstone,
and crystal growths.
- **Alternate labels:**
Speleo_Age, 
Speleo_Age, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SPAG


[]{#spcb}

###  Concentration of polychlorobiphenyls (PCBs) in sediment samples
- Child of:
 [`D0100001`](#D0100001)
 [`C055`](#C055)
 [`H001`](#H001)
 [`sedimentorganicchemistry`](#sedimentorganicchemistry)
- PCB concentrations in sediment, which is considered to be anything
from the bed sampled by a grab or corer, including 'fluff'
- **Alternate labels:**
Sed_PCB, 
Sed_PCB, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SPCB


[]{#spgs}

###  Suspended particulate material grain size parameters
- Child of:
 [`D0100001`](#D0100001)
 [`G015`](#G015)
- Includes all SPM grain size measurements and derived statistics
- **Alternate labels:**
SPM_GrSize, 
SPM_GrSize, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SPGS


[]{#spht}

###  Concentration of inorganic sulphur species in sediment pore water
- Child of:
 [`D0100001`](#D0100001)
 [`C045`](#C045)
- Concentration parameters (including saturation if gaseous) for
inorganic sulphur species in all phases of sediment pore waters
- **Alternate labels:**
PoreWat_S, 
PoreWat_S, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SPHT


[]{#spro}

###  Concentration of proteins in sediment
- Child of:
 [`D0100001`](#D0100001)
 [`C050`](#C050)
 [`sedimentorganicchemistry`](#sedimentorganicchemistry)
- Concentrations of proteins per unit mass or unit volume of sediment
(material collected by a corer including fluff)
- **Alternate labels:**
Sed_Protein, 
Sed_Protein, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SPRO


[]{#spwc}

###  Concentration of inorganic sulphur species in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`C045`](#C045)
- Concentration parameters (including saturation if gaseous) for
inorganic sulphur species in all phases of the water column
- **Alternate labels:**
WC_SulphSpecies, 
WC_SulphSpecies, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SPWC


[]{#sr2d}

###  Two-dimensional seismic reflection
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`SRFL`](#SRFL)
 [`G012`](#G012)
 [`GPYS`](#GPYS)
- Parameters relating to structure beneath sea-bed determined by the
reflection of seismic energy along a single track.
- **Alternate labels:**
2DSeisReflec, 
2DSeisReflec, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SR2D


[]{#sr3d}

###  Three-dimensional seismic reflection
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`SRFL`](#SRFL)
 [`G012`](#G012)
 [`GPYS`](#GPYS)
- Parameters relating to structure beneath sea-bed determined by the
reflection of seismic energy along multiple parallel tracks.
- **Alternate labels:**
3DSeisReflec, 
3DSeisReflec, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SR3D


[]{#srad}

###  Geological sample radioactivity
- Child of:
 [`D0100001`](#D0100001)
 [`C030`](#C030)
 [`G035`](#G035)
- Any parameters quantifying ionising radiation emitted by cores or
samples comprising rock, sediment (including surface sediment such as
fluff)
- **Alternate labels:**
GeoRad, 
GeoRad, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SRAD


[]{#srep}

###  Shellfish reproduction
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B027`](#B027)
 [`H004`](#H004)
- Parameters that quantify the fecundity, reproductive rates or nature
of reproduction in shellfish (molluscs - including cephalopods - and
crustaceans of interest to fisheries research and commercial
fisheries).
- **Alternate labels:**
Sfish_Rep, 
Sfish_Rep, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SREP


[]{#srfl}

###  Seismic reflection
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`G012`](#G012)
 [`GPYS`](#GPYS)
- Parameters relating to the elucidation of geological structure by
quantifying the proportion of waves from a high energy source
reflected by sub-surface layers.
- **Alternate labels:**
Reflection, 
Reflection, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SRFL


[]{#sr2d}

####  Two-dimensional seismic reflection
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`SRFL`](#SRFL)
 [`G012`](#G012)
 [`GPYS`](#GPYS)
- Parameters relating to structure beneath sea-bed determined by the
reflection of seismic energy along a single track.
- **Alternate labels:**
2DSeisReflec, 
2DSeisReflec, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SR2D


[]{#sr3d}

####  Three-dimensional seismic reflection
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`SRFL`](#SRFL)
 [`G012`](#G012)
 [`GPYS`](#GPYS)
- Parameters relating to structure beneath sea-bed determined by the
reflection of seismic energy along multiple parallel tracks.
- **Alternate labels:**
3DSeisReflec, 
3DSeisReflec, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SR3D


[]{#srfr}

###  Seismic refraction
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`G012`](#G012)
- Parameters relating to the elucidation of geological structure by
quantifying the refration of waves from a high energy source by sub-
surface layers.
- **Alternate labels:**
Refraction, 
Refraction, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SRFR


[]{#sscn}

###  Side-scan sonar
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`G012`](#G012)
- A technique for mapping the morphology of the seafloor using a sonar
swath projected sideways from a towed underwater vehicle.
- **Alternate labels:**
Side_Scan, 
Side_Scan, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/SSCN


[]{#g24}

####  Long/short range side scan sonar
- Child of:
 [`SSCN`](#SSCN)
-
- Concept URI: http://vocab.nerc.ac.uk/collection/C77/current/G24


[]{#stmp}

###  Temperature of geological units
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`GPYS`](#GPYS)
 [`GTHM`](#GTHM)
- Parameters that describe the distribution of the degree of hotness
within a body of rock or unlithified sediment.
- **Alternate labels:**
GeolTemp, 
GeolTemp, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/STMP


[]{#rtmp}

####  Rock temperature
- Child of:
 [`005`](#005)
 [`STMP`](#STMP)
- Parameters that describe the distribution of the degree of hotness
within geologic units of lithified sedimentary, igneous of metamorphic
rock.
- **Alternate labels:**
RockTemp
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/RTMP


[]{#stom}

###  Concentration of organic matter in sediments
- Child of:
 [`D0100001`](#D0100001)
 [`sedimentorganicchemistry`](#sedimentorganicchemistry)
- Parameters quantifying the proportion of organic material in a soil
or sediment sample
- **Alternate labels:**
Sed_OrgMatter, 
Sed_OrgMatter, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/STOM


[]{#tadn}

###  Concentration of adenylates in sediment
- Child of:
 [`D0100001`](#D0100001)
 [`C050`](#C050)
 [`sedimentorganicchemistry`](#sedimentorganicchemistry)
- Concentrations of adenylates (ADP, ATP etc) per unit mass or unit
volume of sediment (material collected by a corer including fluff)
- **Alternate labels:**
Sed_Adenylates, 
Sed_Adenylates, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/TADN


[]{#tcnt}

###  Raw temperature and/or salinity instrument output
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`D025`](#D025)
- Direct output parameters from TS instruments such as
thermosalinograph or CTD
- **Alternate labels:**
Raw_TS, 
Raw_TS, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/TCNT


[]{#tdin}

###  Dissolved inorganic nitrogen concentration in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`C005`](#C005)
 [`C040`](#C040)
- Total concentration of all dissolved inorganic nitrogen species in
the water column, usually derived by summation of individual nutrient
concentrations (NO3+NO2+NH4). Some workers may also include urea.
- **Alternate labels:**
DissInorgN, 
DissInorgN, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/TDIN


[]{#tdnt}

###  Dissolved total and organic nitrogen concentrations in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`C005`](#C005)
- Concentration of total (organic plus inorganic) or organic dissolved
nitrogen per unit volume of the water column.  Grouped together as
organic nitrogen frequently determined as total nitrogen.
- **Alternate labels:**
WC_DissNitrogen, 
WC_DissNitrogen, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/TDNT


[]{#tdpx}

###  Dissolved total or organic phosphorus concentration in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`C005`](#C005)
- Concentration of total (organic plus inorganic) or organic dissolved
phosphorus per unit volume of the water column. Grouped together as
organic phosphorus frequently determined as total phosphorus.
- **Alternate labels:**
WC_DissPhosphorus, 
WC_DissPhosphorus, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/TDPX


[]{#tfaa}

###  Dissolved amino acid concentrations in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`C003`](#C003)
- Parameters quantifying the amount of organic compounds containing
both a carboxyl group and an amino group dissolved in a body of water.
- **Alternate labels:**
WC_AminoAcid, 
WC_AminoAcid, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/TFAA


[]{#tmes}

###  Metadata parameters
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`Z005`](#Z005)
- Data parameters that carry information relating to a measured
parameter such as measurement temperatures, integration depths,
quantities sampled and incubation durations
- **Alternate labels:**
Metadata_param, 
Metadata_param, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/TMES


[]{#tnrp}

###  Dissolved inorganic carbon production and respiration in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`O010`](#O010)
- Parameters related to the rates of TCO2 production and consumption
based on light/dark bottle incubations
- **Alternate labels:**
TCO2_Prod, 
TCO2_Prod, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/TNRP


[]{#toch}

###  Concentration of carbohydrates, phenols, alkanols (alcohols), aldehydes and ketones in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`C050`](#C050)
- Concentrations of carbohydrates, phenols, alkanols (alcohols),
aldehydes and simple (non-alkenone) ketones in all phases of any body
of fresh or salt water
- **Alternate labels:**
CarbPhenolAlkanolAldKetWater, 
CarbPhenolAlkanolAldKetWater, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/TOCH


[]{#tran}

###  Transport activity
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`H016`](#H016)
 [`DS12`](#DS12)
- Parameters quantifying the level of activity moving people or cargo
from one place to another.
- **Alternate labels:**
TransAct, 
TransAct, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/TRAN


[]{#tris}

###  Concentration of inorganic sulphur species in sediment
- Child of:
 [`D0100001`](#D0100001)
 [`C045`](#C045)
 [`sedimentinorganicchemistry`](#sedimentinorganicchemistry)
- Concentration parameters for inorganic sulphur species in sediment
(anything collected by a corer including fluff)
- **Alternate labels:**
Sed_SulphSpecies, 
Sed_SulphSpecies, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/TRIS


[]{#tsed}

###  Concentration of suspended particulate material in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`G015`](#G015)
- Parameters quantifying SPM concentration in the water column by
weight, by volume or in terms of turbidity
- **Alternate labels:**
WC_SPM, 
WC_SPM, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/TSED


[]{#tvlt}

###  Raw suspended particulate material concentration sensor output
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`D015`](#D015)
 [`G015`](#G015)
- Raw parameters (voltages and counts) from in-situ suspended
particulate material sensors including transmissometers,
nephelometers,in-situ particle sizers and ABS (including ADCP echo
intensity).
- **Alternate labels:**
Raw_SPM_optics, 
Raw_SPM_optics, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/TVLT


[]{#upth}

###  Bacterial production in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`B005`](#B005)
 [`O010`](#O010)
- Parameters related to bacterial production determination by
measurement of dissolved organic molecule (e.g. leucine, thymidine)
uptake rates
- **Alternate labels:**
WC_BactProd, 
WC_BactProd, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/UPTH


[]{#uvrd}

###  Ultra-violet (UV) radiation
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Parameters relating to the intensity of ultra-violet radiation in
either the atmosphere or the water column
- **Alternate labels:**
UVRad, 
UVRad, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/UVRD


[]{#v999}

###  Microzooplankton taxonomy-related biovolume per unit volume of the water column
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Microzooplankton biovolume parameters presented at the level of taxa
that may be mapped to entities in a standard taxonomy registry such as
WoRMS or ITIS. These may be at any taxonomic level from sub-species
upwards.
- **Alternate labels:**
WC_TaxMicrozooBiovol, 
WC_TaxMicrozooBiovol, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/V999


[]{#vatx}

###  Phytoplankton taxonomic volume in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Any parameterisation of cell volume of free-floating autotrophic
biological entities designated by taxonomic names (e.g. species,
genus, family) in any body of fresh or salt water.
- **Alternate labels:**
PhytoTaxaVolWater, 
PhytoTaxaVolWater, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/VATX


[]{#viru}

###  Virus abundance in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B005`](#B005)
- Any enumeration (e.g. count, number per square metre) of viruses in
any body of fresh or salt water.
- **Alternate labels:**
VirAbundWater, 
VirAbundWater, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/VIRU


[]{#vsra}

###  Visible waveband radiance and irradiance measurements in the atmosphere
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`D015`](#D015)
- Includes visible waveband measurements at discrete wavelengths and
PAR integrated values as photon and energy fluxes. Does not include
satellite radiometer and associated calibration parameters (e.g.
water-leaving radiance and reflectance)
- **Alternate labels:**
Atm_VisRad, 
Atm_VisRad, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/VSRA


[]{#wbrx}

###  Water body redox potential
- Child of:
 [`D0100001`](#D0100001)
 [`C045`](#C045)
- A measure of the tendency of any body of fresh or salt water to
either gain or lose electrons when it is subject to change by
introduction of a new species.
- **Alternate labels:**
RC_redox, 
RC_redox, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/WBRX


[]{#wcoc}

###  Concentration of other organic contaminants in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`C055`](#C055)
 [`H001`](#H001)
- Concentration parameters for carbon compounds regarded as
environmentally harmful in solution or suspension (i.e.includes
measurements in both the dissolved and particulate phases) in any body
of salt or fresh water that are not included in other specific
categories
- **Alternate labels:**
WC_Orgcontam, 
WC_Orgcontam, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/WCOC


[]{#wpro}

###  Concentration of proteins in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`C050`](#C050)
- Concentrations of proteins in all phases of the water column
- **Alternate labels:**
Prot_WX, 
Prot_WX, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/WPRO


[]{#wqbi}

###  Water quality bioindicators
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Parameters quantifying fauna and flora that indicate physical or
chemical conditions in the water column such as colonisation depths
and abundance of indicator species.
- **Alternate labels:**
WaterQualBioind, 
WaterQualBioind, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/WQBI


[]{#wrad}

###  Radioactivity in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C030`](#C030)
- All parameters associated with radioactivity in any body of fresh or
salt water, including radiation counts, isotope activities and
activity ratios. Activities per unit mass of SPM are included.
- **Alternate labels:**
WC_RadAct, 
WC_RadAct, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/WRAD


[]{#wstb}

###  Stable isotopes in water bodies
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C030`](#C030)
- Stable isotope parameters (concentrations, ratios and enrichments)
in both the dissolved and particulate phases of any body of fresh or
salt water.
- **Alternate labels:**
Iso_WC, 
Iso_WC, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/WSTB


[]{#wstr}

###  Wind stress and shear
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Parameters related to forces due to interactions between atmosphere
and the surface of the earth or between atmospheric air masses
- **Alternate labels:**
WindForces, 
WindForces, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/WSTR


[]{#wvsp}

###  Spectral wave data parameters
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`D034`](#D034)
- Parameters for directional and non-directional spectral wave data,
excluding wave directions derived from spectral data.
- **Alternate labels:**
SpectWaveParm, 
SpectWaveParm, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/WVSP


[]{#wvst}

###  Wave height and period statistics
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`D034`](#D034)
- Statistical parameters derived from wave records to express wave
height and period.
- **Alternate labels:**
WaveStats, 
WaveStats, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/WVST


[]{#xmgs}

###  Geological sample magnetic, electrical and acoustic properties
- Child of:
 [`D0100001`](#D0100001)
 [`G012`](#G012)
 [`G040`](#G040)
- Any parameters quantifying the magnetic (e.g. magnetic
susceptibility), electrical (e.g. resistivity) or acoustic (e.g.
P-wave propogation speed) of sediment or rock cores and samples
- **Alternate labels:**
GeoMagElecAcc, 
GeoMagElecAcc, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/XMGS


[]{#xrfc}

###  Raw X-Ray fluorometer (XRF) output from sediment samples
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`sedimentchemistry`](#sedimentchemistry)
-
- **Alternate labels:**
XRFCnt, 
XRFCnt, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/XRFC


[]{#zadx}

###  Zoobenthos dry weight biomass
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Any quantification of the dry mass of zoobenthos (animals living on,
in or near the bed of any water body). Includes animals normally
considered planktonic if collected in sediment and data expressed ash-
free and in terms of carbon, nitrogen etc..
- **Alternate labels:**
ZoobenthDryBiomass, 
ZoobenthDryBiomass, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/ZADX


[]{#zatp}

###  Zooplankton taxonomy-related biomass expressed as protein per unit volume of the water column
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B045`](#B045)
- Zooplankton (mesozooplankton plus larger pelagic animals excluding
fish, reptiles and mammals) protein biomass per unit volume for
entities that have been identified by taxonomic name
- **Alternate labels:**
Zoo_taxa_prot_biom, 
Zoo_taxa_prot_biom, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/ZATP


[]{#zatx}

###  Zooplankton taxonomy-related abundance per unit volume of the water column
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B045`](#B045)
- Zooplankton (mesozooplankton plus larger pelagic animals excluding
fish, reptiles and mammals) abundance parameters presented at the
level of taxa that may be mapped to entities in a standard taxonomy
registry such as WoRMS or ITIS.  These may be at any taxonomic level
from sub-species upwards.
- **Alternate labels:**
Zoo_taxa_abund, 
Zoo_taxa_abund, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/ZATX


[]{#zbtx}

###  Zoobenthos taxonomic abundance
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Any enumeration (e.g. count, number per square metre) of animals
living on or near the seabed designated by taxonomic names (e.g.
species, genus).
- **Alternate labels:**
ZoobenthTaxAbund, 
ZoobenthTaxAbund, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/ZBTX


[]{#zcmp}

###  Zooplankton chemical composition
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B045`](#B045)
- Chemical composition of zooplankton expressed in terms of mass (or
molar quantity) per specimen or per unit tissue mass
- **Alternate labels:**
ZooplChemComp, 
ZooplChemComp, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/ZCMP


[]{#zctc}

###  Zooplankton taxonomy-related biomass expressed as carbon per unit volume of the water column
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B045`](#B045)
- Zooplankton (mesozooplankton plus larger pelagic animals excluding
fish, reptiles and mammals) carbon biomass parameters presented at the
level of taxa that may be mapped to entities in a standard taxonomy
registry such as WoRMS or ITIS.  These may be at any taxonomic level
from sub-species upwards.
- **Alternate labels:**
Zoo_taxa_C_biomass, 
Zoo_taxa_C_biomass, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/ZCTC


[]{#zctn}

###  Zooplankton taxonomy-related biomass expressed as nitrogen per unit volume of the water column
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B045`](#B045)
- Zooplankton (mesozooplankton plus larger pelagic animals excluding
fish, reptiles and mammals) nitrogen biomass parameters presented at
the level of taxa that may be mapped to entities in a standard
taxonomy registry such as WoRMS or ITIS.  These may be at any
taxonomic level from sub-species upwards.
- **Alternate labels:**
Zoo_taxa_N_biomass, 
Zoo_taxa_N_biomass, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/ZCTN


[]{#zfit}

###  Zooplankton and zoobenthos physiological condition parameters
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Parameters indicating the health of zooplankton and zoobenthos taxa,
such as fecundity, egg condition, presence of parasites/diseases etc.
- **Alternate labels:**
ZooPhysioCondition, 
ZooPhysioCondition, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/ZFIT


[]{#znlg}

###  Metal ligand parameters in the water column
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`C035`](#C035)
 [`C045`](#C045)
 [`C050`](#C050)
- Parameters concerned with the complexation of metals as ligands in
the water column
- **Alternate labels:**
WC_MetalLigand, 
WC_MetalLigand, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/ZNLG


[]{#zoob}

###  Zoobenthos taxonomy-related counts
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Zoobenthos count parameters presented at the level of taxa that may
be mapped to entities in a standard taxonomy registry such as WoRMS or
ITIS.  These may be at any taxonomic level from sub-species upwards.
Count includes presence/absence indicators.
- **Alternate labels:**
Zoobenth_taxa_count, 
Zoobenth_taxa_count, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/ZOOB


[]{#zv00}

###  Zooplankton biovolume
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`B045`](#B045)
-
- **Alternate labels:**
ZooBiovol, 
ZooBiovol, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/ZV00


[]{#zwtx}

###  Zoobenthos taxonomy-related wet weight biomass per unit area of the bed
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
- Zoobenthos wet weight biomass per unit area parameters presented at
the level of taxa that may be mapped to entities in a standard
taxonomy registry such as WoRMS or ITIS.  Includes animals considered
as planktonic if they have been returned from sediment samples.
- **Alternate labels:**
Zoobenth_tax_ww_biomass, 
Zoobenth_tax_ww_biomass, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/ZWTX


[]{#zzzz}

###  Unspecified
- Child of:
 [`D0100001`](#D0100001)
 [`005`](#005)
 [`Z005`](#Z005)
- The identity of the parameter is not declared.  Covers cases such as
internal working parameters and dummy channels.
- **Alternate labels:**
Unspec, 
Unspec, 
- Concept URI: http://vocab.nerc.ac.uk/collection/P02/current/ZZZZ



[]{#d0100002}

##  `http://vocab.nerc.ac.uk/collection/D01/current/D0100002`
- Concept URI: http://vocab.nerc.ac.uk/collection/D01/current/D0100002



[]{#d0100003}

##  `http://vocab.nerc.ac.uk/collection/D01/current/D0100003`
- Concept URI: http://vocab.nerc.ac.uk/collection/D01/current/D0100003



[]{#d0100004}

##  `http://vocab.nerc.ac.uk/collection/D01/current/D0100004`
- Concept URI: http://vocab.nerc.ac.uk/collection/D01/current/D0100004



[]{#d0100005}

##  `http://vocab.nerc.ac.uk/collection/D01/current/D0100005`
- Concept URI: http://vocab.nerc.ac.uk/collection/D01/current/D0100005



