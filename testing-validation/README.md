# Testing & Validation

Testing is part of the engineering process for Project ORIGIN, not a final demonstration performed after development is finished.

ORIGIN combines electronics, sensors, software, mechanical systems, communications, power management and higher-level analysis. A failure in any one of those areas can affect the reliability of the complete system. For that reason, validation is organized from individual components through subsystem tests to complete field deployments.

This chapter defines how Team Galene plans, records and interprets ORIGIN tests.

## Objectives

The testing program has five primary goals:

1. **Verify functionality.** Confirm that each subsystem performs its intended function.
2. **Measure performance.** Replace assumptions with repeatable observations and measurements.
3. **Identify failure modes.** Understand how the system behaves when components, communications or environmental conditions are abnormal.
4. **Protect deployment credibility.** Separate manufacturer specifications, engineering targets and validated ORIGIN performance.
5. **Support iteration.** Convert failures and unexpected observations into design changes.

## Validation levels

ORIGIN testing is divided into several levels.

### Component level

Individual electronic components, sensors, connectors, mechanical parts and software functions are checked independently where practical.

### Subsystem level

Examples include Rosetta power and control electronics; radar sensing; environmental sensing; communication paths; enclosure and mounting systems; solar support structure; software data handling; and module interfaces.

### Integrated-system level

The complete ORIGIN Core is operated with representative hardware, firmware, enclosure, sensors and communications.

### Deployment level

The final stage evaluates the system in the geometry, environmental conditions and operational workflow of a real or representative site.

A component passing a bench test does not automatically mean the integrated system is validated.

## Evidence hierarchy

ORIGIN documentation distinguishes four types of technical statements.

| Category | Meaning |
| --- | --- |
| Manufacturer specification | Published by the component manufacturer |
| Design target | Intended engineering objective |
| Observed result | Measurement from a documented ORIGIN test |
| Validated performance | Result reproduced under a defined procedure and accepted for the stated configuration |

This distinction is especially important for sensing range, environmental resistance, battery life, communications reliability and AI-assisted analysis.

## Test traceability

Every meaningful test should identify test ID; date; ORIGIN hardware revision; firmware/software version; mechanical revision where relevant; sensor/module configuration; equipment used; test environment; procedure; expected result; observed result; pass/fail/conditional status; anomalies; evidence files; person performing the test; and required follow-up.

Without traceability, a result becomes difficult to reproduce after the design changes.

## Pass, fail and conditional results

A test may finish with one of the following states.

### PASS

The predefined acceptance criteria were met.

### FAIL

One or more acceptance criteria were not met.

### CONDITIONAL

The test produced useful evidence but cannot support an unrestricted pass. Examples include incomplete coverage, an unresolved anomaly or a result that applies only to a specific configuration.

### NOT TESTED

No valid test evidence has yet been recorded.

### INVALID TEST

The test procedure, instrumentation, configuration or recorded data was insufficient to support a conclusion.

## Test IDs

A consistent naming scheme is recommended:

```text
ORIGIN-[DOMAIN]-[NUMBER]
```

Examples:

```text
ORIGIN-ELEC-001
ORIGIN-SENS-004
ORIGIN-MECH-003
ORIGIN-ENV-002
ORIGIN-FIELD-006
```

The number should remain tied to the test definition even when the procedure is repeated against later revisions.

## Baselines and revisions

A result applies only to the configuration that was tested.

If the enclosure, sensor orientation, PCB, firmware, calibration or power architecture changes, the team should assess whether affected tests must be repeated.

A useful release record includes:

```text
Hardware: Rosetta v2
Firmware: <version>
Mechanical: <revision>
Configuration: <profile>
Test suite: <revision>
```

This prevents results from an early prototype being presented as evidence for a later design without revalidation.

## Failure-oriented testing

Testing should not only confirm normal operation.

ORIGIN must also be exercised under failure conditions such as sensor disconnect; communication loss; restart during operation; low or unstable power; missing storage; invalid sensor data; blocked or misaligned sensing path; partial module failure; configuration corruption; and interrupted software update.

A robust system should distinguish failure from a valid normal state. For example, a disconnected presence sensor must not be interpreted as “no person present.”

## Test evidence

Evidence may include measurement tables; photographs; videos; serial logs; firmware logs; screenshots; exported datasets; CAD inspection screenshots; electrical measurements; environmental observations; coverage maps; and test fixtures and diagrams.

Where possible, raw evidence should be preserved separately from the written interpretation.

## Current validation status

The public documentation intentionally does not claim that every ORIGIN subsystem has completed final field validation.

Some sections currently define the required validation procedure and acceptance framework rather than publishing numerical pass results. This is preferable to filling the documentation with unsupported performance claims.

Validated measurements will be added to [Validation Results](validation-results.md) as reproducible evidence becomes available.

## Chapter structure

[Galene Lab Standards](galene-lab-standards.md) — common rules for test quality and evidence.

[Electronics Testing](electronics-testing.md) — Rosetta power, assembly and electrical verification.

[Sensor Testing](sensor-testing.md) — sensor communication, accuracy, presence coverage and failure handling.

[Mechanical Testing](mechanical-testing.md) — enclosure, mounts, interfaces, solar supports and fit.

[Environmental Testing](environmental-testing.md) — moisture, temperature, exposure and enclosure behavior.

[Field Testing](field-testing.md) — integrated testing in realistic site conditions.

[Validation Results](validation-results.md) — public register of completed evidence and known limitations.

## Principle

The standard for ORIGIN is simple:

> A feature is not considered validated because it worked once. It is validated when the configuration, method, evidence and limitations are clear enough for the result to be reproduced and understood.
