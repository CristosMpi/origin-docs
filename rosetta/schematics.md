# Electrical Design

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
