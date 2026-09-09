# Glossary

This glossary defines the principal terms, subsystem names, engineering concepts, and status language used throughout **ORIGIN Docs**.

Where a term refers to a third-party component, the definition describes how that component is used or discussed within Project ORIGIN. A glossary entry is not, by itself, a performance claim or a substitute for the relevant manufacturer documentation.

## A

### Alert
A notification or operator-facing indication created when ORIGIN determines that an observation, event, health condition, or system state requires attention. An alert does not automatically mean that damage, intrusion, or another real-world incident has been confirmed.

### Aqua Base
An ORIGIN expansion concept intended for deployments in which water-related or moisture-related environmental context is relevant. Aqua Base is treated as a module rather than a required part of every ORIGIN installation.

### Assembly bring-up
The controlled process used after a PCB or complete electronic assembly has been manufactured. It normally begins with visual and unpowered checks, followed by current-limited power-up, rail verification, processor bring-up, peripheral testing, and system-level validation.

## B

### BITs
A modular ORIGIN subsystem intended to extend the platform and support accessible interaction, experimentation, education, or deployment-specific functions. BITs is designed as an expansion rather than a permanent bottom-mounted component so that ORIGIN can remain compatible with ground or soil installations.

### BOM — Bill of Materials
A structured list of the parts required to manufacture an assembly. A production BOM should identify exact manufacturer part numbers, quantities, references, alternatives, fitted/not-fitted status, and other purchasing information. A partial component list is not equivalent to a production-ready BOM.

### Buffering
Temporary local retention of observations, events, logs, or outgoing messages when immediate transmission is not possible. ORIGIN uses a local-first design philosophy so loss of connectivity does not automatically mean loss of all newly generated data.

## C

### C4001
A DFRobot 24 GHz mmWave radar sensor family used in the ORIGIN presence-detection architecture. The current ORIGIN Core design documents three C4001 modules around the enclosure.

### Calibration
The process of establishing, checking, or adjusting the relationship between a sensor or subsystem and the real environment in which it operates. For ORIGIN this may include radar coverage, orientation, environmental baselines, thresholds, or other deployment-specific parameters.

### Centaurus AI
The higher-level analysis and decision-support layer within Project ORIGIN. Centaurus consumes structured observations and system context to help identify patterns, anomalies, or conditions requiring attention. It is not documented as a replacement for deterministic embedded control or human responsibility.

### Commissioning
The formal process that moves an installed ORIGIN unit from “physically present” to “accepted for pilot or operational use.” Commissioning includes hardware checks, configuration verification, calibration, communications tests, sensor tests, fault/recovery checks, documentation, and operator handover.

### Configuration
The set of parameters that determine how an ORIGIN unit behaves at a particular site or in a particular hardware state. Configuration may include sensor enablement, site identity, thresholds, module selection, communications settings, and other deployment-specific values. Exact formats depend on the implemented software release.

### Connectivity
The ability of an ORIGIN unit to exchange data with external systems. Connectivity is treated as a subsystem with its own health state; the system should distinguish normal connection, temporary loss, degraded operation, and recovery.

## D

### Data pipeline
The sequence through which information moves from physical sensing to useful system output. In ORIGIN this is conceptually represented as hardware → driver → normalized observation → validation/state handling → local log or buffer → communications → higher-level processing/operator use.

### Degraded
A health state indicating that a component or subsystem is still providing some useful function but is not operating at the expected level. “Degraded” is intentionally different from both “healthy” and “failed.”

### Deployment
The installation and operation of ORIGIN in a real environment outside normal bench development. A deployment includes the physical unit, its site configuration, calibration, communications, maintenance process, and the people responsible for using the system.

### Deployment architecture
The arrangement of ORIGIN units, monitored zones, communications paths, power sources, operator workflows, and service responsibilities at a particular site.

### DFRobot SEN0609
The specific DFRobot C4001 24 GHz mmWave Human Presence Detection Sensor (25 m version) referenced in current ORIGIN documentation. Manufacturer specifications and ORIGIN-validated field performance are treated separately.

### Diagnostics
The process of identifying why a system, subsystem, sensor, or module is not behaving as expected. ORIGIN diagnostics follow a layered approach so physical, power, processor, sensor, storage, communications, configuration, and analysis faults can be distinguished.

### Durrës Pilot
The planned five-unit ORIGIN pilot associated with the Archaeological Museum of Durrës, Albania. Until installation and commissioning evidence exists, the documentation describes it as a planned/pilot deployment rather than an already operational protection system.

## E

### Edge.Cuts
The KiCad PCB layer that defines board-profile geometry. The reviewed Rosetta v2 Gerber package contains an Edge.Cuts export with a predominantly circular profile and an additional closed rectangular feature near the upper edge; its intended manufacturing interpretation must be confirmed before production release.

