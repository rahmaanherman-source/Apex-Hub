# GODSPEED COMMANDBUS INTEGRATION EXPLORATION

## Canonical flow

```text
Gabby / Terminal
      |
      +--> Path A: existing Godspeed SSE transport
      |       -> authoritative job execution
      |       -> existing Vault / Cost Governor / tools
      |       -> lifecycle events
      |
      +--> Path B: existing local CommandBus.execute
              -> offline/local handlers

Both paths
      -> existing GodspeedEvent validation
      -> existing GabbyStateReducer
      -> existing Gabby provider/avatar
```

## Responsibilities

### CommandBus

- Natural-language command routing.
- Local/offline handler execution where already supported.
- Selection of the authoritative Godspeed path when a remote job is required.
- No duplicate lifecycle reducer.

### Godspeed transport

- Executes real authorized tools/jobs.
- Emits lifecycle events over the existing SSE endpoint.
- Owns authoritative job phase transitions.

### SSE client

- Parses SSE framing.
- Ignores comments/heartbeats for lifecycle state.
- Validates event JSON against the existing event contract.
- Applies bounded retry/backoff for transient transport failures.
- Detects idle timeout.
- Never declares completion from text alone.

### GabbyStateReducer

- Single source for avatar visual state.
- Explicit validated phase has precedence.
- Known event types provide the fallback mapping.
- Unknown events are ignored.
- `session.ping` is a no-op.

## Heartbeat behavior

Preferred transport heartbeat:

`: ping`

Optional structured heartbeat:

`session.ping`

Neither may turn Gabby green or otherwise alter job lifecycle state.

## Test contract

The real Dart test suite must verify, using the actual package structure and existing classes:

- valid event parsing;
- malformed JSON handling;
- missing `type` rejection;
- invalid phase rejection;
- forbidden secret-key metadata rejection/sanitization;
- `session.ping` reducer no-op;
- started/progress/section -> Active/Blue;
- awaiting owner -> Attention/Yellow;
- memory refresh -> Memory/Purple;
- succeeded -> Ready/Green;
- failed -> Error/Red;
- cancelled -> Neutral/White;
- unknown event -> previous state unchanged;
- explicit phase overriding known type mapping;
- model prose containing `done`/`success` does not force Green;
- incomplete stream does not become Green;
- idle timeout follows the configured transport failure policy;
- retry/backoff is bounded.

## Repository rule

Before adding implementation files, inspect the actual Flutter/package tree and reuse equivalent classes. Do not invent imports or duplicate providers/reducers merely to satisfy this document.
