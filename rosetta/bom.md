# Bill of Materials

The Rosetta BOM identifies the components required to assemble a specific hardware revision. A production BOM must match the schematic and PCB source exactly.

## Current status

A final machine-readable Rosetta v2 BOM has not yet been added to this docs repository. The list below is a **verified partial design inventory** based on Rosetta v2 development information, not a purchase-ready BOM.

| Functional block | Part / item | Status |
| --- | --- | --- |
| Main processor | ESP32-family device/module | Exact variant to verify |
| Accelerometer | LIS3DH | Confirmed design component |
| Battery charger / power path | BQ24074RGT | Confirmed design component |
| Buck-boost regulation | TPS63031DSK | Confirmed design component |
| Battery connection | 1×02 connectors, two used in design | Exact connector family to verify |
| External interfaces | 1×03 headers, four used in design | Pinouts to verify |
| Storage | SD-card socket/interface | Exact socket to verify |
| SIM interface | micro-SIM/eSIM-related hardware | Final fitted option to verify |
| Power magnetics | Inductor components around regulator | Exact values/MPNs to verify |
| Passives | Resistors, capacitors, protection/support parts | Full values and quantities required |

## Required production-BOM fields

The released BOM should include at least reference designator; quantity; value/function; manufacturer; manufacturer part number; package/footprint; assembly side; DNP / fitted status; approved alternate part where relevant; and supplier part number where useful.

## Example release format

```text
Designator,Qty,Value,Manufacturer,MPN,Footprint,Fitted
U?,1,MCU.........,Yes
U?,1,LIS3DH.........,Yes
...
```

## DNP components

Do-not-populate options must be explicit. Leaving a footprint unpopulated because “the assembler will understand” is not a controlled manufacturing process.

## Alternate components

Alternates should only be approved after checking package and pin compatibility; voltage/current ratings; temperature range; electrical behavior; firmware implications; and lifecycle/availability.

## BOM-to-PCB verification

Before assembly, compare the BOM against:

1. schematic reference designators;
2. PCB footprints;
3. pick-and-place/position file;
4. assembly drawing;
5. manufacturer component substitutions.

The production BOM will replace this partial inventory once the final v2 source package is committed.
