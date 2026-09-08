# Microcontroller

Rosetta v2 is built around an **ESP32-family** embedded processor. The processor provides the local compute layer that connects physical electronics to ORIGIN firmware and higher-level software.

## Responsibilities

The processor is expected to coordinate:

- startup and self-checks;
- sensor initialization;
- data acquisition;
- local filtering and validation;
- storage operations;
- communications;
- configuration;
- watchdog and recovery behavior;
- diagnostic state reporting.

## Hardware identity

The exact ESP32 variant and module/footprint must be taken from the released schematic and BOM. Documentation should not assume pin compatibility between different ESP32 modules simply because they share the ESP32 name.

Before a production release, record:

| Item | Required release data |
| --- | --- |
| Device / module | Exact manufacturer part number |
| Package / module footprint | Exact PCB footprint |
| Flash / PSRAM | Fitted memory configuration |
| Logic voltage | Verified rail |
| Programming interface | Connector and pinout |
| Boot controls | Button / strap behavior |
| Firmware target | Build environment and board definition |

## Boot sequence

A controlled Rosetta firmware boot should follow a staged model:

```text
Reset / power-on
      ↓
Core rail validation assumptions
      ↓
Processor boot
      ↓
Non-volatile configuration load
      ↓
Storage initialization
      ↓
Peripheral initialization
      ↓
Communications initialization
      ↓
Health-state publication
      ↓
Normal monitoring loop
```

A peripheral failure should not necessarily prevent the entire board from booting. Wherever possible, firmware should enter a degraded but diagnosable mode.

## Pin management

Pin assignments are part of the hardware/firmware interface and must be version-controlled. The firmware should avoid unexplained numeric GPIO references spread throughout the codebase.

Prefer named definitions such as:

```text
PIN_RADAR_A_RX
PIN_SD_CS
PIN_STATUS_LED
PIN_ACCEL_INT
```

The exact names and numbers will be documented once the v2 schematic is committed to the docs source.

## Reset and watchdog behavior

Field electronics must recover from temporary faults. Firmware should therefore define:

- what triggers a software restart;
- what triggers the hardware watchdog;
- which state is retained across restart;
- how repeated boot loops are detected;
- how a failed peripheral is quarantined;
- how restart reasons are logged.

## Development and production firmware

Rosetta should separate development-only behavior from production behavior. Debug logging, test loops and permissive fallback settings are useful during bring-up but should not silently remain enabled in deployment builds.

## Security considerations

The processor is part of ORIGIN’s trust boundary. Firmware release procedures should include control of:

- source version;
- build configuration;
- credentials and secrets;
- update mechanism;
- debug interfaces;
- recovery method.

More detail belongs in [Software](../software/README.md) and [Centaurus AI → Cybersecurity](../centaurus-ai/cybersecurity.md).