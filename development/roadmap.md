# Roadmap

The ORIGIN roadmap defines the sequence by which the project should mature from an integrated prototype platform into a repeatable, evidence-backed heritage monitoring system.

The roadmap is capability-based rather than date-based. Work advances when the required engineering evidence exists, not simply because a target date has arrived.

## Roadmap principles

The roadmap follows five rules:

1. **Stabilize interfaces before adding complexity.**
2. **Validate the physical system before relying on higher-level intelligence.**
3. **Resolve manufacturing blockers before scaling hardware.**
4. **Treat deployment evidence as a development input.**
5. **Do not promote planned capabilities as completed features.**

## Track 1 — Rosetta v2 manufacturing readiness

### Objective

Move Rosetta v2 from a documented board design into a reproducible fabrication and assembly package.

### Current focus

Reconcile the authoritative schematic, PCB, and BOM sources.

Regenerate fabrication outputs from the current PCB revision.

Include complete drill data in the manufacturing package.

Verify board outline and mounting geometry.

Verify component references and footprints.

Produce a revision-controlled BOM.

Prepare placement data where automated assembly is used.

Complete visual and electrical bring-up procedures.

Record manufacturing deviations and approved substitutions.

### Exit criteria

This track is considered mature when a third party can manufacture and assemble the intended Rosetta revision from the released package without relying on undocumented team knowledge.

## Track 2 — Core mechanical stabilization

### Objective

Turn the current tall, faceted ORIGIN enclosure direction into a serviceable mechanical platform suitable for repeated manufacturing and field validation.

### Current focus

Finalize the enclosure architecture around Rosetta v2.

Finalize mounts for the three mmWave sensor modules.

Preserve clear sensor fields of view.

Maintain side-accessible module interfaces.

Refine the solar support system, including the hollow cable-routing support.

Remain within the 250 × 250 × 250 mm single-part manufacturing constraint.

Define fastener strategy and service access.

Improve sealing around penetrations.

Define cable strain relief and internal routing.

Prepare release-quality STEP/STL/CAD exports.

### Exit criteria

A mechanical revision should pass fit, assembly, access, mounting, and relevant environmental tests before becoming the preferred deployment enclosure.

## Track 3 — Sensor-system characterization

### Objective

Establish measured ORIGIN-level sensing behavior rather than relying only on component datasheets.

### Current focus

Characterize the three-sensor mmWave arrangement.

Map coverage and blind regions for representative installations.

Test static and moving presence scenarios.

Identify environmental and geometric false-trigger conditions.

Define calibration procedures.

Characterize sensor-to-sensor consistency.

Verify sensor health reporting.

Document environmental-monitoring channels as hardware is finalized.

### Exit criteria

The sensor system should have documented test methods, repeatable results, deployment-specific calibration rules, and clearly stated limitations.

## Track 4 — Power subsystem maturity

### Objective

Validate the power system as an operational subsystem rather than only as a schematic architecture.

### Current focus

Validate charging behavior.

Characterize regulator behavior under representative loads.

Validate battery operation and recovery paths.

Characterize power consumption by operating state.

Test low-power and fault behavior.

Validate solar integration once the final panel and deployment geometry are fixed.

Establish measurable energy-budget assumptions.

Define power-related health telemetry.

### Exit criteria

Battery-life, solar-autonomy, and recovery claims should only be published once validated on the integrated system under defined conditions.

## Track 5 — Firmware consolidation

### Objective

Create a reproducible embedded software baseline for Rosetta and ORIGIN Core.

### Current focus

Define authoritative firmware source repository and build environment.

Document supported hardware revisions.

Formalize sensor drivers and abstraction boundaries.

Implement structured health states.

Improve local buffering and fault recovery.

Version configuration schemas.

Document logging and diagnostics.

Establish safe update and rollback procedures.

Automate repeatable build outputs where practical.

### Exit criteria

A maintainer should be able to build, install, configure, verify, and recover the firmware from documentation and version-controlled sources.

## Track 6 — Communications and data pipeline

### Objective

Make data movement observable, recoverable, and versioned across unreliable field connectivity.

### Current focus

Define supported transport paths.

Specify message or record schemas.

Assign device and deployment identities.

Preserve timestamps and provenance.

Buffer data during connectivity loss.

