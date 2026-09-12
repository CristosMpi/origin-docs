# Software Installation

Software installation is the process of preparing a Rosetta-based ORIGIN unit with a known firmware build and a valid initial configuration before commissioning.

This page describes the installation workflow at system level. Exact commands, USB identifiers, build-system commands, partition layouts, and flashing addresses will be added from the authoritative firmware repository rather than guessed.

## Installation objectives

A successful installation should result in a unit that boots predictably; reports an identifiable firmware version; loads valid configuration; initializes expected sensors; reports subsystem health; can enter the normal monitoring state; and can be diagnosed if any of those steps fail.

## Before installation

Confirm the hardware before loading software.

At minimum:

1. identify the Rosetta hardware revision;
2. inspect the board for assembly defects;
3. verify supply polarity and expected power rails;
4. confirm the programming/debug connection;
5. disconnect or isolate any external hardware that could be damaged by an incorrect initial configuration.

See [Rosetta → Assembly & Bring-up](../rosetta/assembly-and-bring-up.md).

## Development environment

The final development environment will be documented when the firmware source is connected.

The release instructions should eventually specify supported operating systems; required compiler/toolchain; firmware framework; package/dependency manager; supported programmer/USB interface; version requirements; and build profiles.

These requirements should be version-pinned wherever practical so a release can be reproduced later.

## Recommended installation workflow

The intended workflow is:

```text
Obtain trusted source/release
          ↓
Verify target hardware revision
          ↓
Install required toolchain
          ↓
Build or select release image
          ↓
Connect Rosetta
          ↓
Flash firmware
          ↓
Restart device
          ↓
Check boot log/version
          ↓
Load initial configuration
          ↓
Run commissioning checks
```

## Source builds

When building from source, record the source revision used.

A deployment record should ideally include repository; branch/tag; commit SHA; build profile; resulting firmware version; and operator/date.

This prevents "latest code" from becoming an untraceable deployment artifact.

## Release images

For field deployment, a prebuilt and validated release image may be preferable to requiring every installer to compile the project.

Release images should be associated with a version number; supported Rosetta revision(s); release notes; checksum or integrity value where distributed externally; and configuration compatibility information.

## First boot

The first boot after installation should be observed rather than immediately enclosing the board.

Verify reset cause is reasonable; expected firmware version is reported; storage initializes where applicable; required interfaces initialize; configured sensors appear; missing optional sensors are handled gracefully; communication state is visible; and no repeated reboot loop occurs.

## Initial configuration

Firmware installation and site configuration are separate operations.

A single software release may be used across multiple units while each unit has a unique configuration for device identity; deployment/site identity; sensor enablement; calibration; communication settings; and monitoring parameters.

See [Configuration](configuration.md).

## Secrets and credentials

Secrets must not be stored in this public documentation repository.

If a deployment requires credentials, they should be provisioned through the approved secure process for that deployment. Documentation may describe **where** credentials are configured, but should not contain real tokens, passwords, private keys, or production secrets.

## Installation verification

Before declaring installation complete, perform a short functional check.

A minimum checklist is firmware version recorded; hardware revision recorded; device identity confirmed; configuration loaded successfully; expected sensors healthy; missing sensors reported correctly; local logging/diagnostics available; communication tested if required; restart tested; and no unexplained reset loop.

## Recovery installation

If a unit cannot boot normally, a recovery procedure should allow firmware to be restored through the physical programming interface.

The final recovery guide should document how to force programming/recovery mode; how to erase corrupted firmware/configuration safely; which data is lost during recovery; how to restore a known release; and how to re-provision configuration.

These board-specific steps will be added only after confirmation from the firmware/hardware source.

## Factory/bench provisioning vs field updates

Initial installation is different from later updates.

**Bench provisioning** assumes physical access and allows full verification.

**Field updating** must account for interrupted power, weak connectivity, rollback, and version compatibility.

See [Updates](updates.md).

## Deployment record

For every field unit, Team Galene should maintain a software deployment record such as:

| Field | Example meaning |
| --- | --- |
| Device ID | Unique unit identity |
| Hardware revision | Rosetta revision |
| Firmware version | Installed release |
| Build/commit | Reproducibility identifier |
| Configuration revision | Site settings version |
| Installed by | Responsible operator |
| Installation date | When software was provisioned |
| Verification result | Pass/fail and notes |

## Related pages

See [Firmware](firmware.md), [Configuration](configuration.md), [Updates](updates.md), and [Installation & Deployment](../installation-deployment/README.md).
