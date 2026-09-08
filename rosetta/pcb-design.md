# PCB Design

This page records what can be verified directly from the Rosetta v2 Gerber manufacturing export and highlights the design items that still require source-level review.

## Verified board data

From the uploaded `Rosetta_V2_Reviewed (1)-job.gbrjob` file:

| Property | Value |
| --- | --- |
| PCB tool | KiCad Pcbnew 10.0.1 |
| Export date | 18 July 2026 |
| Layer count | 2 copper layers |
| Reported size | 100.05 × 104.8 mm |
| Board thickness | 1.6 mm |
| Dielectric | FR-4 |
| Top copper | 0.035 mm |
| Bottom copper | 0.035 mm |
| Top solder mask metadata | 0.01 mm |
| Bottom solder mask metadata | 0.01 mm |
| Surface finish | Not specified |

## Exported design rules

The job file reports these outer-layer constraints:

| Rule | Exported minimum |
| --- | ---: |
| Pad-to-pad | 0.20 mm |
| Pad-to-track | 0.20 mm |
| Track-to-track | 0.20 mm |
| Minimum line width | 0.20 mm |

These values describe the design-rule metadata in the export. The selected PCB manufacturer must still confirm that the chosen production process supports them.

## Layer stack

The Gerber job describes the stack in this order:

```text
Top silkscreen
Top paste
Top solder mask
F.Cu — 35 μm
FR-4 dielectric — 1.51 mm metadata
B.Cu — 35 μm
Bottom solder mask
Bottom paste
Bottom silkscreen
```

The nominal overall board thickness is 1.6 mm.

## Board profile

The Edge.Cuts Gerber contains a circular profile with a nominal 100 mm diameter and a smaller rectangular closed profile approximately 22 × 6.79 mm near the upper edge. Together, the job file reports a 100.05 × 104.8 mm bounding box.

Because the closed contours meet or overlap around the upper area, the final board outline should be inspected in the manufacturer’s Gerber viewer before ordering. Ambiguous or overlapping Edge.Cuts can result in an unintended board outline or cut-out.

## Placement and routing priorities

The Rosetta layout should prioritize:

- short, low-impedance power paths;
- correct regulator/charger component placement;
- local decoupling at IC power pins;
- uninterrupted return paths where possible;
- separation of noisy switching nodes from sensitive signals;
- accessible connectors;
- mechanically sensible connector orientation;
- clear silkscreen labeling;
- mounting and enclosure clearances.

## Power-layout sensitivity

Switching converters are especially sensitive to layout. The TPS63031 power loop, inductors and decoupling network should be reviewed against the device layout guidance in the final source design.

## Silkscreen

The export includes front and back silkscreen layers. Production review should verify that:

- reference designators remain readable;
- polarity markers are visible;
- connector pin 1 is clear;
- logos do not cover pads or manufacturing markings;
- text remains inside the finished board outline.

## DRC is necessary but not sufficient

A clean design-rule check does not prove that:

- a footprint matches the real component;
- a connector pinout is correct;
- a board outline is unambiguous;
- drill files were exported;
- power circuitry is electrically correct.

PCB release therefore requires both automated checks and human review.