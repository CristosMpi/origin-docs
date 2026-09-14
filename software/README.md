# Software

ORIGIN software coordinates the physical platform and turns sensor activity into structured, traceable information that users and higher-level services can understand.

## Device software

The embedded software running on Rosetta manages startup, hardware interfaces, sensor discovery, acquisition, timing, local state, storage, communications, configuration, diagnostics, watchdog behavior, and software identity.

## Structured observations

Raw readings are normalized into records with source identity, timestamp, measurement or event type, value, unit where applicable, and health information. This allows the wider ORIGIN system to understand not only what was measured, but where it came from and whether the source was healthy.

## Local resilience

Core monitoring is separated from remote connectivity. If a communications path becomes temporarily unavailable, the device can preserve meaningful local state and use buffering where supported by the installed configuration.

## Configuration-driven behavior

Site identity, enabled sensors, acquisition intervals, module selection, calibration values, event rules, communications behavior, and maintenance modes are controlled through configuration rather than requiring users to alter program code.

## Centaurus integration

Higher-level analysis is handled separately from deterministic device control. Centaurus consumes structured data and context while the embedded software remains responsible for the reliable operation of the physical unit.

Continue with [Architecture](architecture.md), [Firmware](firmware.md), [Installation](installation.md), [Configuration](configuration.md), [Communications](communications.md), [Data Pipeline](data-pipeline.md), and [Updates](updates.md).
