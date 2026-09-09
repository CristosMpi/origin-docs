# Planned Improvements

This page lists planned ORIGIN improvements that are considered technically valuable but are **not yet treated as completed functionality**.

The list is prioritized by impact on reproducibility, reliability, maintainability, deployment readiness, and evidence quality.

## Priority 1 — Complete Rosetta v2 release package

### Goal

Make Rosetta v2 independently manufacturable from a single clearly versioned public release.

### Planned work

- publish the authoritative schematic and PCB sources;
- regenerate Gerbers from the final current PCB revision;
- include complete drill files;
- publish a complete BOM with manufacturer part numbers;
- publish placement/assembly data where relevant;
- identify approved substitutions;
- verify mounting-hole and board-outline geometry;
- archive the exact release package by revision;
- link fabrication outputs back to the source commit or tagged release.

### Expected benefit

Reduces fabrication ambiguity and enables reproducible hardware builds.

## Priority 2 — Freeze the next enclosure release candidate

### Goal

Convert the current tall, architectural enclosure direction into a mechanically frozen candidate suitable for formal validation.

### Planned work

- finalize the external geometry;
- finalize internal Rosetta mounting;
- finalize all three mmWave sensor mounts;
- finalize service-access panels;
- finalize M3 fastener locations and lengths;
- finalize side-accessible BITs attachment;
- finalize solar-panel support geometry;
- retain hollow cable routing through the third solar support;
- verify all individual manufactured parts remain within the 250 × 250 × 250 mm limit;
- create a released STEP/STL/drawing set.

### Expected benefit

Creates a stable physical baseline for fit, sealing, sensor, and environmental testing.

## Priority 3 — Improve enclosure sealing without compromising sensing

### Goal

Reduce ingress and condensation risk while preserving mmWave performance.

### Planned work

- evaluate radar-transparent sensor-window materials;
- improve gasket and joint geometry;
- define cable-gland and strain-relief details;
- test drainage paths;
- study condensation inside the enclosure;
- test the effect of protective covers on mmWave behavior;
- define an evidence-backed environmental target.

### Expected benefit

Improves field reliability while keeping the sensing architecture practical.

## Priority 4 — Characterize the three-mmWave arrangement

### Goal

Replace assumed or datasheet-derived coverage claims with ORIGIN-level measurements.

### Planned work

- map detection range by sensor direction;
- identify blind spots and overlap regions;
- test standing, walking, approaching, departing, and stationary-presence scenarios;
- test reflections near walls, metal, vegetation, and archaeological structures;
- compare indoor and outdoor behavior;
- record false positives and false negatives;
- define site calibration procedures;
- quantify repeatability across multiple sensor modules.

### Expected benefit

Provides real evidence for presence-detection claims and improves deployment planning.

## Priority 5 — Establish a complete power budget

### Goal

Quantify real power consumption and energy autonomy.

### Planned work

- measure current draw by operating state;
- characterize boot, sensing, communications, storage, and low-power modes;
- characterize charging behavior;
- characterize battery discharge under representative loads;
- measure regulator efficiency on the integrated board;
- model and validate solar contribution;
- define low-battery behavior;
- define power-health telemetry;
- validate recovery after extended low-energy periods.

### Expected benefit

Enables defensible battery-life and solar-autonomy planning.

## Priority 6 — Formalize firmware releases

### Goal

Turn the embedded software into a reproducible release process.

### Planned work

- identify the authoritative firmware repository;
- pin supported toolchain/framework versions;
- document exact build targets;
- version configuration schemas;
- version data/message schemas;
- produce tagged firmware releases;
- attach source revision metadata to binaries;
- implement structured logs and diagnostics;
- improve watchdog and fault recovery;
- define update and rollback procedures.

### Expected benefit

Allows maintainers to rebuild and recover the software without undocumented setup knowledge.

## Priority 7 — Expand self-diagnostics

### Goal

Make ORIGIN better at detecting failures in itself.

### Planned work

- add power subsystem health checks;
- detect missing or unresponsive sensors;
- track communication failures;
- track storage utilization and write failures;
- expose firmware reset reasons;
- detect stale sensor data;
- record configuration mismatches;
- add module-presence and compatibility checks;
- improve operator-facing diagnostic summaries.

### Expected benefit

Reduces maintenance time and improves confidence in unattended operation.

## Priority 8 — Improve offline-first data behavior

### Goal

Ensure connectivity loss does not silently destroy data quality.

### Planned work

- define local buffer limits;
- preserve timestamps and sequence identity;
- detect duplicates after reconnect;
- define retry/backoff behavior;
- expose synchronization state;
- distinguish missing data from delayed data;
- test long-duration connectivity loss;
- verify recovery after power cycling while offline.

### Expected benefit

Makes field operation more resilient where network quality is poor.

## Priority 9 — Turn Centaurus into a fully evaluable subsystem

### Goal

Move from architecture-level AI documentation to versioned, measurable implementation evidence.

### Planned work

- define exact analysis tasks;
- define labeled datasets where appropriate;
- separate rules-based logic from learned models;
- version model and decision-logic releases;
- record confidence and provenance;
- build evaluation scripts;
- define threshold-tuning procedures;
- report false-positive and false-negative behavior;
- maintain human-review paths;
- document failure modes and edge cases.

### Expected benefit

Creates credible AI performance claims tied to specific versions and datasets.

## Priority 10 — Strengthen cybersecurity implementation