### Environmental monitoring
The observation of physical environmental conditions relevant to a heritage site. The exact deployed sensor set can vary by ORIGIN configuration, and public documentation distinguishes confirmed sensors from examples or future expansion options.

### ESP32-family processor
The processor family currently documented for Rosetta. Until the exact processor variant is verified from released source material, ORIGIN Docs intentionally avoid presenting a more specific MCU part number as confirmed.

### Event
A structured representation of something the system has observed or inferred as significant enough to record or process beyond a raw sample. An event is not necessarily an alarm.

### Excellon drill file
A manufacturing file commonly used to define PCB holes and drill information. The reviewed Rosetta v2 Gerber ZIP did not include drill data, which is why that package is explicitly marked incomplete for fabrication.

### Expansion System
The common mechanical, electrical, identity, communications, and compatibility model used to connect optional ORIGIN modules to the Core platform.

## F

### Fault
A health state indicating that a component or subsystem cannot provide its expected function or has entered a condition requiring intervention. Fault states should be diagnosable rather than being represented only as missing data.

### Field testing
Testing performed in realistic or real deployment conditions, where geometry, weather, visitors, reflections, communications, installation constraints, and operator workflows can expose issues that are difficult to reproduce in the laboratory.

### Firmware
Software that runs on the embedded controller inside ORIGIN/Rosetta and directly interacts with hardware, sensors, storage, communications, health states, and other device-level functions.

### FMCW — Frequency-Modulated Continuous Wave
A radar technique used by the C4001 mmWave sensor family. Manufacturer documentation should be used for detailed radar implementation and specifications.

## G

### Galene Lab Standards
Team Galene’s documentation framework for reproducible ORIGIN testing. It defines principles for test identity, configuration control, procedure, evidence, results, failures, repetition, and the separation of measured results from assumptions.

### Gerber
A standard family of PCB fabrication files representing copper, solder mask, silkscreen, paste, board geometry, and other manufacturing layers. Gerbers alone may not constitute a complete fabrication package if required drill or manufacturing information is missing.

### GitBook
The documentation publishing platform used for the public ORIGIN documentation site. The documentation source is maintained in the linked GitHub repository and structured through `SUMMARY.md` and GitBook configuration files.

## H

### Health state
A machine- and operator-readable representation of the current condition of a sensor or subsystem. ORIGIN documentation uses states such as initializing, healthy, degraded, missing, invalid, disabled, and fault so different failure modes are not collapsed into one generic error.

### Human-in-the-loop
A design principle in which automated analysis supports human operators rather than removing human responsibility from important decisions. This is a central boundary in the Centaurus AI architecture.

## I

### Invalid
A sensor or data state indicating that information was received but cannot currently be trusted or interpreted as a valid observation. Invalid is different from missing, where no usable observation is available at all.

### IP rating
An Ingress Protection classification describing resistance to solid-particle and water ingress under a defined test standard. ORIGIN does not claim a formal IP rating unless the relevant enclosure revision has actually been tested and documented against that standard.

## K

### KiCad
The electronic design automation software used for at least part of Rosetta PCB development. The reviewed Rosetta v2 fabrication export identifies KiCad Pcbnew 10.0.1 as its generating application.

## L

### LIS3DH
A three-axis accelerometer included in the Rosetta design. It can provide movement or orientation context, subject to the behavior implemented in firmware and validated for a particular release.

### Local-first operation
An ORIGIN design principle in which essential sensing, health handling, and local data retention do not depend completely on continuous remote connectivity. Remote services can add value, but temporary connection loss should not automatically make the device incapable of basic operation.

## M

### Maintenance
The set of preventive, condition-based, and corrective activities used to keep an installed ORIGIN unit in a known state. Maintenance includes inspection, diagnostics, cleaning, alignment checks, replacement, configuration verification, and recommissioning where necessary.

### Missing
A health state meaning that an expected device, sample, peripheral, or data source is not available. The system should report missing data explicitly instead of silently substituting a normal value.

### mmWave — Millimeter wave
Radio-frequency technology using wavelengths in the millimeter range. ORIGIN uses 24 GHz mmWave radar modules for presence and motion-related sensing without relying on conventional camera imagery for that function.

### Module
An optional ORIGIN subsystem that extends the capabilities or deployment form of ORIGIN Core. Current documented module families include BITs, Aqua Base, and Drone Mount.

## O

### Observation
A normalized representation of a measurement or state received from hardware after the software has interpreted the device-level data sufficiently for the rest of the system to use it.

### ORIGIN
Team Galene’s modular engineering platform for monitoring and supporting the protection and long-term preservation of cultural heritage and archaeological environments.

### ORIGIN Core
The principal field unit of Project ORIGIN. ORIGIN Core brings together Rosetta electronics, sensing, power, communications, software, mechanical protection, and the interfaces used by optional modules.

