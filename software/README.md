# Software

The ORIGIN software stack connects the physical monitoring hardware to the logic that turns sensor readings into useful, traceable information.

At the device level, software runs on the Rosetta electronics platform and is responsible for bringing hardware online, reading sensors, checking their health, applying configuration, recording observations, and preparing data for communication or higher-level processing.

At the system level, ORIGIN software also defines how observations are represented, how failures are distinguished from normal readings, how configuration is managed, and how data can be passed toward services such as Centaurus AI.

> **Current documentation status**
>
> This chapter documents the intended and currently known software architecture of ORIGIN. Exact repository paths, package names, protocol endpoints, credentials, production server addresses, and release procedures will be added only from the authoritative codebase and deployment configuration. They are intentionally not invented here.

## Responsibilities of the software stack

ORIGIN software is designed around six primary responsibilities:

1. **Hardware initialization** — bring Rosetta, sensors, storage, and communication interfaces into known states.
2. **Acquisition** — read sensor outputs using the correct timing and interface rules.
3. **Validation** — distinguish valid observations from missing, stale, malformed, or implausible data.
4. **Local decision support** — create structured events and apply device-level rules where appropriate.
5. **Communication** — package and transmit observations, status information, and events without losing the distinction between data and system health.
6. **Maintainability** — support configuration, diagnostics, version tracking, controlled updates, and recovery.

## Software layers

A useful conceptual view is:

```text
Applications / Operators / Centaurus AI
                ↑
       Event & data services
                ↑
      Communications layer
                ↑
   Device logic and validation
                ↑
      Sensor / device drivers
                ↑
          Rosetta hardware
```

The layers are deliberately separated so that a change in one sensor driver does not require redesigning the entire application, and a change in the remote service does not redefine how raw hardware is read.

## Device-side software

The embedded side of ORIGIN is centered on the ESP32-class controller integrated into Rosetta v2.

Its responsibilities include:

- startup and self-checks;
- interface initialization;
- sensor discovery and health state;
- periodic and event-driven acquisition;
- time association;
- local buffering where available;
- event creation;
- communication management;
- configuration loading;
- diagnostics;
- watchdog/recovery behavior;
- software-version reporting.

The exact firmware framework and source-tree organization will be documented after the firmware repository is connected.

## Observations are not the same as events

ORIGIN separates a **measurement** from an **event**.

A measurement is a sensor-derived observation such as a value, state, range, presence output, or health indication.

An event is a higher-level structured record indicating that something relevant happened or changed.

For example:

```text
Sensor reading
     ↓
Validation
     ↓
Observation
     ↓
Context / rule evaluation
     ↓
Event (when applicable)
```

This distinction keeps the system explainable. An operator should be able to understand what the sensor reported separately from what ORIGIN concluded from that report.

## Health is first-class data

A major software rule in ORIGIN is that missing data must never silently become a normal value.

For each important sensor or subsystem, software should be able to represent states such as:

- healthy;
- initializing;
- stale;
- communication failure;
- invalid data;
- disabled;
- unavailable.

A failed presence sensor, for example, must not be interpreted as "no person present." A failed environmental sensor must not be represented as a zero reading.

## Local resilience

ORIGIN is intended for field environments where communication may not always be continuously available.

The software architecture therefore favors local resilience:

- the device should continue core monitoring when remote connectivity is interrupted where technically possible;
- communication failure should create a health state, not crash acquisition;
- important observations should be buffered when storage permits;
- reconnection should not create uncontrolled duplicate events;
- restart behavior should return the device to a known state.

Exact buffering and retry behavior will be documented from the implemented firmware.

## Configuration over hard-coded behavior

Deployment-specific settings should be configuration rather than source-code edits whenever practical.

Examples include:

- device identity;
- site identity;
- enabled sensors;
- acquisition intervals;
- detection parameters;
- communication settings;
- logging level;
- feature flags;
- calibration values.

Secrets should not be committed to the public documentation repository.

See [Configuration](configuration.md).

## Data flow

At a high level:

```text
Physical environment
        ↓
Sensors
        ↓
Rosetta drivers
        ↓
Validation / health checks
        ↓
Normalized observations
        ↓
Local event logic
        ↓
Buffer / log / transport
        ↓
Remote processing or Centaurus AI
        ↓
Operator-facing information
```

See [Data Pipeline](data-pipeline.md) for the detailed model.

## Security philosophy

ORIGIN software should minimize trust in external input and avoid exposing unnecessary control surfaces.

The public docs will describe security architecture and responsible operating practices, but will not publish deployment secrets, active credentials, private keys, hidden administrative endpoints, or other information that would weaken deployed systems.

The higher-level security and AI design is documented under [Centaurus AI](../centaurus-ai/README.md).

## Versioning

Every deployed unit should make its software version identifiable.

A useful release record should associate:

- firmware version;
- hardware revision;
- configuration revision where appropriate;
- build or commit identifier;
- deployment date;
- compatibility notes.

This is necessary for diagnosing field behavior and reproducing test results.

## Chapter map

Continue with:

- [Architecture](architecture.md) — software layers and responsibilities;
- [Firmware](firmware.md) — embedded runtime structure and device behavior;
- [Installation](installation.md) — how software is prepared and loaded;
- [Configuration](configuration.md) — deployment and device settings;
- [Communications](communications.md) — transport principles and failure handling;
- [Data Pipeline](data-pipeline.md) — how readings become structured information;
- [Updates](updates.md) — safe software update and rollback principles.

For the electronics that host this software, see [Rosetta](../rosetta/README.md).