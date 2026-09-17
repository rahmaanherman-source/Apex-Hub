from __future__ import annotations
import re
from ..sandbox import Sandbox


def search(sandbox: Sandbox, pattern: str, path: str = ".", max_hits: int = 200) -> dict:
    root = sandbox.resolve(path); rx = re.compile(pattern); hits=[]
    for p in sandbox.root.rglob("*"):
        if not p.is_file() or any(x in p.parts for x in (".git","node_modules","venv",".venv","__pycache__",".apex")): continue
        try: text=p.read_text(encoding="utf-8",errors="ignore")
        except Exception: continue
        if root.is_dir() and root not in p.parents and p != root: continue
        for i,line in enumerate(text.splitlines(),1):
            if rx.search(line):
                hits.append({"path":str(p.relative_to(sandbox.root)),"line":i,"text":line[:300]})
                if len(hits)>=max_hits: return {"ok":True,"hits":hits,"truncated":True}
    return {"ok":True,"hits":hits}


def glob(sandbox: Sandbox, pattern: str) -> dict:
    return {"ok": True, "matches": sorted(str(p.relative_to(sandbox.root)) for p in sandbox.root.glob(pattern))}
