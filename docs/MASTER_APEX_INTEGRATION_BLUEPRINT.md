# APEX Master Integration Blueprint

## Canonical application root

- Repository: `rahmaanherman-source/Apex-Hub`
- Branch: `main`
- Frontend root: `/`
- Frontend source: `/src`
- Backend service: `/backend`
- Integration definitions: `/integrations`
- Evidence/architecture: `/docs`

## Non-negotiable execution rule

A UI label, deployment dashboard, provider status, or generated response is not proof of execution.

A capability can become GREEN only after:

`DISCOVERED -> AVAILABLE -> AUTHORIZED -> CONNECTED -> HEALTHY -> EXECUTABLE -> VERIFIED`

Every external operation must record enough evidence to distinguish:

- unavailable
- configured
- attempted
- succeeded
- independently verified

No fake success, fake revenue, fake inventory, fake deployment, or fake verification.

## System layers

1. **APEX Hub** — canonical control surface.
2. **Connector layer** — authenticated provider actions.
3. **Truth Gate** — evidence and verification state.
4. **Commerce** — Shopify, Stripe, PayPal, Printify and related revenue flow.
5. **AI** — OpenAI, Google Cloud/Vertex, Hugging Face and authorized model providers.
6. **Data** — Supabase and other authorized data stores.
7. **Analytics** — PostHog and warehouse/analytics providers.
8. **Code/deployment** — GitHub, Vercel, Firebase/Google Cloud and Cloudflare where configured.
9. **Operations** — ClickUp, Linear, Slack, Teams, Notion, Airtable and related systems when authorized.
10. **Evidence** — immutable audit records for every important action.

## Revenue verification chain

`Product -> Storefront -> Checkout -> Payment Provider -> Webhook -> Order -> APEX Revenue Record -> Reconciliation -> VERIFIED`

A deployment marked Live is not sufficient. A sale must be observed through the complete chain.

## Repository rule

Do not turn every repository into a deployment. Classify each repository as one of:

- canonical application
- backend service
- connector/integration
- security/truth/evidence
- data/memory
- documentation/specification
- specialized executable
- archived/experimental

Only canonical production services receive production deployment authority.

## Current APEX-Hub repair gate

The frontend is a React/Vite application rooted at `/`. The backend must use the conventional Python module path `backend/main.py` because the Docker runtime invokes `backend.main:app`.

The backend must contain all routers imported by `backend/main.py`, and its Python dependencies must be declared in `backend/requirements.txt`.

## Verification standard

Before declaring a release complete:

- build succeeds
- typecheck succeeds
- lint succeeds or documented findings are resolved
- backend imports successfully
- backend health endpoint responds
- frontend loads
- browser console has no unexpected errors
- every interactive control has a real action
- external integrations report truthful state
- revenue path is tested end-to-end before revenue is marked verified
