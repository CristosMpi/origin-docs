# Versions

ORIGIN uses versioning to separate project-level releases from the revisions of individual subsystems. This is necessary because the enclosure, Rosetta electronics, firmware, Centaurus AI, modules, and deployment procedures can evolve at different speeds.

## Versioning model

ORIGIN distinguishes four kinds of version information:

- **Project baseline** — the overall documented system generation, such as ORIGIN 2026.
- **Subsystem revision** — the revision of a specific hardware, software, or mechanical subsystem, such as Rosetta v2.
- **Configuration version** — the exact combination of settings, calibration, firmware, modules, and deployment-specific choices used by a unit.
- **Artifact revision** — the revision of a source or export file such as a CAD model, Gerber package, BOM, firmware build, or test procedure.

These identifiers should not be collapsed into a single number.

## Current project baseline

The current documentation baseline is:

**ORIGIN 2026**

This label describes the current generation of the overall project and documentation. It does not mean that every subsystem was created in 2026 or that every component shares one synchronized version number.

## Current electronics baseline

The current custom electronics platform is:

**Rosetta v2**

Rosetta v2 is documented as the current hardware platform for the Core electronics architecture. Its exact manufacturing readiness depends on the current source and release package; the known drill-file issue in an earlier Gerber export remains separately recorded in [Known Issues](known-issues.md).

## Why subsystem versions matter

A system may contain combinations such as:

- ORIGIN 2026 enclosure revision A;
- Rosetta v2 PCB revision B;
- firmware release 0.x;
- Centaurus evaluation build C;
- BITs module revision 2;
- deployment configuration Durrës-Unit-03.

The exact identifiers above are examples of the versioning structure, not current assigned release numbers unless separately recorded in source control.

The purpose is to make it possible to answer questions such as:

- Which hardware revision was tested?
- Which firmware was running when a field event occurred?
- Which enclosure geometry was installed?
- Which calibration values were active?
- Which module revision was attached?
- Which test evidence applies to this configuration?

## Recommended version format

For software and documentation releases, semantic-style versioning can be used where useful:

`MAJOR.MINOR.PATCH`

Where:

- **MAJOR** indicates a breaking compatibility change;
- **MINOR** indicates new backward-compatible functionality;
- **PATCH** indicates fixes or documentation-only corrections that do not intentionally break compatibility.

For physical hardware, revision identifiers are often clearer than semantic versions, for example:

`Rosetta v2 Rev A`

or

`Enclosure Rev B`

The exact scheme should remain stable once public releases begin.

## Breaking changes

A change should be treated as potentially breaking when it changes any of the following:

- PCB connector type or pin assignment;
- voltage or power expectations;
- mounting-hole geometry;
- enclosure clearances;
- sensor orientation or field of view;
- cable routing;
- module mechanical interface;
- data schema;
- configuration schema;
- communications protocol;
- firmware compatibility with hardware;
- calibration interpretation;
- update or recovery process.

Breaking changes should be explicitly documented in the changelog.

## Configuration identity

A deployed unit should be associated with a configuration record containing, where applicable:

- ORIGIN project baseline;
- Rosetta hardware revision;
- enclosure/CAD revision;
- firmware version or commit;
- module list and revisions;
- sensor configuration;
- calibration version;
- configuration schema version;
- Centaurus logic/model version;
- deployment identifier;
- commissioning date;
- relevant maintenance or replacement history.

This allows field observations to be traced back to the exact system that generated them.

## Release states

Version numbers alone do not communicate maturity. Each release should also carry a state.

### Experimental

Suitable for laboratory exploration. Interfaces and behavior may change without migration support.

### Prototype

An integrated implementation exists and can be tested, but should not be assumed deployment-ready.

### Validation candidate

The design is sufficiently stable for formal testing against defined procedures.

### Deployment candidate

Required validation has been completed for the intended controlled deployment context, subject to commissioning.

### Operational

The specific configuration has been commissioned for a deployment and is being maintained under the documented procedures.

### Deprecated

Retained for historical reference or compatibility, but not recommended for new builds.

## Source versus export versions

Editable source files and exported manufacturing or distribution files must remain traceable to one another.

For example:

- a KiCad PCB source should map to a specific Gerber/drill export;
- a CAD assembly should map to the STEP/STL files used for manufacturing;
- a firmware source revision should map to a binary build;
- a test procedure revision should map to the result record that used it.

An export with an unclear source revision should not be treated as a complete release artifact.

## Documentation versioning

Documentation must follow implementation changes.

When a page describes a specific hardware revision, it should identify that revision. When a page is intentionally architectural and version-independent, it should avoid embedding transient values that may become stale.

The main Overview pages follow this rule by describing the system architecture without pretending that every version-specific technical detail is fixed.

## Compatibility matrix

As more public revisions exist, ORIGIN should maintain a compatibility matrix such as:

| Component | Version | Compatible with | Status |
|---|---|---|---|
| ORIGIN Core | 2026 baseline | Rosetta v2 | Current baseline |
| Rosetta | v2 | Current Core architecture | Current electronics baseline |
| Enclosure | current development revision | Rosetta v2 + three mmWave modules | In development |
| Firmware | current development branch | Rosetta v2 | Requires source-controlled release ID |
| Centaurus | current development architecture | ORIGIN data pipeline | Requires validated implementation ID |

The table above reflects the documentation state, not a final production compatibility certification.

## Version retirement

A version can be retired when:

- a replacement has been validated;
- known safety or reliability issues make continued use inappropriate;
- required parts are no longer available;
- maintaining compatibility creates unreasonable technical debt;
- deployment evidence shows that the architecture should be replaced.

Retirement should not erase the previous documentation. Historical records remain important for interpreting older tests and deployed units.

## Versioning rule

If a result cannot be tied to a specific version or configuration, it should not be used as strong evidence for the behavior of a newer or different revision.
