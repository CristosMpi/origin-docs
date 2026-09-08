# Enclosure

The ORIGIN enclosure is the central mechanical structure that carries the electronics, sensors, service interfaces, and upper solar assembly.

The current design direction is **tall, faceted, and more architectural than a conventional electronics box**. A pyramid-influenced or tapered form is being explored because it can create dedicated sensor faces, reduce visual bulk, and give ORIGIN a distinctive identity.

The enclosure is still an evolving design. This page documents the current requirements and architecture without presenting unfinished dimensions as production specifications.

## Core requirements

The current enclosure must accommodate:

- Rosetta v2, approximately 105 × 100 mm;
- three DFRobot C4001 24 GHz mmWave sensors;
- sensor mounting hardware;
- internal wiring and connector clearance;
- power-system wiring;
- service access;
- BIT/module access from a reachable side or raised position;
- a solar-panel support structure;
- a protected solar cable path;
- field mounting or base interfaces.

The design should remain compatible with the project manufacturing limit of approximately **250 × 250 × 250 mm per individual object**.

## Form factor

The preferred form factor is vertically oriented.

Compared with a wide rectangular box, a taller structure can provide:

- a smaller ground footprint;
- better separation between lower mounting hardware and upper sensors;
- room for stacked internal assemblies;
- more useful directional faces;
- improved side access for modules;
- a stronger product identity.

The final height-to-width ratio is not yet frozen and should be determined from the complete CAD assembly and stability tests.

## Faceted sensor geometry

The current concept uses multiple exterior faces so the three radar boards can be aimed in different directions.

A simplified conceptual arrangement is:

```text
          radar face A
             /\
            /  \
 radar B   /Core\   radar C
          /______\
```

This diagram is only conceptual. The final angle between sensors must be determined from the real enclosure geometry and validated coverage tests.

The benefit of a faceted enclosure is that each radar can have:

- a known normal direction;
- a dedicated opening or window;
- repeatable mounting geometry;
- a defined software identity;
- a reproducible test orientation.

## Internal zones

The interior should be divided into functional zones rather than treated as one empty cavity.

A useful packaging model is:

### Upper sensing zone

Contains or supports the three radar modules and their local cable routing.

### Central electronics zone

Contains Rosetta v2 and associated electronics.

This zone should provide:

- PCB mounting bosses or a removable tray;
- clearance around connectors;
- controlled cable routing;
- access for inspection;
- enough space to remove the board without damaging surrounding parts.

### Service zone

Provides access to interfaces that may need to be reached without fully disassembling the product.

Examples can include:

- module connection;
- SD/SIM access if required by the hardware revision;
- programming/debug access;
- service disconnects;
- status indicators.

The exact exposed interfaces should be limited to those genuinely needed in the deployed product.

### Lower mounting zone

Connects the main enclosure to the site-specific support, base, stake, bracket, or other mounting system.

The lower mounting geometry should not block BIT or service access.

## Rosetta mounting

Rosetta should be fixed mechanically using repeatable mounting features.

The enclosure should not rely on loose placement, foam packing, or cable tension to hold the board.

A good internal mounting system should:

- constrain translation and rotation;
- avoid bending the PCB;
- allow the board to be installed after the shell is manufactured;
- provide electrical clearance below the PCB;
- keep fasteners away from sensitive components;
- permit removal using normal tools;
- remain compatible with the current PCB revision.

A removable electronics carrier or tray may be preferable to bosses integrated permanently into the outer shell if board revisions are expected.

## Sensor openings

The current design accepts that the radar sensors may require dedicated external openings.

Those openings must be treated as engineered interfaces rather than simple holes.

Each opening should consider:

- width and height relative to the sensor field of view;
- recess depth;
- drip edges;
- protective lip geometry;
- optional radar-transparent cover material;
- fastening method;
- replacement access;
- drainage;
- exposure to direct rain and debris.

The enclosure should not be described as waterproof solely because most surfaces are sealed.

See [Waterproofing](waterproofing.md).

## Service access

The enclosure should include a deliberate opening strategy.

Possible approaches include:

- removable rear panel;
- split shell;
- lower service cover;
- removable internal cartridge;
- hinged or screw-retained panel.

The preferred method should be selected based on:

