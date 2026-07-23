# APEX HUB ARCHITECTURE
# Platform Organization

## Purpose

This document defines the structural organization of APEX Hub and its core repositories.

---

## High-Level Structure

- **APEX Hub** — One Hub, command center.  
- **MAC LIFE** — PWA Command Center, user‑facing experience.  
- **TruthGate** — Governance, schemas, manifests, certification.  
- **Apex Platform** — Backend services, Decision Engine, APIs.  
- **Concierge** — Guided workflows, onboarding, automation.  
- **Commerce** — Products, orders, payments, subscriptions.  
- **Cryptopulse** — Market intelligence and signals.  
- **Engine Six** — Automation engine and workflow runtime.  
- **Forge** — Local‑first tools and compute.  
- **Studio** — Media and content pipeline.  
- **Vision** — AI models, inference, registry.  

---

## Decision Engine

All services route decisions through:

- `POST /v1/decisions`

Decision Engine provides:

- trust rating  
- evidence  
- explainability  
- certification path  
- audit trail  

---

## TruthGate

TruthGate owns:

- Constitution  
- manifests  
- schemas  
- governance rules  
- certification standards  

Apex Platform and MAC LIFE must conform to TruthGate.

---

## Global Object Registry

Single registry for:

- object types  
- schemas  
- storage locations  
- search indexes  
- permissions models  
- AI context models  

Powers:

- Universal Search  
- Activity feeds  
- Automation triggers  
- Analytics  
- Governance  

---

## Integration Layer

Adapters for:

- Stripe  
- Shopify  
- Slack  
- Discord  
- GitHub  
- Cloudflare  
- Email/SMS providers  

No direct vendor‑specific logic in core modules.  
All external systems go through adapters.

---

## Environments

- `local`  
- `staging`  
- `production`  

Environment configuration via:

- environment variables  
- secrets manager  
- deployment manifests  

Architecture must remain consistent across environments.
