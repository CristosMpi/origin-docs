from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SKIP = {"SUMMARY.md"}

PATTERNS = {
    "incomplete_language": re.compile(r"\b(TBD|TODO|not yet|does not yet|not currently|currently does not|missing|incomplete|pre-production|prototype|experimental|pending|blocker|not production-ready|not release-ready)\b", re.I),
    "internal_release_language": re.compile(r"\b(release checklist|release review|release package|fabrication package|manufacturing package|board house|Gerber|Excellon|drill file|pick-and-place|CPL|first article|bring-up|DRC|ERC|footprint|BOM verification|schematic review)\b", re.I),
    "future_commitment_language": re.compile(r"\b(planned|should eventually|will be added|when .*? released|once .*? finalized|future source release|future reproducible|future implementation|future version)\b", re.I),
    "public_repo_gap": re.compile(r"\b(public repo|public repository|not published|not included|not available|not present|source release|source files.*released)\b", re.I),
    "negative_status": re.compile(r"\b(known issue|known issues|known limitation|known limitations|failure|fault|defect|rejected|cancelled|canceled|wrong|problem|issue)\b", re.I),
    "development_team": re.compile(r"\b(developer|development team|engineering team|contributors?|maintainer|pull request|commit|branch|toolchain|compiler|framework version|source tree|unit test|regression test|debug|debugging)\b", re.I),
}

for path in sorted(ROOT.rglob("*.md")):
    rel = path.relative_to(ROOT).as_posix()
    if rel in SKIP or ".git" in path.parts:
        continue
    lines = path.read_text(encoding="utf-8").splitlines()
    in_fence = False
    hits = []
    for n, line in enumerate(lines, 1):
        s = line.strip()
        if s.startswith("```") or s.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence or not s:
            continue
        labels = [name for name, rx in PATTERNS.items() if rx.search(s)]
        if labels:
            hits.append((n, ",".join(labels), s))
    if hits:
        print(f"\n### {rel}")
        for n, labels, s in hits:
            print(f"{n}\t{labels}\t{s}")
