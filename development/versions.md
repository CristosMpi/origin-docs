# Version Guide

ORIGIN uses clear version identifiers so users, operators, and support personnel can match a physical unit with the correct configuration and documentation.

## Platform generation

The platform generation identifies the overall ORIGIN family described by the documentation. The current documented generation is **ORIGIN 2026**.

## Rosetta revision

Rosetta has its own hardware revision because the electronics can evolve independently from the enclosure or deployment configuration. The current electronics generation described in this wiki is **Rosetta v2**.

## Mechanical revision

The enclosure, sensor mounts, solar support, and module interfaces can carry a mechanical revision. This ensures replacement parts and assembly guidance match the physical unit.

## Software version

The software version identifies the embedded and system software active on a unit. It is used during setup, maintenance, updates, and support.

## Configuration identity

Configuration identifies the site-specific settings of a unit, such as enabled sensors, module selection, acquisition behavior, communication settings, calibration values, and deployment identity.

## Module revision

BITs, Aqua Base, Drone Mount, and other expansion modules can carry their own revision so compatibility with the Core remains clear.

## Deployment record

A deployment record brings the relevant identifiers together. A typical record associates the ORIGIN generation, Rosetta revision, mechanical revision, software version, configuration identity, module set, calibration record, and deployment identifier.

This version model makes service and support straightforward: **the unit can always be traced to the documentation that describes its configuration**.
