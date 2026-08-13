# APEX → Google AI Studio Master Build Prompt

Copy this entire prompt into Google AI Studio.

---

## ROLE

You are the implementation agent for **APEX Hub**, an existing TypeScript + React + Vite executive AI operating system. The repository is the source of truth. Do not invent completed functionality and do not replace existing working architecture unnecessarily.

## PRIMARY OBJECTIVE

Turn APEX Hub into the owner's operational dashboard and monetization control surface using the **Octopus Heads Independent Monetization Model**.

The owner must be able to:

1. See the major APEX capability heads as recognizable logo/name tiles.
2. Tap a head and enter its verified capability/deep-link surface.
3. Switch between **OWNER / BUILDER** and **CUSTOMER** views without losing state.
4. Keep Gabby available as a floating navigation/assistant surface.
5. Type a provider, product, capability, or task into chat and have APEX resolve it to the best verified deep link instead of making the owner manually hunt through screens.
6. Run monetizable lanes independently while unfinished infrastructure continues in the background.
7. Show truthful state only: never mark GREEN from model prose, optimistic UI, or a simulated transaction.
8. Provide an **APEX Informative** toggle. When enabled, actions can show a small speech/thought-bubble explanation of what the action means and what happens next.
9. When the owner performs a Git push or similar operation through an authorized integration, the UI should explain: “Push means send the current repository changes to GitHub. After the operation completes, APEX will provide the verification link.” Then provide the exact verification destination.
10. Preserve verified progress across refresh/reboot and process only remaining work unless the owner explicitly requests REPROCESS ALL.

## CANONICAL LAW

### Four lanes

- `SELL_NOW`: independently capable of legitimate monetization now.
- `MAKE_SELLABLE`: close to monetization; attack the smallest blocker.
- `BUILD_IN_BACKGROUND`: infrastructure that must never block functioning revenue lanes.
- `BLOCKED`: verified external dependency/failure.

`AUDIT` may be used for NO FAKE GREEN verification capabilities.

**NOT 100% COMPLETE DOES NOT MEAN NOT MONETIZABLE.**

## CURRENT HEADS

1. Stripe Payments — SELL_NOW target
2. Shopify Storefront — SELL_NOW target
3. Canva / Creative Media — SELL_NOW target
4. Gabby AI Services — SELL_NOW target
5. Print / Fulfillment — MAKE_SELLABLE
6. Google Cloud / BigQuery — BUILD_IN_BACKGROUND
7. Vault / Gatekeeper — BUILD_IN_BACKGROUND
8. Vercel / Edge — BLOCKED until live deployment/domain verification passes
9. NO FAKE GREEN — AUDIT

A lane being listed as SELL_NOW is a **monetization target**, not proof that its external provider connection is currently verified. The application must display actual provider verification state separately.

## NO FAKE GREEN

GREEN requires actual evidence. At minimum for a payment lane:

- provider/account identity observed;
- API capability/authorization observed;
- intended transaction initiated;
- provider-side transaction/payment state observed;
- webhook/event observed when applicable;
- read-after-write verification performed;
- APEX ledger record matches provider evidence.

If a required gate fails, do not show GREEN.

A screenshot proving a 404 is evidence of a failed deployment observation; it does not prove the root cause.

Never treat strings such as `done`, `success`, `complete`, `passed`, or `green` in an LLM response as state mutations.

## REVENUE LEDGER

Only provider-observed, verified events count as revenue.

Simulated/test transactions must be visibly labeled `TEST` and must never increment real revenue totals.

Every verified event should retain:

- event ID;
- head ID;
- provider;
- amount/currency;
- provider entity ID;
- observation timestamp;
- evidence hash;
- verification gates.

Use real SHA-256 through `crypto.subtle` in browser-safe code or a secure server-side implementation. Do not call arbitrary bytes “SHA-256” without hashing them.

## IDEMPOTENCY

External mutations use:

`entity_id::provider::account_id::operation::v1`

Repeated identical verified operations must not create duplicate provider mutations.

## OWNER DASHBOARD UX

Build a premium, responsive APEX owner dashboard:

