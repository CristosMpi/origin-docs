# Planned Improvements

This page lists planned ORIGIN improvements that are considered technically valuable but are **not yet treated as completed functionality**.

The list is prioritized by impact on reproducibility, reliability, maintainability, deployment readiness, and evidence quality.

## Priority 1 — Complete Rosetta v2 release package

### Goal

Make Rosetta v2 independently manufacturable from a single clearly versioned public release.

### Planned work

Publish the authoritative schematic and PCB sources.

Regenerate Gerbers from the final current PCB revision.

Include complete drill files.

Publish a complete BOM with manufacturer part numbers.

Publish placement/assembly data where relevant.

Identify approved substitutions.

Verify mounting-hole and board-outline geometry.

Archive the exact release package by revision.

Link fabrication outputs back to the source commit or tagged release.

### Expected benefit

Reduces fabrication ambiguity and enables reproducible hardware builds.

## Priority 2 — Freeze the next enclosure release candidate

### Goal

Convert the current tall, architectural enclosure direction into a mechanically frozen candidate suitable for formal validation.

### Planned work

Finalize the external geometry.

Finalize internal Rosetta mounting.

Finalize all three mmWave sensor mounts.

Finalize service-access panels.

Finalize M3 fastener locations and lengths.

Finalize side-accessible BITs attachment.

Finalize solar-panel support geometry.

Retain hollow cable routing through the third solar support.

Verify all individual manufactured parts remain within the 250 × 250 × 250 mm limit.

Create a released STEP/STL/drawing set.

### Expected benefit

Creates a stable physical baseline for fit, sealing, sensor, and environmental testing.

## Priority 3 — Improve enclosure sealing without compromising sensing

### Goal

Reduce ingress and condensation risk while preserving mmWave performance.

### Planned work

Evaluate radar-transparent sensor-window materials.

Improve gasket and joint geometry.

Define cable-gland and strain-relief details.

Test drainage paths.

Study condensation inside the enclosure.

Test the effect of protective covers on mmWave behavior.

Define an evidence-backed environmental target.

### Expected benefit

Improves field reliability while keeping the sensing architecture practical.

## Priority 4 — Characterize the three-mmWave arrangement

### Goal

Replace assumed or datasheet-derived coverage claims with ORIGIN-level measurements.

### Planned work

Map detection range by sensor direction.

Identify blind spots and overlap regions.

Test standing, walking, approaching, departing, and stationary-presence scenarios.

Test reflections near walls, metal, vegetation, and archaeological structures.

Compare indoor and outdoor behavior.

Record false positives and false negatives.

Define site calibration procedures.

Quantify repeatability across multiple sensor modules.

### Expected benefit

Provides real evidence for presence-detection claims and improves deployment planning.

## Priority 5 — Establish a complete power budget

### Goal

Quantify real power consumption and energy autonomy.

### Planned work

Measure current draw by operating state.

Characterize boot, sensing, communications, storage, and low-power modes.

Characterize charging behavior.

Characterize battery discharge under representative loads.

Measure regulator efficiency on the integrated board.

Model and validate solar contribution.

Define low-battery behavior.

Define power-health telemetry.

Validate recovery after extended low-energy periods.

### Expected benefit

Enables defensible battery-life and solar-autonomy planning.

## Priority 6 — Formalize firmware releases

### Goal

Turn the embedded software into a reproducible release process.

### Planned work

Identify the authoritative firmware repository.

Pin supported toolchain/framework versions.

Document exact build targets.

Version configuration schemas.

Version data/message schemas.

Produce tagged firmware releases.

Attach source revision metadata to binaries.

Implement structured logs and diagnostics.

Improve watchdog and fault recovery.

Define update and rollback procedures.

### Expected benefit

Allows maintainers to rebuild and recover the software without undocumented setup knowledge.

## Priority 7 — Expand self-diagnostics

### Goal

Make ORIGIN better at detecting failures in itself.

### Planned work

Add power subsystem health checks.

Detect missing or unresponsive sensors.

Track communication failures.

Track storage utilization and write failures.

Expose firmware reset reasons.

Detect stale sensor data.

Record configuration mismatches.

Add module-presence and compatibility checks.

Improve operator-facing diagnostic summaries.

### Expected benefit

Reduces maintenance time and improves confidence in unattended operation.

## Priority 8 — Improve offline-first data behavior

### Goal

Ensure connectivity loss does not silently destroy data quality.

### Planned work

Define local buffer limits.

Preserve timestamps and sequence identity.

Detect duplicates after reconnect.

Define retry/backoff behavior.

Expose synchronization state.

Distinguish missing data from delayed data.

Test long-duration connectivity loss.

Verify recovery after power cycling while offline.

### Expected benefit

Makes field operation more resilient where network quality is poor.

## Priority 9 — Turn Centaurus into a fully evaluable subsystem

### Goal

Move from architecture-level AI documentation to versioned, measurable implementation evidence.

### Planned work

Define exact analysis tasks.

Define labeled datasets where appropriate.

Separate rules-based logic from learned models.

Version model and decision-logic releases.

Record confidence and provenance.

Build evaluation scripts.

Define threshold-tuning procedures.

Report false-positive and false-negative behavior.

Maintain human-review paths.

Document failure modes and edge cases.

### Expected benefit

Creates credible AI performance claims tied to specific versions and datasets.

## Priority 10 — Strengthen cybersecurity implementation

