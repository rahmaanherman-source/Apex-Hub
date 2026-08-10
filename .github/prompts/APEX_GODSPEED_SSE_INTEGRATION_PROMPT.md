# APEX GODSPEED — SSE / Gabby Integration Prompt

## Mission

Integrate the Godspeed SSE client and strict event contract into the existing APEX Hub architecture. Preserve existing systems. Do not create a second APEX, Gabby, Vault, Truth system, CommandBus, memory system, catalog, orchestrator, or duplicate reducer.

## Required workflow

INSPECT → MAP EXISTING CODE → REUSE → INTEGRATE → BUILD → TEST → COMMIT → DEPLOY → LIVE VERIFY

## SSE

Endpoint:

`POST /api/v1/godspeed/command`

Headers:

`Accept: text/event-stream`
`Content-Type: application/json`

Support:

- SSE data parsing
- comments/heartbeat handling
- strict event validation
- HTTP 429 and 5xx retry
- timeout/network retry
- bounded exponential backoff
- maximum 5 retries by default unless existing APEX configuration overrides it
- 400ms initial delay, doubling with a 15s cap
- terminal transport failure after retries are exhausted
- incomplete streams must never become Ready/Green

## Event contract

Required field:

- `type`: string

Allowed `phase` values:

`queued`, `started`, `streaming`, `toolCall`, `awaitingOwner`, `succeeded`, `failed`, `cancelled`

Allowed `section` values:

`reasoning`, `plan`, `logs`, `progress`, `result`, `next`

`progress` must be numeric and clamped/validated to 0..1.
`partial` must be boolean when present.

Unknown event types may parse but MUST NOT change Gabby's state.

## Gabby state truth

- `job.queued`, `job.started`, `job.progress`, `job.log`, `job.section` → Active / Blue
- `job.awaiting_owner`, `vault.attention` → Attention / Yellow
- `memory.refresh` → Memory / Purple
- `memory.done`, `job.succeeded` → Ready / Green
- `job.failed` → Error / Red
- `job.cancelled` → Neutral / White

Explicit validated phase has precedence over known type mapping, then previous state. Server events should keep type and phase consistent.

LLM prose such as `done`, `finished`, `complete`, or `success` is NEVER a state signal.

## Security

Never expose credentials, API keys, passwords, tokens, access tokens, refresh tokens, private keys, or secret material through Gabby-visible detail, UI, telemetry, or ordinary logs. Malformed payload previews must be sanitized or omitted when safety cannot be established.

## Invalid JSON

A malformed SSE data line must not crash the stream. Handle it through the existing non-secret telemetry/event path when available and continue. Do not convert malformed JSON alone into a false system failure.

## Integration

Connect the validated SSE event stream to the EXISTING Godspeed CommandBus and GabbyStateReducer/provider. Use the same reducer for live SSE and local CommandBus execution. Connect the resulting verified state to the existing Gabby avatar.

Do not create parallel providers or reducers when equivalent existing implementations are present.

## Build and verification

Before committing:

1. Inspect actual package/project structure.
2. Confirm imports and referenced symbols.
3. Check for existing equivalent implementations.
4. Integrate rather than duplicate.
5. Run analyzer/build/tests.
6. Fix errors rather than suppressing them.
7. Do not delete unrelated working code.
8. Confirm the new files exist in the Git repository, not only the workspace.

## Deployment truth

Track separately:

EXISTS
CONNECTED
BUILT
DEPLOYED
LIVE
EXECUTED
VERIFIED

Do not claim LIVE or VERIFIED without runtime evidence.

## Commit

Use the current APEX working branch.

Commit message:

`feat: integrate verified Godspeed SSE and Gabby event state`

If equivalent code already exists, make the smallest safe integration/repair rather than adding duplicates.

## Completion report

Return a concise checklist containing:

- repository inspected
- existing implementation found/reused
- SSE integrated
- schema integrated
- retry/backoff verified
- invalid JSON handling verified
- secret filtering verified
- reducer/avatar wiring verified
- build status
- test status
- commit SHA
- deployment status
- live SSE verification status
- remaining blocker, if any

Never report workspace-only work as repository-complete.
Never report deployment as verified until the live system proves it.
