# Modules

ORIGIN is designed as a modular monitoring platform rather than a single fixed device. The **Modules** layer extends ORIGIN Core for deployments that need different mounting methods, sensing positions, environmental conditions, or physical interaction with the site.

The current module family includes **BITs** — attachable expansion elements that extend the physical and sensing capabilities of ORIGIN, **Aqua Base** — a deployment base intended for water-adjacent or water-oriented use cases, **Drone Mount** — an interface for temporarily integrating ORIGIN hardware with an aerial platform, and **Expansion System** — the common mechanical, electrical, software, and identification principles that allow modules to work with the Core.

The objective is not to create a different ORIGIN device for every scenario. Instead, the same Core architecture should be able to support different configurations around a stable central platform.

## Why modularity matters

Heritage sites vary significantly. A system used around an archaeological structure may need different placement, sensing, power, or mounting characteristics from a system used near water, on elevated structures, or during a temporary survey.

A fixed product would force every deployment into the same physical arrangement. ORIGIN's modular approach instead separates the platform into:

```text
                ┌──────────────────┐
                │    ORIGIN Core   │
                │ Rosetta + sensors│
                │ firmware + comms │
                └────────┬─────────┘
                         │
                Expansion interface
                         │
        ┌────────────────┼────────────────┐
        │                │                │
      BITs          Aqua Base        Drone Mount
```

This architecture allows the Core to remain recognizable and maintainable while modules adapt it to a particular deployment.

## What counts as a module

A module is more than an accessory. To be considered part of the ORIGIN ecosystem, an extension should have a defined relationship with the Core in at least one of the following areas mechanical attachment; electrical power; data or control interface; sensor placement; deployment role; software identification; and maintenance and replacement procedure.

A decorative cover or unrelated mounting bracket is not automatically a module. The expansion system is intended for components that meaningfully extend or adapt system operation.

## Design principles

### Preserve the Core

Modules should avoid requiring permanent modification of Rosetta or the Core enclosure wherever possible.

This improves maintainability because a module can be removed, replaced, or redesigned without rebuilding the central system.

### Make attachment intentional

A module should have a repeatable installation position rather than relying on improvised cable ties, tape, or arbitrary fasteners.

Mechanical interfaces should define where the module attaches; how it is retained; how loads are transferred; how cables are routed; and how the user accesses the attachment after installation.

One important mechanical requirement already identified during ORIGIN enclosure development is that **BIT attachment points should not be placed only on the bottom of the Core**. When a unit is installed into or close to the ground, a bottom-only interface may become inaccessible. Expansion interfaces therefore need to remain reachable in realistic deployments.

### Keep module state visible

A module should not silently disappear from the system.

Where software integration exists, ORIGIN should be able to represent states such as:

```text
DETECTED
READY
ACTIVE
DEGRADED
FAULT
DISCONNECTED
UNSUPPORTED
```

A missing or failed module must be distinguishable from a module that is operating normally but simply has no event to report.

### Avoid hidden dependencies

A module should document what it requires from the Core, such as power; available communication interface; firmware support; mounting clearance; configuration profile; and environmental constraints.

This prevents an apparently compatible accessory from depending on an undocumented board revision or firmware assumption.

## Module lifecycle

A typical module should move through a defined lifecycle:

```text
Physical connection
       ↓
Identification
       ↓
Compatibility check
       ↓
Initialization
       ↓
Health verification
       ↓
Active operation
       ↓
Disconnect / shutdown
```

The exact identification method depends on the final electrical and firmware design. The important architectural requirement is that software should not assume that every possible module is always present.

## Mechanical interface

Mechanical module design should consider fastener type and accessibility; insertion/removal direction; cable strain relief; repeated assembly cycles; weather exposure; vibration and impact; compatibility with the main enclosure; interference with sensors; and interference with mounting to soil, walls, poles, structures, or aerial platforms.

The module interface must also avoid creating blind zones in ORIGIN's primary sensing system.

For example, a module mounted directly in front of a mmWave sensor could fundamentally alter radar performance even if the module itself works correctly.

## Electrical interface

Where a module requires power or data, the final interface specification should define connector family; voltage range; maximum current; polarity; signal levels; communication bus or protocol; hot-plug support, if any; protection requirements; and pin assignment.

These details are **not considered finalized in this overview**. They should be published only from the confirmed Rosetta/module hardware design rather than inferred from prototype wiring.

See [Rosetta → Interfaces](../rosetta/interfaces.md) for the central board interface documentation.

## Software integration

Modules can contribute to the software system in several ways.

A module may provide additional sensor observations; a new deployment mode; a physical actuator or interaction; configuration metadata; a new device-health source; and contextual information for Centaurus AI.

The Core software should treat module-originated information using the same provenance principles as built-in sensors: the source, time, validity, and health state should remain visible.

## Module identity and compatibility

As the ecosystem grows, each module revision should eventually have a stable identifier and compatibility information.

A useful future metadata model is:

```text
module_family
hardware_revision
firmware_requirement
interface_version
serial_or_unit_id
capabilities
health_state
```

This does not require every module to contain complex electronics. Even passive mechanical modules benefit from explicit revision tracking because geometry can change between versions.

## Environmental responsibility

Modules can change the environmental exposure of the Core.

For example a new opening may reduce sealing; an elevated mount may increase wind loading; a water-oriented base may introduce splash or immersion risks; a drone configuration introduces vibration and acceleration; and an external sensor may create a cable ingress path.

For that reason, a module's validation is not complete when the module itself works. The **combined Core + module configuration** must also be tested.

## Validation

Each module should be evaluated in at least four dimensions.

### Mechanical

Attachment strength.

Repeatability.

Interference.

Cable routing.

Removal and replacement.

### Electrical

Correct voltage and current behavior.

Connector integrity.

Fault isolation.

Startup and shutdown behavior.

### Software

Identification.

Health reporting.

Data validity.

Recovery after disconnect.

Compatibility with system versions.

### Deployment

Usefulness in the intended environment.

Installation time.

Maintenance accessibility.

Effect on Core sensing.

Operator usability.

Validated results belong under [Testing & Validation](../testing-validation/README.md).

## Current modules

### BITs

BITs provide a flexible expansion concept around the physical Core and are intended to allow additional functionality to be attached without redesigning the entire main unit.

See [BITs](bits.md).

### Aqua Base

Aqua Base adapts ORIGIN to deployments where the relationship with water or a water-adjacent environment changes the mechanical and monitoring requirements.

See [Aqua Base](aqua-base.md).

### Drone Mount

Drone Mount supports temporary aerial deployment by mechanically integrating ORIGIN hardware with an unmanned aerial platform.

See [Drone Mount](drone-mount.md).

### Expansion System

The Expansion System describes the common architecture that should make current and future modules compatible with ORIGIN.

See [Expansion System](expansion-system.md).

## Related documentation

Continue with [ORIGIN Core](../origin-core/README.md); [Rosetta](../rosetta/README.md); [Mechanical Design](../mechanical-design/README.md); [Software](../software/README.md); and [Testing & Validation](../testing-validation/README.md).
