# Known Issues

This page records unresolved ORIGIN limitations, blockers, and incomplete evidence that may affect manufacturing, validation, deployment, maintenance, or public claims.

The existence of a known issue does not automatically make the entire system unusable. It identifies an area where the current state must be understood before relying on a specific capability.

## Status labels

Each issue should be treated as one of the following:

- **Blocker** — prevents release, fabrication, deployment, or a required validation step.
- **High** — can materially affect reliability, safety, data quality, or maintainability.
- **Medium** — important limitation or incomplete work with a practical workaround.
- **Low** — minor limitation, cleanup item, or documentation gap.
- **Evidence gap** — a claim cannot yet be made because sufficient test evidence is missing.

## KI-001 — Incomplete Rosetta v2 fabrication export

**Status:** Blocker  
**Subsystem:** Rosetta / Manufacturing

The inspected Rosetta v2 Gerber ZIP does not contain the required drill file data.

### Impact

The package should not be treated as a complete fabrication release. A board house requires drill information for plated and/or non-plated holes, mounting holes, and vias as defined by the design.

### Required action

- regenerate fabrication outputs from the authoritative current PCB source;
- include the relevant Excellon drill files;
- confirm the board outline and drill locations;
- verify the package before resubmission;
- archive the verified output with a clear revision identifier.

### Resolution evidence

A regenerated release package that passes a fabrication-output review and matches the source PCB.

## KI-002 — Rosetta source/export traceability is not yet fully public

**Status:** High  
**Subsystem:** Rosetta / Documentation

The public documentation describes Rosetta v2, but the full authoritative schematic, PCB source, BOM, and manufacturing-release set are not yet established as one clearly versioned public package.

### Impact

External builders cannot yet reproduce the hardware with the confidence expected from a mature open hardware release.

### Required action

Publish or link the authoritative source set and assign explicit revision identifiers.

## KI-003 — Rosetta BOM remains incomplete as a release artifact

**Status:** High  
**Subsystem:** Rosetta / Manufacturing

Known major components are documented, but the public BOM is not yet a complete, revision-controlled manufacturing BOM covering every fitted component, quantity, package, manufacturer part number, substitution policy, and assembly status.

### Impact

Automated assembly and independent reproduction remain error-prone.

### Required action

Generate the BOM from the authoritative schematic/PCB source and verify it against the manufactured design.

## KI-004 — Final enclosure revision is still evolving

**Status:** Medium  
**Subsystem:** Mechanical Design

The current documentation reflects the preferred tall, faceted enclosure direction, but the final production geometry, fastener strategy, access panels, sealing details, and exact dimensions are still subject to refinement.

### Impact

Mechanical drawings should not yet be interpreted as a frozen production design unless a specific released CAD revision says otherwise.

### Required action

Freeze a candidate CAD revision, perform fit/assembly/environmental testing, then release the corresponding STEP/STL/drawing package.

## KI-005 — No validated IP rating

**Status:** Evidence gap  
**Subsystem:** Mechanical / Environmental

ORIGIN includes environmental-protection design measures, but no formal IP rating is currently documented as validated for the integrated enclosure.

### Impact

The system must not be publicly described as IP-rated or waterproof without the required test evidence.

### Required action

Define the intended ingress-protection target, test the final enclosure revision accordingly, and record the test method and result.

## KI-006 — Sensor openings complicate environmental sealing

**Status:** High  
**Subsystem:** Mechanical / Sensors

The current enclosure direction prioritizes functional openings or sensor windows for the mmWave modules. These penetrations create sealing and condensation design challenges.

### Impact

Environmental protection and sensor performance must be validated together rather than optimized independently.

### Required action

Test sensor-window materials, sealing geometry, drainage, condensation behavior, and radar performance on the final assembly.

## KI-007 — ORIGIN-level mmWave range is not validated

**Status:** Evidence gap  
**Subsystem:** Sensors

Manufacturer specifications for the DFRobot C4001/SEN0609-class modules do not establish the actual detection range of ORIGIN when the sensors are mounted inside the final enclosure and deployed at a real site.

### Impact

Component-level range figures must not be quoted as guaranteed ORIGIN system performance.

### Required action

Run controlled coverage, range, angle, static-presence, moving-presence, and false-trigger tests using the final sensor mounting arrangement.

## KI-008 — Three-sensor coverage and blind zones require characterization

**Status:** Medium / Evidence gap  
**Subsystem:** Sensors / Mechanical

The current architecture uses three mmWave sensors, but the exact combined coverage pattern depends on enclosure geometry, orientation, site structure, reflections, and installation height.

### Impact

Claims of 360° or complete surrounding coverage are not yet justified.

### Required action

Map real coverage and blind regions during calibration and field testing.

## KI-009 — Environmental sensor configuration is not fully frozen

**Status:** Medium  
**Subsystem:** Sensors

The environmental-monitoring role is part of ORIGIN, but the final public sensor set, exact models, mounting arrangements, sampling behavior, and calibration requirements are not fully frozen across all deployments.

### Impact

Documentation must remain architecture-level until exact hardware is released.

## KI-010 — Battery life is not yet validated

**Status:** Evidence gap  
**Subsystem:** Power

No validated integrated-system battery runtime is currently published.

### Impact

Battery-life figures should not be inferred from cell capacity alone.

### Required action

Measure power consumption across representative operating states and validate runtime under defined deployment conditions.

## KI-011 — Solar autonomy is not yet validated

**Status:** Evidence gap  
**Subsystem:** Power / Mechanical

The mechanical documentation includes solar-panel support and cable routing, but the complete energy balance depends on panel selection, orientation, battery configuration, firmware behavior, local weather, shading, and load profile.

