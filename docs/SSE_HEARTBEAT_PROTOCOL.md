# GODSPEED SSE HEARTBEAT PROTOCOL

## Purpose

Define the heartbeat and idle-timeout contract for the existing APEX Godspeed SSE transport. This is an additive protocol document. It does not create a second SSE transport, CommandBus, reducer, or Truth system.

## Preferred heartbeat

Use an SSE comment heartbeat while a stream remains open:

`: ping`

Recommended interval: approximately 15 seconds, subject to existing server/runtime constraints.

SSE comment heartbeats are transport-level signals only. They MUST NOT change Gabby's visual state, job phase, Truth state, or completion state.

## Optional structured heartbeat

A server may emit:

```json
{"type":"session.ping","job_id":"..."}
```

`session.ping` is informational/transport state only. The existing Gabby reducer MUST return the previous snapshot unchanged for this event.

## Client behavior

The existing SSE client should:

1. Reset its byte/activity timer whenever any valid SSE bytes are received.
2. Ignore comment heartbeat lines for lifecycle-state purposes.
3. Parse `session.ping` only if the existing event contract supports it.
4. Never infer success from heartbeat activity.
5. Never turn an incomplete stream green.
6. Treat approximately 45 seconds without received bytes as `sse_idle_timeout`, unless existing APEX configuration defines a different timeout.
7. Use the existing bounded retry/backoff policy for transient transport failure.
8. After retry exhaustion, emit the existing verified failure state.

## Truth rules

| Signal | Transport effect | Gabby state effect |
|---|---|---|
| `: ping` | Reset activity timer | None |
| `session.ping` | Reset activity timer | None |
| `job.started` | Normal lifecycle event | Active / Blue |
| `job.progress` | Normal lifecycle event | Active / Blue |
| `job.section` | Normal lifecycle event | Active / Blue |
| `job.awaiting_owner` | Normal lifecycle event | Attention / Yellow |
| `job.succeeded` | Terminal success | Ready / Green |
| `job.failed` | Terminal failure | Error / Red |
| `job.cancelled` | Terminal cancellation | Neutral / White |
| stream ends without terminal event | Incomplete | Never Green |
| idle timeout | Transport failure | Existing failure/attention policy; never Green |

## Security

Heartbeat payloads MUST NOT contain credentials, tokens, API keys, passwords, private keys, or other secret material. Comment heartbeats should contain no sensitive data.

## Integration rule

This protocol attaches to the existing:

`SSE client → validated GodspeedEvent → existing GabbyStateReducer → existing provider/avatar`

Do not introduce a parallel reducer or parallel event stream.
