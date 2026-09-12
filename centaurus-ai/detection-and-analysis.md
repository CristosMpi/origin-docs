# Detection & Analysis

Centaurus AI is responsible for interpreting structured observations produced by ORIGIN's sensing and software layers. Its goal is not to react to every individual reading, but to identify patterns that may deserve operator attention.

## From observation to interpretation

A sensor reading is not automatically an event.

A robust analysis pipeline distinguishes:

```text
Raw measurement
      ↓
Validated observation
      ↓
Contextualized observation
      ↓
Pattern / anomaly analysis
      ↓
Candidate event
      ↓
Decision logic
```

This separation helps prevent noise or isolated readings from being treated as meaningful conclusions.

## Analysis categories

Centaurus can conceptually support several forms of analysis.

### Presence and activity analysis

Human-presence information from ORIGIN's radar subsystem can be evaluated over time rather than as isolated detections.

Useful features may include which sensor reported activity; duration of presence; changes in measured distance; direction or movement trends where available; overlap between multiple sensors; and recurrence within a defined time window.

The objective is to build a richer event context without claiming to identify a person.

### Environmental analysis

Environmental data can be examined for threshold violations; rapid changes; long-term drift; unusual combinations of measurements; persistent abnormal states; and differences from a site-specific baseline.

A single high or low measurement may be less informative than a sustained trend.

### Device-health analysis

Centaurus can also analyze the monitoring system itself.

Examples include repeated sensor failures; communication interruptions; battery degradation trends; stale data; devices that reset unusually often; and inconsistent observations from redundant sensors.

This supports predictive maintenance and helps distinguish a genuine site event from a monitoring-system fault.

## Temporal analysis

Time is central to meaningful interpretation.

Centaurus may compare observations using windows such as immediate events, short rolling windows, daily patterns, and longer historical baselines.

The exact durations should be chosen from testing rather than arbitrary values.

For example:

```text
One temperature spike
        ↓
Possibly noise

Sustained abnormal temperature
        ↓
Potential environmental event
```

## Sensor fusion

No single sensor provides complete context.

Sensor fusion can combine independent observations to strengthen or weaken an interpretation.

Conceptually:

```text
Radar observation ──┐
Environmental data ─┼──> Context fusion ──> Candidate event
Device health ──────┘
```

Fusion should not mean simply averaging unrelated signals. Each sensor contributes according to its semantics and quality state.

## Agreement and disagreement

Multiple sensors can disagree.

Centaurus should preserve that disagreement rather than forcing an artificial consensus.

For example one radar reports presence while others do not, one environmental sensor shows a sudden jump while neighbouring sensors remain stable, and a sensor reports a strong signal while its health state is degraded.

Such cases can be classified as ambiguous or low-confidence rather than silently discarded.

## Baselines

Some forms of anomaly detection depend on a baseline of expected behaviour.

A baseline can be based on historical data; operator-defined expected ranges; time-of-day patterns; site configuration; and seasonal behaviour where relevant.

Baselines must be updated carefully. If an abnormal condition persists, the system should not automatically learn that condition as normal without review.

## Anomaly detection

Anomaly detection can help identify conditions not captured by fixed thresholds.

Possible examples include an unusual environmental combination, an unexpected pattern of presence observations, a device behaving differently from comparable units, and a gradual shift that stays inside absolute limits but differs from historical behaviour.

An anomaly is not automatically a threat or failure. It is a statistical or logical indication that something differs from the expected pattern.

## Classification

Where a classification model or rule system is used, outputs should remain limited to categories that have clear operational meaning.

For example, an event taxonomy may distinguish between normal observation; maintenance condition; environmental concern; presence/activity event; communications degradation; ambiguous event; and unknown/unclassified event.

The final taxonomy should be versioned and tied to actual operator workflows.

## Confidence

Confidence should be calculated or assigned using evidence quality, not simply model output.

Relevant factors can include source health; sensor agreement; observation freshness; amount of supporting evidence; model certainty; known site context; and missing data.

A useful principle is:

**high model confidence + poor sensor quality ≠ high system confidence.**

## False positives

False positives are unavoidable in real monitoring systems.

Potential causes include environmental noise; reflections; nearby legitimate activity; unusual deployment geometry; temporary sensor faults; poorly tuned thresholds; model overfitting; and incomplete site context.

Testing should therefore measure more than raw detection rate. It should also measure event precision, false-alarm frequency, and operator burden.

## False negatives

A system can also miss real events.

Potential causes include blind zones; sensor obstruction; connectivity loss; insufficient sampling; model failure; inappropriate thresholds; and novel behaviour not represented during development.

Centaurus should not be described as guaranteeing detection of every relevant event.

## Explainability

Every important Centaurus result should include enough context for later review.

An operator should be able to ask what triggered this event?; which sensors contributed?; what was their health state?; what analysis version was used?; what evidence disagreed?; and why was this severity assigned?.

Explainability does not require exposing internal model mathematics to every operator, but it does require preserving the evidence chain.

## Data minimization

Analysis should use only the information needed for the intended heritage-monitoring function.

For human-presence monitoring, Centaurus does not need to infer personal identity simply to determine that activity occurred in a monitored zone.

This reduces privacy risk and narrows the technical scope.

## Validation

Detection and analysis must be tested against labelled or otherwise verifiable scenarios.

Useful validation dimensions include normal site operation; known presence events; environmental excursions; sensor failure; communication loss; ambiguous multi-sensor cases; long periods of normal operation; and unusual but legitimate activity.

Results should be documented under [Testing & Validation](../testing-validation/README.md).

## Implementation status

This page describes the analysis model and engineering requirements. Exact algorithms, trained-model architectures, feature sets, thresholds, datasets, and measured performance should be added from verified Centaurus implementation and validation records.

## Related documentation

See [Decision Logic](decision-logic.md); [Data Processing](data-processing.md); [Limitations](limitations.md); [Presence Detection](../origin-core/presence-detection.md); and [Environmental Monitoring](../origin-core/environmental-monitoring.md).
