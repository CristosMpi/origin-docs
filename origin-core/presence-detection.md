# Presence Detection

Presence detection is one of ORIGIN Core's primary security-oriented sensing functions. The current design uses multiple long-range 24 GHz mmWave radar sensors so the system can detect human presence and motion without relying only on visible-light cameras or conventional passive-infrared sensing.

## Current sensor choice

The current enclosure concept is designed around three **DFRobot C4001 24 GHz mmWave Human Presence Detection Sensors (25 m version, SEN0609)**.

DFRobot specifies the 25 m version as an FMCW radar sensor with 24 GHz operating frequency; human-presence detection up to 16 m; motion and distance measurement up to 25 m; distance measurement from approximately 1.2 m to 25 m; velocity measurement support; a wide detection beam; and UART-based integration on the 25 m model.

Manufacturer documentation: https://wiki.dfrobot.com/sen0609

These are component specifications. They should **not** be presented as guaranteed ORIGIN system performance until the complete sensor, enclosure, mounting, firmware and site configuration have been validated together.

## Why mmWave

Millimeter-wave radar is useful for ORIGIN because it can detect movement and presence without depending on visible illumination.

Compared with some conventional occupancy technologies, mmWave can also detect smaller movements and can continue detecting a person who is relatively still.

This is relevant to heritage monitoring because a system should not assume that a person is absent simply because they are not moving enough to trigger a basic motion detector.

## Multi-direction architecture

The current mechanical design includes three C4001 modules rather than a single radar.

The goal is to provide multiple sensing directions around the Core.

A conceptual arrangement is:

```text
             Sensor A
                ↑
                │
Sensor B  ←  ORIGIN Core  →  Sensor C
```

The exact angles and orientation depend on the final enclosure geometry and deployment requirements.

The three-sensor approach introduces additional engineering requirements each sensor must have a stable physical orientation; the firmware must identify which sensor generated an event; overlapping detection regions must be understood; blind zones should be measured rather than assumed; sensor outputs should be time-correlated; and reflections and cross-site geometry should be considered during testing.

## Enclosure integration

Radar performance is influenced by the material and geometry in front of the sensor.

For this reason, the current ORIGIN enclosure concept intentionally includes dedicated sensor openings. This can reduce the protection provided by a completely sealed shell, but it avoids designing the sensing system around an unverified assumption that the radar will perform identically through every enclosure material and wall thickness.

This creates a deliberate mechanical trade-off between sensing performance; environmental protection; structural integrity; appearance; and manufacturing simplicity.

The final solution should be validated with the sensors installed in the actual enclosure rather than only tested on a workbench.

## Sensor mounting

The C4001 modules include mounting holes, which are intended to be integrated into the mechanical design so each radar has a defined and repeatable position.

A good mount should prevent the board from rotating; avoid mechanical stress on the PCB; keep the sensing face unobstructed; provide access to the connector; keep fasteners clear of the sensing region where possible; and allow replacement without redesigning the enclosure.

See [Mechanical Design → Sensor Mounting](../mechanical-design/sensor-mounting.md).

## Detection modes

At system level, ORIGIN can distinguish several related concepts.

### Presence

A person may be present even if movement is small.

Presence information is useful when the objective is to determine whether someone remains inside a monitored area.

### Motion

Motion information describes detected movement and may be used for faster event response or tracking changes in activity.

### Distance

Where the sensor output and firmware mode support it, distance can provide additional context about how far a detected target is from the sensor.

### Velocity

Velocity information may be available from the sensor and can contribute additional context in test or future interpretation logic.

ORIGIN should keep these concepts separate rather than converting every radar output into a single generic "motion" flag.

## Event pipeline

A simplified presence-event pipeline is:

```text
Radar return
    ↓
C4001 processing
    ↓
Sensor output / data
    ↓
Rosetta driver
    ↓
Validity checks
    ↓
Per-sensor observation
    ↓
Multi-sensor event logic
    ↓
Local record / transmission / higher-level analysis
```