### Impact

The system should not yet be described as indefinitely solar-powered or energy autonomous.

## KI-012 — Final solar-panel mechanical design is not frozen

**Status:** Medium  
**Subsystem:** Mechanical / Power

The current design requirement includes a third support that also carries the cable internally, but the final support geometry, panel dimensions, fasteners, cable strain relief, and wind-loading validation are still subject to final CAD and testing.

## KI-013 — Firmware source/build environment is not yet fully documented as a reproducible public release

**Status:** High  
**Subsystem:** Software

The public software chapter defines the intended architecture and lifecycle, but exact framework versions, dependency lockfiles, build commands, supported board target, binary releases, and source revision mapping are not yet published as a complete reproducible release.

### Impact

External maintainers cannot yet rebuild an exact deployed firmware image from the documentation alone.

## KI-014 — Communications implementation details are not yet frozen

**Status:** Medium  
**Subsystem:** Software / Connectivity

The architecture defines resilient communications behavior, buffering, provenance, and recovery principles, but exact transport protocols, message schemas, endpoints, retry timing, and backend interfaces should follow the authoritative implementation.

### Impact

The documentation intentionally avoids inventing protocol details.

## KI-015 — Offline buffering limits are not yet validated

**Status:** Evidence gap  
**Subsystem:** Software / Storage

The software architecture requires graceful operation during connectivity loss, but the public documentation does not yet define a validated maximum outage duration or storage capacity for all configurations.

## KI-016 — Centaurus AI implementation/evaluation package is not yet public and frozen

**Status:** High  
**Subsystem:** Centaurus AI

Centaurus is documented as an intelligence and decision-support layer, but the exact deployed model/logic versions, training/evaluation data, thresholds, evaluation scripts, and performance records are not yet established as a public reproducible release.

### Impact

The architecture should not be interpreted as proof of deployed AI accuracy.

## KI-017 — No validated Centaurus accuracy claim

**Status:** Evidence gap  
**Subsystem:** Centaurus AI

No general accuracy, precision, recall, false-alarm rate, or other universal model-performance figure is currently validated in the public documentation.

### Required action

Define the specific task, labeled dataset, evaluation protocol, version, and deployment context before publishing a quantitative result.

## KI-018 — Cybersecurity controls require implementation-level verification

**Status:** High  
**Subsystem:** Security

The documentation defines security principles including authenticated updates, protected credentials, provenance, and defensive boundaries, but each control must be verified against the actual deployed software and infrastructure.

### Impact

Architecture-level security intentions are not equivalent to a security audit.

## KI-019 — Module electrical interfaces are not yet frozen for all extensions

**Status:** Medium  
**Subsystem:** Modules

BITs, Aqua Base, Drone Mount, and future modules are documented around an expansion-system concept, but exact connector, pinout, voltage, power-budget, communications, and identity details remain implementation-specific until formal interface revisions are released.

## KI-020 — Aqua Base environmental limits require validation

**Status:** Evidence gap  
**Subsystem:** Modules / Aqua Base

The Aqua Base concept extends ORIGIN into water-adjacent or water-related environments, but stability, sealing, corrosion, materials, buoyancy/anchoring, cable management, and sensor behavior must be validated for each intended operating condition.

## KI-021 — Drone Mount flight integration requires platform-specific validation

**Status:** High  
**Subsystem:** Modules / Drone Mount

Payload mass, center of gravity, vibration, electromagnetic interaction, mounting security, flight time, regulations, and emergency procedures depend on the specific aircraft and payload configuration.

### Impact

The Drone Mount documentation is not a universal authorization to fly ORIGIN hardware on any drone.

## KI-022 — Durrës pilot is planned, not yet an operational results dataset

**Status:** Medium  
**Subsystem:** Deployments

The five-unit Durrës pilot is documented as the intended first structured heritage-site deployment context. Public documentation should not imply that all five units are already commissioned or that long-term results already exist unless those milestones are actually completed and recorded.

## KI-023 — Field reliability metrics are not yet established

**Status:** Evidence gap  
**Subsystem:** Deployment / Maintenance

Metrics such as uptime, mean time between failures, service interval, communications availability, and maintenance burden require real multi-unit operating history.

## KI-024 — Fixed maintenance intervals are not yet evidence-backed

**Status:** Evidence gap  
**Subsystem:** Maintenance

The maintenance chapter therefore uses condition-based and deployment-dependent servicing rather than inventing universal fixed intervals.

## KI-025 — Final fastener quantities and lengths depend on the frozen mechanical revision

**Status:** Medium  
**Subsystem:** Mechanical

M3 fasteners are part of the current mechanical design workflow, but the final quantity and exact lengths for the complete product cannot be considered fixed until the enclosure, sensor brackets, solar supports, module attachment, and service panels are frozen.

## KI-026 — Public open-source licensing package is not yet finalized

**Status:** Medium  
**Subsystem:** Open Source

The documentation includes a licensing section in the site structure, but the final license selection and the distinction between hardware, software, documentation, third-party assets, and partner materials must be explicit before claiming a complete open-source release.

## Issue resolution process

When an issue is resolved:

1. capture the evidence or source revision that resolves it;
2. update the affected technical documentation;
3. update validation results where appropriate;
4. update the changelog;
5. mark the known issue as resolved or move it into a historical resolved-issues section;
6. determine whether existing deployed units require migration, repair, or recommissioning.

## Public-claims rule

Where a known issue is an evidence gap, the correct documentation behavior is to state that the capability has not yet been validated—not to estimate or infer a result.
