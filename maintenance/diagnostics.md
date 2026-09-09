# Diagnostics

Diagnostics is the process of identifying the cause of abnormal ORIGIN behavior before a repair or replacement is performed.

The objective is to isolate faults logically, preserve evidence and avoid replacing healthy parts because of symptoms caused elsewhere in the system.

## Diagnostic principles

ORIGIN diagnostics follow six rules:

1. **start with evidence** rather than assumptions;
2. **change one variable at a time** where practical;
3. **preserve logs and configuration** before intervention;
4. **separate component failure from system-context failure**;
5. **do not represent unknown state as healthy state**;
6. **revalidate affected functions after repair**.

## Diagnostic layers

A useful sequence is:

```text
Site context
    ↓
Mechanical condition
    ↓
Power integrity
    ↓
Core electronics
    ↓
Sensor / module health
    ↓
Firmware and configuration
    ↓
Communications
    ↓
Data pipeline
    ↓
Higher-level analysis
```

Working from lower layers upward prevents a software symptom from hiding a power or mechanical cause.

## Step 1 — Define the symptom

Write down the actual observed problem.

Good examples:

- `RADAR_B has not produced valid data since 13:42`
- `device rebooted 7 times in 30 minutes`
- `unit is locally operational but remote data stopped`
- `battery state decreases during daylight despite solar exposure`
- `presence events increased after scaffolding was installed`

Avoid vague statements such as “the AI is broken” or “the sensor is bad.”

## Step 2 — Establish scope

Determine whether the issue affects:

- one sensor;
- one module;
- the Rosetta board;
- the power subsystem;
- one communications path;
- one unit;
- multiple units at the same site;
- the entire backend or data destination.

Scope is often the fastest way to distinguish a local hardware fault from a shared service failure.

## Step 3 — Preserve evidence

Before rebooting or replacing anything, save available evidence where possible:

- event logs;
- sensor-health logs;
- reboot reason;
- power telemetry;
- communication state;
- configuration version;
- firmware version;
- recent update history;
- timestamps of first and last known-good operation.

A reboot may temporarily hide the condition that caused the fault.

## Health-state model

Each subsystem should expose a state more expressive than a simple boolean.

Recommended states include:

| State | Meaning |
| --- | --- |
| Healthy | Expected communication and valid data |
| Initializing | Startup not yet complete |
| Degraded | Function remains but reliability is reduced |
| Missing | Expected device or data source is absent |
| Invalid | Data exists but fails validation |
| Disabled | Intentionally excluded |
| Fault | Confirmed failure requiring action |
| Unknown | State cannot currently be determined |

`Unknown`, `Missing` and `Invalid` must not be treated as equivalent to “no event detected.”

## Power diagnostics

Power faults can appear as sensor, software or network faults.

Check:

- battery connection;
- battery physical condition;
- charging-source availability;
- solar cable continuity where appropriate;
- abnormal connector heating;
- unexpected voltage drop;
- repeated brownout/reboot evidence;
- power-management status available through firmware;
- whether failures correlate with radio transmission, sensor activity or time of day.

If electrical measurement is required, use documented test points and safe procedures from the Rosetta hardware documentation.

See [Rosetta → Power Management](../rosetta/power-management.md).

## Boot and reset diagnostics

For unexpected reboots, determine:

- reset cause if available;
- time between resets;
- whether the unit reaches normal operation;
- whether one peripheral consistently fails during startup;
- whether the issue follows a firmware/configuration change;
- whether the issue occurs only under battery or solar operation;
- whether storage access precedes the reset.

Repeated rebooting should be treated as a degraded or out-of-service condition until understood.

## Sensor diagnostics

For a missing or abnormal sensor:

1. confirm the sensor is expected in the configuration;
2. verify physical connection;
3. inspect mounting and cable strain;
4. confirm power where applicable;
5. verify the interface responds;
6. validate returned data format;
7. compare with another known-good channel if possible;
8. restart only the affected driver or subsystem before rebooting the whole system where supported;
9. substitute a known-good sensor only after documenting the original state.

For the three mmWave channels, always preserve sensor identity so a failure does not become hidden by assigning a different sensor to the same logical channel without documentation.

## Radar-specific diagnostics

An mmWave sensor can be electrically healthy but operationally misleading because of installation changes.

Check:

- sensor orientation;
- sensor opening;
- nearby new structures;
- reflective surfaces;
- moving vegetation;
- objects outside the intended monitored area;
- mounting movement;
- configuration changes;
- whether the event is isolated to one radar or shared by several.

If false detections began after a site change, calibration and coverage should be reviewed before replacing hardware.

## Environmental-sensor diagnostics

For implausible environmental data:

