# Sensor System

ORIGIN Core uses a multi-sensor architecture. The goal is not to collect as many measurements as possible, but to combine sensing methods that provide useful and complementary information about the monitored site.

A sensor only becomes part of ORIGIN when its electrical, mechanical and software behavior is understood well enough for the system to distinguish a meaningful observation from a faulty or ambiguous reading.

## Sensor-system responsibilities

The sensor subsystem is responsible for acquiring physical measurements or detection events; exposing the health and availability of connected sensors; applying basic range and validity checks; converting raw outputs into consistent internal data; timestamping or ordering observations; making data available to local logic and higher-level software; and supporting calibration, testing and replacement.

The sensor layer should not silently hide uncertainty. If a device is disconnected, saturated, misconfigured or reporting implausible data, the system should treat that as a diagnostic condition rather than as a genuine environmental event.

## Sensor categories

ORIGIN groups sensing by function rather than by brand or connector type.

### Presence and movement

The current Core design uses long-range 24 GHz mmWave sensing for human-presence and motion-related monitoring.

Three DFRobot C4001 sensors are incorporated into the current enclosure concept so the Core can observe multiple directions. Their exact placement and orientation are part of the mechanical design because radar coverage is strongly affected by geometry and mounting.

See [Presence Detection](presence-detection.md).

### Environmental conditions

ORIGIN can support environmental sensors selected according to the risks relevant to a deployment. Depending on the site, this may include measurements such as temperature, relative humidity or other local environmental variables.

The exact environmental sensor set is deployment- and revision-dependent and should not be assumed from the architecture alone.

See [Environmental Monitoring](environmental-monitoring.md).

### Device-health sensing

Some measurements exist primarily to monitor ORIGIN itself rather than the heritage site.

Examples include supply or battery state; charging condition; communication status; sensor availability; internal fault indicators; and restart or watchdog information.

These signals are important because a monitoring device that cannot report its own failure can create false confidence.

### Expansion sensing

Modules such as BITs, Aqua Base and future attachments may introduce additional sensors. These should enter the system through defined interfaces rather than being handled as isolated special cases wherever possible.

## Current mmWave subsystem

The current mechanical design accommodates three **DFRobot C4001 24 GHz mmWave Human Presence Detection Sensors (SEN0609)**.

According to DFRobot's documentation for the 25 m version, the sensor uses 24 GHz FMCW radar, supports human-presence detection as well as motion/distance measurement, and is specified for presence detection up to 16 m and motion/distance measurement up to 25 m under the manufacturer's stated conditions.

Those manufacturer specifications are useful for component selection, but they are not automatically ORIGIN system specifications. Actual performance depends on mounting height; sensor orientation; surrounding materials; target direction; enclosure openings; site geometry; interference and reflections; firmware configuration; and the detection logic used above the sensor.

ORIGIN's validated detection performance should therefore come from its own test results rather than copying the sensor's maximum datasheet values into system-level claims.

## Data path

A generic sensor data path in ORIGIN is:

```text
Physical condition
      ↓
Sensor element
      ↓
Sensor interface / driver
      ↓
Raw reading or event
      ↓
Validation
      ↓
Normalized observation
      ↓
Local logic / storage / transmission
```

The validation stage is essential. It can include checks such as communication success; expected value range; stale-data detection; startup state; impossible transitions; known sensor error codes; and comparison against related system state.

## Polling and event-driven devices

Not every sensor should be handled in the same way.

Some sensors are naturally **polled**, meaning the controller requests a new measurement at a defined interval. Others can be **event-driven**, providing an output or message only when a condition changes.

The firmware should choose the method that best matches the device while keeping the rest of ORIGIN's data model consistent.

This matters for power consumption as well. A sensor that does not need constant high-rate sampling should not necessarily be operated that way in a battery-powered field device.

## Sampling strategy

Sampling rate should be selected according to what the measurement is meant to detect.

For example slowly changing environmental conditions may not need high-frequency sampling, presence or movement events may require much faster response, diagnostic measurements may be sampled periodically or when a fault occurs, and test modes may temporarily use higher rates than normal deployment.

ORIGIN should therefore use configuration-based sampling rather than one fixed rate for every sensor.

## Calibration

Calibration requirements vary by sensor.

A sensor may require factory calibration only; software offset correction; deployment-specific reference measurements; threshold tuning; physical alignment; and a site-specific baseline.

Calibration information should be stored with the deployment or test record so that later measurements can be interpreted correctly.

A sensor that has been repositioned may need to be treated as a new calibration state even if the hardware has not changed.

## Mounting and field of view

Sensor performance is partly a mechanical problem.

When placing a sensor, the design must consider whether structural parts block the field of view; whether the enclosure material attenuates or distorts the signal; whether cables or fasteners intrude into the sensing region; whether the mounting angle matches the monitored area; whether vibration or movement can change alignment; and whether maintenance can be performed without losing the original orientation.

For the mmWave subsystem, dedicated sensor openings are intentionally accepted in the current enclosure concept even though they complicate waterproofing. Sensing performance and environmental protection therefore have to be balanced through mechanical design rather than assuming the enclosure can be completely sealed with no effect on the sensors.

## Sensor identification

Multiple identical sensors should be distinguishable in software and documentation.

A useful naming convention is based on physical role rather than connection order alone, for example:

```text
PRESENCE_FRONT
PRESENCE_LEFT
PRESENCE_RIGHT
```

or another orientation that matches the final enclosure geometry.

This makes logs and fault reports understandable even after wiring or PCB revisions change the exact connector number.

## Failure handling

Sensor failures should be visible to the rest of the system.

Possible states include:

| State | Meaning |
| --- | --- |
| Healthy | Sensor responds and data passes checks |
| Degraded | Sensor works but quality or confidence is reduced |
| Missing | Sensor does not respond or is disconnected |
| Invalid | Sensor responds but data fails validation |
| Initializing | Sensor is not yet ready for normal operation |
| Disabled | Sensor is intentionally inactive by configuration |

These states allow ORIGIN to report the difference between "nothing detected" and "the detector is not working."

## Sensor fusion

Where multiple sensors observe related phenomena, higher-level software can combine them to improve context.

Sensor fusion in ORIGIN should not mean blindly averaging measurements. It can instead mean comparing independent observations; using one sensor to confirm another; correlating environmental conditions with detection events; recognizing when two sensors disagree; and increasing or reducing confidence according to available evidence.

More advanced interpretation belongs in [Centaurus AI](../centaurus-ai/README.md), while the Core remains responsible for delivering clean, well-described sensor data.

## Testing requirements

Every sensor integration should be tested at three levels:

1. **Component level** — confirm that the device operates according to its interface documentation.
2. **Subsystem level** — confirm reliable operation when connected to Rosetta and installed in the enclosure.
3. **Field level** — confirm that the complete ORIGIN unit produces useful results in a realistic environment.

Manufacturer specifications are not a substitute for the third level.

See [Testing & Validation](../testing-validation/README.md) for the project-wide testing framework.
