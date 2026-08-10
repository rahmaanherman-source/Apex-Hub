# GODSPEED Event Schema

## Purpose

Canonical wire contract for APEX Godspeed lifecycle events consumed by Gabby state and avatar rendering.

## Event shape

Required:

- `type`: string

Optional:

- `job_id`: string
- `phase`: one of `queued`, `started`, `streaming`, `toolCall`, `awaitingOwner`, `succeeded`, `failed`, `cancelled`
- `progress`: number from `0` through `1`
- `section`: one of `reasoning`, `plan`, `logs`, `progress`, `result`, `next`
- `text`: non-secret display text
- `partial`: boolean
- `error_code`: non-secret error identifier
- `meta`: sanitized metadata

## Security

`meta` and Gabby-visible detail MUST NOT contain keys or values exposing credentials, secrets, passwords, tokens, API keys, private keys, refresh tokens, access tokens, or equivalent authentication material.

Never expose raw malformed payloads to the UI or logs when they may contain secrets.

## Unknown event types

Unknown event types may be parsed for transport compatibility but MUST NOT invent or change Gabby's visual state.

## Truth rule

LLM/model prose such as `done`, `finished`, `complete`, or `success` is not a lifecycle signal and MUST NOT change Gabby's visual state.

Visual state must derive from a validated event type and/or explicit validated phase.

## Phase precedence

1. Explicit validated phase, when present.
2. Known event type mapping.
3. Previous state.

The server SHOULD emit matching type and phase values.

## Canonical Gabby mapping

| Event | Phase/state | Gabby state | Color |
|---|---|---|---|
| `job.queued` | queued | active | Blue |
| `job.started` | started | active | Blue |
| `job.progress` | streaming | active | Blue |
| `job.log` | streaming | active | Blue |
| `job.section` | streaming | active | Blue |
| `job.awaiting_owner` | awaitingOwner | attention | Yellow |
| `vault.attention` | — | attention | Yellow |
| `memory.refresh` | — | memory | Purple |
| `memory.done` | — | ready | Green |
| `job.succeeded` | succeeded | ready | Green |
| `job.failed` | failed | error | Red |
| `job.cancelled` | cancelled | neutral | White |

## Streaming rule

An SSE stream that ends without `job.succeeded`, `job.failed`, or `job.cancelled` MUST NOT produce Ready/Green state. It remains active or transitions to the configured incomplete/attention state according to timeout policy.

## Invalid payload rule

Malformed JSON or structurally invalid events MUST NOT crash the SSE stream. The client should emit a safe non-secret diagnostic through the existing telemetry/event path when available and continue processing subsequent events.

## Transport rule

HTTP 429, HTTP 5xx, timeout, and transient network failures use the existing retry policy. Retries MUST be bounded. Exhausted transport retries become a verified failure state.
