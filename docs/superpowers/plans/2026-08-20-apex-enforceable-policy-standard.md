# APEX Enforceable Policy Standard Implementation Plan

> This plan records the approved canonical-law consolidation before promotion to the standalone APEX-Laws repository.

**Goal:** Add immutable policy/runtime separation, confidence, capability, evidence, platform-research, and enforcement rules to the staged APEX-Laws package without creating competing authorities.

**Architecture:** Keep `Apex-Hub/docs/canonical/` as the current staging source because the dedicated `APEX-Laws` repository does not yet exist. Add one focused enforceable-policy document, then update the canonical law bootstrap, index, and memory slab to reference the same rules. Runtime state remains outside canonical policy.

**Tech Stack:** Markdown/YAML/JSON documentation; GitHub canonical staging repository.

**Spec:** User-approved APEX Canonical Standard Addendum supplied in the conversation on 2026-08-20.

## Global Constraints

- Canonical policy and mutable runtime state must remain separate.
- Every verified claim/capability/registry entry must carry confidence and evidence metadata.
- Capability Registry must be checked before implementation decisions.
- Evidence hierarchy must distinguish official documentation, tests, telemetry, community reports, and inference.
- AI-generated output is never canonical evidence by itself.
- Research must precede production approval for platforms, SDKs, APIs, and tools.
- Preserve → Add → Integrate → Test → Verify → Compound.
- No fake green, no fabricated PASS, no fabricated parity percentages.
- The standalone `APEX-Laws` repository remains the canonical destination; `Apex-Hub/docs/canonical/` is staging until that repository exists.

### Task 1: Add the enforceable policy standard

**Files:**
- Create: `docs/canonical/APEX_ENFORCEABLE_POLICY_STANDARD.md`

- [ ] Add immutable-policy/runtime separation.
- [ ] Add confidence schema and allowed values.
- [ ] Add Capability Registry schema and deterministic decision flow.
- [ ] Add Evidence Hierarchy and conflict handling.
- [ ] Add Platform Registry requirements.
- [ ] Add Research Pipeline and AI research rule.
- [ ] Add enforcement requirements and non-fabrication rules.

### Task 2: Bind the policy into the canonical law bootstrap

**Files:**
- Modify: `docs/canonical/APEX_LAWS_REPOSITORY_BOOTSTRAP.md`

- [ ] Add the new policy standard as binding law.
- [ ] Add the canonical execution gate: research → evidence → confidence → capability check → reuse/integrate/partner/build → verify.
- [ ] Preserve all existing law sections.

### Task 3: Update canonical memory

**Files:**
- Modify: `docs/canonical/APEX_CANONICAL_MEMORY_SLAB.md`

- [ ] Record durable recall rules for policy/runtime separation.
- [ ] Record confidence/evidence requirements.
- [ ] Record capability-registry-first decision making.
- [ ] Record research-before-approval and AI-output non-authority.
- [ ] Keep mutable runtime data out of the memory slab.

### Task 4: Update the law index

**Files:**
- Modify: `docs/canonical/APEX_LAWS_INDEX.md`

- [ ] Add the enforceable policy document to binding documents.
- [ ] Keep the standalone APEX-Laws promotion rule explicit.

### Task 5: Verification

- [ ] Re-read every changed file.
- [ ] Confirm no duplicate or contradictory authority was introduced.
- [ ] Confirm no runtime state was inserted into canonical policy.
- [ ] Confirm no unsupported PASS/status values were added.
- [ ] Confirm the staged package still points to `APEX-Laws` as the canonical destination.
