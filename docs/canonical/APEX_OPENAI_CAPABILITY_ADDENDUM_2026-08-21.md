# APEX OPENAI CAPABILITY ADDENDUM — 2026-08-21

**STATUS:** CANONICAL STAGING / SOURCE-INGESTED
**AUTHORITY:** APEX-Laws
**DESTINATION:** `APEX-Laws` standalone repository when independently confirmed
**SOURCE BASIS:** User-supplied OpenAI documentation excerpts for Agents SDK, Image Generation, Realtime/Audio, and GPT-5.6.
**VERIFICATION STATE:** Source-ingested; claims in this addendum require live official-source verification before being promoted to independently verified platform truth.

## 1. Purpose

This addendum records durable architectural implications of the supplied OpenAI platform documentation for APEX/Gabby. It does not replace APEX law and does not authorize capabilities merely because documentation describes them.

The governing APEX boundary remains:

```text
LAW = what must be true
MEMORY = what durably matters
RUNTIME = what is happening now
EVIDENCE = why a claim is trusted
ARCHIVE = historical source material
```

## 2. Agents SDK

The supplied documentation describes the Agents SDK as an application framework for agents that can plan, call tools, collaborate across specialists, and maintain enough state for multi-step work.

Relevant capabilities described in the source:

- code-first agent applications in TypeScript or Python;
- agent definitions and specialist ownership;
- model/provider configuration;
- agent runtime loops and continuation;
- sandbox agents for files, commands, packages, mounts, and provider links;
- orchestration and handoffs;
- agents-as-tools manager-style workflows;
- guardrails and human review;
- resumable approval flows;
- sessions and state;
- hosted tools, function tools, and MCP;
- tracing and evaluation.

### APEX architectural role

Agents SDK is an orchestration layer, not APEX authority.

```text
APEX LAW
  ↓
APEX AUTHORIZATION / GATEKEEPER
  ↓
AGENT ORCHESTRATION
  ↓
TOOLS / MCP / SERVICES
  ↓
RUNTIME
  ↓
EVIDENCE / VERIFICATION
```

The SDK may run the agent loop, but consequential permissions and verification remain governed by APEX.

## 3. Responses API vs Agents SDK

The supplied documentation distinguishes the two paths:

- Responses API: application owns the model interaction loop, tool routing, state, orchestration, and branching.
- Agents SDK: SDK owns the agent loop and recurring orchestration patterns such as tool calls, branching, and handoffs.

APEX should choose based on workflow shape rather than treating one API as universally superior.

## 4. GPT-5.6 Model Family

The supplied documentation states:

- `gpt-5.6` is an alias routing to `gpt-5.6-sol`;
- `gpt-5.6-sol` is the flagship capability tier;
- `gpt-5.6-terra` is positioned for strong performance at lower cost;
- `gpt-5.6-luna` is positioned for efficient high-volume workloads.

The source describes support for:

- `reasoning.effort`: `none`, `low`, `medium`, `high`, `xhigh`, `max`;
- `reasoning.mode: "pro"`;
- persisted reasoning context;
- explicit or implicit prompt caching;
- Programmatic Tool Calling;
- beta multi-agent coordination;
- stronger frontend design judgment;
- improved intent understanding;
- original image detail preservation for supported image inputs.

### APEX model-routing principle

Computational effort should be selected by workload.

```text
LOW LATENCY / HIGH VOLUME
→ lower-cost / lower-effort configuration

NORMAL OPERATIONS
→ balanced reasoning

COMPLEX ENGINEERING / RESEARCH
→ higher reasoning effort

QUALITY-FIRST / HARD VERIFICATION
→ compare high/max and pro configurations empirically
```

No model tier is canonical merely because it is the newest. APEX records model capability and cost as platform-registry facts with confidence and verification metadata.

## 5. Programmatic Tool Calling

The supplied GPT-5.6 documentation describes Programmatic Tool Calling (PTC) for bounded, tool-heavy workflows where code can call eligible tools, pass results between calls, and process intermediate outputs in a hosted runtime.

Strong-fit tasks described by the source include:

- filtering;
- joining;
- ranking;
- deduplication;
- aggregation;
- predictable validation;
- processing large intermediate tool outputs into smaller structured results.

PTC should remain bounded.

Do not use PTC merely because calls are numerous. Prefer direct calls when:

- one call is sufficient;
- intermediate results are small;
- each result may change the next semantic decision;
- an action requires approval;
- the final output must preserve native citations or artifacts.

### APEX PTC boundary

```text
BOUNDED PROCESSING
→ PTC MAY BE USED

SEMANTIC JUDGMENT
→ DIRECT MODEL / AGENT

APPROVAL
→ DIRECT GOVERNED FLOW

FINAL VALIDATION
→ DIRECT GOVERNED FLOW
```

