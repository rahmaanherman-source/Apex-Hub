# APEX Sovereign Audio Studio Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the canonical APEX Sovereign Audio Studio requirements into a verified artist-operated audio runtime that can capture a performance, understand its musical structure, generate instrument interpretations, process it through DSP/tape stages, export the result, and record evidence.

**Architecture:** Build around stable contracts for audio routing, musical intent/hypotheses, variants, tape/DSP, quantized scheduling, laboratory tests, audit/evidence, and export. Reuse existing APEX infrastructure before adding new components, and keep the audio subsystem portable into APEX 360.

**Tech Stack:** C++ audio/DSP core where applicable; existing APEX application/runtime stack; repository-native test/build tooling; machine-readable audit/evidence records.

**Spec:** `docs/canonical/APEX_SOVEREIGN_AUDIO_STUDIO_MASTER_SPEC.md` and `docs/canonical/APEX_SOVEREIGN_AUDIO_STUDIO_LIFECYCLE_BOOTSTRAP.md`

## Global Constraints

- Current scope is audio only; video/vision is deferred.
- Artist-first workflow: `CAPTURE → UNDERSTAND → TRANSFORM → HEAR → CHOOSE → BUILD → EXPORT`.
- Preserve the raw performance and full derivative lineage.
- No heap allocation in real-time audio processing functions.
- Do not claim lock-free behavior solely because atomics are present; prove ownership/synchronization.
- Preserve competing musical hypotheses with confidence values.
- 23 variants is the canonical demonstration count and must remain configurable.
- Tape models are original modular DSP implementations informed by public engineering behavior; do not claim exact proprietary hardware cloning.
- `SOURCE IMPLEMENTED ≠ BUILD VERIFIED ≠ TEST VERIFIED ≠ RUNTIME VERIFIED ≠ HARDWARE VERIFIED ≠ AUDIO VERIFIED`.
- Documentation is specification, not runtime evidence.

---

### Task 1: Repository reconciliation and contracts

**Files:**
- Create: `docs/canonical/APEX_SOVEREIGN_AUDIO_STUDIO_IMPLEMENTATION_MAP.md`
- Modify: existing audio/audit/test files only after inspection
- Test: repository-native build/test commands discovered during inspection

**Interfaces:**
- Consumes: canonical Master Specification, Harmony Engine, Lifecycle Bootstrap.
- Produces: one authoritative implementation map and stable interface inventory for downstream tasks.

- [ ] **Step 1: Inventory existing audio-related files**

Search for router, DSP, scheduler, harmony, tape, capture, MIDI, transport, export, audit, evidence, and test implementations.

- [ ] **Step 2: Classify every relevant requirement**

Use exactly: `EXISTING | MODIFY | NEW | DUPLICATE | MISSING | UNVERIFIED`.

- [ ] **Step 3: Define stable contracts**

Document the interfaces for audio buffers, musical intent, hypotheses, variants, tape stages, scheduler events, lab tests, evidence records, and exports.

- [ ] **Step 4: Run existing tests**

Run the repository's existing audio/runtime test suite before changes and record the baseline.

- [ ] **Step 5: Commit**

Commit the reconciliation map and contract documentation before implementation changes.

---

### Task 2: Sovereign Audio Router

**Files:**
- Modify/Create: repository-native router implementation identified in Task 1
- Test: repository-native router unit tests

**Interfaces:**
- Consumes: bounded stereo audio blocks and bus-control state.
- Produces: deterministic stereo master block and sample-position state.

- [ ] **Step 1: Write tests for null/size handling and deterministic zeroing**

- [ ] **Step 2: Write tests for eight-bus summing and gain limits**

- [ ] **Step 3: Write a concurrency/ownership test for the producer-to-audio-buffer path**

- [ ] **Step 4: Implement the minimum router contract without real-time heap allocation**

- [ ] **Step 5: Run focused router tests**

