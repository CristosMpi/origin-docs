# CAD

ORIGIN's CAD model is the mechanical source of truth for enclosure geometry, component placement, sensor orientation, solar-support interfaces, and assembly relationships.

A useful CAD release must do more than show the outside shape. It should represent the full mechanical assembly closely enough that another team member can manufacture, assemble, inspect, and revise the hardware without relying on undocumented knowledge.

## CAD objectives

The mechanical model should capture:

- overall enclosure geometry;
- Rosetta v2 placement;
- three C4001 sensor positions and angles;
- mounting bosses and fasteners;
- cable channels;
- service covers;
- BIT/module interface location;
- solar-panel supports;
- hollow solar cable route;
- base or field-mount interface;
- gasket/seal geometry where applicable;
- manufacturing splits between parts.

## Master assembly

The preferred workflow is to maintain a **master assembly** containing simplified but dimensionally accurate representations of the major hardware.

The assembly should include at least:

```text
ORIGIN assembly
├── Main enclosure
├── Service cover(s)
├── Rosetta v2 reference model
├── Radar A
├── Radar B
├── Radar C
├── Internal carrier / brackets
├── BIT / expansion interface reference
├── Solar panel
├── Solar support A
├── Solar support B
├── Solar cable support
├── Fastener references
└── Mounting / base reference
```

The exact file hierarchy depends on the CAD platform, but the design intent should remain clear.

## Reference models

Purchased components should be represented using verified dimensions wherever possible.

Examples include:

- Rosetta PCB outline and mounting holes;
- C4001 sensor PCB and mounting holes;
- connectors;
- solar panel;
- inserts;
- standard fasteners;
- glands or grommets.

Reference models should not be casually scaled until they "look right." Critical dimensions should come from drawings, datasheets, measured hardware, or the source design files.

## Rosetta reference

The current Rosetta v2 board is approximately 105 × 100 mm, while the earlier Gerber job metadata indicates an exported overall bounding size around 100.05 × 104.8 mm.

For enclosure release work, the **actual PCB source or verified STEP model** should be used rather than relying only on rounded documentation values.

The enclosure should reserve clearance for:

- PCB edges;
- mounting hardware;
- connectors;
- cable insertion;
- component height;
- service access.

## Sensor references

Each C4001 model should include:

- PCB outline;
- mounting holes;
- connector position;
- sensing face/direction;
- required keep-clear volume.

A visible axis or construction line for each sensor's forward direction is useful for checking coverage geometry.

## Coordinate system

The assembly should use a stable global coordinate system.

A recommended convention is:

- Z: vertical / height;
- X and Y: horizontal enclosure axes;
- origin: central datum near the base or electronics reference.

Sensor orientations, module positions, and drawings should reference the same coordinate logic.

This reduces confusion when mechanical angles are discussed in software or testing documents.

## Parametric design

Where supported by the CAD tool, important dimensions should be parameterised rather than repeated as unrelated fixed numbers.

Useful parameters may include:

- PCB clearance;
- shell thickness;
- sensor stand-off;
- service-gap tolerance;
- insert diameter;
- gasket compression depth;
- support spacing;
- solar angle;
- module-interface height.

Parameterisation makes revision safer because one design change can propagate consistently.

## Manufacturing split

Because individual manufactured objects should remain within approximately **250 × 250 × 250 mm**, CAD should explicitly define part splits.

Splits should be chosen based on engineering considerations such as:

- printer volume;
- print orientation;
- support minimisation;
- structural load direction;
- access to internal hardware;
- replacement strategy;
- appearance.

A split line should not pass through a critical sealing surface or high-load feature without a deliberate joint design.

## Print orientation in CAD

For additively manufactured parts, orientation should be considered during design rather than after export.

CAD geometry can include:

- self-supporting angles;
- flat datum surfaces;
- chamfers instead of unsupported horizontal ceilings;
- sacrificial supports or tabs;
- accessible insert faces;
- layer orientation aligned with structural needs.

The strongest-looking shape is not always strong when printed in the wrong orientation.

## Tolerances

CAD files should distinguish nominal dimensions from required clearances.

Examples:

- a 3 mm screw should not automatically use a 3.00 mm printed clearance hole;
- a PCB should not be trapped between walls at its exact nominal width;
- a service cover needs enough clearance to open after surface variation;
- press fits require process-specific calibration.

Tolerance values should come from manufacturing tests and should be recorded in drawings or design notes.

## Fastener modelling

Critical fasteners should be represented in the assembly so tool and head clearance can be checked.

