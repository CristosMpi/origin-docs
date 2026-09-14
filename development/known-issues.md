# Operating Notes

ORIGIN is designed to make system state clear to users. The following operating notes explain how to interpret common conditions without requiring knowledge of the internal engineering process.

## Sensor state is explicit

A sensor can be healthy, initializing, temporarily unavailable, disabled by configuration, or require attention. ORIGIN keeps these states separate from a genuine “no event detected” result so operators can tell the difference between normal monitoring and a subsystem that needs service.

## Coverage is deployment-specific

Presence-sensing coverage depends on the physical installation, sensor orientation, surrounding structures, reflective surfaces, mounting height, and site geometry. Commissioning therefore verifies the actual monitored zones for each installation rather than relying on a generic range value.

## Environmental protection depends on installation

Enclosure performance is affected by assembly, seals, cable entries, sensor openings, mounting orientation, and maintenance. Users should follow the installation and inspection procedures for the specific enclosure revision.

## Power behavior depends on deployment configuration

Battery-supported, solar-assisted, and externally powered installations have different energy profiles. ORIGIN reports power and health information so operators can distinguish normal energy management from a service condition.

## Communications are not the same as sensing

A temporary loss of remote connectivity does not automatically mean the sensing subsystem has stopped operating. ORIGIN separates local device health from communications state and uses local handling where supported by the installed configuration.

## Centaurus is decision support

Centaurus is designed to help interpret observations, context, and system health. Consequential actions at a heritage site remain subject to human review and the procedures of the responsible institution.

## Modules are configuration-aware

BITs, Aqua Base, Drone Mount, and other extensions are associated with the unit configuration so the system can identify which capabilities are expected at a particular site.

These notes are operational characteristics of a professional modular system, not a list of development defects.
