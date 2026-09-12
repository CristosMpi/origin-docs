# Durrës Pilot

The **Durrës Pilot** is Project ORIGIN's principal real-world cultural-heritage deployment program for 2026.

The current project plan is to provide **five ORIGIN units** to the **Archaeological Museum of Durrës, Albania** for pilot use and evaluation.

The purpose of the pilot is not simply to demonstrate that ORIGIN can be transported to another country. It is intended to test whether the system can be installed, commissioned, operated, maintained, and interpreted in a genuine heritage environment under real constraints.

## Status

The Durrës program should be described as a **planned/pilot deployment** until installation and commissioning evidence confirms otherwise.

This distinction matters. A planned donation or collaboration is not the same as a completed operational deployment.

Public documentation should therefore avoid phrases such as "ORIGIN protects the Archaeological Museum of Durrës" unless the system has actually been installed, commissioned, and accepted for that purpose.

## Why Durrës

Durrës provides an appropriate setting for a heritage-monitoring pilot because the project is designed specifically around the practical difficulties of protecting archaeological and cultural assets.

A real museum or archaeological environment can expose ORIGIN to variables that are difficult to recreate fully in a laboratory, including complex walls and reflective surfaces; visitor movement; restricted mounting locations; conservation requirements; changing temperature and humidity; local communications conditions; staff workflows; maintenance-access constraints; and visually sensitive installation areas.

These conditions are valuable because ORIGIN needs to be judged as a deployed system, not only as a prototype on a workbench.

## Pilot objectives

The pilot is intended to investigate several areas.

### 1. Installation practicality

Determine whether ORIGIN can be physically installed without creating unacceptable interference with the site.

Questions include Can the unit be mounted reversibly?; Can the sensors be oriented correctly without invasive modifications?; Is service access practical?; Can cable routing be made safe and discreet?; and Does the enclosure interfere visually with the environment?.

### 2. Sensor behavior

Evaluate presence and environmental sensing in the actual geometry of the deployment area.

For the mmWave subsystem, this includes coverage direction; overlap between sensors; blind zones; reflections; false detections; repeatability; and detection behavior near walls or display structures.

### 3. Communications

Observe whether the intended communications architecture remains usable under real site conditions.

A field deployment should record connection availability; reconnect behavior; data buffering during outages; delayed delivery; synchronization after reconnection; and operator visibility into connection health.

### 4. Power performance

Where autonomous or solar-assisted power is used, the pilot should test whether real energy availability matches design assumptions.

The relevant questions include actual solar exposure; charging behavior; energy use over the daily cycle; low-power behavior; recovery after low-energy conditions; and effect of shading or seasonal changes.

No battery-life figure should be published for the Durrës pilot until it has been measured under a documented configuration.

### 5. Operator usability

A successful monitoring platform must be understandable to the people responsible for the site.

The pilot should therefore assess whether users can interpret normal state; warning state; alarm/event state; connectivity loss; sensor failure; maintenance requirement; and disabled or intentionally offline state.

### 6. Maintenance burden

The deployment should identify how often physical intervention is required and which operations are difficult in practice.

Examples include enclosure inspection; cleaning; connector access; battery or power-system service; sensor alignment; module replacement; firmware update; and configuration recovery.

## Five-unit deployment model

The planned quantity of five units enables a more useful pilot than a single isolated device.

Multiple units can be used to explore different site positions; different orientations; different environmental conditions; overlap between monitored zones; centralized vs per-unit event handling; maintenance differences between locations; and comparative performance.

The five units should not automatically be assumed to use identical configurations. The final arrangement should follow the site assessment.

## Unit identity

Every pilot unit should receive a stable identifier before installation.

A deployment record should link that identifier to Rosetta hardware revision; enclosure revision; firmware version; software version; module set; calibration version; installation position; commissioning record; and maintenance history.

An example naming convention could be:

```text
DUR-ORIGIN-01
DUR-ORIGIN-02
DUR-ORIGIN-03
DUR-ORIGIN-04
DUR-ORIGIN-05
```

The final naming convention should be chosen before commissioning and used consistently across logs and documentation.

## Site assessment before installation

Before any unit is mounted, Team Galene and the responsible site representatives should document the deployment area.

The assessment should cover heritage/conservation restrictions; available mounting surfaces; prohibited attachment methods; visitor routes; staff-only areas; expected monitored zones; sources of radar reflection; possible water exposure; expected sun/shade conditions; communications coverage; access for future maintenance; and physical security of the unit itself.

See [Site Assessment](../installation-deployment/site-assessment.md).

## Proposed deployment workflow

The Durrës pilot should follow the standard ORIGIN process:

```text
Site review
    ↓
Position selection
    ↓
Mounting design
    ↓
Pre-installation unit test
    ↓
Physical installation
    ↓
Power-up and setup
    ↓
Sensor calibration
    ↓
Coverage testing
    ↓
Communications testing
    ↓
Commissioning
    ↓
Pilot observation period
    ↓
Findings and review
```

## Commissioning requirements

Each installed unit should pass its own commissioning process.

At minimum, commissioning should confirm stable physical mounting; correct sensor orientation; expected sensor health; valid Rosetta startup; correct configuration loaded; reliable local data acquisition; communications behavior; correct timestamps; event generation; recovery after temporary communications loss; understandable operator status; and documented baseline sensor behavior.

A unit that fails one of these checks should remain in a commissioning or pilot-debug state rather than being represented as fully operational.

## Data and privacy

The pilot should collect only the data needed for the monitoring objective and engineering evaluation.

Where presence information is used, public documentation should avoid publishing detailed site-security patterns, exact vulnerable locations, or other information that could increase risk to the museum or its collections.

Logs used for engineering should still preserve enough context to analyze which device generated the record; which sensor generated it; when it occurred; system health at the time; configuration/software version; and whether the event was test-generated or naturally observed.

## Expected pilot outputs

A successful pilot should produce engineering evidence, not only photographs.

Useful outputs include installation records; unit configuration records; sensor coverage maps; false-positive observations; environmental records; communications reliability observations; maintenance logs; operator feedback; fault/recovery records; and design changes resulting from field use.

These outputs should feed into [Findings](findings.md), [Lessons Learned](lessons-learned.md), and [Testing & Validation](../testing-validation/README.md).

## What has not yet been claimed

Until supported by documented pilot evidence, the Durrës deployment should **not** be used to claim guaranteed 360° human detection; a specific end-to-end detection range; a specific AI accuracy percentage; a specific communications uptime percentage; a specific battery autonomy duration; a formal IP rating; zero false alarms; zero maintenance operation; and permanent operational acceptance by the museum.

Those claims require test or operational evidence tied to the deployed configuration.

## Success criteria

The pilot should be considered successful if it generates actionable evidence that improves ORIGIN, even if some components require redesign.

Useful outcomes include confirming a design choice; identifying a mounting problem; discovering a false-detection condition; improving commissioning steps; changing sensor orientation; improving enclosure access; refining power management; and simplifying operator workflow.

A pilot that reveals problems is still valuable if those problems are documented and used to improve the system.

## Documentation after deployment

Once installation begins, this page should be updated with verified information such as installation dates; number of units actually installed; hardware revisions; deployment photographs approved for publication; high-level arrangement; commissioning status; validated findings; and major design changes resulting from the pilot.

Sensitive site details should remain private.

## Related documentation

[Deployment Architecture](deployment-architecture.md), [Findings](findings.md), [Lessons Learned](lessons-learned.md), [Installation & Deployment](../installation-deployment/README.md), and [Testing & Validation](../testing-validation/README.md).
