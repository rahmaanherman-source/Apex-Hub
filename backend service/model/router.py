"""
Model Router – Unified AI interface for APEX Hub.
Auto‑detects local runtimes, falls back to cloud, exposes a single `ask()` function.
"""

import os
import re
import httpx
import yaml
from pathlib import Path
from typing import Optional, Dict, Any, List

# Load configuration
config_path = Path(__file__).parent.parent.parent / "config" / "providers.yaml"
with open(config_path) as f:
    raw = f.read()
# Expand ${VAR} from environment
def _expand_env(match):
    return os.environ.get(match.group(1), "")
config = yaml.safe_load(re.sub(r'\$\{(\w+)\}', _expand_env, raw))

class ModelRouter:
    def __init__(self):
        self.local_providers: List[Dict[str, Any]] = []
        self.cloud_providers: List[Dict[str, Any]] = []
        self._detect_local()

    def _detect_local(self):
        """Ping each enabled local endpoint to see if it's alive."""
        local_cfg = config.get("ai", {}).get("local", {})
        for name, cfg in local_cfg.items():
            if not cfg.get("enabled"):
                continue
            endpoint = cfg.get("endpoint", "")
            if self._is_healthy(endpoint):
                self.local_providers.append({
                    "name": name,
                    "endpoint": endpoint,
                })
        # Cloud providers are always available if enabled
        cloud_cfg = config.get("ai", {}).get("cloud", {})
        for name, cfg in cloud_cfg.items():
            if cfg.get("enabled"):
                self.cloud_providers.append({
                    "name": name,
                    "api_key": cfg.get("api_key"),
                    "endpoint": cfg.get("endpoint"),  # may be None
                })

    def _is_healthy(self, url: str) -> bool:
        try:
            resp = httpx.get(f"{url}/health", timeout=2)
            return resp.status_code == 200
        except Exception:
            return False

    async def ask(
        self,
        prompt: str,
        model: Optional[str] = None,
        use_local: bool = True,
    ) -> Dict[str, Any]:
        """
        Send a prompt to the best available provider.
        Returns a dict with keys: answer, provider, model.
        """
        # 1. If a specific model is requested, try to use it
        if model:
            return await self._ask_model(model, prompt)

        # 2. Prefer local models
        if use_local and self.local_providers:
            provider = self.local_providers[0]  # first available
            return await self._ask_local(provider, prompt)

        # 3. Fallback to cloud
        if self.cloud_providers:
            provider = self.cloud_providers[0]  # first available cloud
            return await self._ask_cloud(provider, prompt)

        raise RuntimeError("No AI provider available. Check config/providers.yaml.")

    async def _ask_model(self, model_name: str, prompt: str) -> Dict[str, Any]:
        # Search in local providers first
        for p in self.local_providers:
            if p["name"] == model_name:
                return await self._ask_local(p, prompt)
        # Then cloud
        for p in self.cloud_providers:
            if p["name"] == model_name:
                return await self._ask_cloud(p, prompt)
        raise ValueError(f"Model {model_name} not found or not enabled.")

    async def _ask_local(self, provider: Dict, prompt: str) -> Dict[str, Any]:
        """Local models usually have an OpenAI‑compatible chat API."""
        endpoint = provider["endpoint"]
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.post(
                f"{endpoint}/v1/chat/completions",
                json={
                    "model": "local-model",  # many ignore this
                    "messages": [{"role": "user", "content": prompt}],
                },
            )
            resp.raise_for_status()
            data = resp.json()
            answer = data["choices"][0]["message"]["content"]
            return {
                "answer": answer,
                "provider": provider["name"],
                "model": "local",
            }

    async def _ask_cloud(self, provider: Dict, prompt: str) -> Dict[str, Any]:
        """Handle different cloud provider APIs."""
        name = provider["name"]
        if name == "openai":
            return await self._ask_openai(provider, prompt)
        elif name == "azure_openai":
            return await self._ask_azure(provider, prompt)
        elif name == "anthropic":
            return await self._ask_anthropic(provider, prompt)
        elif name == "gemini":
            return await self._ask_gemini(provider, prompt)
        elif name == "openrouter":
            return await self._ask_openrouter(provider, prompt)
        else:
            raise ValueError(f"Cloud provider {name} not supported")

    async def _ask_openai(self, provider, prompt):
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.post(
                "https://api.openai.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {provider['api_key']}"},
                json={
                    "model": "gpt-5",
                    "messages": [{"role": "user", "content": prompt}],
                },
            )
            resp.raise_for_status()
            data = resp.json()
            return {
                "answer": data["choices"][0]["message"]["content"],
                "provider": "openai",
                "model": "gpt-5",
            }

    async def _ask_azure(self, provider, prompt):
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.post(
                f"{provider['endpoint']}/openai/deployments/gpt-5/chat/completions?api-version=2024-02-15-preview",
                headers={"api-key": provider["api_key"]},
                json={"messages": [{"role": "user", "content": prompt}]},
            )
            resp.raise_for_status()
            data = resp.json()
            return {
                "answer": data["choices"][0]["message"]["content"],
                "provider": "azure_openai",
                "model": "gpt-5",
            }

    async def _ask_anthropic(self, provider, prompt):
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.post(
                "https://api.anthropic.com/v1/messages",
                headers={
                    "x-api-key": provider["api_key"],
                    "anthropic-version": "2023-06-01",
                },
                json={
                    "model": "claude-3-5-sonnet-20240620",
                    "max_tokens": 1024,
                    "messages": [{"role": "user", "content": prompt}],
                },
            )
            resp.raise_for_status()
            data = resp.json()
            return {
                "answer": data["content"][0]["text"],
                "provider": "anthropic",
                "model": "claude-3-5-sonnet",
            }

    async def _ask_gemini(self, provider, prompt):
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.post(
                f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={provider['api_key']}",
                json={"contents": [{"parts": [{"text": prompt}]}]},
            )
            resp.raise_for_status()
            data = resp.json()
            return {
                "answer": data["candidates"][0]["content"]["parts"][0]["text"],
                "provider": "gemini",
                "model": "gemini-2.0-flash",
            }

    async def _ask_openrouter(self, provider, prompt):
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={"Authorization": f"Bearer {provider['api_key']}"},
                json={
                    "model": "openai/gpt-5",
                    "messages": [{"role": "user", "content": prompt}],
                },
            )
            resp.raise_for_status()
            data = resp.json()
            return {
                "answer": data["choices"][0]["message"]["content"],
                "provider": "openrouter",
                "model": "openai/gpt-5",
            }

# Singleton instance
router = ModelRouter()