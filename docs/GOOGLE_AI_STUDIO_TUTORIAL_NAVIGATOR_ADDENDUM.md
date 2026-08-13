# Google AI Studio Addendum — APEX Tutorial Navigator + Customer Assist Bar

Paste this addendum after the main APEX build prompt.

## OBJECTIVE

Do not turn APEX learning into a crowded video feed. Build a **validated tutorial discovery and AI navigation system** that finds the most useful walkthrough for the exact situation and can expose the same navigation intelligence to the CUSTOMER side.

## TUTORIAL DISCOVERY

When Gabby decides learning is useful, search broadly enough to compare candidates. Do not choose the first result.

Rank candidates using:

1. exact task fit;
2. practical step-by-step walkthrough quality;
3. official/provider authority;
4. independent validation signals when available;
5. current UI/API/version compatibility;
6. useful duration for the available time;
7. hands-on/reproducibility value.

Prefer current official education when it is genuinely the best match. If a third-party walkthrough is materially better validated or more practical, it may win, but the reason and evidence must be shown.

Never say “most validated” unless observable evidence supports that claim. Otherwise say exactly why it was selected.

## ONE GOOD ANSWER > A WALL OF CONTENT

Normally return:

- 1 primary recommendation;
- up to 2 alternatives only when they add distinct value;
- duration;
- source;
- why it matches the current APEX task;
- validation/quality basis;
- exact link.

If nothing is sufficiently relevant, return nothing rather than filling space.

## CURRENT EXAMPLES TO SUPPORT DISCOVERY

Current official material demonstrates the desired format:

- Vercel Foundations provides nine short practical sessions covering account setup, deployments, settings, security, logs, and observability.
- Google Cloud provides interactive BigQuery walkthroughs for loading/querying data plus current videos.
- Shopify's current GraphQL Admin API documentation supports product catalog/search/sync workflows; avoid teaching deprecated REST product-management workflows to new implementations.

These are discovery examples, not hard-coded recommendations. Re-check current relevance before surfacing them.

## CUSTOMER SERVICE ASSIST BAR

Add a compact AI-powered assistance bar to the CUSTOMER view.

Controls:

- **Ask** — natural-language question.
- **Guide Me** — best validated walkthrough for the requested task.
- **Show Me** — exact verified deep link when available.
- **Learn** — short relevant education.
- **Back to Task** — return to the current customer workflow.

The customer does not need to understand APEX internal architecture, repositories, verification gates, or provider internals.

Examples:

Customer: “Where do I add my products?”

→ Show the exact verified product-management destination.

Customer: “How do I set this up?”

→ Find the best current walkthrough and offer Guide Me.

Customer: “I need help with checkout.”

→ Resolve the current checkout help route and, when useful, attach one validated walkthrough.

## AI NAVIGATION RULES

Natural-language intent may resolve to a verified destination, but AI must never invent a URL.

Use APEX deep-link hierarchy:

1. exact verified destination;
2. exact verified customer storefront URL;
3. platform search/help route;
4. nearest safe parent route with explicit instructions;
5. generic homepage only as last resort.

Tell the customer what will happen when they tap the destination.

## OWNER/CUSTOMER SEPARATION

OWNER / BUILDER mode may expose:

- provider names;
- verification state;
- deployment diagnostics;
- repository operations;
- technical tutorials;
- deeper system links.

CUSTOMER mode should expose only the customer-safe capability, guidance, and support destinations appropriate to that customer.

The same underlying navigation resolver may be shared, but presentation, permissions, and data exposure must be separated.

## ACCOUNT-AWARE LEARNING

When an authorized education/account connector supplies real data, allow:

ACCOUNT → COURSE → PROGRESS → SKILL → APEX TASK

Never infer enrollment or progress from a public URL. Never expose credentials. Never claim a connected account unless the connector actually proves it.

## DRIVE MODE

Drive Mode is audio-first. A video can be queued for later, but the active driving experience must not require watching or interacting with the screen.

## CLASSIFICATION

Keep these distinct:

LEARNING | STRUGGLE | IDEA | TASK | OPPORTUNITY | NOTE

An idea is not a problem. A tutorial is not automatically a task. A popular video is not automatically relevant.

## NO FAKE GREEN

Tutorial ranking does not verify APEX infrastructure. A highly authoritative tutorial cannot make a provider connection GREEN. Provider GREEN still requires the independent APEX evidence gates.

## IMPLEMENTATION REQUIREMENT

Inspect the existing APEX application first. Integrate this capability into the existing Gabby, Morning Briefing, OWNER/CUSTOMER switch, deep-link resolver, and Informative systems. Do not create a disconnected tutorial page.

Add tests for:

- tutorial ranking;
- validation evidence display;
- no-result behavior;
- AI URL invention prevention;
- exact deep-link preference;
- OWNER/CUSTOMER information separation;
- Drive Mode audio-first behavior;
- IDEA versus STRUGGLE classification.

## DONE WHEN

The owner can say:

> “Find me the best walkthrough for what we're stuck on.”

and Gabby searches, compares, explains why one was selected, and gives the link.

The customer can say:

> “Show me how to do this.”

and the Customer Assist Bar gives the best validated guidance without exposing owner-only internals.

GODSPEED.
