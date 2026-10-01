# APEX PRIVATE Mode

APEX PRIVATE mode is an explicit user-controlled privacy lane for personal data used during local testing.

## Contract

- Toggle state is visible as `PRIVATE: ON` or `PRIVATE: OFF`.
- While OFF, personal-data values cannot be inserted into the private lane.
- While ON, values such as a phone number or email are accepted by the local private-data boundary and represented to normal UI/evidence as masked metadata only.
- A short-lived lease is created for each use. Default lease TTL is **60 seconds**.
- A lease is single-use and bound to its declared purpose. After consumption it is destroyed.
- Expired or invalid leases cannot be consumed.
- The private value must not be written to logs, telemetry, source, normal chat responses, or ordinary status output.
- Verification evidence uses masked metadata or a non-secret fingerprint, never the value itself.
- The local Gatekeeper is the intended persistence/release boundary. This module does not make cloud transmissions by itself.

## Test model

For local APEX tests, the operator can store their own test phone/email under PRIVATE mode and use that data to exercise the phone/email delivery path. This avoids requiring a third party during functional testing.

A test should record only:

- test kind (`phone` or `email`)
- purpose
- lease id
- masked value
- delivery result
- timestamp
- non-secret fingerprint where useful

The actual value is supplied to the authorized local test adapter only during the 60-second lease window.

## GitHub device authorization

The URL `https://github.com/login/device` is a GitHub device-authorization verification page. A local APEX terminal may open it when a compatible GitHub device-flow client has already generated a one-time user code. The APEX private lane should never store or log the device code or access token in ordinary application logs. GitHub documents that the device flow uses a user code entered at that URL and then polls until authorization succeeds or the code expires.
