# APEX Overnight Phone Control & Antigravity Discovery Design

## Goal
Give the local APEX Overnight Supervisor a phone notification/approval surface while preserving Gatekeeper as the credential boundary and adding evidence-backed Antigravity discovery.

## Architecture
The desktop remains the execution authority: Ollama, deterministic audits, Gatekeeper/Vault metadata, repository checks, repairs, verification, and evidence all run locally. ntfy is used only as a sanitized push transport; the phone receives no secret values and never becomes a credential store. Remote approval is authenticated by a one-time capability bound to an approval request, action, expiry, and nonce; the local gateway remains the only component allowed to mutate the approval queue.

Antigravity discovery is evidence-only overnight. Presence, version, configuration, authentication hints, and capability claims are recorded without inventing endpoints or treating installation presence as verified inference capability. Cloud execution remains daytime/on-demand.

## Security invariants
- Secret values never enter notifications, phone URLs, approval records, reports, logs, model prompts, or source code.
- Credential references may be surfaced; credential values may not.
- Request IDs are identifiers, not authorization credentials.
- Approval capabilities are random, single-use, action-bound, and expiry-bound.
- Expired, replayed, malformed, or mismatched approvals are rejected.
- The overnight supervisor performs no public cloud health probes.
- Only loopback local services are callable by overnight tasks, except the explicit ntfy notification transport.
- No money movement, irreversible publishing, credential rotation, destructive deletion, or ownership changes occur autonomously overnight.
- Every successful action has verification evidence; failures remain failures.

## Phone workflow
1. Overnight task creates a local pending approval.
2. A random one-time approval capability is generated and stored locally; only a sanitized action URL is sent to ntfy.
3. The phone opens the approval URL through the configured private access path.
4. Gateway validates capability, request status, action binding, expiry, and replay state.
5. Gateway atomically records APPROVED/DENIED/DEFERRED and emits evidence.
6. The actual authorized operation, if any, executes on the desktop through Gatekeeper; the phone never receives the credential.

## Antigravity states
`NOT INSTALLED`, `PRESENT — CAPABILITY UNVERIFIED`, `AUTH CONFIGURED — CAPABILITY UNVERIFIED`, `CAPABILITY VERIFIED`, `BLOCKED`, `DAYTIME ONLY`.

## Overnight sequence
System snapshot → local AI discovery → Antigravity discovery → workspace/repository audit → Gatekeeper/Vault audit → local connected-app inventory → security scan → build/test/typecheck/lint → safe repair → re-test → revenue readiness evidence → phone decision queue → report.

## Verification
Tests must cover redaction, approval capability security, expiry/replay, local-only network policy, Antigravity classification, model enumeration, STOP behavior, task sequencing, and report generation. A final post-repair verification pass is mandatory.
