# APEX ENGINEERING AGENT LAW

Before modifying any APEX/Gabby UI, read:

1. `docs/canonical/APEX_GABBY_VISUAL_ENGINEERING_CONTRACT.md`
2. `docs/canonical/APEX_GABBY_VISUAL_CARTOGRAPHY.json`
3. `docs/canonical/APEX_GABBY_VISUAL_REFERENCE.md`
4. `docs/canonical/APEX_GLOBAL_REPAIR_FAILSAFE.md` when the work involves troubleshooting, repair, audit, recovery, or guided fixes.

## Mandatory behavior

- Treat canonical UI requirements as law, not suggestions.
- Inspect existing implementation before creating replacements.
- Never crop, shorten, delete, or hide primary content merely to fit a viewport.
- Preserve complete horizontal collections; users must be able to scroll/swipe left and right.
- Provide an explicit Whole Picture / Overview path for complete workspace visibility.
- Maintain exactly one Gabby runtime, one conversation, one voice, one command system, and one canonical orb.
- Keep Gabby from obstructing primary work.
- Preserve existing working capabilities during UI upgrades.
- For repair flows, preserve the user's investigation checkpoint, show the current repair step, keep the next step ready, provide STOP / CONTINUE / CONTACT GABBY controls, and use the global 60-second observation-window protocol unless the repair requires a different duration.
- Never silently mutate the repository when a repair timer expires.
- Do not report a fix until source, build, runtime, interaction, and relevant visual behavior have been verified.
- A screenshot or successful edit is not sufficient proof of runtime correctness.
- Publish is only successful after a real deployed runtime can be opened and exercised.

## Required verification loop

`INSPECT → CHANGE → BUILD → TEST → RUN → INTERACT → VISUAL-CHECK → EVIDENCE → REPORT`

If the implementation differs from the canonical reference, fix the implementation or explicitly document an authorized deviation. Do not silently simplify the design.


## Canonical Gabby identity and Shopify commerce co-host

The owner-approved Gabby visual identity is canonical. Read:
- `docs/canonical/GABBY_CANONICAL_VISUAL_IDENTITY_2026-09-12.md`
- `skills/GABBY_SHOPIFY_SIDEKICK_CAPABILITIES.md`
- `docs/canonical/APEX_LIFE_GLOBAL_GABBY_COMMERCE_COHOST.md`

Gabby is the single APEX AI co-host/operator identity. Shopify Sidekick is a capability source/integration, not a second assistant or visual identity.

Do not substitute the Shopify Sidekick mascot, a generic chatbot icon, or another generated avatar for Gabby.

Gabby may be used as the APEX Life Global commerce co-host for contextual product spotlights, product education, comparisons, new-arrival presentations, and shopping segments. Use real Shopify product data and real product destinations. Never fabricate prices, inventory, discounts, ratings, specifications, analytics, or completed actions.

For Shopify capabilities, implement only what the connected account, API, extension, permissions, and runtime actually support. Maintain the truth boundary and verification loop.