# GODSPEED ↔ LightSpeed Forge Integration

This document makes `Apex-Hub` the integration/control-plane home while `LightSpeed-Forge` remains the dedicated forge application. The existing Apex-Hub is already the unified Godspeed platform with modular FastAPI routers; this integration adds a security boundary instead of embedding forge secrets or browser trust logic in the hub.

## Boundaries

```text
Apex-Hub
  ├── identity / orchestration / product context
  └── integration contract
          │ HTTPS
          ▼
LightSpeed-Forge
  ├── WebAuthn / passkey authentication
  ├── server-side authorization
  ├── file hashing + canonical manifest
  ├── Vault Root SHA-256
  └── PostgreSQL audit trail
```

## Security rules

- No API keys, database passwords, bootstrap tokens, EINs, or signing secrets in source control.
- Browser state is never an authority boundary.
- WebAuthn challenges are generated and verified server-side.
- Sessions are stored server-side in PostgreSQL and represented in the browser only by an HttpOnly cookie.
- Device fingerprinting is not used as authentication.
- Voice recognition is not used as authentication.
- Client-side malware heuristics are not treated as a security scanner.
- A forge manifest is canonicalized before its Vault Root is computed.
- Every trusted audit is written server-side.

## Integration contract

`LightSpeed-Forge` exposes:

- `GET /health`
- `GET /api/session`
- `POST /api/forge/audit`
- `/auth/*` for passkey registration/authentication

The Hub should call the forge service only through an authenticated service-to-service path in production. Do not add `allow_origins=["*"]` for privileged production endpoints.

## Required production secrets

Provision through Google Secret Manager or an equivalent secret store:

- `DATABASE_URL`
- `SESSION_SECRET`
- `FORGE_BOOTSTRAP_TOKEN` (one-time owner provisioning secret; rotate/disable after registration)
- `WEBAUTHN_RP_ID`
- `WEBAUTHN_ORIGIN`

## What was removed from the prototype

The previous browser design contained hard-coded PIN fallbacks, localStorage trust flags, browser-only device identity, fake biometric success, duplicate HTML documents/scripts, a regex-only malware detector, a client-side network kill switch, and a self-hash that trusted localStorage. Those are presentation features at best and security boundaries at worst. The integration now treats the server as the authority.
