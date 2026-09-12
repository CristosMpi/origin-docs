# Connectivity

Connectivity links ORIGIN Core to the rest of the ORIGIN platform. Its purpose is not simply to make the device "online"; it is to move measurements, events, diagnostics and configuration information in a controlled way while allowing the Core to remain useful when a network path is unavailable.

## Connectivity responsibilities

The connectivity subsystem is responsible for transmitting sensor observations and system events; reporting device health and diagnostic state; receiving configuration or control information where supported; retrying or buffering data when delivery fails; distinguishing network failure from sensor failure; supporting secure communication principles; and preserving local operation when remote connectivity is interrupted.

## Local-first behavior

ORIGIN is designed as a field device, so loss of connectivity should not automatically mean loss of sensing.

A simplified model is:

```text
Sensors
   ↓
Local processing
   ↓
Local storage / event queue
   ↓
Available communication path
   ↓
Remote services / operators
```

If the communication path fails, the Core should continue collecting the information that can still be collected safely and retain relevant records for later delivery where storage and firmware support it.

This makes communications an output path rather than a single point of failure for the entire device.

## Communication layers

ORIGIN connectivity can be understood in three layers.

### Device interface

This is the low-level electrical and firmware interface used by Rosetta and any radio or communication peripheral.

Examples may include embedded wireless capabilities of the controller, UART or other serial links to external communication hardware, SIM-related hardware interfaces in Rosetta revisions, and wired development or service connections.

An interface being present on a PCB does not automatically mean the corresponding network feature is fully validated.

### Transport

The transport layer describes how the field unit reaches another system.

Depending on the hardware revision and deployment, this may involve local wireless networking or another communications path. Cellular support is part of Rosetta's development direction, but it should only be documented as a deployed capability once the complete modem, antenna, firmware, subscription and network path have been validated together.

### Application protocol

Above the physical transport, ORIGIN needs a consistent way to represent and exchange information.

The application layer should define message structure; device identity; timestamps; measurement units; event types; health status; configuration version; and acknowledgement and retry behavior where required.

These details belong primarily to the [Software](../software/README.md) chapter.

## Data classes

Not all information has the same urgency.

ORIGIN can classify outgoing information into categories such as:

| Data type | Example | Typical priority |
| --- | --- | --- |
| Alert/event | Detected presence in a monitored zone | High |
| System fault | Sensor missing or power fault | High |
| Telemetry | Environmental measurement | Normal |
| Health | Battery or network status | Normal |
| Log | Debug or maintenance information | Low |
| Configuration | Device settings and version metadata | Controlled |

A priority model helps the system decide what to transmit first after a network outage or when bandwidth is limited.

## Offline buffering

When communication fails, ORIGIN should avoid immediately discarding information.

Where local storage is available, the software can maintain a queue containing event identifier; timestamp; data payload; priority; delivery state; and retry count.

After the connection returns, the system can transmit queued data according to policy.

This design also creates a clear distinction between **not observed** — no event was detected, **observed but not delivered** — the device captured data but the network failed, and **delivered** — the remote system received the information.

## Device identity

Every ORIGIN Core should have a stable device identity independent of temporary network details such as an IP address.

A useful identity model can include device ID; hardware revision; firmware version; deployment/site ID; and module configuration.

This prevents remote records from becoming ambiguous when a device is moved, updated or connected through a different network.

## Time and timestamps

Remote monitoring is only useful if events can be placed in time.

Connectivity therefore depends on a strategy for timestamps. The system should define how time is obtained and what happens if external time synchronization is temporarily unavailable.

Possible concerns include startup without network access; clock drift; queued events created while offline; daylight-saving or timezone handling in user interfaces; and preserving event ordering even when absolute time is uncertain.

Internally, storing timestamps in a consistent machine-readable form is preferable to embedding local display formatting in device messages.

## Reliability

A connection can fail in many ways: network unavailable; access point unreachable; radio peripheral fault; authentication failure; server unavailable; timeout; malformed response; partial upload; and DNS or routing failure.

The firmware should avoid treating every case as identical where diagnostics can distinguish them.

Useful communication health information includes last successful connection; last successful message delivery; current connection state; number of queued messages; recent retry count; and detected interface faults.

## Security principles

Because ORIGIN may monitor sensitive heritage locations, connectivity must be designed with security in mind.

Core principles include do not transmit credentials in plain text; authenticate remote services where supported; use encrypted transport when practical and supported; minimize unnecessary exposed services; separate public documentation from real deployment secrets; avoid hard-coding private credentials in repositories; and design update and configuration paths so unauthorized changes are difficult.

Higher-level cybersecurity strategy is documented under [Centaurus AI → Cybersecurity](../centaurus-ai/cybersecurity.md) and the Software chapter.

## Configuration changes

Remote configuration can be useful, but it also creates risk.

Any remotely changeable setting should have a defined valid range; a version or revision; validation before application; a recovery path if the new configuration is invalid; and logging so operators know what changed.

Critical hardware settings should not be changed merely because a remote message contains a new value.

## Development and service connectivity

Field connectivity and developer access are different use cases.

During development, engineers may need direct access for firmware upload; serial debugging; raw sensor inspection; configuration; and test automation.

Those interfaces should not automatically remain open or exposed in the same way during a deployed configuration.

## Validation

Connectivity testing should include more than a successful message sent on a laboratory Wi-Fi network.

Tests should cover cold start with network available; cold start with network unavailable; connection loss during operation; recovery after extended outage; queued-message delivery; malformed or rejected messages; authentication failure; server-side downtime; power interruption during transmission; and realistic deployment signal conditions.

## What remains revision-specific

This page intentionally does not declare a single mandatory network technology for every ORIGIN Core. Final deployed connectivity depends on the exact Rosetta revision, firmware, radio hardware and site conditions.

For implementation details, continue to [Software → Communications](../software/communications.md), [Rosetta → Interfaces](../rosetta/interfaces.md), [Rosetta → Microcontroller](../rosetta/microcontroller.md), and [Testing & Validation](../testing-validation/README.md).
