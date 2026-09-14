# Expansion System

The **ORIGIN Expansion System** provides a common architecture for adding optional modules to ORIGIN Core while preserving a consistent user experience.

## Mechanical interface

Modules use defined attachment zones, orientation, retention, cable-routing space, and keep-out regions around sensors and service areas. This prevents an accessory from becoming an unrelated add-on to the enclosure.

## Electrical interface

Supported active modules connect through the Core's expansion power and data architecture. The unit configuration records which module is installed and which behavior is expected.

## Software identity

Modules are identified logically by the software stack. Their observations, events, and health information can therefore be associated with the correct physical extension.

## Compatibility

Compatibility is determined by the ORIGIN generation, Core enclosure, Rosetta revision, software version, and module revision. This information is stored with the configuration rather than left to user guesswork.

## Supported module families

The documented expansion families are **BITs**, **Aqua Base**, and **Drone Mount**. Each serves a different deployment purpose while using the same overall principles of identity, configuration, serviceability, and compatibility.

## Isolation

A module condition is kept separate from the health of unrelated Core functions. This allows the operator to understand whether a service message belongs to an extension or to the main unit.

The Expansion System is what allows ORIGIN to remain one coherent platform across different deployment scenarios.
