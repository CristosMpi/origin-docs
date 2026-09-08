# Hardware Architecture

ORIGIN Core is organized as a set of cooperating hardware subsystems rather than a single monolithic assembly. This makes the system easier to develop, test, repair and upgrade as Project ORIGIN evolves.

## Architectural layers

At a high level, the physical architecture can be represented as:

```text
External environment
      ↓
Sensor layer
      ↓
Rosetta electronics
      ↓
Local power + storage + communications
      ↓
Mechanical enclosure and expansion interfaces
```

Each layer has a different responsibility. The sensor layer interacts with the environment, Rosetta coordinates the electronics, the power subsystem keeps the unit operational, communications move information beyond the device, and the enclosure protects and positions the complete assembly.

## Central electronics platform

The custom Rosetta PCB is the electronic center of ORIGIN Core. Its role is to reduce the number of disconnected modules and improvised wiring paths that would otherwise be required in a field prototype.

Rosetta provides the platform for:

- embedded processing;
- sensor interfaces;
- power management;
- battery connection and charging;
- regulated supply generation;
- local storage-related interfaces;
- connectivity-related interfaces;
- expansion headers and peripheral connections;
- system status and control signals.

The current Rosetta v2 design is approximately 105 × 100 mm. Exact board-level architecture, component selection, schematics, PCB layout and manufacturing information are documented in the [Rosetta](../rosetta/README.md) chapter.

## Sensor integration

Sensors are connected to the Core through defined electrical and mechanical interfaces. This matters because sensing performance depends on much more than whether a module is electrically connected.

A complete sensor integration has to consider:

- supply voltage and current requirements;
- communication interface;
- connector choice;
- cable length and routing;
- physical orientation;
- mounting stiffness;
- field of view;
- exposure to the environment;
- calibration requirements;
- failure detection;
- replacement and servicing.

The current enclosure concept includes three C4001 long-range mmWave presence sensors. Their placement is a mechanical-architecture decision because the enclosure must provide appropriate openings and orientation while also protecting the rest of the electronics.

## Processing architecture

The embedded processor is responsible for coordinating the Core's hardware rather than performing every system function by itself.

Its responsibilities include:

- initializing peripherals;
- polling or receiving sensor data;
- applying device-level validation;
- managing local state;
- controlling communications;
- recording diagnostic information;
- managing power-aware behavior;
- exposing information to higher-level software.

Higher-level reasoning belongs in the software and Centaurus layers. This separation keeps low-level hardware control deterministic and easier to test.

## Power architecture

The hardware is designed around rechargeable battery operation with managed charging and regulated power delivery. In Rosetta v2, the power design includes a BQ24074-family charging stage and a TPS63031-based buck-boost conversion stage.

The exact electrical implementation is documented under [Rosetta → Power Management](../rosetta/power-management.md). At Core level, the important architectural requirements are:

- accept an external energy source;
- charge the battery safely;
- maintain a usable regulated supply across battery conditions;
- expose power state to firmware where possible;
- prevent peripheral power demands from destabilizing the system;
- support deployment-oriented energy planning.

Solar input is part of the intended field architecture, which is why solar-panel mounting and cable routing are also treated as mechanical design requirements.

## Local storage

Field devices need a strategy for data that cannot immediately be transmitted.

The Core architecture therefore includes local-storage capability so information can be buffered, logged or retained for later retrieval. Rosetta v2 includes an SD-card-related interface in its current design direction.

Local storage can be used for:

- diagnostic logs;
- event records;
- temporary telemetry buffering;
- configuration backups;
- test datasets;
- field-validation results.

Storage policy belongs to the [Software](../software/README.md) chapter, while the physical interface belongs to Rosetta.

## Communications interfaces

ORIGIN is designed so communications are not hard-coded to a single deployment assumption. The embedded platform can support local wireless communication and the hardware architecture is being developed with additional connectivity options in mind.

Rosetta v2 includes SIM-related design work, but cellular capability should only be considered an active feature when the full modem, antenna, firmware and network path for a specific revision have been validated.

This documentation therefore distinguishes between:

- interfaces physically present on the board;
- capabilities supported by firmware;
- capabilities validated in a deployed system.

See [Connectivity](connectivity.md) for the Core-level communication model.

## Expansion architecture

ORIGIN is intended to support additional modules without redesigning the entire Core.

Expansion is handled through a combination of:

- electrical headers and interfaces;
- mechanically accessible mounting points;
- cable-routing paths;
- software abstraction;
- module-specific drivers and configuration.

The physical placement of expansion access is particularly important. Interfaces that must be reached after installation cannot be positioned where soil, a wall, mounting hardware or another module would block them.

This requirement has directly influenced the enclosure development, including the placement of BITs-related interfaces away from inaccessible lower surfaces.

## Mechanical-electrical co-design

In ORIGIN, PCB layout and enclosure design are tightly linked.

The enclosure must account for:

- Rosetta board dimensions and mounting holes;
- sensor screw holes;
- sensor field of view;
- cable bend radius;
- battery placement;
- solar cable routing;
- connector access;
- structural supports;
- maintenance access;
- ingress paths;
- thermal behavior.

Likewise, the electronics must account for physical realities such as connector direction, screw access and cable exit points.

This is why the final product cannot be designed effectively by completing the PCB first and treating the enclosure as a box added later.

## Serviceability

A field unit should be repairable at subsystem level.

The hardware architecture therefore favors:

- removable fasteners where appropriate;
- identifiable connectors;
- replaceable sensor modules;
- accessible electronics;
- clear cable routing;
- documented assembly order;
- separation between structural and electrical functions.

The goal is to make diagnosis possible without destroying the enclosure or replacing the entire device.

## Revision control

Hardware architecture evolves through revisions. A change to one part of ORIGIN may require updates in several places:

| Change | Possible impact |
| --- | --- |
| Sensor replacement | Power, firmware, mounting, field of view |
| PCB revision | Mounting holes, connectors, enclosure geometry |
| Battery change | Volume, mass distribution, charging assumptions |
| Solar change | Support geometry, cable route, power budget |
| New module | Electrical interface, software driver, user access |
| New radio | Antenna placement, enclosure material, firmware |

For this reason, hardware revisions should always be documented with both electrical and mechanical consequences.

## What this page does not define

This page defines the Core-level hardware architecture. It does not replace:

- [Rosetta schematics](../rosetta/schematics.md);
- [Rosetta PCB documentation](../rosetta/pcb-design.md);
- [BOM](../rosetta/bom.md);
- [Mechanical Design](../mechanical-design/README.md);
- [Assembly procedures](../rosetta/assembly-and-bring-up.md).

Those pages contain the implementation detail required to reproduce, manufacture and service specific revisions.