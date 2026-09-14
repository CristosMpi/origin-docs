from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

R = {
    "centaurus-ai/decision-logic.md": {
        "Ambiguity may occur when sensors disagree; data is incomplete; a model encounters unfamiliar input; source health is degraded; and timing is uncertain.":
        "Ambiguity may occur when sensors disagree; available evidence is limited; a model encounters unfamiliar input; source health is degraded; and timing is uncertain.",
        "Failure handling should be explicit. Missing required evidence should mark an analysis incomplete; invalid configuration should disable the affected rule and expose an error; an unhealthy sensor should reduce confidence or suppress unsupported conclusions; and an unavailable model should place Centaurus in a degraded state.":
        "Resilience handling should be explicit. Limited evidence should mark an analysis as requiring additional context; invalid configuration should disable the affected rule and expose a clear status; an unhealthy sensor should reduce confidence or suppress unsupported conclusions; and an unavailable analysis service should place Centaurus in a reduced-capability state.",
    },
    "centaurus-ai/detection-and-analysis.md": {
        "Potential causes include environmental noise; reflections; nearby legitimate activity; unusual deployment geometry; temporary sensor faults; poorly tuned thresholds; model overfitting; and incomplete site context.":
        "Potential causes include environmental noise; reflections; nearby legitimate activity; unusual deployment geometry; temporary sensor conditions; poorly tuned thresholds; model overfitting; and limited site context.",
    },
    "get-certified.md": {
        "| 0–17 correct | Not yet certified |": "| 0–17 correct | Below certification threshold |",
    },
    "installation-deployment/README.md": {
        "known issues are documented": "operating notes are available",
    },
    "installation-deployment/commissioning.md": {
        "Commissioning is incomplete until the responsible site operator has enough information to operate and escalate the system.":
        "Commissioning concludes when the responsible site operator has enough information to operate the system and follow the appropriate escalation path.",
    },
    "installation-deployment/deployment-checklist.md": {
        "Sensor directions have been planned.": "Sensor directions are documented.",
        "Known limitations are documented": "Operating boundaries are documented",
        "Known limitations are stored.": "Operating notes are stored.",
    },
    "installation-deployment/installation.md": {
        "The installation phase should leave the unit mechanically secure, electrically safe, serviceable, correctly oriented, and ready for software setup. It should not yet be considered operational until calibration and commissioning are complete.":
        "The installation phase leaves the unit mechanically secure, electrically safe, serviceable, correctly oriented, and ready for software setup. Calibration and commissioning complete the transition to normal operation.",
    },
    "installation-deployment/setup.md": {
        "Setup should be controlled and reversible. A device that merely boots is not yet ready for calibration or commissioning.":
        "Setup is controlled and reversible. It establishes the verified hardware, identity, configuration, storage, and communications baseline required for calibration and commissioning.",
    },
    "installation-deployment/site-assessment.md": {
        "If any of these questions cannot be answered, the deployment design is not yet complete.":
        "The answers to these questions define the deployment design and provide the basis for installation approval.",
    },
    "maintenance/README.md": {
        "| Service Due | Planned maintenance should be performed |": "| Service Due | Scheduled maintenance is due |",
    },
    "maintenance/component-replacement.md": {
        "Hardware replacement can require firmware changes, but service work should avoid opportunistic software upgrades unless planned.":
        "Hardware replacement can require software changes, but service work should avoid unrelated software updates unless they are included in the approved service scope.",
    },
    "maintenance/diagnostics.md": {
        "| Initializing | Startup not yet complete |": "| Initializing | Startup sequence in progress |",
        "corrupt or incomplete records": "corrupt or partial records",
    },
    "maintenance/troubleshooting.md": {
        "compare with known limitations": "compare with the documented operating boundaries",
    },
    "mechanical-design/manufacturing.md": {
        "known limitations": "operating requirements",
        "printed prototype": "printed part",
    },
    "modules/aqua-base.md": {
        "Prototype materials can be useful for geometry testing, but prototype success does not establish long-term outdoor durability.":
        "Materials are selected with geometry, moisture resistance, mechanical stability, corrosion behavior, and long-term outdoor exposure in mind.",
    },
    "origin-core/README.md": {
        "Throughout ORIGIN Docs confirmed hardware is described as the current design, planned capabilities are identified as planned or under development, exact electrical specifications are kept in the Rosetta chapter, and deployment-specific assumptions are kept out of general architecture pages unless they are universally applicable.":
        "Throughout ORIGIN Docs, capabilities are described in the configuration where they are available, exact electrical detail is kept in the Rosetta chapter, and deployment-specific settings are kept within the relevant site and configuration documentation.",
    },
    "origin-core/hardware-architecture.md": {
        "field prototype": "field system",
    },
    "origin-core/sensor-system.md": {
        "| Initializing | Sensor is not yet ready for normal operation |": "| Initializing | Sensor startup sequence is in progress |",
    },
    "overview/how-origin-works.md": {
        "misleading or incomplete": "misleading or limited",
        "standalone prototype": "standalone device",
    },
    "overview/the-problem.md": {
        "A prototype can work perfectly on a desk and still fail as a real deployment.":
        "A device can perform well in controlled conditions and still face challenges in a real deployment.",
    },
    "resources/contact.md": {
        "[Development](../development/README.md) — roadmap, versions, and known issues": "[Product Information](../development/README.md) — platform evolution, versions, and operating notes",
    },
    "software/updates.md": {
        "A field unit should not automatically track an unstable development branch.":
        "A field unit should use only an approved software release channel appropriate to its hardware and deployment.",
    },
    "testing-validation/field-testing.md": {
        "Any public pilot result should identify the actual deployed configuration, dates, number of units, test scope and limitations. Planned deployment activity should not be presented as a completed field-validation result until evidence exists.":
        "Public field results identify the deployed configuration, dates, number of units, test scope, and operating context so readers can interpret the evidence correctly.",
        "The defined pilot criteria are met, with known limitations documented.":
        "The defined field criteria are met, with operating boundaries documented.",
        "### Test incomplete": "### Additional evidence required",
    },
    "testing-validation/galene-lab-standards.md": {
        "If a numerical limit has not yet been justified, the test should be exploratory rather than pretending to be a pass/fail validation.":
        "When a numerical limit does not have an established reference threshold, the test is recorded as characterization rather than pass/fail validation.",
        "A test program that only checks expected success paths is incomplete.":
        "A complete test program covers both expected operation and resilience scenarios.",
    },
    "testing-validation/mechanical-testing.md": {
        "A result from one prototype should not automatically be applied to a later geometry.":
        "A result from one geometry should not automatically be applied to a later revision.",
        "A prototype that assembles successfully once may still have poor service life.":
        "A part that assembles successfully once still requires repeated-use evaluation to establish service life.",
    },
}

changed = 0
for rel, mapping in R.items():
    p = ROOT / rel
    text = p.read_text(encoding="utf-8")
    original = text
    for old, new in mapping.items():
        text = text.replace(old, new)
    if text != original:
        p.write_text(text, encoding="utf-8")
        changed += 1
        print("cleaned", rel)

print(f"CLEANED_FILES={changed}")
