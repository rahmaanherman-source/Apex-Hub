# APEX ECOSYSTEM — MARKET BENCHMARK & REASONABLE UX ARCHITECTURE

SYSTEM_ID: APEX_SOVEREIGN_OPTIMIZER
STATUS: PRODUCTION UX DOCTRINE
SCOPE: CONSUMER MARKET BENCHMARK / DYNAMIC CARD DENSITY

## Purpose
Use adaptive information density rather than an arbitrary global card limit.

Priorities:
- immediate first-fold comprehension
- contextual grouping
- progressive exploration
- horizontal discovery for extended collections
- one unmistakable primary action

## Ecosystem UX Matrix

| App | Primary Above-Fold | Secondary / Extended Deck | Core Trigger |
|---|---|---|---|
| Flora Plug | Location/climate; 2–3 care items; 2 plant spotlights | Species library; Dirt Bar blends | Snap & Check |
| Apex Creator | Broadcast status; recording control; release queue | Track/master shelf; normalization | Go On Air |
| Apex Trades | Site/job check-in; safety badges; 2 critical tasks | Blueprints; equipment; crew communications | Snap Site Hurdle |
| Apex Hub | Store-credit balance; Flora/Creator/Trades portals; digest | Profile; receipts; subscription management | Global Launch |

## Dynamic Density Rules

### First fold
- Present 3–5 meaningful action/status units.
- Prioritize current context over inventory.
- Keep the primary action visually dominant.

### Sections
- Group related items into named sections.
- Typical section size: 2–3 immediate items.
- Avoid vertical walls of repetitive cards.

### Extended decks
- Use horizontal swipe/carousel patterns for larger collections.
- Show partial next-card visibility where appropriate.
- Preserve keyboard and assistive navigation.

### Responsive behavior
- Mobile: compact cards, horizontal shelves, one primary trigger.
- Tablet: increase visible card count without changing hierarchy.
- Desktop: allow denser grids only when viewport width supports it.

## Product Card Contract
Cards may include image, concise title, one-line descriptor, price, and direct action.

Production cards must use real product data. No fabricated inventory, pricing, availability, or imagery.

## Reusable Component Contract
Component: DynamicReasonableDensityShelf

Required:
- horizontal overflow
- snap points
- accessible labels
- responsive minimum card width
- real product data
- no fabricated inventory

## Primary Action Contract
- Flora Plug → Snap & Check
- Apex Creator → Go On Air
- Apex Trades → Snap Site Hurdle
- Apex Hub → Global Launch

A trigger must perform a real action or clearly report NOT_CONFIGURED.

## Evidence Rule
Never convert design intent into implementation status, placeholder data into live inventory, or benchmark observations into verified capabilities.

## Acceptance Criteria
1. First-fold hierarchy is immediately understandable.
2. Extended content is discoverable without overwhelming the viewport.
3. Primary action is unambiguous.
4. Responsive behavior is tested.
5. Real-data boundaries are respected.
6. Accessibility remains functional.