### Goal

Verify that the actual implementation matches the documented security principles.

### Planned work

- remove secrets from public repositories and artifacts;
- define credential provisioning and rotation;
- verify update authenticity;
- protect deployment configuration;
- improve audit/event logging;
- define least-privilege backend access;
- test recovery after credential failure;
- review exposed network services;
- perform implementation-level security review before large-scale deployment.

### Expected benefit

Reduces the risk that monitoring infrastructure itself becomes a security weakness.

## Priority 11 — Standardize the Expansion System

### Goal

Create a stable module interface for BITs, Aqua Base, Drone Mount, and future extensions.

### Planned work

- freeze mechanical attachment references;
- define allowed power ranges;
- define connector/pinout standards where applicable;
- define module identity metadata;
- define compatibility/version negotiation;
- define module health reporting;
- define commissioning steps;
- publish module-interface drawings and schemas.

### Expected benefit

Allows new modules to be created without redesigning ORIGIN Core.

## Priority 12 — Improve BITs serviceability and educational tooling

### Goal

Make BITs easier to access, program, replace, and demonstrate.

### Planned work

- refine the side-accessible attachment;
- standardize fasteners and alignment features;
- improve cable or electrical interface protection;
- document MakeCode workflows;
- create example educational activities;
- define safe sandbox behavior so BITs experimentation does not compromise the Core system.

### Expected benefit

Improves educational use while preserving product serviceability.

## Priority 13 — Mature Aqua Base

### Goal

Turn Aqua Base from a module concept into an evidence-backed deployment option.

### Planned work

- define intended water-adjacent operating environments;
- validate materials against corrosion and moisture;
- define anchoring or support strategy;
- test sealing and cable routing;
- validate sensors in the intended environment;
- define maintenance intervals based on observed fouling/corrosion;
- document safe retrieval and service procedures.

### Expected benefit

Expands ORIGIN to additional conservation contexts without overgeneralizing the Core enclosure.

## Priority 14 — Mature Drone Mount

### Goal

Create a clearly bounded aerial integration path.

### Planned work

- define compatible payload classes;
- validate mounting security;
- characterize center-of-gravity effects;
- characterize vibration transfer;
- evaluate electromagnetic interference;
- define emergency release/removal procedures;
- document platform-specific flight validation;
- keep regulatory responsibility explicit.

### Expected benefit

Makes drone integration safer and more reproducible.

## Priority 15 — Automate configuration and commissioning

### Goal

Reduce manual setup errors when deploying multiple units.

### Planned work

- create a configuration generator;
- validate configuration before flashing/applying it;
- generate deployment IDs automatically;
- produce unit-specific commissioning records;
- detect incompatible hardware/software combinations;
- export human-readable configuration summaries;
- explore MATLAB or other engineering-tool integration where it provides real value.

### Expected benefit

Makes multi-unit deployment faster and less error-prone.

## Priority 16 — Improve maintenance analytics

### Goal

Use service history to improve the product rather than only repair individual failures.

### Planned work

- record failure categories consistently;
- record replaced parts and causes;
- track recurring connector, sealing, sensor, and power issues;
- compare failure patterns by deployment environment;
- identify parts that should become field-replaceable;
- feed recurring faults into design revisions.

### Expected benefit

Turns maintenance records into engineering evidence.

## Priority 17 — Complete the Durrës pilot evidence loop

### Goal

Use the five-unit pilot to validate the real deployment workflow.

### Planned work

- capture site assessments;
- record exact unit configurations;
- perform standardized calibration;
- record commissioning results;
- collect uptime and fault observations;
- collect operator feedback;
- record maintenance interventions;
- compare unit behavior across locations;
- convert findings into documented design changes.

### Expected benefit

Provides the first structured multi-unit field evidence for ORIGIN.

## Priority 18 — Improve open-source release quality

### Goal

Make the public project easier for external contributors and reviewers to reproduce.

### Planned work

- finalize licensing;
- publish contribution guidelines;
- publish hardware source releases;
- publish software source releases;
- publish CAD exports;
- publish BOMs and manufacturing files;
- publish non-sensitive test data where appropriate;
- add issue templates and contribution workflow;
- keep GitBook synchronized with the authoritative repository.

### Expected benefit

Transforms the documentation from a project showcase into a usable engineering resource.

## Priority 19 — Create compatibility and migration tooling

### Goal

Reduce confusion as ORIGIN revisions multiply.

### Planned work

- maintain a hardware/software compatibility matrix;
- define migration notes for breaking changes;
- identify which deployed units require updates;
- preserve historical documentation for older units;
- provide clear deprecation notices.

### Expected benefit

Makes long-term maintenance possible without freezing innovation.

## Priority 20 — Build stronger automated validation

### Goal

Catch regressions earlier.

### Planned work

- automate firmware build checks;
- validate configuration schemas;
- run static documentation link checks;
- verify manufacturing package completeness;
- add software unit/integration tests where appropriate;
- generate repeatable test reports;
- track validation evidence by release.

### Expected benefit

Reduces the chance of releasing incomplete or incompatible artifacts.

## Improvement selection rule

Planned improvements should be promoted into active development based on:

- field risk;
- release blockers;
- impact on reproducibility;
- impact on reliability;
- value to deployment partners;
- test evidence;
- maintenance burden;
- compatibility impact;
- engineering effort.

A planned improvement becomes a supported feature only after implementation, documentation, and the appropriate validation are complete.
