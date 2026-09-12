from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

REPLACEMENTS = {
    "overview/README.md": {
        "This documentation is intended to become the technical source of truth for ORIGIN. They cover not only what the system is, but how it is designed, tested, deployed, maintained, and improved.":
        "This documentation is intended to become the technical source of truth for ORIGIN. It covers not only what the system is, but also how it is designed, tested, deployed, maintained, and improved.",
        "## How to read these docs": "## How to use this documentation",
    },
    "centaurus-ai/architecture.md": {
        "Examples include invalid input should be rejected rather than guessed; unavailable models should trigger degraded mode; broken external connectivity should not delete local evidence; unsupported schema versions should produce explicit compatibility errors; and analysis failures should not be converted into normal events.":
        "Failure isolation should remain explicit. Invalid input should be rejected rather than guessed, unavailable models should trigger a degraded state, broken external connectivity should not delete local evidence, unsupported schema versions should produce clear compatibility errors, and analysis failures should never be represented as normal events.",
    },
    "centaurus-ai/decision-logic.md": {
        "Analysis can produce many intermediate signals anomaly scores; threshold crossings; model predictions; sensor disagreement; confidence estimates; and temporal trends.":
        "Analysis can produce many intermediate signals, including anomaly scores, threshold crossings, model predictions, sensor disagreement, confidence estimates, and temporal trends.",
        "Examples include missing required evidence → mark analysis incomplete, invalid configuration → disable affected rule and expose error, unhealthy sensor → reduce confidence or suppress unsupported conclusion, and model unavailable → enter degraded mode.":
        "Failure handling should be explicit. Missing required evidence should mark an analysis incomplete; invalid configuration should disable the affected rule and expose an error; an unhealthy sensor should reduce confidence or suppress unsupported conclusions; and an unavailable model should place Centaurus in a degraded state.",
    },
    "centaurus-ai/data-processing.md": {
        "Source identity allows operators and developers to answer which ORIGIN unit generated this data?, which physical sensor produced it?, was that source healthy at the time?, and what firmware version produced the record?.":
        "Source identity allows operators and developers to determine which ORIGIN unit and physical sensor produced a record, whether that source was healthy at the time, and which firmware version generated it.",
    },
    "centaurus-ai/detection-and-analysis.md": {
        "An operator should be able to ask what triggered this event?; which sensors contributed?; what was their health state?; what analysis version was used?; what evidence disagreed?; and why was this severity assigned?.":
        "An operator should be able to ask: What triggered this event? Which sensors contributed? What was their health state? What analysis version was used? What evidence disagreed? Why was this severity assigned?",
    },
    "development/README.md": {
        "Examples include a CAD enclosure render is not evidence of environmental resistance; a sensor datasheet is not evidence of ORIGIN system-level detection range; a successful boot is not evidence of long-term firmware reliability; an AI output that appears reasonable is not evidence of accuracy; and an assembled PCB is not proof that the complete manufacturing package is release-ready.":
        "An attractive CAD render is not evidence of environmental resistance. A sensor datasheet does not establish ORIGIN-level detection range, a successful boot does not establish long-term firmware reliability, a plausible AI output does not establish accuracy, and an assembled PCB does not prove that its manufacturing package is release-ready.",
    },
    "development/roadmap.md": {
        "The following areas are valid research directions but are not presented as committed current functionality alternative edge-compute platforms, including Raspberry Pi-class systems; automatic deployment configuration and tooling; improved remote diagnostics; expanded sensor families; additional module classes; fleet-level comparison across multiple heritage sites; stronger automated validation pipelines; and richer visualization and decision-support tools.":
        "The following areas are valid research directions, but they are not presented as committed current functionality: alternative edge-compute platforms, including Raspberry Pi-class systems; automatic deployment configuration and tooling; improved remote diagnostics; expanded sensor families; additional module classes; fleet-level comparison across multiple heritage sites; stronger automated validation pipelines; and richer visualization and decision-support tools.",
    },
    "installation-deployment/commissioning.md": {
        "Examples include disconnect one sensor; disable communications; temporarily remove network access; introduce an intentionally invalid configuration in a controlled test environment; and simulate a module becoming unavailable.":
        "Controlled fault tests can include disconnecting one sensor, disabling communications, temporarily removing network access, introducing an intentionally invalid configuration in a safe test environment, and simulating an unavailable module.",
        "rather than “no presence.”.": "rather than “no presence.”",
    },
    "mechanical-design/README.md": {
        "The current ORIGIN Core enclosure is being developed around the following confirmed project constraints **Rosetta v2 PCB:** approximately 105 × 100 mm;":
        "The current ORIGIN Core enclosure is being developed around the following confirmed project constraints: **Rosetta v2 PCB:** approximately 105 × 100 mm;",
    },
    "mechanical-design/cad.md": {
        "Examples include a 3 mm screw should not automatically use a 3.00 mm printed clearance hole, a PCB should not be trapped between walls at its exact nominal width, a service cover needs enough clearance to open after surface variation, and press fits require process-specific calibration.":
        "For example, a 3 mm screw should not automatically use a 3.00 mm printed clearance hole; a PCB should not be trapped between walls at its exact nominal width; a service cover needs sufficient clearance to remain serviceable despite manufacturing variation; and press fits require process-specific calibration.",
    },
    "modules/bits.md": {
        "Examples include could include environmental, proximity, or site-specific sensing, but only confirmed modules should be listed as supported hardware.":
        "Potential examples include environmental, proximity, or site-specific sensing, but only confirmed modules should be listed as supported hardware.",
    },
    "open-source/development-setup.md": {
        "Examples include should contain placeholders only.": "Examples should contain placeholders only.",
    },
    "software/architecture.md": {
        "The software architecture is designed around the following goals **modularity** — replace or revise components without rewriting the entire stack;":
        "The software architecture is designed around the following goals: **modularity** — replace or revise components without rewriting the entire stack;",
        "Examples include a radar failure should not prevent environmental sensors from being sampled, remote connectivity loss should not erase local health state, a malformed remote message should not crash the acquisition loop, and optional modules should fail gracefully if absent.":
        "Failure isolation is deliberate: a radar failure should not prevent environmental sensors from being sampled, remote connectivity loss should not erase local health state, a malformed remote message should not crash the acquisition loop, and absent optional modules should fail gracefully.",
    },
    "testing-validation/field-testing.md": {
        "Field testing should answer questions such as Does the complete ORIGIN unit remain mechanically stable after installation?; Do sensors cover the intended zones from the installed position?; Are false detections acceptable and explainable?; Does the power system support the intended operating cycle?; Does communication remain reliable enough for the deployment?; Are failures visible to operators?; Can the unit be serviced without disturbing the site?; and Does the system recover correctly after power or network interruption?.":
        "Field testing should answer practical questions such as: Does the complete ORIGIN unit remain mechanically stable after installation? Do the sensors cover the intended zones from the installed position? Are false detections acceptable and explainable? Does the power system support the intended operating cycle? Is communication reliable enough for the deployment? Are failures visible to operators? Can the unit be serviced without disturbing the site? Does the system recover correctly after a power or network interruption?",
        "Recommended checks successful boot; sensor health; storage/logging; communication; known configuration; battery/power state; and mechanical inspection.":
        "Recommended checks include successful boot, sensor health, storage and logging, communications, the known configuration, battery or power state, and a mechanical inspection.",
        "Examples include person enters intended zone; person remains still; person exits; unit is moved or disturbed where tamper sensing is implemented; and selected sensor is disconnected.":
        "Known test events can include a person entering the intended zone, remaining still, and exiting; movement or disturbance of the unit where tamper sensing is implemented; and disconnection of a selected sensor.",
    },
    "testing-validation/galene-lab-standards.md": {
        "Examples include one delayed startup among ten repetitions; temporary communication warning; unexpected temperature rise; visible enclosure flex; and one false detection outside the acceptance window.":
        "Examples include a delayed startup during repeated trials, a temporary communication warning, an unexpected temperature rise, visible enclosure flex, or a false detection outside the acceptance window.",
    },
    "rosetta/rosetta-v2.md": {
        "Rosetta v2 development has included the following main blocks an ESP32-family embedded processor;":
        "Rosetta v2 development has included the following main blocks: an ESP32-family embedded processor;",
        "it should be considered **pre-production** until all of the following are complete schematic review;":
        "it should be considered **pre-production** until all of the following are complete: schematic review;",
    },
    "rosetta/manufacturing.md": {
        "Before uploading to a board house schematic revision frozen;":
        "Before uploading to a board house, confirm the following: schematic revision frozen;",
    },
    "origin-core/README.md": {
        "The Core therefore has several responsibilities at the same time collect data from connected sensors;":
        "The Core therefore has several responsibilities at the same time: collect data from connected sensors;",
    },
    "origin-core/connectivity.md": {
        "A connection can fail in many ways network unavailable;":
        "A connection can fail in many ways: network unavailable;",
    },
    "mechanical-design/waterproofing.md": {
        "The current enclosure architecture has several likely weak points radar openings;":
        "The current enclosure architecture has several likely weak points: radar openings;",
    },
    "open-source/contributing.md": {
        "Before opening a change, determine which kind of contribution you are making documentation correction;":
        "Before opening a change, determine which kind of contribution you are making: documentation correction;",
        "Before requesting review, confirm The change solves a clearly stated problem;":
        "Before requesting review, confirm the following: the change solves a clearly stated problem;",
    },
    "open-source/licensing.md": {
        "Before calling a subsystem formally open-source/open-hardware, confirm The copyright owner(s) are identified;":
        "Before calling a subsystem formally open-source/open-hardware, confirm the following: the copyright owner(s) are identified;",
    },
    "mechanical-design/enclosure.md": {
        "until at least the following are confirmed all internal components fit;":
        "until at least the following are confirmed: all internal components fit;",
    },
}


