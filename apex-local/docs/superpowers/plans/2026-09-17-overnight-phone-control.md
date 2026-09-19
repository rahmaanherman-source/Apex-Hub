# APEX Overnight Phone Control & Antigravity Discovery Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a local-first Overnight Supervisor extension with sanitized phone notifications/approvals, evidence-backed Antigravity discovery, strict secret handling, local connected-app inventory, and post-repair verification.

**Architecture:** Extend the existing `apex-local` Overnight Supervisor rather than creating a second supervisor or Gatekeeper. The phone is a notification/decision surface only; Gatekeeper remains the credential boundary. ntfy is an outbound notification transport, while approval requests use one-time authenticated capabilities and never contain secrets.

**Tech Stack:** Python 3, Flask, PyYAML, requests only for the explicit ntfy transport, Ollama CLI, PowerShell, JSONL evidence, Windows Task Scheduler.

**Spec:** `apex-local/docs/superpowers/specs/2026-09-17-overnight-phone-control-design.md`

## Global Constraints

- Overnight execution is local-first; cloud execution is daytime/on-demand.
- Secret values never enter phone payloads, logs, reports, model prompts, URLs, or source code.
- Request IDs are identifiers, not authorization credentials.
- Approval capabilities are random, single-use, action-bound, and expiry-bound.
- Antigravity presence does not imply verified inference capability.
- No autonomous money movement, irreversible publishing, destructive deletion, credential rotation, or ownership changes.
- Safe repair must be followed by re-test and verification.
- Existing proven APEX components are reused before new implementations are generated.

---

### Task 1: Evidence and redaction boundary

**Files:**
- Modify: `apex-local/overnight/evidence.py`
- Create: `apex-local/overnight/redaction.py`
- Test: `apex-local/tests/test_overnight_security.py`

**Interfaces:**
- `redact(value) -> sanitized value`
- `contains_secret_like_value(text) -> bool`
- `EvidenceLog.write(task, status, payload) -> None`

- [ ] Write failing tests for key-based and string-pattern redaction, including nested structures and traceback/command-output strings.
- [ ] Run the focused tests and confirm failure.
- [ ] Implement centralized redaction without storing raw secret text.
- [ ] Route EvidenceLog through the centralized redactor.
- [ ] Run focused tests and confirm pass.
- [ ] Commit the security boundary.

### Task 2: Approval capability security

**Files:**
- Modify: `apex-local/overnight/approvals/queue.py`
- Modify: `apex-local/overnight/remote/phone_gateway.py`
- Create: `apex-local/tests/test_phone_approvals.py`

**Interfaces:**
- `new_request(action, risk, reason, credential_ref="", context=None) -> request dict`
- `approval_url(request) -> str`
- `approve_with_capability(capability, action) -> result`
- `deny_with_capability(capability, action) -> result`
- `defer_with_capability(capability, action) -> result`

- [ ] Write failing tests for random capability generation, expiry, single-use replay rejection, action binding, and malformed capability rejection.
- [ ] Run focused tests and confirm failure.
- [ ] Implement hashed capability storage; never persist the raw capability in the request JSON.
- [ ] Make gateway mutations atomic and action-bound.
- [ ] Add an explicit emergency STOP endpoint that cannot approve work.
- [ ] Run focused tests and confirm pass.
- [ ] Commit approval security.

### Task 3: ntfy notification adapter

**Files:**
- Create: `apex-local/overnight/notifications/notifier.py`
- Create: `apex-local/overnight/notifications/__init__.py`
- Create: `apex-local/config/phone.yaml.example`
- Test: `apex-local/tests/test_notifier.py`

**Interfaces:**
- `send(title, message, priority="default", tags=None, actions=None) -> dict`
- `NOTIFY_BACKEND` selects the transport.

- [ ] Write tests proving payloads contain no secret-like fields/values and that action URLs use the configured gateway base.
- [ ] Implement the ntfy adapter with bounded timeout and sanitized payloads.
- [ ] Keep the topic configurable and never hard-code a real private topic.
- [ ] Run tests.
- [ ] Commit notification transport.

### Task 4: Antigravity discovery

**Files:**
- Create or replace: `apex-local/overnight/tasks/antigravity.py`
- Modify: `apex-local/config/phone.yaml.example`
- Test: `apex-local/tests/test_antigravity.py`

**Interfaces:**
- `AntigravityDiscovery.run() -> dict`
- Classification states documented by the design spec.

- [ ] Write tests for not-installed, installed-but-unverified, configured-but-unverified, and version-probe failure cases using mocked filesystem/process probes.
- [ ] Implement discovery using configured Windows paths plus PATH lookup.
- [ ] Record only safe metadata; do not dump config files or auth material.
- [ ] Never invent an inference endpoint or capability.
- [ ] Run tests.
- [ ] Commit Antigravity discovery.

### Task 5: Strict overnight network policy and connected-app inventory

**Files:**
- Create: `apex-local/overnight/network_policy.py`
- Create: `apex-local/overnight/tasks/connected_apps.py`
- Replace: `apex-local/overnight/tasks/app_health.py`
- Test: `apex-local/tests/test_local_only.py`

**Interfaces:**
- `assert_local_target(url) -> None`
- `inventory_connected_apps() -> dict`
- `ConnectedApps.run() -> dict`

