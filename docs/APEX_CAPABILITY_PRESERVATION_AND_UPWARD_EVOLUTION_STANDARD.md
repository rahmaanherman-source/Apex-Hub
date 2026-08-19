# APEX Capability Preservation & Upward Evolution Standard

**Status:** CANONICAL
**Scope:** APEX Hub, Gabby, Command Center, Terminal, mobile surfaces, AI Studio builds, and all future APEX UI/UX iterations
**Rule:** NEVER GO DOWN. ONLY GO UP.

## 1. Core Law

An improvement is never permission to remove an existing working capability.

Every new version must preserve the capabilities of the previous verified version while adding, improving, or integrating new capabilities.

> **We do not trade capability for capability. We compound capability.**

A feature is not an improvement if it causes a verified existing capability to disappear, become inaccessible, or regress without an explicitly approved architectural decision.

## 2. Evolution Model

The required evolution path is:

```text
CURRENT VERIFIED SYSTEM
        ↓
PRESERVE WHAT WORKS
        ↓
ADD THE NEW CAPABILITY
        ↓
INTEGRATE
        ↓
TEST OLD + NEW
        ↓
VERIFY
        ↓
UPWARD RELEASE
```

The prohibited pattern is:

```text
CURRENT SYSTEM
        ↓
ADD FEATURE
        ↓
SILENTLY REMOVE EXISTING CAPABILITY
        ↓
CALL THE RESULT "BETTER"
```

That is a **regression**, not an improvement.

## 3. UI Shell Preservation

The APEX shell is an operating surface, not decorative UI.

Where a verified implementation contains these capabilities, they must remain available in subsequent versions unless an intentional architecture change is explicitly approved and verified:

- Left command/navigation sidebar
- Right Gabby/Concierge sidebar where present
- Collapse controls
- Reopen/expand controls
- Icon-rail or equivalent compact navigation state
- Primary navigation
- Secondary navigation
- Active workspace
- Contextual controls
- Workspace state preservation
- Responsive navigation behavior
- Direct access to existing commands and modules

### Required behavior

A user must be able to:

1. Open the application.
2. Access the command/navigation system.
3. Collapse a sidebar/panel when supported by the shell.
4. Work with the expanded workspace.
5. Reopen/expand the navigation or panel.
6. Retain the active workspace and relevant state.
7. Reach the same previously verified capabilities.

If an existing sidebar disappears merely because a new feature was added, the build fails regression review.

## 4. Responsive Preservation

Responsive behavior must transform an existing capability rather than delete it.

Examples:

- Desktop sidebar → compact rail → mobile drawer.
- Right-side Gabby surface → responsive panel/drawer.
- Workspace navigation → mobile navigation control.

Responsive layout is not permission to erase the navigation hierarchy.

## 5. Capability Preservation Ledger

Every meaningful UI/build iteration should maintain a capability-preservation checklist.

```text
VERSION N
  ├── Capability A ✅
  ├── Capability B ✅
  ├── Capability C ✅
  └── Capability D ✅
          ↓
      NEW BUILD
          ↓
  ├── A preserved ✅
  ├── B preserved ✅
  ├── C preserved ✅
  ├── D preserved ✅
  ├── New E added ✅
  └── New F added ✅
          ↓
      REGRESSION TEST
          ↓
        VERIFIED
```

If any previously verified capability becomes unavailable, the build cannot receive a GREEN/VERIFIED release state until the capability is restored or an explicit architecture decision authorizes the change.

## 6. Regression Is a Truth-Gate Failure

APEX uses the existing **No Fake Green** principle here.

A build that adds functionality but removes working functionality is not GREEN merely because the new feature works.

Required status:

- **VERIFIED:** previous capabilities preserved + new capabilities verified.
- **PARTIAL:** new capability works, but preservation is not fully verified.
- **REGRESSION:** previously verified capability was removed or broken.
- **UNVERIFIED:** behavior has not been tested with evidence.

## 7. Acceptance Test

Before release, test both the new capability and the preserved capability set.

```text
OLD CAPABILITY INVENTORY
        ↓
NEW BUILD
        ↓
OLD CAPABILITY TESTS
        ↓
NEW CAPABILITY TESTS
        ↓
INTEGRATION TEST
        ↓
READ-BACK / OBSERVABLE EVIDENCE
        ↓
VERIFIED
```

A successful new feature test does **not** substitute for regression testing.

## 8. AI Builder / AI Studio Rule

AI-generated implementations must treat the existing application as the baseline.

The builder must:

1. Inspect the existing implementation before changing it.
2. Identify existing user-visible capabilities.
3. Preserve existing navigation and controls.
4. Add the requested functionality without destructive replacement.
5. Test the old capabilities after modification.
6. Test the new functionality.
7. Report any intentional breaking change explicitly.

The instruction **"improve"** means improve the existing system—not replace working capabilities with a smaller or less capable version.

## 9. Explicit Change Exception

A capability may be removed only when all of the following are true:

- The removal is intentional.
- The architectural reason is documented.
- The replacement capability is identified, if applicable.
- The impact is known.
- Regression implications are tested.
- The change is explicitly approved through the appropriate APEX change-control process.

Silent loss is never an acceptable change mechanism.

## 10. Canonical APEX Principle

> **PRESERVE → ADD → INTEGRATE → TEST → VERIFY → COMPOUND.**

Never:

> **REMOVE → REPLACE → ASSUME.**

APEX evolves by accumulation of verified capability.

**NEVER GO DOWN. ONLY GO UP.**
