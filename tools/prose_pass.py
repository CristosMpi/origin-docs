from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP = {"SUMMARY.md"}

BULLET_RE = re.compile(r"^(?P<indent>\s*)[-*+]\s+(?P<body>.+?)\s*$")
QUOTE_BULLET_RE = re.compile(r"^(?P<prefix>\s*>\s*)[-*+]\s+(?P<body>.+?)\s*$")
CHECKBOX_RE = re.compile(r"^\[[ xX]\]\s*")
BOLD_LABEL_RE = re.compile(r"^\*\*(.+?)\*\*\s*[—–:-]\s*(.+)$")


def strip_item(text: str) -> str:
    text = CHECKBOX_RE.sub("", text.strip())
    text = re.sub(r"\s+", " ", text)
    return text


def sentence_case_item(text: str) -> str:
    text = strip_item(text)
    m = BOLD_LABEL_RE.match(text)
    if m:
        label, rest = m.groups()
        label = label.rstrip(".:")
        rest = rest.strip()
        if rest and rest[0].isalpha():
            rest = rest[0].lower() + rest[1:]
        text = f"**{label}.** {rest}"
    if text and text[-1] not in ".!?`)]":
        text += "."
    return text


def serial_join(items: list[str]) -> str:
    items = [strip_item(x).rstrip(".;,") for x in items if strip_item(x)]
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} and {items[1]}"
    return ", ".join(items[:-1]) + f", and {items[-1]}"


def semicolon_join(items: list[str]) -> str:
    items = [strip_item(x).rstrip(".;,") for x in items if strip_item(x)]
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]}; and {items[1]}"
    return "; ".join(items[:-1]) + f"; and {items[-1]}"


def is_short_phrase(item: str) -> bool:
    plain = re.sub(r"[`*_\[\]()#]", "", strip_item(item))
    return len(plain) <= 105 and plain.count(". ") == 0 and not plain.endswith((".", "?", "!"))


def intro_can_absorb(line: str) -> bool:
    s = line.strip()
    if not s or s.startswith("#") or s.startswith(">") or s.startswith("|"):
        return False
    return s.endswith(":")


def merge_intro(intro: str, items: list[str]) -> str:
    stem = intro.rstrip()[:-1]
    joined = semicolon_join(items) if len(items) > 4 else serial_join(items)
    if not joined:
        return intro
    if stem.strip().lower() == "examples":
        stem = "Examples include"
    return f"{stem} {joined}."


def render_block(items: list[str]) -> list[str]:
    clean = [strip_item(x) for x in items if strip_item(x)]
    if not clean:
        return []
    if any(BOLD_LABEL_RE.match(x) for x in clean):
        return [sentence_case_item(x) for x in clean]
    if all(is_short_phrase(x) for x in clean):
        if len(clean) <= 6:
            return [serial_join(clean) + "."]
        split = (len(clean) + 1) // 2
        return [serial_join(clean[:split]) + ".", serial_join(clean[split:]) + "."]
    return [sentence_case_item(x) for x in clean]


def cleanup_prose(result: str) -> str:
    # Fix mechanical constructions from list-to-prose conversion.
    result = result.replace("This documentation are", "This documentation is")
    result = result.replace("These documentation", "This documentation")
    result = result.replace(";.", ".")
    result = result.replace(",.", ".")

    # A bare 'Examples:' list should become an actual sentence, not 'Examples X...'.
    result = re.sub(
        r"(?m)^Examples (?!include\b|may\b|of\b|from\b|where\b|such\b)(?=[a-z`*\[])",
        "Examples include ",
        result,
    )

    # Common grammar repair where a converted verb list follows 'objectives are'.
    verbs = "protect|prevent|detect|preserve|secure|maintain|limit|verify|reduce|ensure|support|provide|improve|keep|avoid|enable"
    result = re.sub(
        rf"\b(objectives are) ({verbs})\b",
        lambda m: f"{m.group(1)} to {m.group(2)}",
        result,
        flags=re.IGNORECASE,
    )

    result = result.replace(
        "can conceptually be deployed in several ways locally",
        "can conceptually be deployed in several ways: locally",
    )
    result = result.replace(
        "one of the following **",
        "one of the following: **",
    )

    # Capitalize prose paragraphs accidentally left lower-case after bullets were removed.
    lines = result.splitlines()
    in_fence = False
    polished: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            polished.append(line)
            continue
        if (
            not in_fence
            and line
            and line[0].islower()
            and not line.startswith(("http://", "https://"))
            and not stripped.startswith(("|", "<", "`"))
        ):
            line = line[0].upper() + line[1:]
        polished.append(line.rstrip())

    return "\n".join(polished).strip() + "\n"


def transform(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    in_fence = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            out.append(line)
            i += 1
            continue

        if not in_fence and BULLET_RE.match(line):
            items: list[str] = []
            j = i
            while j < len(lines):
                m = BULLET_RE.match(lines[j])
                if not m:
                    if items and lines[j].startswith(("  ", "\t")) and lines[j].strip() and not lines[j].lstrip().startswith(("- ", "* ", "+ ")):
                        items[-1] += " " + lines[j].strip()
                        j += 1
                        continue
                    break
                items.append(m.group("body"))
                j += 1

            intro_idx = len(out) - 1
            if intro_idx >= 0 and out[intro_idx] == "":
                intro_idx -= 1
            if intro_idx >= 0 and intro_can_absorb(out[intro_idx]):
                out[intro_idx] = merge_intro(out[intro_idx], items)
                if len(out) - 1 > intro_idx and out[-1] == "":
                    out.pop()
                out.append("")
            else:
                rendered = render_block(items)
                if out and out[-1] != "":
                    out.append("")
                for idx, paragraph in enumerate(rendered):
                    out.append(paragraph)
                    if idx != len(rendered) - 1:
                        out.append("")
                out.append("")
            i = j
            continue

        out.append(line)
        i += 1

    compact: list[str] = []
    blank = 0
    for line in out:
        if line.strip() == "":
            blank += 1
            if blank <= 1:
                compact.append("")
        else:
            blank = 0
            compact.append(line.rstrip())

    result = "\n".join(compact).strip() + "\n"
    result = result.replace("These docs", "This documentation")
    result = result.replace("the docs", "the documentation")
    return cleanup_prose(result)


def remaining_bullets(text: str) -> list[str]:
    leftovers: list[str] = []
    in_fence = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if not in_fence and (BULLET_RE.match(line) or QUOTE_BULLET_RE.match(line)):
            leftovers.append(line)
    return leftovers


def main() -> None:
    changed = 0
    scanned = 0
    unresolved: list[tuple[str, str]] = []
    for path in sorted(ROOT.rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        if rel in SKIP or ".git" in path.parts:
            continue
        scanned += 1
        original = path.read_text(encoding="utf-8")
        revised = transform(original)
        if revised != original:
            path.write_text(revised, encoding="utf-8")
            changed += 1
            print(f"updated {rel}")
        else:
            print(f"reviewed {rel} (no change)")
        for leftover in remaining_bullets(revised):
            unresolved.append((rel, leftover))

    print(f"Reviewed {scanned} Markdown pages; changed {changed}.")
    if unresolved:
        print("Unresolved unordered-list syntax remains:")
        for rel, line in unresolved:
            print(f"  {rel}: {line}")
        raise SystemExit(1)
    print("QA passed: no unordered bullet-list syntax remains outside SUMMARY.md or code fences.")


if __name__ == "__main__":
    main()
