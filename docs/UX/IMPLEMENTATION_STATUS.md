# APEX UX — Implementation Status Contract

## Status model

| Status | Meaning |
|---|---|
| SPEC | Defined by UX/design contract; not yet implemented |
| IN_PROGRESS | Implementation work has started |
| VERIFIED | Implemented and tested with evidence |
| BLOCKED | Cannot proceed because a dependency or failure remains |
| NOT_CONFIGURED | Capability is intentionally defined but not connected |

## Evidence rule

A status must describe the actual state of the feature, not the desired state.

A document, mockup, screenshot, or agent assertion alone does not establish VERIFIED.

### Minimum VERIFIED evidence

Depending on feature type, record:
- test performed
- date/time
- environment
- result
- relevant commit/deployment identifier
- failure details when applicable

## Current UX architecture baseline

| Surface | UX contract | Initial status |
|---|---|---|
| APEX Hub | Ecosystem benchmark + density doctrine | SPEC |
| Flora Plug | Dynamic reasonable density | SPEC |
| Apex Creator | Progressive density | SPEC |
| Apex Trades | Contextual first fold | SPEC |
| Future APEX apps | Shared contract template | SPEC |

This table tracks UX architecture status only. It must not be interpreted as product/runtime verification.

## Agent rule

Antigravity and other agents must not upgrade SPEC, IN_PROGRESS, BLOCKED, or NOT_CONFIGURED to VERIFIED without executing the relevant test and recording evidence.
