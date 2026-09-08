# Configuration

Configuration defines how a specific ORIGIN unit behaves without requiring source-code changes for every deployment.

The exact configuration file format, storage location, schema, and provisioning mechanism will be documented when the authoritative firmware repository is connected. This page defines the configuration model and operating rules that the implementation should follow.

## Why configuration matters

ORIGIN may be deployed in different physical environments with different sensors, monitoring priorities, communication conditions, and maintenance constraints.

Hard-coding those differences into firmware would make releases difficult to maintain and audit.

Configuration should therefore cover deployment-specific values such as:

- device identity;
- site identity;
- enabled sensors and modules;
- sampling intervals;
- sensor-specific parameters;
- calibration values;
- event thresholds;
- communications settings;
- logging verbosity;
- feature flags;
- maintenance/test modes.

## Configuration categories

A useful conceptual model is:

```text
configuration
├── identity
├── hardware
├── sensing
├── events
├── communications
├── logging
├── maintenance
└── security references
```

### Identity

Identity settings may include:

- device ID;
- deployment/site ID;
- hardware revision label;
- logical role.

Device identity should remain stable across normal firmware updates.

### Hardware

Hardware configuration describes what is physically expected to be present.

Examples:

- radar count;
- optional module enablement;
- storage availability;
- interface assignments;
- hardware feature flags.

If configured hardware is missing, the firmware should report a health error instead of silently pretending it is disabled.

### Sensing

Sensing configuration may contain:

- acquisition frequency;
- averaging/filter parameters;
- detection mode;
- sensor operating parameters;
- calibration coefficients;
- enable/disable state.

Values should remain within validated safe ranges.

### Event rules

Deterministic event rules can be configuration-driven where appropriate.

Examples:

- threshold crossing;
- state-change reporting;
- persistence duration;
- cooldown/debounce windows;
- alarm enablement.

The exact rules must remain explainable and testable.

### Communications

Communications configuration may define:

- enabled transport(s);
- network/operator settings;
- remote service identifier;
- retry behavior;
- reporting cadence.

Production credentials themselves should not appear in public documentation.

## Defaults

Every configuration field should have one of three states:

1. **required** — firmware must not proceed into normal operation without it;
2. **optional with safe default** — firmware can use a documented default;
3. **derived** — calculated from other validated information.

Undefined behavior should not be treated as a configuration strategy.

## Validation

Configuration must be validated before it is applied.

Useful validation checks include:

- schema version supported;
- required fields present;
- numeric ranges valid;
- known sensor/module names only;
- no duplicate identities;
- incompatible options rejected;
- communication parameters syntactically valid.

If validation fails, firmware should report the error clearly and use a safe state.

## Configuration versioning

Configuration should carry a version or revision identifier.

A useful record is:

```text
configuration_version: <revision>
schema_version: <schema>
device_id: <identity>
```

This makes it possible to determine which settings produced a field result.

## Schema migration

As firmware evolves, old configurations may no longer match the latest schema.

The update process should therefore define whether firmware:

- supports the previous schema;
- automatically migrates it;
- requires an explicit migration step;
- rejects it and asks for re-provisioning.

Silent interpretation of incompatible configuration is risky.

## Configuration precedence

If ORIGIN supports multiple configuration sources, precedence must be defined.

For example, a system could conceptually have:

```text
compiled safe defaults
        ↓
local persistent configuration
        ↓
approved deployment override
```

The actual order should be implemented and documented once the firmware is available.

## Calibration data

Calibration values are configuration, but they deserve special handling because they affect measurement validity.

Calibration records should identify:

- sensor/device identity;
- calibration date;
- procedure/reference;
- resulting coefficients or offsets;
- firmware/hardware revision where relevant.

Calibration should not be overwritten accidentally by a routine firmware update.

## Secrets

Secrets are not ordinary configuration values.

Do not commit the following to `origin-docs` or other public repositories:

- passwords;
- API tokens;
- private keys;
- SIM PIN/PUK values;
- production certificates;
- private backend credentials.

Public configuration examples should use obvious placeholders.

## Human-readable diagnostics

At startup, firmware should log enough non-sensitive information to make configuration problems visible.

Useful examples include:

- configuration revision;
- device ID;
- enabled sensor set;
- communication mode;
- validation result.

Secrets must be redacted.

## Configuration changes in the field

A field configuration change should be traceable.

For important deployments, record:

- previous revision;
- new revision;
- who approved/applied it;
- timestamp;
- reason for change;
- verification outcome.

This is especially important when configuration affects detection behavior.

## Test configuration

Development/test profiles should be clearly distinguishable from deployment profiles.

A test profile may deliberately use:

- faster sampling;
- verbose logs;
- simulated inputs;
- disabled communications;
- diagnostic modes.

A device should not accidentally be deployed while still using laboratory settings.

## Example conceptual configuration

The following is illustrative only and is **not** the final ORIGIN configuration syntax:

```yaml
device:
  id: ORIGIN-EXAMPLE
  site: EXAMPLE-SITE

sensors:
  radar_a:
    enabled: true
  radar_b:
    enabled: true

monitoring:
  environmental_interval_s: 60

logging:
  level: info
```

It demonstrates structure only. Do not use it as firmware input unless a future release explicitly documents this schema.

## Related pages

See:

- [Firmware](firmware.md)
- [Installation](installation.md)
- [Communications](communications.md)
- [Updates](updates.md)