### ORIGIN Docs
The maintained technical documentation for Project ORIGIN, covering architecture, hardware, software, AI, mechanical design, installation, testing, deployment, maintenance, development, open-source status, sponsors, and project terminology.

## P

### PCB — Printed Circuit Board
A manufactured board that mechanically supports and electrically connects electronic components using conductive tracks, pads, vias, and other features.

### PCBA — Printed Circuit Board Assembly
A PCB after components have been assembled onto it. PCBA production normally requires manufacturing information beyond bare-board Gerbers, such as a BOM and component-placement data.

### Pilot deployment
A controlled real-world deployment used to evaluate installation, operation, performance, maintenance, usability, and system assumptions before broader rollout.

### Presence detection
The ORIGIN subsystem responsible for identifying presence- or motion-related radar observations. Current mechanical and sensor documentation is based around three DFRobot C4001 SEN0609 modules.

### Provenance
Information that records where data, configuration, results, or decisions came from. Good provenance makes it possible to connect a result to the correct unit, hardware revision, firmware, site configuration, calibration state, timestamp, and test or deployment context.

## R

### Recommissioning
A controlled validation process performed after a meaningful service action or change to confirm that the unit still satisfies its deployment requirements. Recommissioning may be required after sensor replacement, major configuration changes, enclosure work, firmware changes, or other interventions.

### Reversible mounting
A heritage-oriented installation principle in which mounting methods should avoid unnecessary or permanent modification of protected surfaces and should be removable where site requirements demand it.

### Rollback
The controlled return from a new software, firmware, configuration, or model version to a previously known working version when an update fails validation or causes unacceptable behavior.

### Rosetta
The custom electronics platform at the center of ORIGIN Core. It provides the embedded processing, power-management, sensor, storage, and expansion foundation on which the field unit operates.

### Rosetta v2
The current documented generation of the Rosetta PCB. The reviewed fabrication export is a two-layer, approximately 100 × 105 mm board package generated in July 2026. The reviewed ZIP is not production-ready because drill data is absent and some release metadata remains incomplete.

## S

### Sensor fusion
The process of interpreting information from multiple sensors or multiple observations together rather than treating each source as an isolated final decision. Centaurus and other higher-level logic can use this approach to add context and reduce over-reliance on one signal.

### Sensor state model
The software model used to describe whether a sensor is disabled, initializing, healthy, degraded, missing, invalid, or in fault. Exact implemented states should follow the corresponding firmware release.

### Site assessment
The pre-installation process used to understand a heritage site before choosing ORIGIN positions, mounting methods, sensor orientation, power strategy, communications, maintenance access, and commissioning criteria.

### Solar system
The mechanical and electrical subsystem used when an ORIGIN configuration includes solar-assisted energy input. Current mechanical design includes a third hollow solar-panel support intended to provide a protected cable route.

### Source of truth
The authoritative version of information used for engineering decisions. For public ORIGIN Docs, the GitHub repository is the maintained source for the documentation content; hardware, firmware, CAD, and manufacturing releases should each identify their own authoritative versioned artifacts.

## T

### Team Galene
The student robotics and engineering team from the 4th General Lyceum of Ioannina, Greece, responsible for developing Project ORIGIN.

### Telemetry
Structured device information communicated for monitoring, diagnostics, analysis, or operator visibility. ORIGIN documentation does not assume a particular cloud provider or transport protocol unless one is confirmed by the released implementation.

### Troubleshooting
The structured process of moving from an observed symptom toward the most likely failure domain, collecting evidence, applying a controlled corrective action, and confirming recovery.

## U

### Unit identity
A stable identifier assigned to an ORIGIN field unit so its hardware revision, enclosure, firmware, configuration, calibration, deployment position, and maintenance history can be traced consistently.

### Update
A controlled change to firmware, software, configuration, AI/model components, or other versioned system assets. ORIGIN update design emphasizes compatibility checks, validation, recovery, traceability, and rollback rather than assuming every new version should be deployed immediately.

## V

### Validation
The process of collecting sufficient evidence to support a technical claim or to determine whether a component, subsystem, or complete ORIGIN configuration meets defined acceptance criteria.

### Validation result
A documented outcome tied to a specific test configuration and evidence set. ORIGIN Docs distinguish validated results from observations, defined procedures, identified issues, and claims that have not yet been validated.

### Version
A controlled identifier for a hardware, software, configuration, CAD, documentation, or deployment state. ORIGIN uses versioning to prevent results or fixes from being applied to the wrong revision.

## W

### Waterproofing
The collection of design methods used to reduce water ingress risk, including enclosure geometry, seals, drainage strategy, cable routing, interfaces, and assembly quality. ORIGIN uses the term descriptively unless a formal ingress-protection test has established a certified or validated rating.

---

If a term in ORIGIN Docs is unclear or is used inconsistently, it should be treated as a documentation issue and clarified before the term becomes part of a formal requirement, manufacturing release, or validation claim.
