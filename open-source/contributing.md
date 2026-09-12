# Contributing

Contributions to ORIGIN should improve technical correctness, reproducibility, safety, maintainability, accessibility, or field usefulness.

The project welcomes contributions in documentation, electronics, firmware, AI, mechanical design, testing, deployment methodology, and maintenance practice. Contribution quality matters more than contribution volume.

## Before contributing

Before opening a change, determine which kind of contribution you are making documentation correction; technical clarification; bug fix; new feature; hardware revision; mechanical revision; test/validation improvement; deployment finding; maintenance improvement; security improvement; and proposal or research idea.

Different changes require different evidence.

## Core contribution rules

Every contribution should follow these principles.

### 1. Do not invent system behavior

If a value has not been measured, do not present it as measured.

If a feature is planned, do not present it as implemented.

If a component datasheet gives a maximum range, do not present that value as validated ORIGIN system performance.

### 2. Tie claims to revisions

A result from one Rosetta board, enclosure, firmware build, or site configuration may not apply to another.

State the relevant revision whenever the difference matters.

### 3. Preserve known limitations

Do not remove warnings, limitations, or known issues merely to make the project look more polished.

A limitation should be removed only when the underlying issue has been resolved and evidence supports the change.

### 4. Protect sensitive information

Never contribute passwords or secrets; deployment credentials; private keys; private archaeological-site security details; personal information; confidential commercial information; unpublished partner terms; and material the project is not permitted to redistribute.

### 5. Prefer reproducible evidence

Useful contributions include test procedures; measurements; photos tied to a test record; logs; schematic references; source files; validated manufacturing outputs; and clearly described failure cases.

## Documentation contributions

Documentation changes should be technically useful, not just stylistic.

Good documentation contributions may correct an inaccurate component description; clarify current versus planned behavior; add a missing installation step; add a troubleshooting path; explain a known manufacturing failure; improve cross-links between related pages; document a validation procedure; and improve terminology consistency.

When changing one technical fact, search for other places where the same fact may appear.

## Hardware contributions

Hardware changes should include enough context for review.

For an electronics change, provide where applicable problem statement; affected revision; schematic change; PCB change; reason for component selection; power/interface implications; ERC/DRC status; fabrication implications; validation plan; and compatibility impact.

Do not submit a generated Gerber-only change when the editable PCB source should also change.

## Mechanical contributions

Mechanical changes should consider more than visual appearance.

Review Rosetta fit; mmWave sensor position and field of view; screw access; cable routing; solar support; sealing paths; BIT/module access; mounting to soil/site infrastructure; serviceability; manufacturing constraints; and the 250 × 250 × 250 mm maximum single-part requirement where applicable.

Changes to sensor orientation require renewed coverage validation.

## Firmware contributions

Firmware changes should document affected interfaces; configuration changes; compatibility impact; failure behavior; test method; and recovery/rollback considerations where relevant.

Do not hard-code credentials or site-specific secrets.

## Centaurus AI contributions

AI-related contributions require special care because apparent improvements can create hidden false-positive or false-negative behavior.

Contributions should explain input data assumptions; output meaning; confidence handling; evaluation method; failure cases; changes to thresholds/rules/models; privacy implications; and whether human review remains required.

Do not describe a model as accurate, reliable, autonomous, or secure without evidence supporting those claims.

## Testing contributions

A good test contribution states:

1. objective;
2. setup;
3. equipment;
4. procedure;
5. acceptance criteria;
6. recorded outputs;
7. result;
8. anomalies;
9. revision tested.

A failed test is still useful evidence and should not be hidden.

## Deployment findings

Field observations are especially valuable.

A deployment finding should separate observation; suspected cause; confirmed cause, if known; operational impact; workaround; proposed design change; and validation needed before closing the finding.

Avoid presenting an interpretation as confirmed fact until it is verified.

## Contribution workflow

A typical workflow is:

```bash
git clone https://github.com/CristosMpi/origin-docs.git
cd origin-docs
git switch -c docs/my-change
```

Make the change, then review the diff:

```bash
git diff
```

Commit it:

```bash
git add <files>
git commit -m "Describe the engineering change"
```

Push the branch and open a pull request when external contribution workflows are enabled.

## Pull request checklist

Before requesting review, confirm The change solves a clearly stated problem; Current, planned, and conceptual behavior are distinguished; Technical values come from a source or measurement; Affected revisions are identified where needed; Related documentation is updated; Internal links still work; No secrets or private information are included; Known limitations are preserved or updated with evidence; Required tests have been performed or clearly marked as pending; Compatibility impact is stated; and The licensing status of contributed material is clear.

## Review criteria

Maintainers should review contributions for:

### Technical correctness

Does the change match the actual system?

### Evidence

Are claims supported by source, measurement, or clearly identified assumptions?

### Scope

Does the change solve one coherent problem without introducing unrelated edits?

### Safety

Could the change create electrical, mechanical, battery, environmental, or deployment risk?

### Security and privacy

Does the contribution expose sensitive information or weaken the defensive architecture?

### Reproducibility

Can another contributor understand and repeat the work?

### Maintainability

Does the change create unnecessary complexity or undocumented coupling?

## Compatibility changes

A contribution is compatibility-relevant if it changes, for example connector pinout; power requirements; PCB footprint; enclosure interface; sensor orientation; message/schema format; configuration format; firmware/hardware dependency; and module interface.

Compatibility changes should be reflected in the version documentation and, when appropriate, the changelog.

## Closing issues

Do not close an engineering issue merely because a fix was designed.

A stronger closure sequence is:

`issue identified → fix implemented → relevant test performed → evidence reviewed → docs updated → issue closed`

For field-critical problems, successful bench testing may not be sufficient; field re-validation may be required.

## Style

Documentation should be professional; concise where possible; technically precise; explicit about uncertainty; and understandable by a competent reader outside Team Galene.

Avoid marketing language such as “perfect,” “fully secure,” “100% accurate,” or “maintenance-free.”

## Attribution

Contributors should only submit material they are allowed to contribute. Third-party diagrams, CAD files, code, photos, logos, datasheets, and text may have separate rights or attribution requirements.

## Licensing note

The repository currently does not contain a formal project-wide `LICENSE` file. Until Team Galene adopts explicit licensing terms, contributors should not assume that repository publication alone grants unrestricted reuse rights.

The [Licensing](licensing.md) page describes the current status.

## Contribution principle

A contribution is valuable when it makes ORIGIN easier to **understand, reproduce, validate, deploy, maintain, or improve without reducing trust in the engineering record**.
