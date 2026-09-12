# Software Architecture

ORIGIN software is organized as a layered system so that hardware access, device logic, communications, higher-level analysis, and operator-facing behavior can evolve independently.

The architecture is intentionally modular. A sensor driver should not need to know how a remote dashboard renders data, and a remote service should not need to know the electrical details of Rosetta.

## Architectural goals

The software architecture is designed around the following goals **modularity** — replace or revise components without rewriting the entire stack; **traceability** — preserve where an observation came from and how it was interpreted; **resilience** — continue safe local operation during partial failures; **testability** — make subsystems independently testable; **configuration-driven behavior** — avoid unnecessary source edits per deployment; **diagnostics** — expose health and failure states explicitly; and **security** — reduce unnecessary trust and avoid embedding secrets in public code or docs.

## Layer model

A conceptual architecture is:

```text
┌──────────────────────────────────────────┐
│ Operator / application layer             │
│ Dashboards, alerts, reporting, workflows │
├──────────────────────────────────────────┤
│ Centaurus AI / analysis layer            │
│ Correlation, interpretation, risk logic  │
├──────────────────────────────────────────┤
│ Remote data and event services           │
│ Ingestion, storage, normalization        │
├──────────────────────────────────────────┤
│ Communications layer                     │
│ Transport, retry, session/status logic   │
├──────────────────────────────────────────┤
│ Device services                          │
│ Acquisition, validation, events, health  │
├──────────────────────────────────────────┤
│ Drivers / hardware abstraction           │
│ Sensors, storage, modem, buses            │
├──────────────────────────────────────────┤
│ Rosetta v2 hardware                      │
└──────────────────────────────────────────┘
```

Not every deployment needs every layer to run on a separate physical machine. The diagram describes responsibility boundaries, not necessarily network boundaries.

## Hardware abstraction

The lowest software layer translates physical interfaces into predictable software operations.

A driver should ideally provide functions equivalent to:

```text
initialize()
read()
health()
configure()
reset()
```

The exact APIs depend on the firmware framework, but the design principle is stable: device logic should interact with a clean interface rather than manipulate every register or serial command directly throughout the codebase.

## Device services

Above the drivers sits the main embedded application logic.

This layer is responsible for scheduling acquisition; validating returned data; associating time and source identity; maintaining subsystem health state; applying local thresholds or rules where appropriate; creating normalized observations; creating structured events; and preparing output for logging or transport.

## Observation model

A normalized observation should carry enough context to be useful outside the sensor driver.

A conceptual record could include:

```text
observation
├── device_id
├── source_id
├── timestamp
├── type
├── value / state
├── unit (when applicable)
├── quality / validity
└── metadata
```

This is a conceptual model, not a declaration of the final wire format.

## Event model

Events represent relevant changes, conditions, or system states rather than raw samples.

Examples may include presence detected; sensor unavailable; configuration loaded; communication restored; power state changed; threshold crossed; and device restarted.

A good event model includes enough context to explain what happened without requiring access to hidden internal state.

## Communications boundary

The communications layer receives structured records from device services and handles transport concerns separately.

This separation matters because transport can fail independently of acquisition.

For example:

```text
Sensors: healthy
Acquisition: healthy
Local buffer: healthy
Remote transport: offline
```

That state is fundamentally different from a sensor failure and should be represented differently.

## Remote ingestion

On the remote side, incoming data should be validated again before being accepted as trusted application data.

Useful checks include device identity; schema or message version; timestamp sanity; expected source type; duplicate handling; malformed message rejection; and authentication/authorization where implemented.

The exact backend implementation is not yet documented here because the authoritative backend source has not been connected.

## Centaurus integration

Centaurus AI sits above the base data path rather than replacing it.

That means ORIGIN should be able to preserve raw or normalized observations even when higher-level analysis is unavailable.

Conceptually:

```text
Observation
   ├── stored / logged
   ├── used for deterministic rules
   └── supplied to Centaurus when relevant
```

This improves explainability and prevents an AI layer from becoming the only source of truth about what the sensors actually reported.

## State machines

Several ORIGIN software functions are easier to reason about when implemented as explicit state machines.

Examples include:

### Sensor state

```text
OFFLINE
  ↓
INITIALIZING
  ↓
HEALTHY
  ↘
   DEGRADED / ERROR
```

### Communication state

```text
DISCONNECTED
    ↓
CONNECTING
    ↓
CONNECTED
    ↓
RETRYING
```

### Update state

```text
IDLE
 ↓
VALIDATING
 ↓
INSTALLING
 ↓
VERIFYING
 ↓
SUCCESS / ROLLBACK
```

Explicit states make logs, tests, and recovery behavior easier to understand.

## Failure isolation

One subsystem failure should not automatically bring down unrelated functions.

Examples include a radar failure should not prevent environmental sensors from being sampled, remote connectivity loss should not erase local health state, a malformed remote message should not crash the acquisition loop, and optional modules should fail gracefully if absent.

## Logging

Logs should support development and field diagnosis without exposing secrets.

Useful log categories include startup; hardware initialization; sensor state changes; communication state changes; configuration changes; update events; and error/recovery events.

Passwords, tokens, private keys, and sensitive credentials should never be written to normal logs.

## Time handling

Time is essential for correlating observations.

The software should distinguish between device uptime, local clock time, synchronized absolute time where available, and timestamps received from external systems.

If absolute time is not trustworthy, the data record should not pretend otherwise.

## Compatibility

Software releases should document compatibility with Rosetta hardware revision; sensor configuration; storage format; communication schema; and Centaurus/backend expectations.

This is especially important as ORIGIN evolves between prototype revisions.

## Related pages

See [Firmware](firmware.md); [Communications](communications.md); [Data Pipeline](data-pipeline.md); [Configuration](configuration.md); and [Centaurus AI](../centaurus-ai/README.md).
