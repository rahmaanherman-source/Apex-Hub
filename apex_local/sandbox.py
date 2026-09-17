from __future__ import annotations
from pathlib import Path


class SandboxError(Exception):
    pass


class Sandbox:
    """Workspace chroot. Every path resolves inside workspace root or is rejected."""

    def __init__(self, workspace: str):
        self.root = Path(workspace).expanduser().resolve()
        if not self.root.exists():
            raise SandboxError(f"Workspace does not exist: {self.root}")

    def resolve(self, rel_or_abs: str) -> Path:
        p = Path(rel_or_abs)
        if not p.is_absolute():
            p = self.root / p
        p = p.resolve()
        try:
            p.relative_to(self.root)
        except ValueError:
            raise SandboxError(f"Path escapes workspace: {rel_or_abs} -> {p}")
        return p
