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

reconcile the authoritative schematic, PCB, and BOM sources;.

regenerate fabrication outputs from the current PCB revision;.

include complete drill data in the manufacturing package;.

verify board outline and mounting geometry;.

verify component references and footprints;.

produce a revision-controlled BOM;.

prepare placement data where automated assembly is used;.

complete visual and electrical bring-up procedures;.

record manufacturing deviations and approved substitutions.

### Exit criteria

This track is considered mature when a third party can manufacture and assemble the intended Rosetta revision from the released package without relying on undocumented team knowledge.

## Track 2 — Core mechanical stabilization

### Objective

Turn the current tall, faceted ORIGIN enclosure direction into a serviceable mechanical platform suitable for repeated manufacturing and field validation.

### Current focus

finalize the enclosure architecture around Rosetta v2;.

finalize mounts for the three mmWave sensor modules;.

preserve clear sensor fields of view;.

maintain side-accessible module interfaces;.

refine the solar support system, including the hollow cable-routing support;.

remain within the 250 × 250 × 250 mm single-part manufacturing constraint;.

define fastener strategy and service access;.

improve sealing around penetrations;.

define cable strain relief and internal routing;.

prepare release-quality STEP/STL/CAD exports.

### Exit criteria

A mechanical revision should pass fit, assembly, access, mounting, and relevant environmental tests before becoming the preferred deployment enclosure.

## Track 3 — Sensor-system characterization

### Objective

Establish measured ORIGIN-level sensing behavior rather than relying only on component datasheets.

### Current focus

characterize the three-sensor mmWave arrangement;.

map coverage and blind regions for representative installations;.

test static and moving presence scenarios;.

identify environmental and geometric false-trigger conditions;.

define calibration procedures;.

characterize sensor-to-sensor consistency;.

verify sensor health reporting;.

document environmental-monitoring channels as hardware is finalized.

### Exit criteria

The sensor system should have documented test methods, repeatable results, deployment-specific calibration rules, and clearly stated limitations.

## Track 4 — Power subsystem maturity

### Objective

Validate the power system as an operational subsystem rather than only as a schematic architecture.

### Current focus

validate charging behavior;.

characterize regulator behavior under representative loads;.

validate battery operation and recovery paths;.

characterize power consumption by operating state;.

test low-power and fault behavior;.

validate solar integration once the final panel and deployment geometry are fixed;.

establish measurable energy-budget assumptions;.

define power-related health telemetry.

### Exit criteria

Battery-life, solar-autonomy, and recovery claims should only be published once validated on the integrated system under defined conditions.

## Track 5 — Firmware consolidation

### Objective

Create a reproducible embedded software baseline for Rosetta and ORIGIN Core.

### Current focus

define authoritative firmware source repository and build environment;.

document supported hardware revisions;.

formalize sensor drivers and abstraction boundaries;.

implement structured health states;.

improve local buffering and fault recovery;.

version configuration schemas;.

document logging and diagnostics;.

establish safe update and rollback procedures;.

automate repeatable build outputs where practical.

### Exit criteria

A maintainer should be able to build, install, configure, verify, and recover the firmware from documentation and version-controlled sources.

## Track 6 — Communications and data pipeline

### Objective

Make data movement observable, recoverable, and versioned across unreliable field connectivity.

### Current focus

define supported transport paths;.

specify message or record schemas;.

assign device and deployment identities;.

preserve timestamps and provenance;.

buffer data during connectivity loss;.

detect delayed, duplicated, or malformed records;.

validate reconnect behavior;.

define retention and synchronization rules;.

document compatibility between firmware and downstream data consumers.

### Exit criteria

A network outage should degrade data delivery predictably without silently corrupting measurements or losing the ability to diagnose what happened.

## Track 7 — Centaurus AI validation

### Objective

Move Centaurus from architectural intent toward measurable and reviewable decision support.

### Current focus

define explicit input data requirements;.

separate deterministic rules from learned analysis;.

define event and anomaly classes;.

record confidence and provenance;.

create labeled evaluation datasets where appropriate;.

define false-positive and false-negative review methods;.

establish versioned model/evaluation records;.

validate human-review workflows;.

document privacy and security constraints.

### Exit criteria

Centaurus capabilities should be associated with measurable evaluation procedures, known limitations, and traceable model or logic versions.

## Track 8 — Module interface standardization

### Objective

Make BITs, Aqua Base, Drone Mount, and future modules behave as controlled extensions rather than one-off attachments.

### Current focus

define mechanical interface expectations;.

define electrical/power boundaries where applicable;.

define module identity and compatibility information;.

define health/status integration;.

define module-specific commissioning rules;.

keep module removal from compromising Core serviceability;.

document breaking interface changes.

### Exit criteria

A new module should be integrable through documented interfaces without redesigning the core system for every extension.

## Track 9 — Deployment readiness

### Objective

Turn laboratory integration into a repeatable field process.

### Current focus

standardize site assessment;.

standardize mounting and setup;.

verify sensor orientation and coverage;.

formalize calibration;.

verify power and communications readiness;.

perform end-to-end commissioning;.

establish handover and service records;.

define rollback/removal procedures;.

preserve heritage-site reversibility requirements.

### Exit criteria

Different trained operators should be able to deploy comparable units using the same documented process and produce comparable commissioning records.

## Track 10 — Durrës pilot execution

### Objective

Use the planned five-unit collaboration with the Archaeological Museum of Durrës as a controlled learning deployment.

### Current focus

confirm site-specific requirements;.

match unit configuration to installation locations;.

establish baseline records;.

perform deployment and commissioning using the documented workflow;.

collect reliability, sensing, maintenance, and operator observations;.

distinguish failures from site-specific behavior;.

feed evidence back into hardware, software, and procedures.

### Exit criteria

The pilot should produce traceable deployment evidence and concrete engineering lessons, not only a demonstration of the project concept.

## Track 11 — Maintenance and serviceability

### Objective

Reduce the amount of expert knowledge required to keep deployed units operating.

### Current focus

improve self-diagnostics;.

define service states;.

identify field-replaceable components;.

standardize inspection records;.

improve fault isolation;.

document recommissioning after repair;.

refine enclosure access and fastener strategy;.

establish spare-part and compatibility records.

### Exit criteria

Routine faults should be diagnosable and repairable without rebuilding the entire device or losing configuration history.

## Track 12 — Open-source release quality

### Objective

Make the public project understandable and reproducible without exposing sensitive deployment or cybersecurity information.

### Current focus

maintain GitBook/GitHub synchronization;.

publish source and export artifacts by revision;.

maintain BOM, CAD, schematic, and manufacturing references;.

publish contribution guidance;.

define licenses clearly;.

separate public engineering documentation from credentials and operational secrets;.

keep changelog and known-issues records current.

### Exit criteria

A technically competent external reader should be able to understand what ORIGIN is, what is currently supported, what remains experimental, and how to reproduce the released parts of the project.

## Longer-term exploration

The following areas are valid research directions but are not presented as committed current functionality alternative edge-compute platforms, including Raspberry Pi-class systems; automatic deployment configuration and tooling; improved remote diagnostics; expanded sensor families; additional module classes; fleet-level comparison across multiple heritage sites; stronger automated validation pipelines; and richer visualization and decision-support tools.

## Roadmap review

The roadmap should be revised whenever field evidence changes priorities; a hardware revision breaks an interface; a major blocker is resolved; a planned feature is dropped; a new deployment introduces requirements not covered by the current architecture; and validation shows that an assumption was incorrect.

The roadmap is therefore a controlled development guide, not a promise that every listed feature will ship unchanged.
