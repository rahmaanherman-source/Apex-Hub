# APEX 360 Media Interaction Contract

Status: CANONICAL UX REQUIREMENT

## Purpose

When an asset is a true 360° photograph or equirectangular panorama, the APEX UI should present it as an interactive 360° viewer when technically supported—not flatten it into a cropped static thumbnail.

## Required behavior

- Preserve the complete source image/data; do not crop away the panorama to make it fit a card.
- Allow drag/swipe left and right to rotate the 360° view.
- Support mouse/touch interaction where the runtime permits.
- Provide a clear affordance that the image is interactive when discoverability would otherwise be weak.
- Preserve the full image as the source asset even when a thumbnail/preview is shown.
- On smaller screens, reflow the viewer or allow horizontal navigation; never solve viewport constraints by deleting/cropping meaningful content.
- If the source is not actually 360°, do not falsely label it as 360°. A normal photograph may use a controlled presentation effect, but it must remain distinguishable from a true panoramic viewer.
- 360 interaction must not create a second Gabby instance or obstruct primary workspace controls.

## Acceptance test

A true 360 asset passes only when:

1. The full source is retained.
2. A user can rotate the scene horizontally by drag/swipe.
3. The viewer works on supported desktop and mobile input modes.
4. No primary content is silently cropped to fit the viewport.
5. The implementation is tested in the actual runtime before being reported as complete.

## Verification rule

`SOURCE TYPE → VIEWER MODE → INTERACTION TEST → RESPONSIVE TEST → VISUAL CHECK → EVIDENCE`

Documentation alone is not proof of runtime support.
