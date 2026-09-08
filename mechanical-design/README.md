# Mechanical Design

ORIGIN is not only an electronics and software project. Its mechanical system determines whether the sensors can see the intended area, whether the electronics can survive real deployment, whether maintenance is practical, and whether the complete product can be manufactured repeatedly.

The current mechanical design direction is a **tall, vertically oriented enclosure** rather than a low, bulky box. Team Galene is deliberately exploring a more distinctive architectural form, including pyramidal and faceted geometries, so ORIGIN can have a recognisable identity while still behaving like an engineered field device.

This chapter documents the mechanical design principles, current enclosure constraints, sensor mounting, solar support, environmental protection, materials, CAD workflow, and manufacturing strategy.

## Current design basis

The current ORIGIN Core enclosure is being developed around the following confirmed project constraints:

- **Rosetta v2 PCB:** approximately 105 × 100 mm;
- **three DFRobot C4001 24 GHz mmWave sensors** integrated around the enclosure;
- dedicated openings or windows for the mmWave sensors;
- a vertically biased form factor, with height preferred over unnecessary width;
- a modular attachment point for BITs that remains accessible after the device is installed in soil or close to the ground;
- a solar-panel support system with a **third structural support that also provides a protected cable path**;
- no single manufactured object should exceed approximately **250 × 250 × 250 mm**;
- field serviceability must be considered from the beginning rather than added after the enclosure is complete.

These constraints describe the present mechanical direction. Exact production dimensions, tolerances, fasteners, seals, wall thicknesses, and materials are revision-controlled design details and should be published only after the relevant CAD revision is frozen.

## Mechanical architecture

At a high level, ORIGIN's mechanical system can be separated into several functional regions:

```text
Solar / upper structure
        ↓
Sensor-facing upper enclosure
        ↓
Rosetta + internal electronics volume
        ↓
Service / module interface zone
        ↓
Site-specific mounting or base
```

This layered approach helps prevent one requirement from controlling the whole product. For example, sensor geometry can evolve without forcing a complete redesign of the solar support, and a module interface can remain reachable without moving the main electronics.

## Why enclosure geometry matters

For ORIGIN, the outer shell is part of the sensing system.

The enclosure influences:

- radar field of view;
- sensor orientation;
- water ingress paths;
- internal temperature;
- cable bend radius;
- wireless performance;
- service access;
- structural loading;
- mounting stability;
- visual impact at a heritage site.

This means the enclosure cannot be treated as a decorative cover placed around finished electronics. Electronics, sensing, software assumptions, and mechanical geometry must be developed together.

## Design priorities

The current mechanical priorities are:

1. **Protect the electronics** from normal deployment conditions.
2. **Preserve sensor performance** by controlling mounting angle and obstructions.
3. **Keep the product maintainable** so parts can be inspected and replaced.
4. **Avoid unnecessary bulk** while providing enough internal volume for routing and assembly.
5. **Support modularity** without putting important interfaces in inaccessible locations.
6. **Respect manufacturing limits** so the design can be produced with available processes.
7. **Create a distinctive product identity** without allowing appearance to compromise engineering requirements.

## Current enclosure concept

The present direction uses a tall central body with multiple faces or facets rather than a simple rectangular project box.

That architecture is useful because it can provide separate surfaces for:

- the three mmWave sensors;
- logos or identification;
- service interfaces;
- module attachment;
- structural ribs;
- cable paths;
- upper solar supports.

The exact exterior form is still a development variable. A pyramidal or tapered architecture is being considered because it provides a strong visual identity and naturally creates directional sensor faces.

See [Enclosure](enclosure.md).

## Internal packaging

Internal packaging should be designed from a digital assembly rather than by estimating clearances from the outside.

At minimum, CAD should reserve volume for:

- Rosetta v2;
- connectors and cable exits;
- battery or power hardware where applicable;
- three radar boards and their connectors;
- fastener heads and tools;
- service clearances;
- strain relief;
- wiring bends;
- seals and mating surfaces.

A component fitting inside the nominal enclosure volume is not enough. It must also be possible to **install, connect, inspect, and remove** it.

## Sensor integration

The three C4001 sensors include PCB mounting holes and should be located by dedicated mechanical features rather than adhesive-only placement.

The enclosure should therefore provide:

- repeatable mounting points;
- a defined sensing direction;
- controlled stand-off from the external wall/opening;
- connector access;
- protection against rotation;
- clearance from nearby conductive hardware where practical;
- replacement access.

See [Sensor Mounting](sensor-mounting.md).

## Solar integration

The solar assembly should be considered a structural subsystem, not simply a panel glued to the top of the product.

The present concept calls for three supports, with the third support also acting as a protected route for the solar cable into the enclosure. This avoids leaving an exposed cable draped around the outside of the unit.

See [Solar System](solar-system.md).

## Environmental protection

ORIGIN's sensing requirements create an important trade-off: the mmWave sensors may benefit from dedicated openings, but openings reduce the simplicity of the environmental seal.

The design therefore uses a **risk-managed environmental protection strategy** rather than claiming that every version is fully waterproof.

Protection should be assessed around:

- top-facing seams;
- sensor openings;
- cable penetrations;
- fasteners;
- service covers;
- module interfaces;
- drainage and trapped water;
- condensation.

See [Waterproofing](waterproofing.md).

## Manufacturing envelope

For the current project workflow, individual mechanical objects should remain within approximately **250 × 250 × 250 mm**.

This affects how large shells, covers, solar mounts, and bases are divided into parts.

Splitting a design into multiple manufactured parts is acceptable when it improves:

- printer compatibility;
- assembly;
- serviceability;
- replacement cost;
- orientation and surface quality;
- strength in the required directions.

The mechanical design should not force a one-piece enclosure simply for visual simplicity.

## Revision control

Mechanical files should be versioned in the same way as electronics and software.

A useful release should identify:

- assembly revision;
- compatible Rosetta revision;
- compatible sensor revision;
- module-interface revision;
- manufacturing process;
- material;
- required hardware;
- known limitations.

A STEP or STL file without revision context is not sufficient production documentation.

## Validation

Mechanical validation should include more than checking whether the parts fit on screen.

Tests should cover:

- physical assembly;
- connector access;
- screw access;
- cable routing;
- radar field-of-view impact;
- stability;
- repeated opening/closing;
- solar-support stiffness;
- module insertion/removal;
- water-path inspection;
- outdoor exposure where appropriate;
- transportation and handling.

Formal results belong under [Testing & Validation](../testing-validation/README.md).

## Chapter contents

Continue with:

- [Design Philosophy](design-philosophy.md)
- [Enclosure](enclosure.md)
- [Sensor Mounting](sensor-mounting.md)
- [Solar System](solar-system.md)
- [Waterproofing](waterproofing.md)
- [Materials](materials.md)
- [CAD](cad.md)
- [Manufacturing](manufacturing.md)

The objective of this chapter is to make ORIGIN's physical architecture understandable and reproducible while clearly separating current design intent from dimensions or manufacturing details that have not yet been frozen.