# Software Updates

Software updates allow ORIGIN to receive bug fixes, new capabilities, security improvements, and compatibility changes after initial installation.

Because ORIGIN is intended for field deployment, an update mechanism must prioritize **recoverability and traceability** over convenience. An interrupted or incompatible update must not leave a deployed unit permanently unusable.

The exact OTA mechanism, image format, signing process, partition layout, and release commands will be documented from the authoritative firmware repository. This page defines the required update lifecycle and safety principles.

## Update objectives

A controlled update process should identify the current version; determine whether the target release is compatible; obtain a trusted update artifact; validate the artifact before activation; preserve required configuration/calibration data; restart into the new software in a controlled way; verify successful operation; recover or roll back if verification fails; and record the update result.

## Update lifecycle

A conceptual update flow is:

```text
Current release
      ↓
Update available
      ↓
Compatibility check
      ↓
Download / receive artifact
      ↓
Integrity / authenticity validation
      ↓
Stage update
      ↓
Install / activate
      ↓
Restart
      ↓
Post-update self-check
      ↓
SUCCESS ───────→ normal operation
      │
      └─ failure → rollback / recovery
```

## Version identity

The device should always be able to report its current firmware version.

A release identity should ideally include semantic or project version; build/commit identifier; supported Rosetta revision(s); schema/configuration compatibility; release date; and release notes.

Without a stable version identity, diagnosing a field unit becomes unnecessarily difficult.

## Compatibility checks

Before installation, the updater should verify that the release is appropriate for the target device.

Potential compatibility dimensions include hardware revision; flash/storage layout; bootloader requirements; sensor configuration; configuration schema; communication schema; and backend/Centaurus compatibility.

An update that is valid software but incompatible with the installed hardware should be rejected before activation.

## Configuration preservation

Firmware updates should not unintentionally erase deployment identity, calibration, or approved site configuration.

The update design should explicitly define which data is part of firmware; persistent device configuration; calibration data; runtime cache/queue; and diagnostic logs.

If a schema migration is required, it should be controlled and testable.

## Integrity and authenticity

A device should not install an update merely because a file was received successfully.

Depending on the final implementation, validation may include cryptographic hash/integrity check, signed release verification, authenticated transport, and allowed version/source checks.

The exact security mechanism must be documented from the actual implementation and should not rely on hidden assumptions.

## Interrupted updates

Power or network loss can happen during a field update.

The design should ensure that interruption during download/staging does not corrupt the currently running release.

If the platform supports separate active and staging images, update activation should occur only after the new artifact is fully received and validated.

## Post-update verification

A successful boot is not enough to prove an update succeeded.

After activation, verify firmware version matches the intended release; configuration loaded; required sensors initialize; storage initializes; communication behaves as expected; watchdog/reset loop is absent; and critical self-tests pass.

Only then should the release be marked healthy.

## Rollback

A field-ready update strategy should include a rollback or recovery path.

Rollback may be triggered when firmware fails to boot; repeated watchdog resets occur; post-update health checks fail; configuration cannot be migrated; and critical communications fail because of incompatibility.

The exact rollback mechanism depends on the firmware/partition architecture and will be documented once verified.

## Manual recovery

Even if OTA is implemented, physical recovery should remain possible for development and maintenance.

A recovery procedure should define how to:

1. connect to Rosetta physically;
2. enter recovery/programming mode;
3. install a known-good release;
4. restore or re-provision configuration;
5. verify all critical hardware.

## Release channels

If multiple release channels are used, they should be clearly separated.

For example **development** — rapid iteration, verbose diagnostics, **testing/validation** — candidate release under controlled testing, and **stable/deployment** — release approved for field use.

A field unit should not automatically track an unstable development branch.

## Update policy

Not every available update should be installed immediately.

A deployment policy may consider severity of the fix; compatibility risk; site access schedule; current unit stability; ability to recover physically; and whether the update changes detection behavior.

Changes that affect monitoring logic should receive documented validation before broad deployment.

## Security updates

Security-related fixes may require faster deployment than ordinary feature updates.

However, urgency should not remove the need for artifact validation, compatibility checks, and rollback planning.

## Logging and audit trail

Each update attempt should produce a record containing, where practical device ID; old version; target version; update start time; source/method; validation result; activation result; rollback result if any; and final active version.

This helps distinguish software changes from unrelated hardware or environmental problems.

## Testing updates before deployment

Before a release reaches field units, test at least:

### Normal update

Old → new release.

Configuration retained.

Sensors healthy.

Communication restored.

### Interrupted download/staging

Network lost.

Power removed before activation.

Device remains on old known-good software.

### Bad artifact

Corrupted image.

Wrong hardware release.

Unsupported version.

Validation rejects it.

### Failed activation

Simulated boot failure or failed health check.

Rollback/recovery functions correctly.

### Migration

Previous supported configuration schema upgrades correctly.

Invalid configuration is rejected safely.

## Deployment checklist

Before approving an update for field use release source/tag identified; release notes written; supported hardware listed; configuration compatibility checked; upgrade tested from currently deployed version; interrupted update tested; rollback/recovery tested; post-update self-check defined; and deployment record prepared.

## Related pages

See [Firmware](firmware.md); [Installation](installation.md); [Configuration](configuration.md); [Communications](communications.md); [Development → Versions](../development/versions.md); and [Development → Changelog](../development/changelog.md).
