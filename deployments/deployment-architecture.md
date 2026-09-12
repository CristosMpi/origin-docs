# Deployment Architecture

ORIGIN deployment architecture defines how one or more ORIGIN units are arranged at a heritage site and how those units interact with local sensors, modules, communications infrastructure, software services, Centaurus AI, and human operators.

The architecture must be designed per site. A museum gallery, an outdoor archaeological area, a monument, and a temporary excavation do not have the same geometry or operational constraints.

## Architectural layers

A deployment can be viewed as five layers.

### 1. Site layer

The physical heritage environment protected objects or areas; walls and structures; visitor routes; staff access routes; environmental exposure; power availability; radio environment; and mounting restrictions.

### 2. Device layer

One or more ORIGIN Core units containing Rosetta electronics; presence sensors; environmental sensing; local storage/processing; and optional modules.

### 3. Communications layer

The path between the field units and higher-level services.

Depending on the final configuration, this layer may include local wireless connectivity, cellular connectivity, or other approved transports.

The public documentation intentionally does not publish credentials, secrets, private endpoints, or sensitive network configuration.

### 4. Processing layer

Software receives, validates, timestamps, stores, and interprets data from the deployed units.

Centaurus AI may provide higher-level analysis, correlation, anomaly detection, or prioritization where enabled and validated.

### 5. Operator layer

Human users review health states, events, warnings, and maintenance needs.

Human operators remain part of the decision chain, particularly where an event could lead to physical intervention at a heritage site.

## Single-unit deployment

The simplest configuration uses one ORIGIN Core.

```text
Monitored zone
    ↓
ORIGIN Core
    ↓
Communications
    ↓
ORIGIN software
    ↓
Operator
```

This arrangement is useful for a bounded area, pilot test, or isolated monitoring objective.

Its main limitation is coverage: one device position cannot automatically be assumed to observe every relevant area around a complex site.

## Multi-unit deployment

A multi-unit deployment uses several ORIGIN units to cover different zones.

```text
Zone A ── ORIGIN 01 ─┐
Zone B ── ORIGIN 02 ─┤
Zone C ── ORIGIN 03 ─┼── communications ── software / Centaurus ── operator
Zone D ── ORIGIN 04 ─┤
Zone E ── ORIGIN 05 ─┘
```

This model is relevant to the planned five-unit Durrës pilot.

Multiple units enable broader site coverage; zone-specific sensor orientation; comparative testing; redundancy of observations in selected areas; distributed environmental monitoring; and better localization of events by source unit.

## Unit independence

A deployment should remain understandable even when one unit fails.

Each ORIGIN unit therefore needs stable identity; independent health reporting; independent timestamped observations; local fault states; configuration version; and known location/zone association.

A missing device should produce a degraded deployment state, not silently disappear from the system.

## Zone model

Rather than treating a site as one undifferentiated area, ORIGIN can associate units and sensors with logical zones.

Examples include might include:

```text
ZONE_ENTRANCE
ZONE_GALLERY_A
ZONE_EXTERIOR_NORTH
ZONE_STORAGE_APPROACH
```

These are only examples. Actual zone names should be site-approved and should avoid exposing sensitive security information in public records.

A zone definition should include physical purpose; associated device(s); associated sensors; expected normal activity; relevant alert rules; and maintenance access notes.

## Sensor geometry

Sensor coverage is a geometric property of the installed system.

For the three C4001 mmWave sensors used in the current ORIGIN Core concept, deployment design must consider mounting direction; enclosure orientation; wall reflections; nearby objects; overlap; blind areas; target approach direction; and mounting height.

The correct architecture is therefore created from measured coverage, not from a drawing alone.

## Power architecture

Each deployed unit must have a defined energy architecture.

Possible configurations include battery-supported operation, solar-assisted operation, fixed external power, and hybrid arrangements.

The deployment record should identify which configuration is used per unit.

