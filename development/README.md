# Development

ORIGIN is an active engineering project. Its development process is organized around controlled iteration: define a problem, design a change, prototype it, test it, document the evidence, and only then promote it into the current system.

This chapter records that lifecycle. It is intended to make the project understandable not only as a finished concept, but as an evolving technical system with explicit versions, open issues, planned improvements, and documented engineering decisions.

## Development model

ORIGIN does not treat every prototype as a release. Work moves through a sequence of maturity states:

1. **Concept** — an idea or requirement exists, but no implementation is considered stable.
2. **Prototype** — a first physical or software implementation exists and is suitable for experimentation.
3. **Integrated** — the feature has been connected to the wider ORIGIN architecture.
4. **Validated** — the relevant test procedure has produced sufficient evidence for the stated claim.
5. **Deployment candidate** — the feature is suitable for controlled field use, subject to the deployment checklist.
6. **Operational** — the feature has been commissioned for a specific deployment and is being maintained under an accepted configuration.
7. **Deprecated** — the feature or design is retained for historical compatibility but is no longer preferred for new builds.

These states are intentionally separate. A component can be mechanically integrated without being environmentally validated, and a software function can be implemented without being proven reliable enough for field use.

## Current development baseline

The documentation currently uses **ORIGIN 2026** as the project-level baseline. Within that baseline, the current custom electronics platform is **Rosetta v2**.

The project-level version and subsystem versions are related but not identical. For example, Rosetta can receive a hardware revision without implying that every mechanical, software, AI, or deployment subsystem has changed at the same time.

The main development areas are:

- ORIGIN Core architecture;
- Rosetta electronics;
- embedded firmware;
- Centaurus AI and data processing;
- mechanical enclosure and mounting;
- sensing and presence detection;
- solar and power integration;
- BITs, Aqua Base, and Drone Mount extensions;
- deployment and maintenance procedures;
- testing and validation methods;
- documentation and open-source release quality.

## Change control

A development change should identify at least:

- what is changing;
- why the change is needed;
- which subsystem owns the change;
- which interfaces are affected;
- what previous behavior may be invalidated;
- how the change will be tested;
- whether documentation must be updated;
- whether deployed units require migration or recommissioning.

Changes that affect physical fit, wiring, power, communications, calibration, data interpretation, or safety should never be treated as isolated cosmetic changes.

## Compatibility first

ORIGIN is modular, so development depends heavily on interface stability.

A new revision should preserve compatibility where practical, but compatibility must never be claimed without checking the relevant mechanical, electrical, communications, software, and data interfaces.

Where compatibility cannot be preserved, the change should be documented as a breaking change and accompanied by a migration path where practical.

## Evidence before claims

Development status is not determined by how complete a design looks. A result becomes part of the supported system only when evidence exists for the claim being made.

Examples:

- a CAD enclosure render is not evidence of environmental resistance;
- a sensor datasheet is not evidence of ORIGIN system-level detection range;
- a successful boot is not evidence of long-term firmware reliability;
- an AI output that appears reasonable is not evidence of accuracy;
- an assembled PCB is not proof that the complete manufacturing package is release-ready.

This principle is reflected throughout [Testing & Validation](../testing-validation/README.md).

## Development records

This chapter is divided into five records.

### [Roadmap](roadmap.md)

Defines the major development tracks and the order in which ORIGIN should mature.

### [Versions](versions.md)

Explains project and subsystem versioning, compatibility, and release-state terminology.

### [Changelog](changelog.md)

Records material changes that affect users, builders, maintainers, or deployment behavior.

### [Known Issues](known-issues.md)

Maintains an explicit register of unresolved limitations, defects, risks, and incomplete release artifacts.

### [Planned Improvements](planned-improvements.md)

Lists prioritized technical improvements without presenting them as already implemented.

## What belongs in the roadmap

The roadmap should contain work that changes capability, reliability, maintainability, manufacturability, evidence quality, or deployment readiness.

Small wording corrections and routine documentation maintenance do not need to be roadmap items unless they materially affect safe use or reproducibility.

## What belongs in known issues

A known issue is broader than a software bug. It can include:

- incomplete manufacturing files;
- unresolved mechanical interference;
- environmental sealing weaknesses;
- unvalidated performance claims;
- missing test evidence;
- version incompatibilities;
- deployment-specific limitations;
- unclear service procedures;
- data-quality risks;
- security or privacy concerns that still require mitigation.

The known-issues register should be updated when an issue is discovered, materially changes, gains a workaround, or is resolved.

## Release discipline

Before a subsystem is described as a release candidate, the team should confirm that:

- its source files are identifiable;
- its revision is recorded;
- its interfaces are documented;
- required manufacturing or build files are present;
- known blockers are recorded;
- relevant validation has been completed;
- recovery or rollback is possible where applicable;
- documentation matches the implementation.

Before deployment, the additional requirements in [Installation & Deployment](../installation-deployment/README.md) apply.

## Documentation as part of development

Documentation is treated as an engineering artifact. A change is not complete if the hardware, software, calibration, maintenance, or deployment behavior has changed but the documentation still describes the previous state.

Where exact values are not yet confirmed, the documentation should say so rather than fill the gap with an assumed value.

## Project history and active development

ORIGIN has evolved through multiple mechanical concepts, sensor arrangements, PCB iterations, manufacturing attempts, software concepts, and module designs. Earlier work remains useful because it captures decisions and failure modes, but historical prototypes should not automatically be interpreted as current architecture.

The active baseline should always be determined from the version records, current CAD/electronics sources, current software sources, and the latest validated deployment configuration.

## Development priorities

The project currently prioritizes:

- completing reproducible Rosetta v2 manufacturing outputs;
- improving enclosure maturity and field serviceability;
- validating sensing behavior at system level;
- strengthening power and communications reliability;
- turning Centaurus concepts into measurable, testable capabilities;
- preparing repeatable deployment procedures;
- collecting controlled pilot evidence;
- maintaining honest public documentation as the project changes.

These priorities are expanded in the [Roadmap](roadmap.md) and [Planned Improvements](planned-improvements.md).

## Engineering principle

The development objective is not to make ORIGIN appear finished. It is to make each revision more reproducible, testable, maintainable, and useful in real heritage environments.
