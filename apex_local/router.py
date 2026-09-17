from __future__ import annotations
from .config import Profile
from .providers import make_provider, BaseProvider


class Router:
    def __init__(self, profile: Profile):
        self.profile = profile
        kwargs = {"endpoint": profile.endpoint, "model": profile.model} if profile.provider == "ollama" else {}
        self.provider: BaseProvider = make_provider(profile.provider, **kwargs)

    def pick(self) -> BaseProvider:
        if not self.provider.available():
            raise RuntimeError(f"Provider '{self.profile.provider}' is not available. Switch to offline profile.")
        return self.provider
