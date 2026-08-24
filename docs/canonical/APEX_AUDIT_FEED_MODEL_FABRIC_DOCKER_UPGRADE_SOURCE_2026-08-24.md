# APEX Audit Feed + Model Fabric + Docker Upgrade Source Record

**Date:** 2026-08-24  
**Repository:** `rahmaanherman-source/Apex-Hub`  
**Status:** SOURCE-DERIVED SPECIFICATION / RUNTIME VERIFICATION REQUIRED

## Purpose

This document records the file-level upgrade package supplied for APEX Audit Feed, APEX AI / Model Fabric / Gabby, Docker runtime integrations, staging, and GCP toggles. It is architecture/source material, not proof that every listed file exists or that every integration has executed.

The governing truth boundary is:

> Files existing ≠ code executed.

Promotion must remain:

**SPECIFIED / IMPLEMENTED → TESTED → VERIFIED**

No documentation-only status may be promoted to green.

## 1. File-Level Upgrade Map

### Canonical documentation

- `docs/canonical/APEX_AUDIT_FEED_AND_MODEL_FABRIC.md`
- `docs/audit/APEX_AUDIT_FEED_IMPLEMENTATION_RECORD_2026-08-24.md`
- `docs/operations/APEX_MODEL_FABRIC_RUNBOOK.md`
- `docs/gabby/GABBY_CHIEF_OF_STAFF_SPEC.md`
- `docs/gabby/GABBY_MEMORY_SLAB_SPEC.md`
- `docs/gabby/GABBY_TRUTH_ENGINE_SPEC.md`
- `docs/gabby/GABBY_EVALUATION_SPEC.md`

### Audit and evidence

- `supabase/migrations/20260824_apex_audit_feed.sql`
- `src/lib/audit/AuditBus.py`
- `src/lib/evidence/evidence_store.py`
- `src/lib/evidence/evidence_validator.py`

### AI / Model Fabric

- `src/lib/ai/model_registry.py`
- `src/lib/ai/model_adapter.py`
- `src/lib/ai/model_router.py`
- `src/lib/ai/capability_registry.py`
- `src/lib/ai/gpu_probe.py`
- `src/lib/ai/runtime_discovery.py`
- `src/lib/ai/resource_admission.py`
- `src/lib/ai/evaluation.py`

### Gabby

- `src/lib/gabby/chief_of_staff.py`
- `src/lib/gabby/memory_slab.py`
- `src/lib/gabby/truth_engine.py`
- `src/lib/gabby/approval_gate.py`
- `src/lib/gabby/task_controller.py`

### Runtime API

- `src/api/audit.py`
- `src/api/models.py`
- `src/api/gabby.py`

### Verification

- `tests/audit/test_append_only.py`
- `tests/audit/test_hash_chain.py`
- `tests/audit/test_idempotency.py`
- `tests/audit/test_consumers.py`
- `tests/ai/test_model_registry.py`
- `tests/ai/test_router.py`
- `tests/ai/test_vram_admission.py`
- `tests/ai/test_evaluation.py`
- `tests/gabby/test_truth_engine.py`
- `tests/gabby/test_memory_slab.py`
- `tests/gabby/test_approval_gate.py`

## 2. Docker / Integration Layer

The supplied runtime blueprint adds:

- `Dockerfile`
- `docker-compose.yml`
- `docker-compose.external.yml`
- `docker-entrypoint.sh`
- `.env.example`
- `.gitignore`
- `backend/main.py`
- `backend/integrations/config.py`
- `backend/integrations/unreal_adapter.py`
- `backend/integrations/blender_adapter.py`
- `backend/integrations/stripe_adapter.py`
- `backend/integrations/gcp_adapter.py`
- `backend/audit_feed_server.py`
- `app/components/IntegrationToggle.tsx`

The intended core stack is frontend, FastAPI backend, PostgreSQL, Redis, and an Audit Feed WebSocket. External integration profiles cover Unreal Engine, Blender, and Stripe CLI. GCP is an optional integration.

## 3. Integration Toggle Law

Environment/settings toggles are intended to control integration adapters:

- `ENABLE_UNREAL`
- `ENABLE_BLENDER`
- `ENABLE_STRIPE`
- `ENABLE_GCP`

Disabled integrations must fail closed rather than pretending to connect. The supplied examples specify a 403-style disabled response and explicit missing-credential errors.

Secrets must not be hardcoded or committed. Production/staging credentials are intended to use Docker secrets or an approved secure vault boundary.

## 4. Audit Feed Requirements

Integration actions should produce auditable events. The supplied example establishes an event shape containing fields such as:

