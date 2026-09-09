# X-ray computed tomography instrument

from claude 2026-08-10.  Anthropic. (2026). Claude (Claude Opus 4.6) [Large language model]. Response generated February 13, 2026. https://claude.ai/

The main swappable components in a lab-based micro/nano-CT system:

**X-ray source/tube** — different tubes for different applications. Sealed tubes vs. open (demountable) tubes. Different target materials (tungsten for general use, molybdenum for soft tissue/low-Z contrast, copper, silver, chromium for specific energy ranges). Transmission targets vs. reflection targets — transmission targets give a smaller focal spot (better resolution) but lower power. Some systems have interchangeable target inserts within the same tube housing. The filament is also a consumable within open tubes.

**Filters** — thin metal foils placed in the beam path to harden the spectrum (remove low-energy photons that contribute to beam hardening artifacts but don't penetrate the sample). Common materials include aluminum, copper, tin, brass in various thicknesses. Swapped based on sample composition and desired energy range. Some systems have a motorized filter wheel.

**Collimators/apertures** — define the beam geometry. Different slit widths or pinhole sizes for different resolution/flux tradeoffs.

**Detector** — the most significant interchangeable component in many systems. Flat panel detectors (large field of view, moderate resolution) vs. CCD/CMOS cameras coupled to scintillator screens via fiber optic or lens coupling. Different scintillator materials (CsI, GOS, GGG, LuAG) optimized for different energy ranges and resolution requirements. Some systems allow swapping between a high-resolution detector (small field of view, fine pixel pitch) and a survey detector (large field of view, coarser pixels).

**Scintillator screen** — on lens-coupled detector systems, the scintillator can often be swapped independently. Thicker scintillators give more signal but worse spatial resolution (light spread); thinner ones give better resolution but less efficiency. Different materials for different energy ranges.

**Optical magnification lens** — on lens-coupled systems, different objective lenses provide different magnification/resolution/field-of-view combinations. Essentially the same tradeoff as microscope objectives.

**Sample stage/holder** — different mounting fixtures for different sample types and sizes. Rotation stages with different load capacities. Specialized holders for in-situ experiments (heating stages, compression cells, flow cells, environmental chambers). The stage precision (step size, wobble/runout) directly affects reconstruction quality.

**Sample environment chambers** — for in-situ work: heating stages (up to ~1500°C), cooling stages, mechanical loading frames, fluid flow cells, humidity chambers, gas environment cells. These are accessories that mount around or replace the standard sample stage.

**Gratings/optics** (on synchrotron or advanced lab systems) — zone plates, Kirkpatrick-Baez mirrors, condensers for full-field or scanning configurations. More relevant to synchrotron nano-CT than lab systems.

**For your metadata schema decomposition:**

```
XCT System
├── X-ray Source
│   ├── Target (material, geometry)
│   ├── Filament (type, if open tube)
│   └── Operating parameters (voltage, current, focal spot size)
├── Beam Conditioning
│   ├── Filter (material, thickness)
│   └── Collimator/Aperture (geometry, size)
├── Sample Stage
│   ├── Rotation stage (precision, range)
│   ├── Translation stages (X, Y, Z range and precision)
│   └── Sample environment (if any — heating, loading, etc.)
├── Detector
│   ├── Detector type (flat panel, lens-coupled CCD/CMOS)
│   ├── Scintillator (material, thickness)
│   ├── Optics/lens (magnification, NA — if lens-coupled)
│   └── Pixel count and pitch
└── Reconstruction/Control Software
```

The key parameters that change between scans on the same instrument are source voltage/current, filter selection, detector selection or binning mode, source-to-sample and sample-to-detector distances (which determine geometric magnification), rotation step size, and exposure time per projection. These are all method/acquisition parameters rather than instrument identity properties — analogous to the GC oven program or MS scan range in your py-GC-MS work. The swappable hardware components (target, filter, detector, scintillator) sit in between — they're part of the instrument configuration for a given session but change between sessions.