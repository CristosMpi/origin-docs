from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

R = {
    "deployments/deployment-architecture.md": {
        "The physical heritage environment protected objects or areas; walls and structures; visitor routes; staff access routes; environmental exposure; power availability; radio environment; and mounting restrictions.":
        "The physical heritage environment includes protected objects or areas; walls and structures; visitor routes; staff access routes; environmental exposure; power availability; radio environment; and mounting restrictions.",
        "Examples include might include:": "Example zones might include:",
    },
    "deployments/future-deployments.md": {
        "Typical characteristics controlled indoor environment; reliable fixed power may be available; dense visitor activity; reflective surfaces and display cases; strict visual-impact requirements; controlled staff access; and potentially reliable local networking.":
        "Typical characteristics include a controlled indoor environment; potentially reliable fixed power; dense visitor activity; reflective surfaces and display cases; strict visual-impact requirements; controlled staff access; and potentially reliable local networking.",
        "Typical characteristics direct weather exposure; solar power may be important; changing temperature and humidity; variable communications coverage; larger monitored zones; difficult maintenance access; and stronger environmental-protection requirements.":
        "Typical characteristics include direct weather exposure; the possible need for solar power; changing temperature and humidity; variable communications coverage; larger monitored zones; difficult maintenance access; and stronger environmental-protection requirements.",
        "future multi-unit deployments can use the same principles stable unit IDs;":
        "future multi-unit deployments can use the same principles: stable unit IDs;",
        "international deployment introduces additional considerations local regulations;":
        "international deployment introduces additional considerations: local regulations;",
    },
    "development/versions.md": {
        "when it changes any of the following PCB connector type or pin assignment;":
        "when it changes any of the following: PCB connector type or pin assignment;",
        "containing, where applicable ORIGIN project baseline;":
        "containing, where applicable: ORIGIN project baseline;",
    },
    "installation-deployment/README.md": {
        "At minimum the correct hardware revision is identified;":
        "At minimum, confirm that the correct hardware revision is identified;",
    },
    "maintenance/component-replacement.md": {
        "After installing the replacement verify mounting;":
        "After installing the replacement, verify mounting;",
    },
    "maintenance/diagnostics.md": {
        "save available evidence where possible event logs;":
        "save available evidence where possible: event logs;",
    },
    "maintenance/routine-maintenance.md": {
        "the following should be reviewed automatically or during normal operator monitoring device online/offline state;":
        "the following should be reviewed automatically or during normal operator monitoring: device online/offline state;",
        "if any of the following is found repeated device resets;":
        "if any of the following is found: repeated device resets;",
    },
    "mechanical-design/design-philosophy.md": {
        "through at least one of the following sensor placement;":
        "through at least one of the following: sensor placement;",
    },
    "open-source/README.md": {
        "Contributions should improve one or more of the following correctness;":
        "Contributions should improve one or more of the following: correctness;",
    },
    "open-source/repository.md": {
        "A deployment record should identify, where practical ORIGIN system revision;":
        "A deployment record should identify, where practical: ORIGIN system revision;",
    },
    "resources/contact.md": {
        "For questions about ORIGIN Core; Rosetta hardware; software architecture; Centaurus AI; sensors; mechanical design; testing and validation; installation or maintenance; and errors or ambiguities in ORIGIN Docs.":
        "Use the technical contact route for questions about ORIGIN Core, Rosetta hardware, software architecture, Centaurus AI, sensors, mechanical design, testing and validation, installation or maintenance, and errors or ambiguities in ORIGIN Docs.",
        "check these sections first [Overview](../overview/README.md)":
        "check these sections first: [Overview](../overview/README.md)",
    },
    "rosetta/manufacturing.md": {
        "The uploaded Rosetta v2 archive contains **10 files** `F_Cu.gbr`;":
        "The uploaded Rosetta v2 archive contains **10 files**: `F_Cu.gbr`;",
    },
    "rosetta/assembly-and-bring-up.md": {
        "Initial objectives are no rapid current-limit condition; no unexpected heating; charger/system node behaves plausibly; regulated rail reaches the intended voltage; and processor rail is stable.":
        "The initial objectives are to avoid a rapid current-limit condition or unexpected heating, confirm plausible charger/system-node behavior, verify that the regulated rail reaches its intended voltage, and confirm that the processor rail is stable.",
    },
    "origin-core/hardware-architecture.md": {
        "the important architectural requirements are accept an external energy source;":
        "the important architectural requirements are to accept an external energy source;",
    },
    "software/firmware.md": {
        "The following will be added when the firmware repository is available language/framework;":
        "The following will be added when the firmware repository is available: language/framework;",
    },
    "software/updates.md": {
        "record containing, where practical device ID;":
        "record containing, where practical: device ID;",
        "Before approving an update for field use release source/tag identified;":
        "Before approving an update for field use, confirm the following: release source/tag identified;",
    },
    "software/installation.md": {
        "A minimum checklist is firmware version recorded;":
        "A minimum checklist should confirm: firmware version recorded;",
    },
}

changed = 0
for rel, mapping in R.items():
    p = ROOT / rel
    text = p.read_text(encoding="utf-8")
    old_text = text
    for old, new in mapping.items():
        text = text.replace(old, new)
    if text != old_text:
        p.write_text(text, encoding="utf-8")
        changed += 1
        print(f"corrected {rel}")
print(f"STRUCTURAL_CORRECTIONS={changed}")
