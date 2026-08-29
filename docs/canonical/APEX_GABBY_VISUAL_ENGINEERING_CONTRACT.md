# APEX/GABBY WHOLE-WORKSPACE VISUAL & NAVIGATION CONTRACT

**Status: CANONICAL — MUST BE OBEYED**

## Purpose

The canonical APEX/Gabby interface must preserve the complete workspace. A viewport is not permission to remove, crop, shorten, hide, or silently redesign content that exists outside the current frame.

## Non-negotiable rules

1. **NO CLIPPED PRIMARY CONTENT.** If the canonical composition is wider than the viewport, the user must be able to move through it with horizontal scrolling/swiping, panel collapse/expand, or an equivalent discoverable navigation mechanism.
2. **LEFT ↔ RIGHT IS FIRST-CLASS NAVIGATION.** Content that exists to the left or right of the viewport remains present and reachable. Never delete or shorten it merely to make a screenshot fit.
3. **WHOLE PICTURE VIEW.** Provide an explicit Overview/Whole Picture control that exposes the complete active workspace and lets the user jump to any region.
4. **RESPONSIVE ≠ DESTRUCTIVE.** Desktop, tablet, and phone layouts may reflow, but required content and functionality must remain accessible. Do not solve responsiveness by silently removing features.
5. **ONE GABBY.** One Gabby runtime, one conversation, one voice, one command system, one canonical orb. Different panels/modes are views into the same Gabby, not separate assistants.
6. **GABBY MUST NOT OBSTRUCT THE WORK.** The orb may float or anchor over the interface, but it must intelligently resize/reposition so primary work remains usable.
7. **VISUAL REFERENCE IS EVIDENCE.** Approved screenshots/reference images are retained as canonical visual evidence. Implementations must be compared against them rather than approximated from memory.
8. **VISUAL CARTOGRAPHY.** Canonical screens should have machine-readable geometry where practical: canvas size, regions, bounding boxes, anchors, spacing, z-order, responsive rules, and interaction zones.
9. **FUNCTIONALITY MUST SURVIVE UI UPGRADES.** Camera/capture, files, thumbnails, editing, animation, audio, export/share, voice input, chat, navigation, and publish flows must remain functional after visual changes.
10. **PUBLISH MEANS LIVE.** A Publish control is not green merely because a builder generated a bundle. Acceptance is BUILD → TEST → DEPLOY → LIVE URL → OPEN → INTERACT → VERIFY.
11. **NO-FAKE-GREEN.** Code presence, documentation, screenshots, or a claimed fix are not runtime evidence. Required behavior must be executed and verified.
12. **PRESERVE THE WHOLE PICTURE.** If 20 or 30 items exist in a horizontal collection, the UI must allow the user to see all of them by scrolling/swiping. Do not truncate the collection to the first few visible items just because the current viewport is narrow.

## Required interaction model

- Horizontal overflow: swipe/drag/scroll left-right.
- Vertical overflow: scroll up-down.
- Dense panels: collapse/expand without deleting content.
- Complete workspace: `WHOLE PICTURE` / `OVERVIEW` view.
- Focused work: selecting a region returns to a usable focused view.
- Touch + mouse + trackpad: all supported where the platform permits.

## Reference screenshot

`assets/canonical/gabby/apex-workspace-reference-2026-08-29.jpg`

The supplied screenshot is retained as a **current-state visual reference/evidence capture** for the clipping/navigation defect. It must not be treated as the desired final appearance; the target is the same complete information made fully reachable and usable.

## Acceptance criteria

A change fails if any of the following occurs:

- cards/items disappear solely because they are outside the viewport;
- the user cannot reach left/right content;
- the UI crops a canonical region instead of providing navigation;
- an Overview/Whole Picture path is absent where the complete workspace is required;
- a second Gabby/orb/runtime is mounted;
- the orb blocks primary work;
- an existing working capability is broken by the UI upgrade;
- Publish reports success without a verified live runtime.

**Law:** If it exists in the canonical design, the user must be able to reach it. **Do not shorten the picture to make the implementation easier.**