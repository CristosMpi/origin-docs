# Findings

This page records field findings from ORIGIN deployments and pilot activities.

A finding is an **evidence-backed observation** about how the system behaves in practice. It is not automatically a final design conclusion and should not be exaggerated into a project-wide claim without supporting data.

## Current status

As of the current documentation revision, the Durrës deployment is still described as a planned pilot. Therefore, this page intentionally does **not** invent operational outcomes, sensor statistics, uptime values, or performance figures that have not yet been measured.

The structure below defines how real findings should be captured once field evidence is available.

## Finding format

Each finding should contain:

| Field | Description |
| --- | --- |
| Finding ID | Stable identifier |
| Deployment | Site/pilot where it occurred |
| Date | When the observation was made |
| Device(s) | Affected ORIGIN unit identifiers |
| Configuration | Hardware, firmware, software, module, and calibration versions |
| Observation | What was actually seen |
| Evidence | Logs, measurements, photographs, test record, or operator report |
| Impact | Why the observation matters |
| Confidence | How strongly the evidence supports the interpretation |
| Action | Design/process change, further test, or no action |
| Status | Open, monitoring, resolved, or accepted |

## Example finding structure

```text
Finding ID: DUR-F-001
Deployment: Durrës Pilot
Device: DUR-ORIGIN-02
Observation: [measured field observation]
Evidence: [test record / log reference]
Impact: [engineering consequence]
Action: [required follow-up]
Status: Open
```

The example above is a format only and does not represent a real Durrës finding.

## Categories of findings

### Mechanical

Potential field findings can include:

- mounting movement;
- service-access difficulty;
- enclosure deformation;
- fastener loosening;
- cable strain;
- water paths;
- sensor-opening contamination;
- solar-support vibration;
- difficult assembly/disassembly.

### Sensor

Potential findings include:

- unexpected blind zones;
- reflections from walls or cases;
- differences between bench and installed performance;
- cross-zone detections;
- environmental-sensor drift;
- false presence events;
- sensor startup instability;
- sensitivity to mounting angle.

### Power

Potential findings include:

- insufficient solar exposure;
- unexpected energy consumption;
- charging interruptions;
- low-energy recovery behavior;
- power rail instability;
- battery servicing difficulty.

### Communications

Potential findings include:

- unstable coverage;
- reconnect delays;
- delayed records;
- synchronization issues;
- local buffering limitations;
- confusing offline-state reporting.

### Software

Potential findings include:

- configuration errors;
- difficult recovery procedures;
- ambiguous operator states;
- excessive event volume;
- missing health information;
- time-synchronization problems.

### Centaurus AI

Potential findings include:

- over-prioritization;
- under-prioritization;
- poor handling of missing sensors;
- weak explanation of a decision;
- sensitivity to site-specific baseline changes;
- false anomaly patterns.

## Evidence quality

Not all field observations have equal strength.

### Anecdotal

A single person reports an issue but no supporting record exists.

Useful as a lead, but not enough for a validated claim.

### Reproduced

The behavior can be intentionally reproduced under similar conditions.

This is stronger evidence and often sufficient to open a design issue.

### Measured

The finding includes quantitative measurements or logs.

### Repeated

The behavior appears across multiple test runs, units, or conditions.

### Independently confirmed

More than one observer, data source, or measurement method supports the conclusion.

ORIGIN should prefer measured and repeated evidence when deciding whether to change a design baseline.

## Negative findings are valuable

A pilot should not hide failures.

Examples of useful negative findings include:

- a sensor arrangement that leaves an unacceptable blind zone;
- a mounting method that is too invasive;
- a solar orientation that does not supply enough energy;
- a communications path that is unreliable;
- a maintenance operation that requires too much disassembly;
- an AI rule that produces too many irrelevant events.

These findings directly improve later versions.

## No-fault findings

Sometimes a test shows that a suspected problem is not significant.

That result should also be recorded.

For example:

- a specific enclosure face does not measurably degrade radar behavior;
- a mounting method remains stable after repeated service cycles;
- a particular event rule does not increase false positives under the tested conditions.

Recording these results prevents the same question from being investigated repeatedly without context.

## Relationship to validation results

Deployment findings and formal validation results serve different purposes.

- **Findings** capture what was noticed in practice.
- **Validation results** record whether a defined test met a defined acceptance criterion.

A field finding may later become the basis of a validation test.

See [Validation Results](../testing-validation/validation-results.md).

## Relationship to lessons learned

A finding becomes a lesson learned when it produces a broader engineering conclusion.

Example:

```text
Finding:
A specific mounting position caused repeated radar reflections.

Lesson:
Sensor orientation must be validated after installation against nearby reflective geometry.

Design/process change:
Add an installed-coverage test to commissioning.
```

See [Lessons Learned](lessons-learned.md).

## Publishing findings

Public documentation should avoid revealing:

- exact security blind spots;
- sensitive site layouts;
- access-control weaknesses;
- network credentials;
- detailed attack paths;
- private operator information.

A public finding can describe the engineering lesson without publishing information that increases risk to the protected heritage site.

## Current finding register

At present, no Durrës operational findings are published because the pilot has not been documented here as commissioned and operational.

Known development findings from laboratory and manufacturing work are recorded in their relevant chapters, including the incomplete Rosetta v2 fabrication export identified in the Testing & Validation and Rosetta documentation.

When deployment evidence becomes available, this page should be updated with real, traceable field records.

## Related documentation

- [Durrës Pilot](durres-pilot.md)
- [Lessons Learned](lessons-learned.md)
- [Testing & Validation](../testing-validation/README.md)
- [Field Testing](../testing-validation/field-testing.md)
