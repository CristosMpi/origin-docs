# Deployments

The **Deployments** chapter documents how Project ORIGIN moves from laboratory development into real heritage-site use.

A deployment is not treated as simply placing hardware at a site. It is a controlled engineering process that combines site assessment, installation, configuration, validation, operation, observation, maintenance, and documented review.

The purpose of this chapter is to preserve that operational context. A result obtained on a workbench cannot automatically be assumed to hold at an archaeological site, museum, monument, outdoor excavation, or other cultural-heritage environment. Every site changes the system through its geometry, materials, climate, radio environment, visitor activity, mounting constraints, and operational rules.

## Deployment philosophy

ORIGIN deployments follow five principles:

1. **Protect the heritage asset first.** Monitoring equipment must never introduce greater physical, visual, environmental, or operational risk than the problem it is intended to address.
2. **Use reversible installation methods wherever possible.** Permanent alteration of historic fabric should be avoided unless explicitly approved by the responsible authority.
3. **Validate in context.** Sensor performance, connectivity, power behavior, enclosure performance, and event logic must be checked after the unit is installed in its real position.
4. **Document the exact configuration.** Hardware revision, firmware, software, calibration, module configuration, mounting geometry, and site conditions must be traceable.
5. **Separate observations from conclusions.** Field observations become validated project claims only when supported by sufficient evidence.

## Deployment lifecycle

A complete ORIGIN deployment is divided into several stages:

```text
Site selection
    ↓
Site assessment
    ↓
Deployment design
    ↓
Pre-deployment verification
    ↓
Physical installation
    ↓
Setup and calibration
    ↓
Commissioning
    ↓
Operational observation
    ↓
Maintenance and review
    ↓
Findings and lessons learned
```

The detailed installation workflow is documented separately under [Installation & Deployment](../installation-deployment/README.md).

This chapter focuses on the higher-level deployment record: why a site was selected, how the ORIGIN system was arranged, what was learned, and what should change before the next deployment.

## Current deployment program

The principal deployment documented for ORIGIN 2026 is the planned **Durrës Pilot** in Albania.

The project plan includes the donation of **five ORIGIN units** to the **Archaeological Museum of Durrës** as a real-world cultural-heritage pilot.

The pilot is intended to move ORIGIN beyond demonstration-only use and expose the system to the practical realities of installation, commissioning, site geometry, long-term monitoring, maintenance, and cooperation with heritage professionals.

See [Durrës Pilot](durres-pilot.md).

## What a deployment record contains

Each deployment should maintain, at minimum:

| Record | Purpose |
| --- | --- |
| Site identifier | Unambiguous reference to the deployment location |
| Responsible organization | Identifies the authority or partner responsible for the site |
| ORIGIN unit IDs | Identifies the exact deployed hardware |
| Hardware revision | Links field behavior to a physical design version |
| Firmware/software versions | Makes the deployment reproducible |
| Module configuration | Records which optional ORIGIN modules are installed |
| Installation date | Establishes the operational timeline |
| Mounting geometry | Documents height, orientation, direction, and attachment method |
| Sensor configuration | Records enabled sensors and site-specific settings |
| Power architecture | Defines solar, battery, external power, or mixed configuration |
| Communications architecture | Defines how the unit reaches higher-level services |
| Calibration record | Preserves site-specific baselines and thresholds |
| Commissioning result | Shows whether the system met its deployment acceptance criteria |
| Maintenance history | Records interventions after installation |
| Findings | Captures observed field behavior |

Sensitive site-security information should not be published in public documentation when doing so would increase risk to the protected asset.

## Deployment architecture

A single ORIGIN deployment can contain one or more ORIGIN Core units and may use different combinations of modules depending on the site.

Conceptually:

```text
Heritage site
    │
    ├── ORIGIN Core A
    │      ├── Rosetta v2
    │      ├── local sensors
    │      └── optional modules
    │
    ├── ORIGIN Core B
    │      └── ...
    │
    └── ORIGIN Core N
           ↓
     communications path
           ↓
     ORIGIN software / Centaurus AI
           ↓
      operator review
```