- seal complexity;
- assembly time;
- tool access;
- cable routing;
- print orientation;
- replacement requirements.

A service panel should not be positioned where installation hardware makes it inaccessible.

## Fastener strategy

Fasteners should be standardised where practical.

Mechanical documentation should define:

- screw size;
- length;
- head type;
- insert or nut type;
- installation torque where relevant;
- required washers;
- whether thread-locking is used;
- which joints are intended for repeated service.

Heat-set inserts may be suitable for repeatedly opened 3D-printed parts, but the exact insert specification should be frozen only after print-material and wall-thickness testing.

## Cable management

Cable routing is part of the enclosure design.

Wires should not be allowed to move freely around the cavity.

The CAD model should include or reserve:

- cable channels;
- tie points;
- strain relief;
- bend clearance;
- separation from screw paths;
- protection from sharp printed edges;
- slack required for service-panel removal.

Cable routes should also avoid obstructing radar boards or antenna regions.

## BIT interface placement

The BIT attachment area must remain accessible after the device is mounted.

This means the main interface should **not be placed on the underside** where soil, a stake, or mounting base could block it.

The current enclosure philosophy therefore favours a side-accessible or raised interface.

The module connection should be mechanically keyed or clearly oriented so users cannot easily install a BIT incorrectly.

## Solar integration

The top of the enclosure must support the solar assembly without transferring excessive bending load into thin shell walls.

Load paths should move through reinforced features or dedicated supports.

The third solar support also needs to contain a protected cable path from the panel into the enclosure.

See [Solar System](solar-system.md).

## Stability

A tall enclosure must be checked for stability under:

- self-weight;
- solar-panel overhang;
- cable forces;
- handling;
- wind exposure;
- uneven mounting surfaces;
- accidental light contact.

The centre of mass should remain as low as practical. Heavy components should not be placed near the top unless required.

For stake or soil installations, the structural relationship between the enclosure and ground interface should be tested rather than assumed.

## Thermal considerations

A sealed or semi-sealed enclosure exposed to sunlight can become significantly warmer than ambient air.

Mechanical design should therefore consider:

- solar loading;
- internal heat generation;
- material temperature limits;
- colour and surface finish;
- ventilation only where compatible with environmental protection;
- thermal spacing around power components.

No thermal-performance claim should be made until the assembled enclosure has been tested under representative conditions.

## Tolerances

The CAD model should not use zero-clearance fits for parts made by additive manufacturing.

Tolerance should be assigned according to the process and function.

Examples include:

- sliding cover clearance;
- PCB edge clearance;
- insert-hole sizing;
- screw clearance holes;
- mating-shell gaps;
- cable-channel width;
- sensor-board stand-off.

Final values should be based on test coupons and the actual manufacturing equipment/material rather than a universal assumed tolerance.

## Assembly sequence

The enclosure should have a documented assembly order.

A representative sequence is:

1. install threaded inserts or captive hardware;
2. install sensor mounts;
3. route sensor cables;
4. install Rosetta carrier;
5. connect internal wiring;
6. install service interfaces;
7. attach the lower mounting interface;
8. install the solar cable and supports;
9. perform electrical checks;
10. close and seal the enclosure;
11. perform final functional testing.

The exact sequence should be updated when the final CAD revision is released.

## Release criteria

An enclosure revision should not be called production-ready until at least the following are confirmed:

- all internal components fit;
- fasteners are accessible;
- sensor orientation is repeatable;
- all required connectors can be reached;
- cable routing is controlled;
- the shell can be opened and reassembled;
- the solar structure is mechanically stable;
- the module interface remains accessible after mounting;
- environmental weak points are documented;
- the complete assembly fits manufacturing limits;
- a physical prototype has been tested.

## Related documentation

See:

- [Sensor Mounting](sensor-mounting.md)
- [Solar System](solar-system.md)
- [Waterproofing](waterproofing.md)
- [CAD](cad.md)
- [Manufacturing](manufacturing.md)
- [Installation & Deployment](../installation-deployment/README.md)

The enclosure is expected to evolve as ORIGIN moves from prototype to field-ready hardware. Every mechanical revision should preserve the underlying goals: compact footprint, strong sensor geometry, maintainability, modularity, and a distinctive but functional architecture.