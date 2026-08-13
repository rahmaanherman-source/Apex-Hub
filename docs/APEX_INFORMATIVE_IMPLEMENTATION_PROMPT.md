# APEX INFORMATIVE — IMPLEMENTATION PROMPT

Build this into the existing APEX Hub owner dashboard. Do not create a separate demo, mock dashboard, or parallel application.

## OWNER EXPERIENCE

The owner dashboard is the command center. Preserve the existing APEX visual language and responsive behavior. It must work on desktop and phone.

Each provider/service tile contains:

- provider logo/avatar
- provider name
- connection/verification state
- direct-launch action
- optional APEX INFORMATIVE toggle
- optional status details

Provider examples include GitHub, Vercel, Canva, Google Cloud, BigQuery, Vertex AI, Stripe, Shopify, Cloudflare, and other configured APEX providers.

## APEX INFORMATIVE

Add a global `APEX INFORMATIVE` switch and allow it to be respected by action surfaces.

When ON, every action that a non-expert may reasonably need explained gets a small floating speech/thinking bubble beside or immediately above the control. The bubble explains:

1. What the action is.
2. Why people use it.
3. What will happen next.
4. What evidence will determine success.

When OFF, hide the explanatory bubbles and keep the dashboard in zero-noise mode.

The informative layer is read-only. It MUST NOT mutate workflow state, authorize actions, or create verification evidence.

## PUSH EXPLANATION

For the button `PUSH TO GITHUB`, show this exact concise explanation when APEX INFORMATIVE is ON:

> **What is PUSH?** PUSH sends your committed changes to the connected GitHub repository. People use PUSH to put their saved Git changes on the remote repository so connected systems such as Vercel can receive the new commit and start their deployment workflow.

Then show the lifecycle visually:

`READY → PUSHING → PUSHED → DEPLOYING → VERIFYING → VERIFIED`

Never skip states merely because an AI response says “done.”

## GABBY NAVIGATION

Gabby is a floating navigation assistant, not a replacement for the dashboard.

If the owner types:

- `Take me to Stripe`
- `Show me BigQuery`
- `Open Vercel`
- `Show me the current deployment`
- `Show me revenue`

resolve the request to the best available verified deep link and navigate there without requiring manual scrolling.

Use the existing deep-link hierarchy:

1. exact verified admin deep link
2. exact customer/storefront URL
3. platform search route
4. nearest parent route with explicit guidance
5. generic homepage only as final fallback

If a target cannot be verified, say so and provide the closest safe route rather than inventing a URL.

## OWNER / CUSTOMER SWITCH

Provide a clear owner/customer mode switch.

OWNER mode exposes build, deployment, provider management, verification, terminal shortcuts, and internal operational status.

CUSTOMER mode exposes only customer-safe commerce/product/service experiences. Never expose secrets, tokens, internal evidence, deployment controls, or private owner tooling.

## NO-FAKE-GREEN

Green is allowed ONLY after independent verification evidence passes.

For Vercel:

- Git commit exists
- Vercel deployment exists
- deployment is READY
- production target/alias is identified
- live URL responds successfully
- application evidence is present

404, ERROR, QUEUED, timeout, missing evidence, or incomplete streams cannot be GREEN.

Model-generated text cannot mutate status.

## VERCEL TERMINAL PANEL

Add a copyable terminal panel for:

```bash
npm i -g vercel
vercel login
vercel
vercel --prod
```

AI-agent support:

```bash
# Claude Code / Cursor
npx plugins add vercel/vercel-plugin

# Other supported agents
npx skills add vercel-labs/agent-skills
```

Do not claim that clicking a browser control installed a CLI on the owner's computer. The UI must explain that these are terminal commands.

## REVENUE-FIRST NEXT ACTIONS

Surface the next operational actions in this order:

1. custom domain
2. environment variables
3. Vercel Functions/webhooks
4. Stripe checkout verification
5. Shopify commerce verification
6. Google Cloud/BigQuery/Vertex verification
7. runtime/deployment health

Do not expose secret values. Use Vault/Gatekeeper references.

## ACCEPTANCE TESTS

- APEX INFORMATIVE can be turned ON/OFF without resetting workflow state.
- PUSH has an explanatory bubble when ON and no bubble when OFF.
- Informative text never turns a status green.
- Owner/customer switching preserves the current route/workflow state.
- Gabby can navigate by provider name without manual scrolling.
- Every provider tile has a visible name and recognizable logo/avatar.
- Direct links are actual configured/verified links, not placeholders.
- Vercel deployment state is rendered from observed deployment evidence.
- 404/ERROR/QUEUED states remain non-green.
- Responsive layout works on phone and desktop.
- No credentials appear in UI, chat, logs, or informative bubbles.

Finish by running the project's normal build/test workflow and report observed evidence. Do not report PASS unless the evidence exists.
