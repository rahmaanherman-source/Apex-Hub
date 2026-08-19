# GOLDEN WORLD — SOURCE RECONCILIATION / REBOOT MAP

**Status:** SOURCE-INGESTED / RECONCILIATION REQUIRED

## Mission

Consolidate the supplied Golden World generations into one canonical implementation without losing the original design, STEM sequence, game mechanics, or world-building concepts.

## Source families

### 1. Golden World v5/v7 application prototypes

Includes:
- FastAPI backend
- SQLite persistence
- JWT authentication
- WebSockets
- player registration
- XP/levels
- achievements
- missions
- zones
- creation system
- leaderboard
- Sentinel logging/incidents
- browser client
- Capacitor shell
- deployment scripts

**Classification:** IMPLEMENTATION SOURCE. Runtime production status remains unverified until executed and read back.

### 2. Golden World STEM Quest Network

Core method:

`Challenge → Applied Logic → Interaction → Competency Evidence → Reward → World Growth`

Requirements:
- mathematics
- science
- software development
- audio/music
- technical/trade scenarios
- adaptive remediation when a learner is stuck
- real-time competency tracking
- hidden/integrated education rather than forced lessons

The supplied STEM Scope Sequence document is the curriculum authority once its actual contents are ingested.

### 3. World / exploration layer

Source concepts include:
- Journey mode
- open exploration
- side quests
- real-world cities and landmarks
- real history, science, culture, sports and almanac information
- seasonal/real-world calendars and events
- local people/knowledge contributions
- source-backed facts
- explicit separation of verified reality from game fiction/speculation

### 4. Quantum Realm

Source concepts include:
- separate imaginative realm
- original story/IP
- Gabby as a persistent companion
- technical/energy manifestations
- real-world ↔ Quantum narrative relationships
- cross-world quests and consequences

No source claim that the Quantum Realm is scientifically real should be promoted into factual game content. In-world fiction must remain clearly distinguished from verified real-world information.

### 5. Social / multiplayer

Source concepts include:
- solo Journey mode
- cooperative missions
- small team coordination
- five-person team play
- larger social missions/events
- pre-mission briefing
- team composition and attribute matching
- equipment/loadout selection
- hidden objectives/discoveries
- time/performance scoring
- leaderboards
- meaningful consequences without hard-fail punishment dominating play

### 6. Inventory / equipment / weapon claim

Source conversations contain a claimed ~1,000-weapon/item concept.

Current audit finding:
- supplied Golden World prototype installers do not contain a weapons table, manifest, IDs, stats, loadouts, or 1,000 generated records.

Classification:
**DESIGN/CLAIM — NOT VERIFIED.**

Do not record “1,000 weapons built” until a real dataset, implementation, runtime loading, and test/read-back evidence exist.

### 7. Cultural / real-world integrity

Golden World must follow:

`REAL-WORLD DATA → SOURCE → VERIFY → CONTEXT → PLAYER`

Game fiction follows a separate path:

`FICTION DESIGN → GAME RULES → PLAYER EXPERIENCE`

Speculation/unknowns should be labeled rather than presented as fact.

### 8. Gabby

Gabby is intended as:
- friend
- teacher
- guide
- contextual assistant
- optional hint provider
- adaptive learner support
- persistent companion across modes
- Quantum Realm companion

Rule:

`GUIDE, DON'T FORCE.`

Educational support should be available without turning gameplay into mandatory classroom interruptions.

### 9. Reward/learning loop

The intended loop is:

`ATTEMPT → DECISION → CONSEQUENCE → FEEDBACK → MASTERY → REWARD`

Possible rewards include:
- XP
- items
- cosmetics/skins
- attributes
- world-building resources
- collectibles
- access to new quests/zones
- exceptional mastery bonuses

### 10. Adaptive competency engine

Every educational challenge should be mappable to:

- skill
- concept
- prerequisite
- difficulty
- attempt
- result
- evidence
- mastery state

Recommended mastery states:

`INTRODUCED → PRACTICING → DEVELOPING → COMPETENT → MASTERED`

Unsuccessful attempts should create targeted remediation rather than simply declaring failure.

### 11. Golden World implementation layers

```text
GOLDEN WORLD
│
├── WORLD ENGINE
│   ├── geography
│   ├── locations
│   ├── buildings
│   ├── events
│   └── world state
│
├── QUEST ENGINE
│   ├── objectives
│   ├── dependencies
│   ├── branching outcomes
│   ├── hidden goals
│   └── rewards
│
├── COMPETENCY ENGINE
│   ├── STEM/trade skills
│   ├── scope/sequence mappings
│   ├── mastery tracking
│   └── remediation
│
├── PLAYER SYSTEM
│   ├── inventory
│   ├── attributes
│   ├── cosmetics
│   ├── achievements
│   └── reputation
│
├── SOCIAL ENGINE
│   ├── teams
│   ├── matchmaking
│   ├── cooperative objectives
│   └── leaderboards
│
├── GABBY
│   ├── guidance
│   ├── education
│   ├── discovery
│   └── Quantum companion
│
├── REAL-WORLD KNOWLEDGE
│   ├── source registry
│   ├── current data
│   ├── provenance
│   └── uncertainty labels
│
├── QUANTUM REALM
│   ├── fiction layer
│   ├── world rules
│   ├── narrative links
│   └── cross-world missions
│
└── SAFETY / PRIVACY
    ├── child account controls
    ├── parent workflows
    ├── privacy
    ├── moderation
    └── audit
```

## Current implementation gap register

### P0
- Locate/confirm the canonical Golden World repository.
- Ingest the STEM Scope Sequence source document.
- Define the canonical data model for world, quest, competency, player, inventory, and evidence.
- Replace prototype status strings with real verification states.
- Add parent consent/verification workflow; parent-email collection alone is not consent proof.
- Define child-safe data retention and access rules.

### P1
- Build competency-to-quest mapping.
- Build adaptive remediation engine.
- Build mission briefing/loadout flow.
- Build real inventory/item system.
- Build multiplayer team/state model.
- Build real-world source/provenance system.
- Build seasonal event calendar ingestion and validation.
- Build Quantum Realm as explicitly fictional game content.

### P2
- Expand world content.
- Add city/location datasets.
- Add global cultural event adapters.
- Add player legacy/history system.
- Add cross-world consequence engine.
- Scale generated/templated side-quest creation with verification and safety gates.

## Acceptance rule

No Golden World feature is GREEN because a button renders, a boolean flips, or a script prints COMPLETE.

Required lifecycle:

`DEFINED → WRITTEN → RUNNING → TESTED → DEPLOYED → HEALTHY → INTEGRATED → VERIFIED`
