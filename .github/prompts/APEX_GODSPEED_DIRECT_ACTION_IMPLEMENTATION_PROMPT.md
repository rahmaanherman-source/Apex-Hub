# APEX GODSPEED — DIRECT ACTION IMPLEMENTATION PROMPT

Paste this entire prompt into the connected APEX build/coding agent.

---

## ROLE

You are implementing an additive capability inside the existing `rahmaanherman-source/Apex-Hub` repository.

You are NOT designing a new platform.
You are NOT replacing APEX.
You are NOT creating duplicate infrastructure.

The canonical architecture already exists.

Your job is to inspect the current repository, identify the existing implementations for the requested capabilities, and extend them safely.

## PRIMARY OBJECTIVE

Implement and integrate the APEX GODSPEED Direct Action / Computer Use / AI Operator model defined in:

`docs/APEX_GODSPEED_DIRECT_ACTION_ADDENDUM.md`

The operating principle is:

> THE OWNER SHOULD NOT HAVE TO HUNT.

The owner speaks or types an intent. APEX resolves the exact service/resource/problem/action, chooses the best authorized execution method, executes or guides, verifies the resulting state, returns to APEX, and records the evidence.

## ABSOLUTE NON-NEGOTIABLES

1. Preserve the existing APEX architecture.
2. Do not create a second APEX.
3. Do not create a second Gabby.
4. Do not create a second Vault.
5. Do not create a second Truth system.
6. Do not create a second Catalog.
7. Do not create a second Queue system.
8. Do not create a second Orchestrator.
9. Do not create a parallel service registry if one already exists.
10. Do not rewrite functioning infrastructure merely to fit this feature.
11. Inspect the repository before changing code.
12. Reuse existing components before adding new ones.
13. Never expose credentials, tokens, private keys, cookies, or secret values.
14. Never claim an external action succeeded merely because local code exists or an API returned HTTP 200.
15. Every external success claim requires post-action verification.
16. Do not invent service capabilities, deep links, quotas, balances, or UI controls.
17. Never fabricate screen coordinates.
18. Never silently convert free execution into paid execution.
19. Preserve task continuity when the owner must leave APEX.
20. Keep the implementation additive and backwards compatible.

## PHASE 1 — INSPECT FIRST

Before writing code, inspect:

- repository structure
- APEX_ONE_SLAB
- master build specification
- existing service registry
- existing capability registry
- existing orchestration layer
- existing Gabby/operator interface
- existing Vault/Gatekeeper references
- existing Truth/verification layer
- existing queue/job system
- existing audit/telemetry system
- existing deep-link/navigation utilities
- existing API routes
- existing UI pages/components
- existing provider integrations
- existing model router/cost governor

Search for existing implementations using terms such as:

`operator`
`action-card`
`provider`
`capability`
`service-registry`
`deep-link`
`truth`
`verification`
`gabby`
`orchestrator`
`vault`
`gatekeeper`
`queue`
`task continuity`
`computer use`
`browser`
`execution`

Create no duplicate implementation if an equivalent already exists.

## PHASE 2 — CAPABILITY MODEL

Extend the existing service/provider registry, if present, so each provider can advertise verified capabilities.

Minimum conceptual fields:

```text
provider
account_ref
resource_ref
authorization_state
capabilities
api_capable
browser_capable
computer_use_capable
local_capable
deep_link_capable
cost_class
quota_state
last_verified_at
health
truth_state
```

Do not store secret values in this registry.

Capability states must distinguish:

`DISCOVERED`
`AVAILABLE`
`AUTHORIZED`
`VERIFIED`
`UNAVAILABLE`
`UNKNOWN`

Never infer `VERIFIED` from `DISCOVERED`.

## PHASE 3 — EXECUTION ROUTER

Implement or extend the existing execution router.

Selection priority:

```text
APEX NATIVE ACTION
→ AUTHORITATIVE API
→ CONNECTED TOOL
→ AUTHORIZED LOCAL TERMINAL
→ AUTHORIZED BROWSER/COMPUTER-USE AGENT
→ VERIFIED EXACT DEEP LINK + OWNER GUIDANCE
→ MANUAL INSTRUCTIONS
```

Choose the safest and most reliable authorized path.

If an API can perform the operation reliably, prefer it over UI automation.

If an action is only available through the UI, use an authorized browser/computer-use capability if one actually exists.

If neither exists, open the exact verified destination and guide the owner.

## PHASE 4 — INTENT TO EXACT ACTION

Gabby/operator input must resolve through:

```text
OWNER INTENT
↓
TASK CLASSIFICATION
↓
SERVICE
↓
ACCOUNT
↓
PROJECT/RESOURCE
↓
ACTUAL ERROR OR STATE
↓
EXACT DESTINATION
↓
EXACT ACTION
↓
EXECUTION PROVIDER
↓
EXECUTE OR GUIDE
↓
VERIFY
↓
RETURN TO TASK
```

Example:

Owner says:

