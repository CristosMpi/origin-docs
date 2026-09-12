from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SKIP = {"SUMMARY.md"}
patterns = [
    ("clausal_examples", re.compile(r"\bExamples include .*(?:\bshould\b|→|\bis not\b|\bdoes not\b|\bcan still\b)", re.I)),
    ("bare_examples", re.compile(r"^Examples? (?!include\b|may\b|can\b|of\b|from\b|where\b|such\b|for\b)", re.I)),
    ("question_chain", re.compile(r"\bsuch as (?:Does|Do|Are|Can|Is|Should|Will)\b")),
    ("for_example_missing_punct", re.compile(r"^For example [a-z]")),
    ("recommended_checks", re.compile(r"^(?:Recommended|Required|Useful|Important) (?:checks|items|information|fields|records|steps|outputs) [a-z]", re.I)),
    ("include_missing_colon", re.compile(r"\b(?:goals|objectives|priorities|states|categories|areas|factors|requirements|responsibilities) (?:include|are) [^:.]{0,45}(?:;)", re.I)),
    ("many_semicolons", re.compile(r"(?:;[^;]*){7,}")),
    ("double_period", re.compile(r"[.!?][.!?]+$")),
    ("documentation_pronoun", re.compile(r"This documentation is[^\n]{0,180}\. They\b")),
]

count = 0
for path in sorted(ROOT.rglob('*.md')):
    rel = path.relative_to(ROOT).as_posix()
    if rel in SKIP or '.git' in path.parts:
        continue
    lines = path.read_text(encoding='utf-8').splitlines()
    in_fence = False
    for n, line in enumerate(lines, 1):
        s = line.strip()
        if s.startswith('```') or s.startswith('~~~'):
            in_fence = not in_fence
            continue
        if in_fence or not s or s.startswith(('#', '|', '>')):
            continue
        for label, rx in patterns:
            if rx.search(s):
                count += 1
                print(f"{label}\t{rel}:{n}\t{s}")
                break
print(f"TOTAL_SUSPECT_LINES={count}")
