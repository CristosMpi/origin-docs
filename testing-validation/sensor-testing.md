# Sensor Testing

Sensor testing verifies that ORIGIN's sensing layer produces useful, distinguishable and repeatable observations under the conditions in which the system is intended to operate.

The objective is not merely to confirm that a sensor returns data. The test program must also examine range, repeatability, mounting effects, blind zones, failure states and the difference between raw sensor output and a system-level event.

## Scope

Sensor validation may include electrical communication; startup behavior; stable repeated readings; calibration where relevant; missing-device detection; invalid-data handling; enclosure effects; mounting-angle effects; coverage mapping; false detections; multi-sensor interaction; and field behavior.

## Test configuration

Every sensor result should identify:

```text
Sensor model
Sensor identifier
Firmware version
Configuration/profile
Mechanical mounting revision
Mounting height
Orientation
Enclosure revision
Test environment
```

This is particularly important for mmWave sensors because physical geometry can materially affect observed coverage.

## Communication validation

For each sensor channel:

1. power the system;
2. verify that the sensor initializes;
3. confirm valid communication;
4. record multiple readings or events;
5. disconnect the sensor deliberately;
6. verify that the system reports a missing/fault state;
7. reconnect it;
8. confirm recovery.

A disconnected sensor must never appear as a valid zero or "nothing detected" state.

## Stable identity

Each sensor should have a stable logical identity.

For the three current mmWave channels, identifiers such as:

```text
RADAR_A
RADAR_B
RADAR_C
```

may be used until final direction-based names are fixed.

Logs must preserve the source identity so that coverage and false detections can be traced to a physical sensor.

## mmWave presence-detection testing

The current ORIGIN Core mechanical concept uses three DFRobot C4001 24 GHz mmWave sensors.

Manufacturer specifications describe component capabilities, but ORIGIN must validate its own performance with sensors installed in the final or representative enclosure.

### Bench test

Verify startup; UART/data communication as applicable; presence event output; motion response; distance output where used; repeated detection; and restart recovery.

### Installed-enclosure test

Repeat the test after installing the sensor behind the real mechanical interface.

Compare the result with the bench setup to identify effects from sensor opening geometry; wall material; nearby fasteners; internal structure; cable routing; and mounting angle.

## Coverage mapping

A coverage map should be measured rather than inferred from a datasheet illustration.

A practical method is to establish a grid or marked route around the unit.

At each position record distance from sensor; angle or direction; target state; sensor(s) detecting the target; detection latency if relevant; repeated-trial count; and anomalies.

Suggested target states include normal walking; slow walking; approach; departure; standing relatively still; and edge-of-zone movement.

## Multi-radar testing

Three radars introduce system-level behavior that cannot be tested with one sensor alone.

Tests should examine simultaneous detections; overlap regions; disagreement between radars; event ordering; source identity; blind zones; and detection outside the intended monitored area.

The presence of three sensors should not be described as guaranteed 360-degree coverage until measured coverage supports that claim.

## False-detection testing

False positives should be actively investigated.

Potential sources may include people outside the intended zone; movement behind penetrable materials; reflections; nearby machinery; moving vegetation or objects; unusual geometry; and configuration sensitivity.

Record false detections rather than tuning them away without evidence.

A useful record contains:

```text
Observed event
Actual situation
Sensor source
Duration
Distance / zone
Environmental context
Configuration
Reproducible? yes/no
```

## False-negative testing

A false negative occurs when a relevant target or condition is present but the expected sensor observation does not occur.

For presence sensing, test difficult cases such as low movement; edge of expected field; target partially obstructed; approach from different directions; and multiple people where appropriate.

## Environmental sensors

For environmental sensing, validation should include comparison with an appropriate reference where possible.

Examples may include temperature; humidity; pressure; water-related measurements; and other installed environmental channels.

For each channel record reference instrument; sensor reading; difference; ambient conditions; stabilization time; and repeated measurements.

Do not publish an accuracy figure unless the method and reference are adequate to support it.

## Accelerometer / motion sensor testing

Where the LIS3DH or another inertial sensor is used on the tested revision, verify device detection; axis response; orientation consistency; stationary baseline; repeatable movement detection; and restart behavior.

If it is used for tamper or movement events, validate the event threshold on the installed enclosure rather than only with the bare PCB.

## Sampling and timestamps

Sensor data should be checked for plausible timestamps; expected sampling interval; gaps; duplicate samples; stale values; impossible jumps; and source identity.

Timing errors can create misleading higher-level analysis even when the sensor itself is operating correctly.

## Sensor health states

The software should preserve states such as:

| State | Meaning |
| --- | --- |
| Healthy | Valid sensor communication/data |
| Initializing | Startup not complete |
| Missing | No expected communication |
| Invalid | Data present but not trustworthy |
| Disabled | Intentionally excluded |
| Degraded | Available with a known limitation |

Tests should exercise these states where practical.

## Calibration

Calibration procedures depend on the sensor type.

Calibration must not be treated as a universal one-time step. Relevant settings may depend on enclosure revision; mounting position; site geometry; firmware version; and sensor replacement.

See [Installation & Deployment → Calibration](../installation-deployment/calibration.md).

## Repeatability

For an important performance claim, repeat the same test under the same defined setup.

Record number of trials; number of successful observations; variation; failures; and anomalies.

Avoid reporting a single best-case result as representative performance.

## Regression testing

Re-test affected sensing functions after changes to sensor model; sensor firmware/configuration; physical angle; mounting height; enclosure openings; nearby structural elements; driver code; and event-processing logic.

## Example sensor-validation matrix

| Test | Current public status |
| --- | --- |
| Sensor communication | Procedure defined |
| Disconnect detection | Procedure defined |
| Reconnect recovery | Procedure defined |
| mmWave bench response | Results to be published from recorded test evidence |
| Installed-enclosure coverage | Validation required |
| Multi-radar overlap map | Validation required |
| False-positive characterization | Validation required |
| Environmental-sensor comparison | Revision-dependent |
| Health-state handling | Procedure defined |

## Evidence

Useful evidence includes coverage maps; event logs; timestamped datasets; test videos; photographs of sensor orientation; reference-distance markings; configuration files; and environmental reference readings.

## Related documentation

See [ORIGIN Core → Sensor System](../origin-core/sensor-system.md); [Presence Detection](../origin-core/presence-detection.md); [Rosetta Sensors](../rosetta/sensors.md); [Environmental Testing](environmental-testing.md); [Field Testing](field-testing.md); and [Validation Results](validation-results.md).
