# APEX GLOBAL SIDEBAR & READABILITY STANDARD

**Status:** Canonical UI/UX requirement  
**Applies to:** APEX / GODSPEED Command Hub and all modules rendered inside its application shell  
**Rule:** Non-negotiable unless a later canonical architecture decision explicitly supersedes it.

## 1. Purpose

The APEX Command Hub is an operating console, not a collection of disconnected screens. The user must be able to see, reach, understand, and operate every relevant system area without hunting through unrelated pages.

The global navigation shell is therefore part of the system architecture.

## 2. Permanent Global Sidebar

On desktop, the global sidebar MUST remain available throughout the application.

It MUST NOT:

- disappear on individual routes;
- be replaced by unrelated page-specific navigation;
- force the user to hunt for modules;
- hide important navigation behind unnecessary interactions;
- create duplicate dashboards for the same capability;
- change structure between modules without an explicit architectural reason.

The same application shell should contain the major APEX modules, using existing module names/routes where they already exist.

### Minimum navigation surface

The exact list must be reconciled against the live repository before implementation, but the Command Hub should expose the applicable existing capabilities including:

- Dashboard
- AI / Gabby
- System Health
- Analytics
- Real-Time Monitor
- Incident Alerts
- Deployments
- Launch Roadmap
- Verification
- Integrations
- Shopify / Commerce
- Payments
- Products
- Orders
- Revenue
- Data Pipeline
- Database
- Security
- Credentials / Vault
- Evidence
- Audit Log
- Settings

**Do not create duplicates when an existing canonical module already provides the capability.**

## 3. Consistent Application Shell

Every major module should render inside the same shell:

```text
GLOBAL SIDEBAR
      ↓
PAGE HEADER
      ↓
PAGE CONTENT
      ↓
REAL STATUS
      ↓
REAL ACTIONS
      ↓
REAL EVIDENCE
      ↓
ERROR / LOADING / EMPTY STATES
```

The shell is shared. Module-specific execution remains owned by the module.

## 4. Navigation Behavior

The sidebar MUST:

1. remain visible on desktop;
2. remain consistent across routes;
3. identify the active module/page;
4. preserve normal routing behavior;
5. survive page refresh;
6. work with browser back/forward navigation;
7. avoid covering critical content;
8. avoid causing horizontal overflow;
9. use readable labels;
10. provide accessible names/tooltips where an icon-only control is unavoidable;
11. never expose a dead navigation item as if it were functional.

On narrow/mobile layouts, the sidebar may become a navigation drawer, but navigation must remain discoverable and usable. Responsive behavior must not destroy readability or access to system functions.

## 5. Readability Is a Functional Requirement

Information that exists but cannot be read or understood is not operationally useful.

All user-facing system information must remain readable, including:

- page titles;
- headings;
- navigation labels;
- button labels;
- status text;
- errors;
- warnings;
- timestamps;
- tables;
- evidence references;
- logs;
- progress values;
- percentages;
- verification results;
- system responses.

Do not rely on color alone to communicate meaning.

Do not use tiny critical text, clipped labels, unreadable tables, hidden controls, poor contrast, overlapping content, or controls that fall outside the viewport.

## 6. Every Visible Control Must Work

Every visible button, navigation item, toggle, form action, filter, tab, and primary control must have a real implementation path.

A control is not complete merely because it renders.

Minimum acceptance state:

```text
VISIBLE
  +
READABLE
  +
NAVIGABLE
  +
CONNECTED
  +
EXECUTABLE
  +
TESTED
  +
VERIFIED
```

A decorative or placeholder control must not be presented as operational.

## 7. No Fake Green

The UI must never imply a stronger state than the evidence supports.

Use explicit states such as:

- **VERIFIED** — required real check passed;
- **CONNECTED** — connection exists, but do not imply successful operation unless tested;
- **UNTESTED** — implementation exists but has not been proven;
- **BLOCKED** — a known dependency prevents execution;
- **FAILED** — the required operation failed;
- **UNKNOWN / UNVERIFIED** — insufficient evidence.

Green is reserved for a defined verified/healthy condition. A UI flag, database boolean, or successful render is not proof by itself.

## 8. Real-Time Requirement

Where the system claims real-time behavior, the implementation must demonstrate the complete path:

```text
SOURCE / EVENT
      ↓
BACKEND / DATA LAYER
      ↓
REAL-TIME CHANNEL / SUBSCRIPTION / EVENT PIPELINE
      ↓
STATE UPDATE
      ↓
VISIBLE UI UPDATE
      ↓
EVIDENCE / TIMESTAMP
```

A static dashboard, periodically refreshed page, mocked value, or local-only state must not be labeled real-time unless the actual requirement is satisfied and tested.

## 9. Status Must Be Drillable

High-level status summaries must be traceable to the underlying state.

For example:

```text
SYSTEM HEALTH: 92%
        ↓
WHAT IS THE 92%?
        ↓
verified components
pending components
failed components
blocked components
unverified components
        ↓
individual evidence
```

Percentages MUST have a defined denominator. Never display a vague confidence percentage as if it were a completion or verification percentage.

## 10. Gabby Integration

Gabby is the universal human-facing interface across the APEX ecosystem, but specialized modules retain execution authority.

The standard flow is:

```text
USER
  ↓
GABBY UI
  ↓
AUTHORIZATION / GATEKEEPER
  ↓
SPECIALIZED MODULE
  ↓
REAL EXECUTION
  ↓
EVIDENCE / RESULT
  ↓
GABBY UI
```

Gabby must not bypass module permissions, validation, security controls, or truth/evidence gates.

Gabby should make system state easier to understand, not manufacture success.

## 11. Regression Protection

The global shell is protected behavior.

A feature change in one module must not silently remove or degrade:

- global navigation;
- sidebar readability;
- active-route indication;
- routing;
- system status visibility;
- evidence access;
- real-time indicators;
- responsive navigation.

Every UI audit must include a regression check of the global shell.

## 12. Acceptance Test

Before declaring the UI complete, test:

### Navigation

- every sidebar destination;
- every active-state indicator;
- refresh on every major route;
- browser back/forward;
- direct URL navigation;
- desktop sidebar persistence;
- mobile drawer/navigation behavior.

### Readability

- headings;
- labels;
- buttons;
- tables;
- status values;
- errors;
- evidence;
- timestamps;
- percentages;
- long text;
- narrow viewport behavior.

### Functionality

- every visible primary action;
- every form;
- every filter;
- every integration action;
- loading states;
- success states;
- failure states;
- empty states.

### Truth

- no fake green;
- no unverified success claims;
- no mocked data presented as live data;
- no real-time claim without a real event path;
- no completion claim without verification evidence.

## 13. Operating Rule

APEX follows:

```text
AUDIT
  ↓
UNDERSTAND
  ↓
PRESERVE
  ↓
FIND ALL GAPS
  ↓
FIX SAFELY
  ↓
RECORD THE FIX
  ↓
RETEST
  ↓
REBUILD
  ↓
REBOOT
  ↓
VERIFY
```

Do not stop after the first successful fix when additional failures remain reachable.

## 14. Governing Principle

**If the information exists, the system must provide a clear, readable, truthful path to it.**

**If a control exists, it must actually work.**

**If the system says green, the evidence must earn green.**

**The human operates the system; the system should not make the human act as its monitoring middleware.**

---

**Canonical source:** APEX / GODSPEED architecture standards.  
**Change rule:** Extend existing canonical architecture; do not create competing navigation or UI standards.
