"""Bounded APEX workspace discovery."""
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CANDIDATES = [
    ROOT,
    Path(os.path.expandvars(r"%USERPROFILE%/Desktop/apex-local")),
    Path(os.path.expandvars(r"%USERPROFILE%/Desktop/APEX")),
]


def discover_workspaces(candidates=None) -> list[Path]:
    found = []
    for candidate in candidates or DEFAULT_CANDIDATES:
        path = Path(candidate).expanduser().resolve()
        if path.exists() and path.is_dir() and path not in found:
            found.append(path)
    return found
