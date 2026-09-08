# System Architecture

ORIGIN is organized as a modular, layered system so that sensing, electronics, software, intelligent analysis, and deployment hardware can evolve without becoming one tightly coupled design.

This page describes the **conceptual architecture** of the project. Exact components, interfaces, pin assignments, protocols, dimensions, and version-specific behavior belong in the corresponding technical sections.

## Architecture at a glance

The ORIGIN ecosystem can be viewed as five interacting layers:

```text
┌─────────────────────────────────────────────┐
│            Human / Site Layer               │
│ Conservation staff • operators • deployment │
└──────────────────────┬──────────────────────┘
                       │
┌──────────────────────▼──────────────────────┐
│        Intelligence & Data Layer            │
│ Centaurus AI • analysis • records • events  │
└──────────────────────┬──────────────────────┘
                       │
┌──────────────────────▼──────────────────────┐
│             Software Layer                  │
│ Firmware • communications • configuration   │
│ diagnostics • storage • device behavior     │
└──────────────────────┬──────────────────────┘
                       │
┌──────────────────────▼──────────────────────┐
│          Electronics & Sensing Layer        │
│ Rosetta • sensors • power • interfaces      │
└──────────────────────┬──────────────────────┘
                       │
┌──────────────────────▼──────────────────────┐
│           Physical Deployment Layer         │
│ Enclosure • mounts • environment • modules  │
└─────────────────────────────────────────────┘
```

The layers are shown vertically for clarity, but the system is not strictly one-way. Diagnostics, configuration, maintenance, and control information can move in both directions.

## Physical deployment layer

The physical layer is where ORIGIN meets the real environment.

It includes the enclosure, sensor openings or protected interfaces, mounting hardware, structural supports, cable routing, weather protection, and any site-specific mechanical elements.

This layer also includes specialized physical platforms such as Aqua Base and Drone Mount when they are used.

Mechanical choices directly affect the quality of the rest of the system. Sensor orientation can affect measurements; enclosure material can affect radio performance; thermal design can affect electronics; and maintenance access can determine whether a deployed system remains practical to operate.

For that reason, mechanical design is part of the architecture rather than packaging added after the electronics are finished.

## Electronics and sensing layer

This layer contains the hardware responsible for interacting with the environment and supporting device operation.

### Sensors

Sensors provide the measurements and events used by ORIGIN. They are selected and positioned according to the deployment objective rather than treated as a permanent universal set.

### Rosetta

Rosetta is the custom electronics platform at the center of ORIGIN's hardware architecture. Its purpose is to provide a common foundation for processing, power management, storage, interfaces, communications, and expansion.

Rosetta also provides an important boundary in the architecture: external sensors and modules can change while the system retains a consistent central electronics platform.

### Power

Power is treated as a system-level subsystem because it affects operating time, communications, processing, sensor behavior, and maintenance.

The detailed implementation depends on the Rosetta revision and deployment configuration and is documented in the [Rosetta](../rosetta/README.md) and [ORIGIN Core](../origin-core/README.md) sections.

## Software layer

The software layer coordinates hardware and turns individual components into a functioning monitoring system.

Its responsibilities include areas such as:

- hardware initialization;
- sensor acquisition;
- timing and scheduling;
- configuration;
- local data handling;
- storage;
- communications;
- diagnostics;
- device state management;
- update mechanisms.

A key architectural principle is separation between low-level device behavior and higher-level analysis. The embedded system should remain understandable and diagnosable even when intelligent processing is unavailable or changed.

This separation also makes testing easier. Sensor interfaces, storage, communications, and diagnostics can be validated independently before the complete data and AI pipeline is involved.

## Intelligence and data layer

The intelligence and data layer turns collected information into a form that can support interpretation.

Centaurus AI belongs to this layer, together with the surrounding data-processing logic.

The architecture distinguishes between **data collection** and **intelligent interpretation**. This is intentional: the system should preserve useful observations even if an AI component is unavailable, revised, or replaced.

Centaurus can build on the information supplied by the rest of the platform, but it should not become a hidden dependency for basic device operation.

This layer also considers cybersecurity and data integrity. A connected monitoring platform must be able to reason not only about what the environment is doing, but also whether its own data and behavior can be trusted.

## Human and site layer

The final layer is the most important one: the people and heritage environment for which the system exists.

ORIGIN is not designed to make conservation decisions independently. The architecture is intended to deliver observations, events, diagnostics, and analysis in a form that can support human assessment.

This keeps a clear distinction between:

- what the system measures;
- what the software detects;
- what the AI suggests;
- what a responsible person decides.

## Extension architecture

ORIGIN's modular design allows additional capabilities to connect to the wider platform.

### BITs

BITs are intended to function as modular capability extensions. Their purpose is to allow new functions to be introduced without changing every part of ORIGIN Core.

### Aqua Base

Aqua Base changes the physical deployment context while remaining part of the same project ecosystem. It demonstrates why the architecture separates sensing and software concepts from one permanent enclosure format.

### Drone Mount

Drone Mount extends ORIGIN toward mobile or aerial inspection. This introduces different constraints around power, weight, orientation, motion, and communication, while still reusing elements of the broader sensing and data architecture.

## Interfaces between subsystems

A modular system only works when interfaces are clearly defined.

ORIGIN therefore treats subsystem boundaries as important design objects. Examples include:

| Boundary | What must be defined |
| --- | --- |
| Sensor ↔ Rosetta | electrical interface, power, signals, data format, physical connection |
| Rosetta ↔ Firmware | hardware resources, drivers, initialization, fault behavior |
| Firmware ↔ Communications | message structure, retry behavior, connection state |
| Device ↔ Data layer | timestamps, identifiers, measurements, events, diagnostics |
| Data layer ↔ Centaurus | validated inputs, context, analysis outputs, confidence/limitations |
| Core ↔ Module | mechanical, electrical, power, communication, and software compatibility |
| ORIGIN ↔ Human | understandable status, alerts, maintenance information, documentation |

The detailed definitions of these interfaces are version-specific and belong in later documentation.

## System states and diagnostics

A field system should not be thought of only as either "working" or "broken."

ORIGIN's architecture supports the idea of observable system states. A unit may be operating normally, temporarily offline, running with a sensor unavailable, experiencing reduced power, or requiring maintenance.

Diagnostics are therefore cross-cutting. They are not confined to one layer:

- electronics can report hardware conditions;
- firmware can report device state;
- communications can report connectivity;
- data services can identify missing or unusual data;
- Centaurus can help interpret patterns;
- maintenance procedures can resolve the underlying issue.

## Versioning

ORIGIN is an active development project, so the architecture is intentionally separated from individual implementations.

For example, **Rosetta v2** is a specific hardware revision. The architectural role of Rosetta can remain stable even when individual components, connectors, or board layouts change in future revisions.

This documentation follows the same principle:

- Overview pages explain stable project concepts.
- Technical pages document the current implementation.
- Version pages preserve important differences between revisions.
- Development pages record future work without presenting it as already implemented.

## Architectural goal

The purpose of this structure is to keep ORIGIN understandable as it grows.

A new sensor should not require a new project. A new enclosure should not require a new data model. A new AI method should not require rewriting the firmware. A new deployment platform should be able to reuse as much of the ecosystem as practical.

That is the core architectural principle behind ORIGIN: **common foundations, replaceable modules, explicit interfaces, and continuous iteration.**

Continue to [Team Galene](team-galene.md) to learn about the team developing the system.
