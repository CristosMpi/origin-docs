# Troubleshooting

This page provides a symptom-based troubleshooting reference for deployed ORIGIN systems.

Troubleshooting should be used to narrow a problem quickly, but final repair decisions should still follow the evidence-driven process in [Diagnostics](diagnostics.md).

## Before troubleshooting

Before changing anything:

- record the unit and site ID;
- note the exact symptom;
- preserve available logs;
- record firmware and configuration versions;
- determine the last known-good time;
- check whether the problem affects one unit or several;
- inspect for recent site, weather, hardware or software changes.

Avoid immediately rebooting the device unless operational safety requires it.

---

## Unit is completely offline

### Possible causes

- battery depleted or disconnected;
- charging/solar input unavailable;
- power-management fault;
- damaged cable or connector;
- Rosetta not booting;
- severe internal moisture or physical damage.

### Checks

1. inspect the unit physically;
2. inspect battery and power connections;
3. check solar/input cabling;
4. verify whether the device shows any startup behavior;
5. inspect recent remote logs for the last reported power state or reset reason;
6. if safe, test power according to the Rosetta procedure.

### Escalate when

- the battery is damaged;
- power rails are unstable;
- there is internal moisture;
- Rosetta does not boot with a known-good power source.

---

## Unit repeatedly reboots

### Possible causes

- unstable input power;
- brownout;
- battery problem;
- firmware fault;
- peripheral fault during startup;
- storage issue;
- watchdog/reset loop.

### Checks

- record reset reason if available;
- note reboot interval;
- correlate resets with radio transmission, sensor initialization or storage access;
- compare behavior on known-good power where safe;
- inspect recent firmware/update history;
- disconnect only a suspected expansion module if the service process permits isolation.

A device in a reboot loop should not be considered healthy even if it periodically reconnects.

---

## One mmWave radar is missing

### Checks

1. confirm that the radar is enabled in configuration;
2. confirm logical sensor identity;
3. inspect its connector and cable;
4. verify mounting has not damaged the PCB or connector;
5. check the interface/driver state;
6. compare with another radar channel;
7. substitute a known-good sensor only after documenting the original behavior.

If the fault follows the sensor, replacement is likely appropriate. If it remains on the same channel, investigate the interface, cable, power or Rosetta connection.

---

## Radar reports too many detections

### Possible causes

- changed site geometry;
- moved sensor orientation;
- vegetation movement;
- activity outside the intended monitored area;
- reflective surfaces;
- new barriers/scaffolding;
- incorrect configuration;
- event-interpretation issue.

### Checks

- compare the current site with commissioning photographs;
- verify sensor orientation;
- inspect the sensing opening;
- identify which radar is producing the events;
- compare timing across the three radars;
- reproduce using controlled movement;
- review configuration changes;
- review higher-level Centaurus/rule interpretation only after raw radar behavior is understood.

Do not reduce sensitivity blindly to suppress alerts. That may create undetected areas.

---

## Radar fails to detect expected presence

### Checks

- confirm the correct radar channel is active;
- inspect orientation and obstruction;
- verify the target location is within the commissioned coverage map;
- repeat a controlled presence test;
- check whether enclosure parts or new objects block or alter the sensing geometry;
- compare raw sensor output with the system event layer.

Manufacturer sensor range is not the same as validated ORIGIN detection range.

---

## Environmental reading is implausible

### Checks

- inspect the sensor opening;
- check contamination or condensation;
- verify the reading is not stale;
- verify units and conversion;
- compare with a suitable reference instrument;
- examine whether the value is drifting, noisy or stuck;
- check configuration/calibration state.

A surprising reading may represent a real environmental condition, so verify with evidence before declaring the sensor faulty.

---

## All sensors are missing

### Possible causes

- shared power fault;
- common interface problem;
- firmware initialization failure;
- Rosetta fault;
- configuration corruption.

### Checks

- confirm Rosetta boot state;
- inspect shared power/connector paths;
- review firmware startup logs;
- verify configuration and expected sensor list;
- check whether any local peripheral remains visible.

When many independent sensors fail simultaneously, investigate shared infrastructure before replacing sensors.

---

## Module is attached but not detected

### Checks

- confirm the correct module is physically attached;
- inspect connector seating;
- verify power availability;
- confirm compatibility revision;
- inspect the expansion interface;
- check software module enumeration;
- test without the module to confirm ORIGIN Core remains healthy.

For BITs, also confirm the side-accessible interface has not been physically damaged or obstructed.

---

## Solar charging appears weak or absent

### Checks

- inspect panel cleanliness;
- inspect new shading;
- inspect panel orientation;
- inspect all three supports;
- inspect the hollow third support cable path;
- inspect cable continuity/connectors;
- verify charging-state telemetry if available;
- compare behavior across daylight conditions rather than one instant reading.

If the panel or support has shifted, restore geometry before evaluating electrical performance.

---

## Battery drains faster than expected

### Possible causes

- reduced charging input;
- battery degradation;
- abnormal radio activity;
- repeated rebooting;
- peripheral staying active;
- increased sampling/transmission configuration;
- temperature effects;
- battery damage.

### Checks

- inspect battery physically;
- review charging history;
- review reboot history;
- compare firmware/configuration with the known baseline;
- identify unusually high activity;
- evaluate actual energy behavior over a representative interval.

Do not publish a battery-life claim from one deployment unless it is supported by controlled validation.

---

## Device has local data but nothing appears remotely

### Checks

Follow the communications path in order:

1. local sensing works;
2. local event/storage works;
3. communication interface is recognized;
4. network link or registration exists;
5. transport connection succeeds;
6. authentication succeeds;
7. remote service accepts data;
8. operator interface maps data to the correct unit.

