# Changelog

This changelog records material changes to ORIGIN that affect architecture, compatibility, manufacturing, deployment, validation, or public documentation.

It is not intended to capture every small wording correction. Changes should be added when they alter what builders, maintainers, operators, or evaluators need to know.

## Unreleased

### Documentation

Expanded the public ORIGIN documentation into a complete engineering structure covering Overview, ORIGIN Core, Rosetta, Software, Centaurus AI, Modules, Mechanical Design, Installation & Deployment, Testing & Validation, Deployments, Maintenance, and Development.

Added explicit separation between implemented, planned, conceptual, and not-yet-validated capabilities.

Added public validation-status language to prevent component datasheet values from being misrepresented as ORIGIN system-level results.

Added deployment, commissioning, maintenance, diagnostics, and service procedures.

Added versioning, roadmap, known-issues, and planned-improvements records.

### Team documentation

Updated the current ORIGIN development-team list to reflect the active documented team composition.

### Rosetta v2

Documented Rosetta v2 as the current custom electronics baseline.

Added architecture, interfaces, power-management, sensor, PCB-design, BOM, manufacturing, assembly/bring-up, and troubleshooting documentation.

Inspected the available Gerber export and documented its manufacturing metadata.

Recorded that the inspected Gerber package does not include the required drill data and therefore should not be treated as a complete fabrication package.

### Mechanical system

Documented the current tall/faceted enclosure direction.

Documented packaging around Rosetta v2.

Documented support for three mmWave presence-sensing modules.

Documented side-accessible BITs integration rather than a bottom-mounted interface that could interfere with soil-mounted configurations.

Documented the solar support concept with a third hollow support for cable routing.

Recorded the 250 × 250 × 250 mm maximum single-part manufacturing constraint used by the current design process.

Added sealing, material-selection, CAD-release, and mechanical-manufacturing guidance.

### Software

Added embedded software architecture and lifecycle documentation.

Defined configuration, communications, data pipeline, offline buffering, health-state, update, and rollback concepts.

Explicitly avoided publishing invented endpoints, credentials, schemas, or framework-specific commands before the authoritative software source is available.

### Centaurus AI

Added architecture, detection and analysis, decision logic, data processing, cybersecurity, and limitations documentation.

Added confidence, provenance, false-positive/false-negative, human-review, and evaluation requirements.

Defined Centaurus as decision support rather than an unquestionable autonomous authority.

### Modules

Added full documentation for BITs, Aqua Base, Drone Mount, and the Expansion System.

Added module-interface expectations covering mechanical, electrical, data, identity, health, and compatibility concerns.

### Installation and deployment

Added site-assessment guidance for heritage environments.

Added installation, setup, calibration, commissioning, and deployment-checklist procedures.

Added rollback and reversible-installation principles.

### Testing and validation

Added Galene Lab Standards.

Added electronics, sensor, mechanical, environmental, and field-testing procedures.

Added a validation-results register that distinguishes validated, observed, conditional, identified-issue, and not-yet-validated states.

### Deployments

Documented the planned five-unit Durrës pilot with the Archaeological Museum of Durrës.

Explicitly separated planned pilot scope from completed operational results.

Added deployment architecture, findings, lessons-learned, and future-deployment frameworks.

### Maintenance

Added routine maintenance, inspection, diagnostics, component replacement, and troubleshooting procedures.

Added service-state and recommissioning concepts.

## 2026 development milestones

### Rosetta v2 electronics redesign

Continued custom PCB development around the Rosetta v2 architecture.

Evaluated manufacturing workflows using KiCad and EasyEDA Pro.

Worked through footprint, library, routing, edge-cut, fabrication-output, and assembly-data issues.

Identified the absence of drill data in one manufacturing submission/export as a release blocker.

### mmWave sensing direction

Explored alternative 360° sensing geometries before converging toward a design using discrete DFRobot C4001/SEN0609-class mmWave modules.

Integrated the sensor mounting problem into the enclosure architecture rather than treating sensing as an external accessory.

### Enclosure development

Explored multiple enclosure concepts, including Twin Spire and Diagrid directions.

Refined the preferred direction toward a taller, more architectural and product-ready enclosure.

Added sensor openings, fastening considerations, BITs access, and solar-support cable routing to the mechanical requirements.

### Field deployment preparation

Defined the Durrës pilot as the first major structured deployment context.

Began aligning documentation, commissioning, testing, maintenance, and deployment records around a multi-unit field rollout.

## 2025–2026 project evolution

ORIGIN evolved from a competition-driven cultural-heritage concept into a broader modular monitoring platform with custom electronics, embedded software, AI-assisted analysis, multiple extension modules, field-deployment procedures, and open engineering documentation.

During this period the project also expanded its focus from demonstrating functionality to documenting manufacturability, maintainability, validation evidence, deployment constraints, and failure modes.

## Changelog policy

A future changelog entry should include date or release identifier; affected subsystem; concise description of the change; compatibility impact; validation impact; and migration or recommissioning requirement if applicable.

When a known issue is resolved, the changelog should record the fix and the [Known Issues](known-issues.md) page should be updated at the same time.
