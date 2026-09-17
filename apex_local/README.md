# APEX Local

Self-contained local terminal agent based on the supplied APEX Local specification.

- Offline `echo` provider by default
- Optional local Ollama provider
- Workspace sandbox
- Permission modes: `ask`, `accept-edits`, `read-only`
- Local sessions, tools, routing, hooks, skills, and subagents
- No cloud provider is required

Run:

```powershell
python -m apex_local.cli init --workspace . --profile offline
python -m apex_local.cli status
python -m apex_local.cli run
```

The canonical APEX repository is `rahmaanherman-source/Apex-Hub`; this implementation lives under `apex_local/`.
