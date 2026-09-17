from __future__ import annotations
import json
from pathlib import Path

class SkillStore:
    def __init__(self,root:Path): self.root=root; self.root.mkdir(parents=True,exist_ok=True)
    def list(self): return sorted(p.stem for p in self.root.glob("*.json"))
    def get(self,name):
        p=self.root/f"{name}.json"
        return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None
    def put(self,name,spec): (self.root/f"{name}.json").write_text(json.dumps(spec,indent=2),encoding="utf-8")
    def delete(self,name):
        p=self.root/f"{name}.json"
        if p.exists(): p.unlink(); return True
        return False
