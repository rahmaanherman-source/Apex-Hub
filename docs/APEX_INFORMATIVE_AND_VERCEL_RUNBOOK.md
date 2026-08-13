# APEX INFORMATIVE + VERCEL RUNBOOK

Version: 2026-08-12
Status: CANONICAL OWNER-UX SPEC

## 1. APEX INFORMATIVE

`APEX INFORMATIVE` is an optional explanation layer for the owner/operator dashboard.

- ON: actions expose a small floating explanation bubble next to the relevant control.
- OFF: explanations are hidden and the dashboard operates in zero-noise mode.
- Informative text never changes application state.
- Informative text never authorizes an action.
- Informative text never creates a GREEN/VERIFIED state.

### Example: PUSH

**Button:** `PUSH TO GITHUB`

**Informative bubble:**
> Push means sending the committed changes from this working copy to the connected GitHub repository. After the push, the connected deployment system may build and deploy that commit.

**Reason:** People use PUSH to send their saved Git changes to the remote repository so other systems, such as a connected Vercel deployment, can receive the new commit.

### Action lifecycle

`READY → CONFIRM → PUSHING → PUSHED → DEPLOYING → VERIFYING → VERIFIED`

Any failed, timed-out, or incomplete step remains RED/YELLOW according to the Truth Engine. Never infer success from model text.

## 2. OWNER DASHBOARD

The owner view is the command center. It must support:

- provider logo/face + provider name
- one-tap launch to the exact provider or verified deep link
- provider status
- informative bubble toggle
- owner/customer view switch
- Gabby floating navigation
- command/chat navigation such as `Take me to Stripe`, `Show me BigQuery`, `Open the current Vercel deployment`, or `Show revenue path`
- terminal shortcuts for supported operations
- responsive phone + desktop layout

The customer view is separate from the owner view and must not expose owner-only credentials, controls, deployment actions, or internal evidence.

## 3. NO-FAKE-GREEN RULE

A button, halo, badge, or status indicator may show GREEN only when the underlying operation has independently verifiable evidence.

For deployment:

1. Git commit exists.
2. Vercel deployment exists.
3. Deployment reaches READY.
4. Production target/alias is identified.
5. Live URL returns a successful HTTP response.
6. Application evidence is present.

A deployment page returning 404 is not GREEN.

## 4. VERCEL OWNER WORKFLOW

Terminal setup:

```bash
npm i -g vercel
vercel login
vercel
```

Production deployment:

```bash
vercel --prod
```

For Claude Code or Cursor:

```bash
npx plugins add vercel/vercel-plugin
```

For Cline, Windsurf, GitHub Copilot, and other supported agents:

```bash
npx skills add vercel-labs/agent-skills
```

The APEX dashboard should present these as copyable terminal actions, not pretend that a browser button has installed software on the owner's machine.

## 5. VERCEL NEXT STEPS FOR APEX

Priority order:

1. Custom domain for the owner/customer entry point.
2. Environment variables through Vercel's environment configuration; never place secrets in source code.
3. Vercel Functions for server-side provider operations and webhook receivers.
4. Stripe checkout/webhook verification.
5. Shopify commerce verification.
6. Google Cloud/BigQuery/Vertex connector verification.
7. Deployment health and runtime error monitoring.

## 6. COMMAND SEMANTICS

`PUSH` = send committed local changes to the remote Git repository.

`DEPLOY` = create a Vercel deployment from the project source.

`VERIFY` = observe independent evidence that the requested operation completed successfully.

`GREEN` = verification gates passed; it is never synonymous with "the AI said done."

`APEX INFORMATIVE` = explanation-only UI layer that can be switched OFF.

`GABBY NAVIGATE` = resolve a named service/action to the best available verified deep link and take the owner there without requiring manual scrolling.

## 7. SAFETY BOUNDARY

Credentials remain behind the Vault/Gatekeeper. The owner dashboard may expose a provider launch link and connection status, but never display secret keys, access tokens, or private credentials in the UI, chat transcript, logs, or informative bubbles.
