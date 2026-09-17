from __future__ import annotations
from pathlib import Path
from .sandbox import Sandbox


def read_file(sandbox: Sandbox, path: str, max_bytes: int = 500_000) -> dict:
    p = sandbox.resolve(path)
    if not p.exists(): return {"ok": False, "error": f"Not found: {path}"}
    if p.is_dir(): return {"ok": False, "error": f"Is a directory: {path}"}
    data = p.read_bytes()[:max_bytes]
    return {"ok": True, "path": str(p), "content": data.decode("utf-8", "replace"), "truncated": len(data) >= max_bytes}


def list_dir(sandbox: Sandbox, path: str = ".") -> dict:
    p = sandbox.resolve(path)
    if not p.exists(): return {"ok": False, "error": f"Not found: {path}"}
    return {"ok": True, "path": str(p), "entries": [{"name": c.name, "type": "dir" if c.is_dir() else "file", "size": c.stat().st_size if c.is_file() else None} for c in sorted(p.iterdir())]}


def write_file(sandbox: Sandbox, path: str, content: str) -> dict:
    p = sandbox.resolve(path); p.parent.mkdir(parents=True, exist_ok=True); p.write_text(content, encoding="utf-8")
    return {"ok": True, "path": str(p), "bytes": len(content)}


def edit_file(sandbox: Sandbox, path: str, old: str, new: str, count: int = 1) -> dict:
    p = sandbox.resolve(path)
    if not p.exists(): return {"ok": False, "error": f"Not found: {path}"}
    text = p.read_text(encoding="utf-8")
    if old not in text: return {"ok": False, "error": "old string not found"}
    p.write_text(text.replace(old, new, count), encoding="utf-8")
    return {"ok": True, "path": str(p), "replacements": count}
