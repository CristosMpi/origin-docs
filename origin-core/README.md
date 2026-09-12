# ORIGIN Core

ORIGIN Core is the primary field unit of Project ORIGIN. It brings together sensing, local processing, power management, communications, mechanical protection, and the interfaces required to connect ORIGIN's wider modular ecosystem.

The Core is designed around one central idea: a monitoring device for cultural-heritage environments should not behave like a collection of unrelated sensors. It should operate as a coordinated system that can observe its surroundings, interpret what it measures, communicate useful information, report its own condition, and remain maintainable over repeated deployments.

## Role inside Project ORIGIN

At system level, ORIGIN Core sits between the physical environment and the higher-level software and decision layers.

```text
Heritage environment
        ↓
Sensors and local inputs
        ↓
ORIGIN Core
        ↓
Rosetta electronics + firmware
        ↓
Data processing / communications
        ↓
Centaurus AI and operator-facing systems
```

The Core therefore has several responsibilities at the same time: collect data from connected sensors; detect events relevant to site monitoring; provide local processing and device control; manage power and energy availability; communicate status and observations; support modular attachments and future expansion; protect the electronics in a field-ready enclosure; and expose enough diagnostic information for maintenance and testing.

The design intentionally separates these responsibilities into subsystems so that one part of ORIGIN can evolve without forcing a complete redesign of every other part.

## Main subsystems

### Rosetta electronics

[Rosetta](../rosetta/README.md) is the custom electronics platform at the center of ORIGIN Core. It provides the embedded control, power-management functions, sensor interfaces, storage and connectivity-related interfaces used by the unit.

The ORIGIN Core chapter describes what the complete field unit needs from Rosetta. The Rosetta chapter documents the board itself in greater electrical and manufacturing detail.

### Sensor system

ORIGIN Core supports a collection of sensors rather than relying on a single sensing method. Each sensor contributes a different type of evidence about the state of the site.

The current mechanical design includes three long-range C4001 24 GHz mmWave presence sensors positioned to provide coverage in multiple directions. Additional environmental and system-health inputs can be connected according to the deployment configuration.

See [Sensor System](sensor-system.md) and [Presence Detection](presence-detection.md).

### Power system

The Core is intended to operate as a self-contained field device. Its power architecture combines energy input, battery management, regulated power delivery, monitoring, and software-level power awareness.

Solar integration is part of the mechanical and electrical design direction, while Rosetta contains the electronics responsible for battery charging and regulated supply generation.

See [Power System](power-system.md).

### Connectivity

A monitoring system is only useful if observations can reach the people or software responsible for acting on them. ORIGIN therefore treats communications as a subsystem rather than an afterthought.

The connectivity layer is responsible for moving measurements, events, diagnostics and configuration information between the field unit and the rest of the ORIGIN platform. The exact transports available depend on the hardware revision and deployment configuration.

See [Connectivity](connectivity.md).

### Mechanical enclosure

The enclosure is part of the Core architecture, not just packaging. It determines sensor visibility, cable routing, antenna placement, thermal behavior, maintenance access, water resistance, mounting options, solar-panel support and the physical accessibility of expansion interfaces.

The final enclosure generation is being developed around a more vertical, distinctive architectural form rather than a conventional electronics box. Mechanical details are documented under [Mechanical Design](../mechanical-design/README.md).

## Operational model

A simplified ORIGIN Core operating cycle is:

1. **Power and initialize** — Rosetta starts, validates essential hardware and initializes attached devices.
2. **Acquire** — connected sensors produce measurements or event information.
3. **Validate** — firmware checks whether readings are usable and identifies obvious sensor or communication faults.
4. **Interpret** — relevant measurements are converted into higher-level observations or events.
5. **Store and communicate** — information can be retained locally and/or transmitted according to system configuration.
6. **Diagnose** — the unit records its own operational condition so failures can be distinguished from genuine site events.
7. **Repeat** — monitoring continues according to the configured sampling and event logic.

This cycle is deliberately broader than "read a sensor and send a value." Reliable field monitoring requires the system to understand whether the sensor, power source and communications path are themselves operating correctly.

## Designed for modularity

ORIGIN Core is the base of a larger ecosystem. The project includes modular extensions such as **BITs**, for expandable functionality and local attachments, **Aqua Base**, for deployment scenarios involving water-related monitoring or operation, and **Drone Mount**, for aerial or mobile use cases where compatible sensing needs to be carried by a drone platform.

These modules are documented separately in [Modules](../modules/README.md). The Core architecture is designed so that extensions connect through defined mechanical, electrical and software boundaries instead of becoming permanent one-off modifications.

## Field-oriented design principles

ORIGIN Core is developed around several engineering principles.

### Local capability matters

A field unit should not become useless because a network connection is temporarily unavailable. Local sensing, processing, storage and diagnostics therefore remain important even when remote communication is part of the deployment.

### Sensors must be treated as imperfect

A sensor reading is not automatically a fact. Range, mounting, environmental conditions, blind zones, interference and communication faults can all affect measurements. ORIGIN's documentation and testing therefore distinguish between sensor output and validated system behavior.

### Power is part of reliability

Battery state, charging conditions and supply stability directly affect whether monitoring can continue. Power information is therefore treated as operational telemetry rather than hidden electrical detail.

### Maintenance must be possible

The system is designed to be opened, inspected, diagnosed and updated. Connectors, mounting, cable paths and service access are considered during enclosure development so that a deployed unit does not become disposable when one component needs attention.

### The architecture must survive revisions

Project ORIGIN is still evolving. Hardware revisions, sensor choices and enclosure generations will change. The Core is therefore documented by subsystem and interface so that the overall architecture remains understandable across versions.

## Current development status

ORIGIN Core is an actively developed system. Some architectural decisions are stable while exact component choices, mechanical dimensions and deployment-specific sensor configurations continue to evolve.

Throughout ORIGIN Docs confirmed hardware is described as the current design, planned capabilities are identified as planned or under development, exact electrical specifications are kept in the Rosetta chapter, and deployment-specific assumptions are kept out of general architecture pages unless they are universally applicable.

This prevents early prototypes from being presented as final specifications.

## Chapter map

Continue through the Core documentation in this order [Hardware Architecture](hardware-architecture.md) — physical and electronic subsystem boundaries; [Sensor System](sensor-system.md) — how sensing devices are organized and validated; [Power System](power-system.md) — energy input, battery management and regulated power; [Connectivity](connectivity.md) — data movement, offline behavior and communications responsibilities; [Environmental Monitoring](environmental-monitoring.md) — environmental observations and deployment-specific sensing; and [Presence Detection](presence-detection.md) — the mmWave-based human-presence subsystem.

For board-level details, continue to [Rosetta](../rosetta/README.md).
