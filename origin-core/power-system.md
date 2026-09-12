# Power System

Power is a core reliability subsystem in ORIGIN. A field-monitoring device cannot be considered operational merely because its processor is running; sensing, storage, communications and attached modules all depend on stable energy availability.

ORIGIN therefore treats power as a monitored system with defined states, limits and failure behavior.

## Power-system goals

At Core level, the power architecture is intended to accept energy from an external source; charge and protect the rechargeable battery system; generate stable regulated power for the electronics; continue operating across normal battery-voltage changes; make power condition visible to firmware where supported; support power-aware operating modes; prevent one peripheral from destabilizing the entire unit; and support field-oriented energy sources such as solar.

The exact electrical circuit belongs to the [Rosetta Power Management](../rosetta/power-management.md) documentation. This page describes how the power subsystem behaves as part of ORIGIN Core.

## Architecture

A simplified energy path is:

```text
External energy source
        ↓
Charging / power-path management
        ↓
Rechargeable battery
        ↓
Regulation
        ↓
System power rails
        ↓
Rosetta + sensors + peripherals
```

The power path must work in both directions conceptually: energy moves toward the loads, while status information moves back toward the firmware and diagnostic layer.

## Rosetta v2 power stages

The current Rosetta v2 design includes a **BQ24074-family battery-charging / power-path stage** and a **TPS63031-based buck-boost regulation stage**.

These components support the broader design goal of operating from a rechargeable battery while maintaining a stable supply for the rest of the system.

Exact component values, rail voltages, current limits and PCB implementation must be taken from the validated schematic and BOM for the specific Rosetta revision rather than inferred from this Core-level page.

## Solar integration

Solar input is part of ORIGIN's field-deployment direction.

This affects more than the charging circuit. A usable solar implementation also requires appropriate panel sizing; mechanical support; panel orientation; protected cable routing; strain relief; weather exposure planning; connector selection; and energy-budget calculations.

The current enclosure concept includes dedicated solar-panel supports and a cable-routing path through a structural support so power wiring can reach the internal electronics without becoming an exposed loose cable.

Mechanical details are documented in [Mechanical Design](../mechanical-design/README.md).

## Battery role

The battery acts as an energy buffer between variable input conditions and the electronic loads.

In practice, this means ORIGIN should be able to tolerate periods where incoming energy is lower than instantaneous consumption, provided the battery has sufficient stored energy.

Battery-related design decisions include chemistry and nominal voltage; capacity; maximum charge current; expected discharge current; temperature limits; physical dimensions; connector and replacement method; and expected runtime without charging.

These values should be published only after the selected battery configuration has been validated.

## Energy budget

An ORIGIN deployment should have an explicit energy budget.

A simplified calculation is:

```text
Average system power
    = base electronics
    + sensors
    + communications
    + storage
    + attached modules
```

The average value matters more than a single instantaneous reading when estimating runtime, but peak current also matters because short high-current events can cause supply drops even when the long-term average is acceptable.

The energy budget should therefore record both **average consumption**, for runtime and solar sizing and **peak consumption**, for regulator, battery and wiring design.

## Power-aware firmware

Firmware can improve reliability by changing behavior according to available energy.

Possible operating states include:

| State | Typical behavior |
| --- | --- |
| Normal | Full configured sensing and communication |
| Energy-saving | Reduced non-essential activity or communication frequency |
| Critical | Preserve essential monitoring and logs; limit optional loads |
| Recovery | Resume normal operation only after stable power returns |

The exact thresholds and actions should be determined through testing rather than guessed.

## Peripheral power management

Sensors and modules may have very different power requirements. The system should avoid assuming that every peripheral can remain active continuously under every deployment condition.

Where the hardware supports it, peripherals may be powered continuously; enabled only during measurement windows; restarted after a detected fault; disabled by configuration; and isolated during diagnostics.

Power-control strategy must account for sensor warm-up time and the possibility that power cycling changes calibration or state.

## Power telemetry

Useful power-related telemetry can include battery voltage or estimated state; external-source presence; charging state; low-voltage events; brownout or reset history; regulator or rail faults where measurable; and time spent in energy-saving modes.

Even when not every value is available on a particular revision, the software architecture should distinguish power health from ordinary sensor data.

## Failure modes

Potential power failures include:

### Energy-source loss

The external source may be disconnected, shaded, damaged or unavailable. ORIGIN should continue on stored energy when possible and report the change in power condition.

### Battery depletion

If stored energy reaches a critical level, the system should avoid repeated unstable restart cycles. A controlled low-power or shutdown strategy is preferable to unpredictable brownouts.

### Load-induced voltage drop

A communications event, module startup or sensor load can produce a current spike. Power validation should include worst-case combined loads, not only idle operation.

### Charging fault

A connected external source does not guarantee that the battery is charging correctly. Charging state should be verified during hardware validation.

### Connector or cable failure

Field wiring can fail mechanically. Cable strain relief and service inspection therefore belong to reliability engineering, not just enclosure aesthetics.

## Testing

Power validation should include startup from battery only; startup with external energy present; transition between charging and battery operation; operation across the intended battery-voltage range; peak-load testing; prolonged run testing; low-energy behavior; recovery after power interruption; solar-input testing under realistic conditions; and thermal observation of charging and regulation components.

Testing should be repeated after significant changes to sensors, radios, battery capacity or attached modules because all of them can change the power profile.

## Safety and serviceability

Rechargeable batteries and charging electronics require deliberate handling. The final deployment documentation should define approved battery type; connector polarity; replacement procedure; inspection criteria; storage conditions; damaged-battery handling; and maximum validated charging conditions.

Until those values are frozen for a production revision, they should remain version-specific rather than being presented as universal ORIGIN specifications.

## Related documentation

Continue with [Rosetta → Power Management](../rosetta/power-management.md) for circuit-level implementation, [Mechanical Design → Solar System](../mechanical-design/solar-system.md) for panel mounting and cable routing, [Testing & Validation](../testing-validation/README.md) for power-test procedures, and [Maintenance](../maintenance/README.md) for inspection and replacement workflows.
