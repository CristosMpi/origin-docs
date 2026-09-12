# Installation & Deployment

Installing ORIGIN is not only a mechanical task. A field deployment combines site assessment, mounting, power, communications, sensor orientation, configuration, calibration, commissioning, documentation, and handover.

The objective of this chapter is to make deployment repeatable and auditable. A unit should not be considered deployed simply because it powers on; it should be considered deployed only after its physical installation, sensing behavior, data path, configuration, and operational responsibilities have been checked together.

## Deployment lifecycle

A complete ORIGIN deployment follows six stages:

```text
Site assessment
      ↓
Physical installation
      ↓
Initial setup
      ↓
Calibration
      ↓
Commissioning
      ↓
Operational handover
```

Each stage should leave enough documentation for another person to understand what was installed, where it was installed, how it was configured, and what limitations were observed.

## Before going to site

Before transport, the deployment team should confirm that the unit has already passed bench-level checks.

At minimum, confirm that the correct hardware revision is identified; the current firmware version is known; Rosetta powers correctly; the expected sensors are detected; local logging works; configuration can be read back; known issues are documented; mounting hardware is complete; required tools and fasteners are packed; the deployment configuration has been prepared; and a rollback plan exists if commissioning fails.

Field installation should not be used as a substitute for basic workshop validation.

## Site-specific configuration

Every heritage location is different. ORIGIN therefore needs a deployment profile that captures the site's physical and operational context.

A deployment profile should include site name and internal identifier; unit identifier; installation coordinates or mapped location where appropriate; mounting orientation; sensor-facing directions; power source; connectivity method; enabled modules; local thresholds and rules; commissioning date; responsible operator or institution; maintenance contact; and known site-specific limitations.

No credentials, access tokens, SIM secrets, or private operational details should be committed to the public documentation repository.

## Heritage-site constraints

ORIGIN is intended for cultural-heritage environments, so deployment decisions must account for the site itself.

The installation should avoid unnecessary intervention in historic material. Drilling, adhesives, clamps, stakes, and support structures should be approved by the relevant site authority before use.

Where possible, installation should prefer reversible fixing methods; existing infrastructure; non-destructive supports; clearly documented contact points; removable cable routing; and minimal visual impact.

The monitoring system must not become a new source of physical risk to the heritage asset.

## System-level checks

A successful deployment confirms more than individual component operation.

The following chain should work end to end:

```text
Physical stimulus
      ↓
Sensor observation
      ↓
Rosetta acquisition
      ↓
Firmware validation
      ↓
Local event / record
      ↓
Communications
      ↓
Upstream processing
      ↓
Operator-visible result
```

A failure at any stage should be distinguishable from a valid “nothing detected” state.

## Deployment evidence

Each installation should produce a deployment record containing at least unit serial or internal ID; hardware revision; firmware version; photos of final installation; sensor orientation map; power configuration; network status; calibration results; commissioning results; outstanding defects; acceptance decision; and date and responsible personnel.

This record becomes the baseline against which later maintenance and performance changes can be compared.

## Rollback principle

If a deployment cannot be commissioned safely and reliably, the correct outcome may be to stop, revert, or remove the unit.

Examples of rollback conditions include unstable power; repeated sensor failures; unsafe mounting; water ingress risk; unacceptable false detections; inability to verify communications; conflict with site operations; configuration mismatch; and missing approval for the selected mounting method.

The presence of a deadline should not override these conditions.

## Chapter structure

This chapter is organized as follows [Site Assessment](site-assessment.md) — evaluate the location before installation; [Installation](installation.md) — mount the hardware and route power/cables; [Setup](setup.md) — initialize the software and deployment configuration; [Calibration](calibration.md) — establish reliable sensor behavior for the site; [Commissioning](commissioning.md) — verify the complete system before acceptance; and [Deployment Checklist](deployment-checklist.md) — field-ready checklist for a deployment team.

For the physical enclosure and mounting design, see [Mechanical Design](../mechanical-design/README.md). For software configuration, see [Software → Configuration](../software/configuration.md). For later field results, see [Deployments](../deployments/README.md).
