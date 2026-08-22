# APEX LAW — EXECUTION BOUNDARY

This file is the executable-law anchor for the verification layer. It does not replace the canonical law documents under `docs/canonical/`.

## Non-negotiable rules

1. **No fake green.** A registry label, UI indicator, code presence, or AI-generated statement is not proof.
2. **Research before approval.** Capabilities are researched and evidence-linked before governance approval.
3. **Runtime and governance are separate.** Operational health is `UNKNOWN | CONFIGURED | CONNECTED | FAILED`; governance is `RESEARCHED | CANDIDATE | TESTED | APPROVED | VERIFIED | REJECTED`.
4. **Verification requires evidence.** A `VERIFIED` claim requires a reproducible runtime test, persisted raw evidence, and a hash-linked Verification Evidence Object (VEO).
5. **Runtime cannot grant governance approval.** The verification engine may record `TESTED`; it must not silently promote `APPROVED` or `VERIFIED`.
6. **Real execution only.** Network and process adapters perform actual I/O with timeout and error handling. Synthetic responses are prohibited.
7. **Golden World is deterministic.** Canonical files are explicitly manifested, sorted, hashed with SHA-256, and checked for drift.
8. **Secrets stay out of evidence.** Credentials, private keys, and raw secrets must never be written to evidence artifacts.
9. **Preserve working architecture.** Hardening extends the existing APEX Hub rather than creating a parallel replacement system.

## Truth Gate

The Truth Gate fails closed when the required governance status or evidence cannot be resolved. Evidence must be independently retrievable from the repository/runtime evidence layer.
