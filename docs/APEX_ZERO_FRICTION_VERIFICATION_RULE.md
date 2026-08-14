# APEX Zero-Friction Verification Rule

**Owner / Architect:** Rahmaan Manzar Herman / APEX Global LLC  
**System:** APEX Hub / Gabby / Truth Gate  
**Status:** Canonical design rule  
**Date:** 2026-08-14

## Purpose

APEX must not create unnecessary verification loops for a user who is already inside an authenticated, authorized APEX session.

The system should move from **state → action → result** in one surface whenever the required evidence is already available.

## Core Rule

> **If APEX already possesses sufficient current evidence to verify the requested state, verify it in place. Do not send the user somewhere else merely to rediscover the same problem.**

A status such as `UNVERIFIED` must be actionable from the same screen.

The user should be able to press **VERIFY NOW** (or the context-appropriate action), receive the actual result, and—when the result identifies a fixable issue—be given the direct next action or direct path to fix it.

## No Verification Loops

APEX must avoid this pattern:

`UNVERIFIED → external page → same diagnostic → return to APEX → external page → fix`

Prefer:

`UNVERIFIED → VERIFY NOW → precise result → FIX / RETRY / DONE`

If an external provider is genuinely required for the fix, APEX should open the exact relevant provider action, preserve context, and return the user to the same APEX state after completion when technically possible.

## Verification vs. Authorization

These are different states and must not be conflated:

- **Authenticated:** the current session/user identity is established.
- **Authorized:** the identity has permission to perform the requested operation.
- **Verified:** APEX has current evidence that the specific claim or capability is true.
- **Healthy:** the connected capability is functioning as expected.
- **Executable:** the requested action can actually run now.

A user being authenticated does not automatically make every external capability verified. But if APEX already has sufficient evidence for the specific check, it must not make the user repeat authentication or navigate elsewhere unnecessarily.

## One-Button Principle

For every actionable state, the UI should expose the shortest valid action:

| State | Preferred action |
|---|---|
| `UNVERIFIED` | `VERIFY NOW` |
| `VERIFIED` | `OPEN / USE / RUN` |
| `AUTH_REQUIRED` | `SIGN IN / AUTHORIZE` |
| `BLOCKED` | `FIX NOW` |
| `ERROR` | `RETRY` or precise `FIX NOW` |
| `EXPIRED` | `RE-AUTHORIZE` or `ROTATE` |
| `HEALTH_DEGRADED` | `DIAGNOSE` / `REPAIR` |

Do not make a user navigate to a generic settings page when the system can identify the specific setting or dependency that must change.

## Truth Gate Still Applies

Zero-friction does **not** mean fake verification.

APEX must never turn `UNVERIFIED` into `VERIFIED` merely because the user pressed a button.

The button must execute a real check or retrieve current trusted evidence.

The result must be explicit:

- `VERIFIED`
- `NOT VERIFIED`
- `AUTHORIZED BUT UNTESTED`
- `BLOCKED`
- `ERROR`
- `EXPIRED`

The UI must show the reason when verification fails.

## Identity / Biometric Session

If the APEX application already has a current identity session established through an approved authentication mechanism (including platform biometric/passkey authentication where actually implemented), reuse that current session evidence rather than asking the user to authenticate again for the same session.

Do **not** claim biometric verification merely because a device is unlocked or because a browser/session exists. Biometric/passkey verification must be backed by the actual authentication mechanism and its server-verifiable result.

## Direct Diagnosis

Every failed verification should answer three questions in the same surface:

1. **What failed?**
2. **Why did it fail?**
3. **What exact action fixes it?**

Avoid generic messages such as `Go to settings` when a more precise instruction is available.

## Real-Time Requirement

Where a provider supports live health/status checks, APEX should display current evidence rather than stale labels.

The following visualizations may be used when real telemetry exists:

- GPU thermal plot
- model latency chart
- request/response health
- connector health
- queue depth
- error rate
- resource utilization

Never render synthetic telemetry as if it were real.

## Terminal Integration

The APEX Terminal and dashboard must share the same state model.

A verification initiated from either surface should update the same underlying status rather than creating two independent diagnostics.

Preferred flow:

`Dashboard → VERIFY NOW → Truth Gate → live check → shared state → Dashboard + Terminal updated`

or

`Terminal → verify command → Truth Gate → live check → shared state → Dashboard updated`

## UX Principle

> **NO EXTRA STEPS. NO DEAD-END STATUS. NO GENERIC REDIRECTS. NO FAKE GREEN.**

The system should be as direct as the evidence allows.

## Acceptance Tests

A build satisfies this rule only if:

1. An `UNVERIFIED` item has a direct in-place verification action.
2. The action performs a real check or retrieves trusted current evidence.
3. A successful check changes the shared state to `VERIFIED`.
4. A failed check explains the exact failure.
5. A fixable failure exposes a direct fix/retry action when technically possible.
6. The user is not sent through a redundant external loop.
7. Existing authenticated session evidence is reused when valid.
8. Biometric/passkey claims are only made when backed by the actual authentication mechanism.
9. Dashboard and Terminal use the same verification state.
10. No synthetic telemetry is presented as live data.

## APEX Law

**Flow over noise. Evidence over ceremony. One action when one action is sufficient.**