- [ ] **Step 6: Record whether the implementation supports a defensible lock-free claim**

- [ ] **Step 7: Commit**

---

### Task 3: Musical intent and harmonic extraction

**Files:**
- Create/Modify: repository-native musical analysis modules identified in Task 1
- Test: pitch/note/key/harmony corpus tests

**Interfaces:**
- Consumes: recorded PCM audio.
- Produces: musical intent object containing pitch, notes, timing, tonal candidates, harmony candidates, and confidence values.

- [ ] **Step 1: Write fixtures for monophonic and polyphonic recordings**

- [ ] **Step 2: Write tests for pitch and note-event extraction**

- [ ] **Step 3: Write tests for onset/timing extraction**

- [ ] **Step 4: Write tests that preserve multiple key/harmony hypotheses**

- [ ] **Step 5: Implement the analysis pipeline**

- [ ] **Step 6: Run corpus tests and calculate actual errors/accuracy**

- [ ] **Step 7: Record confidence/error results without inventing target attainment**

- [ ] **Step 8: Commit**

---

### Task 4: One-variant instrument transformation path

**Files:**
- Create/Modify: repository-native variant-generation/arrangement modules
- Test: end-to-end analysis-to-one-variant test

**Interfaces:**
- Consumes: musical intent + artist instruction.
- Produces: one traceable arrangement variant with source lineage and render reference.

- [ ] **Step 1: Write the end-to-end test for `MIC/PCM → ANALYSIS → MUSICAL_INTENT → VARIANT → EXPORT`**

- [ ] **Step 2: Implement the variant object with source ID, musical representation, transformation parameters, and status**

- [ ] **Step 3: Connect one instrument realization**

- [ ] **Step 4: Connect preview/audition and export**

- [ ] **Step 5: Run the end-to-end test**

- [ ] **Step 6: Commit**

---

### Task 5: 23-variant orchestration

**Files:**
- Modify: variant-generation modules from Task 4
- Test: 23-variant generation and diversity tests

**Interfaces:**
- Consumes: musical intent + natural-language direction + configurable count.
- Produces: `Variant[]` with canonical 23-result demonstration support.

- [ ] **Step 1: Write a test requiring exactly 23 traceable variants for the canonical demonstration**

- [ ] **Step 2: Write tests proving every variant references the same source intent**

- [ ] **Step 3: Write a meaningful musical-feature diversity test**

- [ ] **Step 4: Implement configurable variant count**

- [ ] **Step 5: Implement instrument-family selection and natural-language transformation parameters**

- [ ] **Step 6: Run 23-variant tests and capture render success/failure**

- [ ] **Step 7: Commit**

---

### Task 6: Sovereign Tape Engine

**Files:**
- Create/Modify: tape modules identified in Task 1
- Test: tape model coefficient, stability, nonlinear-response, and signal-measurement tests

**Interfaces:**
- Consumes: clean audio + tape configuration.
- Produces: processed audio plus model metadata.

- [ ] **Step 1: Write tests for TapeSpeed, TapeEQ, saturation, wow/flutter, noise, and head behavior contracts**

- [ ] **Step 2: Implement independent modules with clean-source preservation**

- [ ] **Step 3: Implement Track, Mix, Master, and Godspeed gates**

- [ ] **Step 4: Implement artist-facing controls `CHARACTER / WEIGHT / WIDTH / GLUE / AGE / SPEED`**

- [ ] **Step 5: Measure nonlinear/frequency/noise behavior where applicable**

- [ ] **Step 6: Record reference assumptions separately from measured output**

- [ ] **Step 7: Commit**

---

### Task 7: Move Music scheduler

**Files:**
- Modify/Create: scheduler implementation identified in Task 1
- Test: scheduler boundary/drift tests

**Interfaces:**
- Consumes: sample position, BPM, sample rate, clip ID, track index.
- Produces: quantized clip event with measured target position.

