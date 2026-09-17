from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Capabilities:
    """Local replacement for Antigravity's regional capability matrix."""
    text: bool = True
    code: bool = True
    multimodal: bool = False
    image: bool = False
    shell: bool = True
    files: bool = True
    search: bool = True

    def as_dict(self) -> dict[str, bool]:
        return {
            "text": self.text, "code": self.code, "multimodal": self.multimodal,
            "image": self.image, "shell": self.shell, "files": self.files,
            "search": self.search,
        }


@dataclass
class Guarantees:
    """True by construction — nothing leaves the machine."""
    training_excluded: bool = True
    no_third_party_logging: bool = True
    no_network_calls: bool = True
    no_vendor_account: bool = True
    audit_log_local: bool = True

    def as_dict(self) -> dict[str, bool]:
        return self.__dict__.copy()


@dataclass
class Limitations:
    """Local replacements for Antigravity's known-limitation list."""
    no_cloud_models: bool = True
    no_remote_agents: bool = True
    ollama_optional: bool = True
    image_generation_unavailable: bool = True

    def as_dict(self) -> dict[str, bool]:
        return self.__dict__.copy()
