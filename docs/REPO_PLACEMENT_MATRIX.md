# APEX / GODSPEED — SOURCE-TO-REPOSITORY PLACEMENT MATRIX

**Status:** CANONICAL PLACEMENT MAP / SOURCE-INGESTED

## Governing rule

Every supplied artifact belongs to the repository that owns the capability. `Apex-Hub` remains the canonical map/control documentation surface. Existing specialized repositories are preferred over creating duplicate implementations.

**No Fake Green:** placement means ownership/location, not completion. A capability is only VERIFIED after real execution, read-back, and evidence.

## Placement map

| Source / capability | Canonical repository | What belongs there | Status rule |
|---|---|---|---|
| APEX master integration, architecture, governance, truth standards, cross-repo registry | `Apex-Hub` | master docs, capability registry, placement matrix, acceptance criteria, reconciliation records | documentation/integration authority |
| GODSPEED Totality / Omega orchestration | `Apex-Hub` + execution components in `APEX-TERMINAL` | orchestration specs, module registry, verification contracts; executable terminal/control logic in Terminal | do not duplicate engine blindly |
| Gabby universal interface/agent | `Apex-Gabby-` | companion, agent behavior, epistemic validation, interface contracts | runtime proof required |
| Terminal execution/control | `APEX-TERMINAL` | actual commands, project execution, health/read-back, verification ladder | runtime proof required |
| Mobile command surface | `Apex-Breeze` | mobile UI, control surface, device interaction, bridge client | runtime proof required |
| Connection/bridge layer | `Apex-Bridge` | authorized phone/device to runtime connection, transport and command contracts | runtime proof required |
| Security/Sentinel | `Apex-Sentinel` | monitoring, anomaly detection, incident handling, security UI/extension adapters | security tests required |
| Credential vault | `Apex-Omni-Vaulta` | credential references, secure storage contracts, vault integrations | secrets never copied to chat/source/UI |
| Truth verification | `Truth-Gate-` | claim/evidence status, read-back verification, contradiction handling, verification records | evidence required |
| Durable archive/memory | `Apex-Heritage-` | source archive, provenance, durable memory, consolidation records | source preserved; secrets excluded |
| Vision/computer vision | `Apex-Forensic-Vision` | CV/vision adapters, analysis pipelines, evidence capture | real input tests required |
| Studio/audio/video/design | `Apex-Studio-OS-` | studio workflows and asset lifecycle | asset/runtime proof required |
| Product/ecommerce production | `APEX-Omni-Product-Studio` | product creation/catalog assets and production workflow | real product/read-back proof required |
| Commerce intelligence/execution | `Apex-Hub` as integration map; implementation should live in existing commerce/product repo if present | ingestion, scoring, pricing, decision, Shopify/Matrixify, monitoring, learning contracts | first real product loop required |
| Revenue/money engine | `Apex-Hub` integration docs + existing revenue/product implementation home | APEX Flow, ledger, work orders, approval queue, Stripe/Shopify event contracts | real payment/webhook proof required |
| IP/patent automation | `GODSPEED-PATENT-ENGINE-`, `Apex-IP-ENGINE-` | IP workflows, provenance, patent-related artifacts | legal claims require verification |
| Concierging/service layer | `Apex-Concierge` | service workflows and user-facing service automation | execution proof required |
| Brain/reasoning source | `THE-BRAIN-V1` | reasoning/memory/agent source components | integration proof required |
| OAuth/integration onboarding | `Apex-OAuth-Wizard` | authorization flows and integration setup | consent/token handling required |
| Command/portal surfaces | `apex-ecosystem-portal`, `executive-command-deck` | portal/deck UI and summaries | UI must connect to real state |
| Golden World game | **Existing Golden World repository/package; do not create duplicate until actual repo is located/confirmed** | game engine, world, missions, zones, inventory, progression, multiplayer, Quantum Realm, educational systems | code/runtime evidence required |
| Golden World STEM sequence | **Golden World documentation/data home; canonical curriculum source linked from `Apex-Hub`** | curriculum source, versioned scope/sequence, competency map, mission mappings | source document controls sequencing |
| Golden World Sentinel | `Apex-Sentinel` with Golden World adapter/config | child-safe monitoring, server health, incidents | security/runtime proof required |
| Golden World mobile shell | `Apex-Breeze` or existing Golden World mobile app repo | Capacitor shell and device deployment | build/read-back required |
| Golden World Blender HUD | `Apex-Studio-OS-` or existing Golden World Blender asset home | Blender scene/scripts/HUD assets | actual `.blend` load/test required |
| MAC LIFE Ultimate v3 | Preserve as reference/source; production capabilities belong in owning APEX repos (`Apex-Forensic-Vision`, `Apex-Concierge`, etc.) | encryption/logging, quantum demos, CV, analytics, media processing; refactor, don't duplicate | simulated features remain DEMO |
| APEX Flow financial controls | revenue implementation home; map from `Apex-Hub` | append-only ledger, fee logic, approval queue, payout execution, webhooks | actual money movement/read-back required |
| Commerce OS | `APEX-Omni-Product-Studio` / existing commerce implementation home, linked from `Apex-Hub` | market signals, ingestion, scoring, pricing, decision, Shopify, Matrixify, inventory/order sync, monitoring, learning | 10→100→1000→2000 evidence path |
| ARK strategic protection | `the-ark-hq` | protection/family/strategic mission material | strategic source, not runtime green |
| Funding/capital research | `Apex-Hub` docs | opportunities, eligibility, application state, evidence | current external verification required |
| Social command center | `Apex-Studio-OS-` or existing social/content implementation home; map in `Apex-Hub` | social adapters, scheduling, analytics, content lifecycle | platform API proof required |
| Autonomous build/self-healing | `APEX-TERMINAL` + `Apex-Hub` governance | CI/CD, isolated builds, security checks, deploy/read-back, rollback policies | high-impact actions require authorization |
| MAC LIFE visual command-center UI requirements | `Apex-Hub` as UX standard; implementation in owning surface | large metrics, cards, status badges, responsive shell, real-time state | visuals never establish backend truth |
| 89%/percentage evidence model | `Apex-Hub` / Truth Gate | denominators, claim sets, evidence pointers | never fabricate confidence/completion |

## Source handling rules

1. Preserve source artifacts in the archive or source-designated location.
2. Extract durable requirements into the owning repository.
3. Link cross-repository dependencies instead of copying entire systems.
4. Never copy raw credentials, biometric secrets, tokens, or private keys into source packages or durable memory.
5. Treat prior claims of LIVE/COMPLETE/VERIFIED as source claims until independently proven.
6. When no dedicated repository is currently confirmed, record the capability as **UNASSIGNED / LOCATE EXISTING REPO** rather than creating a duplicate.

## Golden World specific consolidation

The Golden World source set currently contains multiple generations of the same architecture: v5/v7 installers, Totality/Omega shells, Sentinel/mobile/Blender concepts, STEM quest mechanics, real-world/Quantum world design, multiplayer concepts, inventory/weapon concepts, cultural calendar/real-world data concepts, and adaptive learning.

These must converge into one canonical Golden World implementation home once the actual existing repository is identified. Until then, `Apex-Hub` holds the placement and reconciliation record only.

## Verification lifecycle

`DEFINED → WRITTEN → RUNNING → TESTED → DEPLOYED → HEALTHY → INTEGRATED → VERIFIED`

A repository location is never itself evidence of runtime completion.
