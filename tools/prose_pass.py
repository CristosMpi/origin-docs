from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP = {"SUMMARY.md"}

BULLET_RE = re.compile(r"^(?P<indent>\s*)[-*+]\s+(?P<body>.+?)\s*$")
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
    return f"{stem} {joined}."


def render_block(items: list[str]) -> list[str]:
    clean = [strip_item(x) for x in items if strip_item(x)]
    if not clean:
        return []

    # Labelled definitions read more professionally as short standalone paragraphs.
    if any(BOLD_LABEL_RE.match(x) for x in clean):
        return [sentence_case_item(x) for x in clean]

    # Short noun/verb phrases become one compact narrative sentence.
    if all(is_short_phrase(x) for x in clean):
        if len(clean) <= 6:
            return [serial_join(clean) + "."]
        split = (len(clean) + 1) // 2
        first = serial_join(clean[:split]) + "."
        second = serial_join(clean[split:]) + "."
        return [first, second]

    # Longer entries become prose paragraphs rather than an artificial list.
    return [sentence_case_item(x) for x in clean]


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
                    # Allow a single indented continuation line inside a bullet.
                    if items and lines[j].startswith(("  ", "\t")) and lines[j].strip() and not lines[j].lstrip().startswith(("- ", "* ", "+ ")):
                        items[-1] += " " + lines[j].strip()
                        j += 1
                        continue
                    break
                items.append(m.group("body"))
                j += 1

            # Find the immediately preceding prose line, allowing one blank separator.
            intro_idx = len(out) - 1
            if intro_idx >= 0 and out[intro_idx] == "":
                intro_idx -= 1

            if intro_idx >= 0 and intro_can_absorb(out[intro_idx]):
                out[intro_idx] = merge_intro(out[intro_idx], items)
                # Remove the blank line that separated the intro and list.
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

    # Collapse excessive blank lines introduced by conversion.
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

    # Editorial polish for recurring documentation phrasing.
    result = result.replace("These docs", "This documentation")
    result = result.replace("the docs", "the documentation")
    result = result.replace("Do not", "Do not")
    return result


def main() -> None:
    changed = 0
    scanned = 0
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
    print(f"Reviewed {scanned} Markdown pages; changed {changed}.")


if __name__ == "__main__":
    main()
