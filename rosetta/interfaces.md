# Interfaces

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
