from __future__ import annotations
from enum import Enum


class Decision(str, Enum):
    ALLOW = "allow"
    DENY = "deny"
    ASK = "ask"


class Mode(str, Enum):
    ASK = "ask"
    ACCEPT_EDITS = "accept-edits"
    READ_ONLY = "read-only"


TOOL_CATEGORY = {
    "read_file": "read",
    "list_dir": "read",
    "search": "read",
    "glob": "read",
    "write_file": "write",
    "edit_file": "write",
    "run_shell": "shell",
}


class PermissionGate:
    """Mirrors agy's semantics locally."""

    def __init__(self, mode: Mode, auto_yes: bool = False):
        self.mode = mode
        self.auto_yes = auto_yes

    def check(self, tool_name: str, args: dict) -> Decision:
        cat = TOOL_CATEGORY.get(tool_name, "unknown")

        if cat == "read" or cat == "unknown":
            return Decision.ALLOW

        if self.mode == Mode.READ_ONLY:
            return Decision.DENY

        if cat == "write":
            if self.mode == Mode.ACCEPT_EDITS or self.auto_yes:
                return Decision.ALLOW
            return Decision.ASK

        if cat == "shell":
            if self.auto_yes:
                return Decision.ALLOW
            return Decision.ASK

        return Decision.DENY
