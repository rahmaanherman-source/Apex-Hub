# APEX Sovereign Audio Studio — Lifecycle Bootstrap

**Status:** CANONICAL BUILDER BOOTSTRAP  
**Scope:** Audio only; future portable subsystem of APEX 360  
**Verification law:** No-Fake-Green  
**Artist role:** Primary hands-on acceptance authority for musical usefulness and studio workflow

## 1. Mission

Bootstrap the APEX Sovereign Audio Studio as a deterministic, artist-first audio laboratory. The immediate objective is not the broader APEX 360 vision. The immediate objective is to make the audio core real: capture, route, analyze, transform, audition, mix, master, export, and preserve evidence.

The system must let the artist use ordinary studio hardware—such as a USB microphone/Yeti-class microphone—to create and test music directly inside the APEX application. The completed audio subsystem must later be portable into APEX 360 without redesigning the core contracts.

## 2. Canonical creative loop

`CAPTURE → UNDERSTAND → TRANSFORM → HEAR → CHOOSE → BUILD → EXPORT`

The core differentiator is:

`SUNG/HUMMED IDEA → MEASURABLE MUSICAL REPRESENTATION → COMPETING INTERPRETATIONS → INSTRUMENT REALIZATIONS → ARTIST CHOICE`

The artist can say:

> "I kind of hear this. Give me 23 different results."

The runtime must turn that request into a structured generation job. Twenty-three is the canonical demonstration count, not a hard architectural limit.

## 3. Deterministic lifecycle state machine

Every build/capability moves through explicit states:

`SPECIFIED`
→ `INSPECTED`
→ `IMPLEMENTED`
→ `BUILT`
→ `UNIT_TESTED`
→ `INTEGRATED`
→ `RUNTIME_TESTED`
→ `MEASURED`
→ `EVIDENCE_RECORDED`
→ `VERIFIED`
→ `PROMOTED`

A failure or missing evidence moves the capability to:

`BLOCKED` or `UNVERIFIED`

It may not jump directly to `VERIFIED`.

### State rules

| State | Meaning | Required evidence |
|---|---|---|
| SPECIFIED | Requirement is defined | Canonical spec/prompt |
| INSPECTED | Existing repository surface checked | File/path inventory |
| IMPLEMENTED | Source implementation exists | Source diff/file |
| BUILT | Source compiles/builds | Build output |
| UNIT_TESTED | Focused tests pass | Test output |
| INTEGRATED | Component is connected to the real path | Integration test/output |
| RUNTIME_TESTED | Actual runtime executes the path | Runtime evidence |
| MEASURED | Objective metric captured where applicable | Measurement artifact |
| EVIDENCE_RECORDED | Evidence is persisted | Audit/evidence record |
| VERIFIED | Claim-specific evidence meets acceptance criteria | Verification record |
| PROMOTED | Capability may be treated as available | Registry update |

## 4. Phase bootstrap

### Phase 0 — Repository truth lock

**Objective:** Prevent duplicate systems and false implementation claims.

Actions:

1. Inspect the repository before writing replacement files.
2. Locate existing audio router, DSP, scheduler, recording, MIDI/transport, export, audit, evidence, and test infrastructure.
3. Map each requirement to `EXISTING`, `MODIFY`, `NEW`, `DUPLICATE`, `MISSING`, or `UNVERIFIED`.
4. Reuse existing APEX infrastructure whenever its contract satisfies the requirement.
5. Preserve the existing canonical Harmony Engine and Master Specification as authoritative requirements.

**Exit gate:** repository map exists and duplicate implementations are not silently introduced.

### Phase 1 — Sovereign Router

**Objective:** Establish deterministic signal-flow integrity.

Architecture:

`INPUT → ROUTER → TRACK BUSSES → MIX BUS → MASTER BUS`

The router is a directed signal graph. Each processor node has explicit input/output ownership and a defined buffer contract.

Requirements:

- bounded audio block processing
- no heap allocation in the real-time processing function
- explicit buffer ownership
- deterministic output initialization
- configurable sample rate/buffer size
- configurable bus gain
- sample-position tracking
- safe null/size handling
- concurrency model documented and tested

**Important correction:** `std::atomic` members alone do not prove a lock-free or race-free audio system. Producer/consumer ownership and buffer publication must be explicit.

**Exit gate:** build + focused router tests + runtime audio-path test + evidence record.

### Phase 2 — Harmonic Extraction Engine

**Objective:** Convert recorded musical performance into structured musical information.

Pipeline:

`AUDIO → STFT/PITCH FEATURES → NOTE EVENTS → ONSETS/RHYTHM → TONAL CENTER → KEY/SCALE HYPOTHESES → INTERVALS → HARMONY HYPOTHESES → CONFIDENCE`

Represent, where supported:

- fundamental frequency
- MIDI-style note number
- cents deviation
- octave
- onset/offset
- duration
- intervals
- melodic contour
- harmonic intervals
- chord candidates
- key candidates
- scale/mode candidates
- tempo/rhythm relationship
- phrase boundaries
- confidence

Do not collapse ambiguity into a false single answer. Store competing hypotheses and let the artist select/override them.

**Acceptance direction:** use a ground-truth corpus with manually annotated examples. Measure monophonic and polyphonic performance separately. Do not encode unsupported accuracy percentages as achieved results.

**Exit gate:** representative corpus test + measured accuracy/error report + runtime artist test.

