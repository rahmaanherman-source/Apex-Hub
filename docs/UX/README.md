# APEX UX — Canonical Index

**Canonical source:** `docs/UX/APEX_ECOSYSTEM_MARKET_BENCHMARK.md`

This directory is the canonical entry point for APEX consumer UX architecture.

## Inheritance chain

`APEX Ecosystem Doctrine` → `App UX Contract` → `Implementation` → `Verification`

### App contracts

- Flora Plug → `Flora-plug/docs/UX/DYNAMIC_REASONABLE_DENSITY.md`
- Apex Creator → `Apex-365/docs/UX/APEX_CREATOR_DENSITY.md`

## Shared rules

1. Adaptive density; no arbitrary global card-count ceiling.
2. First fold prioritizes current context and one primary action.
3. Extended content uses progressive disclosure and horizontal shelves where appropriate.
4. Real data only in production.
5. Design specification is not implementation verification.
6. A feature becomes VERIFIED only after evidence-based testing.

## Status vocabulary

Use only:
- SPEC
- IN_PROGRESS
- VERIFIED
- BLOCKED
- NOT_CONFIGURED

Do not use "100% operational" as a substitute for feature-level evidence.

## Maintenance

When a new APEX app is created:
1. Copy the UX contract template.
2. Define its first-fold context.
3. Define its extended deck.
4. Define its primary trigger.
5. Link the app contract back to this doctrine.
6. Track implementation status separately from design intent.