- [ ] Write tests rejecting non-loopback URLs for overnight task execution while permitting localhost Gatekeeper/Ollama.
- [ ] Remove public cloud endpoint probes from overnight app health.
- [ ] Inventory provider configuration and Gatekeeper metadata without making external calls.
- [ ] Classify entries as `VERIFIED_LOCAL`, `DAYTIME_CHECK_REQUIRED`, `MISSING_CONFIGURATION`, or `BLOCKED`.
- [ ] Run tests.
- [ ] Commit local-only policy.

### Task 6: Complete local model discovery

**Files:**
- Modify: `apex-local/overnight/ollama_bridge.py`
- Modify: `apex-local/overnight/tasks/local_ai_discovery.py`
- Test: `apex-local/tests/test_local_ai_discovery.py`

**Interfaces:**
- `list_models() -> list[str]`
- `health_check(model, timeout=...) -> dict`
- `LocalAIDiscovery.run() -> dict`

- [ ] Write tests proving every discovered model is considered, not just the first five.
- [ ] Implement bounded per-model health checks with deterministic timeouts.
- [ ] Record verified models and failures separately.
- [ ] Avoid logging model output beyond safe length/shape metadata.
- [ ] Run tests.
- [ ] Commit local AI discovery.

### Task 7: Workspace, MCP, and Gatekeeper reconciliation

**Files:**
- Create: `apex-local/overnight/workspace.py`
- Create: `apex-local/overnight/tasks/mcp_audit.py`
- Modify: `apex-local/overnight/tasks/gatekeeper_audit.py`
- Test: `apex-local/tests/test_workspace_discovery.py`

**Interfaces:**
- `discover_workspaces() -> list[Path]`
- `MCPAudit.run() -> dict`
- `GatekeeperAudit.run() -> dict`

- [ ] Write tests for workspace discovery and metadata-only Gatekeeper handling.
- [ ] Discover configured APEX workspaces without traversing arbitrary sensitive system directories.
- [ ] Audit MCP configuration/availability without exposing credentials.
- [ ] Add evidence that Gatekeeper is bound to loopback and that credential values are never requested by the audit.
- [ ] Run tests.
- [ ] Commit reconciliation layer.

### Task 8: Build/test/repair/re-test lifecycle

**Files:**
- Modify: `apex-local/overnight/supervisor.py`
- Modify: `apex-local/overnight/tasks/build_test.py`
- Modify: `apex-local/overnight/tasks/safe_repair.py`
- Create: `apex-local/overnight/tasks/reverify.py`
- Test: `apex-local/tests/test_supervisor_sequence.py`

**Interfaces:**
- `SEQUENCE` includes discovery → audit → repair → reverify → report.
- `Reverify.run() -> dict`

- [ ] Write tests asserting reverify occurs after repair and STOP prevents later tasks.
- [ ] Expand build/test discovery to configured workspaces.
- [ ] Keep safe repairs strictly non-destructive.
- [ ] Add explicit post-repair verification.
- [ ] Run tests.
- [ ] Commit lifecycle changes.

### Task 9: Revenue readiness and dynamic morning report

**Files:**
- Create: `apex-local/overnight/tasks/revenue_readiness.py`
- Modify: `apex-local/overnight/tasks/report.py`
- Test: `apex-local/tests/test_report.py`

**Interfaces:**
- `RevenueReadiness.run() -> dict`
- `Report.run() -> dict`

- [ ] Write tests proving the report distinguishes verified infrastructure from prepared opportunities.
- [ ] Remove hard-coded claims that require fresh evidence.
- [ ] Generate a morning queue from actual evidence and explicit owner-action requirements.
- [ ] Include Antigravity, phone decisions, connected-app inventory, re-verification, and proof sections.
- [ ] Run tests.
- [ ] Commit report changes.

### Task 10: Scheduler, phone gateway startup, and operator docs

**Files:**
- Modify: `apex-local/scripts/register_overnight.ps1`
- Modify: `apex-local/scripts/run_overnight_now.ps1`
- Create: `apex-local/scripts/start_phone_gateway.ps1`
- Create: `apex-local/docs/overnight-phone-control.md`
- Test: PowerShell smoke checks + Python test suite

- [ ] Make scheduler working directory and interpreter explicit.
- [ ] Start gateway only on loopback unless an authenticated private transport is configured.
- [ ] Document ntfy setup and the security model without calling the topic a complete authentication boundary.
- [ ] Document Tailscale/private-network preference and explicitly warn against unauthenticated public tunneling.
- [ ] Run the complete test suite and smoke checks.
- [ ] Commit operational wiring.

### Task 11: Final verification and review

**Files:**
- All implementation files above.

- [ ] Run all Python tests.
- [ ] Run static syntax/import checks.
- [ ] Inspect the final diff for secret-bearing strings and unsafe network destinations.
- [ ] Verify the supervisor sequence contains post-repair verification.
- [ ] Verify Antigravity is never marked verified solely because an executable exists.
- [ ] Verify phone payloads contain no secret values.
- [ ] Verify approval replay/expiry/action mismatch are rejected.
- [ ] Verify no overnight task performs public cloud health probes.
- [ ] Commit only after verification evidence is captured.
