# Open Source

ORIGIN is being documented in public so that its engineering decisions can be inspected, reproduced, challenged, and improved. This chapter explains what is currently available, how the public repository is organized, how contributors should work with it, and what remains to be released before the project can be described as a complete open-source hardware and software platform.

> **Current status:** the documentation repository is public, but the project should not yet be treated as fully open-source in the formal licensing sense. No repository-wide `LICENSE` file is currently present. Reuse rights must therefore not be assumed until Team Galene publishes an explicit license or set of licenses.

## Why ORIGIN is being developed openly

Cultural-heritage technology benefits from transparency. A monitoring system intended for archaeological and museum environments should be understandable by the people who deploy, maintain, evaluate, and improve it.

The open-development goals for ORIGIN are to:

- make engineering decisions inspectable;
- make limitations and known issues visible rather than hidden;
- allow schools, researchers, makers, museums, and heritage organizations to learn from the project;
- make future replication possible when the necessary design sources are released;
- support peer review of electronics, mechanics, software, testing, and deployment practices;
- preserve project knowledge beyond a single competition season;
- create a traceable development history for future ORIGIN revisions.

Open development does **not** mean publishing every internal detail immediately. Security credentials, private deployment information, personal data, unannounced partner information, and material that could weaken a real deployment should remain outside the public repository.

## Current public repository

The documentation is maintained in:

`CristosMpi/origin-docs`

The repository is currently used as the source for the ORIGIN technical documentation and GitBook structure. It contains the major project chapters for ORIGIN Core, Rosetta, Software, Centaurus AI, Modules, Mechanical Design, Installation & Deployment, Testing & Validation, Deployments, Maintenance, Development, Open Source, Partners & Sponsors, and Resources.

The repository currently contains documentation rather than a complete hardware/software release bundle. In particular, a public documentation page describing a schematic or firmware subsystem is not the same thing as publishing the authoritative source files for that subsystem.

## What counts as an open release

For ORIGIN, a subsystem should only be called openly released when the files needed to understand, modify, and reproduce it are actually available under a clear license.

Depending on the subsystem, that can include:

| Area | Expected release material |
|---|---|
| Documentation | Markdown source, diagrams, references, change history |
| Electronics | Editable schematic source, PCB source, fabrication outputs, BOM, assembly data |
| Mechanical | Native CAD or maintainable source model, STEP exports, drawings, manufacturing notes |
| Firmware | Source code, build instructions, dependency/version information, configuration examples |
| Centaurus AI | Source or reproducible implementation description, model/configuration metadata where appropriate, evaluation methodology |
| Modules | Mechanical/electrical interface definitions, source files, compatibility information |
| Testing | Procedures, acceptance criteria, datasets or result summaries where safe to publish |

A rendered PDF, screenshot, STL, Gerber, or binary can be useful, but by itself it is not always sufficient for meaningful modification.

## Publication maturity

ORIGIN uses the following practical publication states.

### Documented

The subsystem is explained publicly, but the underlying source files may not yet be released.

### Source available

The editable design or code source is public, but reproduction instructions or validation evidence may still be incomplete.

### Reproducible

Another competent builder should have enough information to reproduce the subsystem without relying on undocumented private knowledge.

### Validated release

The published source, manufacturing outputs, instructions, and validation evidence correspond to the same identified revision.

The goal is to move important ORIGIN subsystems toward **validated release**, not merely to upload isolated files.

## What should not be published

Public engineering does not remove the need for responsible information handling. Do not commit:

- passwords, API keys, tokens, Wi-Fi credentials, SIM credentials, private certificates, or secrets;
- private museum or archaeological-site security details;
- exact information that would unnecessarily expose a deployed unit to tampering;
- personal data from visitors, operators, students, or partners;
- private contact information without permission;
- copyrighted third-party files that Team Galene is not permitted to redistribute;
- sponsor discount codes, shipping details, invoices, or private commercial terms;
- unannounced agreements or confidential partner material.

Use sanitized examples for configuration and deployment documentation.

## Documentation as engineering infrastructure

The documentation repository is not intended to be a marketing archive. It is part of the engineering system.

When a hardware revision changes, the corresponding Rosetta, Mechanical Design, Testing, Development, and Maintenance documentation should change with it. When a known issue is discovered, it should be recorded. When a deployment reveals a new failure mode, the finding should become a lesson, requirement, test, or design change.

This relationship is important:

`source change → documentation change → validation change → release record`

A public repository is useful only when it reflects the actual state of the project.

## Repository responsibilities

The ORIGIN documentation repository should maintain:

- stable chapter structure;
- clear revision terminology;
- traceable known issues;
- conservative technical claims;
- explicit status labels for planned versus implemented features;
- working internal navigation;
- links to authoritative source repositories when those are released;
- a clearly stated license once licensing is selected.

## Contribution philosophy

Contributions should improve one or more of the following:

- correctness;
- reproducibility;
- safety;
- maintainability;
- clarity;
- test coverage;
- deployment quality;
- accessibility;
- heritage-site suitability.

Changes that make the project look more complete while reducing technical accuracy should not be accepted.

## Open-source roadmap

The major steps toward a mature public ORIGIN release are:

1. maintain publication-quality technical documentation;
2. choose and publish explicit licenses;
3. publish authoritative source files by subsystem;
4. connect released hardware, software, CAD, and documentation to compatible version identifiers;
5. publish reproducible build and manufacturing instructions;
6. publish validated release packages rather than disconnected exports;
7. establish issue and contribution workflows;
8. preserve a security boundary between public engineering information and deployment-sensitive material.

## In this chapter

- [Repository](repository.md) — repository purpose, organization, source-of-truth rules, and release structure.
- [Development Setup](development-setup.md) — how to work with the documentation and future engineering repositories.
- [Contributing](contributing.md) — contribution standards, review expectations, and change discipline.
- [Licensing](licensing.md) — current licensing status and the requirements for a formal open-source release.

## Principle

ORIGIN should be open in a way that makes the engineering **more trustworthy**, not merely more visible.
