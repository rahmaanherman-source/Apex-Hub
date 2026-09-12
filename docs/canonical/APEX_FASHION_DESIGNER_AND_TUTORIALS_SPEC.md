# APEX Fashion Designer + APEX Tutorials — Canonical Product Specification

**Status:** CANONICAL PRODUCT REQUIREMENT — initial repository capture  
**Parent:** APEX Hub  
**Purpose:** Capture the requested interactive fashion-design and learning experience as a durable repository specification so the feature is not lost in builder chat history.

## 1. Product concept

APEX Hub should include a fashion-focused experience where users can:

1. Browse a fashion catalog.
2. Open a garment/design workspace.
3. Visually edit the garment.
4. Ask Gabby for design suggestions.
5. Drag suggested/generated artwork onto garment placement zones.
6. Learn from tutorials while designing.
7. Save designs as projects and continue refining them.
8. Develop design judgment and skills rather than merely consuming finished products.

The experience is intended to support family participation and future designers. It should feel like a creative studio and learning environment, not a generic ecommerce product page.

## 2. Garment interaction model

A garment is an editable composition with explicit zones.

### Garment zones

The initial zone model must support at minimum:

- Collar
- Sleeves
- Chest/front
- Back
- Logo/brand placement

The architecture must allow additional zones later without redesigning the core editor.

### Direct manipulation

Users should be able to:

- Hover over an editable garment area to reveal that it is interactive.
- Click/select the area.
- Change its color.
- Change its available style/variant.
- Preview the result immediately.
- Select artwork/assets.
- Drag artwork from a suggestion/catalog tray onto the garment.
- Reposition, resize, rotate, and remove placed artwork.
- Undo/redo changes.
- Reset a zone without destroying the whole design.
- Save the current design as a project.

The interaction should make the relationship between a physical garment part and its editable digital representation obvious.

## 3. Gabby design assistance

Gabby is the creative copilot, not a replacement for the designer.

The user can type a natural-language request to Gabby, such as a request for:

- collar ideas
- sleeve treatments
- chest graphics
- back graphics
- logo treatments
- color combinations
- typography ideas
- pattern ideas
- complete outfit concepts

Gabby should return several distinct suggestions rather than one forced answer.

Each suggestion should be actionable:

- preview it;
- apply it;
- drag it into a garment zone;
- modify it;
- save it;
- reject it and request another direction.

Generated artwork/design suggestions must remain clearly represented as generated or user-created assets and must not silently overwrite an existing design.

## 4. Design playground

The core experience should be a visual playground:

**Choose garment → choose zone → choose color/style → choose or generate artwork → place → refine → save → learn/share/continue.**

The editor should prioritize direct manipulation and visual feedback over forms and configuration screens.

## 5. Fashion catalog

APEX Hub should expose a fashion catalog that can contain:

- garments
- garment types
- colors
- styles
- collections
- patterns
- graphics
- logos
- typography
- accessories
- completed community/family projects where sharing is authorized

Catalog browsing and designing are connected but remain distinct surfaces.

A catalog item should be able to become the starting garment for the design workspace without requiring the user to rebuild the selection.

## 6. APEX Tutorials

APEX Tutorials should be a first-class learning surface inside APEX Hub.

Tutorials should teach both the product and the discipline of fashion design.

Examples:

- How to choose a garment silhouette
- How collar choices change the look
- Sleeve design fundamentals
- Front/chest composition
- Back graphic composition
- Logo placement
- Color theory
- Typography
- Pattern and texture
- Building a collection
- Turning an idea into a wearable design
- Reviewing and improving a design

Tutorials should be interactive where practical.

A tutorial may point at the exact control or garment zone being taught and allow the learner to perform the action rather than only watch a video.

## 7. Catalog-to-tutorial-to-design loop

The intended learning loop is:

**Explore catalog → select garment → learn a concept → experiment → ask Gabby → apply suggestion → refine → save design → receive next useful lesson.**

The system should not turn learning into a crowded video feed. Existing APEX tutorial-discovery rules remain authoritative for tutorial discovery and validation.

## 8. Family / emerging-designer mode

The experience should support multiple people learning and creating together.

Where authorization permits, users can:

- open a shared project;
- teach another family member;
- leave design feedback;
- compare versions;
- build a collection together;
- save individual designer profiles/projects;
- preserve attribution/provenance for original work.

The product should encourage experimentation and skill development, especially for young or emerging designers.

## 9. Shared APEX architecture

This is an APEX Hub application/module, not a separate disconnected ecosystem.

Use existing shared APEX capabilities for:

- identity
- permissions
- projects
- assets
- AI/Gabby orchestration
- storage/Vault where applicable
- analytics
- notifications
- publishing/sharing

Do not duplicate Gabby as a second assistant.

Providers remain implementation details and must remain replaceable. The canonical APEX architecture must not become dependent on a particular builder/vendor.

## 10. Surface separation

The Fashion Designer, APEX Tutorials, Store, Education, Studio, and other APEX Hub surfaces should remain visually and functionally distinct while using controlled shared relationships.

Do not allow unrelated application features to bleed into the fashion editor.

The fashion editor owns its garment-design controls. Shared APEX services provide identity, assets, Gabby, persistence, and orchestration.

## 11. Project data model

A saved fashion project should preserve at minimum:

- project ID
- owner/authorized collaborators
- garment/base item
- garment zones
- zone colors
- zone styles/variants
- placed assets
- asset positions
- asset transformations
- typography settings
- generated suggestions used
- design version/history
- creation/update timestamps
- provenance for imported/generated assets
- tutorial lessons completed or associated with the project

Never flatten the design into a single irreversible image when structured project data can be preserved.

## 12. Safety and rights

The system must distinguish:

- user-created assets
- APEX catalog assets
- generated assets
- imported third-party assets

Do not imply that generated or imported artwork is automatically cleared for commercial use.

Sharing must respect permissions and user authorization.

## 13. Implementation direction

Build in verifiable increments:

1. Fashion catalog shell.
2. Garment viewer with selectable zones.
3. Zone color/style controls.
4. Drag-and-drop asset placement.
5. Undo/redo and project save.
6. Gabby suggestion interface.
7. Generated/suggested asset application.
8. APEX Tutorials integration.
9. Family/collaboration permissions.
10. Version history/provenance.
11. Tests and accessibility.
12. Mobile/tablet/desktop refinement.

Do not replace or delete existing APEX Hub modules while implementing this feature.

## 14. Acceptance target

A first successful end-to-end demonstration should allow a user to:

1. Enter APEX Hub.
2. Open the Fashion experience.
3. Browse the catalog.
4. Pick a garment.
5. Click the collar.
6. Change its color.
7. Change its style.
8. Click the chest/back/sleeve zone.
9. Ask Gabby for several design ideas.
10. Drag one idea onto the garment.
11. Move/resize the artwork.
12. Save the design.
13. Open an associated tutorial.
14. Continue editing after the lesson.
15. Save a version without destroying the previous version.

**Canonical intent:** APEX should help people become designers by letting them explore, learn, create, manipulate, receive AI assistance, and preserve their work.
