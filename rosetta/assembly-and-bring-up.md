# Startup & Verification

Rosetta startup verification confirms that the electronics and connected ORIGIN Core subsystems enter a known, healthy operating state.

## Power-on sequence

When the unit starts, Rosetta establishes the required power rails, starts the embedded processor, loads the active configuration, initializes storage and interfaces, and checks the expected sensors and modules.

## Processor verification

The embedded controller reports its software identity and begins the ORIGIN device-state sequence. Repeated resets or an unexpected startup state are surfaced through diagnostics rather than hidden from the operator.

## Sensor verification

Each configured sensing channel is initialized and associated with its logical identity. The three C4001 radar channels, environmental sensors, the LIS3DH, and supported modules can therefore be checked independently.

## Storage and communications

Where local storage is used, the system verifies access before relying on it for logging or buffering. Communications state is reported separately so a transport interruption is not confused with a sensor condition.

## Ready state

A Core unit is ready for normal use when its required subsystems have initialized, the intended configuration is active, system time is meaningful, and the reported health state matches the installed hardware.

This verification sequence is also used after service, component replacement, or a software update.