PTC must never become a bypass around APEX authorization, evidence, approval, or no-fake-green rules.

## 6. Multi-Agent Workflows

The supplied GPT-5.6 documentation describes beta multi-agent coordination in the Responses API for parallel independent workstreams followed by synthesis.

APEX may use this pattern when tasks genuinely divide into independent specialist work.

Example:

```text
                         APEX / GABBY
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
       RESEARCH            BUILD              VALIDATE
          │                   │                   │
          └───────────────────┼───────────────────┘
                              ▼
                          SYNTHESIS
                              ▼
                     EVIDENCE / DECISION
```

Parallelism must not be used merely to create additional agents. Each specialist needs a defined responsibility, evidence boundary, and handoff contract.

## 7. Image Generation

The supplied Image Generation documentation describes two API paths:

### Image API

For direct image generation/editing workflows, including:

- generation from text;
- edits of existing images;
- reference-image generation;
- masked editing;
- output size/quality/format/compression/background controls;
- streaming partial images.

The supplied source identifies `gpt-image-2` as the latest GPT Image model in that documentation.

### Responses API image generation

The supplied source describes image generation as a built-in Responses API tool, enabling image generation within conversations and multi-step workflows.

It also describes:

- multi-turn editing;
- image inputs through URLs, base64 data URLs, or File IDs;
- previous-response continuation;
- image-generation call IDs for continued context;
- `action` modes such as automatic selection, forced generation, or forced edit when valid image context exists;
- streaming partial images;
- revised prompts returned by image-generation calls.

### APEX creative-system role

Image generation belongs behind the creative/runtime boundary.

```text
GABBY / USER INTENT
        ↓
AGENT REASONING
        ↓
IMAGE GENERATION / EDIT TOOL
        ↓
APEX RUNTIME
        ↓
ASSET + PROVENANCE
        ↓
VISUAL VERIFICATION
```

A generated image is an output artifact, not automatically a verified design, character, asset, or production-ready result.

For Character Studio, generated assets should remain associated with character/version/project context where the runtime supports that relationship.

## 8. Image Reference and Mask Rules

The supplied documentation states that image edits can use one or more reference images and masks.

For masked editing, the source states that:

- the image and mask must match in format and size;
- the mask must contain an alpha channel;
- when multiple input images are supplied, the mask applies to the first image;
- masking guides the model and is not guaranteed to be pixel-perfect.

APEX should therefore distinguish:

```text
REQUESTED REGION
≠
MODEL-GENERATED RESULT
≠
VERIFIED REGION PRESERVATION
```

## 9. Image Output and Verification

The supplied documentation describes output controls including size, quality, format, compression, and transparent background where supported.

It also identifies limitations involving:

- latency;
- precise text rendering;
- recurring-character consistency;
- structured composition control.

These limitations are operationally important for Character Studio. A visually successful generation should not be treated as proof of exact layout, identity consistency, or text correctness without inspection.

## 10. Realtime and Audio

The supplied Realtime documentation distinguishes live sessions from request-based audio APIs.

### Voice agent

Use a realtime voice-agent session when the model should:

- listen;
- reason;
- speak;
- call tools;
- maintain conversation state.

The supplied source identifies `gpt-realtime-2.1` as the low-latency voice-agent model in its architecture table.

### Translation

Use a dedicated realtime translation session for continuous speech translation rather than the ordinary assistant turn lifecycle.

### Transcription

Use realtime transcription when the goal is streaming transcript deltas without model-generated spoken responses.

Use bounded/file transcription for uploaded or bounded audio workflows.

## 11. Realtime Transport

The supplied source recommends transport based on capture/playback location:

```text
Browser / Mobile
→ WebRTC

Server media pipeline / raw audio
→ WebSocket

Telephony
→ SIP
```

For APEX Terminal browser/mobile voice interaction, WebRTC is the primary architectural candidate described by the source.

## 12. Gabby Voice Boundary

Realtime is a communication layer, not an authority layer.

```text
REALTIME
= live communication

AGENTS SDK / RESPONSES
= reasoning + orchestration

APEX GATEKEEPER
= authorization

APEX RUNTIME
= operational state

EVIDENCE
= verification basis

MEMORY
= durable knowledge
```

Therefore a voice command such as:

> “Gabby, change the character armor.”

must still resolve through the same authorization, capability, runtime, evidence, and verification path as a typed command.

Voice cannot bypass APEX controls.

## 13. Realtime Safety Identifier

The supplied source states that individual-user applications should send a stable, privacy-preserving safety identifier with Realtime requests and that the identifier does not automatically carry over from other API sessions.

APEX should treat safety-identifier propagation as an explicit session integration requirement, subject to the applicable official implementation documentation and privacy requirements.

## 14. GPT-5.6 Prompting / Autonomy Law

