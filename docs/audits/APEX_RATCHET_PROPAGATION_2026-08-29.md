# APEX UI REGRESSION RATCHET — PROPAGATION RECORD

**Date:** 2026-08-29
**Status:** LOCKED / ACTIVE

## What changed

The owner established a permanent APEX rule:

> **A freeze/watermark/reference marker is a floor. Once a UI or system state is marked approved and verified, future work may go higher but may not go lower.**

This is a regression ratchet. It is not a suggestion, design preference, or historical note.

## Rule

```text
APPROVED / VERIFIED
        ↓
   WATERMARK / MARK
        ↓
      FLOOR
        ↓
EQUAL OR BETTER ONLY
        ↓
NEW APPROVED FLOOR
```

A newer commit does not automatically move the floor. A redesign does not automatically move the floor. A successful build does not automatically move the floor.

## Protected examples

For Gabby/APEX UI, a baseline can protect:

- canonical cosmic Gabby Orb/avatar
- established navigation and workspace tabs
- layout hierarchy
- viewport composition
- control placement and scale
- voice/microphone/chat/command surfaces
- animations and state behavior
- responsive behavior
- existing working functionality
- visual quality and information density

The current screenshot regression is therefore treated as a **regression candidate** because the established navigation disappeared/reduced and secondary brown/orange controls became disproportionately large and intrusive. Exact source-code cause still requires implementation-level comparison.

## Required response

```text
DETECT
→ STOP
→ IDENTIFY BASELINE
→ COMPARE
→ FIND ROOT CAUSE
→ RESTORE IF BELOW FLOOR
→ VERIFY
→ APPROVE UPGRADE ONLY IF EQUAL/BETTER
→ RECORD NEW BASELINE
```

## Propagation

The ratchet reference was added to these APEX repositories in this session:

- `Apex-Hub`
- `Apex-Gabby-`
- `APEX-TERMINAL`
- `Apex-Sentinel`
- `Apex-Omni-Vault`
- `Apex-Bridge`
- `Apex-Concierge`
- `Apex-OAuth-Wizard`
- `APEX-Omni-Product-Studio`
- `Apex-Heritage-`
- `Apex-Phoenix-`
- `Apex-Steward-`
- `APEX-Lifecycle-V1`
- `apex-ecosystem-portal`
- `Apex-Forensic-Vision`
- `Truth-Gate-`
- `GABBY-CORE-STEWARD`
- `Apex-Studio-OS-`

## Existing same-day UI law

The repository audit also found same-day commits titled `LOCK: APEX UI change control law` across the APEX estate. This confirms the ratchet extends an already-established protection mechanism rather than inventing an unrelated governance concept.

## Standalone governance repository

The intended canonical home remains:

`apex-integrated-rule`

Repository search found no existing repository with that name. The available GitHub integration in this session does not expose a repository-creation operation, so no false claim is made that the standalone repository exists.

An APEX Hub issue records this remaining infrastructure action: issue #15, `CREATE: standalone apex-integrated-rule governance repository`.

## Final law

> **THE MARK IS THE FLOOR.**
>
> **If APEX froze it, approved it, or watermarked it as an accepted baseline, nothing may silently take the system below that mark. We can improve it. We can replace it only with an equal-or-better verified successor. We do not downgrade.**

**GODSPEED.**
