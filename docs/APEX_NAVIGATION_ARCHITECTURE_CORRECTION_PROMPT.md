# APEX NAVIGATION ARCHITECTURE CORRECTION PROMPT

**Purpose:** Source-of-truth prompt for correcting the APEX Dashboard navigation presentation in Google AI Studio or another UI builder.

---

## FIX THE NAVIGATION ARCHITECTURE — DO NOT JUMBLE OR OVERLAP THE UI

When I said I wanted the APEX Dashboard to be **layered**, I did **NOT** mean that panels, windows, cards, or interfaces should be stacked on top of each other randomly.

I mean **structured layered navigation** — like a professional operating system/application shell.

### REQUIRED NAVIGATION HIERARCHY

**LAYER 1 — PRIMARY NAVIGATION**

Place the major APEX areas in a clean primary navigation bar.

Example:

`COMMAND HUB | GABBY AI | FORENSICS | FINANCE | ORDERS | ARCHIVE | SETTINGS`

These are the major application destinations.

**LAYER 2 — SECONDARY NAVIGATION**

When a primary section is selected, expose its related subsections in a dedicated secondary navigation area.

Example:

`GABBY AI → Operator | Audit Feed | Tasks | Memory | System Status`

**LAYER 3 — ACTIVE WORKSPACE**

The selected tab opens its actual content in the main workspace.

**Do NOT open content as a floating window over the dashboard.**

### OPTIONAL UTILITY NAVIGATION

Navigation may also exist across the top, along the left side, or along the bottom when useful, but each navigation surface must represent a different level or utility function.

Do not duplicate the same navigation unnecessarily.

---

## CRITICAL UI RULE

**TABS ARE NOT WINDOWS.**

A tab changes the active view inside the application shell.

Do NOT:

- stack dashboards on dashboards;
- put Gabby over the dashboard as a floating box;
- create overlapping panels;
- hide navigation underneath another panel;
- create multiple competing hamburger menus;
- make cards behave like independent windows;
- randomly layer components because the word "layered" was used.

### WHAT "LAYERED" MEANS

```text
PRIMARY NAVIGATION
        ↓
SECONDARY NAVIGATION
        ↓
ACTIVE WORKSPACE
        ↓
OPTIONAL CONTEXTUAL / UTILITY CONTROLS
```

Not:

```text
WINDOW
   over
WINDOW
   over
WINDOW
```

---

# GABBY AI

Gabby is a **first-class application section**, not a floating dashboard covering the Command Hub.

When **GABBY AI** is selected:

1. The main workspace changes to Gabby.
2. Gabby's tools appear inside that workspace.
3. Her tabs/sub-tabs remain organized within that section.
4. The Command Hub remains accessible through primary navigation.
5. Nothing needs to physically cover or obscure another interface.

---

# COLLAPSING NAVIGATION — REQUIRED

The navigation shell must support **intentional collapsing**, not disappearing/jumbling behavior.

### Desktop behavior

The left/secondary navigation may collapse to a compact rail when the user intentionally clicks its collapse control.

When expanded:

- show the navigation labels;
- show the relevant section grouping;
- preserve the active state;
- keep the workspace clean.

When collapsed:

- keep the navigation rail visible enough to remain discoverable;
- preserve recognizable icons/marks;
- keep the active destination identifiable;
- never cover the workspace;
- never move the hamburger control to a random location;
- never cause the content to overlap the navigation.

### Mobile/small-screen behavior

Collapse intelligently into:

```text
PRIMARY MENU
      ↓
SECTION
      ↓
SUBSECTION
      ↓
CONTENT
```

Use a navigation drawer where appropriate.

Do **not** simply shrink every component until text, controls, or panels overlap.

### Collapse control

There must be **one clear navigation collapse/expand control** for the relevant navigation surface.

Do not create multiple competing three-line/hamburger controls.

---

# HAMBURGER / THREE-LINE CONTROL POSITION

The three-line menu control currently appears all the way on the far right when viewed from the user's normal screen orientation.

**Fix this.**

The hamburger/collapse control belongs to the navigation shell and must be positioned with the navigation/brand controls in the intended upper corner.

If the existing shield/brand area occupies that corner, the hamburger control must be **inside or immediately associated with that navigation/brand area**, not stranded at the opposite edge of the screen.

Requirements:

