# Sensors

Rosetta supports both sensors located on the PCB and sensors mounted elsewhere in ORIGIN Core. The board’s job is to provide stable electrical interfaces and reliable data paths; the physical sensing strategy is documented at the ORIGIN Core level.

## On-board motion sensing

Rosetta v2 design work includes an **LIS3DH three-axis accelerometer**.

Potential ORIGIN uses include detecting movement of the Core; detecting orientation changes; recording mechanical disturbance; supporting tamper-related logic; and adding context to other sensor events.

These are system use cases, not automatic properties of the component. Thresholds and event logic must be defined and tested in firmware.

## External sensing

Most environmental and presence sensors are physically placed according to the enclosure and deployment geometry rather than simply where they fit on the PCB.

Rosetta therefore acts as the electrical hub for external sensing such as mmWave presence sensors, environmental sensors, modular accessories, and future expansion sensors.

See [ORIGIN Core → Sensor System](../origin-core/sensor-system.md).

## Sensor-driver model

Firmware should expose a consistent state model regardless of sensor type:

```text
DISABLED
INITIALIZING
HEALTHY
DEGRADED
MISSING
INVALID
FAULT
```

A missing sensor must not silently become a normal zero reading.

## Sensor metadata

Every logged sample should carry enough metadata to be meaningful later. Where appropriate this includes sensor identity; timestamp; raw or engineering value; units; validity flag; calibration/version information; and health state.

## Accelerometer validation

For the LIS3DH subsystem, bring-up should include:

1. confirming device communication;
2. reading the device identity register where supported;
3. confirming plausible static acceleration values;
4. rotating the board and observing axis changes;
5. confirming interrupt behavior if interrupts are used;
6. documenting axis orientation relative to the physical enclosure.

The last step is especially important. A technically correct X/Y/Z reading is not useful if the firmware team does not know how those axes map to the installed ORIGIN Core.

## External sensor power

External sensors can create transient current demand and electrical noise. The interface documentation should therefore identify which rail supplies each external header and whether that rail is switched or always active.

## Calibration

Calibration belongs to the sensor-plus-installation combination. Replacing a sensor, changing the enclosure or moving the unit may require recalibration even when the PCB remains unchanged.

Validated procedures belong in [Testing & Validation](../testing-validation/README.md).
