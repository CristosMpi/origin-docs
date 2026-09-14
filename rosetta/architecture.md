# Architecture

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
