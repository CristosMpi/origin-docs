# Our Solution

ORIGIN approaches heritage protection as a **system engineering problem**.

Instead of building one fixed monitoring device, Team Galene is developing a modular platform that can combine sensing, custom electronics, software, intelligent analysis, and different physical deployment methods around a common architecture.

The objective is not to replace conservation professionals. ORIGIN is intended to support them by making environmental and site information easier to collect, organize, and interpret between direct inspections.

## A modular monitoring platform

The core idea behind ORIGIN is adaptability.

Different sites may require different sensors, mounting positions, power strategies, or communication methods. ORIGIN therefore separates the platform into subsystems that can evolve independently while still working together.

At a high level, the solution consists of five layers:

1. **Physical deployment** — the enclosure, mounting, protection, and site-specific installation.
2. **Sensing and electronics** — sensors and the Rosetta electronics platform.
3. **Embedded software** — firmware that manages hardware, measurements, communications, and system health.
4. **Data and intelligence** — processing, analysis, event detection, and Centaurus AI.
5. **Extensions** — modules such as BITs, Aqua Base, and Drone Mount that adapt the platform to additional use cases.

This layered architecture makes it possible to improve one part of ORIGIN without redesigning the entire system.

## ORIGIN Core

**ORIGIN Core** is the central field platform.

It brings together the hardware that must operate at or near the monitored location: electronics, sensors, power, communications, and the mechanical structure required to keep those systems usable in the field.

The Core is intended to act as the stable foundation of an installation. Depending on the deployment, different sensors and modules can be added around that foundation.

The detailed design of this subsystem is documented under [ORIGIN Core](../origin-core/README.md).

## Rosetta: custom electronics for ORIGIN

A major part of the project is **Rosetta**, Team Galene's custom electronics platform.

Rather than relying indefinitely on a collection of separate development boards, Rosetta is being developed to integrate the electrical functions needed by ORIGIN into a purpose-built platform.

Its role includes providing a foundation for processing, power management, sensor interfaces, storage, communications, and expansion.

This gives Team Galene greater control over how the system is packaged, powered, connected, and upgraded. It also allows the electronics to be designed together with the enclosure and the deployment requirements.

See [Rosetta](../rosetta/README.md) for version-specific hardware documentation.

## Software as the operating layer

Hardware alone cannot provide continuous monitoring.

ORIGIN's embedded software is responsible for turning physical components into a coordinated system. At the device level, software can manage tasks such as sensor acquisition; timing and measurement cycles; system state; local storage; communications; configuration; diagnostics; and update behavior.

The software architecture is designed to keep the system maintainable as the hardware changes. This is particularly important for a project that evolves through multiple Rosetta revisions and different sensor configurations.

See [Software](../software/README.md) for the implementation-focused documentation.

## Centaurus AI

**Centaurus AI** is the intelligent analysis layer associated with ORIGIN.

Its purpose is to explore how collected data can be interpreted more effectively than through raw measurements alone. Depending on the implementation, intelligent processing can help identify patterns, detect unusual behavior, prioritize events, or support system-level decisions.

Centaurus is also connected to ORIGIN's cybersecurity work. As the platform becomes more capable and connected, intelligent features must be developed alongside safeguards for data integrity, device behavior, access, and communication.

The project deliberately separates intelligent assistance from final human judgment. ORIGIN can help surface information; conservation and operational decisions remain the responsibility of people.

See [Centaurus AI](../centaurus-ai/README.md) for the dedicated architecture and limitations pages.

## Modular extensions

ORIGIN is designed to expand beyond a single field unit.

### BITs

**BITs** are modular extensions intended to add capabilities to the system without rebuilding the complete ORIGIN platform. This modular approach allows the project to explore additional functions while keeping a common underlying architecture.

### Aqua Base

**Aqua Base** extends the project toward water-related deployments and environments where the standard field configuration is not the appropriate physical platform.

### Drone Mount

**Drone Mount** explores how ORIGIN sensing or inspection capabilities can be adapted for aerial operation and locations that are difficult to reach from a fixed ground installation.

These modules are described in more detail under [Modules](../modules/README.md).

## Designed around the full deployment lifecycle

ORIGIN is not considered complete when the electronics power on.

A real monitoring system has a lifecycle:

**site assessment → configuration → installation → calibration → operation → diagnostics → maintenance → upgrade**

The project therefore includes dedicated documentation for installation, testing, validation, maintenance, and deployments.

This matters because many practical failures occur outside the schematic or source code. A sensor can be electrically correct but badly positioned. An enclosure can be strong but difficult to maintain. A power system can work in a laboratory but be unsuitable for an unattended installation.

ORIGIN's solution is to treat those concerns as part of the engineering from the beginning.

## Human-centered monitoring

ORIGIN is designed as a decision-support platform, not an autonomous authority.

The system can collect measurements, detect changes, record events, and assist with interpretation. Its role is to improve awareness and provide technical evidence. It does not replace conservation expertise, site policies, or professional assessment.

This principle influences how alerts, AI, and automation are developed: the goal is to make important information easier to notice and understand while keeping people in control of consequential decisions.

## Why this architecture is useful

The modular architecture gives ORIGIN several advantages as an engineering platform components can be revised independently; the same core ideas can support different deployment scenarios; hardware and software can evolve without discarding the entire system; new modules can be added over time; testing can be performed at subsystem and full-system levels; and documentation can distinguish stable concepts from version-specific implementation details.

The result is a project that can grow from a student engineering prototype toward a more mature, testable, and deployable heritage technology platform.

Continue to [How ORIGIN Works](how-origin-works.md) for a step-by-step view of the system during operation.
