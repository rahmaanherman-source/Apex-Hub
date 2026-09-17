# APEX Memory Codex

**Status:** CANONICAL ARCHITECTURE SPECIFICATION
**Version:** 1.0.0
**Purpose:** Truth-anchored memory, task-state integrity, hallucination mitigation, and auditable self-correction for the APEX ecosystem.

## Core Law

> Remember what is verified. Distinguish evidence from inference. Never mistake confidence for truth. Never report an untested operation as working. Never silently overwrite history. When uncertain, stop guessing and obtain evidence.

## 1. Architecture

```text
USER INPUT
    ↓
APEX GATEKEEPER
intent / permissions / task ID / deduplication
    ↓
STATE-MACHINE LEDGER
NEW → AUTHORIZED → RUNNING → VALIDATING → VERIFIED → LOCKED
                         ↘ BLOCKED / FAILED / REVIEW
    ↓
CONTEXT ROUTER
Truth Slab + Project Memory + Current State + Authorized Live Sources
    ↓
COGNITIVE ENGINE
local model / cloud model / research / coding
    ↓
VALIDATION ENGINE
provenance + contradiction checks + deterministic tests + semantic relevance + uncertainty
    ↓
PASS?
 ├─ YES → OUTPUT + EVIDENCE → AUDIT LOG
 └─ NO  → REFLECT / RESEARCH / REVALIDATE
    ↓
MEMORY CONSOLIDATOR
promote / retain / archive / review
```

## 2. Truth Slab

The Truth Slab is the durable source of verified facts. A similarity score is a relevance signal, **not proof of truth**.

```json
{
  "id": "FACT_000001",
  "status": "VERIFIED",
  "content": "Example verified fact",
  "source": {
    "type": "user|document|api|web|test",
    "reference": "SOURCE_ID"
  },
  "verified_by": "human|system|external_source",
  "verified_at": "ISO8601",
  "supersedes": null,
  "confidence": 1.0,
  "immutable": true,
  "hash": "SHA256..."
}
```

### Truth rules

- `VERIFIED` requires evidence/provenance.
- `SUPPORTED` means evidence exists but verification is incomplete.
- `UNCERTAIN` means evidence is insufficient.
- `CONTRADICTED` means credible evidence conflicts with the claim.
- Verified facts are immutable; corrections create a new event/version and preserve history.
- Vector similarity can retrieve relevant facts but cannot independently establish truth.

## 3. State-Machine Ledger

Every meaningful operation receives a unique `task_id`.

```text
NEW
 ↓
AUTHORIZED
 ↓
RUNNING
 ↓
VALIDATING
 ├──→ BLOCKED
 ├──→ FAILED
 ├──→ REVIEW
 └──→ VERIFIED
          ↓
        LOCKED
```

If a task is already `VERIFIED` or `LOCKED` and the requested operation is materially identical, retrieve the recorded result instead of repeating the work. Explicit re-verification creates a new verification event.

## 4. No-Fake-Green Gate

```text
GREEN  = independently verified
YELLOW = partially verified / evidence incomplete
RED    = failed / contradicted / unavailable
GRAY   = not tested
```

Never derive GREEN from an AI-generated assertion alone.

Examples:

```text
Button exists                  ≠ Button works
Local operation works          ≠ Production operation works
API returned 200                ≠ Business operation succeeded
UI says complete                ≠ External system confirmed completion
```

## 5. Validation Contract

```json
{
  "task_id": "APEX-12345",
  "operation": "OPERATION_NAME",
  "requested": true,
  "executed": true,
  "tests": {
    "api": "PASS",
    "database": "PASS",
    "webhook": "PASS",
    "ui": "PASS",
    "external_confirmation": "PASS"
  },
  "result": "VERIFIED",
  "evidence": ["TEST_ID", "EVENT_ID", "EXTERNAL_ID"],
  "timestamp": "ISO8601"
}
```

Missing required external confirmation must not be represented as fully verified when the operation depends on an external system.

## 6. Hallucination Defense

