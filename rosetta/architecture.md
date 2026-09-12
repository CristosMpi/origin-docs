# Architecture

Rosetta is organized as a set of electrical subsystems connected around the embedded processor. Keeping these blocks conceptually separate makes schematic review, PCB debugging and firmware development easier.

## High-level block diagram

```text
                External / solar input
                         │
                         ▼
              Charging / power path
                         │
                 Battery interface
                         │
                         ▼
                Voltage regulation
                         │
          ┌──────────────┴──────────────┐
          ▼                             ▼
    Embedded processor            Peripheral rails
          │                             │
   ┌──────┼─────────┬──────────┐        │
   ▼      ▼         ▼          ▼        ▼
Sensors  Storage  Comms   Expansion   External sensors
```

## Processing block

The ESP32-family processor is the logical center of Rosetta. Firmware running on this device is responsible for coordinating peripherals, validating readings, maintaining system state and passing data to the higher ORIGIN software layers.

The processor should not be treated as the source of power integrity. It depends on the power subsystem being stable before firmware can operate correctly.

## Power block

Rosetta v2 design work includes two important power-management devices **BQ24074RGT** for battery charging / power-path functions and **TPS63031DSK** for regulated power conversion.

The final schematic determines exact rail names, current limits, resistor values and control connections. Those values should not be inferred from the IC names alone.

## Motion / board-state sensing

The design includes an **LIS3DH** accelerometer. At ORIGIN system level, an accelerometer can support board-orientation, movement or tamper-related observations, but the exact firmware behavior must be defined separately from the existence of the sensor.

## Storage and removable media

Rosetta development includes an SD-card interface so local logs or operational data can be retained when network connectivity is unavailable or when local diagnostics are required.

Storage should be treated as a managed subsystem with explicit mount, write, flush and error states rather than as permanently reliable memory.

## Cellular / SIM interface

The board design has also included micro-SIM/eSIM-related interface work. The presence of a SIM interface does not by itself mean the board contains a complete cellular modem. The modem, SIM routing, power requirements and firmware stack must be documented together before cellular connectivity is considered a released capability.

## External interfaces

Rosetta v2 has been designed with battery and expansion headers so that ORIGIN sensors and modules can be connected without soldering directly to the processor.

The final public pinout should only be published from the released schematic. Connector names that appeared during development, including several 1×03 headers and battery connectors, should be mapped to stable functional names before release.

## Separation of concerns

A useful design rule for Rosetta is to keep each failure domain identifiable:

| Subsystem | Typical failure symptom |
| --- | --- |
| Input / charging | Battery does not charge or system fails on external power |
| Regulation | Processor resets or rails are outside tolerance |
| Processor | No firmware boot or peripheral control |
| Storage | Logging failures or filesystem errors |
| Sensors | Missing, invalid or implausible readings |
| Communications | Data remains local or link cannot be established |
| Connectors | Intermittent or absent external-device operation |

This model is used in the [Assembly & Bring-up](assembly-and-bring-up.md) and [Troubleshooting](troubleshooting.md) procedures.

## Architecture principle

Rosetta should fail observably. A disconnected sensor, missing storage device or communication fault should become an explicit software state rather than silently becoming a normal-looking reading.
