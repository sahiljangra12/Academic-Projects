"""Fail if any relative link or image in a README points to a missing file."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATTERN = re.compile(r'\]\(([^)\s]+)\)|(?:src|href)="([^"]+)"')

broken = []
for readme in ROOT.rglob("README.md"):
    if ".git" in readme.parts:
        continue
    for match in PATTERN.finditer(readme.read_text(encoding="utf-8")):
        target = next(g for g in match.groups() if g)
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        if not (readme.parent / target.split("#")[0]).exists():
            broken.append(f"{readme.relative_to(ROOT)} -> {target}")

print("\n".join(broken) if broken else "All README links resolve.")
sys.exit(1 if broken else 0)
