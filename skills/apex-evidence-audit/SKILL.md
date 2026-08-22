---
name: apex-evidence-audit
description: Audit APEX claims, capabilities, artifacts, and verification statuses against reproducible evidence. Use whenever a system is reported as configured, connected, approved, or verified, or when fake-green risk must be checked.
metadata:
  apex_id: APEX-SKILL-002
  version: "1.0"
  status: candidate
  evidence_level: official
  owner: APEX
  registry: capability-registry
---
# APEX Evidence Audit

Never infer verification from configuration, UI badges, code presence, or a registry label. Establish the claim, identify the required test, execute or inspect the test evidence, and return the strongest status supported by evidence.

## Required result
- `status`: UNKNOWN, CONFIGURED, CONNECTED, TESTED, APPROVED, VERIFIED, FAILED
- `claim`
- `evidence_refs`
- `tests_run`
- `limitations`

`VERIFIED` requires reproducible evidence tied to the exact capability/version and a successful test. Missing or synthetic evidence fails closed.

## Boundaries
- Never create evidence merely to satisfy a status.
- Never return secrets or raw credentials.
- Treat AI-generated claims as unverified until independently supported.
