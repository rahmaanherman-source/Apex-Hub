# APEX GODSPEED / SENTINEL / LIGHTSPEED FORGE / GOLDEN WORLD — SOURCE RECONCILIATION

Status: SOURCE-INGESTED / NOT PRODUCTION-VERIFIED

## Purpose

This document records the four security/packaging/code slabs supplied for consolidation:

1. APEX GODSPEED Flutter Native Wrapper
2. APEX SENTINEL Chrome Extension
3. LIGHTSPEED FORGE standalone HTML
4. GOLDEN WORLD Unity C# World Engine

The source also includes research claims concerning WebAuthn, biometrics, secure hardware, authenticated encryption, and post-quantum cryptography.

## Canonical ownership / placement

| Source | Owning repository | Role |
|---|---|---|
| APEX GODSPEED wrapper / command surface | APEX-TERMINAL + Apex-Breeze | execution surface + mobile control surface |
| APEX SENTINEL extension | Apex-Sentinel | monitoring/security layer |
| LIGHTSPEED FORGE | LightSpeed-Forge | file intake, hashing, packaging, chain-of-custody utility |
| GOLDEN WORLD Unity rules | Golden World implementation repository to be confirmed; architecture referenced from Apex-Hub | game/world engine |
| biometric/security research | Apex-Hub + Truth-Gate- + Apex-Omni-Vaulta | policy, verification, credential/security architecture |

## Evidence-state policy

The supplied slabs may be runnable or structurally complete, but the repository must not treat them as production verified merely because they contain code or print a SHA-256 checksum.

Required ladder:

DEFINED → IMPLEMENTED → RUNNING → TESTED → READ-BACK VERIFIED → PRODUCTION VERIFIED

## Critical findings to preserve

### APEX GODSPEED

- The wrapper creates a Flutter project and embeds the supplied HTML in a WebView.
- The browser layer uses local storage, WebAuthn/platform authenticator probing, SHA-256 hashing, ZIP packaging, Pyodide, speech APIs, and device profiling.
- The supplied PIN fallback `1111` is a development convenience and must not be treated as production authentication.
- A self-computed page hash or device fingerprint is an integrity signal, not a cryptographic root of trust.
- CDN-loaded JS/Pyodide dependencies create external supply-chain/runtime dependencies and must be reviewed before a sovereign/offline claim.

### APEX SENTINEL

- Manifest V3 extension source is a prototype security monitor.
- URL substring matching is not a malware detector and must not be described as comprehensive protection.
- Extension permission review is useful but should be treated as advisory until independently tested.
- `webRequest`/blocking behavior, manifest permissions, and Chrome-version compatibility require current runtime verification.

### LIGHTSPEED FORGE

- SHA-256 file hashing and a combined vault hash provide tamper-evident evidence, not immutable storage.
- The chain-of-custody display is locally generated and can be altered with local application state.
- The supplied malware scan is heuristic and must not be represented as a complete malware scanner.
- ZIP creation is packaging; it is not a secure archival system by itself.

### GOLDEN WORLD

- The Unity source defines a ZoneData asset and WorldDesignRuleEngine.
- The supplied `AbilitySystem` currently returns `true` for ability/power checks, so this is a rule-engine scaffold rather than an enforced progression system.
- Actual Unity project integration, gameplay verification, safety controls, curriculum integration, and multiplayer/world systems remain separate implementation work.

## Security architecture alignment

Canonical APEX pattern:

VAULT → GATEKEEPER → AUTHORIZED USE → EXECUTION → READ-BACK → VERIFIED EVIDENCE

Biometric authentication should unlock a device-bound authenticator or authorization ceremony; raw biometric data must not become application secrets or durable conversational memory.

The repository must distinguish:

- identity proof
- device possession
- authorization
- cryptographic key material
- biometric template handling
- audit evidence

These are related but not interchangeable claims.

## External-platform references

The supplied source explicitly requested GitHub, Vercel, and Hugging Face involvement. Current connected platform state should be recorded separately from code provenance:

- GitHub: repositories and source provenance
- Vercel: deployment/project state
- Hugging Face: model/research discovery only when an actual model or research dependency is selected

No external deployment or model dependency is considered verified merely because a platform is available.

## Canonical rule

KEEP THE SOURCE. SEPARATE THE CLAIM. TEST THE IMPLEMENTATION. PRESERVE THE EVIDENCE. NEVER PROMOTE A SIMULATION, PLACEHOLDER, LOCAL HASH, UI STATUS, or code comment to GREEN without runtime evidence.
