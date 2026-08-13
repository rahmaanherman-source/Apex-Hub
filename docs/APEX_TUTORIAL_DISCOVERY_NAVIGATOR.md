# APEX Tutorial Discovery Navigator

## Purpose

APEX must not crowd the owner with random videos. When learning is useful, Gabby should search for the **best validated walkthrough** for the exact task, skill gap, or idea context.

This is a discovery and navigation layer, not a generic video feed.

## Selection law

Rank candidate tutorials by evidence, in this order:

1. **Task fit** — directly teaches the current APEX task or blocker.
2. **Walkthrough quality** — demonstrably step-by-step, practical, and usable.
3. **Source authority** — official platform/provider education is preferred when it teaches the needed workflow accurately.
4. **Independent validation** — user ratings, completion signals, credible reviews, community confirmation, or other observable evidence where available.
5. **Recency** — current UI/API/version compatibility.
6. **Duration fit** — prioritize a useful lesson that fits the available time.
7. **Hands-on value** — preference for material that lets the owner reproduce the action.

Never claim a tutorial is “most validated” unless the evidence actually supports that ranking. If validation data is unavailable, label the basis of selection explicitly.

## Discovery record

Every recommendation should store:

- title
- provider/source
- URL
- content type: video | walkthrough | course | documentation
- duration when available
- skill/topic
- APEX task it supports
- source authority score
- validation evidence summary
- freshness/version signal
- hands-on score
- reason recommended
- date discovered
- optional account/course/progress reference

## APEX recommendation behavior

Gabby should ask herself:

> What is MAC doing now, what is blocking him, what is coming next, and is there a short piece of validated instruction that would materially improve the outcome?

If no, recommend nothing.

If yes, recommend **one primary item**, with up to two alternatives only when they provide meaningfully different value.

Examples:

- Vercel 404 problem → deployment/routing troubleshooting walkthrough, not a generic Vercel introduction.
- BigQuery setup → interactive query/load walkthrough when that is the current task.
- Shopify catalog work → current GraphQL Admin product workflow rather than deprecated REST instructions.
- Stripe webhook work → current webhook/payment integration walkthrough matched to the actual implementation.

## Customer Service / Customer Side

The same tutorial/navigation engine becomes a customer-facing assistance bar, but with a different policy.

### Customer Assist Bar

A compact bar can expose:

- **Ask** — type what the customer wants to accomplish.
- **Guide me** — get the best validated walkthrough.
- **Show me** — open the exact relevant page or deep link when available.
- **Learn** — short educational material.
- **Back to task** — return to the customer workflow.

The customer should not need to understand APEX internals, provider names, repository concepts, or verification terminology.

## AI navigation

AI may resolve natural-language intent to a verified destination:

> “Where do I add my products?”

→ resolve to the exact product-management destination when verified.

> “Show me how to connect my store.”

→ resolve to the appropriate current setup walkthrough.

> “I need help with checkout.”

→ surface the relevant help/tutorial and exact customer action.

AI navigation must never invent a URL. If an exact destination cannot be verified, use the next-safe deep-link tier and explain what the customer will see.

## Account-aware learning

When an authorized account integration exposes course/progress information, APEX may connect:

`ACCOUNT → COURSE → PROGRESS → SKILL → APEX TASK`

Never expose private account data unnecessarily. Never claim course progress that was not observed.

## Drive Mode

Drive Mode is audio-first. It may queue a tutorial or lesson for listening when appropriate, but the UI must not encourage screen interaction while driving.

Suggested queue format:

`APEX DRIVE — 18 min`

1. Primary lesson — 8 min — exact current task
2. Optional lesson — 6 min — supporting skill
3. Optional lesson — 4 min — next likely step

## No-noise rule

Do not send a tutorial recommendation merely because a topic is popular. The recommendation must have a concrete APEX reason.

Do not turn every user statement into a learning problem. Preserve separate classifications:

`LEARNING | STRUGGLE | IDEA | TASK | OPPORTUNITY | NOTE`

## Truth rule

Tutorial quality is evidence-scored separately from system/provider verification. A highly rated video does not make an APEX provider connection GREEN.

Likewise, an official tutorial does not prove that the user's account, deployment, API, or integration is working.

## Current validated-source examples

As of 2026-08-12, current official sources include:

- Vercel Foundations: nine short sessions covering account setup, deployments, settings, security, logs, and observability.
- Google Cloud BigQuery interactive walkthroughs: guided loading/querying workflows and videos.
- Shopify current GraphQL Admin product documentation: current product catalog/query workflows; REST product management is legacy/deprecated for new app development.

These are examples for the discovery engine, not hard-coded endorsements. The engine should re-evaluate current source quality when making a recommendation.
