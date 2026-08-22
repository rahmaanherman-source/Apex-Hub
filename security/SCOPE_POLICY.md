# Authorized Security Scope Policy

## Required before active assessment

Every target must have:

- `scope_id`
- `owner_or_customer`
- `authorization_reference`
- `authorized_assets`
- `excluded_assets`
- `allowed_test_classes`
- `start_time`
- `end_time`
- `emergency_stop_contact`

## Scope states

- `DRAFT` — not executable
- `AUTHORIZED` — permitted for the specified window
- `EXPIRED` — execution blocked
- `SUSPENDED` — execution blocked
- `COMPLETED` — assessment closed

## Hard gates

The engine MUST refuse active testing when:

- authorization is absent;
- the target is outside the explicit asset scope;
- the authorization window has expired;
- the requested test class is not permitted;
- an emergency stop is active.

## Evidence

Every executed check records:

- scope ID
- target identifier
- check ID
- execution timestamp
- result state
- evidence reference
- tool/version when applicable
- operator/system identity

Raw credentials and sensitive secrets must never be stored as evidence.