This prevents unnecessary hardware replacement during a backend or network outage.

---

## Remote dashboard shows the wrong unit or wrong data source

### Checks

- confirm physical unit ID;
- confirm configuration/provisioning identity;
- confirm module identity;
- inspect backend mapping;
- inspect timestamps;
- compare raw transmitted identity with displayed identity.

Treat identity mismatch as a data-integrity problem, not merely a cosmetic dashboard issue.

---

## Data timestamps are wrong

### Checks

- verify device time source;
- inspect time synchronization status;
- determine whether only remote display time is wrong;
- inspect timezone conversion outside the device where relevant;
- confirm buffered/offline records preserve original acquisition time.

Do not rewrite historical event time simply to match upload time.

---

## Storage errors or missing local records

### Checks

- inspect storage initialization;
- check available space;
- look for write failures;
- inspect whether power loss occurred during writes;
- preserve recoverable data;
- test read/write behavior before replacing or reformatting storage.

If records are corrupted, note the affected time range in the maintenance record.

---

## Device works after reboot but fault later returns

A reboot is not proof of repair.

### Action

- record the temporary recovery;
- compare time-to-failure;
- preserve logs before the next reboot;
- identify the recurring trigger;
- treat the issue as unresolved until root cause is identified or sufficient monitoring confirms stability.

---

## Internal condensation is found

### Action

1. remove the unit from normal service if electronics may be affected;
2. isolate power safely;
3. photograph the moisture pattern;
4. identify likely entry or condensation path;
5. inspect seals, cable entries and sensor openings;
6. inspect electronics for corrosion;
7. dry and repair only using an approved process;
8. re-test environmental protection and affected electronics.

Do not simply dry the enclosure and return it to service without investigating why moisture entered or formed.

---

## Water is present near a sensor opening but not electronics

Because ORIGIN includes intentional sensing openings, local water exposure may not necessarily mean the protected electronics compartment has failed.

Check:

- drainage behavior;
- opening geometry;
- water track direction;
- sensor condition;
- internal protected area;
- whether the installation angle has changed.

Record the condition and escalate to mechanical redesign if it recurs.

---

## Enclosure or mounting has cracked

### Action

- determine whether the crack affects structural stability;
- determine whether sensor orientation has changed;
- inspect nearby fasteners for over-compression;
- inspect for water pathways;
- compare against the released CAD/material/process;
- replace the affected part if necessary;
- repeat relevant mechanical and sensing checks.

Repeated cracks at the same feature should be treated as a design issue.

---

## Solar support is loose

### Action

- place the system in maintenance state;
- inspect all support attachment points;
- inspect the panel for secondary damage;
- inspect cable routing, especially through the hollow third support;
- restore released geometry;
- verify charging and mechanical stability.

Do not leave the panel supported by fewer structural elements than the released design.

---

## BIT interface is inaccessible after installation

The BIT interface is intended to remain accessible and should not be on the buried underside of a soil-mounted unit.

If access has been blocked:

- inspect whether the unit shifted;
- inspect whether soil, vegetation or another object obstructs the side interface;
- restore access without damaging the site;
- verify the connector after clearing the obstruction.

If the installation itself makes normal access impossible, revise the deployment arrangement rather than repeatedly excavating around the unit.

---

## Firmware update fails

### Checks

- verify image/version compatibility;
- verify power stability;
- verify communication stability if updating remotely;
- preserve the existing known-good firmware where rollback is supported;
- inspect update logs;
- do not repeatedly retry an update during unstable power.

After recovery, verify the running firmware and configuration versions explicitly.

See [Software → Updates](../software/updates.md).

---

## Configuration change causes abnormal behavior

### Action

- record the changed configuration version;
- compare with the last known-good configuration;
- restore the known-good configuration if safe;
- verify behavior;
- identify which parameter caused the change;
- repeat any calibration affected by thresholds, sensor mapping or orientation assumptions.

Configuration rollback should be documented just like firmware rollback.

---

## Centaurus produces an unexpected alert

### Checks

1. inspect the source event;
2. verify sensor health;
3. inspect raw measurements;
4. inspect event normalization;
5. check model/rule version;
6. inspect confidence and context;
7. compare with known limitations.

Do not modify AI/rule thresholds until the source data is confirmed valid.

See [Centaurus AI](../centaurus-ai/README.md).

---

## Several units at one site fail simultaneously

Prioritize shared causes:

- communications outage;
- backend outage;
- extreme weather;
- shared power infrastructure;
- environmental event;
- common firmware/configuration deployment.

The probability that several independent sensors fail identically at the same instant is generally lower than a shared-system cause.

---

## Fault cannot be reproduced

Record:

- exact original symptom;
- time;
- environmental conditions;
- logs;
- actions already taken;
- current state.

Then increase targeted monitoring rather than declaring success without evidence.

Intermittent faults are still faults.

## When to remove a unit from service

A unit should not be relied on for normal monitoring when there is:

- battery safety concern;
- exposed electrical conductor;
- unstable mounting;
- internal water exposure affecting electronics;
- repeated uncontrolled rebooting;
- inability to distinguish sensor failure from “no event”;
- unresolved identity/data-integrity problem;
- widespread invalid sensor data.

## After troubleshooting

Once the fault is corrected:

1. document the root cause and action;
2. verify the expected health state;
3. repeat affected calibration;
4. repeat affected commissioning checks;
5. confirm remote data flow;
6. return the unit to normal service only after the evidence supports it.

If the same failure appears across multiple units or revisions, create a development issue and feed the finding into the project roadmap rather than treating every occurrence as isolated maintenance.
