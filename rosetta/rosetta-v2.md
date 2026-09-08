# Rosetta v2

Rosetta v2 is the current electronics revision documented for Project ORIGIN. It is the board generation around which the present ORIGIN Core mechanical and embedded architecture is being developed.

## Verified manufacturing-export metadata

The uploaded Gerber archive contains a KiCad Gerber job file with the following metadata:

| Property | Exported value |
| --- | --- |
| Project name | `Rosetta_V2_Reviewed (1)` |
| Generator | KiCad Pcbnew 10.0.1 |
| Creation date | 18 July 2026, 17:50:40 +03:00 |
| Copper layers | 2 |
| Overall reported size | 100.05 × 104.8 mm |
| Board thickness | 1.6 mm |
| Base dielectric | FR-4 |
| Outer copper thickness | 0.035 mm per side |
| Finish | Not specified in job file |
| Revision field | `rev?` |

The `rev?` revision field is a release-management warning: future fabrication packages should contain a definite hardware revision identifier.

## Exported layer set

The archive contains:

- front copper;
- back copper;
- front solder mask;
- back solder mask;
- front solder paste;
- back solder paste;
- front silkscreen;
- back silkscreen;
- board profile / Edge.Cuts;
- Gerber job metadata.

The archive does **not** contain an Excellon drill file. This means the package should not be considered a complete fabrication release where plated or non-plated holes are required.

## Functional design

Rosetta v2 development has included the following main blocks:

- an ESP32-family embedded processor;
- battery charging and power-path management around the BQ24074RGT;
- regulated power conversion around the TPS63031DSK;
- an LIS3DH accelerometer;
- removable/local storage interfaces;
- cellular/SIM-related interface work;
- battery and external expansion connectors;
- status, button and supporting passive circuitry.

The exact final reference designators, pin assignments and fitted options must be verified against the latest schematic and BOM before they are published as production data.

## Mechanical envelope

The Gerber profile indicates a predominantly circular main outline with a nominal diameter of approximately 100 mm, plus a smaller rectangular profile feature near the top of the board. Taken together, the job file reports a 100.05 × 104.8 mm bounding size.

Because the profile contains more than one closed contour and the contours interact near the upper edge, the fabrication preview should be checked carefully before release. A board house must interpret the intended outer perimeter and any cut-out correctly.

## Why v2 exists

Rosetta v2 is not just a cosmetic PCB revision. It represents the move toward a board that is designed around the requirements of the full ORIGIN Core:

- compact integration inside the enclosure;
- repeatable external sensor wiring;
- managed battery operation;
- local processing and storage;
- future expansion without rewiring the entire system;
- fabrication by standard PCB manufacturers.

## Release state

The current v2 export is useful as an engineering snapshot, but it should be considered **pre-production** until all of the following are complete:

- schematic review;
- final PCB design-rule check;
- drill-file export and verification;
- BOM verification;
- component-position / assembly-file verification where assembly is outsourced;
- fabrication preview review;
- first-article electrical bring-up;
- functional firmware testing;
- enclosure fit test;
- versioned release archive.

## Recommended release naming

Instead of filenames such as `Reviewed (1)`, a production release should use a stable naming convention, for example:

```text
rosetta-v2.0/
├── source/
├── gerber/
├── drill/
├── bom/
├── assembly/
├── drawings/
└── RELEASE.md
```

Each release should state the board revision, date, commit or source-file identifier, firmware compatibility and known limitations.

## Related pages

See [Architecture](architecture.md), [PCB Design](pcb-design.md), [Manufacturing](manufacturing.md) and [Assembly & Bring-up](assembly-and-bring-up.md).