- verify the sensor is physically exposed as intended;
- inspect contamination;
- check for condensation;
- compare against a reference instrument where available;
- determine whether the value is stuck, noisy, drifting or simply outside historical expectations;
- verify units and conversion logic;
- check time alignment.

Do not treat disagreement with expectation as proof of sensor failure without a reference measurement.

## Storage diagnostics

Investigate:

- storage present/absent state;
- mount or initialization success;
- available capacity;
- file-system errors;
- write failures;
- corrupt or incomplete records;
- repeated recovery behavior;
- whether power interruption occurred during writes.

Preserve recoverable data before reformatting or replacing storage.

## Communications diagnostics

Separate local device health from remote connectivity.

Check in this order:

1. device is running;
2. local data acquisition continues;
3. interface hardware is recognized;
4. network registration or link exists;
5. transport connection can be established;
6. authentication succeeds;
7. data is accepted by the remote service;
8. remote processing displays the unit correctly.

A backend outage should not be diagnosed as a Rosetta hardware fault.

## Configuration diagnostics

Verify:

- configuration version;
- expected unit identity;
- enabled sensors;
- thresholds;
- communication settings;
- module configuration;
- calibration values;
- compatibility with the running firmware.

A unit may behave “incorrectly” while doing exactly what an unintended configuration tells it to do.

## Firmware diagnostics

Determine:

- firmware version;
- update date;
- whether the issue began after an update;
- whether another unit on the same version shows the issue;
- whether rollback is available and safe;
- whether logs indicate driver or task failures.

Do not use firmware rollback as a substitute for preserving evidence.

## Module diagnostics

For BITs, Aqua Base, Drone Mount or future modules:

- confirm physical presence;
- verify module identity;
- confirm electrical interface;
- verify compatibility version;
- check software detection;
- inspect module-specific health;
- isolate the module to determine whether it affects the Core.

A malfunctioning expansion module should not be allowed to hide the health of ORIGIN Core itself.

## Data-pipeline diagnostics

When raw sensing appears correct but application behavior is wrong, trace one event through the pipeline:

```text
raw sensor data
→ local timestamp
→ validation
→ local event
→ storage
→ transmission
→ ingestion
→ processing
→ Centaurus / rules
→ operator-visible result
```

Record the last stage at which the event is known to be correct.

This turns a broad “data problem” into a bounded fault domain.

## Centaurus-related diagnostics

If higher-level analysis appears incorrect:

- confirm the raw source data first;
- verify missing/invalid inputs are represented correctly;
- verify model/rules version;
- review confidence and event context;
- determine whether the behavior is reproducible;
- compare with the documented expected interpretation;
- avoid changing model thresholds before confirming sensor integrity.

See [Centaurus AI → Limitations](../centaurus-ai/limitations.md).

## Known-good substitution

Substituting a known-good part is useful only when controlled.

Document:

- original part identity;
- original behavior;
- replacement identity;
- whether the fault follows the part or remains with the channel;
- final configuration.

If the fault remains after substitution, return attention to cabling, interface, power, firmware or system context.

## Diagnostic decision table

| Symptom | First areas to check |
| --- | --- |
| Unit completely offline | Power, boot state, physical damage |
| Frequent rebooting | Power integrity, reset cause, firmware, storage |
| One radar missing | Connection, power, interface, sensor identity |
| Radar false detections | Site change, orientation, opening, configuration |
| All sensors missing | Shared power, firmware, bus/interface, Rosetta |
| Valid local data but no remote data | Network, transport, authentication, backend |
| Wrong remote unit identity | Configuration, provisioning, backend mapping |
| Environmental values implausible | Exposure, contamination, units, reference check |
| Storage warnings | Capacity, file-system state, power interruption |
| Module not detected | Mechanical/electrical connection, compatibility, software |

## Escalation

Escalate to component replacement when a fault is isolated to a replaceable component and sufficient evidence supports that diagnosis.

Escalate to development when:

- multiple units show the same fault;
- failure follows a hardware or firmware revision;
- replacement does not resolve the issue;
- the fault represents a design weakness rather than random component failure;
- data integrity cannot be assured.

## Diagnostic record

Record:

```text
unit_id
site_id
symptom
first_observed
last_known_good
scope
firmware_version
configuration_version
health_states
evidence_preserved
tests_performed
results
fault_domain
root_cause
confidence_in_root_cause
action_taken
revalidation_required
```

## Completion criteria

Diagnostics is complete when one of the following is true:

- root cause is identified with sufficient confidence;
- the problem is narrowed to a defined subsystem requiring deeper engineering analysis;
- the symptom cannot be reproduced but evidence and monitoring actions are documented.

Do not label an unresolved fault “fixed” only because it temporarily disappeared after a reboot.
