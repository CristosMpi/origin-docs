# Schematics

The schematic is the authoritative electrical description of Rosetta. Gerbers show what copper and artwork were exported, but they do not replace a schematic for understanding connectivity, component values, rail intent or interface pinouts.

## Current documentation status

A complete Rosetta v2 schematic source has **not yet been added to this public documentation repository**. The Rosetta pages therefore document only information that is confirmed from project development history or the uploaded manufacturing export.

Exact pinouts, net names, component values and reference designators should be added only after the latest schematic source is committed and reviewed.

## Expected schematic blocks

The v2 schematic should be organized into recognizable blocks such as:

```text
Input / charging
Battery connections
Voltage regulation
ESP32 processor
Programming / boot control
LIS3DH accelerometer
SD storage
SIM / communications interface
External headers
Buttons / indicators
Protection and supporting passives
```

## Review checklist

Before a schematic is tagged for manufacturing, verify:

### Power

all supply pins are connected to the intended rail;.

decoupling capacitors are present and correctly valued;.

charger and regulator passive networks match the chosen operating point;.

ground domains are deliberate;.

connector polarities are unambiguous.

### Processor

boot-strapping pins are in valid states;.

programming/debug access exists;.

reset/enable behavior is correct;.

unused pins are intentionally handled.

### Peripherals

logic-voltage compatibility is verified;.

pull-ups/pull-downs are present where required;.

chip-select/address choices do not conflict;.

interrupt lines match firmware expectations.

### Connectors

pin numbering matches the footprint;.

pin 1 is visibly identifiable;.

external voltages cannot be accidentally applied to logic-only pins;.

connector names describe function.

## Design-review history

During Rosetta v2 development, several schematic/footprint areas required special attention, including component footprints, rail naming, connector assignments and passives around power circuitry. Examples discussed during review included items such as U6, VDD_1V8, J9–J11, L1/L2, J4 and C18.

These references are recorded here as **review-history markers**, not as proof that a current fault exists. They should be checked against the latest source before the design is released.

## Publishing the schematic

When the final schematic is added, this page should include source format and software version; PDF export; hardware revision; release date; sheet index; net/rail glossary; and links to the matching PCB and BOM release.

The schematic, PCB, BOM and firmware compatibility record should share one release identifier.
