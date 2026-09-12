# Inspection

Inspection is the structured examination of a deployed ORIGIN unit before any repair decision is made. Its purpose is to identify physical degradation, confirm whether the installation still matches the commissioned state, and collect evidence that can guide diagnostics.

Inspection should be systematic and repeatable. A casual visual check is not enough for a device expected to provide trustworthy monitoring data.

## Inspection sequence

A complete inspection should move from least invasive to most invasive:

1. remote status review;
2. site context review;
3. external visual inspection;
4. mechanical inspection;
5. sensor and module inspection;
6. power and solar inspection;
7. internal inspection only when justified;
8. functional verification;
9. documentation and disposition.

This sequence minimizes unnecessary disturbance.

## 1. Remote status review

Before visiting the device, review available telemetry.

Check last communication timestamp; recent reboot history; sensor health states; missing-data intervals; invalid readings; storage warnings; power-related warnings; firmware version; configuration version; module identities; and repeated alerts.

Remote status gives context for what to look for physically.

## 2. Site context review

Inspect the surrounding area before inspecting the device itself.

Look for changes such as vegetation growth; new structures; temporary barriers; moved objects; construction activity; new visitor routes; new sources of vibration; standing water; erosion; changed shading; and evidence of vandalism or accidental impact.

A change in the site can create apparent device problems even when the hardware is healthy.

## 3. External enclosure inspection

Inspect every accessible face of the enclosure.

### Structural condition

Check for cracks; layer separation or delamination in printed parts; deformation; warping; broken corners; impact damage; loose panels; missing fasteners; and damaged access features.

### Surface condition

Check for UV degradation; discoloration; brittle surfaces; abrasion; chemical contamination; biological growth; and dirt accumulation.

Surface appearance alone is not a failure, but it may indicate material aging that should be monitored.

## 4. Mounting inspection

The mounted position is part of ORIGIN's sensing configuration.

Verify the unit has not rotated; the unit has not tilted; the mounting base is stable; fasteners remain present; mounting points are not cracking; no historic fabric has been damaged; soil-mounted installations have not shifted because of erosion or compaction; and cables are not carrying mechanical load.

Where reference photographs or orientation marks exist, compare them with the current state.

## 5. Sensor inspection

Each sensor should be inspected both mechanically and functionally.

For the three mmWave sensors verify mounting screws; confirm the PCB has not shifted; inspect dedicated sensor openings; remove debris; look for moisture accumulation; confirm the sensing face is unobstructed; and verify orientation against the commissioned geometry.

For environmental sensors inspect exposure openings, remove contamination that could alter readings, check that ventilation paths are not blocked, and verify any protective membrane or shield is intact.

A physically intact sensor can still be electrically unhealthy, so visual inspection must be followed by functional checks.

## 6. Solar subsystem inspection

Inspect the solar assembly as a structure and as a cable path.

Check solar panel damage; contamination or shading; support stiffness; all support fasteners; the third hollow support; cable routing through the support; abrasion; pinch points; water entry routes; and connector condition.

Movement in the solar support may also apply force to the enclosure or cable entry and should not be treated only as a panel issue.

## 7. Cable and connector inspection

External cables should be checked for cuts; crushed insulation; bending damage; strain at entry points; UV damage; corrosion; loose connectors; contamination; exposed conductors; and contact with sharp edges.

Cable paths should also maintain drainage behavior so water is not directed into the enclosure.

## 8. BIT and expansion-module inspection

For attached modules, verify correct module identity; secure mounting; connector retention; no unexpected movement; no contact with soil or water unless specifically designed for it; no damaged housing; no cable strain; and software reports the expected module state.

A module that is physically present but not recognized by software requires diagnostics.

## 9. Seal and opening inspection

Inspect environmental barriers without claiming an unvalidated IP rating.

Look for torn or displaced gaskets; compressed or permanently deformed seals; seal contamination; cracks near screw bosses; water tracks; condensation marks; damaged cable glands; blocked drain paths; and debris at radar openings.

Because ORIGIN includes intentional sensor openings, the inspection should evaluate the actual water-management design rather than assuming the enclosure is fully sealed.

## 10. Internal inspection

Only open the unit when necessary and in suitable conditions.

Inspect internally for condensation; water marks; corrosion; discoloration from heat; loose hardware; detached connectors; damaged insulation; foreign debris; battery swelling; abnormal odor; PCB contamination; movement of Rosetta or sensors; and damage to storage or communication modules.

If internal moisture is found, document its location before cleaning because the pattern may identify the entry route.

## 11. Battery inspection

Where a battery is present, inspect for swelling; puncture; leakage; corrosion; damaged leads; insulation wear; connector overheating; and unexpected movement inside its mount.

A suspicious battery should be isolated and handled according to the battery manufacturer's safety requirements.

Do not continue normal operation merely because the battery still provides voltage.

## 12. Rosetta inspection

Inspect the Rosetta PCB for secure mounting; connector seating; contamination; corrosion; damaged components; heat discoloration; cracked solder joints visible under suitable inspection; foreign conductive material; and cable strain.

Do not probe or modify the board at a heritage site unless the service procedure specifically requires it and power has been safely isolated.

## Functional inspection

After physical checks, verify the system functionally.

Confirm normal boot; stable power state; expected firmware identity; expected configuration identity; sensor enumeration; valid readings; local storage health; communication; correct remote unit identity; and absence of new persistent errors.

For presence sensing, a simple controlled movement test can verify that each radar contributes expected observations, but a full coverage test is required if the orientation has changed.

## Inspection severity classification

Findings should be classified consistently.

| Level | Meaning | Typical response |
| --- | --- | --- |
| Observation | No current functional effect | Record and monitor |
| Minor | Small defect with low immediate risk | Correct during routine service |
| Significant | Likely to affect reliability or sensing | Diagnose and repair before normal service if possible |
| Critical | Safety risk, data-integrity risk or loss of essential function | Remove from normal monitoring / isolate as required |

Examples of critical findings can include internal water around electronics, damaged battery, unstable mounting, exposed conductors or a condition that causes the system to report false healthy status.

## Inspection record

A useful inspection record contains:

```text
unit_id
site_id
date
inspector
remote_status_review
site_changes
mount_condition
enclosure_condition
sensor_condition
solar_condition
cable_condition
module_condition
seal_condition
internal_inspection
battery_condition
rosetta_condition
functional_check
findings
severity
recommended_action
photos_reference
```

## Inspection does not equal validation

An inspection can show that a component appears intact and functions at the time of service. It does not automatically prove long-term reliability or validated performance.

If the inspection uncovers a condition that may have affected monitoring accuracy, the relevant [Testing & Validation](../testing-validation/README.md) procedure should be repeated.

## Next steps

If no meaningful defect is found, return to [Routine Maintenance](routine-maintenance.md).

If a fault or inconsistent behavior is found, continue with [Diagnostics](diagnostics.md).

If a part is confirmed defective, use [Component Replacement](component-replacement.md).

For symptom-based investigation, see [Troubleshooting](troubleshooting.md).