A deployment is therefore a **system-of-systems configuration**, not merely a collection of identical devices.

See [Deployment Architecture](deployment-architecture.md).

## Deployment states

For documentation purposes, ORIGIN deployments should use explicit lifecycle states.

| State | Meaning |
| --- | --- |
| Proposed | Candidate site identified but not approved |
| Assessment | Site requirements are being measured and reviewed |
| Planned | Deployment architecture has been defined |
| Installation | Hardware is physically being installed |
| Commissioning | The installed system is undergoing acceptance testing |
| Pilot operation | System is active but still under controlled evaluation |
| Operational | Deployment has passed its defined acceptance criteria |
| Suspended | Deployment remains installed but is intentionally inactive |
| Removed | Equipment has been taken out of service at the site |

A deployment should not be described as operational merely because the hardware powers on.

## Pilot deployments vs production deployments

ORIGIN documentation distinguishes between **pilot** and **production** use.

### Pilot deployment

A pilot is primarily intended to learn.

It may investigate:

- installation methods;
- sensor coverage;
- environmental robustness;
- communications reliability;
- maintenance burden;
- operator workflow;
- false-positive behavior;
- power performance;
- public-space constraints;
- module usefulness.

Changes during a pilot are expected, but must be documented.

### Production deployment

A production deployment should use a validated hardware/software baseline and defined acceptance criteria.

Before ORIGIN is represented as a production monitoring system, the required functionality should have supporting evidence from testing and field operation.

See [Testing & Validation](../testing-validation/README.md).

## Heritage-specific deployment constraints

ORIGIN deployments are unusual because the monitored environment may itself be irreplaceable.

Important constraints can include:

- prohibition on drilling or permanent mounting;
- restrictions on adhesives or contact materials;
- visual-impact requirements;
- limits on cable routing;
- archaeological sensitivity below ground level;
- visitor-access requirements;
- conservation requirements;
- museum operating procedures;
- protected-area permissions;
- restrictions on radio equipment;
- privacy obligations;
- maintenance-access limitations.

The correct deployment method therefore depends on both engineering and conservation considerations.

## Evidence hierarchy

Field documentation should identify the strength of each claim.

### Planned

The feature or procedure is part of the deployment design but has not yet been executed.

### Installed

The physical or software configuration is confirmed to exist at the site.

### Observed

A behavior has been seen during field use but has not necessarily been validated statistically or across multiple conditions.

### Validated

A defined test was performed under documented conditions and met its acceptance criteria.

### Operational result

A result was obtained during sustained deployment rather than a short test session.

This hierarchy prevents a single successful demonstration from becoming an exaggerated public performance claim.

## Deployment findings

Deployment findings should include both successful and unsuccessful outcomes.

Examples include:

- which sensor orientations produced useful coverage;
- where radar reflections caused ambiguity;
- whether mounting remained stable;
- whether solar exposure matched the design assumption;
- whether communications were reliable;
- whether operators understood system states;
- whether maintenance access was practical;
- whether water paths appeared after rain;
- whether thresholds required adjustment;
- whether an optional module added enough value to justify its complexity.

See [Findings](findings.md).

## Lessons learned

Lessons learned are broader engineering conclusions extracted from deployments.

A lesson should ideally include:

1. the original assumption;
2. what happened in practice;
3. the evidence supporting the observation;
4. the resulting design or process change.

See [Lessons Learned](lessons-learned.md).

## Future deployments

Future ORIGIN deployments should build on the same documented process rather than starting from an undocumented configuration each time.

The long-term goal is to develop reusable deployment patterns for different heritage-site classes while retaining enough flexibility for site-specific needs.

See [Future Deployments](future-deployments.md).

## Related documentation

- [Installation & Deployment](../installation-deployment/README.md)
- [Testing & Validation](../testing-validation/README.md)
- [ORIGIN Core](../origin-core/README.md)
- [Mechanical Design](../mechanical-design/README.md)
- [Software](../software/README.md)
- [Centaurus AI](../centaurus-ai/README.md)
