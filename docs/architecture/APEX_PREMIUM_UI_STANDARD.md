# APEX Premium UI Standard

## Status
CORE ARCHITECTURAL / DESIGN CONSTRAINT

## Principle
APEX does not target "functional enough" UI.

APEX targets a premium, memorable, world-class product experience: the level of polish users expect from leading consumer technology, creative platforms, and premium digital products.

**HI-FI means HIGH FIDELITY AND HIGH QUALITY.**

A hi-fi screen is not merely a wireframe with colors applied. It is a production-quality visual and interaction experience.

## Non-negotiable quality floor

APEX UI must not regress below the established reference quality.

Every new screen, component, module, or redesign must satisfy:

1. Functional correctness.
2. Visual fidelity to the approved APEX design language/reference.
3. Strong hierarchy and readability.
4. Deliberate spacing and alignment.
5. Premium typography.
6. Consistent interaction behavior.
7. Responsive quality.
8. Accessibility without visual degradation.
9. Fast perceived and actual performance.
10. Clear loading, empty, error, success, partial, and unknown states.
11. Consistent Gabby presence and behavior.
12. Truth/verification states that are visually unmistakable.

## The APEX quality rule

**DO NOT MAKE IT WORSE.**

When modifying an existing UI:

CURRENT EXPERIENCE
→ AUDIT
→ PROPOSED CHANGE
→ VISUAL/INTERACTION COMPARISON
→ REGRESSION CHECK
→ ACCEPT OR REJECT

If the proposed change is less clear, less polished, less usable, less accessible, less performant, or less visually faithful, reject it.

## Premium means intentional, not ornamental

"Pretty" is a requirement, but APEX does not equate pretty with decoration.

Premium quality comes from:
- composition
- typography
- spacing
- visual rhythm
- contrast
- information density
- motion used with purpose
- excellent empty states
- excellent error states
- meaningful micro-interactions
- coherent iconography
- consistent controls
- responsive behavior
- clear system status

Do not add effects merely to appear sophisticated.

## Reference-first design

When MAC supplies a visual reference, it is the primary design source of truth.

The implementation must:
- reproduce the reference faithfully
- preserve its hierarchy and identity
- preserve important proportions and spacing relationships
- preserve its interaction model where known
- improve only when the improvement is clearly additive
- never replace the reference with a generic AI-generated dashboard

Reference fidelity is a requirement, not inspiration.

## APEX + Gabby

Gabby is the universal human-facing interface across APEX.

Every APEX module is Gabby-operable while retaining its specialized execution authority.

The UI should feel like one ecosystem, not a collection of unrelated applications.

## Truth UI

Truth and verification are first-class visual states.

Use explicit statuses:
- GREEN — VERIFIED
- YELLOW — PARTIAL
- BLUE — COMPUTED
- PURPLE — CLAIMED
- RED — FAILED
- BLACK — UNKNOWN

Never represent a verification percentage as a percentage of literal truth.

## Visual workspace

APEX may provide an embedded visual workspace/sketchpad/system canvas as a first-class module. The canvas should use the same premium APEX design language and Gabby interface rather than appearing as a disconnected third-party application.

## Commerce UI

The commerce experience must make the money path visually obvious:
SOURCE → PRODUCT → IMAGE → VALIDATION → SHOPIFY → PUBLISH → READ-BACK → VERIFIED

Real runtime values only. No fabricated green states.

## CRM / system visualization

Where appropriate, APEX may present relationships visually:
customer → project → product → order → payment → support → evidence

The visual layer should remain understandable at a glance while allowing drill-down through Gabby.

## Builder instructions

Any AI builder receiving an APEX UI task must:

1. Inspect existing APEX components before creating replacements.
2. Inspect approved reference screens before designing.
3. Preserve the established visual language.
4. Build the complete requested scope, not a partial interpretation.
5. Verify every acceptance criterion.
6. Report incomplete requirements instead of suggesting them as if they were new.
7. Never spend execution credits rebuilding an already-completed requirement without identifying a meaningful delta.
8. Reject visual regressions.
9. Never call a screen complete solely because it compiles.
10. Provide visual and functional evidence before declaring completion.

## Quality gate

A screen is not COMPLETE until:

- required functionality works
- visual reference requirements pass
- responsive states pass
- loading/empty/error/success states exist where applicable
- Gabby interaction is present where required
- Truth Gate rules are respected
- no security boundary is bypassed
- no existing approved functionality regressed
- evidence supports completion

## North-star statement

**If APEX is intended to stand beside the world's best digital products, it must never intentionally ship a lower design standard than the best experience already available to us.**

We compete on usefulness, truth, speed, reliability, and experience.
