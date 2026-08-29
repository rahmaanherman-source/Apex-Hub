# APEX UI REGRESSION RATCHET LAW

**STATUS: LOCKED — APEX-WIDE GOVERNANCE**

## Purpose

A frozen, approved, verified UI or interaction state is a **minimum acceptable baseline**, not merely a historical snapshot.

A freeze/watermark/reference marker means:

> **THIS VERSION WAS ACCEPTED. THIS IS THE FLOOR.**

Future work may move the system **upward** (equal or better), but may not move it **downward** without an explicit owner-approved superseding baseline.

## The Ratchet Rule

```text
APPROVED / VERIFIED BASELINE
            ↓
          FLOOR
            ↓
   EQUAL OR BETTER ONLY
            ↓
       NEW BASELINE
```

There is no silent downgrade path.

A newer commit is **not** automatically a better baseline. A redesign is **not** automatically an upgrade. A successful build is **not** proof that a UI remains acceptable.

## What a Baseline Protects

A frozen/watermarked baseline may protect any owner-approved material characteristic, including:

- Gabby identity and canonical orb
- avatar assets and quality
- navigation and workspace doors
- layout hierarchy
- viewport composition
- control placement and scale
- typography
- colors and materials
- animation/state behavior
- interaction models
- voice/microphone surfaces
- chat/command surfaces
- accessibility behavior
- responsive behavior
- existing working functionality
- visual density and information hierarchy

## Regression Definition

A regression exists when a proposed or shipped change causes the system to become materially weaker, less usable, less complete, less truthful, less accessible, less functional, or visually inferior to the approved baseline.

Examples include:

- removing established navigation
- replacing a real capability with a mock
- replacing the canonical Gabby orb with a weaker icon
- shrinking or obscuring Gabby to solve another layout problem
- enlarging secondary controls until they dominate the workspace
- deleting working controls to simplify a viewport
- introducing clipping, overflow, drift, collapse, bounce, or unintended movement
- losing voice, chat, routing, or workspace functionality
- silently changing a frozen visual contract

## Restore Rule

When a regression is detected:

1. STOP the change.
2. Identify the protected baseline.
3. Compare current behavior against the baseline.
4. Identify the exact regression and root cause.
5. Restore the last known-good baseline when the proposed change is not demonstrably equal or better.
6. Only then resume improvement work.

Do not redesign around a regression.

## Superseding a Baseline

A baseline can only move upward through an explicit owner-approved change.

The new version must:

- identify the previous baseline
- document the intended improvement
- demonstrate no material loss
- pass functional verification
- pass visual comparison
- pass interaction checks
- receive explicit approval
- be versioned as the new baseline

Then and only then:

```text
OLD FLOOR → APPROVED UPGRADE → NEW FLOOR
```

The old baseline remains historically recoverable.

## Evidence Rule

A watermark/marker is evidence of an approved reference state. It is not a claim that every runtime deployment currently matches it.

Therefore distinguish:

```text
BASELINE APPROVED
BASELINE IMPLEMENTED
BASELINE DEPLOYED
BASELINE LIVE
BASELINE VERIFIED
```

Never collapse these states into one status.

## APEX-Wide Scope

This law applies across APEX, including but not limited to:

- APEX Hub
- APEX Terminal
- Gabby
- Sentinel
- Vault / Gatekeeper
- Bridge / integration infrastructure
- 360 / W360
- Social
- Commerce
- Concierge
- Product Studio
- future APEX workspaces

It is governance, not an application feature.

## Canonical Build Loop

```text
INPUT
→ EVALUATE
→ MAP
→ GAP CHECK
→ REUSE
→ UPGRADE
→ BUILD
→ VERIFY
→ INTEGRATE
```

For visual/runtime changes:

```text
REFERENCE
→ CONTRACT
→ IMPLEMENTATION
→ VISUAL COMPARISON
→ APPROVAL
→ FREEZE / WATERMARK
→ INTERACTION CHECK
→ RUNTIME TRUTH
→ TESTS
→ RELEASE
```

## Hard Rule

> **A freeze is a floor, not a ceiling.**
>
> **Once APEX marks something as approved and verified, nothing may silently take the system below that mark. We can go higher. We cannot go lower.**

**GODSPEED.**
