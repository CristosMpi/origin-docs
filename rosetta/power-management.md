# Power Management

Rosetta's power subsystem is designed to keep ORIGIN Core stable across battery operation, charging, external energy input, and changing peripheral load.

## Main components

The architecture uses the **BQ24074RGT** for battery charging and power-path functions and the **TPS63031DSK** for regulated conversion. Together they provide the foundation for a compact field-oriented energy system.

## Battery and external energy

Rosetta supports a rechargeable battery architecture and can be integrated with an external source such as the ORIGIN solar subsystem. The exact energy profile depends on the deployment configuration and enabled peripherals.

## Stable rails

The processor, storage, sensors, and communications hardware require stable supply rails. Rosetta therefore separates power conversion from the application logic and allows software to interpret available power-health information where supported.

## Power-aware operation

ORIGIN software can use power state when scheduling communications, sensing, maintenance alerts, or reduced-energy behavior. This is particularly useful in solar-assisted or remote deployments.

## User interpretation

Power information should be read as part of overall device health. A communications interruption, sensor restart, or reduced activity can have a different meaning depending on the available energy state.

See [ORIGIN Core → Power System](../origin-core/power-system.md) for the system-level view and [Solar System](../mechanical-design/solar-system.md) for the mechanical energy-input architecture.
