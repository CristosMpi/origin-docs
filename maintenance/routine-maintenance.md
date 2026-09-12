# Routine Maintenance

Routine maintenance keeps ORIGIN reliable between major service events. It combines automated health monitoring with periodic physical inspection, cleaning and verification of the installed system.

The exact interval must be set for each deployment according to environment, access constraints and site risk. ORIGIN does not currently claim one universal validated maintenance period.

## Maintenance philosophy

Routine service should be **preventive** — identify degradation before failure; **minimal** — disturb the installation only as much as necessary; **traceable** — record every action; **repeatable** — use the same checklist and acceptance logic; and **site-aware** — protect the heritage environment as well as the device.

## Continuous remote checks

Where remote telemetry is available, the following should be reviewed automatically or during normal operator monitoring device online/offline state; last successful communication time; unexpected reboot frequency; sensor health states; missing or invalid measurements; local storage state; time synchronization status; battery or power-health indicators available to software; solar or charging behavior where telemetry exists; module presence; firmware and configuration version; and persistent warnings or error counters.

A remote health warning should create a maintenance action when it persists, repeats or affects monitoring confidence.

## Scheduled site visit

A normal site visit should include the following stages.

### 1. Pre-visit review

Before travelling to the site review recent device health; inspect recent alerts; identify missing data periods; note repeated sensor or network failures; confirm current hardware, firmware and configuration revisions; and prepare approved spare parts and tools if a likely fault is already known.

This avoids unnecessary opening or removal of the unit.

### 2. Installation condition

Before touching ORIGIN, inspect the installation in place.

Check for visible displacement; leaning or rotation; loosened mounting hardware; damage caused by visitors, animals or maintenance activity around the site; obstruction of sensor openings; vegetation growth around the unit; dirt, mud, dust, insects or debris; signs of water flow or standing water; and changed surroundings that may affect sensing.

Take comparison photographs where practical.

### 3. Enclosure exterior

Inspect cracks; warping; impact marks; UV or weathering damage; loose panels; missing fasteners; deformation around access points; sensor aperture damage; cable-entry condition; and evidence of moisture pathways.

Damage to the enclosure should be evaluated not only cosmetically but for its effect on sensing, structure and environmental protection.

### 4. Sensor faces

For each sensor aperture or exposed sensing surface remove loose dirt using a method safe for the material; confirm the sensor is not physically displaced; check mounting fasteners; confirm there is no new obstruction; and inspect the opening for water or debris accumulation.

For the three mmWave sensors, preserve the commissioned orientation. Do not casually rotate a sensor during cleaning because small orientation changes can alter coverage.

### 5. Solar subsystem

Where the solar subsystem is installed, inspect panel surface cleanliness; panel damage; mounting stiffness; fasteners; all three supports; the hollow cable support and cable path; abrasion or pinching; water entry risk; and shading that did not exist during commissioning.

If the panel has shifted, its alignment should be restored and the power subsystem rechecked.

### 6. BIT and module interfaces

Inspect external module interfaces for mechanical damage; loose attachment; corrosion or contamination; cable strain; missing covers or protective parts; and unintended contact with soil or standing water.

BIT access should remain usable from the designed side position and should not be buried or blocked after installation changes.

## Cleaning

Cleaning should use the least aggressive method that is effective.

Avoid methods that may scratch sensing windows; force water into openings; damage seals; remove protective coatings; leave conductive residue; and chemically attack printed polymers or adhesives.

Do not use pressure washing on ORIGIN unless a future validated enclosure version explicitly permits it.

## Fastener checks

Fasteners should be checked for loss; looseness; corrosion; damaged threads; cracked mounting bosses; and excessive compression of printed or polymer parts.

Fasteners should not be repeatedly over-tightened as a preventive measure. Excessive torque can damage the enclosure, PCB mounts or seals.

Where a documented torque exists for a released design, use that value. If no validated torque is published, avoid inventing one in field documentation.

## Internal inspection

The enclosure does not need to be opened at every visit if remote health and external inspection show no reason to do so.

Opening is appropriate when there is evidence of moisture; power instability; loose internal hardware; damaged cabling; connector faults; sensor replacement need; battery concerns; and scheduled internal service.

Unnecessary opening increases the chance of contaminating the enclosure or damaging seals.

## Internal service checks

When the enclosure is opened safely, inspect Rosetta mounting; connectors; wiring strain relief; battery condition; signs of overheating; corrosion; condensation; foreign objects; loosened screws; damaged insulation; storage-media seating if serviceable; and module connections.

Any evidence of water inside the protected electronics area should be treated as a failure requiring investigation, not merely wiped away.

## Functional verification

Before leaving the site, perform a basic functional check.

Confirm normal startup; expected sensor health; each mmWave sensor communicates; environmental sensors produce valid data; module state is correct; communications recover; the device appears remotely under the correct identity; recent data reaches the expected destination; and no new persistent warnings are present.

If the installation was physically disturbed, repeat the affected calibration checks.

## After severe weather

A targeted inspection is recommended after conditions capable of exceeding the normal mechanical or environmental load of the installation.

Examples include severe storms; unusually high winds; flooding; hail; extreme heat; freezing conditions where relevant; and nearby construction or site maintenance.

The focus should be on mounting movement, water pathways, solar supports, cable damage and sensor alignment.

## After site changes

Even when ORIGIN itself has not changed, its environment may have.

Reassess if the site gains scaffolding; fencing; signs; new lighting or electrical equipment; vegetation; visitor barriers; storage objects; and new paths or traffic patterns.

Such changes may alter radar reflections, coverage or expected environmental baselines.

## Maintenance record

A routine visit should record at minimum:

```text
unit_id
site_id
date
reason
external_condition
mount_condition
sensor_condition
solar_condition
module_condition
internal_inspection_performed
health_check_result
cleaning_performed
parts_replaced
calibration_performed
follow_up_required
technician
```

Photographs can be especially useful for tracking gradual physical changes.

## Escalation criteria

Escalate from routine maintenance to diagnostics or repair if any of the following is found repeated device resets; damaged battery; internal moisture; structural cracking; loose sensor mounting that changes orientation; missing sensor communication; unstable power; persistent storage errors; repeated false detections after site changes; degraded cable insulation; damaged solar support; and unauthorized physical modification.

See [Diagnostics](diagnostics.md) and [Troubleshooting](troubleshooting.md).

## Return-to-service rule

Routine maintenance is complete only when:

1. the physical installation is secure;
2. no unresolved critical defect remains;
3. the unit reports expected health;
4. any disturbed sensor has been rechecked;
5. maintenance actions are documented;
6. the system is returned to the correct operational state.

For significant work, use the full [Commissioning](../installation-deployment/commissioning.md) procedure before returning the unit to normal monitoring.