### Goal

Verify that the actual implementation matches the documented security principles.

### Planned work

Remove secrets from public repositories and artifacts.

Define credential provisioning and rotation.

Verify update authenticity.

Protect deployment configuration.

Improve audit/event logging.

Define least-privilege backend access.

Test recovery after credential failure.

Review exposed network services.

Perform implementation-level security review before large-scale deployment.

### Expected benefit

Reduces the risk that monitoring infrastructure itself becomes a security weakness.

## Priority 11 — Standardize the Expansion System

### Goal

Create a stable module interface for BITs, Aqua Base, Drone Mount, and future extensions.

### Planned work

Freeze mechanical attachment references.

Define allowed power ranges.

Define connector/pinout standards where applicable.

Define module identity metadata.

Define compatibility/version negotiation.

Define module health reporting.

Define commissioning steps.

Publish module-interface drawings and schemas.

### Expected benefit

Allows new modules to be created without redesigning ORIGIN Core.

## Priority 12 — Improve BITs serviceability and educational tooling

### Goal

Make BITs easier to access, program, replace, and demonstrate.

### Planned work

Refine the side-accessible attachment.

Standardize fasteners and alignment features.

Improve cable or electrical interface protection.

Document MakeCode workflows.

Create example educational activities.

Define safe sandbox behavior so BITs experimentation does not compromise the Core system.

### Expected benefit

Improves educational use while preserving product serviceability.

## Priority 13 — Mature Aqua Base

### Goal

Turn Aqua Base from a module concept into an evidence-backed deployment option.

### Planned work

Define intended water-adjacent operating environments.

Validate materials against corrosion and moisture.

Define anchoring or support strategy.

Test sealing and cable routing.

Validate sensors in the intended environment.

Define maintenance intervals based on observed fouling/corrosion.

Document safe retrieval and service procedures.

### Expected benefit

Expands ORIGIN to additional conservation contexts without overgeneralizing the Core enclosure.

## Priority 14 — Mature Drone Mount

### Goal

Create a clearly bounded aerial integration path.

### Planned work

Define compatible payload classes.

Validate mounting security.

Characterize center-of-gravity effects.

Characterize vibration transfer.

Evaluate electromagnetic interference.

Define emergency release/removal procedures.

Document platform-specific flight validation.

Keep regulatory responsibility explicit.

### Expected benefit

Makes drone integration safer and more reproducible.

## Priority 15 — Automate configuration and commissioning

### Goal

Reduce manual setup errors when deploying multiple units.

### Planned work

Create a configuration generator.

Validate configuration before flashing/applying it.

Generate deployment IDs automatically.

Produce unit-specific commissioning records.

Detect incompatible hardware/software combinations.

Export human-readable configuration summaries.

Explore MATLAB or other engineering-tool integration where it provides real value.

### Expected benefit

Makes multi-unit deployment faster and less error-prone.

## Priority 16 — Improve maintenance analytics

### Goal

Use service history to improve the product rather than only repair individual failures.

### Planned work

Record failure categories consistently.

Record replaced parts and causes.

Track recurring connector, sealing, sensor, and power issues.

Compare failure patterns by deployment environment.

Identify parts that should become field-replaceable.

Feed recurring faults into design revisions.

### Expected benefit

Turns maintenance records into engineering evidence.

## Priority 17 — Complete the Durrës pilot evidence loop

### Goal

Use the five-unit pilot to validate the real deployment workflow.

### Planned work

Capture site assessments.

Record exact unit configurations.

Perform standardized calibration.

Record commissioning results.

Collect uptime and fault observations.

Collect operator feedback.

Record maintenance interventions.

Compare unit behavior across locations.

Convert findings into documented design changes.

### Expected benefit

Provides the first structured multi-unit field evidence for ORIGIN.

## Priority 18 — Improve open-source release quality

### Goal

Make the public project easier for external contributors and reviewers to reproduce.

### Planned work

Finalize licensing.

Publish contribution guidelines.

Publish hardware source releases.

Publish software source releases.

Publish CAD exports.

Publish BOMs and manufacturing files.

Publish non-sensitive test data where appropriate.

Add issue templates and contribution workflow.

Keep GitBook synchronized with the authoritative repository.

### Expected benefit

Transforms the documentation from a project showcase into a usable engineering resource.

## Priority 19 — Create compatibility and migration tooling

### Goal

Reduce confusion as ORIGIN revisions multiply.

### Planned work

Maintain a hardware/software compatibility matrix.

Define migration notes for breaking changes.

Identify which deployed units require updates.

Preserve historical documentation for older units.

Provide clear deprecation notices.

### Expected benefit

Makes long-term maintenance possible without freezing innovation.

## Priority 20 — Build stronger automated validation

### Goal

Catch regressions earlier.

### Planned work

Automate firmware build checks.

Validate configuration schemas.

Run static documentation link checks.

Verify manufacturing package completeness.

Add software unit/integration tests where appropriate.

Generate repeatable test reports.

Track validation evidence by release.

### Expected benefit

Reduces the chance of releasing incomplete or incompatible artifacts.

## Improvement selection rule

Planned improvements should be promoted into active development based on field risk; release blockers; impact on reproducibility; impact on reliability; value to deployment partners; test evidence; maintenance burden; compatibility impact; and engineering effort.

A planned improvement becomes a supported feature only after implementation, documentation, and the appropriate validation are complete.
