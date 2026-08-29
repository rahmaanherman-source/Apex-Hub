# APEX/GABBY VISUAL REFERENCE — 2026-08-29

## Source

This document records the user-provided screenshot captured on August 29, 2026 as the source reference for the current UI regression: primary workspace content extends beyond the visible viewport and is being clipped instead of remaining reachable.

**Captured image:** 1080 × 1440 px.

The original uploaded photo is retained in the conversation source. This repository also contains a machine-readable engineering/cartography representation at:

`assets/canonical/gabby/apex-workspace-reference-2026-08-29.svg`

## What the reference establishes

- The workspace contains multiple content cards/items that may extend beyond the current viewport.
- The user requires access to the complete collection, not only the cards currently visible.
- Left/right content must remain present and reachable by horizontal scroll/swipe or equivalent navigation.
- The interface must not crop or shorten the collection to make the layout fit.
- The complete workspace needs an explicit Whole Picture / Overview path.
- Gabby remains a single assistant/runtime and must not be duplicated to solve layout problems.
- The Gabby orb must remain usable without blocking the primary work surface.

## Engineering interpretation

This screenshot is **defect evidence**, not a license to copy the current clipped state as the final design. The target implementation preserves the complete information architecture while making every region reachable and usable.

## Regression statement

**FAIL:** content exists outside the viewport but cannot be reached, or is removed/cropped to fit.

**PASS:** all primary content remains in the DOM/application model, is reachable by horizontal/vertical navigation as appropriate, and Whole Picture/Overview exposes the complete workspace.
