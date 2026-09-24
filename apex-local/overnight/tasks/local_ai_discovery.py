"""Discover and health-check every installed Ollama model."""
from .base import Task
from .. import ollama_bridge as ob


def discover_model_health() -> dict:
    running = ob.is_running()
    if not running:
        running = ob.ensure_running()
    models = ob.list_models() if running else []
    health = {}
    for model in models:
        health[model] = ob.health_check(model, timeout=90)
    return {"ollama_running": running, "models": models, "health": health, "verified": [m for m, result in health.items() if result.get("ok")]}


class LocalAIDiscovery(Task):
    name = "local_ai_discovery"
    timeout_s = 900

    def run(self):
        return discover_model_health()