- consistent placement across routes;
- visually associated with the sidebar/navigation it controls;
- reachable without covering content;
- clear expand/collapse behavior;
- no duplicate hamburger controls;
- no random floating menu button.

The control must not be allowed to drift to the far opposite side merely because of a flex/layout rule.

---

# APEX SENTINEL BRANDING — REQUIRED

The upper-corner brand/shield area must use the **existing APEX Sentinel system branding/logo** when that asset is available in the existing project/system.

**Do not substitute a random third-party, stock, placeholder, generated, or unrelated logo.**

The APEX Sentinel logo is part of the system identity and should be treated as an existing system asset.

### Branding rules

- Reuse the existing APEX Sentinel logo asset.
- Do not redraw or replace it with unrelated branding.
- Do not use another company's logo.
- Do not use a generic placeholder where the existing asset is available.
- Preserve the existing logo's intended proportions and visual identity.
- Place it in the intended upper-corner brand/shield area.
- The logo should function as part of the APEX application shell, not as a random decorative image.

If the exact asset cannot be located in the current project, **do not invent a replacement and do not silently substitute another logo**. Identify the missing asset as an unresolved dependency.

---

# RESPONSIVE SHELL

The same hierarchy must remain intact across screen sizes.

### Desktop

```text
[APEX SENTINEL / BRAND] [PRIMARY NAVIGATION]
                 ↓
       [SECONDARY NAVIGATION]
                 ↓
          [WORKSPACE]
```

### Collapsed desktop

```text
[APEX SENTINEL] [COMPACT NAV RAIL] [WORKSPACE]
                       ↑
                collapse control
```

### Mobile

```text
[APEX SENTINEL] [MENU]
        ↓
     SECTION
        ↓
   SUBSECTION
        ↓
     CONTENT
```

No overlapping layers. No competing menus. No content hidden underneath navigation.

---

# DO NOT BREAK EXISTING APEX FUNCTIONALITY

Keep the existing APEX functionality, routes, data model, providers, services, authentication, integrations, and system capabilities.

This task is a **navigation architecture and presentation correction**, not a reason to rebuild the application from scratch or remove existing capabilities.

Reuse the existing shell, routing, services, widgets, providers, and assets wherever they already exist.

Do not create duplicate architecture merely to solve a presentation problem.

---

# ACCEPTANCE TEST

The correction is not complete until all of the following are true:

### Navigation

- Primary navigation is clearly separated from secondary navigation.
- Secondary navigation belongs to the selected primary section.
- Active content renders in the main workspace.
- Tabs behave as navigation, not windows.
- Gabby does not physically cover the Command Hub.
- The Command Hub remains reachable from Gabby.

### Collapsing

- Sidebar/secondary navigation can intentionally collapse.
- Sidebar/secondary navigation can intentionally expand.
- Collapsing does not overlap content.
- Expanding does not create duplicate navigation.
- The active route remains clear in both states.
- Mobile navigation becomes a clean drawer/menu hierarchy rather than a shrunken pile of controls.

### Hamburger

- There is one clear collapse/menu control for the navigation surface.
- It is positioned with the navigation/brand area.
- It is not stranded on the far opposite side of the screen.
- Its placement is consistent across routes.

### Branding

- The existing APEX Sentinel logo is used when available.
- No unrelated/random logo is displayed.
- No third-party logo is substituted.
- The logo remains inside the intended APEX shell/brand area.

### Visual integrity

- No overlapping dashboards.
- No floating Gabby panel covering other interfaces.
- No navigation hidden underneath another panel.
- No competing hamburger menus.
- No cards behaving like windows.
- No horizontal overflow caused by the navigation shell.
- Content remains clean and usable.

### Functional integrity

- Existing routes still work.
- Existing data remains connected.
- Existing capabilities remain available.
- Existing services/providers are preserved.
- No fake success state is introduced.

---

# FINAL DESIGN PRINCIPLE

The interface should feel like a **real operating system / command center** where every navigation element has a defined level.

```text
WHERE AM I?
→ PRIMARY SECTION

WHAT PART OF IT AM I IN?
→ SECONDARY TAB

WHAT AM I DOING?
→ ACTIVE WORKSPACE

WHAT ACTIONS ARE AVAILABLE?
→ CONTEXTUAL CONTROLS
```

**The objective is layered navigation, not layered windows.**

**The navigation shell organizes the application. It must never become the obstruction.**

**Use the existing APEX Sentinel identity. Do not replace system branding with unrelated branding.**