The supplied documentation recommends leaner prompts, explicit autonomy boundaries, concise tool descriptions, and measurable success criteria.

APEX should centralize action boundaries rather than repeat conflicting approval instructions across every prompt.

Baseline policy shape:

```text
ANSWER / EXPLAIN / REVIEW / DIAGNOSE / PLAN
→ inspect and report
→ do not implement unless requested

CHANGE / BUILD / FIX
→ make requested in-scope local changes
→ run relevant non-destructive validation

EXTERNAL WRITE / DESTRUCTIVE ACTION / PURCHASE /
MATERIAL SCOPE EXPANSION
→ require confirmation
```

This policy is subordinate to APEX Law and must be implemented through actual authorization controls where consequential operations are involved.

## 15. Persisted Reasoning Boundary

GPT-5.6 persisted reasoning can support continuity across multi-turn work. It must not be conflated with APEX Memory.

```text
PERSISTED REASONING
→ active reasoning continuity

APEX MEMORY
→ durable operating knowledge

RUNTIME
→ current state

ARCHIVE
→ historical source material
```

Reasoning context is not automatically promoted into durable memory.

## 16. Capability Registry Entries Required

The following capabilities should be represented in the APEX Capability Registry with evidence metadata before being treated as production-approved:

- OpenAI Agents SDK;
- Responses API agent orchestration;
- GPT-5.6 model family and model routing;
- GPT-5.6 reasoning modes/effort;
- Programmatic Tool Calling;
- Responses API multi-agent beta;
- GPT Image image generation;
- GPT Image image editing/reference/masking;
- image streaming/partial images;
- Realtime voice-agent sessions;
- Realtime translation sessions;
- Realtime transcription sessions;
- WebRTC realtime transport;
- WebSocket realtime transport;
- SIP realtime transport;
- safety-identifier handling.

Each record must include status, confidence, source, evidence level, last tested, and applicable version/expiration information.

## 17. APEX Capability Decision

The new OpenAI capabilities do not authorize duplicate construction where an approved existing capability can be reused.

The deterministic APEX decision remains:

```text
EXISTING APEX CAPABILITY?
→ REUSE

APPROVED PLATFORM / SDK / API?
→ INTEGRATE

APPROVED PARTNER?
→ PARTNER / INTEGRATE

NO SUITABLE EXISTING PATH?
→ BUILD ONLY IF JUSTIFIED

NO SAFE / ECONOMIC PATH?
→ DOCUMENT LIMITATION
```

## 18. Character Studio Implications

The supplied documentation strengthens the target architecture for the existing APEX Terminal Character Studio:

- GPT Image can serve generation/editing/reference workflows;
- Responses API can coordinate image generation inside multi-step agent workflows;
- Agents SDK can own bounded specialist orchestration;
- Realtime can provide hands-free Gabby interaction;
- voice commands must route through the same runtime and authorization path;
- image outputs must be recorded as runtime artifacts rather than falsely treated as verified state;
- iterative image editing can preserve conversational context through response continuation;
- partial image streaming can support interactive generation previews where implementation and UX testing justify it.

The APEX Terminal remains a native workspace rather than being replaced by a separate AI application.

## 19. Evidence and No-Fake-Green Requirement

Documentation claims remain distinct from implementation proof.

For each integrated capability, APEX should distinguish:

```text
DOCUMENTED
→ CONFIGURED
→ CONNECTED
→ EXECUTED
→ TESTED
→ VERIFIED
```

No status may skip directly from documentation to `VERIFIED`.

## 20. Durable Architectural Relationship

The combined architecture is:

```text
                         APEX / GABBY
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
       Responses          Agents SDK          Realtime
          │                   │                   │
          │             orchestration        live voice
          │                   │                   │
          └──────────────┬────┴───────────────────┘
                         │
                      TOOLS
                         │
            ┌────────────┼─────────────┐
            ▼            ▼             ▼
           PTC       IMAGE GEN      EXTERNAL
            │            │           SERVICES
            └────────────┼─────────────┘
                         ▼
                   APEX GATEKEEPER
                         ▼
                    APEX RUNTIME
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
        MEMORY         EVIDENCE       ARCHIVE
```

The central rule is unchanged:

**AI can reason, communicate, generate, orchestrate, and propose. APEX governs what becomes authorized runtime state and what becomes verified truth.**

## 21. Promotion Gate

Before this addendum or any derived capability record is marked independently verified:

1. Read the current official OpenAI documentation.
2. Confirm model/API availability in the target account and environment.
3. Confirm current SDK/API schemas.
4. Test representative workflows.
5. Record request/runtime evidence where applicable.
6. Record cost and latency measurements where material.
7. Record failures and limitations.
8. Update the Capability Registry.
9. Promote only the claims supported by evidence.

**NO FALSE GREEN. NO UNVERIFIED AUTHORITY.**
