# Data Pipeline

The ORIGIN data pipeline defines how physical sensor output becomes structured, validated information that can be logged, transmitted, analyzed, and presented to operators.

The core principle is simple: **preserve provenance and meaning at every stage**. A raw sensor response, a normalized observation, and a higher-level event are not the same thing and should not be mixed together.

## Pipeline overview

A conceptual ORIGIN data path is:

```text
Physical condition
      ↓
Sensor hardware
      ↓
Driver / parser
      ↓
Validation
      ↓
Normalized observation
      ↓
Local context / event logic
      ↓
Local storage or queue
      ↓
Transport
      ↓
Remote ingestion
      ↓
Storage / analytics / Centaurus
      ↓
Operator-facing information
```

Each stage adds context but should retain enough information to trace the result back to the original source.

## Stage 1 — sensor acquisition

The first stage retrieves information from physical sensors and subsystems.

Depending on the device, acquisition may be:

- periodic;
- event-driven;
- stream-based;
- polled through a bus;
- received over a serial interface.

The acquisition layer should attach source identity immediately so readings from different sensors cannot be confused later.

## Stage 2 — parsing

Device-specific data is translated into software values.

Parsing may include:

- decoding frames;
- extracting fields;
- converting byte order;
- translating status bits;
- applying documented units;
- rejecting malformed records.

Parsing does not automatically make a value trustworthy.

## Stage 3 — validation

Validation determines whether the parsed observation is fit for use.

Checks can include:

- communication integrity;
- expected response length;
- valid status flags;
- plausible range;
- age/staleness;
- known source;
- required fields present.

A failed validation should produce a health/quality state rather than a fake measurement.

## Stage 4 — normalization

Different sensors express information differently. Normalization gives the rest of ORIGIN a consistent conceptual format.

A normalized record should retain fields such as:

```text
device identity
source identity
observation type
value/state
unit where applicable
observation timestamp
quality/validity
software/schema version
relevant metadata
```

The final serialized schema will be documented from the implementation.

## Stage 5 — local context

Some observations are useful only when interpreted in context.

For example:

- a radar changes from clear to occupied;
- a value crosses a configured threshold;
- a sensor stops reporting;
- communication returns after an outage.

The local software can convert these state changes into structured events while preserving the underlying observation.

## Measurements vs events

A useful distinction is:

| Type | Purpose |
| --- | --- |
| Measurement/observation | Represents what a sensor or subsystem reported |
| Health record | Represents whether a source is operating correctly |
| Event | Represents a relevant change or condition |
| Derived result | Represents a computed or AI-assisted interpretation |

Keeping these categories separate improves explainability.

## Provenance

Every meaningful record should answer:

- Which ORIGIN unit produced this?
- Which sensor/subsystem produced it?
- When was it observed?
- Which software/configuration version interpreted it?
- Was it valid, degraded, or estimated?
- Was it measured directly or derived later?

This is especially important for testing and cultural-heritage deployments where data may be reviewed after an incident.

## Time

The pipeline should distinguish different timestamps where necessary.

For example:

```text
observed_at
queued_at
sent_at
received_at
processed_at
```

Not all are required in every record, but the design must avoid replacing the original observation time with the eventual upload time after an outage.

## Local buffering

When remote communication is unavailable, the pipeline may store pending records locally if storage allows.

Buffering policy should define:

- which records are retained;
- maximum capacity;
- prioritization;
- overflow behavior;
- persistence across reboot;
- resend order;
- expiration/staleness rules.

Health and high-value events may require stronger retention than routine telemetry.

## Duplicate handling

Retries can produce duplicate messages.

The pipeline should support a strategy for detecting or tolerating duplicates, potentially using:

- message IDs;
- device sequence numbers;
- source + timestamp + record identity;
- idempotent remote ingestion.

The exact mechanism will depend on the final protocol.

## Schema versioning

Data formats evolve as ORIGIN evolves.

Every persistent or transmitted structured format should have a versioning strategy.

A schema change may affect:

- field names;
- units;
- source identifiers;
- status values;
- nested structure;
- event meanings.

Remote services should reject unknown incompatible schemas rather than silently misinterpreting data.

## Units

Engineering data must use explicit units.

Values should never depend on undocumented assumptions such as whether temperature is Celsius or Fahrenheit, or whether distance is millimeters or meters.

Unit conversion should occur at a defined layer and be testable.

## Missing data

Missing data is information.

The pipeline should distinguish:

- no event occurred;
- value is unavailable;
- sensor timed out;
- sensor is disabled;
- communication path failed;
- record was rejected as invalid.

Using `0` for all of these would destroy meaning.

## Derived values

Some values may be calculated from one or more observations.

Derived records should identify:

- inputs used;
- algorithm/version where relevant;
- calculation timestamp;
- quality/uncertainty if applicable.

This is particularly important for AI-assisted outputs.

## Centaurus AI boundary

Centaurus consumes validated structured information from the ORIGIN pipeline.

A recommended conceptual relationship is:

```text
Normalized observations ───────┐
Health/status records ─────────┼─→ Centaurus analysis
Deterministic events ──────────┘

Original records remain separately traceable.
```

An AI result should not overwrite the underlying observation.

## Operator presentation

The final stage presents information in a form useful to a person.

A dashboard or notification may simplify the data, but it should still preserve access to important context such as:

- source device;
- time;
- event type;
- subsystem health;
- confidence/analysis status where relevant.

## Data retention

Retention requirements depend on deployment, storage capacity, privacy, and institutional needs.

The software architecture should make retention policy explicit rather than keeping data indefinitely by accident.

Potential data classes may need different retention:

- routine environmental telemetry;
- system health logs;
- security-oriented events;
- diagnostic debug logs;
- AI-derived results.

## Privacy and minimization

ORIGIN should collect and retain only information needed for the monitoring purpose.

Radar-based presence data, even without recognizable imagery, can still describe human activity and should be treated responsibly.

The pipeline should therefore support data minimization and deployment-specific retention rules.

## Pipeline testing

Testing should verify the entire chain, not only individual sensors.

Useful tests include:

1. inject a known sensor observation;
2. verify normalized value and unit;
3. verify source identity;
4. verify event behavior;
5. interrupt communication;
6. confirm queue behavior;
7. reconnect;
8. verify original timestamp is preserved;
9. verify duplicate handling;
10. confirm remote record matches the original observation.

## Related pages

See:

- [Architecture](architecture.md)
- [Firmware](firmware.md)
- [Communications](communications.md)
- [Centaurus AI](../centaurus-ai/README.md)
- [Testing & Validation](../testing-validation/README.md)
