# Lessons Learned

The purpose of deployment lessons is to convert field experience into better engineering decisions.

A lesson is broader than a single finding. It explains what an observation means for the design, installation process, validation method, operator workflow, or future deployment architecture.

## Current status

No Durrës-specific operational lessons are presented as established facts until the pilot has been installed, commissioned, and observed.

This page therefore documents the **lesson framework** and the engineering principles that future deployment evidence should either confirm, refine, or challenge.

## From finding to lesson

A useful lesson has four parts:

1. **Assumption** — what the team expected before deployment.
2. **Observation** — what happened in the real environment.
3. **Interpretation** — why the difference matters.
4. **Change** — what should be modified in design, testing, or procedure.

Example structure:

```text
Assumption:
One radar orientation would provide sufficient coverage of a zone.

Observation:
Installed geometry created a repeatable blind area.

Interpretation:
Coverage cannot be accepted from CAD orientation alone.

Change:
Require post-installation coverage mapping before commissioning.
```

This is an example of the method, not a published Durrës result.

## Lesson categories

### Site assessment

Future deployments should test whether the pre-deployment site assessment captured enough information about geometry; conservation restrictions; surface suitability; visitor flow; communications conditions; sun/shade exposure; and maintenance access.

If installation repeatedly encounters surprises, the assessment procedure should be improved.

### Mechanical integration

The field environment will show whether the enclosure and mounting system are practical outside the lab.

Key questions include Is the unit easy to install without invasive work?; Is it stable over time?; Can staff service it without removing unrelated parts?; Are sensor openings easy to inspect and clean?; Does the solar support remain rigid?; and Are BIT interfaces still reachable after installation?.

### Sensor placement

One of the most important expected lessons is that sensor performance depends on installation geometry.

Future deployment evidence should be used to refine radar orientation; overlap rules; minimum clearance from nearby structures; mounting-height recommendations; calibration procedure; and coverage test methods.

### Environmental protection

Water resistance and environmental durability should be judged on the installed enclosure, not only on individual parts.

The deployment process should reveal whether water drains away correctly; seams remain protected; sensor openings introduce unacceptable exposure; condensation occurs; materials age as expected; and maintenance restores sealing correctly.

### Power

Solar and battery assumptions should be compared with real use.

Important lessons may include how much shading matters; which operating modes dominate energy consumption; whether recovery after low energy is reliable; whether maintenance staff can diagnose low-power states; and whether panel orientation is practical at heritage sites.

### Communications

Real deployments should determine whether the intended communications model is robust enough.

Lessons may affect retry behavior; local buffering; operator offline warnings; data synchronization; time handling; and network setup procedure.

### Human factors

A technically correct system can still fail operationally if users do not understand it.

The pilot should therefore produce lessons about status terminology; alarm presentation; maintenance instructions; onboarding; documentation clarity; false-alarm fatigue; and escalation workflow.

### Centaurus AI

Field use should validate whether Centaurus adds useful context without creating false confidence.

Lessons should examine how operators interpret confidence; whether explanations are useful; whether the AI reacts sensibly to missing sensors; whether site-specific baselines are necessary; and whether prioritization reduces or increases workload.

## Design feedback loop

Deployment lessons should feed back into the product-development process.

```text
Deployment
    ↓
Finding
    ↓
Root-cause analysis
    ↓
Lesson learned
    ↓
Design / firmware / process change
    ↓
Lab validation
    ↓
Next deployment
```

The final step is important: a change made because of a field problem must still be validated before it becomes the next baseline.

## Repeated lessons

If the same issue appears at multiple sites, it should be treated as a systemic design issue rather than a local anomaly.

Repeated lessons may justify new hardware revision; enclosure redesign; firmware default change; new commissioning test; updated module specification; new maintenance procedure; and new site-assessment requirement.

## Documentation discipline

Lessons should be versioned and linked to evidence.

A lesson should identify deployment source; affected revision; related finding IDs; affected subsystem; engineering owner; change implemented; and validation status after the change.

This creates traceability from real-world observation to product improvement.

## Avoiding overgeneralization

A result from one location should not automatically be applied to every heritage site.

For example, a communications problem caused by one building's structure may not imply that the communications design is globally inadequate.

The lesson should be scoped correctly site-specific; environment-specific; hardware-specific; configuration-specific; and general/systemic.

## Current project-wide lessons already reflected in the documentation

Even before formal Durrës field results are published, several development principles have already been incorporated into the ORIGIN documentation process manufacturer component specifications are kept separate from ORIGIN-validated system performance; missing or failed sensors must not be represented as a normal "no event" state; the current Rosetta v2 manufacturing export is not treated as fabrication-complete when the drill data is missing; mmWave sensor geometry must be validated with the real enclosure and installation position; deployment configuration and software versions must be traceable; and pilot activity should not be described as production operation before commissioning evidence exists.

These principles come from the engineering workflow and known development issues; they are not presented as Durrës pilot outcomes.

## Future updates

Once the Durrës pilot produces field evidence, this page should be expanded with real lessons and the specific changes they cause in ORIGIN 2026 or later revisions.

## Related documentation

[Findings](findings.md), [Durrës Pilot](durres-pilot.md), [Development](../development/README.md), and [Testing & Validation](../testing-validation/README.md).