At minimum, CAD should verify:

- screw length;
- head clearance;
- insert depth;
- nut capture;
- washer space;
- tool access;
- no collision with electronics.

Full-thread geometry is usually unnecessary for performance and can make files heavy; simplified fastener models are acceptable if dimensions are accurate.

## Cable routing

Cable paths should be represented explicitly.

This is particularly important for:

- radar cables;
- solar cable;
- battery/power wiring;
- service connections;
- module interfaces.

CAD should verify:

- minimum bend space;
- strain-relief location;
- cover closure;
- separation from screws;
- no cable crossing through solid parts;
- enough service slack.

The hollow solar support should be checked with the actual cable diameter and required connector/termination method.

## Sealing surfaces

Where a gasket or seal is used, the mating geometry should be modelled intentionally.

CAD should define:

- seal path;
- groove dimensions where applicable;
- compression surfaces;
- fastener spacing;
- corner radii;
- seam overlap.

A gasket should not be added after the shell is complete without checking whether the mating surfaces can compress it evenly.

## Module interface

The BIT/expansion interface should be modelled as a reusable interface rather than a one-off hole.

The CAD should define:

- insertion direction;
- mechanical keying;
- retention method;
- connector clearance;
- external access;
- protective cap/blank geometry if applicable;
- keep-out region around the interface.

The interface should remain accessible after ORIGIN is installed.

## Interference checking

Before export, the assembly should be checked for collisions.

Important checks include:

- Rosetta vs shell;
- sensors vs fasteners;
- cables vs covers;
- solar cable vs support bends;
- screws vs PCB components;
- module insertion path vs base/mount;
- service cover removal path;
- solar support vs sensor field of view.

CAD collision-free status does not replace a physical assembly test, but it catches avoidable errors early.

## Drawing package

For important manufactured parts, a release should include drawings where practical.

Drawings can identify:

- overall dimensions;
- critical hole spacing;
- fastener callouts;
- material;
- revision;
- tolerances;
- surface requirements;
- assembly notes.

This is especially useful for parts that may later be CNC machined, laser cut, or fabricated by a sponsor rather than printed directly from STL.

## File formats

A mechanical release should preserve editable source files and provide neutral/export formats as appropriate.

Recommended outputs may include:

- native CAD source;
- STEP for interoperable solid geometry;
- STL or 3MF for additive manufacturing;
- PDF drawings;
- DXF for suitable 2D profiles.

STL alone should not be treated as the master design because it loses parametric and feature information.

## STEP releases

STEP is particularly useful for ORIGIN because it allows electronics, enclosure, brackets, and partner-fabricated parts to be reviewed across different CAD systems.

A STEP export should be checked after generation for:

- missing bodies;
- incorrect units;
- broken assemblies;
- accidental hidden components;
- coordinate shifts;
- duplicated parts.

## File naming

A consistent naming convention should identify revision and purpose.

For example:

```text
ORIGIN_Core_Enclosure_R03.step
ORIGIN_Radar_Mount_R02.step
ORIGIN_Solar_Cable_Support_R01.step
ORIGIN_Core_Assembly_R03.step
```

The exact convention can evolve, but ambiguous files such as `final2_fixed_new.step` should be avoided.

## Revision history

Each released mechanical revision should record:

- revision identifier;
- date;
- author/editor;
- compatible Rosetta revision;
- major changes;
- manufacturing status;
- validation status;
- known issues.

A revision should move from concept to release only after the relevant prototype has been checked.

## Pre-release checklist

Before publishing a CAD package, verify:

- [ ] all components are the correct revision;
- [ ] overall size fits manufacturing constraints;
- [ ] Rosetta has service clearance;
- [ ] all three radars are correctly oriented;
- [ ] sensor openings are unobstructed;
- [ ] BIT interface is accessible;
- [ ] solar third support contains a usable cable path;
- [ ] fasteners are accessible;
- [ ] cables can be routed;
- [ ] no critical interference remains;
- [ ] sealing surfaces are defined;
- [ ] exported STEP/STL files open correctly;
- [ ] filenames and revision metadata are correct.

## Related documentation

See:

- [Enclosure](enclosure.md)
- [Sensor Mounting](sensor-mounting.md)
- [Solar System](solar-system.md)
- [Materials](materials.md)
- [Manufacturing](manufacturing.md)

The CAD package should make the physical design reproducible. The goal is not only to preserve how ORIGIN looks, but to preserve **why every interface is where it is and how the device is actually assembled**.