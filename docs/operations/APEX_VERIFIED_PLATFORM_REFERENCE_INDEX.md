# APEX VERIFIED PLATFORM REFERENCE INDEX

**Purpose:** Reference-only inventory of external APEX-related platforms and project locations verified from connected account surfaces. This is evidence, not a claim that every listed app is production-ready.

**Verification law:** An entry may be marked `VERIFIED_EXISTENCE` only when the connected platform directly returned the project/account record. Runtime health, feature completeness, deployment health, or commercial readiness require separate evidence and are not implied.

## Verified connected platforms

| Platform | Evidence observed | Status | Scope |
|---|---|---|---|
| GitHub | `rahmaanherman-source/Apex-Hub` exists; also `apex-hub-production`, `APEX-Omni-Product-Studio`, `revenue-juggernaut` returned in the connected repository inventory | VERIFIED_EXISTENCE | Repository existence/access; contents require separate verification |
| Base44 | Connected account returned 16 app records, including `APEX BRIDGE`, `GODSPEED Bulk-Connect`, `Apex Godspeed`, `Apex identifier`, `Apex Breeze (Copy)`, `APEX Access Control Pro`, `Lyra`, `SETH (Copy)`, `Superagent`, `Vesper`, `FounderConnect`, `CryptoPulse AI (Copy)`, and `CODE GEN AI (Copy)` records | VERIFIED_EXISTENCE | App records exist in the connected Base44 account; individual runtime/capability status is not inferred |
| Replit | Connected account returned `Apex Sovereign Optimizer` | VERIFIED_EXISTENCE | Repl record exists; runtime status separately tested below |
| Notion | Connected search returned an APEX-related page titled `so we always remembere hjow to` with APEX ARCHITECT STATUS content | VERIFIED_EXISTENCE | Page existence/searchability |
| Jotform | Connected search returned `GODSPEED Intake – Bookmarks & Knowledge Ingestion` | VERIFIED_EXISTENCE | Form existence |
| Airtable | Connected account returned one base, `Untitled base` | VERIFIED_EXISTENCE | Base existence; contents not inferred |
| Vercel | Connected account returned team `rahmaanherman-source's projects`; project listing request failed | PARTIAL_VERIFICATION | Team existence verified; project existence not claimed from this check |

## Explicit non-green runtime evidence

### Replit — Apex Sovereign Optimizer

The supplied current Replit deployment screenshot shows the page rendering underlying application UI, but the Vite development overlay reports:

`[plugin:runtime-error-plugin] (unknown runtime error)`

Therefore the deployment is **NOT** marked runtime-green or production-ready. This is intentionally preserved as a failure state under APEX no-fake-green rules.

## Search surfaces with no matching APEX record in this check

- Canva: connected search returned no APEX design results.
- Linear: connected search returned no APEX results.

These are **NOT** marked absent from the user's accounts. They are only `NO_MATCH_IN_CURRENT_SEARCH`.

## Verification boundary

This index records what was directly observed through connected platform/account surfaces. It does not convert a project name, screenshot, AI statement, or historical mention into proof of implementation. Manual/documentation verification, runtime testing, feature testing, and production/commercial verification remain separate evidence classes.

## APEX no-fake-green rule

`EXISTS` != `WORKING` != `VERIFIED_CAPABILITY` != `PRODUCTION_READY`.

A manual or canonical reference may describe a capability only after the underlying capability has the evidence required by the applicable APEX verification standard.

## Current evidence date

2026-08-21
