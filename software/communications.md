# Communications

ORIGIN communications connect the device-side monitoring system to remote services, operators, and higher-level analysis without making remote connectivity a prerequisite for every local function.

The final protocol stack, backend endpoint structure, authentication mechanism, and message schema will be documented from the authoritative software source. This page focuses on the communication architecture and the rules the implementation should follow.

## Communications goals

The communications subsystem should provide:

- reliable transfer of observations and events;
- explicit connection/health state;
- bounded retry behavior;
- offline tolerance where local storage permits;
- message traceability;
- compatibility/version identification;
- secure handling of credentials;
- separation between transport failure and sensor failure.

## Separation from acquisition

Sensor acquisition should not depend directly on an active remote connection.

Conceptually:

```text
Sensors
   ↓
Local acquisition
   ↓
Validation
   ↓
Observation queue/buffer
   ↓
Communications
   ↓
Remote service
```

If the last step fails, the earlier steps should remain operational where possible.

## Connection state

Communications should expose an explicit state rather than a single boolean flag.

For example:

```text
DISABLED
DISCONNECTED
CONNECTING
CONNECTED
DEGRADED
RETRYING
ERROR
```

This state should be available to diagnostics and, where useful, transmitted later as a system event.

## Transport independence

ORIGIN should treat the transport layer as replaceable where practical.

The hardware platform may support different physical/network paths depending on revision and deployment. The data model above transport should therefore not assume one specific bearer.

A normalized observation should remain the same logical observation whether it eventually travels over Wi-Fi, cellular connectivity, a local gateway, or another supported path.

## Message categories

A useful communication model separates several message categories.

### Telemetry

Periodic or event-driven sensor observations.

### Events

Structured records describing relevant changes such as presence, subsystem failure, reboot, or communication restoration.

### Health/status

Device and subsystem health information.

### Configuration control

Approved configuration changes or synchronization, if remote configuration is implemented.

### Update control

Release/update metadata, if remote software updating is implemented.

Control-plane messages should receive stricter validation than ordinary telemetry.

## Message identity

Each outgoing record should be traceable to a source.

Conceptually useful fields include:

```text
device_id
message_id or sequence
source_id
message_type
timestamp
schema_version
payload
```

The final wire schema may differ, but these concepts help with duplication, debugging, and compatibility.

## Delivery semantics

Field networks can disconnect, duplicate requests, or reconnect unpredictably.

ORIGIN should therefore define how it treats:

- messages sent but not acknowledged;
- duplicate retransmission;
- out-of-order arrival;
- stale queued data;
- reconnect after long outage.

Remote services should not assume that every message arrives exactly once unless the chosen implementation truly guarantees it.

## Offline buffering

Where local storage permits, ORIGIN should be able to queue important records during an outage.

A buffer policy must define:

- maximum size;
- what happens when full;
- priority between health/events and routine telemetry;
- retention period;
- resend ordering;
- duplicate protection.

Important fault and security-oriented events may deserve different priority from high-frequency routine samples.

## Retry strategy

Unbounded rapid reconnect loops waste energy and can overload both the device and remote service.

A robust retry policy can use:

- limited immediate retries;
- increasing delay/backoff;
- maximum delay;
- reset after successful connection;
- explicit degraded state after repeated failures.

The exact values should be measured against real deployment conditions.

## Time and ordering

Transmission time is not necessarily observation time.

If a record was collected while offline, it should preserve the original observation timestamp where trustworthy.

This allows the remote side to distinguish:

```text
observed_at: 10:04
received_at: 10:27
```

That difference matters during outages.

## Security

Production communication credentials and secrets must not be published in this repository.

The implementation should follow principles such as:

- authenticate devices/services where appropriate;
- encrypt data in transit when supported by the chosen protocol;
- validate certificates/peers correctly;
- avoid hard-coded reusable secrets in public source;
- limit permissions to what the device requires;
- support credential replacement when practical.

Exact security implementation belongs in the authoritative code and deployment documentation.

## Input validation

Remote input should be treated as untrusted until validated.

This includes:

- configuration messages;
- update metadata;
- commands;
- time synchronization data;
- server responses.

Malformed or unexpected remote input must not crash the monitoring loop.

## Rate control

Communication frequency affects:

- power consumption;
- cellular/network usage;
- backend load;
- event latency;
- storage requirements.

ORIGIN may therefore use different policies for different data classes—for example immediate transmission of an important event but batched or periodic routine measurements.

## Diagnostics

Useful communications diagnostics include:

- current transport state;
- last successful connection;
- last successful transmission;
- pending queue depth;
- retry count;
- error category;
- signal/network metrics when available and safe to expose.

Do not log credentials.

## Testing

Communications testing should include:

### Normal operation

- successful connection;
- telemetry delivery;
- event delivery;
- reconnect after controlled restart.

### Network loss

- disconnect during monitoring;
- long outage;
- repeated short outages;
- restoration with queued data.

### Backend problems

- timeout;
- service unavailable;
- invalid response;
- authentication failure;
- schema mismatch.

### Queue behavior

- queue grows during outage;
- queue survives restart if designed to persist;
- full-buffer policy works as intended;
- resend does not generate uncontrolled duplicates.

## Communications and Centaurus

Centaurus should consume structured data through a defined software boundary rather than reading physical sensors directly.

This allows the same validated observation stream to serve storage, deterministic rules, AI analysis, and operator tools.

## Related pages

See:

- [Architecture](architecture.md)
- [Data Pipeline](data-pipeline.md)
- [Configuration](configuration.md)
- [Updates](updates.md)
- [ORIGIN Core → Connectivity](../origin-core/connectivity.md)
