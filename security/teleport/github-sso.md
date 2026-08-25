# Teleport GitHub SSO Integration

Teleport may be used as the infrastructure identity and RBAC enforcement plane for APEX.

## Intended flow

GitHub organization/team membership → Teleport authentication connector → Teleport roles → short-lived identity → APEX infrastructure/MCP access.

## Role mapping contract

Use GitHub organization/team slugs. Recommended APEX role classes:

- `apex-admin`: tightly controlled infrastructure administration.
- `apex-engineer`: application and deployment operations.
- `apex-operator`: bounded operational actions.
- `apex-auditor`: read-only audit/observability.
- `apex-agent`: machine/agent identity with least privilege.

## Security requirements

- Default deny for new capabilities.
- Explicit allow lists for servers and tools.
- Explicit deny rules for destructive capabilities.
- Short-lived identities where supported.
- Human approval for high-risk operations.
- Full audit context for authentication, authorization, invocation, and denial events.

## OAuth boundary

GitHub OAuth client IDs, client secrets, Teleport identity files, and any provider credentials are runtime secrets and MUST NOT be committed here.

The exact callback URL, organization slug, team mappings, proxy address, and Teleport version are deployment-specific runtime configuration.

## Verification

A Teleport SSO setup is only considered VERIFIED after:

1. GitHub authentication succeeds.
2. Team claims map to the expected Teleport role.
3. Expected APEX access succeeds.
4. An unauthorized action is denied.
5. The authorization result is visible in audit evidence.
6. Short-lived credential/session behavior is confirmed where applicable.
