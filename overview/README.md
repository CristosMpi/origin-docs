# Overview

Project ORIGIN is Team Galene's modular technology platform for the protection, monitoring, and long-term preservation of cultural heritage sites.

Cultural heritage is exposed to a combination of environmental stress, human activity, difficult site conditions, limited infrastructure, and delayed detection of problems. ORIGIN is being developed around a simple idea: **heritage protection should be continuous, adaptable, and practical to deploy in the real world.**

Rather than treating monitoring as a single sensor or a single device, ORIGIN combines custom electronics, sensing, software, artificial intelligence, modular attachments, and deployment-oriented mechanical design into one expandable system.

## What ORIGIN is

ORIGIN is designed as an ecosystem rather than a fixed product. Its core platform can collect information from its surroundings, process and communicate that information, and work with specialized modules depending on the needs of a site.

The project currently includes several major technology areas:

| Area | Role in ORIGIN |
| --- | --- |
| **ORIGIN Core** | The main field platform that integrates sensing, power, communications, and the physical enclosure. |
| **Rosetta** | Team Galene's custom electronics platform, developed to provide the electrical foundation for ORIGIN. |
| **Software** | Firmware, communications, configuration, data handling, and the software services that connect the system. |
| **Centaurus AI** | The intelligent analysis and cybersecurity layer developed around ORIGIN's data and operation. |
| **BITs** | Modular extensions intended to expand the capabilities of an installation without redesigning the full system. |
| **Aqua Base** | A specialized ORIGIN module for deployments where water-related operation or monitoring is required. |
| **Drone Mount** | A deployment module intended to extend ORIGIN concepts to aerial or hard-to-reach inspection scenarios. |

These parts are developed as a connected system, but they are documented separately so that each subsystem can evolve without making the rest of the documentation difficult to follow.

## Design principles

ORIGIN is guided by several principles that affect both the engineering and the way the project is documented.

### Modular by design

Different heritage sites have different risks. A system suitable for an archaeological site may not need the same sensors or mounting method as one used around a museum, monument, storage area, or remote structure. ORIGIN therefore aims to support modular sensing and deployment instead of relying on one permanently fixed configuration.

### Built for real environments

The project is not intended to exist only as a laboratory prototype. Mechanical protection, power availability, sensor placement, maintenance, communications, installation constraints, and field serviceability are treated as part of the engineering problem.

### Hardware and software developed together

ORIGIN's physical design, Rosetta electronics, firmware, data flow, and intelligent processing are closely connected. Decisions in one part of the system are evaluated in relation to the others rather than as isolated components.

### Expandable rather than disposable

The system is designed around upgradeable modules and evolving electronics. New sensors, revised Rosetta boards, software updates, and specialized modules can be introduced as the project develops.

### Documentation as part of the project

This documentation is intended to become the technical source of truth for ORIGIN. They cover not only what the system is, but how it is designed, tested, deployed, maintained, and improved.

## From prototype to deployment

ORIGIN has been developed through Team Galene's robotics and engineering work, with the project progressing from concept development into custom electronics, mechanical design, software, testing, and field-oriented deployment planning.

A major part of this approach is validating the project outside a competition environment. ORIGIN's deployment work includes a pilot connected with the **Archaeological Museum of Durrës in Albania**, which is documented separately in the [Deployments](../deployments/README.md) section.

## How to read these docs

If you are new to ORIGIN, continue through this Overview section in order:

1. [Introduction](introduction.md) — the project's purpose and scope.
2. [The Problem](the-problem.md) — the challenges ORIGIN is designed to address.
3. [Our Solution](our-solution.md) — the engineering approach behind the project.
4. [How ORIGIN Works](how-origin-works.md) — the system-level operating concept.
5. [System Architecture](system-architecture.md) — how the major subsystems fit together.
6. [Team Galene](team-galene.md) — the student team developing ORIGIN.

For implementation details, continue to [ORIGIN Core](../origin-core/README.md), [Rosetta](../rosetta/README.md), [Software](../software/README.md), and [Centaurus AI](../centaurus-ai/README.md).

> **Documentation status:** ORIGIN is an actively developed engineering project. Detailed specifications may change between versions. Version-specific pages take precedence over high-level descriptions in this Overview.
