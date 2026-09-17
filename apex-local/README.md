# APEX Local

Local-first APEX orchestration workspace. Ollama is the default inference provider; cloud providers are opt-in.

## Quick start
1. Run `APEX_INSTALL.ps1` from Windows PowerShell.
2. The installer creates the local workspace, Python environment, Ollama model(s), Vault, backend, shortcuts, and health checks.
3. Backend docs: http://127.0.0.1:8000/docs

Secrets belong in `secrets/.env` and are never committed.
