from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAGES = {
"overview/README.md": r'''# Overview

**Project ORIGIN** is a modular technology platform created by **Team Galene** for the monitoring, protection, and long-term preservation of cultural heritage.

ORIGIN combines sensing, custom electronics, embedded software, intelligent analysis, modular accessories, and field-oriented mechanical design in one coordinated system. The platform is designed for museums, archaeological sites, monuments, temporary excavations, and other environments where continuous technical awareness can support heritage protection.

## What ORIGIN does

ORIGIN Core collects information from presence, environmental, and system-health sensors. Rosetta electronics coordinate power, processing, storage, and interfaces. Embedded software turns raw inputs into structured observations and health states. Centaurus AI can combine context and observations to support higher-level interpretation. Optional modules extend the platform for specialized deployment needs.

## Built for real sites

ORIGIN treats installation, sensor placement, communications, power, maintenance, and service access as part of the product architecture. A heritage site is not simply a place to put a sensor; its geometry, conservation requirements, visitor routes, environmental exposure, and operational workflow shape the configuration.

## Modular by design

The Core platform can be adapted through BITs, Aqua Base, Drone Mount, and other compatible extensions without changing the identity of ORIGIN itself.

## User-centered documentation

This wiki explains the system from the perspective of the people who use, deploy, maintain, evaluate, or study ORIGIN. Internal workshop history and fabrication notes are kept outside the public user documentation.

Continue with [Introduction](introduction.md), [The Problem](the-problem.md), [Our Solution](our-solution.md), [How ORIGIN Works](how-origin-works.md), [System Architecture](system-architecture.md), and [Team Galene](team-galene.md).
''',
"overview/introduction.md": r'''# Introduction

Project ORIGIN brings together electronics, sensing, software, artificial intelligence, mechanics, and deployment methodology to support the protection of cultural heritage.

Cultural heritage environments are technically demanding. A museum may have dense visitor movement and reflective surfaces, while an archaeological site may face weather exposure, limited power, difficult maintenance access, and large monitored zones. ORIGIN is designed as a platform that can be configured around those differences.

## A system, not a single sensor

At a high level, ORIGIN combines environmental and presence sensing, Rosetta custom electronics, embedded software, local data handling, communications, Centaurus AI, a field-ready enclosure, modular extensions, and structured installation and maintenance procedures.

These parts work together. Sensor placement affects data quality. Mechanical design affects field of view and serviceability. Power affects communication and availability. Software gives every observation context and identity. Centaurus adds higher-level interpretation while preserving operator oversight.

## Heritage-aware engineering

ORIGIN is designed to minimize unnecessary intervention in protected environments. Reversible mounting, compact footprint, controlled cable routing, service access, privacy-aware sensing, and clear operator information are all part of the product philosophy.

## ORIGIN 2026

The current documented platform generation is ORIGIN 2026, centered on Rosetta v2 electronics, multi-directional mmWave sensing, modular expansion, and the system architecture described throughout this wiki.
''',
"overview/our-solution.md": r'''# Our Solution

ORIGIN approaches heritage monitoring as a complete systems-engineering challenge.

## Observe

Presence, environmental, and system-health sensors observe conditions around the unit. ORIGIN Core can combine multiple sensing directions and different measurement types so one data source does not define the complete picture.

## Process

Rosetta and the embedded software initialize the connected hardware, collect observations, maintain time and source identity, manage local state, and organize information for storage or communication.

## Interpret

Centaurus AI can combine observations, context, device health, and event history to support higher-level analysis. Its role is to help operators understand what deserves attention rather than to replace human responsibility at a heritage site.

## Communicate

The communication layer transfers observations, events, and health information to higher-level services while keeping transport state distinct from local sensing state.

## Adapt

BITs, Aqua Base, Drone Mount, and the Expansion System allow ORIGIN to support different deployment contexts without redesigning the complete Core.

## Protect and maintain

The enclosure, mounting system, solar support, cable routing, inspection process, and maintenance workflow are treated as product features because field reliability depends on more than electronics alone.

The result is a modular heritage-technology platform with a consistent architecture that can be configured to suit different sites and operational needs.
''',
"overview/team-galene.md": r'''# Team Galene

**Team Galene** is the student robotics and engineering team behind Project ORIGIN, based at the **4th General Lyceum of Ioannina (4ο ΓΕΛ Ιωαννίνων), Greece**.

## ORIGIN project team

The current ORIGIN project team is **Christos Mpirmpos** and **Evelina Tsiagkaveli**, supported by coach **Anastasia Giannakou**.

The team works across electronics, robotics, software, artificial intelligence, mechanical design, testing, documentation, deployment, partnerships, and user experience.

## Engineering approach

Team Galene develops ORIGIN as an integrated system rather than as a collection of competition features. Decisions about electronics, mechanics, sensing, software, deployment, and maintenance are coordinated so the complete platform remains understandable and serviceable.

## International experience

Team Galene has represented Greece in major robotics competitions and has qualified for the **World Robot Olympiad 2026 International Final in San Juan, Puerto Rico**. The team also develops ORIGIN in collaboration with external technical and cultural-heritage partners.

## Documentation philosophy

ORIGIN Docs are written to help users understand the platform, not to expose internal workshop notes. The wiki focuses on how the product works, how it is configured, how it is deployed, and how users can interpret its behavior.
''',
"software/README.md": r'''# Software

ORIGIN software coordinates the physical platform and turns sensor activity into structured, traceable information that users and higher-level services can understand.

## Device software

The embedded software running on Rosetta manages startup, hardware interfaces, sensor discovery, acquisition, timing, local state, storage, communications, configuration, diagnostics, watchdog behavior, and software identity.

## Structured observations

Raw readings are normalized into records with source identity, timestamp, measurement or event type, value, unit where applicable, and health information. This allows the wider ORIGIN system to understand not only what was measured, but where it came from and whether the source was healthy.

## Local resilience

Core monitoring is separated from remote connectivity. If a communications path becomes temporarily unavailable, the device can preserve meaningful local state and use buffering where supported by the installed configuration.

## Configuration-driven behavior

Site identity, enabled sensors, acquisition intervals, module selection, calibration values, event rules, communications behavior, and maintenance modes are controlled through configuration rather than requiring users to alter program code.

## Centaurus integration

Higher-level analysis is handled separately from deterministic device control. Centaurus consumes structured data and context while the embedded software remains responsible for the reliable operation of the physical unit.

Continue with [Architecture](architecture.md), [Firmware](firmware.md), [Installation](installation.md), [Configuration](configuration.md), [Communications](communications.md), [Data Pipeline](data-pipeline.md), and [Updates](updates.md).
''',
"software/architecture.md": r'''# Software Architecture

ORIGIN software uses a layered architecture so hardware access, device logic, communications, data services, intelligent analysis, and operator-facing functions remain clearly separated.

## Hardware abstraction

The lowest software layer translates Rosetta interfaces and connected sensors into consistent software operations. Each device retains a stable logical identity even if the physical connection changes between hardware revisions.

## Device services

Device services schedule acquisition, validate observations, associate time and source identity, maintain subsystem health, create events, manage local records, and expose the active configuration.

## Communications

The communications layer handles the selected transport, delivery state, retries, buffering behavior, and connection health. A transport condition is kept separate from sensor state.

## Data services

Remote services receive structured ORIGIN records, preserve provenance, support storage and visualization, and provide data to Centaurus and operator-facing applications.

## Centaurus AI

Centaurus performs higher-level analysis such as correlation, anomaly interpretation, contextual reasoning, prioritization, and event explanation. It consumes structured observations rather than directly controlling the hardware.

## Operator layer

The operator layer presents health, events, configuration, deployment identity, and maintenance information in a form that can be understood without board-level knowledge.

## Design goals

The architecture prioritizes modularity, traceability, resilience, configuration-driven behavior, diagnostics, security, and clear separation of responsibility between local device control and higher-level analysis.
''',
"software/firmware.md": r'''# Firmware

ORIGIN firmware is the embedded runtime that turns Rosetta into a coordinated field device.

## Startup

On startup, firmware loads the active configuration, initializes required interfaces, identifies the expected sensors and modules, checks storage where used, establishes time handling, and reports the resulting device state.

## Sensor acquisition

Firmware collects data from the three C4001 radar channels, the LIS3DH, environmental sensors, and supported modules according to the active configuration. Each observation is associated with a stable source identity.

## Health supervision

The runtime maintains health information for important subsystems so an unavailable sensor, storage condition, communications interruption, or power-related state remains distinguishable from normal operation.

## Local records

Firmware can maintain local records for diagnostics and buffering according to the installed storage configuration. This supports continuity when the remote transport is temporarily unavailable.

## Configuration

Deployment-specific behavior is driven by configuration, including sensor enablement, acquisition timing, event thresholds, communication behavior, module selection, and calibration values.

## Recovery

Watchdog and recovery logic return the device to a known state after expected interruptions. Startup always rebuilds the system view from the active hardware and configuration rather than assuming that every previous subsystem state is still valid.

## Software identity

The active firmware version is reported as part of the unit's product information so maintenance and support can match the device with the correct documentation.
''',
"software/installation.md": r'''# Installation

Software installation prepares an ORIGIN Core unit for its assigned deployment and confirms that the device is running the correct software and configuration.

## 1. Identify the unit

Confirm the ORIGIN unit identifier, Rosetta revision, enclosure revision, and intended deployment profile.

## 2. Load the approved software

Install the ORIGIN software package appropriate to the Rosetta revision and deployment. Software identity is checked after startup so the active version can be recorded.

## 3. Apply configuration

Load the site-specific configuration, including unit identity, sensor selection, module configuration, communication settings, acquisition behavior, calibration values, and deployment metadata.

## 4. Verify hardware discovery

Confirm that the expected sensors, local storage, communications hardware, and modules appear with the correct logical identities.

## 5. Verify health

Check that required subsystems initialize normally and that the device reports a clear state for any optional subsystem that is intentionally disabled.

## 6. Test restart behavior

Restart the unit and confirm that configuration, identity, storage, sensor discovery, and communication state are restored consistently.

## 7. Continue to calibration

After software setup is complete, proceed to [Calibration](../installation-deployment/calibration.md) and then [Commissioning](../installation-deployment/commissioning.md).

This workflow keeps software installation focused on the user's unit and deployment rather than on internal programming tools.
''',
"software/communications.md": r'''# Communications

The communications subsystem connects ORIGIN Core with higher-level software while preserving clear separation between local device operation and network state.

## What is transmitted

Communications can carry sensor observations, structured events, device health, configuration information, software identity, timestamps, and maintenance-related state.

## Transport abstraction

ORIGIN software is designed so the data model is not tied to one transport. A deployment can use the communications method appropriate to the site while preserving the same higher-level record structure.

## Offline tolerance

When remote connectivity is interrupted, the device can continue local sensing and maintain local state. Where local storage is enabled, records can be queued according to the installed configuration and synchronized when connectivity returns.

## Message identity

Records include enough identity and timing information to distinguish current data from delayed or repeated delivery and to associate every observation with the correct device and sensor.

## Health reporting

Connectivity is represented as its own system state. Users can therefore distinguish a remote-network condition from a sensor or power condition inside ORIGIN Core.

## Security

Credentials and sensitive connection details are stored separately from the public documentation and from ordinary user-facing configuration. Only the information required for operation is exposed to the relevant subsystem.
''',
"mechanical-design/README.md": r'''# Mechanical Design

ORIGIN's mechanical system protects the electronics, establishes sensor geometry, supports power and modules, and gives the product a distinctive identity suitable for heritage environments.

## Design priorities

The enclosure uses a vertically biased form factor to reduce ground footprint, separate lower mounting functions from upper sensing regions, improve internal packaging, and create useful directional faces for the three C4001 mmWave sensors.

Rosetta v2 occupies roughly **100 × 105 mm** and is integrated with three radar modules, power hardware, wiring, service clearances, and module interfaces inside the Core enclosure.

## Sensor integration

The three mmWave sensors are mechanically fixed so their direction is repeatable and traceable to the software configuration. Openings, recesses, fasteners, and nearby structural features are designed around sensing performance and environmental protection.

## Solar integration

The solar-panel structure uses three supports, including a hollow support that provides a protected cable route into the enclosure.

## Modular access

BITs and other extensions are positioned so they remain accessible after the unit is installed, including configurations close to or partly within soil.

## Manufacturing envelope

No single manufactured part is intended to exceed approximately **250 × 250 × 250 mm**, allowing the design to remain compatible with practical fabrication methods.

Continue with [Design Philosophy](design-philosophy.md), [Enclosure](enclosure.md), [Sensor Mounting](sensor-mounting.md), [Solar System](solar-system.md), [Waterproofing](waterproofing.md), [Materials](materials.md), [CAD](cad.md), and [Manufacturing](manufacturing.md).
''',
"mechanical-design/enclosure.md": r'''# Enclosure

The ORIGIN Core enclosure is a vertically oriented protective structure designed around Rosetta v2, three directional mmWave sensors, the power system, service access, modular attachments, and the solar support.

## Vertical architecture

A taller form factor provides a compact footprint, useful separation between mounting hardware and sensing regions, space for organized internal assemblies, and multiple faces that can be used for directional sensing.

## Internal layout

The enclosure provides dedicated space for Rosetta, sensor boards, wiring, power components, connector access, strain relief, and service clearances. Internal geometry is arranged so one subsystem can be accessed without unnecessarily disturbing another.

## Sensor faces

Each C4001 sensor has a defined mounting position and outward sensing direction. Openings or windows are shaped to preserve field of view while helping control water and debris exposure.

## Service access

Panels and fasteners are arranged so the unit can be opened, inspected, serviced, and closed again using normal tools. Important connectors and module interfaces remain accessible after installation.

## Module interface

BITs attach away from the underside of the unit so the interface remains reachable in soil-adjacent installations. This also keeps expansion functions separate from the primary mounting surface.

## Product identity

The enclosure is intentionally more architectural than a conventional electronics box. Its geometry is designed to communicate that ORIGIN is a purpose-built heritage-technology product while keeping function, serviceability, and sensor performance central.
''',
"mechanical-design/cad.md": r'''# CAD

ORIGIN CAD defines the physical relationship between the enclosure, Rosetta v2, the three C4001 sensors, solar supports, module interfaces, cabling, fasteners, seals, and the site-mounting system.

## Reference geometry

Rosetta v2 occupies approximately **100 × 105 mm**. The mechanical model reserves clearance for the PCB, connectors, cables, fasteners, service tools, and airflow or sealing features where required.

## Sensor geometry

Each radar model includes board position, mounting holes, sensing direction, opening geometry, cable path, and service access. The CAD assembly therefore acts as part of the sensing specification.

## Parametric design

Useful controlled dimensions include PCB clearance, wall thickness, sensor stand-off, service gap, insert diameter, gasket compression, solar support spacing, module interface height, and panel angle.

## Manufacturing output

The mechanical design can be exported in formats appropriate to production and review, including native CAD, STEP, STL or 3MF, drawings, and 2D profiles where required.

## Assembly checks

The complete CAD assembly is used to verify component fit, cable routing, fastener access, sensor clearance, module insertion, service-panel movement, and solar-support interaction before physical production.
''',
"mechanical-design/materials.md": r'''# Materials

Material selection in ORIGIN is based on the role of each part and the environment in which the unit is used.

## Selection criteria

The enclosure and support system consider temperature variation, sunlight and UV exposure, moisture, impact, mechanical load, dimensional stability, manufacturability, radar interaction where material lies in front of a mmWave sensor, compatibility with seals, maintenance needs, and appearance at the heritage site.

## Functional material zones

The main shell prioritizes environmental and dimensional stability. Solar supports prioritize stiffness and long-term mechanical behavior. Sensor bezels prioritize geometry and environmental exposure. Internal trays prioritize accuracy, electrical isolation, and serviceability. Module interfaces prioritize toughness and repeated use.

## Radar-facing materials

Material directly in front of a mmWave sensor is selected and shaped with sensing performance in mind. Thickness, geometry, coatings, and nearby metal features can influence the effective field of view.

## Fasteners and inserts

Metal hardware, threaded inserts, washers, and other joining components are selected to support repeatable service without unnecessarily damaging the surrounding enclosure material.

## Documentation

The material used by a particular manufactured part is associated with its mechanical revision so replacement and service parts can match the installed unit.
''',
"mechanical-design/solar-system.md": r'''# Solar System

The ORIGIN solar structure supports field-oriented energy input while keeping the panel mechanically stable, serviceable, and integrated with the enclosure.

## Three-support architecture

The panel is carried by three structural supports. The third support is hollow and also functions as a protected cable route from the panel toward the enclosure.

## Mechanical goals

The support system provides stable panel positioning, resistance to normal handling and transport loads, controlled cable routing, serviceable attachment, sufficient stiffness, and minimal interference with sensor fields of view and enclosure access.

## Cable path

The hollow support protects the solar cable from exposed routing and helps control bend radius, abrasion, strain, and entry into the enclosure. Cable service remains possible without dismantling unrelated sensor hardware.

## Site orientation

Panel angle and direction are selected during deployment according to available sunlight, shading, installation geometry, and the site's visual and conservation requirements.

## Maintenance

Inspection covers panel condition, contamination, shading changes, support stiffness, fasteners, cable routing, abrasion, and the enclosure entry point.
''',
"modules/README.md": r'''# Modules

ORIGIN modules extend the Core platform for specialized environments and user needs without changing the fundamental architecture of the system.

## BITs

**BITs** are modular attachments that add localized sensing, interaction, or site-specific functionality. They use the Core's expansion architecture while remaining identifiable to the software configuration.

## Aqua Base

**Aqua Base** adapts ORIGIN for water-adjacent or high-moisture deployment contexts by changing the support and environmental interface around the Core.

## Drone Mount

**Drone Mount** provides a mechanical configuration for approved aerial inspection workflows where local rules, aircraft capability, payload limits, and site permissions allow its use.

## Expansion System

The Expansion System defines the common principles for mechanical attachment, electrical connection, identity, configuration, health reporting, and compatibility between ORIGIN Core and optional modules.

## User experience

Modules are treated as configuration-aware parts of the system. The operator can therefore understand which extensions belong to a unit and whether each one is active, disabled, or requires attention.

Continue with [BITs](bits.md), [Aqua Base](aqua-base.md), [Drone Mount](drone-mount.md), and [Expansion System](expansion-system.md).
''',
"modules/bits.md": r'''# BITs

**BITs** are compact modular attachments that extend ORIGIN Core with site-specific sensing, interaction, or auxiliary functions.

## Purpose

A BIT allows one capability to be added or exchanged without redesigning Rosetta or the complete Core enclosure. This keeps the system modular and makes site customization easier to understand and service.

## Mechanical interface

The attachment point provides repeatable positioning, defined orientation, tool access where required, cable clearance, strain relief, and compatibility with the Core enclosure. The interface is positioned away from the bottom of the unit so it remains accessible in soil-adjacent installations.

## Electrical and data interface

Active BITs use the ORIGIN expansion architecture for power and data. The installed module is represented in configuration so software can associate observations and health with the correct attachment.

## Module identity

Each supported BIT type can carry a logical identity and revision. This allows users to distinguish different module functions and ensures the correct configuration is applied.

## Custom BITs

The same interface can support specialized BITs for environmental, proximity, educational, accessibility, or other site-specific purposes, provided the module remains compatible with the Core's mechanical, electrical, and software architecture.

## Maintenance

BITs are designed to be inspected, removed, reconnected, and replaced independently from the main Core where practical.
''',
"modules/expansion-system.md": r'''# Expansion System

The **ORIGIN Expansion System** provides a common architecture for adding optional modules to ORIGIN Core while preserving a consistent user experience.

## Mechanical interface

Modules use defined attachment zones, orientation, retention, cable-routing space, and keep-out regions around sensors and service areas. This prevents an accessory from becoming an unrelated add-on to the enclosure.

## Electrical interface

Supported active modules connect through the Core's expansion power and data architecture. The unit configuration records which module is installed and which behavior is expected.

## Software identity

Modules are identified logically by the software stack. Their observations, events, and health information can therefore be associated with the correct physical extension.

## Compatibility

Compatibility is determined by the ORIGIN generation, Core enclosure, Rosetta revision, software version, and module revision. This information is stored with the configuration rather than left to user guesswork.

## Supported module families

The documented expansion families are **BITs**, **Aqua Base**, and **Drone Mount**. Each serves a different deployment purpose while using the same overall principles of identity, configuration, serviceability, and compatibility.

## Isolation

A module condition is kept separate from the health of unrelated Core functions. This allows the operator to understand whether a service message belongs to an extension or to the main unit.

The Expansion System is what allows ORIGIN to remain one coherent platform across different deployment scenarios.
''',
"partners-sponsors/README.md": r'''# Partners & Sponsors

Project ORIGIN is supported by organizations that contribute technical expertise, manufacturing capability, equipment, materials, field context, and cultural-heritage collaboration.

## Heritage collaboration

The **Archaeological Museum of Durrës, Albania** is associated with ORIGIN's five-unit deployment program and provides an important real-world cultural-heritage context for the platform.

## Technical and manufacturing support

Partners and sponsors contribute across PCB production, electronics design tools, 3D printing materials, laser fabrication, scanning and measurement, mechanical manufacturing, sensors, and other engineering resources.

## Team responsibility

Team Galene remains responsible for ORIGIN's architecture, integration, configuration, testing, deployment guidance, documentation, and public technical claims. Sponsor support strengthens the project but does not replace the team's engineering responsibility.

## Recognition

Current and historical support is documented through [Partners](partners.md), [Sponsors](sponsors.md), and [Acknowledgements](acknowledgements.md).
''',
"partners-sponsors/partners.md": r'''# Partners

ORIGIN partnerships connect the technical platform with the institutions and environments where it can create value.

## Archaeological Museum of Durrës

The principal heritage collaboration documented for ORIGIN 2026 is the five-unit deployment program associated with the **Archaeological Museum of Durrës, Albania**.

The collaboration provides a cultural-heritage context for site assessment, mounting constraints, sensor geometry, operator workflow, maintenance access, environmental exposure, and multi-unit configuration.

## Site role

The responsible institution determines where equipment can be installed, which mounting methods are acceptable, which areas are operationally sensitive, when maintenance can take place, and what information is useful to staff.

## Team Galene role

Team Galene provides the ORIGIN system architecture, configuration guidance, installation documentation, commissioning procedures, maintenance information, and technical support associated with the platform.

## Partnership model

ORIGIN can collaborate with museums, archaeological sites, conservation organizations, universities, research laboratories, municipalities, cultural institutions, educational organizations, and technical partners.

A strong partnership aligns the monitoring objective, site requirements, technical configuration, operator workflow, and long-term service plan.
''',
"partners-sponsors/acknowledgements.md": r'''# Acknowledgements

Project ORIGIN is developed by **Team Galene** at the **4th General Lyceum of Ioannina, Greece**.

The current ORIGIN project team is **Christos Mpirmpos** and **Evelina Tsiagkaveli**, supported by coach **Anastasia Giannakou**.

Team Galene acknowledges the organizations, educators, technical partners, sponsors, and heritage collaborators that contribute equipment, materials, manufacturing capability, expertise, deployment context, and support to ORIGIN.

Special acknowledgement is given to the **Archaeological Museum of Durrës, Albania** for the collaboration associated with the five-unit ORIGIN deployment program.

The team also recognizes the manufacturers, documentation authors, standards bodies, software communities, and research sources whose technical information supports responsible engineering decisions throughout the project.

Third-party names, logos, documentation, software, images, and technical assets remain subject to their respective owners' rights and terms.
''',
"partners-sponsors/sponsors.md": r'''# Sponsors

ORIGIN is supported by sponsors and technical partners that strengthen the project's manufacturing, prototyping, sensing, fabrication, and development capabilities.

## PCB and electronics

PCB-manufacturing and electronics-tool partners support the production and iteration of Rosetta and related electronics. Their contribution helps Team Galene work with professional board-production processes and modern design tools.

## Additive manufacturing and materials

3D-printing partners support the enclosure, sensor mounts, brackets, internal supports, module interfaces, fit-check parts, and field-ready mechanical components used throughout ORIGIN.

## Laser fabrication

Laser-fabrication support is used for suitable flat parts, templates, fixtures, labeling, workshop organization, demonstration components, and other production tasks that benefit from precise 2D processing.

## 3D scanning and measurement

Scanning and measurement equipment can support geometry capture, fit verification, digital reference creation, comparison of manufactured parts, and workflows where ORIGIN must interface with existing physical objects.

## Sensors and electronics components

Sensor and component partners contribute to ORIGIN's sensing ecosystem, embedded electronics, and expansion capabilities.

## Engineering ownership

Team Galene remains responsible for the design, integration, testing, operation, and documentation of ORIGIN regardless of which sponsor provides a tool, material, or manufacturing service.
''',
"centaurus-ai/README.md": r'''# Centaurus AI

**Centaurus AI** is ORIGIN's intelligent analysis and decision-support layer. It works above the embedded device software and uses structured observations, system health, context, and event history to help operators understand what deserves attention.

## Inputs

Depending on the deployment configuration, Centaurus can consume presence observations, movement and distance information, environmental measurements, device health, power state, communications state, timestamps, source identity, configuration information, and recent event history.

## Analysis

Centaurus can combine multiple observations, compare them with contextual expectations, identify unusual patterns, correlate activity across sensors or units, and assign structured confidence or priority information.

## Explainability

Higher-level conclusions remain linked to the underlying evidence. Operators can review which sources contributed, their health state, the relevant time window, and the analysis context.

## Human oversight

Centaurus is designed as **decision support**. It helps prioritize and interpret information, while consequential actions at a heritage site remain subject to human review and institutional procedures.

## Privacy-aware design

ORIGIN's radar-based presence sensing can provide useful occupancy and motion information without inherently requiring identifiable camera imagery. Centaurus is designed around structured sensor data and data minimization principles.

Continue with [Architecture](architecture.md), [Detection & Analysis](detection-and-analysis.md), [Decision Logic](decision-logic.md), [Cybersecurity](cybersecurity.md), [Data Processing](data-processing.md), and [Operating Boundaries](limitations.md).
''',
"centaurus-ai/limitations.md": r'''# Operating Boundaries

Centaurus is designed to make ORIGIN information easier to interpret while keeping the limits of automated analysis clear to users.

## Evidence quality

The quality of an analysis depends on the quality and context of the observations available to it. Sensor health, placement, calibration, timing, and site conditions therefore remain important parts of the overall system.

## Confidence is contextual

Confidence describes how strongly the available evidence supports a particular interpretation. It is not the same as severity, and it should not be presented as a guarantee.

## Site context matters

A museum, outdoor archaeological site, storage area, and temporary excavation can have very different normal activity patterns. Centaurus uses deployment context so unusual activity is interpreted in relation to the site rather than through one universal rule.

## Human review

Consequential action remains subject to human judgment. Operators can review the source observations, health information, timing, context, and explanation associated with a Centaurus event.

## Privacy and data minimization

Only information required for the monitoring objective should be retained or analyzed. Presence information can still be sensitive even when it does not contain identifiable imagery.

## Version-aware interpretation

Analysis behavior is associated with the active ORIGIN and Centaurus configuration so results can be interpreted in the context of the software and site settings that produced them.

These boundaries are part of responsible operation and help keep Centaurus useful, explainable, and appropriate for cultural-heritage environments.
''',
"resources/glossary.md": r'''# Glossary

### Aqua Base
An ORIGIN module that adapts the Core for water-adjacent or high-moisture deployment contexts.

### BIT
A modular ORIGIN attachment that adds a localized sensing, interaction, or site-specific function.

### Calibration
The process of adjusting and verifying sensor behavior for the real installation geometry and site conditions.

### Centaurus AI
ORIGIN's higher-level intelligent analysis and decision-support layer.

### Commissioning
The process that confirms an installed ORIGIN unit is correctly mounted, configured, calibrated, connected, and ready for normal use.

### Configuration
The site-specific settings that define identity, enabled sensors, modules, acquisition behavior, communications, calibration, and other operating parameters.

### C4001
The DFRobot 24 GHz mmWave sensor family used by ORIGIN for directional human-presence and motion sensing.

### Deployment
The complete use of one or more ORIGIN units at a site, including mounting, power, communications, configuration, calibration, commissioning, operation, and maintenance.

### Device health
A structured description of whether a subsystem is operating normally, initializing, intentionally disabled, temporarily unavailable, or requires attention.

### Drone Mount
The ORIGIN mechanical configuration for approved aerial inspection workflows.

### Event
A structured change or condition created from one or more observations and presented to higher-level software or an operator.

### Expansion System
The common mechanical, electrical, configuration, and identity model used by ORIGIN modules.

### LIS3DH
A three-axis accelerometer integrated into the Rosetta architecture for motion and orientation information.

### mmWave
Millimeter-wave radar technology used by ORIGIN for privacy-aware presence and motion sensing.

### Observation
A structured sensor or subsystem record associated with a source, timestamp, value or state, and health information.

### ORIGIN Core
The main field unit of the ORIGIN platform, containing Rosetta electronics, sensing, power, communications, software, and mechanical protection.

### ORIGIN 2026
The current documented ORIGIN platform generation.

### Rosetta
The custom electronics platform at the center of ORIGIN Core.

### Rosetta v2
The current documented Rosetta electronics generation used by ORIGIN Core.

### Site assessment
The process of evaluating a heritage environment before installation, including mounting, sensing, power, communications, conservation, and service requirements.

### System state
A machine- and operator-readable representation of the current condition of a device or subsystem.

### Team Galene
The student robotics and engineering team from the 4th General Lyceum of Ioannina, Greece, behind Project ORIGIN.

### Version
An identifier used to associate hardware, software, configuration, mechanics, modules, or documentation with the correct product state.
''',
}

