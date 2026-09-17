# Latch + APEX on Windows

Latch Desktop is an optional governance/control plane for agent sessions. APEX remains the local-first runtime and owns its own routing/approval policy.

## Prerequisites

- Windows 10/11
- Node.js 20+
- npm
- Git

## Install from the official source

```powershell
git clone https://github.com/latchagent/latch-core.git
cd latch-core
npm install
npm run dev
```

The project documents Windows support and uses a local authorization server for runtime policy enforcement.

## APEX integration posture

- Keep APEX Ollama local inference independent of Latch.
- Use Latch for agent/tool governance, worktree isolation, activity monitoring, and optional sandboxing.
- Do not put APEX API secrets into agent prompts.
- Do not assume Latch is a secret vault. Its documented capabilities are broader agent governance; use a dedicated credential manager if you need secret storage/delivery.
- Keep `secrets/.env` out of Git as an interim APEX development mechanism.
- For production credentials, prefer an OS credential store or dedicated secret manager and add an explicit APEX adapter.

## Verify after launch

Run the APEX health check:

```powershell
.\scripts\health_check.ps1
```

Then inspect Latch's policy/activity controls before connecting an agent. Do not grant destructive shell, payment, or external-send permissions merely to make a first test pass.
