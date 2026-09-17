# Request flow

1. Client sends a task to `/run`.
2. Orchestrator resolves the task type through `config/models.yaml`.
3. Local Ollama is selected by default.
4. Skill calls are separate from inference.
5. Mutating skills return `approval_required` unless explicitly approved.
6. Health is available at `/health`.

No cloud fallback occurs unless configuration explicitly enables it.