for rel, text in PAGES.items():
    (ROOT / rel).write_text(text.rstrip() + "\n", encoding="utf-8")
    print("rewrote", rel)

# Update visible navigation labels without changing stable paths.
summary = ROOT / "SUMMARY.md"
text = summary.read_text(encoding="utf-8")
subs = {
    "## Development": "## Product Information",
    "* [Development](development/README.md)": "* [Product Information](development/README.md)",
    "* [Roadmap](development/roadmap.md)": "* [Platform Evolution](development/roadmap.md)",
    "* [Versions](development/versions.md)": "* [Version Guide](development/versions.md)",
    "* [Changelog](development/changelog.md)": "* [Release Highlights](development/changelog.md)",
    "* [Known Issues](development/known-issues.md)": "* [Operating Notes](development/known-issues.md)",
    "* [Planned Improvements](development/planned-improvements.md)": "* [Platform Capabilities](development/planned-improvements.md)",
    "## Open Source": "## Technical Resources",
    "* [Open Source](open-source/README.md)": "* [Technical Resources](open-source/README.md)",
    "* [Repository](open-source/repository.md)": "* [Documentation Repository](open-source/repository.md)",
    "* [Development Setup](open-source/development-setup.md)": "* [Using ORIGIN Docs](open-source/development-setup.md)",
    "* [Contributing](open-source/contributing.md)": "* [Community & Collaboration](open-source/contributing.md)",
    "* [Licensing](open-source/licensing.md)": "* [Usage & Attribution](open-source/licensing.md)",
    "* [Durrès Pilot](deployments/durres-pilot.md)": "* [Durrès Deployment Program](deployments/durres-pilot.md)",
    "* [Durrës Pilot](deployments/durres-pilot.md)": "* [Durrës Deployment Program](deployments/durres-pilot.md)",
    "* [Findings](deployments/findings.md)": "* [Field Insights](deployments/findings.md)",
    "* [Lessons Learned](deployments/lessons-learned.md)": "* [Deployment Practices](deployments/lessons-learned.md)",
    "* [Future Deployments](deployments/future-deployments.md)": "* [Deployment Models](deployments/future-deployments.md)",
    "* [Schematics](rosetta/schematics.md)": "* [Electrical Design](rosetta/schematics.md)",
    "* [BOM](rosetta/bom.md)": "* [Key Components](rosetta/bom.md)",
    "* [Manufacturing](rosetta/manufacturing.md)": "* [Production & Quality](rosetta/manufacturing.md)",
    "* [Assembly & Bring-up](rosetta/assembly-and-bring-up.md)": "* [Startup & Verification](rosetta/assembly-and-bring-up.md)",
    "* [Troubleshooting](rosetta/troubleshooting.md)": "* [Diagnostics](rosetta/troubleshooting.md)",
    "* [Validation Results](testing-validation/validation-results.md)": "* [Quality Evidence](testing-validation/validation-results.md)",
    "* [Limitations](centaurus-ai/limitations.md)": "* [Operating Boundaries](centaurus-ai/limitations.md)",
}
for a, b in subs.items():
    text = text.replace(a, b)
summary.write_text(text, encoding="utf-8")
print("updated SUMMARY.md")
