# Firmware

The ORIGIN firmware is the embedded software layer that runs on Rosetta and directly manages the hardware installed in ORIGIN Core.

Its job is not simply to "read sensors." It is responsible for bringing the device into a known state, supervising connected subsystems, validating data, maintaining health information, creating structured observations, handling communication, and recovering from predictable failure conditions.

## Current platform

Rosetta v2 is built around an ESP32-class controller. The exact firmware framework, build system, repository path, and versioning convention will be added once the authoritative source repository is connected.

This page therefore documents the firmware responsibilities and expected structure without inventing implementation details.

## Startup sequence

A robust startup sequence should make initialization explicit.

Conceptually:

```text
Power applied
    ↓
Boot / reset cause recorded
    ↓
Core runtime initialized
    ↓
Configuration loaded
    ↓
Storage checked
    ↓
Hardware interfaces initialized
    ↓
Sensors initialized
    ↓
Communication subsystem initialized
    ↓
Health state established
    ↓
Normal monitoring loop
```

Failures during startup should be logged and reflected in subsystem health rather than silently ignored.

## Main firmware responsibilities

The embedded firmware should cover at least the following areas.

### Hardware initialization

Initialize buses and serial interfaces.

Configure GPIO safely.

Establish known power/control states.

Initialize storage where present.

Identify optional hardware.

Avoid enabling subsystems in an undefined sequence.

### Sensor drivers

Each sensor driver should isolate device-specific commands and timing from the rest of the application.

A driver should normally expose capabilities such as initialization; reading or polling; configuration; health reporting; restart/recovery; and conversion into normalized values.

### Scheduler

Not every sensor needs to run at the same rate.

The firmware should support a scheduling model that distinguishes periodic measurements; continuous or stream-oriented sensors; event-driven inputs; health checks; communication maintenance; and background storage or retry tasks.

### Validation

Raw sensor output should be checked before being promoted to a trusted observation.

Validation may include expected message length; checksum or integrity checks where supported; range validation; timeout detection; stale-data detection; impossible-state rejection; and source identity.

### Health supervision

Subsystem health should be tracked independently.

A conceptual internal state might look like:

```text
system_health
├── controller
├── storage
├── power
├── radar_a
├── radar_b
├── radar_c
├── environmental_sensor_x
└── communications
```

This makes it possible to describe a partially degraded device instead of reducing everything to "online" or "offline."

## Main loop / task model

The exact execution model will depend on the final firmware framework, but the logical tasks remain similar:

```text
Acquire sensors
      ↓
Validate
      ↓
Update health
      ↓
Normalize observations
      ↓
Evaluate local event rules
      ↓
Record / queue
      ↓
Transmit when possible
```

Tasks that can block for long periods should not prevent critical acquisition or watchdog servicing.

## Watchdog and recovery

An unattended field device should have defined recovery behavior.

Useful recovery mechanisms include task or system watchdogs; communication retry with bounded backoff; driver-level sensor reset; peripheral reinitialization; and controlled device restart after unrecoverable states.

Recovery should be logged so that repeated failures can be diagnosed later.

## Reset cause

On every boot, firmware should record the available reset reason.

Examples may include power-on reset; software reset; watchdog reset; brownout; and update-related restart.

Repeated unexpected resets are an important diagnostic signal.

## Local storage

Where storage is available, firmware can use it for buffered observations; diagnostic logs; configuration snapshots; update metadata; and temporary offline queues.

Storage failures must be represented separately from communication failures.

## Sensor identity

Each connected sensor should have a stable software identity.

For example, a three-radar arrangement should not produce three anonymous streams. The data should preserve which physical radar produced the observation.

The final names should match the mechanical configuration once fixed.

## Event generation

Firmware may generate deterministic local events from known conditions.

Examples include sensor unavailable; presence state changed; threshold exceeded; power condition changed; communication lost/restored; device rebooted; and configuration changed.

Higher-level AI analysis should remain separable from these deterministic events.

## Safe defaults

If configuration is missing or invalid, firmware should fail into a defined safe/default mode rather than operating with random memory or partial settings.

Safe behavior may include disable unsupported interfaces, use conservative acquisition settings, refuse to enable a feature that lacks required configuration, and report configuration errors clearly.

## Debug builds vs deployment builds

Development firmware may expose additional logging or test commands that are inappropriate for deployment.

Release documentation should distinguish development/debug build, validation build, and deployment/release build.

Diagnostic conveniences must not accidentally become permanent security weaknesses.

## Firmware version reporting

Every unit should expose or log an identifiable firmware version.

A useful version record should include:

```text
firmware_version
hardware_revision
build_identifier
build_date (when reproducible/useful)
configuration_version
```

A source commit identifier is especially useful during testing.

## Testing firmware

Firmware validation should include:

### Unit / driver testing

Valid responses.

Invalid responses.

Timeouts.

Disconnected sensor.

Restart recovery.

### Integration testing

Multiple sensors active simultaneously.

Storage plus communications.

Repeated reconnects.

Long-duration acquisition.

### Fault injection

Deliberately test sensor unplugged; communication unavailable; malformed input; storage failure; repeated reboot; and partial configuration.

### Soak testing

Run a representative device continuously to detect memory leaks, task stalls, queue growth, and intermittent communication faults.

## What still needs authoritative source material

The following will be added when the firmware repository is available: language/framework; toolchain; exact build commands; source-tree structure; task names; libraries/dependencies; pin definitions; actual message schemas; and release version history.

## Related pages

See [Architecture](architecture.md); [Installation](installation.md); [Configuration](configuration.md); [Communications](communications.md); and [Rosetta](../rosetta/README.md).
