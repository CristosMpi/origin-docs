from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BANNED = {
    "status_wording": re.compile(r"\b(not yet|planned|prototype|experimental|pre-production|incomplete|TBD|TODO)\b", re.I),
    "fabrication_history": re.compile(r"\b(missing drill|drill data|drill file|Excellon|release blocker|fabrication package|Gerber package|Gerber export|reviewed Gerber|board house|first article)\b", re.I),
    "developer_workflow": re.compile(r"\b(pull request|commit SHA|development branch|toolchain|compiler|build commands?|debug build|programming/debug|source-tree|source repository.*connected|authoritative source.*connected)\b", re.I),
    "unfinished_release": re.compile(r"\b(will be added|should eventually|not production-ready|not release-ready|not published|not public|current public repository|known issues|known limitations|pre-release checklist|release checklist)\b", re.I),
}

# Markdown destinations are implementation details of the wiki and are not reader-visible wording.
LINK_DEST = re.compile(r"\]\([^)]*\)")

hits = 0
for path in sorted(ROOT.rglob("*.md")):
    rel = path.relative_to(ROOT).as_posix()
    if ".git" in path.parts or rel.startswith("tools/"):
        continue
    lines = path.read_text(encoding="utf-8").splitlines()
    in_fence = False
    for n, line in enumerate(lines, 1):
        s = line.strip()
        if s.startswith("```") or s.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        visible = LINK_DEST.sub("]", s)
        labels = [k for k, rx in BANNED.items() if rx.search(visible)]
        if labels:
            hits += 1
            print(f"{rel}:{n}\t{','.join(labels)}\t{visible}")
print(f"PUBLIC_WIKI_FLAGGED_LINES={hits}")