For solar configurations, the deployment plan must account for panel orientation; shading; seasonal sun angle; support structure; cable routing through the hollow third support where used; charging-system behavior; and low-energy recovery.

A system should not be commissioned as autonomous until its energy behavior has been observed under representative conditions.

## Communications architecture

A communications design should answer four questions:

1. How does a field unit transmit data?
2. What happens when that path fails?
3. How does the system identify delayed/replayed data?
4. How does an operator know the device is offline?

The architecture should support graceful degradation.

A temporary communications failure should not automatically destroy local observations. Where supported by the implementation, buffering and later synchronization should preserve data provenance and timing.

## Time synchronization

Multi-unit deployments depend on meaningful timestamps.

Time-related records should distinguish measurement time, local record time, transmission time, and server receipt time.

This is especially important when connectivity is intermittent, because an event received later may have occurred much earlier.

## Data identity

Every record should be traceable to its source.

A normalized record should be able to preserve fields conceptually equivalent to:

```text
site_id
device_id
sensor_id
measurement_type
measurement_time
value_or_event
quality_state
configuration_version
firmware_version
```

The exact implemented schema belongs in the Software documentation once finalized.

## Health architecture

Deployment health is more than "online" or "offline."

Useful health categories include device reachable; firmware running; power healthy; sensor healthy; communications healthy; data current; configuration valid; module healthy; and time synchronized.

A device may be reachable while one sensor is failed. The operator interface should preserve this distinction.

## Event architecture

A raw sensor observation is not necessarily an alert.

Conceptually:

```text
Raw observation
    ↓
Validation
    ↓
Context
    ↓
Correlation
    ↓
Rule / decision logic
    ↓
Event classification
    ↓
Operator presentation
```

This separation reduces the risk that a single noisy input creates an exaggerated system-level conclusion.

## Centaurus AI in deployments

Centaurus AI may consume records from one or multiple ORIGIN units.

Potential functions include correlating events across zones; identifying unusual patterns; prioritizing operator attention; comparing current data with site baselines; and detecting device-health anomalies.

Centaurus must not be treated as infallible. Its outputs should remain versioned, reviewable, and tied to the underlying evidence.

See [Centaurus AI](../centaurus-ai/README.md).

## Local vs centralized behavior

A resilient deployment should define which functions require remote services and which functions remain local.

Local functions may include sensor acquisition; basic validation; health monitoring; temporary storage; and local event generation.

Centralized functions may include multi-device correlation; dashboards; long-term storage; advanced analysis; and fleet management.

The exact implementation depends on the software revision.

## Physical security

The monitoring system itself can become a target.

Deployment architecture should consider tamper-resistant placement; protected cabling; concealed or controlled service access; fastener selection; detection of unexpected device movement where supported; and avoiding publicly documented vulnerable mounting details.

## Privacy and data minimization

Presence monitoring should be configured for the minimum information required by the site objective.

ORIGIN's radar-based sensing can provide presence information without inherently requiring identifiable camera imagery, but occupancy and behavioral data can still be sensitive.

The deployment architecture should define what is collected; why it is needed; how long it is retained; who can access it; and what is published.

## Architecture record

Each real deployment should produce a versioned architecture record containing site identifier; device count; device-to-zone mapping; module configuration; power configuration; communications configuration; sensor orientation summary; software/firmware baseline; operator workflow; and commissioning status.

Sensitive security details can be kept in restricted documentation while the public architecture remains high-level.

## Change management

Once a deployment is commissioned, architectural changes should be recorded.

Examples include moving a device; changing sensor orientation; adding a module; changing communications transport; replacing Rosetta hardware; changing calibration; and changing alert logic.

After a significant change, relevant commissioning tests should be repeated.

## Related documentation

[Durrës Pilot](durres-pilot.md), [Installation & Deployment](../installation-deployment/README.md), [Software Architecture](../software/architecture.md), [Centaurus AI Architecture](../centaurus-ai/architecture.md), and [Testing & Validation](../testing-validation/README.md).
