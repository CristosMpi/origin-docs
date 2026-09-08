# Power Management

Rosetta’s power subsystem converts external energy and battery energy into stable rails for the processor, storage and peripherals. Power integrity is one of the most important parts of board bring-up because unstable rails can appear as software, sensor or communication faults.

## Confirmed design components

Rosetta v2 development includes:

- **BQ24074RGT** — battery charger / power-path controller;
- **TPS63031DSK** — buck-boost regulator.

The exact resistor network, current limits, rail values and enable behavior must be taken from the final schematic rather than inferred from reference designs.

## Functional model

```text
External input
     │
     ▼
BQ24074 power-path / charging stage
     │
     ├────────► Battery
     │
     ▼
System power node
     │
     ▼
TPS63031 regulation stage
     │
     ▼
Regulated electronics rail(s)
```

This diagram describes the intended functional relationship, not the complete schematic.

## Battery interface

The v2 design history includes dedicated 1×02 battery connectors. Before release, the connector documentation must define:

- polarity;
- connector family;
- allowed battery chemistry;
- nominal and maximum voltage;
- current rating;
- whether both connectors are equivalent or have different roles.

Never infer connector polarity from physical orientation alone.

## Charging and input power

A charger IC only works safely when its surrounding design is correct. Release review should verify:

- input-voltage range;
- charge-current programming;
- thermal design;
- battery-temperature assumptions if applicable;
- input-current limits;
- system load sharing;
- status outputs;
- reverse-current behavior.

## Buck-boost regulation

The TPS63031 stage allows the regulated rail to remain controlled across a battery/input range that may pass above and below the target output voltage. The board-level design still needs correct inductors, capacitors, layout and feedback/control configuration.

The exact L1/L2 implementation should be verified in the released schematic and PCB, because inductor footprints and routing were among the areas reviewed during v2 development.

## Bring-up measurements

Before installing sensitive peripherals, the following should be measured with a current-limited supply:

| Check | Expected result |
| --- | --- |
| Input-to-ground resistance | No obvious short |
| Battery polarity | Matches schematic and connector marking |
| Charger system node | Stable and plausible |
| Regulator output | Matches released schematic target |
| Idle current | Consistent with expected unprogrammed/boot state |
| Thermal behavior | No component rapidly overheating |

Exact voltage and current acceptance ranges should be added once the final schematic values are released.

## Power-state observability

Firmware should expose useful power diagnostics where the hardware permits it. Examples include charger status, low-battery state, brownout/restart reason and external-power presence.

## Failure patterns

Power faults often appear indirectly:

- repeated ESP32 resets;
- corrupted SD writes;
- sensors disappearing under load;
- communications failing only during transmission;
- regulator or charger overheating;
- board working from bench power but not from battery.

For systematic diagnosis see [Troubleshooting](troubleshooting.md).