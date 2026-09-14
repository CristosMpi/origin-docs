# Firmware

ORIGIN firmware is the embedded runtime that turns Rosetta into a coordinated field device.

## Startup

On startup, firmware loads the active configuration, initializes required interfaces, identifies the expected sensors and modules, checks storage where used, establishes time handling, and reports the resulting device state.

## Sensor acquisition

Firmware collects data from the three C4001 radar channels, the LIS3DH, environmental sensors, and supported modules according to the active configuration. Each observation is associated with a stable source identity.

## Health supervision

The runtime maintains health information for important subsystems so an unavailable sensor, storage condition, communications interruption, or power-related state remains distinguishable from normal operation.

## Local records

Firmware can maintain local records for diagnostics and buffering according to the installed storage configuration. This supports continuity when the remote transport is temporarily unavailable.

## Configuration

Deployment-specific behavior is driven by configuration, including sensor enablement, acquisition timing, event thresholds, communication behavior, module selection, and calibration values.

## Recovery

Watchdog and recovery logic return the device to a known state after expected interruptions. Startup always rebuilds the system view from the active hardware and configuration rather than assuming that every previous subsystem state is still valid.

## Software identity

The active firmware version is reported as part of the unit's product information so maintenance and support can match the device with the correct documentation.
