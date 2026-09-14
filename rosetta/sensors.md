# Sensors

Rosetta supports both on-board sensing and the external sensor ecosystem used by ORIGIN Core.

## LIS3DH

The on-board **LIS3DH** is a three-axis accelerometer. Within ORIGIN it can provide information related to orientation, movement, and physical state of the unit.

## External presence sensors

ORIGIN Core uses three **DFRobot C4001 24 GHz mmWave** sensors for directional presence and motion sensing. Rosetta provides the connection and processing environment required to integrate those channels into the wider system.

## Environmental sensors

Environmental channels can be added according to the deployment profile. The software architecture keeps each measurement associated with its source identity, units, timestamp, and health state.

## Sensor health

A sensing channel is more than a numerical value. ORIGIN also tracks whether the channel is initializing, operating normally, intentionally disabled, or requires attention. This makes operator information clearer and supports maintenance.

## Calibration and placement

Sensor performance depends on the physical installation. Mounting angle, enclosure geometry, surrounding materials, and site conditions are therefore documented as part of calibration and commissioning.
