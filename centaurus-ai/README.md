# Centaurus AI

**Centaurus AI** is the higher-level analysis and decision-support layer of Project ORIGIN. Its role is to turn validated sensor observations and system-health information into structured context that can help operators understand what is happening at a monitored heritage site.

Centaurus is intentionally positioned **above** the sensing and firmware layers. Rosetta and ORIGIN Core are responsible for collecting data, identifying sensor health, and producing structured observations. Centaurus consumes those observations and evaluates relationships between them.

It is not intended to replace museum staff, archaeologists, security personnel, conservators, or other responsible operators. Its purpose is to help them interpret information faster and with more context.

## What Centaurus does

At a high level, Centaurus can support five classes of work:

1. **Observation analysis** — interpret structured sensor and system observations.
2. **Context fusion** — combine related observations from different sensors or time periods.
3. **Event assessment** — determine whether a set of observations is routine, unusual, or potentially important.
4. **Decision support** — attach severity, confidence, rationale, and recommended operator attention to an event.
5. **System protection** — support cybersecurity and integrity checks around the data and software path.

The exact algorithms, model families, thresholds, and production deployment architecture remain version-dependent and should be documented from the real implementation as Centaurus matures.

## Position in ORIGIN

A simplified system relationship is:

```text
Physical environment
        ↓
Sensors
        ↓
Rosetta / ORIGIN firmware
        ↓
Validated observations
        ↓
Software data pipeline
        ↓
Centaurus AI
        ↓
Context / classification / confidence
        ↓
Operator-facing event
```

This separation is deliberate. AI should not be the first component that decides whether a sensor is healthy, whether a packet is valid, or whether a measurement is physically plausible. Those checks belong earlier in the system.

## Inputs

Depending on the deployed configuration, Centaurus may consume structured information such as:

- human-presence observations;
- motion, distance, or direction-related observations;
- environmental measurements;
- device-health information;
- power and battery status;
- communication status;
- timestamp and source identity;
- configuration/version metadata;
- recent event history;
- site-specific operating context.

The architecture should preserve the identity and provenance of every input. Centaurus should know not only **what value arrived**, but also where it came from, when it was generated, what device produced it, and whether that source was healthy.

## Outputs

A Centaurus output should be more informative than a binary alarm.

A useful output model includes:

```text
Event
├── category
├── severity
├── confidence
├── contributing observations
├── affected device / zone
├── timestamp
├── rationale / evidence summary
├── data-quality state
└── recommended operator attention
```

This structure supports traceability and makes later review easier.

## Confidence is not certainty

Any confidence value produced by Centaurus should be interpreted as a model or rule-system assessment, not as proof.

For example, a high-confidence event can still be wrong because of:

- unusual site geometry;
- faulty or misconfigured sensors;
- a distribution shift between testing and deployment;
- incomplete context;
- unexpected environmental conditions;
- software or data-quality problems.

For this reason, Centaurus should retain the underlying observations that contributed to an event.

## Human-in-the-loop operation

ORIGIN is designed around human responsibility.

Centaurus may prioritize, classify, summarize, or recommend attention, but final operational decisions remain with authorized people. This is especially important when events could lead to security responses, maintenance actions, or conclusions about conditions affecting cultural heritage.

The intended flow is:

```text
Centaurus assessment
        ↓
Operator review
        ↓
Human decision
        ↓
Response / investigation / maintenance
```

## Design principles

### Evidence before conclusion

Centaurus should preserve the observations behind an event rather than returning only a label.

### Data quality awareness

A model should not treat missing, stale, or unhealthy sensor data as equivalent to healthy observations.

### Conservative automation

The system should avoid irreversible actions based solely on uncertain inference.

### Site-specific context

A museum interior, archaeological site, storage area, and outdoor monument can have very different normal behavior. The analysis layer should be configurable for deployment context.

### Versioned behavior

Changes to models, thresholds, or rules can change event behavior. The software must therefore identify the analysis version responsible for a result.

### Privacy by design

Centaurus should process only the information required for the monitoring objective and avoid unnecessary collection or retention.

## AI and deterministic logic

Not every part of Centaurus needs to be machine learning.

A robust architecture may combine:

- deterministic validation;
- rule-based event logic;
- thresholds and hysteresis;
- temporal correlation;
- statistical methods;
- anomaly detection;
- trained models where they provide a measurable advantage.

Using AI only where it improves the system keeps behavior easier to test and explain.

## Relationship with cybersecurity

Centaurus also has a cybersecurity dimension. Analysis results are only useful if the data pipeline can be trusted.

Security considerations therefore include:

- device identity;
- data integrity;
- authentication;
- authorization;
- secure configuration;
- protected update paths;
- auditability;
- resistance to malformed or manipulated input.

See [Cybersecurity](cybersecurity.md).

## Validation status

Centaurus should not be described as a production-grade autonomous security or conservation system until its models, decision logic, failure states, and operating limits have been validated in representative field conditions.

Public ORIGIN documentation should distinguish between:

- architecture goals;
- implemented capabilities;
- laboratory-tested behavior;
- field-validated behavior;
- planned features.

This distinction is especially important for AI because model capability can be easy to overstate when only demonstration data has been tested.

## Chapter contents

Continue with:

- [Architecture](architecture.md)
- [Detection & Analysis](detection-and-analysis.md)
- [Decision Logic](decision-logic.md)
- [Cybersecurity](cybersecurity.md)
- [Data Processing](data-processing.md)
- [Limitations](limitations.md)

For the lower-level data path that feeds Centaurus, see [Software](../software/README.md) and [ORIGIN Core](../origin-core/README.md).
