# Galene Lab Standards

The **Galene Lab Standards** define the minimum quality requirements for tests performed on Project ORIGIN.

They are not intended to imitate a formal accredited laboratory standard. Their purpose is to make Team Galene's engineering evidence consistent, repeatable, auditable and useful across project revisions.

## 1. Define the question before testing

Every test should begin with a specific engineering question.

Weak example:

```text
Test the radar.
```

Better example:

```text
Verify that each installed radar can be identified independently and that a disconnected radar is reported as a fault rather than as an empty monitored zone.
```

A test without a defined question often produces observations that cannot support a clear conclusion.

## 2. Define acceptance criteria in advance

Pass criteria should be written before the result is known.

This reduces the risk of changing the definition of success after seeing the outcome.

Acceptance criteria may be numerical limits; required states; repeatability requirements; maximum error; required recovery behavior; physical inspection criteria; and successful completion of a sequence.

If a numerical limit has not yet been justified, the test should be exploratory rather than pretending to be a pass/fail validation.

## 3. Record the tested configuration

Every result must be attached to a known configuration.

At minimum, record where applicable:

| Field | Example |
| --- | --- |
| Hardware | Rosetta v2 |
| PCB revision | exact revision or commit |
| Firmware | version / commit |
| Mechanical revision | enclosure revision |
| Sensor configuration | sensor models and positions |
| Module configuration | installed modules |
| Test profile | configuration name |

A result without configuration traceability should not be reused as validation evidence for another revision.

## 4. Preserve raw evidence

Interpretation and evidence are different things.

A conclusion may say:

```text
All three radar channels were detected after restart.
```

The evidence should preserve the underlying information, such as serial log; timestamped event file; video; test table; photograph of wiring; and measurement screenshot.

Raw evidence should not be silently edited to make a result appear cleaner.

## 5. Use repeatable procedures

A useful procedure tells another team member what to do without relying on undocumented knowledge.

A procedure should normally include:

1. required equipment;
2. setup diagram or configuration;
3. preparation steps;
4. measurement sequence;
5. number of repetitions where relevant;
6. expected output;
7. acceptance criteria;
8. shutdown or recovery steps.

## 6. Control one variable where practical

When investigating a problem, change one meaningful variable at a time where possible.

For example, when testing a radar opening keep sensor position fixed, keep firmware fixed, keep target route fixed, and change only the opening geometry.

This makes it easier to connect an observed change to a cause.

## 7. Repeat measurements

A single successful trial may be useful during development but is weak validation evidence.

Repeated trials help reveal intermittent faults; variation; startup differences; environmental sensitivity; operator effects; and inconsistent mechanical positioning.

The required number of repetitions depends on the claim being tested. The test record should state the number performed rather than implying statistical confidence that was not established.

## 8. Measure uncertainty honestly

Measurements have limitations.

Possible uncertainty sources include instrument accuracy; measurement resolution; human positioning; target movement; ambient conditions; mounting tolerances; time synchronization; and sampling interval.

Where uncertainty is meaningful, record it or at least identify the dominant source.

## 9. Separate component specifications from ORIGIN results

Manufacturer specifications may be used to define expected operating conditions, but they are not equivalent to complete-system validation.

For example, a radar module's published maximum distance does not prove that the same distance is achieved when the sensor is installed inside ORIGIN's final enclosure at a heritage site.

Public documentation should label values as either manufacturer specification, design target, observed ORIGIN result, and validated ORIGIN result.

## 10. Test failures explicitly

A test program that only checks expected success paths is incomplete.

Where safe and practical, deliberately create faults such as unplugging a sensor; interrupting communications; rebooting the controller; disconnecting external power; presenting invalid input; moving or obstructing a sensor; removing a module; and interrupting an update.

The objective is to verify that the system fails visibly and recoverably.

## 11. No hidden “pass” assumptions

A system being powered does not mean it is healthy.

Examples of states that must remain distinct include:

```text
Sensor healthy + no target
Sensor missing
Sensor initializing
Sensor invalid
Sensor disabled
```

Similarly:

```text
Network available
Network unavailable
Data queued locally
Transmission failed
```

Validation should confirm that these states can be distinguished.

## 12. Use calibrated or checked instruments where needed

Not every development measurement requires laboratory-grade equipment, but the equipment must be appropriate for the claim.

Examples include multimeter for rail verification; regulated bench supply for controlled power tests; known reference distance for radar tests; scale or force method for mechanical loading; and thermometer/hygrometer for environmental context.

If equipment calibration status is unknown and could materially affect the result, record that limitation.

## 13. Photograph the setup

A setup photograph is often one of the most valuable pieces of test evidence.

It can reveal details that are otherwise missed in written notes cable routing; sensor direction; fixture position; enclosure revision; mounting height; target path; and environmental context.

## 14. Record anomalies, even when the test passes

A pass does not mean that unusual behavior should be omitted.

Examples one delayed startup among ten repetitions; temporary communication warning; unexpected temperature rise; visible enclosure flex; and one false detection outside the acceptance window.

An anomaly can become important in a later failure investigation.

## 15. Do not delete failed results

Failed tests are engineering evidence.

When a design changes after a failure, the historical result should remain available with its original configuration and status. A later passing revision does not invalidate the usefulness of the earlier failure record.

## 16. Re-test after relevant changes

Changes that may require regression testing include PCB revision; component substitution; firmware sensor-driver changes; power-management changes; enclosure geometry changes; radar opening changes; sensor angle changes; mounting-height changes; communications changes; configuration changes; and AI or event-processing changes.

The team should identify which tests are affected rather than repeating every test blindly.

## 17. Use a standard test record

Recommended template:

```text
Test ID:
Title:
Date:
Operator:

Objective:

Configuration:
- Hardware:
- Firmware:
- Mechanical:
- Sensors/modules:

Equipment:

Procedure:
1.
2.
3.

Acceptance criteria:

Observed results:

Status: PASS / FAIL / CONDITIONAL / INVALID

Anomalies:

Evidence:

Follow-up:
```

## 18. Validation before public claims

A public technical claim should be traceable to evidence appropriate to the claim.

Before publishing a value as validated ORIGIN performance, confirm the test configuration is known; the procedure is documented; the measurement is reproducible; the limitation is stated; and the result applies to the current revision or is clearly revision-specific.

## 19. Safety and heritage-site responsibility

Testing must not create unnecessary risk to people, equipment or cultural heritage.

At real sites do not modify historic fabric without permission; use reversible test fixtures where possible; protect visitors and staff from trip hazards; do not intentionally create unsafe electrical conditions; coordinate disruptive testing with site operators; and follow local rules for drones and restricted areas.

## 20. Final rule

The Galene Lab Standards prioritize **evidence over appearance**.

A documented failure with a clear corrective action is more valuable than an undocumented demonstration that appeared to work.