Use multiple independent signals:

1. Authoritative evidence exists.
2. Claim does not contradict locked facts.
3. Provenance supports the claim.
4. Deterministic validation passes where applicable.
5. Semantic relevance is sufficient.
6. Uncertainty is acceptable.

A Shannon entropy signal, cosine similarity score, or model confidence value is **not a standalone truth oracle**.

## 7. Memory Hierarchy

```text
L0 — CURRENT TURN       temporary conversation state
L1 — WORKING MEMORY     active task/project context
L2 — PROJECT MEMORY     durable project notes
L3 — TRUTH SLAB         verified facts + provenance
L4 — AUDIT LEDGER       immutable historical events
L5 — ARCHIVE            long-term source material
```

Never automatically promote L0 directly into L3. Promotion follows:

```text
Candidate Fact → Evidence → Validation → Verification → Truth Slab
```

## 8. Consolidation

Nightly/background maintenance must preserve recoverability.

```text
RAW EVENTS
    ↓
DEDUPLICATE
    ↓
CLASSIFY
    ↓
CONTRADICTION DETECTION
    ↓
RETENTION ANALYSIS
    ↓
ARCHIVE LOW-VALUE DATA
    ↓
PROPOSE NEW FACTS
    ↓
VERIFY
    ↓
PROMOTE VERIFIED FACTS
```

**Archive is not Delete.** Historical evidence remains recoverable.

## 9. Master Processing Algorithm

```pseudo
PROCESS(query):
    task = IDENTIFY_TASK(query)
    state = SML.lookup(task.id)

    IF state == LOCKED AND request_is_same_operation(query):
        RETURN verified_result(task.id)

    context = ROUTER.collect(
        TruthSlab,
        ProjectMemory,
        CurrentState,
        AuthorizedExternalSources
    )

    evidence = RETRIEVE_EVIDENCE(query, context)
    draft = GENERATE(query, evidence)

    validation = VALIDATE(
        draft,
        authoritative_evidence,
        TruthSlab,
        deterministic_tests,
        contradiction_rules,
        relevance_signal,
        uncertainty_signal
    )

    IF validation == VERIFIED:
        RECORD_AUDIT_EVENT()
        UPDATE_SML(VERIFIED)
        RETURN draft + evidence

    IF validation == UNCERTAIN:
        RESEARCH()
        REVALIDATE()

    IF validation == CONTRADICTED:
        STOP()
        FLAG_FOR_REVIEW()

    IF validation == FAILED:
        RECORD_FAILURE()
        RETURN failure_state
```

## 10. Controlled Self-Correction

The system may propose improvements, but foundational rules, security policies, Truth Slab records, credentials, and production code must not be silently modified by an autonomous critic.

```text
AI PROPOSES
    ↓
TEST
    ↓
VERIFY
    ↓
AUTHORIZED GATE
    ↓
COMMIT
    ↓
AUDIT
```

This provides self-correction without uncontrolled self-modification.

## 11. APEX Reliability Requirements

- Every production action has an observable state.
- Every important result has evidence.
- Every external integration has an explicit success criterion.
- Failed tests remain visible.
- Contradictions become review items rather than being silently reconciled.
- Historical state is append-only/auditable.
- Credentials never belong in model memory or source-controlled Truth Slab content.
- Provider integrations remain replaceable implementation tools unless explicitly designated otherwise.
- No placeholder, simulated, or mocked behavior may be represented as production functionality.

## 12. Definition of Done

An APEX feature is not DONE because code was generated. It is DONE only when:

```text
IMPLEMENTED
   +
UNIT TESTED
   +
INTEGRATION TESTED
   +
UI/E2E TESTED where applicable
   +
EXTERNAL SYSTEM VERIFIED where applicable
   +
AUDIT EVIDENCE RECORDED
   =
VERIFIED
```

Otherwise the system reports the actual state: `INCOMPLETE`, `BLOCKED`, `FAILED`, `REVIEW`, or `NOT_VERIFIED`.
