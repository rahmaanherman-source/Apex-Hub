from __future__ import annotations
import json
import os
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Optional


APEX_HOME = Path(os.environ.get("APEX_HOME", Path.cwd() / ".apex"))
CONFIG_PATH = APEX_HOME / "config.json"


@dataclass
class Profile:
    name: str
    provider: str = "echo"           # echo | mock | ollama
    model: str = "qwen2.5-coder:7b"
    endpoint: str = "http://localhost:11434"
    capabilities: list[str] = field(default_factory=lambda: ["text", "code"])
    notes: str = ""


DEFAULT_PROFILES = {
    "offline": Profile(name="offline", provider="echo", model="echo", capabilities=["text"]),
    "local":   Profile(name="local",   provider="ollama", model="qwen2.5-coder:7b", capabilities=["text", "code"]),
    "mock":    Profile(name="mock",    provider="mock", model="mock", capabilities=["text"]),
}


@dataclass
class APEXConfig:
    profile: str = "offline"
    mode: str = "accept-edits"       # ask | accept-edits | read-only
    workspace: str = "."
    log_level: str = "INFO"
    profiles: dict[str, Profile] = field(default_factory=lambda: dict(DEFAULT_PROFILES))

    @classmethod
    def load(cls) -> "APEXConfig":
        if CONFIG_PATH.exists():
            try:
                raw = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
                profiles = {
                    k: Profile(**v) for k, v in raw.get("profiles", {}).items()
                }
                if not profiles:
                    profiles = dict(DEFAULT_PROFILES)
                return cls(
                    profile=raw.get("profile", "offline"),
                    mode=raw.get("mode", "accept-edits"),
                    workspace=raw.get("workspace", "."),
                    log_level=raw.get("log_level", "INFO"),
                    profiles=profiles,
                )
            except Exception:
                pass
        return cls()

    def save(self) -> None:
        APEX_HOME.mkdir(parents=True, exist_ok=True)
        payload = {
            "profile": self.profile,
            "mode": self.mode,
            "workspace": self.workspace,
            "log_level": self.log_level,
            "profiles": {k: asdict(v) for k, v in self.profiles.items()},
        }
        CONFIG_PATH.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def current_profile(self) -> Profile:
        return self.profiles.get(self.profile) or DEFAULT_PROFILES["offline"]
