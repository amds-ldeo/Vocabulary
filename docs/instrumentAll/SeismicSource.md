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


- [Seismic source instrument](#icat07)
    - [Pinger sub-bottom profilers](#394)
    - [parametric sub-bottom profilers](#396)
    - [Aquapulse](#aqpl)
    - [airgun array](#arag)
    - [Boomer](#bomr)
    - [Chirp](#chrp)
    - [earthquake](#ertq)
    - [high resolution low penetration explosives](#exhl)
    - [high penetration low resolution explosives](#exlh)
    - [Flexichoc](#flxs)
    - [Flexotir](#flxt)
    - [GI-gun](#giag)
    - [marine vibroseis](#mvbr)
    - [natural source](#nats)
        - [earthquake](#ertq)
    - [single-bubble airgun](#sbag)
    - [airgun](#snag)
    - [watergun](#snwg)
    - [Sparker](#sprk)
    - [Vaporchoc](#vshc)

**Concepts**

[]{#icat07}

##  Seismic source instrument
- Categories used in the SeaDataNet project to classify energy sources
used in seismic surveys.
- **Alternate labels:**
SeaDataNet seismic source types, 
seismic sources, 
- Concept URI: http://vocab.nerc.ac.uk/collection/L21/current/ICAT07


[]{#394}

###  Pinger sub-bottom profilers
- Child of:
 [`ICAT07`](#ICAT07)
- Marine seismic sources that send sound pulses into the sub-sea floor
sediments. The sound pulses bounce off the sea floor and subsequent
buried sediment layers according to differences in their acoustic
impedance (hardness) and in turn, their density. Pingers are linear,
single channel, high frequency systems that typically operate at
frequencies greater than 2 kHz and penetrate to several tens of
metres.
- Concept URI: http://vocab.nerc.ac.uk/collection/L05/current/394


[]{#396}

###  parametric sub-bottom profilers
- Child of:
 [`ICAT07`](#ICAT07)
- Marine seismic sources that send sound pulses into the sub-sea floor
sediments. The sound pulses bounce off the sea floor and subsequent
buried sediment layers according to differences in their acoustic
impedance (hardness) and in turn, their density. Parametric sub-bottom
profilers are non-linear systems that transmit two different higher
frequencies that interact during sound propagation to generate a
resultant lower operating frequency with narrow bandwidth. They
typically operate at frequencies greater than 2 kHz and penerate to
several hundreds of metres.
- Concept URI: http://vocab.nerc.ac.uk/collection/L05/current/396


[]{#aqpl}

###  Aquapulse
- Child of:
 [`ICAT07`](#ICAT07)
- A marine seismic source where a propane-oxygen mixture is exploded
inside a steel cylinder.
- Concept URI: http://vocab.nerc.ac.uk/collection/L05/current/AQPL


[]{#arag}

###  airgun array
- Child of:
 [`ICAT07`](#ICAT07)
- A marine seismic source where multiple airguns of different sizes
are tuned so that  a broader frequency spectrum will be generated.
- Concept URI: http://vocab.nerc.ac.uk/collection/L05/current/ARAG


[]{#bomr}

###  Boomer
- Child of:
 [`ICAT07`](#ICAT07)
- A marine seismic energy source in which capacitors are charged to
high voltage and then discharged through a transducer in the water.
The transducer consists of a flat coil with a spring-loaded aluminium
plate. Eddy currents force the plates to separate sharply, producing a
low pressure region between the plates into which the water rushes
generating a pressure wave by implosion.
- Concept URI: http://vocab.nerc.ac.uk/collection/L05/current/BOMR


[]{#chrp}

###  Chirp
- Child of:
 [`ICAT07`](#ICAT07)
- Chirp systems emit a 'swept-frequency signal', meaning that the
transmitted signal is emitted over a period of time and over a set
range of frequencies. This repeatable (transmitted) waveform can be
varied in terms of pulse length, frequency bandwidth, and
phase/amplitude. A matched filter, or correlation process, collapses
the swept frequency modulated (FM) received signal into a pulse of
short duration, maximizing the signal-to-noise-ratio. The reflected
signal is received by a tuned transducer array that generates the
outgoing acoustic energy. Chirps operate within a range of 400Hz - 24
kHz and are used for the first 20-30 metres of unconsolidated
sediments.
- Concept URI: http://vocab.nerc.ac.uk/collection/L05/current/CHRP


[]{#ertq}

###  earthquake
- Child of:
 [`NATS`](#NATS)
 [`ICAT07`](#ICAT07)
- A sudden release of stress in the Earth's crust that creates energy
in the form of seimic waves.
- Concept URI: http://vocab.nerc.ac.uk/collection/L05/current/ERTQ


[]{#exhl}

###  high resolution low penetration explosives
- Child of:
 [`ICAT07`](#ICAT07)
- Groups all explosives that allows high resolution but low
penetration surveys.
- Concept URI: http://vocab.nerc.ac.uk/collection/L05/current/EXHL


[]{#exlh}

###  high penetration low resolution explosives
- Child of:
 [`ICAT07`](#ICAT07)
- Groups all explosives that allows high penetration but low
resolution surveys.
- Concept URI: http://vocab.nerc.ac.uk/collection/L05/current/EXLH


[]{#flxs}

###  Flexichoc
- Child of:
 [`ICAT07`](#ICAT07)
- An implosive energy source for marine shooting. Two plates are
separated by compressed air until they lock into position. The air
between them is then pumped out creating a vacuum. On the signal the
plates are unlocked and the water pressure forces them together
creating a shock wave in the water.
- Concept URI: http://vocab.nerc.ac.uk/collection/L05/current/FLXS


[]{#flxt}

###  Flexotir
- Child of:
 [`ICAT07`](#ICAT07)
- A seismic method for marine shooting whereby small charges are
propelled through a rubber hose by water under pressure into a steel
cage where they are detonated. Holes in the cage allow the water
repelled by the explosion to flow out and in thus dissipating some of
the energy in the bubble effect.
- Concept URI: http://vocab.nerc.ac.uk/collection/L05/current/FLXT


[]{#giag}

###  GI-gun
- Child of:
 [`ICAT07`](#ICAT07)
- A marine seismic source where a pair of conventional airguns (one,
the generator, fires in the conventional manner; the second, known as
the injector) fires some milliseconds later to prevent bubble from
collapsing. Could be used in true GI mode (volume of injector twice of
volume of generator), harmonic mode (same volume of generator and
injector) or true airgun (no delay between generator and injector).
- Concept URI: http://vocab.nerc.ac.uk/collection/L05/current/GIAG


[]{#mvbr}

###  marine vibroseis
- Child of:
 [`ICAT07`](#ICAT07)
- A marine seismic source generating sweeps of controlled varying
frequency (from a few Hz to hundreds of Hz) and duration.
- Concept URI: http://vocab.nerc.ac.uk/collection/L05/current/MVBR


[]{#nats}

###  natural source
- Child of:
 [`ICAT07`](#ICAT07)
- Any kind of natural source of acoustic waves, that can be used in
passive seismics.
- Concept URI: http://vocab.nerc.ac.uk/collection/L05/current/NATS


[]{#ertq}

####  earthquake
- Child of:
 [`NATS`](#NATS)
 [`ICAT07`](#ICAT07)
- A sudden release of stress in the Earth's crust that creates energy
in the form of seimic waves.
- Concept URI: http://vocab.nerc.ac.uk/collection/L05/current/ERTQ


[]{#sbag}

###  single-bubble airgun
- Child of:
 [`ICAT07`](#ICAT07)
- Array of air gun tuned in order to obtain the necessary energy wile
reducing the size of the air guns.
- Concept URI: http://vocab.nerc.ac.uk/collection/L05/current/SBAG


[]{#snag}

###  airgun
- Child of:
 [`ICAT07`](#ICAT07)
- A marine seismic source which injects a bubble of highly compressed
air into the water. Oscillations of the bubble as it alternatively
expands and contracts generate a sonic wave whose frequency depends on
the amount of air in the bubble, its pressure, and the water depth.
- Concept URI: http://vocab.nerc.ac.uk/collection/L05/current/SNAG


[]{#snwg}

###  watergun
- Child of:
 [`ICAT07`](#ICAT07)
- A marine seismic energy source divided into two chambers, the firing
chamber, which contains compressed air, and the other chamber, which
is filled with water. When the gun is fired, the compressed air forces
the shuttle downward and this expels the water from the lower chamber.
The shot of water leaving the gun creates a void behind it and the
collapse of water into this void creates an acoustic wave.
- Concept URI: http://vocab.nerc.ac.uk/collection/L05/current/SNWG


[]{#sprk}

###  Sparker
- Child of:
 [`ICAT07`](#ICAT07)
- A seismic source in which an electrical discharge in water is the
energy source.
- Concept URI: http://vocab.nerc.ac.uk/collection/L05/current/SPRK


[]{#vshc}

###  Vaporchoc
- Child of:
 [`ICAT07`](#ICAT07)
- A marine seismic energy source in which a quantity of superheated
steam under high pressure is iniected into water. Subsequent
condensation of the steam attenuates bubble oscillation.
- Concept URI: http://vocab.nerc.ac.uk/collection/L05/current/VSHC



