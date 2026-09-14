# Rosetta

**Rosetta** is the custom electronics platform at the center of ORIGIN Core. It brings processing, power management, sensing interfaces, local storage, communications support, and expansion connectivity together on one coordinated board architecture.

The current documented generation is **Rosetta v2**.

## Role inside ORIGIN

Rosetta acts as the electrical bridge between the physical sensors and the ORIGIN software stack. It powers and supervises connected subsystems, provides the embedded processing environment, supports local data handling, and exposes the interfaces used by the enclosure and optional modules.

## Main functions

Rosetta v2 combines an ESP32-class embedded processor, battery and input-power management, regulated power conversion, LIS3DH motion/orientation sensing, storage-related interfaces, external sensor connections, communications-related interfaces, user/status signals, and expansion connectivity.

## Physical format

Rosetta v2 uses a compact two-layer PCB architecture with an overall footprint of roughly **100 × 105 mm** and a nominal board thickness of **1.6 mm**. Its geometry is designed to fit the vertically oriented ORIGIN Core enclosure while keeping connectors and service points accessible.

## Why a custom board matters

A custom electronics platform makes ORIGIN easier to integrate, configure, service, and reproduce than a collection of loosely connected development boards. Power paths, sensor connections, storage, processing, and expansion are organized around one system architecture.

Continue with [Rosetta v2](rosetta-v2.md), [Architecture](architecture.md), [Microcontroller](microcontroller.md), [Power Management](power-management.md), [Interfaces](interfaces.md), [Sensors](sensors.md), [Electrical Design](schematics.md), [PCB Design](pcb-design.md), [Components](bom.md), [Production & Quality](manufacturing.md), [Startup & Verification](assembly-and-bring-up.md), and [Diagnostics](troubleshooting.md).
