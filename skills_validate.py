#!/usr/bin/env python3
"""Validate APEX Agent Skills structure and reject fake-green metadata."""
from __future__ import annotations
import re, sys, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?$")


def frontmatter(text: str):
    if not text.startswith("---\n"):
        return None, "missing YAML frontmatter"
    end = text.find("\n---", 4)
    if end < 0:
        return None, "unclosed YAML frontmatter"
    block = text[4:end]
    data = {}
    for line in block.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith(" "):
            continue
        if ":" not in line:
            return None, f"invalid frontmatter line: {line}"
        k, v = line.split(":", 1)
        data[k.strip()] = v.strip().strip('"')
    return data, None


def validate(path: Path):
    issues=[]; warnings=[]
    md=path/"SKILL.md"
    if not md.exists(): return ["missing SKILL.md"], []
    text=md.read_text(encoding="utf-8")
    fm, err=frontmatter(text)
    if err: issues.append(err); return issues,warnings
    for key in ("name","description"):
        if key not in fm or not fm[key]: issues.append(f"missing {key}")
    if "name" in fm:
        if not NAME_RE.fullmatch(fm["name"]): issues.append("invalid skill name")
        if fm["name"] != path.name: issues.append("name does not match directory")
        if "--" in fm["name"]: issues.append("consecutive hyphens are forbidden")
    if len(fm.get("description","")) > 1024: issues.append("description exceeds 1024 characters")
    if len(text.splitlines()) > 500: warnings.append("SKILL.md exceeds recommended 500 lines")
    if "TODO" in text or "FIXME" in text: warnings.append("contains TODO/FIXME")
    if re.search(r"status:\s*verified", text, re.I):
        warnings.append("skill claims verified status; repository validation does not grant verification")
    return issues,warnings


def main():
    if not SKILLS.exists():
        print("skills/: missing")
        return 1
    invalid=0
    for p in sorted(x for x in SKILLS.iterdir() if x.is_dir()):
        issues,warnings=validate(p)
        print(("PASS" if not issues else "FAIL"), p.name)
        for x in issues: print("  ISSUE:",x)
        for x in warnings: print("  WARN:",x)
        invalid += bool(issues)
    # Registry JSON, when present, must parse. This validator deliberately does not
    # promote capabilities to VERIFIED; runtime evidence does that.
    reg=ROOT/"CAPABILITY-REGISTRY/registry.json"
    if reg.exists():
        try: json.loads(reg.read_text(encoding="utf-8"))
        except Exception as e:
            print("FAIL registry.json:",e); invalid += 1
    return int(bool(invalid))

if __name__ == "__main__": sys.exit(main())
