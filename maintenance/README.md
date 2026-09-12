# Maintenance

Long-term value from ORIGIN depends on more than successful installation. A deployed unit must remain mechanically secure, electrically healthy, correctly configured, environmentally protected and trustworthy as a monitoring source over time.

This chapter defines the maintenance approach for **Project ORIGIN 2026** and provides a common workflow for routine care, inspection, diagnostics, replacement and fault recovery.

> ORIGIN maintenance documentation describes the service process and the checks that should be performed. Exact replacement intervals and component lifetimes must be based on deployment evidence rather than assumed values.

## Maintenance objectives

Maintenance has five primary objectives:

1. preserve reliable sensing;
2. prevent small mechanical or environmental issues from becoming system failures;
3. detect degraded components before they silently corrupt monitoring data;
4. maintain traceability of every service action;
5. keep the installed system safe and reversible at heritage sites.

A unit that still powers on is not automatically considered healthy. ORIGIN maintenance therefore looks at the complete system, including enclosure and mounting integrity; seals and environmental exposure; Rosetta electronics; battery and solar subsystem; sensor condition and alignment; communications; firmware and configuration state; local storage; timekeeping and data provenance; module interfaces; and event generation and monitoring behavior.

## Maintenance model

ORIGIN uses three complementary maintenance layers.

### Preventive maintenance

Preventive maintenance is performed before a failure is visible. It includes cleaning, visual inspection, fastener checks, seal inspection, cable checks and verification that the unit is still reporting healthy data.

The purpose is to reduce unexpected downtime and catch gradual degradation early.

### Condition-based maintenance

Condition-based maintenance is triggered by system evidence rather than only by a calendar.

Examples include repeated communication failures; increasing sensor error rates; abnormal battery behavior; unstable power rails; repeated reboots; missing data; mounting movement; condensation or water evidence; radar coverage changes; and excessive false detections.

Condition-based maintenance is especially important for ORIGIN because two heritage deployments with the same hardware may experience very different environmental loads.

### Corrective maintenance

Corrective maintenance begins when a fault has already been confirmed.

The objective is not simply to replace parts as quickly as possible. The technician should first determine what failed; why it failed; whether the failure affected stored or transmitted data; whether another subsystem caused the fault; and whether the replacement requires recalibration or recommissioning.

## Maintenance status model

A deployed ORIGIN unit should have an operational status that is separate from individual sensor states.

Recommended maintenance states are:

| State | Meaning |
| --- | --- |
| Healthy | No known maintenance issue is affecting intended operation |
| Monitor | Minor condition detected; continued observation required |
| Service Due | Planned maintenance should be performed |
| Degraded | A subsystem is impaired but limited operation remains possible |
| Out of Service | Unit should not be relied on for monitoring |
| Maintenance | Unit is intentionally under service |
| Recommissioning | Service is complete but operational validation is still required |

A degraded or failed subsystem must not be represented to operators as normal operation.

## Recommended maintenance cadence

Until long-term field data establishes final intervals, maintenance frequency should be defined per deployment according to exposure and risk.

A useful baseline is:

| Trigger | Typical activity |
| --- | --- |
| Continuous / automated | Device health, sensor health, communication, storage and power diagnostics |
| Routine operator review | Check alerts, missing data, abnormal trends and device state |
| Scheduled site visit | Mechanical inspection, cleaning, seal inspection, cable inspection and functional checks |
| After severe weather | Inspect mounting, solar support, openings, water exposure and physical damage |
| After firmware or hardware change | Re-run affected validation and commissioning checks |
| After confirmed fault | Perform targeted diagnostics, repair and recommissioning |

This table is an operational framework, **not a validated lifetime guarantee or mandatory calendar interval**.

## Before touching the unit

Maintenance work should begin with documentation rather than tools.

Record site identifier; ORIGIN unit identifier; date and technician; reason for service; current firmware version; current configuration version; current module list; current health state; recent alerts or anomalies; and photographs of the installation before disturbance where appropriate.