def generic_polish(text: str) -> str:
    # Punctuation around sequences of questions converted from bullet lists.
    text = text.replace("?; and ", "? ")
    text = text.replace("?; ", "? ")
    text = text.replace("?.", "?")

    # Introduce multi-question sequences cleanly.
    text = re.sub(r"\bquestions such as (Does|Do|Are|Can|Is|Should|Will)\b", r"questions such as: \1", text)
    text = re.sub(r"\bQuestions include (Can|Does|Do|Are|Is|Should|Will)\b", r"Questions include: \1", text)
    text = re.sub(r"\bKey questions include (Can|Does|Do|Are|Is|Should|Will)\b", r"Key questions include: \1", text)
    text = re.sub(r"\bPlacement questions include should\b", "Placement review should answer questions such as: Should", text)
    text = re.sub(r"\bshould answer (Which|What|Can|Does|Do|Are|Is|Should|Will)\b", r"should answer: \1", text)
    text = re.sub(r"\bto answer questions such as (Which|What|Can|Does|Do|Are|Is|Should|Will)\b", r"to answer questions such as: \1", text)

    # Standard English punctuation after 'for example'.
    text = re.sub(r"(?m)^For example (?![,])", "For example, ", text)

    # Common list lead-ins that lost punctuation when unordered bullets were converted.
    text = text.replace("Recommended evidence pre/post photographs;", "Recommended evidence includes pre/post photographs;")
    text = text.replace("Examples include should contain placeholders only.", "Examples should contain placeholders only.")
    return text


changed = 0
for rel, replacements in REPLACEMENTS.items():
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    original = text
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = generic_polish(text)
    if text != original:
        path.write_text(text, encoding="utf-8")
        changed += 1
        print(f"polished {rel}")

# Apply the safe generic punctuation rules to every content page as well.
for path in sorted(ROOT.rglob("*.md")):
    rel = path.relative_to(ROOT).as_posix()
    if rel == "SUMMARY.md" or rel in REPLACEMENTS or ".git" in path.parts:
        continue
    text = path.read_text(encoding="utf-8")
    revised = generic_polish(text)
    if revised != text:
        path.write_text(revised, encoding="utf-8")
        changed += 1
        print(f"polished {rel}")

print(f"POLISHED_FILES={changed}")