- [ ] **Step 1: Write exact-boundary and neighboring-sample tests**

- [ ] **Step 2: Write BPM/sample-rate change tests**

- [ ] **Step 3: Write long-run drift and quantization-error tests**

- [ ] **Step 4: Implement deterministic scheduling**

- [ ] **Step 5: Run focused scheduler tests**

- [ ] **Step 6: Record measured timing error**

- [ ] **Step 7: Commit**

---

### Task 8: Artist laboratory and evidence manifest

**Files:**
- Create/Modify: repository-native lab/verification UI and audit/evidence modules
- Test: evidence-recording and end-to-end lab tests

**Interfaces:**
- Consumes: runtime capabilities and actual studio-device state.
- Produces: guided test result + machine-readable evidence record.

- [ ] **Step 1: Write the lab test sequence**

The sequence is: microphone → record → playback → routing → analysis → hypotheses → 23 variants → audition → selection → DSP/tape → scheduler → export → audit.

- [ ] **Step 2: Write evidence schema tests**

- [ ] **Step 3: Implement automatic capture of available device/build/test conditions**

- [ ] **Step 4: Implement claim-specific pass/fail states**

- [ ] **Step 5: Ensure failed/missing evidence remains `BLOCKED` or `UNVERIFIED`**

- [ ] **Step 6: Run the laboratory against the actual application runtime**

- [ ] **Step 7: Commit evidence infrastructure**

---

### Task 9: Audio measurements and promotion gate

**Files:**
- Modify: evidence/verification registry identified in Task 1
- Test: promotion-gate tests

**Interfaces:**
- Consumes: test results and evidence artifacts.
- Produces: claim-specific verification status.

- [ ] **Step 1: Write tests preventing promotion without required evidence**

- [ ] **Step 2: Add measurements for latency, LUFS, true peak, clipping, and signal integrity where the runtime path supports them**

- [ ] **Step 3: Add hardware-dependent status separation**

- [ ] **Step 4: Run the promotion-gate test suite**

- [ ] **Step 5: Update the capability registry only for supported claims**

- [ ] **Step 6: Commit**

---

### Task 10: APEX 360 portability contract

**Files:**
- Create: `docs/canonical/APEX_SOVEREIGN_AUDIO_STUDIO_APEX360_PORTABILITY.md`
- Modify: capability/interface documentation as needed
- Test: interface/serialization compatibility tests

**Interfaces:**
- Consumes: verified audio capability contracts.
- Produces: stable capability boundaries for future APEX 360 integration.

- [ ] **Step 1: Define portable capability boundaries**

- [ ] **Step 2: Define project/session/asset lineage serialization**

- [ ] **Step 3: Define APEX 360 integration points without implementing video/vision**

- [ ] **Step 4: Test serialization/deserialization of musical intent, variants, and evidence records**

- [ ] **Step 5: Commit portability documentation**

---

## Verification Gate

The project may not be described as fully verified until the actual runtime demonstrates the required path and the evidence record supports the corresponding claims.

Minimum end-to-end acceptance path:

`MIC → RECORD → ANALYZE → KEY/HARMONY HYPOTHESES → 23 VARIANTS → AUDITION → SELECT → ROUTE → DSP/TAPE → EXPORT → AUDIT`

The artist's hands-on session establishes user acceptance for the observed workflow. Objective measurements establish technical claims. Neither substitutes for the other.

## Plan self-review

- **Spec coverage:** repository reconciliation, router, harmonic extraction, one-variant path, 23 variants, tape engine, scheduler, artist lab, evidence/promotion, and APEX 360 portability are all represented.
- **No fake green:** every verification claim requires a corresponding test or measurement; source code alone is never promoted.
- **No duplicate systems:** Task 1 precedes implementation and requires repository inspection.
- **No unsupported accuracy claims:** the plan requires measurement against a corpus rather than asserting percentages in advance.
- **Audio-only scope:** video/vision is explicitly deferred.