If the unit is being removed or opened, preserve relevant logs before power is disconnected whenever possible.

## Heritage-site considerations

Service work at a heritage site must respect the same principles as installation avoid unnecessary contact with historic fabric; use reversible mounting methods where possible; do not drill, cut or modify protected material without authorization; prevent tools, fasteners or debris from damaging the site; preserve the approved appearance and position of the installation; and document any physical change made during service.

A maintenance action that improves the device but damages the site is not acceptable.

## Electrical safety

Before opening the enclosure or replacing electrical components:

1. place the device in maintenance state;
2. preserve logs if possible;
3. disconnect external power sources;
4. isolate battery power according to the hardware procedure;
5. verify the expected unpowered state before manipulating connectors or boards.

Battery systems must be inspected for swelling, leakage, heat damage, damaged insulation or abnormal odor. A visibly damaged energy-storage component should not be returned to service.

## Environmental protection during service

Opening an enclosure temporarily removes part of its environmental protection.

Service should therefore be performed in conditions that prevent rain entry; dust contamination; loose debris entering connectors; moisture becoming trapped during reassembly; and damage to seals.

Before closing the enclosure, inspect the sealing surfaces and confirm that cables, wires or debris are not trapped across the seal path.

## Maintenance records

Every service action should produce a maintenance record.

At minimum, record:

```text
unit_id
site_id
service_date
reason_for_service
initial_health_state
inspection_findings
diagnostic_results
actions_performed
parts_replaced
firmware_before
firmware_after
configuration_before
configuration_after
calibration_required
commissioning_required
final_health_state
technician
notes
```

If a component is replaced, record its previous and new identifier or revision whenever available.

## Change control

Maintenance can unintentionally become an undocumented redesign.

Examples include replacing a sensor with a different model; changing fastener type; changing seal material; rerouting wiring; substituting battery chemistry; changing solar-panel geometry; and modifying firmware during service.

Any change that affects compatibility, performance or validation should be handled through the normal development and validation process, not treated as an invisible maintenance substitution.

## Recalibration after service

Recalibration may be required after changes to radar position or angle; environmental sensor position; enclosure geometry near a sensor; solar alignment; mounting height or orientation; sensor replacement; configuration thresholds; and relevant firmware behavior.

The calibration procedure is documented under [Installation & Deployment → Calibration](../installation-deployment/calibration.md).

## Recommissioning after maintenance

A repaired unit should not return directly from “maintenance” to “healthy” simply because it powers on.

Depending on the work performed, recommissioning should confirm power stability; sensor health; communication; storage; timekeeping; configuration correctness; expected event behavior; environmental sealing; mechanical security; module detection; and remote visibility.

For significant repairs, repeat the relevant portions of the [Commissioning](../installation-deployment/commissioning.md) process.

## Evidence and validation

Maintenance procedures should evolve from field evidence.

Repeated service findings can reveal systemic design issues such as a fastener that loosens frequently; a cable route that traps water; a seal that degrades too quickly; a connector that is difficult to service; a sensor position that shifts after handling; and a battery configuration that does not match real deployment conditions.

These patterns should become engineering findings and feed back into ORIGIN development rather than being repeatedly repaired without design action.

## Chapter contents

[Routine Maintenance](routine-maintenance.md) — preventive service workflow and recurring care, [Inspection](inspection.md) — structured physical and functional inspection, [Diagnostics](diagnostics.md) — systematic fault isolation and health interpretation, [Component Replacement](component-replacement.md) — safe and traceable replacement process, and [Troubleshooting](troubleshooting.md) — symptom-based fault investigation and recovery.

## Related documentation

See also [Installation & Deployment](../installation-deployment/README.md); [Testing & Validation](../testing-validation/README.md); [Mechanical Design](../mechanical-design/README.md); [Rosetta](../rosetta/README.md); [Software](../software/README.md); and [Modules](../modules/README.md).