- `event_type`
- `source`
- `provider`
- `severity`
- `timestamp`
- `hash`
- `prev_hash`
- `canonical`

The Audit Feed must support append-only behavior, hash-chain verification, idempotency, consumer/replay behavior, and real-time delivery where implemented.

## 5. Model Fabric Requirements

The AI layer is intended to provide:

1. Live model registry.
2. Provider-neutral adapters.
3. Local-first routing.
4. Capability evidence.
5. Actual GPU/VRAM detection.
6. Runtime/model discovery.
7. VRAM admission and fallback.
8. Model benchmarking/evaluation.

The capability registry remains an evidence-bearing decision layer rather than a decorative inventory. Runtime discovery and GPU/VRAM state must be measured rather than assumed.

## 6. Gabby Requirements

Gabby is specified as the operating/orchestration layer with:

- Chief-of-Staff behavior.
- Durable project memory.
- Fact/evidence enforcement.
- Human authorization gates.
- Task orchestration.
- Evidence storage and validation.

Gabby must not convert an intended action, generated response, or documentation statement into a verified fact without supporting evidence.

## 7. Docker Verification Sequence

The supplied execution sequence is:

1. Build and start the core Docker stack.
2. Check service health and integration toggles.
3. Test disabled integrations and capture expected fail-closed behavior.
4. Enable Unreal/Blender only with real credentials and a real reachable service.
5. Test Audit Feed WebSocket delivery.
6. Verify Docker service discovery.
7. Deploy to staging only after local verification passes.
8. Verify staging HTTPS, integration calls, and Audit Feed events.

The blueprint's example services include frontend on 3000, backend on 8000, Audit Feed on 3001, PostgreSQL on 5432, and Redis on 6379. These are target/example ports from the supplied source and are not runtime evidence by themselves.

## 8. Staging Requirements

The supplied staging architecture uses Docker Compose, Nginx, TLS/Certbot, Docker secrets, PostgreSQL, Redis, frontend, backend, and Audit Feed services.

Staging verification must establish actual HTTP success, actual integration behavior, and actual WebSocket delivery. A compose file or configuration alone does not establish deployment.

## 9. GCP Boundary

The source explicitly identifies the GCP adapter as **NOT_IMPLEMENTED / pending** in its honest status table. Therefore GCP must remain unimplemented/unverified unless repository inspection and runtime evidence establish otherwise.

A GCP toggle existing in configuration is not evidence that the adapter exists or that an upload has succeeded.

## 10. Source-Supplied Honest Status Baseline

The supplied blueprint records the following baseline:

| Component | Source status | Required evidence before promotion |
|---|---|---|
| Docker Unreal/Blender test | IMPLEMENTED / NOT_TESTED | Real Docker execution and real service/API response |
| Staging deployment | IMPLEMENTED / NOT_DEPLOYED | Actual staging deployment and health checks |
| GCP integration toggle | IMPLEMENTED / NOT_TESTED | Real GCP test with approved credentials |
| Audit Feed in staging | IMPLEMENTED / NOT_TESTED | Real-time event evidence |
| Unreal adapter | NOT_CONNECTED | Reachable Unreal service + authenticated test |
| Blender adapter | NOT_CONNECTED | Reachable Blender service + authenticated test |
| Stripe adapter | NOT_CONNECTED | Stripe CLI/webhook test evidence |
| GCP adapter | NOT_IMPLEMENTED | Actual implementation + tests |

These statuses are source-derived and must not be treated as current repository/runtime truth without inspection.

## 11. Required Repository Audit

Before adding further architecture, inspect the actual repository and produce a file manifest with:

- `EXISTING`
- `MODIFIED`
- `NEW`
- `MISSING`
- `DUPLICATE`
- `UNVERIFIED`

The audit should:

1. Find every referenced file that actually exists.
2. Find every referenced file that is missing.
3. Compare existing implementations against this source package.
4. Identify duplicate or overlapping systems.
5. Inspect Audit Feed implementation.
6. Inspect AI / Model Fabric implementation.
7. Inspect Docker integration code.
8. Inspect Unreal/Blender/Stripe/GCP adapters.
9. Inspect Gabby orchestration.
10. Inspect tests and migrations.
11. Run available verification.
12. Produce an evidence-backed status matrix.
13. Refuse to promote documentation-only claims to green.

## 12. Governing Principle

This record is intentionally a bridge between architecture and execution. It preserves the supplied upgrade plan while keeping the APEX evidence boundary intact:

**Specify it. Implement it. Test it. Verify it. Then promote it.**

No fake green.