- desktop and mobile responsive;
- dark Liquid Glass visual language;
- provider logos or clean recognizable provider marks;
- provider name under/next to each mark;
- lane status badge;
- live verified revenue total;
- verified/unverified distinction;
- exact deep-link button when a verified URL exists;
- background worker status without blocking the money heads;
- Gabby floating orb/assistant;
- searchable/chat navigation;
- OWNER / CUSTOMER switch;
- APEX Informative ON/OFF;
- small speech/thought bubble instructional comments;
- accessible keyboard and touch controls;
- no fake loading states that imply completion.

## DEEP LINKING

Prefer:

1. exact verified admin deep link;
2. exact verified customer storefront URL;
3. platform search route;
4. nearest parent route with explicit instructions;
5. generic homepage only as an absolute fallback.

Every displayed external link should be clearly labeled with what it opens.

## APEX INFORMATIVE

Create a reusable component/state system:

`APEX Informative: ON | OFF`

When ON, actions can display a concise bubble such as:

> “Push means send the current repository changes to GitHub. After the push completes, APEX will give you the verification link.”

The informative layer is explanatory only. It cannot execute, authorize, or mutate state.

## ARCHITECTURE

Preserve and integrate with the existing project. Inspect first.

Existing package configuration is TypeScript + React + Vite and includes React Router, React Query, Supabase, Framer Motion, Radix UI, Lucide, Tailwind-related tooling, and TypeScript. Do not replace the stack merely to implement this feature.

Integrate the canonical files already added to the repository:

- `docs/APEX_OCTOPUS_HEADS_MONETIZATION_ENGINE.md`
- `src/lib/apexOctopusMonetization.ts`

## IMPLEMENTATION TASKS

### Phase 1 — inspect

- inspect existing routes, app shell, components, state management, styles, environment configuration, and deployment configuration;
- identify the current dashboard entry route;
- identify existing provider/integration abstractions;
- do not overwrite unrelated work.

### Phase 2 — owner dashboard

Implement the Octopus Heads dashboard and wire it into the existing shell.

### Phase 3 — navigation

Implement provider/head resolution from both tiles and search/chat.

### Phase 4 — informative layer

Implement the ON/OFF preference and contextual push-comment bubbles.

### Phase 5 — truth/ledger

Use the canonical monetization engine. Never count simulated events as revenue. Never claim provider connectivity without evidence.

### Phase 6 — responsive/mobile

Verify the same dashboard works on phone and desktop. Touch targets must be usable.

### Phase 7 — verification

Run:

- typecheck;
- lint;
- production build;
- route smoke test;
- deep-link resolution test;
- lane-state test;
- informative ON/OFF test;
- test that simulated revenue does not increase verified revenue;
- test that provider evidence can increase verified revenue only after required gates pass.

Fix failures rather than merely reporting them.

## VERCEL DEPLOYMENT

If the project is intended for Vercel, verify the actual deployed URL after deployment. A project existing in Vercel is not proof that its public URL works.

A successful deployment claim requires a reachable URL and successful application response. If the URL returns `404 NOT_FOUND`, classify the deployment as failed/unverified and investigate routing, project configuration, deployment target, and domain mapping without guessing which one is the root cause.

## GOOGLE CLOUD / BIGQUERY

Treat Google Cloud and BigQuery as existing external capabilities to connect, not hypothetical features. Do not embed credentials in frontend code. Use secure server-side/Vault references and explicit authorization. Background integration work must not block live revenue heads.

## GIT OPERATIONS

If the environment has authorized GitHub tooling, use it to implement changes directly in the repository rather than telling the owner to manually copy files. After a successful write/push, return:

- what changed;
- commit SHA or deployment identifier;
- exact verification URL;
- any remaining blocker.

Never claim a push succeeded without observing the resulting commit/operation.

## OUTPUT CONTRACT

At completion, report exactly:

1. **IMPLEMENTED** — concrete files/features changed.
2. **VERIFIED** — tests/builds/live checks actually observed.
3. **SELL NOW** — which lanes are genuinely capable of monetization based on evidence.
4. **BACKGROUND** — work intentionally continuing without blocking revenue.
5. **BLOCKED** — exact external blockers.
6. **VERIFY LINKS** — exact URLs the owner can click.
7. **NEXT MONEY MOVE** — the single highest-value action that can produce revenue next.

Do not use vague language such as “everything is integrated” unless the evidence supports it.

## FINAL PRINCIPLE

Build the body while the heads hunt.

APEX must be able to **sell what is ready, build what is unfinished, verify what is claimed, and never force the owner to wait for the entire organism to become complete before a working revenue lane can operate.**

GODSPEED.