Detect delayed, duplicated, or malformed records.

Validate reconnect behavior.

Define retention and synchronization rules.

Document compatibility between firmware and downstream data consumers.

### Exit criteria

A network outage should degrade data delivery predictably without silently corrupting measurements or losing the ability to diagnose what happened.

## Track 7 — Centaurus AI validation

### Objective

Move Centaurus from architectural intent toward measurable and reviewable decision support.

### Current focus

Define explicit input data requirements.

Separate deterministic rules from learned analysis.

Define event and anomaly classes.

Record confidence and provenance.

Create labeled evaluation datasets where appropriate.

Define false-positive and false-negative review methods.

Establish versioned model/evaluation records.

Validate human-review workflows.

Document privacy and security constraints.

### Exit criteria

Centaurus capabilities should be associated with measurable evaluation procedures, known limitations, and traceable model or logic versions.

## Track 8 — Module interface standardization

### Objective

Make BITs, Aqua Base, Drone Mount, and future modules behave as controlled extensions rather than one-off attachments.

### Current focus

Define mechanical interface expectations.

Define electrical/power boundaries where applicable.

Define module identity and compatibility information.

Define health/status integration.

Define module-specific commissioning rules.

Keep module removal from compromising Core serviceability.

Document breaking interface changes.

### Exit criteria

A new module should be integrable through documented interfaces without redesigning the core system for every extension.

## Track 9 — Deployment readiness

### Objective

Turn laboratory integration into a repeatable field process.

### Current focus

Standardize site assessment.

Standardize mounting and setup.

Verify sensor orientation and coverage.

Formalize calibration.

Verify power and communications readiness.

Perform end-to-end commissioning.

Establish handover and service records.

Define rollback/removal procedures.

Preserve heritage-site reversibility requirements.

### Exit criteria

Different trained operators should be able to deploy comparable units using the same documented process and produce comparable commissioning records.

## Track 10 — Durrës pilot execution

### Objective

Use the planned five-unit collaboration with the Archaeological Museum of Durrës as a controlled learning deployment.

### Current focus

Confirm site-specific requirements.

Match unit configuration to installation locations.

Establish baseline records.

Perform deployment and commissioning using the documented workflow.

Collect reliability, sensing, maintenance, and operator observations.

Distinguish failures from site-specific behavior.

Feed evidence back into hardware, software, and procedures.

### Exit criteria

The pilot should produce traceable deployment evidence and concrete engineering lessons, not only a demonstration of the project concept.

## Track 11 — Maintenance and serviceability

### Objective

Reduce the amount of expert knowledge required to keep deployed units operating.

### Current focus

Improve self-diagnostics.

Define service states.

Identify field-replaceable components.

Standardize inspection records.

Improve fault isolation.

Document recommissioning after repair.

Refine enclosure access and fastener strategy.

Establish spare-part and compatibility records.

### Exit criteria

Routine faults should be diagnosable and repairable without rebuilding the entire device or losing configuration history.

## Track 12 — Open-source release quality

### Objective

Make the public project understandable and reproducible without exposing sensitive deployment or cybersecurity information.

### Current focus

Maintain GitBook/GitHub synchronization.

Publish source and export artifacts by revision.

Maintain BOM, CAD, schematic, and manufacturing references.

Publish contribution guidance.

Define licenses clearly.

Separate public engineering documentation from credentials and operational secrets.

Keep changelog and known-issues records current.

### Exit criteria

A technically competent external reader should be able to understand what ORIGIN is, what is currently supported, what remains experimental, and how to reproduce the released parts of the project.

## Longer-term exploration

The following areas are valid research directions, but they are not presented as committed current functionality: alternative edge-compute platforms, including Raspberry Pi-class systems; automatic deployment configuration and tooling; improved remote diagnostics; expanded sensor families; additional module classes; fleet-level comparison across multiple heritage sites; stronger automated validation pipelines; and richer visualization and decision-support tools.

## Roadmap review

The roadmap should be revised whenever field evidence changes priorities; a hardware revision breaks an interface; a major blocker is resolved; a planned feature is dropped; a new deployment introduces requirements not covered by the current architecture; and validation shows that an assumption was incorrect.

The roadmap is therefore a controlled development guide, not a promise that every listed feature will ship unchanged.
