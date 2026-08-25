# APEX Centralized Identity & Agent Security

## Purpose

Provide one security architecture for human users and APEX bots/agents without copying provider secrets into every agent.

## Canonical flow

```text
Human / Bot Identity
        ↓
GitHub SSO / Identity Provider
        ↓
Teleport identity + RBAC (optional enforcement plane)
        ↓
APEX Gatekeeper
        ↓
credentialRef only
        ↓
APEX Vault
        ↓
authorized provider connection
        ↓
Audit + result verification
```

## Providers represented by the current APEX environment surface

- Google / Gemini
- OpenAI
- Azure OpenAI
- Anthropic
- GitHub
- Stripe
- GCP
- Apple
- Unreal
- Blender

This document defines architecture only. It does not contain or request raw credentials.

## Hard rules

1. Raw secrets never enter source control, prompts, UI, chat history, logs, URLs, or analytics.
2. Agents receive credential references, not master secret values.
3. Vault remains the canonical secret store.
4. Gatekeeper remains the canonical APEX authorization/orchestration boundary.
5. Teleport is an optional infrastructure identity/RBAC/MCP enforcement plane; it does not replace Vault or Gatekeeper.
6. Human approval is required for high-risk or destructive operations.
7. Every external action must produce an audit event and an evidence/result record.
8. Authentication is distinct from authorization and distinct from result verification.

## State model

```text
DEFINED → CONFIGURED → CONNECTED → TESTED → VERIFIED
```

Installing a skill, creating an OAuth application, or configuring a variable does not by itself mean an integration is connected or verified.
