# Data Processing

Centaurus depends on a reliable data-processing path between ORIGIN devices and the analysis layer. The purpose of this path is to preserve meaning, quality, provenance, and timing as observations move through the system.

## Processing stages

A typical Centaurus data path is:

```text
Observation received
      ↓
Schema validation
      ↓
Source / timestamp checks
      ↓
Normalization
      ↓
Quality-state propagation
      ↓
Context enrichment
      ↓
Feature / event preparation
      ↓
Analysis
      ↓
Decision output
      ↓
Storage / operator presentation
```

Each stage should be testable independently.

## Schema validation

Every input should conform to a known schema version.

A structured observation should generally include message or observation ID; device identity; sensor identity; timestamp; observation type; value or event payload; units where applicable; quality/health state; and firmware/schema version.

Messages missing required fields should not be guessed into completeness.

## Source identity

The data-processing layer should preserve where every observation originated.

Source identity allows operators and developers to determine which ORIGIN unit and physical sensor produced a record, whether that source was healthy at the time, and which firmware version generated it.

This is necessary for debugging and auditability.

## Time handling

Time-related errors can corrupt event interpretation.

The processing path should distinguish between observation time, receipt time, processing time, and event creation time.

If device time is uncertain or unsynchronized, that uncertainty should remain visible rather than silently replacing the timestamp with server receipt time.

## Ordering

Network delivery can be delayed or out of order.

Centaurus should therefore avoid assuming that receipt order always equals observation order.

Where ordering matters, the system can use timestamps, monotonic sequence identifiers, buffering windows, and duplicate identifiers.

## Duplicate handling

Retransmission is useful for reliability, but it can create duplicate records.

The pipeline should use stable message or observation identifiers where possible so retries do not generate duplicate events.

## Normalization

Normalization creates a consistent internal representation.

Examples include converting units; standardizing sensor names; converting device-specific state codes into shared quality states; enforcing consistent numerical representation; and mapping observation types into a stable taxonomy.

Normalization should preserve original source data when practical so transformations can be reviewed.

## Quality-state propagation

Data quality is part of the observation.

Possible states include valid; degraded; stale; missing; invalid; initializing; and intentionally disabled.

A later analysis stage should not strip away this information.

## Context enrichment

Raw observations become more useful when combined with deployment metadata.

Centaurus can associate a record with site; monitored zone; device role; sensor orientation; deployment configuration; active operating mode; and local policy.

Context should come from versioned configuration so historical events can be interpreted using the configuration active at that time.

## Feature preparation

If a statistical or machine-learning model requires derived features, feature generation should be reproducible.

Examples may include rolling averages; rates of change; event duration; sensor agreement counts; recent event frequency; and deviation from baseline.

The feature definition and version should be tied to the model or ruleset using it.

## Buffering and offline operation

Connectivity interruptions should not automatically destroy observations.

Depending on the deployment, data may be buffered on the ORIGIN device, on a local gateway, in an ingestion queue, and in persistent backend storage.

When buffered data arrives later, the system must preserve its original observation time.

## Backpressure

A processing system can receive data faster than downstream services can handle it.

The architecture should define bounded behavior such as queue limits; prioritization; controlled dropping of low-value telemetry where acceptable; preserved high-priority events; and visible degraded-state reporting.

Unlimited buffering can create its own availability failure.

## Retention

Not all data needs to be stored indefinitely.

Retention can differ between raw high-rate telemetry; normalized observations; significant events; audit records; and model evaluation datasets.

Retention policy should balance engineering value, operational needs, storage cost, privacy, and legal requirements.

## Data minimization

Centaurus should avoid collecting additional personal information simply because it may be technically possible.

The system should store only the data required for monitoring, maintenance, validation, and legitimate operational analysis.

## Training and evaluation data

If Centaurus uses trained models, training data must be treated separately from live production data.

Important controls include documented source; consent/legal basis where relevant; labelling quality; separation between training and evaluation sets; representation of realistic deployment conditions; versioning; and protection against accidental inclusion of sensitive information.

## Dataset shift

A model validated in one environment may perform differently in another.

Potential causes include different site geometry; different sensor placement; environmental conditions; firmware changes; new hardware revisions; and changed visitor behaviour.

Centaurus should therefore monitor performance after deployment rather than treating validation as permanent.

## Event records

A structured event should preserve enough information for investigation.

A useful event record may contain:

```text
Event ID
Site / device / zone
Event category
Severity
Confidence
Start / end time
Contributing observations
Quality state
Centaurus version
Model / ruleset version
Configuration version
Operator disposition
```

## Privacy and access

Data access should follow least privilege.

Different roles may need different views, for example maintenance staff need device health, operators need current events, developers may need diagnostic traces, and administrators may manage configuration.

Access to raw data should not automatically be broader than access to summarized events.

## Data export

If data is exported for research, testing, or reporting, the export should identify date range; site/device scope; schema version; processing state; whether records are raw, normalized, or derived; and any anonymization or filtering applied.

## Reproducibility

A historical Centaurus result should be reproducible as far as practical from source observations; analysis version; model/ruleset version; configuration version; and feature-processing version.

This is particularly important when model behaviour changes over time.

## Implementation status

This page defines the intended processing contract. Exact database schemas, queue technologies, serialization formats, storage services, retention durations, feature implementations, and data-access APIs should be documented from the verified Centaurus codebase and deployment configuration.

## Related documentation

See [Architecture](architecture.md), [Detection & Analysis](detection-and-analysis.md), [Cybersecurity](cybersecurity.md), and [Software Data Pipeline](../software/data-pipeline.md).
