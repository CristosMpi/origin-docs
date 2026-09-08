# Interfaces

Rosetta connects ORIGIN Core to batteries, removable storage, sensors, communications hardware and expansion modules. These interfaces should be documented by function rather than only by connector reference designator so that hardware and firmware remain understandable across board revisions.

## Interface categories

Rosetta v2 development has included the following interface groups:

- battery / power connectors;
- external sensor headers;
- storage interface;
- SIM-related interface;
- programming and debug access;
- user controls and status signals;
- future expansion connections.

## Battery connectors

The design history includes **two 1×02 battery-related connectors**. The released schematic must define their exact role, polarity and electrical equivalence.

Before field use, the board should have clear polarity marking both in documentation and on the silkscreen where possible.

## Expansion headers

Rosetta v2 development includes **multiple 1×03 headers** intended for external devices and sensor integration. Four such headers were part of the v2 design work.

A final pinout table should be generated from the released schematic in this format:

| Connector | Pin 1 | Pin 2 | Pin 3 | Voltage domain | Intended use |
| --- | --- | --- | --- | --- | --- |
| TBD | TBD | TBD | TBD | TBD | External sensor / expansion |

Until that table is verified, devices should not be connected based on connector position alone.

## SD storage

The board design includes an SD-card interface for local data storage. The final documentation should identify:

- socket type;
- bus type;
- chip-select pin where applicable;
- supported voltage;
- card-detect behavior if implemented;
- safe removal procedure;
- filesystem expected by firmware.

Local storage is particularly useful when ORIGIN operates without dependable network access.

## SIM / cellular-related interface

Rosetta v2 development includes micro-SIM/eSIM-related work. This interface should be documented together with the modem architecture because a SIM socket is only one part of a cellular subsystem.

The release documentation must clarify whether the fitted configuration uses:

- removable micro-SIM;
- eSIM;
- both as alternatives;
- neither in the current assembly.

## Programming and debug

Every released Rosetta board should have a documented way to:

- flash firmware;
- recover a non-booting board;
- access serial diagnostics;
- place the processor into the required boot mode;
- identify ground and logic-voltage levels.

Debug access should be physically available during development but reviewed from a security perspective before deployment.

## Buttons and status signals

The v2 design history includes button/status-related circuitry. The final schematic should define each control with a functional name rather than relying only on references such as BTN or generic LED labels.

## Interface release rule

A connector is considered documented only when all of the following are known:

1. physical connector type;
2. pin numbering orientation;
3. electrical function of every pin;
4. voltage/current limits;
5. firmware relationship;
6. expected external device;
7. behavior when left disconnected.

This prevents a mechanically compatible connector from being mistaken for an electrically compatible one.