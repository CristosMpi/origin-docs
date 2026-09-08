# Commissioning

Commissioning is the final technical acceptance stage before ORIGIN enters normal operation at a site.

It verifies the complete system under realistic conditions: physical installation, power, sensing, storage, communications, configuration, alert/event behavior, recovery from faults, and operator handover.

A unit should not be described as commissioned until the end-to-end monitoring path has been tested and any remaining limitations have been documented.

## Commissioning objectives

Commissioning should confirm that:

- the installation matches the approved site plan;
- the correct hardware and software versions are active;
- all required sensors and modules are healthy;
- the deployment configuration is correct;
- local storage is reliable;
- communications behave as intended;
- sensor events produce the expected software response;
- fault states are visible;
- the unit recovers correctly from expected interruptions;
- the site operator understands the system's normal and abnormal states.

## Configuration freeze

Before commissioning tests begin, record the exact configuration under test.

Capture:

- unit ID;
- Rosetta hardware revision;
- enclosure revision;
- firmware version;
- configuration version;
- module list;
- calibration revision;
- Centaurus model/rule version if used.

If any of these change during commissioning, note the change and repeat the affected tests.

## Physical acceptance

Inspect the installed hardware one final time.

Verify:

- mounting is secure;
- orientation matches the deployment record;
- radar openings are unobstructed;
- solar panel and supports are secure where used;
- cable routing is protected;
- service access remains possible;
- enclosure seams and penetrations are correctly closed;
- no component interferes with public access or heritage assets.

Photograph the accepted final state.

## Power acceptance

Confirm the system remains stable during realistic operation.

Check:

- boot from the intended supply;
- stable operation with all normal sensors enabled;
- battery/charging behavior where applicable;
- recovery after a controlled power cycle;
- correct reporting of low-power or power-related fault states where supported.

A system that repeatedly resets or only works from temporary workshop power should fail commissioning.

## Sensor acceptance

Run representative tests for every required sensing function.

For presence detection:

- trigger each radar from its intended area;
- verify correct sensor identity;
- verify expected event timing;
- test at least one known non-target area;
- verify a disconnected or failed sensor is reported as a fault rather than “no presence.”

For environmental sensing:

- verify all channels update;
- confirm readings remain plausible;
- confirm timestamps and sensor IDs are preserved;
- verify any configured alert logic with a safe simulated condition where practical.

## End-to-end event test

At least one controlled event should be followed through the complete pipeline.

Example:

```text
Known test stimulus
      ↓
Sensor detects condition
      ↓
Rosetta records observation
      ↓
Firmware produces event
      ↓
Local storage records event
      ↓
Communication sends event
      ↓
Upstream system receives event
      ↓
Operator can identify unit + source + time
```

Record the test event ID or timestamp so it can be traced across the system.

## Offline and reconnection test

If the deployment uses intermittent connectivity, intentionally test loss of the network path.

Verify that:

- the unit remains operational;
- sensor data is not silently discarded beyond documented limits;
- local buffering behaves as designed;
- health state shows the communication problem;
- reconnection occurs correctly;
- queued records are handled according to policy;
- duplicates or ordering issues are understood.

## Storage-failure awareness

Where practical, verify that storage failure is detectable.

The system should never indicate fully healthy monitoring if required records cannot be written.

Commissioning should confirm the operator can distinguish:

- healthy storage;
- storage nearly full;
- storage unavailable;
- data buffered for transmission;
- data successfully transmitted.

Exact indicators depend on the final software implementation.

## Restart and recovery

Perform at least one controlled restart.

After restart, verify:

- configuration is retained;
- unit identity is unchanged;
- sensors return to healthy state;
- communications reconnect;
- time is valid;
- local storage remains accessible;
- no false critical event is generated solely by startup unless startup-state alerts are intentionally configured.

## Fault-injection checks

Where safe, simulate selected failures to prove that ORIGIN exposes faults rather than hiding them.

Examples:

- disconnect one sensor;
- disable communications;
- temporarily remove network access;
- introduce an intentionally invalid configuration in a controlled test environment;
- simulate a module becoming unavailable.

Do not perform fault tests that could damage hardware or affect the protected site.

## Alert and decision review

For any rule-based or Centaurus-generated event used operationally, confirm:

- event source is visible;
- event severity is understandable;
- confidence is not confused with severity;
- operator can identify the supporting sensor observations;
- known false-positive cases are documented;
- no automated action is enabled beyond what has been explicitly approved and validated.

## Operator handover

Commissioning is incomplete until the responsible site operator has enough information to operate and escalate the system.

Handover should cover:

- normal health indicators;
- degraded/fault states;
- how to identify the unit;
- what to do after a power loss;
- what to do after a communications failure;
- how to report a sensor fault;
- maintenance access restrictions;
- whom to contact for support;
- which alerts require human verification.

## Acceptance categories

A commissioning result can be classified as:

### Accepted

All required functions pass and no unresolved critical issue remains.

### Accepted with limitations

The deployment is usable, but documented non-critical limitations remain. These limitations must be visible in the deployment record.

### Rework required

One or more required checks fail, but the problem can reasonably be corrected before operation.

### Rejected / rollback

The installation cannot currently meet the deployment objective safely or reliably and should not enter normal operation.

## Commissioning record

Record at minimum:

| Field | Record |
| --- | --- |
| Unit ID | Identifier |
| Site | Location |
| Date | Commissioning date |
| Hardware revision | Recorded |
| Firmware version | Recorded |
| Configuration version | Recorded |
| Calibration revision | Recorded |
| Physical inspection | Pass / fail |
| Power test | Pass / fail |
| Sensor test | Pass / fail |
| End-to-end event | Pass / fail |
| Offline/recovery test | Pass / fail / N/A |
| Restart test | Pass / fail |
| Outstanding issues | List |
| Acceptance | Accepted / limited / rework / rejected |
| Responsible personnel | Names/roles |

After successful commissioning, the deployment enters routine operation and maintenance. Use the [Deployment Checklist](deployment-checklist.md) as the field summary and see [Maintenance](../maintenance/README.md) for ongoing care.