The distinction between sensor output and system event is important. A sensor may report activity, but ORIGIN firmware and higher-level software decide how that observation is represented and whether it contributes to an alert.

## Sensor identity

Each radar should have a stable logical identity based on position.

The final naming convention should match the enclosure geometry, for example:

```text
RADAR_A
RADAR_B
RADAR_C
```

or direction-based names once the final orientation is fixed.

Logs should always identify the source radar so test results and real events can be analyzed later.

## Overlap and blind zones

Using multiple radars does not automatically produce complete 360-degree coverage.

The real coverage depends on the manufacturer's beam pattern; mounting angle; mounting height; distance from the monitored area; surrounding walls and objects; target direction; reflections; and enclosure geometry.

ORIGIN should therefore maintain a tested coverage map for each standard deployment arrangement.

A useful validation procedure is to divide the monitored area into test positions and record whether each radar detects stationary presence; slow movement; normal walking; approach and departure; and targets near the edge of the expected field of view.

## False detections and ambiguity

Radar is not perfect. A presence subsystem may be affected by movement outside the intended monitored zone; reflections from surrounding surfaces; movement behind materials the radar can penetrate; nearby machinery or moving objects; sensor configuration; and unusual mounting conditions.

For that reason, ORIGIN should not describe a single radar detection as proof of unauthorized activity.

Higher-level event logic can use context such as which sensor detected the target; duration of presence; repeated observations; distance trend; time of day or site state; related sensors; and operator-defined rules.

## Privacy-oriented design

One advantage of radar-based presence sensing is that it does not inherently require capturing a recognizable image of a person in order to detect occupancy or motion.

This can be useful at sites where the system needs awareness of human activity but where continuous camera recording would introduce additional privacy, storage and operational concerns.

This does not mean mmWave sensing is automatically privacy-neutral. Presence and movement data can still be sensitive and should be handled according to the deployment's policies and applicable requirements.

## Failure states

The system should distinguish at least:

| State | Meaning |
| --- | --- |
| No presence | Sensor is healthy and reports no relevant target |
| Presence detected | Sensor is healthy and reports presence |
| Motion detected | Sensor reports movement according to configured mode |
| Initializing | Sensor is not ready for normal interpretation |
| Missing | No valid communication or expected signal from sensor |
| Invalid | Data is received but fails software validation |
| Disabled | Sensor is intentionally excluded from active monitoring |

A failed radar must never be represented as simply "no person detected."

## Startup behavior

Sensors may need a defined initialization sequence before their output is trusted.

Firmware should therefore:

1. power or initialize the radar;
2. configure the required operating mode;
3. confirm communication;
4. allow any required startup period;
5. mark the sensor healthy only after valid data is observed.

This prevents startup transients from becoming false alerts.

## Testing plan

Presence detection should be validated in stages.

### Bench testing

Confirm reliable electrical communication; configuration commands; stable repeated readings; expected event output; and recovery after restart or disconnect.

### Enclosure testing

Repeat detection tests with the sensor mounted in the real Core enclosure.

This verifies opening geometry; mounting angle; fastener effects; cable routing; and mechanical stability.

### Coverage testing

Measure detection across known positions and directions.

### Multi-sensor testing

Evaluate overlapping detection; simultaneous events; sensor identity in logs; disagreement between radars; and event ordering.

### Field testing

Test at realistic heritage-site distances and geometry, with the unit mounted in its intended position.

## Performance claims

ORIGIN documentation should use two different types of values:

### Component specification

Values published by DFRobot for the C4001 sensor.

### ORIGIN validated performance

Values measured with the complete ORIGIN Core in a documented test setup.

Only the second category should be used to make claims about how far or how reliably **ORIGIN itself** detects people in a deployment.

Validated results will be published under [Testing & Validation](../testing-validation/README.md).

## Related documentation

See [Sensor System](sensor-system.md); [Hardware Architecture](hardware-architecture.md); [Mechanical Design → Sensor Mounting](../mechanical-design/sensor-mounting.md); [Software](../software/README.md); [Centaurus AI](../centaurus-ai/README.md); and [Testing & Validation](../testing-validation/README.md).