### Phase 3 — Generative Interpretation / 23 Variants

**Objective:** Turn one musical intent object into multiple musically meaningful realizations.

Input:

`MUSICAL_INTENT + ARTIST_DIRECTION + VARIANT_COUNT`

Output:

`VARIANT[1..N]`

Each variant carries:

- source asset ID
- instrument/arrangement identity
- key/tonal interpretation
- tempo
- note/chord representation where available
- transformation parameters
- confidence/status
- preview/render reference
- keep/reject/favorite state

Canonical example families include horns, flute/woodwinds, strings, piano/keys, guitar, bass, synths, mallets, hybrid/neural instruments, and ensemble arrangements.

Diversity testing should compare meaningful musical feature vectors, not merely waveform distance. Distinctness must not be achieved by adding random noise.

**Exit gate:** 23 reproducible candidate records + audible audition path + lineage + diversity evidence.

### Phase 4 — Sovereign Tape Engine

**Objective:** Bring tape/recorder behavior into the studio as a modular creative processing layer without replacing the clean source.

Architecture:

`CLEAN SOURCE → TAPE MODEL → DSP → MIX/MASTER`

Modules:

- TapeTransport
- TapeSpeed
- TapeFormula
- TapeLevelCalibration
- BiasModel
- TapeNonlinearity/MagneticSaturation
- HeadWidth
- HeadBump
- TapeEQ/RecordEQ/ReproduceEQ
- Crosstalk
- WowFlutter
- Hysteresis/Memory
- TapeNoise
- Dropouts
- Azimuth
- PunchInPunchOut
- StereoMasterMode
- MultitrackMode

Four gates:

1. TRACK TAPE — multitrack character
2. MIX TAPE — mix/stem character
3. MASTER TAPE — stereo mastering character
4. GODSPEED TAPE — APEX-original musical controls

Controls:

`CHARACTER / WEIGHT / WIDTH / GLUE / AGE / SPEED`

Reference-machine engineering behavior may be studied from public documentation, but the implementation must be original and must not be represented as an exact proprietary hardware clone without evidence.

**Exit gate:** coefficient/model tests + signal measurements + audible artist test + evidence record.

### Phase 5 — Move Music Scheduler

**Objective:** Deterministic musical timing.

The scheduler supports configurable BPM/sample rate and 1/16-note quantization. The canonical demonstration is 124 BPM.

Test:

- exact boundary
- immediately before boundary
- immediately after boundary
- repeated boundaries
- BPM changes
- sample-rate changes
- long-running sample positions
- floating-point-to-integer quantization error

Do not call the scheduler sample-accurate merely because it computes an integer sample position. Measure the error.

**Exit gate:** deterministic scheduler tests + measured boundary error + runtime trigger test.

### Phase 6 — Artist Laboratory

**Objective:** Make the actual artist's studio the verification environment.

Guided lab sequence:

1. Connect microphone.
2. Select input.
3. Record a short performance.
4. Play it back.
5. Analyze pitch/note/timing.
6. Review competing key/harmony hypotheses.
7. Ask for 23 variants.
8. Audition variants.
9. Keep one or more.
10. Route through DSP/tape.
11. Quantize/trigger where applicable.
12. Export stems/master.
13. Confirm lineage and audit record.

The application should display the test state and capture machine/runtime conditions automatically. The artist should not have to reconstruct technical details manually after the session.

**Exit gate:** complete hands-on session with evidence for every claim actually tested.

## 5. Verification manifest

For every build/capability produce a machine-readable record containing at least:

- capability ID
- source path(s)
- commit/build identifier
- implementation state
- test name(s)
- runtime path
- hardware/device information when applicable
- sample rate
- buffer size
- BPM when applicable
- measured metric(s)
- expected threshold
- actual result
- pass/fail
- evidence path/reference
- timestamp
- dependencies
- unresolved limitations

## 6. Claim-specific verification

The following claims require their own evidence:

- real-time/no-allocation behavior
- lock-free/concurrency behavior
- pitch/key/harmony accuracy
- 23-result generation
- instrument transformation
- timing/quantization
- round-trip latency
- LUFS
- true peak
- clipping/signal integrity
- tape-model behavior
- microphone/device compatibility
- MIDI/transport synchronization
- export correctness

The chain is strict:

`SOURCE IMPLEMENTED ≠ BUILD VERIFIED ≠ TEST VERIFIED ≠ RUNTIME VERIFIED ≠ HARDWARE VERIFIED ≠ AUDIO VERIFIED`

## 7. Artist acceptance versus engineering proof

The artist can personally execute the laboratory session. That session is valid user-acceptance evidence for the observed workflow, but it does not automatically prove every engineering claim.

Objective measurements prove objective claims. The artist's selection proves musical usefulness. Both belong in the evidence model.

## 8. Bootstrap completion condition

The bootstrap is complete when the studio can execute the end-to-end creative path and produce an evidence-backed record:

`MIC → RECORD → ANALYZE → HYPOTHESES → 23 VARIANTS → AUDITION → SELECT → ROUTE → TAPE/DSP → EXPORT → AUDIT`

The audio subsystem remains standalone-usable and exposes clean capability boundaries so it can become the audio pillar of APEX 360.

**Final lock:** Build the path. Measure the path. Record the evidence. Never promote a claim because the documentation says it passed.
