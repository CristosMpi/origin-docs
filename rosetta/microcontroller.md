# Microcontroller

Rosetta v2 uses an **ESP32-class embedded controller** as the main processing element of ORIGIN Core.

## Responsibilities

The controller coordinates startup, sensor initialization, data acquisition, local validation, storage operations, communications, configuration, timing, watchdog behavior, and device-health reporting.

## Startup behavior

At startup, the controller loads the active configuration, initializes required interfaces, identifies connected sensors and modules, establishes local storage where used, and exposes the resulting health state to the software stack.

## Local resilience

ORIGIN is designed so temporary loss of a remote service does not automatically stop local sensing. The embedded controller maintains local device state and can preserve records according to the installed configuration.

## Sensor identity

Each important sensing channel is mapped to a logical identity. This means a physical sensor can be serviced or replaced without making historical records ambiguous.

## Security role

The embedded controller is also part of the system trust boundary. Device identity, configuration, credentials, update behavior, and access to protected functions are handled separately from public documentation and ordinary user-facing settings.