`"Vercel failed again. Fix it."`

APEX should not simply open Vercel.

It should resolve:

```text
SERVICE: Vercel
ACCOUNT: verified account reference
PROJECT: APEX Hub
RESOURCE: failed deployment
ERROR: actual build/deployment error
ACTION: repair/redeploy if authorized
DESTINATION: exact deployment/log/resource page
```

## PHASE 5 — EXACT DESTINATION ENGINE

Create or extend the existing contextual destination model.

A destination should support:

```text
service
account_ref
project
resource
page
url
deep_link
action
requires_auth
auth_state
capability
last_verified_at
status
```

Do not fall back to generic homepages when a verified contextual destination is available.

If a provider does not expose a stable deep link, record the limitation and provide the most precise verified route possible.

## PHASE 6 — DIRECT ACTION CARD

Use the existing APEX UI/design system.

Do not invent a second dashboard.

Add a compact action card capable of displaying:

```text
SERVICE
ACCOUNT
RESOURCE
PROBLEM
STATUS
EXACT DESTINATION
ACTION
CAN APEX EXECUTE?
OWNER ACTION REQUIRED?
VERIFICATION
```

Buttons/actions where applicable:

```text
EXECUTE
OPEN EXACT PAGE
SHOW ME
VERIFY
RETURN TO TASK
```

All buttons must call real application behavior or be disabled with an explicit reason.

Do not create decorative controls that do nothing.

## PHASE 7 — TASK CONTINUITY

Every external task must preserve a resumable task context.

Minimum state:

```text
original_task_id
original_intent
current_step
blocked_step
required_input
source_destination
provider
authorization_state
resume_action
verification_requirement
status
```

Example:

```text
TASK: Fix Shopify connection
BLOCKED: required provider value missing
DESTINATION: exact Shopify source page
OWNER ACTION: obtain value
RESUME: apply value → test → verify Shopify connection
```

When the owner returns, resume the original task rather than creating a new unrelated task.

## PHASE 8 — COMPUTER/BROWSER USE

Support computer/browser execution only when a connected provider explicitly exposes that capability and authorization exists.

Allowed operations include:

- inspect visible UI
- locate controls
- identify visible errors
- locate forms
- locate settings
- compare expected and actual UI state
- guide owner
- perform authorized actions

Never invent controls or coordinates.

If the interface cannot be reliably interpreted, stop the visual action and fall back to the exact verified destination plus human guidance.

## PHASE 9 — VALUE RESOLUTION

When a service requires a value, search existing authorized sources first:

```text
APEX DATABASE
→ VAULT REFERENCE
→ SERVICE REGISTRY
→ CONFIGURATION
→ CANONICAL CATALOG
→ CONNECTED PROVIDER
→ AUTHORIZED REPOSITORY
```

If found:

- use it through the authorized execution path
- do not display the secret
- do not log the secret

If missing:

```text
IDENTIFY VALUE
→ IDENTIFY SOURCE
→ OPEN EXACT SOURCE
→ OWNER OBTAINS VALUE
→ RETURN
→ APPLY
→ TEST
→ VERIFY
```

## PHASE 10 — AUTHORIZATION

Automatically permitted when connected and authorized:

- read-only inspection
- health checks
- status checks
- diagnostics
- log analysis
- code analysis
- tests
- safe validation
- queue inspection
- preauthorized retries

Require explicit owner approval before:

- financial transactions
- purchases
- ad spend
- campaign launch
- destructive deletion
- production asset deletion/replacement
- price changes
- account closure
- security downgrades
- other materially consequential external actions

Never bypass an authorization boundary merely because an agent has browser access.

## PHASE 11 — VERIFY EVERYTHING

Implement verification after every consequential external operation.

Required pattern:

```text
REQUESTED
↓
EXECUTED
↓
REMOTE STATE CHECK
↓
EXPECTED STATE?
├── YES → VERIFIED
└── NO → FAILED / RECOVERY
```

Example:

A deployment API returns a deployment ID.

That is not proof that the application is live.

The system must verify the deployment's actual state and, where appropriate, the reachable application/health endpoint.

## PHASE 12 — TRUTH STATES

Preserve these as separate states:

```text
EXISTS
CONNECTED
AUTHORIZED
FUNCTIONAL
EXECUTED
ACCEPTED
DEPLOYED
LIVE
VERIFIED
PERFORMING
PROFITABLE
```

Do not collapse them into a single boolean.

## PHASE 13 — FAILURE RECOVERY

On failure:

1. Preserve state.
2. Capture actual error.
3. Classify it.
4. Identify responsible service/resource.
5. Determine whether APEX can safely repair it.
6. Repair when authorized.
7. Retry only when safe/idempotent.
8. Resolve exact owner destination when human action is required.
9. Resume original task.
10. Verify final state.

Action cards must show the actual blocker, not a generic error.

## PHASE 14 — LOCAL/FREE-FIRST COST GOVERNOR

Use:

```text
LOCAL
→ VERIFIED FREE
→ INCLUDED
→ LOWEST-COST CAPABLE
→ PREMIUM
```

Before any paid execution:

- inspect local capability
- inspect verified free quota
- inspect included capacity
- inspect lower-cost capable providers
- calculate/estimate cost when possible
- show why payment is required
- obtain required approval

If quota cannot be verified:

`BALANCE_UNKNOWN`

Never invent a free balance or reset date.

## PHASE 15 — MODEL ROUTING

Use actual measured task fit.

Track:

```text
provider
model
capability
speed
quality
coding
reasoning
vision
voice
tool_use
context
cost
availability
local/free/included/paid
last_test
```

Route each task to the best verified capable provider rather than automatically choosing the largest model.

## PHASE 16 — COMMERCE INTEGRATION

Do not create a separate commerce path.

Use the existing APEX flow:

```text
CANONICAL CATALOG
→ SHOPIFY
→ STOREFRONT
→ CHECKOUT
→ STRIPE
→ WEBHOOK
→ APEX
→ VERIFIED ORDER
```

For the 2,000-product publication:

1. locate canonical source
2. validate schema/media/variants/pricing/availability/identifiers
3. resolve existing Shopify connection
4. verify authorization/scopes
5. publish controlled test set
6. verify remote products
7. verify storefront
8. verify cart
9. perform safe checkout test
10. verify Stripe
11. verify webhook
12. verify APEX order/event state
13. only then enqueue bulk publication
14. report requested/queued/completed/failed/retryable
15. never silently truncate

## PHASE 17 — AUDIT/EVIDENCE

Record non-secret evidence for each action:

```text
task_id
timestamp
actor
provider
capability
requested_action
actual_action
source_reference
before_state
after_state
truth_state
verification_result
retry_state
cost_class
owner_approval_state
```

Do not record secret values.

## PHASE 18 — TESTING

Add/update tests for:

### Unit
- capability resolution
- execution priority
- deep-link selection
- authorization boundary
- truth-state transitions
- task continuity
- cost routing
- secret redaction

### Integration
- provider registration
- action-card creation
- execute endpoint
- verify endpoint
- return-to-task state
- failure recovery

### End-to-end
- owner intent → exact destination
- owner intent → authorized execution → verification
- missing value → exact source → resume task
- failed operation → repair → verify
- unavailable provider → fallback provider
- unknown quota → BALANCE_UNKNOWN

### UI
Every rendered action control must either:

1. execute a real action,
2. navigate to a verified destination,
3. trigger verification,
4. return to the active task,
5. or be disabled with a truthful explanation.

No dead buttons.

## PHASE 19 — BUILD/DEBUG

Run the repository's existing formatter, linter, type checks, unit tests, integration tests, and build commands.

Do not invent a new toolchain when an existing one is present.

If a build fails:

`ACTUAL ERROR → ROOT CAUSE → MINIMAL REPAIR → TEST AGAIN`

Do not mask errors.

## PHASE 20 — DOCUMENTATION

Update only the necessary canonical documentation.

Required:

- `docs/APEX_GODSPEED_DIRECT_ACTION_ADDENDUM.md`
- relevant existing architecture/spec documents
- relevant service/capability documentation
- relevant runbook/test documentation

Do not create redundant documentation systems.

## PHASE 21 — FINAL ACCEPTANCE GATE

Do not claim complete until all applicable checks are supported by evidence:

```text
[ ] Existing architecture inspected
[ ] Existing registry reused/extended
[ ] Existing Gabby reused
[ ] Existing Vault reused
[ ] Existing Truth system reused
[ ] Existing Queue reused
[ ] Provider capabilities discoverable
[ ] Execution routing works
[ ] Exact destinations work
[ ] Task continuity works
[ ] Owner authorization boundaries work
[ ] Secret redaction verified
[ ] API-first routing verified
[ ] Browser/computer-use fallback is capability-gated
[ ] Action cards are functional
[ ] No dead buttons
[ ] Post-action verification works
[ ] Failure recovery works
[ ] Cost governor works
[ ] Commerce path remains intact
[ ] Tests pass
[ ] Build passes
[ ] Documentation updated
[ ] Git diff reviewed
```

## FINAL RESPONSE FORMAT

After implementation, report exactly:

### IMPLEMENTED
What was actually changed.

### REUSED
Existing APEX systems reused.

### FILES CHANGED
Exact paths.

### TESTS
Exact commands/results.

### VERIFIED
Only behavior actually verified.

### NOT VERIFIED
Anything that requires live credentials, external services, browser/computer-use access, deployment, or other unavailable runtime evidence.

### NEXT BLOCKER
One highest-priority blocker only.

Never use phrases such as "fully complete", "zero-fail", or "production ready" unless the corresponding external/runtime evidence actually exists.

**PRESERVE → CONNECT → EXECUTE → GUIDE → VERIFY → RETURN → CONTINUE.**
