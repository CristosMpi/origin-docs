# Rosetta v2

Rosetta v2 is the current electronics generation used by ORIGIN Core. It was designed to consolidate the functions that a field monitoring unit needs into a compact, serviceable platform.

## Hardware profile

Rosetta v2 uses a two-layer FR-4 PCB architecture with a nominal thickness of **1.6 mm** and an overall footprint of approximately **100 × 105 mm**. The board format is optimized for integration into the ORIGIN Core enclosure and for clear routing between power, processing, sensing, storage, and expansion functions.

## Functional blocks

The board architecture includes an ESP32-class embedded processor, power-path and battery-charging functions around the **BQ24074RGT**, regulated conversion around the **TPS63031DSK**, an **LIS3DH** three-axis accelerometer, local/removable storage support, communications-related interfaces, battery connections, external sensor connections, expansion headers, buttons, and status/control signals.

## Integration with ORIGIN Core

Rosetta does not operate as an isolated electronics board. Its connectors, mounting position, power behavior, sensor identities, and software configuration are coordinated with the enclosure and the rest of ORIGIN Core.

The three C4001 mmWave presence sensors are treated as directional sensing channels and are mounted mechanically so their physical orientation matches the software and deployment configuration.

## Version identity

A Rosetta v2 board is associated with its ORIGIN generation, enclosure revision, software version, configuration identity, and installed module set. This allows support and maintenance guidance to match the exact unit in service.
