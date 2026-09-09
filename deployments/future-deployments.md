# Future Deployments

Future ORIGIN deployments should build on the evidence gathered from laboratory validation and the Durrës pilot rather than repeating the project from scratch at every site.

The long-term objective is to develop a small number of **repeatable deployment patterns** that can be adapted to different heritage environments while preserving traceability, reversibility, and site-specific validation.

## Deployment maturity path

ORIGIN should move through deployment maturity in stages.

```text
Laboratory validation
    ↓
Single-site pilot
    ↓
Multi-unit pilot
    ↓
Repeated deployment pattern
    ↓
Validated operational baseline
```

Moving to the next stage should depend on evidence, not schedule alone.

## What future deployments must inherit

Every future deployment should inherit a validated baseline for:

- Rosetta hardware revision;
- enclosure revision;
- sensor mounting geometry;
- firmware version;
- communications behavior;
- configuration format;
- module compatibility;
- commissioning procedure;
- maintenance procedure;
- validation requirements.

A future site may change the local configuration, but the underlying baseline should remain identifiable.

## Deployment classes

Different heritage environments may require different standard patterns.

### Indoor museum deployment

Typical characteristics:

- controlled indoor environment;
- reliable fixed power may be available;
- dense visitor activity;
- reflective surfaces and display cases;
- strict visual-impact requirements;
- controlled staff access;
- potentially reliable local networking.

Priorities may include:

- discreet mounting;
- false-positive control;
- operator usability;
- minimal visual intrusion;
- indoor environmental monitoring.

### Outdoor archaeological deployment

Typical characteristics:

- direct weather exposure;
- solar power may be important;
- changing temperature and humidity;
- variable communications coverage;
- larger monitored zones;
- difficult maintenance access;
- stronger environmental-protection requirements.

Priorities may include:

- drainage;
- UV/weather durability;
- power autonomy;
- secure mounting;
- robust communications recovery.

### Monument deployment

Typical constraints can include:

- very limited mounting options;
- strict conservation requirements;
- public visibility;
- limited power infrastructure;
- sensitive aesthetic context.

Reversible mounting and low visual impact become especially important.

### Temporary excavation deployment

Temporary sites may prioritize:

- rapid setup;
- portability;
- temporary power;
- changing site geometry;
- easy relocation;
- short commissioning cycles.

The mechanical system may therefore use a different mounting solution than a long-term museum deployment.

## Deployment templates

After enough evidence has been collected, Team Galene can define versioned templates such as:

```text
ORIGIN-DEPLOY-INDOOR-v1
ORIGIN-DEPLOY-OUTDOOR-v1
ORIGIN-DEPLOY-TEMP-v1
```

A deployment template could define:

- approved hardware revision;
- standard module set;
- mounting guidance;
- sensor orientation starting point;
- power configuration;
- communications options;
- commissioning tests;
- maintenance intervals;
- known limitations.

Templates are starting points, not substitutes for site assessment.

## Criteria for adding a new site

A potential deployment should be considered only when several conditions can be satisfied.

### Heritage suitability

The installation must be acceptable to the site authority and conservation requirements.

### Technical suitability

The site must support a realistic power, mounting, communications, and maintenance plan.

### Operational owner

Someone must be responsible for interpreting alerts, maintaining the system, and reporting issues.

### Validation capacity

The team must be able to commission the system properly rather than simply install it and leave.

### Evidence value

Pilot deployments should ideally answer a useful engineering question rather than only provide visibility.

## Scaling from five units

If the Durrës five-unit model is successful, future multi-unit deployments can use the same principles:

- stable unit IDs;
- zone mapping;
- per-unit health;
- common configuration baseline;
- centralized event correlation;
- consistent commissioning records.

Scaling the number of devices increases operational complexity.

The system must therefore avoid assuming that a fleet is healthy because most units are online. Each device and sensor should remain individually visible.

## Fleet management

As deployments grow, ORIGIN will need stronger fleet-management practices.

These may include:

- unit inventory;
- hardware revision tracking;
- firmware/software version tracking;
- deployment location records;
- module inventory;
- configuration status;
- last contact time;
- health history;
- maintenance history;
- open issues.

This can begin as structured documentation and later evolve into dedicated software tooling.

## Remote maintenance

Future deployments should minimize unnecessary site visits while preserving safe recovery paths.

Potential capabilities include:

- remote health inspection;
- configuration updates;
- software update management;
- log retrieval;
- fault-state diagnosis;
- controlled reboot or recovery.

Remote actions must be authenticated and designed so a failed update does not permanently disable the unit.

See [Software Updates](../software/updates.md).

## Modular expansion

Future sites may use different optional modules.

Possible combinations include:

- BITs for accessible or educational interaction;
- Aqua Base for water-related monitoring contexts;
- Drone Mount for approved aerial inspection workflows;
- future expansion modules that comply with the ORIGIN interface model.

A module should only be included when it has a clear site purpose and has passed the relevant validation.

See [Modules](../modules/README.md).

## Future hardware revisions

Deployment findings may justify new Rosetta or enclosure revisions.

A hardware change should create a new identifiable revision rather than silently changing deployed units.

Examples include:

- improved connectors;
- revised sensor mounting;
- better environmental protection;
- improved power management;
- different communications hardware;
- serviceability improvements.

Every new revision should re-run the tests affected by the change.

## Future software and AI

Centaurus AI and ORIGIN software can become more useful as the number of deployments increases, because more diverse operating conditions can be observed.

However, new field data should not automatically be used to claim better AI performance.

Future model development should maintain:

- dataset provenance;
- privacy controls;
- clear train/test separation;
- versioned models;
- site-specific evaluation;
- false-positive/false-negative analysis;
- human review.

## International deployments

ORIGIN is intended as a broadly applicable heritage-protection platform, but international deployment introduces additional considerations:

- local regulations;
- radio approvals;
- privacy law;
- transport restrictions;
- language/localization;
- maintenance responsibility;
- partner training;
- climate differences.

The Durrës collaboration provides a useful first international pilot context for developing these processes.

## Partner model

Future deployments may be performed with museums, archaeological organizations, NGOs, educational institutions, municipalities, or other heritage stakeholders.

A deployment partnership should define:

- responsibilities;
- equipment ownership;
- installation approval;
- data responsibility;
- maintenance responsibility;
- publication permissions;
- pilot duration;
- removal/end-of-pilot procedure.

## End-of-deployment planning

Every future deployment should define how it ends.

The plan should cover:

- safe shutdown;
- data export/retention;
- removal of equipment;
- restoration of the mounting area;
- inventory return or transfer;
- final findings report;
- archiving of configuration and logs.

This is particularly important for temporary installations at heritage sites.

## Roadmap toward repeatability

The deployment roadmap is therefore:

1. complete and document Durrës planning;
2. install and commission only when site approval and hardware readiness allow;
3. collect real field evidence;
4. publish non-sensitive findings;
5. convert findings into lessons;
6. update hardware/software/process baselines;
7. repeat validation;
8. define the first reusable deployment template;
9. use that template at a second site;
10. compare results across sites before claiming general performance.

## Related documentation

- [Durrës Pilot](durres-pilot.md)
- [Findings](findings.md)
- [Lessons Learned](lessons-learned.md)
- [Development Roadmap](../development/roadmap.md)
- [Testing & Validation](../testing-validation/README.md)
