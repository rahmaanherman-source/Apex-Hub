# APEX Audit Feed + Model Fabric — Canonical Integration Specification

## 1. Audit event taxonomy

Canonical domains: `router`, `webhook`, `transactions`, `ledger`, `payout_fx`, `registry`, `verification`, `identity`, `security`, `admin`, plus `model_fabric` for local model discovery, health, capability testing, benchmarking, routing, fallback, and cloud escalation.

Representative events:

- `router.decision`, `router.fallback`, `router.circuit_breaker.open`, `router.circuit_breaker.close`, `router.no_route`
- `webhook.received`, `webhook.verified`, `webhook.signature_failed`, `webhook.processed`, `webhook.replayed`
- `tx.authorized`, `tx.captured`, `tx.settled`, `tx.failed`, `tx.refunded`, `tx.disputed`, `tx.reversed`
- `ledger.posted`, `ledger.reconciled`, `ledger.exception`, `ledger.chain_verified`, `ledger.chain_broken`
- `verification.gate_1.source` through `verification.gate_6.recon`, `verification.passed`, `verification.failed`
- `registry.changed`, `provider.status_changed`, `provider.registered`
- `model.discovered`, `model.health_checked`, `model.capability_tested`, `model.benchmarked`, `model.license_reviewed`, `model.enabled`, `model.disabled`
- `model.route_selected`, `model.fallback`, `model.no_route`, `model.cloud_escalation_requested`, `model.cloud_escalation_approved`, `model.cloud_escalation_denied`

## 2. Audit invariants

- `event_id` is unique and is the idempotency key.
- `seq` establishes one append order.
- `prev_hash` references the prior event hash; the first event uses 64 zeroes.
- `hash = SHA256(prev_hash || canonical)`.
- Audit rows are append-only: updates and deletes are rejected by database trigger.
- Consumers use durable cursors and may replay a failed batch; they must never silently skip an event.
- Alert delivery is idempotent on `(rule_id,event_id)`.
- Sensitive payment data such as PAN/CVV never enters audit payloads.

## 3. Local model truth states

`catalog_only` = known candidate, no local installation proof.

`discovered_local` = observed by a real local runtime probe.

`verified_local` = discovered, healthy, capability-tested, license-reviewed as required, and enabled by policy.

A UI must never translate a catalog candidate into installed/healthy/selectable status.

## 4. Model adapter contract

Every adapter exposes identity, execution scope, runtime, modalities, capabilities, context limits, resource requirements, privacy class, license/commercial-use status, health evidence, capability-test evidence, benchmark evidence, and current operational state.

Cloud adapters additionally expose a data-egress contract: permitted data classes, region, retention reference, approval requirement, and cost-estimate requirement.

## 5. Local-first router

Hard filters precede ranking:

1. task capability and modality match;
2. installed, healthy, enabled;
3. exact license/commercial-use requirement satisfied;
4. privacy/data-class policy satisfied;
5. hardware/VRAM admission passes;
6. required tool/structured-output support exists.

Only then may ranking consider quality evidence, latency, queue depth, measured resource cost, reliability, and context suitability.

If no compliant local route exists, the router returns an escalation requirement. It does not call a cloud provider itself. Cloud execution requires an approved adapter, local-gap evidence, data-egress assessment, cost estimate, and explicit policy/user approval.

## 6. VRAM admission

`usable_vram = free_vram - max(2048 MB, 15% of total VRAM)`.

Estimated footprint must include model weights, KV/context memory, workflow overhead, workload-specific latent memory, and safety margin. Admission occurs only when the complete estimate is within usable VRAM.

Fallback sequence: smaller verified model → lower quantization → reduced context/batch → lower image/video resolution or duration → queue → CPU/offload only if policy permits → block with `LOCAL_CAPACITY_INSUFFICIENT` → authorized cloud escalation requirement.

## 7. Truth/evidence gate

Material claims used for publication, payment, deployment, or irreversible actions require current verified evidence. Unsupported or stale material claims cause `REVIEW` or `BLOCK`, never automatic green.

## 8. Project memory slab

Persistent project state separates immutable source evidence from derived working context. It records source hashes, verified facts, open questions, model evaluation envelopes, approvals, decisions, execution events, and reboot reconciliation state.

Reboot behavior: preserve evidence → reload active slab → verify source hashes/freshness → flag stale/contradictory facts → retrieve current evidence → supersede outdated derived facts without erasing history → rebuild context → run project evaluation checks.

## 9. Continuous evaluation

Re-evaluate when model digest/version, prompt template, knowledge corpus, retrieval configuration, tools, context envelope, policy threshold, product/category, or market changes. Store the evaluation evidence and do not promote a regression to an approved operating envelope.

## 10. Implementation status

Architecture and source files are now recorded in the repository. Runtime installation, database application, local hardware discovery, model benchmarking, provider authentication, and production wiring remain UNVERIFIED until executed and evidenced.
