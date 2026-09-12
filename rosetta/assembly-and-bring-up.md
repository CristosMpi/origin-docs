# Assembly & Bring-up

Bring-up is the controlled process used to determine whether a newly assembled Rosetta board is electrically safe and functionally correct before it is installed inside ORIGIN Core.

The main principle is simple: **do not connect everything and hope it boots**. Test the board in stages so that a failure can be localized.

## 1. Documentation match

Before powering the board, confirm that the physical PCB matches the intended release board revision; schematic revision; BOM revision; component-placement file; firmware target; and assembly notes.

## 2. Visual inspection

Inspect both sides under good lighting/magnification.

Look for solder bridges; tombstoned passives; missing components; reversed polarized parts; incorrect IC orientation; damaged pads; unsoldered pins; debris or solder balls; and connector damage.

Pay particular attention to the charger, regulator and processor areas.

## 3. Unpowered electrical checks

Before applying power measure resistance from main input to ground; measure resistance from battery rail to ground; measure resistance from each regulated rail to ground; check that connector polarity matches documentation; and confirm there is no obvious short.

A low resistance is not automatically a fault, but an unexpected near-short should be investigated before power is applied.

## 4. Current-limited first power

Use a bench supply with an appropriate current limit for the design state.

The initial objectives are to avoid a rapid current-limit condition or unexpected heating, confirm plausible charger/system-node behavior, verify that the regulated rail reaches its intended voltage, and confirm that the processor rail is stable.

Do not connect external sensors during the first rail test unless they are necessary for the power architecture.

## 5. Thermal check

After a short powered interval, inspect the board for abnormal heating. A thermal camera is useful but not required; careful touch should only be used where electrically safe.

Unexpected heating is a reason to remove power and investigate.

## 6. Processor bring-up

Once rails are stable:

1. verify reset/enable behavior;
2. connect the documented programming interface;
3. confirm the ESP32 target is detected;
4. flash a minimal bring-up firmware;
5. confirm serial/debug output;
6. record reset reason and boot state.

## 7. Peripheral bring-up

Enable one subsystem at a time.

Recommended order:

```text
Processor
   ↓
On-board accelerometer
   ↓
Storage
   ↓
Buttons / indicators
   ↓
External interfaces
   ↓
Communications
   ↓
Full ORIGIN sensor set
```

This sequence reduces the chance that several simultaneous faults hide the real cause.

## 8. LIS3DH test

Verify bus communication; expected device identity where available; plausible static acceleration; axis response when the PCB is rotated; and interrupts if used.

Document the physical axis orientation.

## 9. Storage test

For the SD subsystem initialize the card; create a test file; write known data; flush/close; power-cycle; read the data back; and test missing-card behavior.

## 10. External-interface test

Before plugging in a sensor, measure the connector supply voltage and verify the pinout against the schematic.

Then test external devices one at a time.

## 11. Battery and charging test

Only after bench-power behavior is understood should battery operation be validated.

Check connector polarity; system operation from battery; charging behavior from external input; transition between external input and battery; thermal behavior under charging/load; and low-battery/brownout behavior.

Exact current and voltage acceptance criteria must be defined from the released power schematic.

## 12. Full-system soak test

A board that passes a short bench test should run for an extended period while logging resets; sensor failures; storage errors; communication interruptions; power-state changes; and temperatures where measured.

## Bring-up record

Each first article should have a test record containing:

| Field | Example |
| --- | --- |
| PCB revision | v2.x |
| Board serial / identifier | Assigned during test |
| Assembly date | YYYY-MM-DD |
| Firmware commit | Git SHA / tag |
| Rail checks | Pass/fail + measured values |
| Peripheral checks | Pass/fail |
| Known rework | Description |
| Tester | Name/initials |
| Final disposition | Pass / rework / reject |

Bring-up results should feed directly into [Testing & Validation](../testing-validation/README.md).
