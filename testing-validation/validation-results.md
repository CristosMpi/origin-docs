# Validation Results

This page is the public register for Project ORIGIN validation evidence.

Its purpose is to prevent design intentions, manufacturer specifications and informal demonstrations from being presented as completed ORIGIN validation.

## Status definitions

| Status | Meaning |
| --- | --- |
| **Validated** | Reproducible evidence exists for the stated configuration and claim |
| **Observed** | Behavior has been seen during development, but evidence is not yet sufficient for a formal validation claim |
| **Procedure defined** | A repeatable test method exists, but completed evidence is not yet published |
| **Conditional** | Evidence exists with important configuration or scope limitations |
| **Issue identified** | Testing/review found a problem requiring correction or revalidation |
| **Not yet validated** | No public evidence supports the claim yet |

## Current public validation register

The table below reflects the evidence currently available in the documentation repository.

| Domain | Item | Status | Public conclusion |
| --- | --- | --- | --- |
| Manufacturing | Rosetta v2 Gerber package completeness | **Issue identified** | Reviewed export is missing Excellon drill files and must not be treated as a complete fabrication package |
| PCB | Rosetta v2 exported stack-up metadata | **Observed from export** | 2-layer, 1.6 mm FR-4, 35 μm copper metadata recorded from the reviewed manufacturing export |
| Electronics | First-power electrical validation | **Procedure defined** | Full measured bring-up results not yet published here |
| Power | Rail stability and current consumption | **Procedure defined** | Numerical system performance remains to be published from controlled tests |
| Sensors | Sensor communication and fault-state tests | **Procedure defined** | Test method defined; public test records still required |
| Presence detection | Installed three-radar coverage | **Not yet validated** | No public claim of guaranteed 360° ORIGIN coverage |
| Presence detection | Maximum ORIGIN detection range | **Not yet validated** | Manufacturer C4001 capability must not be treated as ORIGIN system range |
| Mechanical | Rosetta/enclosure fit | **Procedure defined** | Revision-specific inspection results still required |
| Mechanical | Radar mounting and alignment | **Procedure defined** | Final released enclosure must be inspected and sensor-tested |
| Mechanical | Solar-support robustness | **Procedure defined** | No public structural load rating is claimed |
| Environmental | Waterproofing / ingress rating | **Not yet validated** | ORIGIN currently makes no formal IP-rating claim |
| Environmental | Operating temperature range | **Not yet validated** | Component limits are not equivalent to full-system validation |
| Software | Fault-state architecture | **Procedure defined** | Implementation must be verified against the actual firmware release |
| Communications | Offline buffering / recovery | **Procedure defined** | Release-specific field evidence required |
| Centaurus AI | Detection/analysis performance | **Not yet validated** | No unsupported accuracy, precision or autonomous-decision claim is made |
| Field deployment | Durrës pilot | **Planned / evidence pending** | Deployment planning must not be presented as completed field validation until records exist |

## Confirmed manufacturing finding

The strongest specific public finding currently recorded comes from review of the Rosetta v2 manufacturing export supplied during documentation development.

The package included PCB fabrication layers and Gerber job metadata, but **no Excellon drill files were present**.

### Result

**Status: Issue identified**

The reviewed package is incomplete for normal PCB fabrication and should be regenerated or supplemented before being treated as a production manufacturing release.

This finding is also documented in [Rosetta → Manufacturing](../rosetta/manufacturing.md) and [Electronics Testing](electronics-testing.md).

## Rosetta v2 export metadata

The reviewed board export provides useful revision-specific metadata generated using KiCad Pcbnew 10.0.1; generated on 18 July 2026; two copper layers; nominal 1.6 mm FR-4 construction in the job metadata; 35 μm copper metadata; and exported board bounding size approximately 100.05 × 104.8 mm.

These values describe the reviewed export. They do **not** by themselves validate electrical performance or the physical dimensions of every later Rosetta revision.

## Claims intentionally not made

Until test evidence is added, ORIGIN documentation does not claim a validated value for complete-system battery life; solar autonomy; waterproof/IP rating; maximum field operating temperature; maximum ORIGIN presence-detection distance; guaranteed 360° coverage; false-positive rate; false-negative rate; AI accuracy; communications uptime; and multi-year outdoor durability.

The absence of these numbers is deliberate. Publishing an unsupported number would reduce the value of the documentation.

## How new results are added

A result should be promoted to **Validated** only when the evidence includes:

1. a defined test ID;
2. exact tested revision/configuration;
3. repeatable procedure;
4. acceptance criteria defined before conclusion;
5. raw or traceable evidence;
6. observed result;
7. limitations;
8. reviewer/team sign-off appropriate to the project.

## Recommended result format

Future results should be added in a consistent form.

```text
Test ID: ORIGIN-SENS-001
Title: <test title>

Configuration:
Hardware: <revision>
Firmware: <version>
Mechanical: <revision>
Configuration profile: <profile>

Procedure:
<link or summary>

Acceptance criteria:
<criteria>

Result:
<measurement / observation>

Status:
PASS / FAIL / CONDITIONAL

Limitations:
<scope>

Evidence:
<files / logs / photos>
```

## Result tables by domain

As evidence grows, this page should maintain separate tables for:

### Electronics

Power rails.

Startup.

Current consumption.

Charging/power transitions.

Sensor buses.

Storage.

Restart recovery.

### Sensors

Environmental-sensor comparison.

Radar coverage.

Stationary-presence behavior.

False detections.

Blind zones.

Multi-radar behavior.

### Mechanical

Critical dimensions.

PCB fit.

Assembly cycles.

Solar support.

Base stability.

Cable routing.

Service access.

### Environmental

Splash exposure.

Condensation.

Solar heating.

Humidity.

Dust/debris.

Material aging.

### Software and communications

Fault handling.

Data integrity.

Offline buffering.

Restart recovery.

Update rollback.

Message ordering.

### Centaurus AI

If quantitative AI results are later published, they should include the dataset, test split, metric definitions, model/version and deployment limitations. A single generic “accuracy” percentage is not sufficient.

### Field deployment

Field results should identify site; dates; number of units; actual hardware/software revision; test duration; coverage configuration; known events; false events; failures; and maintenance interventions.

## Historical results

When a later revision improves a result, the older result should remain available with its revision identifier.

Example:

```text
Rosetta v2 / Enclosure R3 — FAIL — radar opening caused unacceptable obstruction
Rosetta v2 / Enclosure R4 — PASS — revised opening under same procedure
```

Keeping both results makes the engineering evolution visible.

## Relationship to competition demonstrations

Competition demonstrations and presentations are valuable communication tools, but they are not automatically validation evidence.

A feature demonstrated successfully at an event may be recorded as an observation. It should only be promoted to a validated result if the configuration, procedure and evidence satisfy the Galene Lab Standards.

## Transparency principle

This register should remain conservative.

When evidence is incomplete, the correct status is **not yet validated**, not an estimated value.

As the ORIGIN 2026 system progresses through bench testing, integration and field deployment, this page should become the central evidence index for the project's technical claims.

## Related documentation

See [Galene Lab Standards](galene-lab-standards.md); [Electronics Testing](electronics-testing.md); [Sensor Testing](sensor-testing.md); [Mechanical Testing](mechanical-testing.md); [Environmental Testing](environmental-testing.md); and [Field Testing](field-testing.md).
