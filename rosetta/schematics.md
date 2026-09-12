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

All supply pins are connected to the intended rail.

Decoupling capacitors are present and correctly valued.

Charger and regulator passive networks match the chosen operating point.

Ground domains are deliberate.

Connector polarities are unambiguous.

### Processor

Boot-strapping pins are in valid states.

Programming/debug access exists.

Reset/enable behavior is correct.

Unused pins are intentionally handled.

### Peripherals

Logic-voltage compatibility is verified.

Pull-ups/pull-downs are present where required.

Chip-select/address choices do not conflict.

Interrupt lines match firmware expectations.

### Connectors

Pin numbering matches the footprint.

Pin 1 is visibly identifiable.

External voltages cannot be accidentally applied to logic-only pins.

Connector names describe function.

## Design-review history

During Rosetta v2 development, several schematic/footprint areas required special attention, including component footprints, rail naming, connector assignments and passives around power circuitry. Examples discussed during review included items such as U6, VDD_1V8, J9–J11, L1/L2, J4 and C18.

These references are recorded here as **review-history markers**, not as proof that a current fault exists. They should be checked against the latest source before the design is released.

## Publishing the schematic

When the final schematic is added, this page should include source format and software version; PDF export; hardware revision; release date; sheet index; net/rail glossary; and links to the matching PCB and BOM release.

The schematic, PCB, BOM and firmware compatibility record should share one release identifier.
