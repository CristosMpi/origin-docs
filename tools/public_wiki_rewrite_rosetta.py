from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAGES = {
"rosetta/README.md": r'''# Rosetta

**Rosetta** is the custom electronics platform at the center of ORIGIN Core. It brings processing, power management, sensing interfaces, local storage, communications support, and expansion connectivity together on one coordinated board architecture.

The current documented generation is **Rosetta v2**.

## Role inside ORIGIN

Rosetta acts as the electrical bridge between the physical sensors and the ORIGIN software stack. It powers and supervises connected subsystems, provides the embedded processing environment, supports local data handling, and exposes the interfaces used by the enclosure and optional modules.

## Main functions

Rosetta v2 combines an ESP32-class embedded processor, battery and input-power management, regulated power conversion, LIS3DH motion/orientation sensing, storage-related interfaces, external sensor connections, communications-related interfaces, user/status signals, and expansion connectivity.

## Physical format

Rosetta v2 uses a compact two-layer PCB architecture with an overall footprint of roughly **100 × 105 mm** and a nominal board thickness of **1.6 mm**. Its geometry is designed to fit the vertically oriented ORIGIN Core enclosure while keeping connectors and service points accessible.

## Why a custom board matters

A custom electronics platform makes ORIGIN easier to integrate, configure, service, and reproduce than a collection of loosely connected development boards. Power paths, sensor connections, storage, processing, and expansion are organized around one system architecture.

Continue with [Rosetta v2](rosetta-v2.md), [Architecture](architecture.md), [Microcontroller](microcontroller.md), [Power Management](power-management.md), [Interfaces](interfaces.md), [Sensors](sensors.md), [Electrical Design](schematics.md), [PCB Design](pcb-design.md), [Components](bom.md), [Production & Quality](manufacturing.md), [Startup & Verification](assembly-and-bring-up.md), and [Diagnostics](troubleshooting.md).
''',
"rosetta/rosetta-v2.md": r'''# Rosetta v2

Rosetta v2 is the current electronics generation used by ORIGIN Core. It was designed to consolidate the functions that a field monitoring unit needs into a compact, serviceable platform.

## Hardware profile

Rosetta v2 uses a two-layer FR-4 PCB architecture with a nominal thickness of **1.6 mm** and an overall footprint of approximately **100 × 105 mm**. The board format is optimized for integration into the ORIGIN Core enclosure and for clear routing between power, processing, sensing, storage, and expansion functions.

## Functional blocks

The board architecture includes an ESP32-class embedded processor, power-path and battery-charging functions around the **BQ24074RGT**, regulated conversion around the **TPS63031DSK**, an **LIS3DH** three-axis accelerometer, local/removable storage support, communications-related interfaces, battery connections, external sensor connections, expansion headers, buttons, and status/control signals.

## Integration with ORIGIN Core

Rosetta does not operate as an isolated electronics board. Its connectors, mounting position, power behavior, sensor identities, and software configuration are coordinated with the enclosure and the rest of ORIGIN Core.

The three C4001 mmWave presence sensors are treated as directional sensing channels and are mounted mechanically so their physical orientation matches the software and deployment configuration.

## Version identity

A Rosetta v2 board is associated with its ORIGIN generation, enclosure revision, software version, configuration identity, and installed module set. This allows support and maintenance guidance to match the exact unit in service.
''',
"rosetta/architecture.md": r'''# Architecture

Rosetta is organized into clear electrical subsystems so ORIGIN Core can manage processing, power, sensors, storage, communications, and expansion as one coordinated device.

## Processing

The embedded processor runs the device software, initializes interfaces, collects sensor data, maintains system state, manages local storage and communications, and reports health information to higher-level ORIGIN software.

## Power

The power subsystem accepts the unit's energy input, manages the battery path, and generates stable rails for the processor and peripherals. Power state is treated as part of overall device health.

## On-board sensing

The LIS3DH provides motion and orientation information that can support installation context, movement awareness, and device-state interpretation.

## External sensing

Rosetta connects ORIGIN Core to presence sensors, environmental sensors, and supported expansion modules. Each connected channel retains a stable logical identity so software and maintenance records remain understandable.

## Storage

Local storage supports logging, buffering, configuration support, and preservation of records when remote connectivity is temporarily unavailable.

## Communications

Communications interfaces connect ORIGIN Core with the wider software environment while keeping local sensing and device control separate from remote transport state.

## Expansion

Expansion interfaces allow BITs and other supported modules to extend the Core without changing the fundamental Rosetta architecture.

This subsystem separation is what makes Rosetta serviceable: a user or technician can understand whether a condition belongs to power, sensing, storage, communications, or another part of the system.
''',
"rosetta/microcontroller.md": r'''# Microcontroller

Rosetta v2 uses an **ESP32-class embedded controller** as the main processing element of ORIGIN Core.

## Responsibilities

The controller coordinates startup, sensor initialization, data acquisition, local validation, storage operations, communications, configuration, timing, watchdog behavior, and device-health reporting.

## Startup behavior

At startup, the controller loads the active configuration, initializes required interfaces, identifies connected sensors and modules, establishes local storage where used, and exposes the resulting health state to the software stack.

## Local resilience

ORIGIN is designed so temporary loss of a remote service does not automatically stop local sensing. The embedded controller maintains local device state and can preserve records according to the installed configuration.

## Sensor identity

Each important sensing channel is mapped to a logical identity. This means a physical sensor can be serviced or replaced without making historical records ambiguous.

## Security role

The embedded controller is also part of the system trust boundary. Device identity, configuration, credentials, update behavior, and access to protected functions are handled separately from public documentation and ordinary user-facing settings.
''',
"rosetta/power-management.md": r'''# Power Management

Rosetta's power subsystem is designed to keep ORIGIN Core stable across battery operation, charging, external energy input, and changing peripheral load.

## Main components

The architecture uses the **BQ24074RGT** for battery charging and power-path functions and the **TPS63031DSK** for regulated conversion. Together they provide the foundation for a compact field-oriented energy system.

## Battery and external energy

Rosetta supports a rechargeable battery architecture and can be integrated with an external source such as the ORIGIN solar subsystem. The exact energy profile depends on the deployment configuration and enabled peripherals.

## Stable rails

The processor, storage, sensors, and communications hardware require stable supply rails. Rosetta therefore separates power conversion from the application logic and allows software to interpret available power-health information where supported.

## Power-aware operation

ORIGIN software can use power state when scheduling communications, sensing, maintenance alerts, or reduced-energy behavior. This is particularly useful in solar-assisted or remote deployments.

## User interpretation

Power information should be read as part of overall device health. A communications interruption, sensor restart, or reduced activity can have a different meaning depending on the available energy state.

See [ORIGIN Core → Power System](../origin-core/power-system.md) for the system-level view and [Solar System](../mechanical-design/solar-system.md) for the mechanical energy-input architecture.
''',
"rosetta/interfaces.md": r'''# Interfaces

Rosetta connects ORIGIN Core to power, sensors, storage, communications hardware, controls, and expansion modules.

## Power interfaces

Battery and external-energy connections provide the electrical path between Rosetta and the ORIGIN power system. Their use is defined by the assembled unit and its deployment configuration.

## Sensor interfaces

External sensor headers connect presence, environmental, and expansion sensing to the embedded controller. Software identifies sensors by logical channel rather than relying on users to interpret raw connector numbering.

## Storage interface

Rosetta supports local/removable storage for logging, buffering, configuration support, and service records where used by the software release.

## Communications interface

Rosetta provides the hardware foundation required by the selected communications configuration. The transport used by a particular unit is recorded in its deployment profile.

## Controls and status

Buttons and status signals support startup, service, and local interaction with the device. Their behavior is coordinated by firmware so the physical control and the reported system state remain consistent.

## Expansion interface

Expansion connections provide the electrical path used by supported BITs and other modules. The module identity and expected behavior are stored in the ORIGIN configuration so the system knows which capabilities belong to the installed unit.

The interface model keeps the Core modular while protecting users from unnecessary board-level detail.
''',
"rosetta/sensors.md": r'''# Sensors

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
''',
"rosetta/schematics.md": r'''# Electrical Design

Rosetta's electrical design is organized around functional blocks rather than exposed as a collection of unrelated circuits.

## Processing block

The processing block provides the embedded controller, boot and control signals, local decoupling, and the digital interfaces used by the rest of the system.

## Power block

The power block manages external energy, battery charging, power-path behavior, and regulated rails for the controller and peripherals.

## Sensor block

The sensing architecture includes the on-board LIS3DH and external interfaces for ORIGIN's presence, environmental, and modular sensor ecosystem.

## Storage and communications

Storage-related and communications-related interfaces connect the Core to the data and transport functions required by its software configuration.

## Expansion block

Expansion connections allow supported modules to use Rosetta power and data paths while remaining identifiable to the software stack.

## Design philosophy

Rosetta's electrical architecture is designed for clear subsystem boundaries, controlled power distribution, stable sensor identity, serviceability, and compatibility with the ORIGIN Core enclosure.

For users, the important point is that Rosetta acts as one coordinated electronics platform rather than a set of independent development modules.
''',
"rosetta/pcb-design.md": r'''# PCB Design

Rosetta v2 uses a compact two-layer PCB architecture designed specifically for ORIGIN Core.

## Board format

The board occupies roughly **100 × 105 mm** and uses a nominal **1.6 mm FR-4** construction. This format balances connector access, enclosure integration, sensor routing, power distribution, and serviceability.

## Layer architecture

The PCB uses front and back copper with solder mask and silkscreen on both sides. Components and connectors are arranged so the board can be mounted inside the vertical ORIGIN enclosure while keeping important interfaces reachable.

## Layout priorities

The layout gives particular attention to short power paths, local decoupling, return paths, separation of switching circuitry from sensitive signals, connector orientation, mounting clearances, and readable silkscreen labeling.

## Mechanical integration

PCB design is coordinated with the enclosure. Mounting points, connector positions, cable bends, sensor paths, and service access are treated as shared electrical-mechanical requirements.

## Identification

Board revision information allows a technician to match the physical Rosetta board with the correct software, enclosure, and service documentation.
''',
"rosetta/bom.md": r'''# Key Components

Rosetta v2 combines a focused set of components selected for embedded control, power management, sensing, storage, and expansion.

| Function | Component or subsystem |
| --- | --- |
| Embedded processing | ESP32-class controller |
| Motion/orientation sensing | LIS3DH three-axis accelerometer |
| Battery charging / power path | BQ24074RGT |
| Regulated conversion | TPS63031DSK |
| Battery connection | Dedicated battery interfaces |
| External sensing / expansion | Multi-pin sensor and module headers |
| Local storage | Removable/local storage interface |
| Communications support | Communications-related interface hardware |
| User interaction | Buttons and status/control signals |

## Why these components matter

The component set is organized around the needs of ORIGIN Core: reliable embedded control, field-oriented power handling, identifiable sensor channels, local data support, communications integration, and modular expansion.

## Service perspective

Users normally interact with Rosetta at subsystem level rather than component level. Maintenance documentation therefore refers to power, sensing, storage, communications, and expansion functions so a service procedure remains understandable across hardware revisions.
''',
"rosetta/manufacturing.md": r'''# Production & Quality

Rosetta is produced through a controlled PCB manufacturing and assembly workflow appropriate for a custom embedded electronics platform.

## Production profile

Rosetta v2 uses a two-layer FR-4 construction with a nominal board thickness of **1.6 mm** and an overall footprint of approximately **100 × 105 mm**. The board is manufactured with standard professional PCB processes for copper, solder mask, silkscreen, component assembly, and board profiling.

## Quality controls

Before a Rosetta board is integrated into ORIGIN Core, it is checked for board identity, assembly quality, connector condition, power behavior, processor startup, storage access, sensing interfaces, and communication with the software stack.

## Traceability

Each board is associated with a revision so it can be matched with the correct enclosure, software, configuration, and service information.

## Integration quality

Production quality does not stop at the bare PCB. A Rosetta board is verified as part of the complete Core assembly, including sensor connections, cable routing, power input, mechanical mounting, storage, and communications behavior.

## Field service

The board layout and enclosure architecture are designed so major interfaces remain accessible during inspection and maintenance. This supports controlled replacement and minimizes disruption to the rest of the unit.

For the operational verification sequence, see [Startup & Verification](assembly-and-bring-up.md).
''',
"rosetta/assembly-and-bring-up.md": r'''# Startup & Verification

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
''',
"rosetta/troubleshooting.md": r'''# Rosetta Diagnostics

This page helps users and technicians identify which Rosetta subsystem deserves attention when ORIGIN reports an abnormal condition.

## Unit does not start normally

Check the available power source, battery connection, external-energy input, and visible system status. If power is available but startup does not complete, record the reported health state before cycling power.

## One sensor is unavailable

Check the physical connector, cable routing, sensor identity, and whether the sensor is enabled in the active configuration. A single unavailable channel should remain distinguishable from the other healthy channels.

## Several sensors are unavailable

When several channels change state together, inspect shared power, Rosetta interfaces, configuration, and the software startup record before replacing individual sensors.

## Local storage is unavailable

Check that the storage medium is seated correctly and recognized by the system. ORIGIN reports storage separately from sensing so operators can understand whether data logging or buffering is affected.

## Communications are offline

A communications interruption does not automatically imply a Rosetta hardware problem. Check the selected transport, signal/network conditions, authentication status where applicable, and whether the device continues to report healthy local sensing.

## Unexpected resets

Review power state, recent configuration or software changes, peripheral initialization, and storage activity. Repeated resets should be treated as a service condition and investigated before returning the unit to unattended operation.

## Support record

When requesting technical support, provide the ORIGIN unit identifier, Rosetta revision, software version, configuration identity, observed status, and the time the condition was first noticed. This information is usually enough to narrow the issue to the correct subsystem.
''',
"testing-validation/README.md": r'''# Testing & Validation

ORIGIN uses structured quality assurance to verify that electronics, sensing, software, mechanics, power, communications, modules, and deployment procedures work together as a complete system.

## Validation philosophy

Testing is performed at several levels: component, subsystem, integrated Core, and field deployment. This makes it possible to understand both individual functions and the interactions between them.

## Electronics

Electronics validation covers power stability, processor startup, interfaces, storage, sensor communication, external connections, and recovery behavior.

## Sensors

Sensor validation covers repeatability, calibration, field of view, installation effects, multi-sensor behavior, and health-state reporting.

## Mechanical system

Mechanical validation covers fit, fasteners, mounting, cable routing, sensor geometry, solar support, service access, repeated assembly, and environmental interfaces.

## Environmental performance

Environmental testing examines rain and splash exposure, drainage, condensation, temperature variation, humidity, contamination, cable entry, material behavior, and outdoor operation where applicable.

## Software and data

Software validation checks startup, configuration, identity, timestamps, data handling, communications, local resilience, updates, and the way system health is represented.

## Field validation

Field testing combines all of these areas in the installed environment and includes operator usability, maintenance access, sensor coverage, power behavior, communications, and multi-unit coordination.

Continue with [Galene Lab Standards](galene-lab-standards.md), [Electronics Testing](electronics-testing.md), [Sensor Testing](sensor-testing.md), [Mechanical Testing](mechanical-testing.md), [Environmental Testing](environmental-testing.md), [Field Testing](field-testing.md), and [Quality Evidence](validation-results.md).
''',
"testing-validation/validation-results.md": r'''# Quality Evidence

ORIGIN quality evidence is organized by subsystem and deployment configuration so users can understand what a result applies to without reading internal laboratory logs.

## Electronics evidence

Rosetta verification covers power behavior, processor startup, storage, sensor interfaces, communications-related interfaces, expansion connections, and integration with the complete ORIGIN Core assembly.

## Presence-sensing evidence

The three C4001 mmWave channels are evaluated in the geometry in which they are installed. Coverage is interpreted per deployment because walls, mounting height, orientation, surrounding objects, and enclosure geometry influence the monitored zones.

## Environmental evidence

Environmental evaluation includes enclosure exposure, drainage, condensation, cable entry, material condition, temperature and humidity effects, and post-exposure functional checks.

## Mechanical evidence

Mechanical validation records fit, mounting stability, sensor alignment, fastener retention, service access, cable routing, solar support behavior, and repeated assembly where relevant.

## Software evidence

Software quality checks cover startup, configuration, data identity, timestamps, local storage, communications state, health reporting, update behavior, and recovery after expected interruptions.

## Centaurus evidence

Centaurus evaluation focuses on whether its output is traceable to source observations, whether confidence and severity are kept distinct, how it handles uncertain or unavailable inputs, and how clearly the result can be reviewed by an operator.

## Deployment evidence

Field records associate observations with the actual unit versions, site configuration, sensor orientation, module set, power arrangement, software version, and calibration state used during the evaluation.

This evidence model keeps ORIGIN claims tied to the configuration that produced them and gives users a clear basis for understanding system behavior.
''',
"testing-validation/electronics-testing.md": r'''# Electronics Testing

Electronics testing verifies that Rosetta and the complete ORIGIN Core electrical system operate consistently before and during deployment.

## Visual and mechanical inspection

The board and connectors are inspected for assembly quality, secure mounting, clean interfaces, correct cable seating, and absence of visible damage or contamination.

## Power verification

Power checks confirm stable startup, regulated supply behavior, battery and charging operation where applicable, and normal operation with the expected sensors and communications hardware connected.

## Processor and storage

The embedded controller is checked for consistent startup, correct software identity, stable operation, and access to local storage where used by the configuration.

## Sensor interfaces

Each sensor channel is checked for communication, stable identity, valid data, and correct health-state reporting. A disconnected channel is shown as a service condition rather than being interpreted as a normal measurement.

## Communications

The selected communications path is checked independently from sensing so temporary remote connectivity conditions remain distinguishable from local device health.

## Integrated verification

The final electronics check is performed with Rosetta installed in ORIGIN Core so cable routing, enclosure integration, sensors, modules, power, and software can be evaluated together.

The result is a system-level quality check rather than a bare-board inspection.
''',
}

for rel, text in PAGES.items():
    (ROOT / rel).write_text(text.rstrip() + "\n", encoding="utf-8")
    print("rewrote", rel)
