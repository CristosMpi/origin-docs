# Troubleshooting

Rosetta troubleshooting should proceed from power and physical assembly toward firmware and higher-level behavior. Changing several things at once makes faults harder to identify.

## Manufacturing package rejected or shows no holes

**Symptom:** board-house preview shows pads but no drill holes, or the manufacturer reports missing drill data.

**Current v2 export finding:** the reviewed Gerber ZIP contains copper, mask, paste, silkscreen, Edge.Cuts and `.gbrjob` files, but **no drill file**.

**Action:** regenerate KiCad fabrication outputs including Excellon plated/non-plated drill files as required, then inspect the manufacturer preview again.

## Board outline looks wrong

**Symptom:** manufacturer preview shows an unexpected cut-out, circular outline error or disconnected/overlapping profile.

**Cause to investigate:** the reviewed Edge.Cuts export contains a circular main contour and a smaller rectangular closed contour near the top. Their relationship must be intentional.

**Action:** open the PCB source and inspect Edge.Cuts for duplicate, intersecting or unintended closed shapes. Re-export after correction.

## Board does not power

Check in this order:

1. input polarity;
2. input voltage at connector;
3. resistance to ground with power removed;
4. charger/system node;
5. regulator input;
6. regulator output;
7. processor supply;
8. enable/reset conditions.

Do not begin by changing firmware if the processor rail is absent.

## Board immediately hits current limit

Remove power and inspect for solder bridges; reversed ICs; incorrect regulator/charger assembly; shorted capacitors; damaged components; and incorrect footprint-to-part mapping.

Use resistance measurements to isolate the shorted rail.

## Regulator output is incorrect

Verify exact fitted regulator part; inductor values and footprints; input voltage; surrounding capacitors; enable/control pins; solder quality; and PCB layout around the switching loop.

L1/L2 were among the areas that received attention during v2 design review and should be checked against the latest source.

## ESP32 does not program

Check correct programming connector/pinout; ground connection; logic-voltage level; reset/enable state; boot strap/button state; USB-UART or programmer operation; firmware board target; and processor orientation and soldering.

## ESP32 resets repeatedly

Possible causes include unstable regulated rail; insufficient current capability under load; brownout during radio transmission; watchdog restart; firmware crash; boot-strap pin conflict; and external peripheral pulling a critical line.

Capture the serial reset reason before changing hardware.

## Accelerometer not detected

Check LIS3DH power rail; bus pull-ups where required; address selection; CS/address pin state; SCL/SDA or SPI continuity; firmware bus configuration; and footprint orientation.

## SD card fails

Check socket soldering; card voltage; bus wiring; chip-select definition; card format; firmware filesystem handling; and power integrity during writes.

Test missing-card and card-insertion states separately.

## External sensor fails only when connected

Measure the header before connecting the sensor supply voltage, ground continuity, signal idle voltage, and pin order.

Then verify that the external module’s current draw and logic levels are compatible.

## Cellular/SIM path does not work

Do not troubleshoot only the SIM holder. Verify the complete chain:

```text
SIM/eSIM
   ↓
Modem / cellular hardware
   ↓
Power rail and peak-current capability
   ↓
UART/USB/other control interface
   ↓
Firmware driver
   ↓
Network configuration
```

## PCB assembly part does not fit footprint

Stop assembly and compare manufacturer package drawing, schematic symbol pin numbers, PCB footprint pad numbers, and physical part orientation.

Footprint mismatch is a source-design issue, not an assembly problem to solve by forcing the component onto the board.

## Revision confusion

Files such as `Reviewed (1)` are not sufficient release identifiers. If schematic, PCB, BOM and Gerbers cannot be proven to belong to the same revision, do not order or assemble the board until the release set is reconciled.

## Escalation rule

When troubleshooting, record exact board revision; measured values; firmware commit; test setup; and symptoms before and after each change.

A reproducible failure is much easier to fix than an undocumented one.
