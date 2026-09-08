# Setup

Setup begins after the ORIGIN unit has been physically installed and inspected. This stage brings the device into its site-specific software state: identity, configuration, sensor inventory, communications, timekeeping, logging, and operator-facing status.

Setup should be controlled and reversible. A device that merely boots is not yet ready for calibration or commissioning.

## Setup objectives

By the end of setup, the deployment team should be able to answer:

- Which ORIGIN unit is this?
- Which hardware and firmware revisions are installed?
- Which sensors and modules are expected?
- Which configuration is active?
- Is time synchronized?
- Is local logging functioning?
- Is the communications path operational or intentionally offline?
- Can the device report its own health?

## Initial boot

Power the unit while monitoring its startup behavior.

Observe for:

- normal boot indication;
- repeated resets;
- unexpected delays;
- missing sensors;
- abnormal power behavior;
- configuration errors;
- storage errors;
- communication failures.

The expected startup sequence should include hardware initialization, sensor detection, configuration loading, storage checks, and communication initialization.

A sensor that fails to initialize should be represented as unavailable or unhealthy, not silently interpreted as a valid zero reading.

## Confirm identity

Every deployed unit should have a stable identity.

Verify:

- ORIGIN unit ID;
- Rosetta hardware revision;
- enclosure revision if tracked separately;
- firmware version;
- enabled module set;
- site/deployment profile identifier.

These values should appear in logs and deployment records so later data can be traced to the actual deployed configuration.

## Hardware inventory

Compare the software-detected hardware against the installation record.

Expected items may include:

- Rosetta v2;
- internal sensors;
- three C4001 radar channels where fitted;
- storage subsystem;
- communications hardware;
- solar or power-management status inputs;
- BITs or other modules;
- optional expansion modules.

Any mismatch must be investigated before calibration.

## Configuration loading

Load the approved site configuration rather than editing arbitrary values directly in the field.

A deployment configuration may include:

- unit identity;
- sensor enable/disable state;
- sample intervals;
- radar operating parameters;
- local event thresholds;
- logging behavior;
- communications settings;
- module configuration;
- upstream destination identifiers;
- time zone or timestamp handling;
- maintenance/reporting intervals.

Exact parameter names depend on the final firmware implementation.

## Configuration validation

After applying configuration, read it back from the device and compare it with the intended deployment profile.

The setup record should capture:

- configuration version;
- configuration checksum or revision identifier where supported;
- date applied;
- person responsible;
- any deliberate deviation from the standard profile.

This prevents a configuration from being considered applied merely because an upload command succeeded.

## Credentials and secrets

Secrets must not be embedded in public documentation or committed to the public repository.

Examples include:

- Wi-Fi passwords;
- SIM credentials;
- API tokens;
- private endpoint keys;
- device certificates;
- administrator passwords.

Provision them using the secure mechanism supported by the final software architecture.

## Time and timestamps

Correct timing is essential for correlating sensor events.

Verify that:

- the device has a valid clock;
- time synchronization succeeds where a network source is available;
- timestamps survive communication interruptions appropriately;
- time zone handling is defined;
- logs clearly distinguish local time from UTC if both are used.

If reliable time is unavailable, the condition should be visible in device health and in recorded data.

## Storage check

Before enabling normal monitoring, verify local storage.

Check:

- storage is detected;
- filesystem or storage area is writable;
- a test record can be created;
- available capacity is reasonable;
- recovery from a restart does not corrupt recent data;
- the firmware handles storage failure without falsely reporting normal operation.

Where an SD card is used, card health and seating should be verified.

## Communications setup

Bring up the intended communications path.

Depending on the deployment, this may be Wi-Fi, cellular, wired network, a gateway, or intentionally local-only operation.

Verify separately:

1. interface initialization;
2. network attachment;
3. upstream reachability;
4. authentication;
5. successful transmission of a test record;
6. correct handling of loss and reconnection.

A network connection alone does not prove that application data is reaching the expected destination.

## Local-only and offline mode

ORIGIN should remain able to distinguish healthy offline operation from failure.

If the site intentionally operates without continuous connectivity:

- confirm local records are stored;
- confirm queue/buffer behavior;
- document capacity limits;
- verify how data will later be retrieved or synchronized;
- ensure operators understand which functions require connectivity.

## Health state

Before calibration, the device should provide a health summary covering at least:

- power state;
- sensor state;
- storage state;
- communication state;
- time state;
- configuration validity;
- module state.

Suggested health semantics are:

- **Healthy** — functioning as intended;
- **Degraded** — usable, but one or more non-critical capabilities are impaired;
- **Fault** — required capability is unavailable;
- **Initializing** — not ready for interpretation;
- **Disabled** — intentionally excluded.

## Setup acceptance

Setup is complete only when:

- unit identity is correct;
- hardware inventory matches the physical installation;
- the intended configuration has been applied and read back;
- local storage is working;
- timestamps are valid or the timing limitation is explicitly recorded;
- communication behavior matches the deployment design;
- no unresolved critical health fault exists.

The unit can then proceed to [Calibration](calibration.md).