# Limitations

Centaurus AI is a decision-support and analysis layer, not a source of certainty. Its outputs depend on the quality of the data, the assumptions built into the analysis, the deployment environment, and the extent to which the system has been validated under realistic conditions.

Documenting limitations is therefore part of the engineering design, not an afterthought.

## AI does not create ground truth

Centaurus can analyze observations, but it cannot know more than the evidence available to it.

If sensors are obstructed, unhealthy, misconfigured, or placed poorly, the analysis layer cannot reliably compensate for those weaknesses.

A useful principle is:

**better analysis cannot replace missing evidence.**

## Dependence on sensor quality

Centaurus inherits uncertainty from ORIGIN Core.

Potential sensor-related limitations include blind zones; reflections; environmental noise; sensor drift; temporary communication failures; incomplete calibration; degraded power conditions; and mounting changes.

Centaurus should propagate these quality states into its outputs rather than hiding them.

## False positives

Centaurus may classify normal activity as unusual.

False positives can result from legitimate visitor or staff activity; temporary environmental changes; unusual but harmless site conditions; poorly tuned thresholds; model overfitting; incomplete context; and deployment conditions that differ from training/testing.

Excessive false positives can reduce operator trust and create alert fatigue.

## False negatives

Centaurus can also fail to identify a meaningful event.

Possible causes include insufficient sensor coverage; weak or ambiguous signals; missing observations; unfamiliar event patterns; overly conservative thresholds; model failure; and data-processing faults.

The system should never be marketed as guaranteeing detection of every intrusion, environmental problem, or system fault.

## Model confidence is not probability of truth

Many models can produce a confidence score, probability-like value, or anomaly score.

Such values only have meaning within the model's validation context. A score of 0.9 does not automatically mean that an event has a 90% real-world probability of being correct.

Calibration must be measured before confidence values are interpreted operationally.

## Distribution shift

AI and statistical systems can behave differently when the real deployment differs from development data.

Changes may include a different museum or archaeological site; altered enclosure geometry; new sensor revision; new firmware; changed visitor patterns; seasonal conditions; and different mounting height or orientation.

A validated model should therefore be re-evaluated after material changes to the system or deployment.

## Limited generalization

A model trained or tuned for one type of site should not automatically be assumed to work equally well everywhere.

Heritage environments can differ significantly in geometry; materials; public access; climate; typical activity; available power/connectivity; and security requirements.

Site-specific calibration or configuration may be necessary.

## Incomplete context

Centaurus may not know information that a human operator knows.

For example scheduled maintenance; an authorized visitor after hours; construction activity; a temporary exhibition change; and a sensor intentionally disconnected for service.

Operator context can therefore be essential to correct interpretation.

## Ambiguity

Some events cannot be classified confidently.

Centaurus should support an explicit ambiguous/unknown state instead of forcing every event into a definitive category.

Ambiguity is especially likely when sensors disagree, required data is missing, multiple explanations fit the observations, and the input is outside the validated operating range.

## Dependence on configuration

Bad configuration can produce bad analysis even when the software is functioning correctly.

Examples include incorrect sensor-zone mapping; inappropriate environmental thresholds; wrong operating schedule; stale site metadata; and mismatched model/ruleset version.

Configuration validation and version control are therefore essential.

## Connectivity limitations

If Centaurus depends partly on remote processing, connectivity loss can reduce capability.

A robust deployment should define which functions continue locally and which functions enter degraded mode.

Delayed data can still be useful historically, but it may no longer support real-time response.

## Compute limitations

AI processing can require more compute, memory, or storage than embedded sensing.

Depending on the final architecture, this may limit model size; processing frequency; local inference capability; retained history; and response latency.

Performance requirements must be validated on the actual target hardware or service environment.

## Explainability limitations

Not every trained model is naturally interpretable.

Even when Centaurus preserves contributing observations, the internal reason a complex model produced a particular score may not always be fully explainable.

For important decisions, simpler and more transparent methods may be preferable when they provide comparable performance.

## Cybersecurity limitations

No cybersecurity architecture eliminates all risk.

Residual risks can remain from software vulnerabilities; compromised credentials; supply-chain dependencies; insecure operator devices; physical access; configuration mistakes; and unknown vulnerabilities.

Security controls must be maintained over time rather than treated as a one-time feature.

## Privacy limitations

Even non-camera sensors can produce information about human activity.

Presence, timing, and movement-pattern data may still be sensitive depending on deployment context. Data minimization, access controls, and appropriate retention policies remain necessary.

## Conservation limitations

ORIGIN and Centaurus are monitoring tools. They do not replace professional conservation assessment.

An unusual environmental measurement may indicate that further investigation is needed, but Centaurus should not independently diagnose damage to an artefact, monument, or archaeological structure unless a future capability is specifically validated for that purpose.

## Security-response limitations

Likewise, presence detection does not prove unauthorized access or malicious intent.

A radar observation can indicate that someone is present or moving; it cannot, by itself, establish who that person is or why they are there.

Operator review remains necessary.

## Validation boundaries

Every claimed capability should state the conditions under which it was tested.

Useful validation metadata includes site/test environment; hardware revision; firmware version; Centaurus version; model/ruleset version; sensor configuration; sample size; and measured false-positive/false-negative rates where applicable.

Without this context, performance claims are easy to misinterpret.

## Development status

Centaurus is an evolving subsystem of Project ORIGIN. Architecture pages describe intended engineering behavior, but not every documented capability should be assumed to be fully implemented or field-validated.

The documentation should progressively replace design intent with measured implementation facts as the project matures.

## Appropriate use

Centaurus is best understood as a system that can organize sensor evidence; identify unusual patterns; prioritize events; support maintenance and monitoring; and provide context for human decisions.

It should not be treated as an autonomous authority for security, conservation, legal, or emergency decisions.

## Related documentation

See [Detection & Analysis](detection-and-analysis.md), [Decision Logic](decision-logic.md), [Cybersecurity](cybersecurity.md), and [Testing & Validation](../testing-validation/README.md).
