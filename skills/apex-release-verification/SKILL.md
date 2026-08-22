---
name: apex-release-verification
description: Verify release artifacts, manifests, tests, evidence, and integrity before deployment or publication.
metadata:
  apex_id: APEX-SKILL-011
  version: "1.0"
  status: candidate
---
# APEX Release Verification

Hash release artifacts, create a deterministic manifest, run installation or execution checks, verify the integrity chain, and record evidence. Signing requires a runtime secret; unsigned artifacts must not be represented as signed.
