# Architecture

Centaurus AI is designed as a **context and decision-support layer** that sits above ORIGIN's embedded sensing and communications stack.

Its architecture separates data acquisition, validation, analysis, event generation, and operator presentation so that faults in one stage do not silently contaminate another.

## Architectural position

The end-to-end ORIGIN software path can be represented as:

```text
Sensors
   ↓
Rosetta firmware
   ↓
Validated observations
   ↓
Transport / buffering
   ↓
Normalization
   ↓
Centaurus analysis
   ↓
Event logic
   ↓
Operator-facing output
```

Centaurus begins only after lower-level software has already established basic data validity and source identity.

## Core layers

A useful Centaurus architecture can be divided into six logical layers.

### 1. Ingestion

The ingestion layer receives structured observations from ORIGIN devices or intermediate services.

Responsibilities include accepting supported message versions; checking required fields; verifying timestamps and source identifiers; rejecting malformed payloads; and preserving original observations for traceability.

### 2. Normalization

Different sensors can produce data with different units, rates, and semantics.

Normalization converts incoming observations into stable internal representations so later analysis does not depend on device-specific formatting.

Normalization can include unit conversion; consistent timestamp handling; source naming; quality-state mapping; range validation; and event-type normalization.

### 3. Context engine

The context engine associates observations with information such as device; zone; site; sensor type; recent event history; deployment configuration; and expected operating state.

This allows Centaurus to interpret the same sensor reading differently depending on location and situation.

### 4. Analysis layer

The analysis layer evaluates observations using one or more techniques.

Potential methods include rules; thresholds; temporal windows; statistical comparison; anomaly detection; sensor fusion; and trained machine-learning models.

The implementation should use the simplest method that reliably solves each problem.

### 5. Decision layer

The decision layer converts analysis results into operator-relevant events.

It can determine event category; severity; confidence; whether additional evidence is needed; whether an event should be merged with an existing event; and whether a notification is warranted.

### 6. Audit and output layer

Every important event should remain explainable after it occurs.

The audit/output layer therefore preserves event ID; source observations; analysis version; configuration version; decision result; timestamps; and operator acknowledgement or later disposition where available.

## Separation between deterministic and learned behavior

Centaurus should not hide all logic behind an opaque model.

A preferred pattern is:

```text
Input validation
      ↓
Deterministic preprocessing
      ↓
Context building
      ↓
Optional ML/statistical analysis
      ↓
Deterministic safety rules
      ↓
Event output
```

This gives the project clear places to test behavior and enforce safety constraints.

## State management

Many meaningful events depend on time rather than on a single sample.

Centaurus may therefore maintain short-lived or persistent state such as last healthy observation; previous presence state; rolling environmental baseline; duration of an abnormal condition; active event state; and recent communication failures.

State must be versioned and recoverable enough that service restarts do not create misleading conclusions.

## Event correlation

Independent observations can refer to the same real-world occurrence.

For example:

```text
Radar A detects presence
Radar B detects movement
Door-area vibration changes
        ↓
Correlation window
        ↓
Single structured event
```

Correlation helps reduce notification noise and gives operators a more coherent picture.

## Confidence model

Confidence should reflect evidence quality rather than be used as decorative metadata.

Factors may include sensor health; agreement between sensors; amount of evidence; model confidence; data freshness; missing observations; and known deployment conditions.

A confidence score should never erase uncertainty that originates from unhealthy sensors.

## Data-quality propagation

Quality states should propagate through the complete architecture.

For example:

```text
Sensor missing
   ↓
Observation quality = unavailable
   ↓
Analysis marked incomplete
   ↓
Decision confidence reduced
   ↓
Operator sees degraded evidence
```

The alternative—silently treating missing data as zero—is unsafe and misleading.

## Deployment boundaries

Centaurus can conceptually be deployed in several ways: locally near ORIGIN devices, on a site gateway, on a remote server, and as a hybrid local/remote system.

The exact production deployment is not fixed in this documentation because it depends on the final implementation, connectivity requirements, performance constraints, and site policies.

## Local versus remote processing

Local processing offers advantages such as lower latency, continued operation during connectivity loss, and reduced external data transfer.

Remote processing can offer more compute resources, centralized fleet analysis, simpler model updates, and long-term cross-device analytics.

A hybrid design can combine both.

## Versioning

Each analysis result should be attributable to a specific software state.

Useful version identifiers include firmware version; message schema version; Centaurus application version; model version; ruleset version; and site-configuration version.

This becomes essential when comparing behavior before and after an update.

## Failure isolation

Centaurus should fail in ways that remain visible.

Failure isolation should remain explicit. Invalid input should be rejected rather than guessed, unavailable models should trigger a degraded state, broken external connectivity should not delete local evidence, unsupported schema versions should produce clear compatibility errors, and analysis failures should never be represented as normal events.

## Observability

A maintainable AI system needs operational telemetry about itself.

Centaurus should expose or record information such as ingestion success/failure rates; queue depth; processing latency; rejected messages; model/rule errors; active version identifiers; degraded services; and event-generation counts.

This is system observability, not surveillance of end users.

## Security boundary

The AI layer must not assume all inputs are trustworthy simply because they came through ORIGIN infrastructure.

The architecture should verify identity, authorization, and message integrity at appropriate boundaries. See [Cybersecurity](cybersecurity.md).

## Implementation status

This page defines the intended architecture and design constraints. Exact service names, programming languages, database technologies, model-serving frameworks, queue systems, and deployment topology should be added only from the verified Centaurus source code and deployment configuration.

## Related documentation

See [Detection & Analysis](detection-and-analysis.md); [Decision Logic](decision-logic.md); [Data Processing](data-processing.md); [Cybersecurity](cybersecurity.md); and [Software Architecture](../software/architecture.md).
