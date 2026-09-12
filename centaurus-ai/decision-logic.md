# Decision Logic

Decision logic is the layer that converts Centaurus analysis results into operator-relevant events. Its purpose is to reduce noise, preserve uncertainty, and ensure that an alert reflects more than a single unexamined sensor value.

## Why a separate decision layer matters

Analysis can produce many intermediate signals anomaly scores; threshold crossings; model predictions; sensor disagreement; confidence estimates; and temporal trends.

These are not all directly actionable.

The decision layer evaluates them against context and policy before producing an event.

```text
Analysis result
      ↓
Context + quality state
      ↓
Rules / decision logic
      ↓
Severity + confidence
      ↓
Operator-facing event
```

## Event states

A useful event lifecycle can include:

```text
Candidate
   ↓
Confirmed
   ↓
Active
   ↓
Acknowledged
   ↓
Resolved / dismissed
```

Not every candidate needs to become a notification.

## Severity

Severity should describe potential operational importance, not model confidence.

For example, a future deployment might use levels such as informational, attention required, elevated concern, and critical.

The exact labels and thresholds should match real operator workflows and be validated with the institutions using ORIGIN.

## Confidence and severity are different

A low-confidence event can still involve a potentially serious condition, while a high-confidence event may be routine.

For example:

```text
High confidence + low severity
= clearly detected routine activity

Low confidence + high potential severity
= ambiguous evidence that may still require review
```

The system should retain both dimensions separately.

## Evidence aggregation

Decision logic may combine multiple pieces of evidence.

A conceptual evidence record can contain:

```text
Event evidence
├── radar observation
├── environmental condition
├── system-health state
├── temporal context
└── site configuration
```

The resulting event should preserve which observations contributed and which observations conflicted.

## Hysteresis

Threshold-based systems can repeatedly switch state when measurements hover near a boundary.

Hysteresis can reduce this behavior by using different conditions for entering and leaving an event state.

For example:

```text
Normal → Alert: higher threshold
Alert → Normal: lower recovery threshold
```

Exact values must be determined by testing.

## Persistence

Some conditions should persist for a minimum duration before becoming an event.

This can help distinguish brief noise from sustained environmental change, transient communication loss from a persistent outage, and momentary activity from continued presence.

Persistence windows should be documented and versioned.

## Cooldowns and duplicate suppression

If the same condition remains active, the system should avoid creating a new event every processing cycle.

Instead, it can update the existing event, extend its duration, add new evidence, and escalate severity if conditions worsen.

This reduces notification fatigue.

## Escalation

An event can become more important as evidence accumulates.

Possible escalation factors include longer duration; additional agreeing sensors; worsening environmental values; repeated activity; simultaneous system-health problems; and operator-defined protected periods.

Escalation logic should be deterministic enough to audit.

## De-escalation and recovery

Events should not remain critical forever after the underlying condition disappears.

Recovery logic can consider return to a stable normal range; healthy readings for a defined period; restored communication; operator acknowledgement; and maintenance confirmation.

The reason an event closed should be logged.

## Unknown and ambiguous states

Centaurus must support an explicit **unknown** or **ambiguous** outcome.

Forcing every input into either "safe" or "dangerous" creates false certainty.

Ambiguity may occur when sensors disagree; data is incomplete; a model encounters unfamiliar input; source health is degraded; and timing is uncertain.

In such cases, the appropriate action may simply be to request operator review.

## Rules and learned models

Decision logic should remain understandable even when trained models contribute analysis.

A recommended separation is:

```text
Model / statistical output
        ↓
Confidence + evidence
        ↓
Explicit decision policy
        ↓
Event
```

This allows safety-critical constraints to remain outside a learned model.

## Site-specific policy

Different sites may have different operating rules.

Examples include public opening hours; restricted zones; maintenance periods; expected staff activity; and acceptable environmental ranges.

Site-specific policy should be configuration, not hard-coded assumptions.

## Human override

Authorized operators should be able to acknowledge, dismiss, annotate, or otherwise review events.

Human actions should be recorded for audit and can later support evaluation of false positives or poor rules.

## Safe defaults

When Centaurus cannot evaluate an event reliably, it should default to visible uncertainty rather than silently claiming normal operation.

Examples include missing required evidence → mark analysis incomplete, invalid configuration → disable affected rule and expose error, unhealthy sensor → reduce confidence or suppress unsupported conclusion, and model unavailable → enter degraded mode.

## Auditability

Each decision should retain decision timestamp; ruleset/model version; configuration version; evidence identifiers; severity; confidence; reason or rule path; and event lifecycle history.

This makes post-event analysis possible.

## Testing decision logic

Decision rules should be tested with repeatable scenarios including boundary values; repeated identical events; conflicting sensors; missing data; prolonged abnormalities; recovery from abnormal states; model unavailability; and configuration errors.

Tests should verify both event creation and event suppression.

## Implementation status

The exact severity scale, ruleset syntax, correlation windows, persistence values, notification policies, and operator interfaces must be derived from the final Centaurus implementation and pilot requirements. This page defines the behavior the decision layer should provide without claiming unverified production settings.

## Related documentation

See [Detection & Analysis](detection-and-analysis.md), [Architecture](architecture.md), [Limitations](limitations.md), and [Testing & Validation](../testing-validation/README.md).
