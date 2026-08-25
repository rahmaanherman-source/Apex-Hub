# APEX AI / Eri Integration Boundary

**Status:** ARCHITECTURE DEFINED — EXTERNAL REPOSITORY NOT IDENTIFIED/CONNECTED

## Purpose

APEX Analytics may expose an AI-agent layer for explaining analytics, surfacing anomalies, and proposing next actions. The AI layer does not become the source of truth and does not receive unrestricted credentials.

## Boundary

```text
APEX DATA + EVIDENCE
        |
        v
ANALYTICS ENGINE
        |
        +--> AI / Eri proposal layer
        |
        v
TRUTH GATE / AUTHORIZATION
        |
        v
EXECUTION
```

The agent can propose. Deterministic services verify and execute according to policy.

## Required controls

- Vault-controlled credentials
- credential references rather than raw secrets in prompts
- least-privilege tool access
- audit event for every material agent action
- explicit authorization for high-impact operations
- no fake success states
- source/evidence attached to analytical claims
- model output separated from measured system state

## External AI Eri status

The exact repository/account for the user's existing "AI Eri" implementation was not identifiable from the currently connected GitHub repositories. This file reserves the integration boundary without claiming that an external Eri repository has been connected.

When the correct repository is identified, add a verified adapter/reference here rather than guessing or importing an unrelated public project.
