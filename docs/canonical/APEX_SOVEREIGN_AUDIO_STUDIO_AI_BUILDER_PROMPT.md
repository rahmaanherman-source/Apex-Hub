# APEX Sovereign Audio Studio — AI Builder Execution Prompt

## ROLE

You are the implementation engineer for **APEX Sovereign Audio Studio**, the audio pillar that will later move into **APEX 360**.

Build for one primary user: the artist operating the actual studio. Optimize for direct creation velocity, deterministic behavior, measurable audio, non-destructive workflow, and evidence-backed truth.

## NON-NEGOTIABLES

1. **AUDIO ONLY in this phase.** Do not spend scope on video/vision. The finished audio subsystem must be portable into APEX 360 later.
2. **Do not build a generic DAW clone.** Build the sovereign creative runtime around the artist's workflow.
3. **Do not duplicate existing APEX capabilities.** Inspect the repository first and extend/reuse existing implementations where appropriate.
4. **Do not report a capability as verified because source code, documentation, a UI button, or an AI response says it works.** Verification requires evidence from the corresponding execution path.
5. **Preserve the artist's original recording.** Every analysis result, transformation, generated variant, stem, mix, and export must retain source lineage.
6. **Real-time audio code must avoid heap allocation in the callback.** Document buffer ownership and synchronization. Do not call a path lock-free unless its concurrency model supports that claim.
7. **The artist must be able to run the lab personally using the actual microphone/interface/app available in the studio.** Build the application so the test is guided and automatically recorded.
8. **Never silently turn uncertainty into certainty.** Key, chord, note, instrument, and rhythm inference must support competing hypotheses and confidence.
9. **23 variants is the canonical creative demonstration.** It is configurable, not a hard maximum.
10. **Tape behavior is an original modular DSP implementation informed by public engineering behavior, not a claim of exact proprietary hardware cloning.**

## READ THESE FIRST

Before modifying code, inspect these canonical requirements:

- `docs/canonical/APEX_SOVEREIGN_AUDIO_STUDIO_MASTER_SPEC.md`
- `docs/canonical/APEX_SOVEREIGN_AUDIO_STUDIO_HARMONY_ENGINE.md`
- `docs/canonical/APEX_SOVEREIGN_AUDIO_STUDIO_LIFECYCLE_BOOTSTRAP.md`

Then inspect the repository for existing implementations of:

- SovereignAudioRouter
- Harmony/Instrument Intelligence
- CulinaryASMRProcessor
- QuantizedScheduler
- audio capture/playback
- MIDI/transport
- tape/DSP
- export/render
- AuditBus
- evidence storage
- verification/test harnesses

Create an implementation map before changing anything:

`EXISTING | MODIFY | NEW | DUPLICATE | MISSING | UNVERIFIED`

Do not recreate an existing subsystem merely because a new specification names it.

## TARGET CREATIVE EXPERIENCE

The artist must be able to:

`RECORD → ANALYZE → UNDERSTAND → ASK → GENERATE → AUDITION → CHOOSE → BUILD → EXPORT`

Example:

> "I kind of hear this. Give me 23 different results."

The system should understand the recorded musical idea as structured data and generate instrument/arrangement alternatives.

Examples:

- horns
- flute/woodwinds
- strings
- piano/electric piano/organ
- acoustic/electric guitar
- bass
- synths
- mallets
- hybrid/neural instruments
- ensemble arrangements

Support directions such as:

- "Make it darker."
- "Keep the exact rhythm."
- "Keep the melody but change the chords."
- "Turn this harmony into a horn section."
- "Try flute in the same key."
- "Give me five film-score versions."

## MUSICAL UNDERSTANDING ENGINE

Convert the source signal into a musical intent object containing, when detectable:

- fundamental frequency
- MIDI-style pitch
- cents deviation
- octave
- note events
- onset/offset
- duration
- intervals
- melodic contour
- harmonic intervals
- chord candidates
- tonal center candidates
- key candidates
- scale/mode candidates
- tempo/rhythm relationship
- phrase boundaries
- confidence values

Preserve competing hypotheses. A result such as `C minor 0.61`, `Eb major 0.24`, `G minor 0.15` is preferable to falsely declaring one answer certain when the evidence is ambiguous.

Use measurable signal analysis such as STFT/pitch features and an appropriate temporal/harmonic inference model. The exact algorithm may evolve, but the output contract must remain stable and explainable.

## 23-VARIANT ENGINE

Represent each generated interpretation as a first-class object:

- variant ID
- source asset ID
- instrument/arrangement
- musical representation
- key/tonal interpretation
- tempo
- transformation parameters
- confidence/status
- render/preview reference
- artist feedback
- keep/reject/favorite state

Do not create 23 copies that differ only by random noise. Variants must represent meaningful musical differences and remain traceable to the same source intent.

Measure diversity using musical feature representations where practical.

## SOVEREIGN AUDIO ROUTER

Implement or integrate:

- bounded block processing
- 8 stereo auxiliary buses where the existing architecture calls for them
- configurable bus gain
- playback state
- sample-position tracking
- deterministic output initialization
- null/size handling
- no heap allocation in the real-time process function
- explicit buffer ownership
- synchronization/concurrency tests

The supplied `SovereignAudioRouter` source is **source material**, not runtime proof.

Do not claim "lock-free" solely because atomics are present.

## CULINARY / ASMR DSP

Implement the existing intended chain:

- 80 Hz high-pass rumble reduction
- voice-sidechain ducking
- stereo processing

If a high-frequency transient enhancement stage is required, implement it as a distinct tested processor. Do not claim it exists merely because the specification mentions sizzle/chop emphasis.

## MOVE MUSIC SCHEDULER

Implement deterministic quantized clip scheduling:

- configurable sample rate
- configurable BPM
- 1/16-note subdivision
- canonical example: 48 kHz / 124 BPM
- clip ID
- track index
- target sample position
- activation state

Test exact boundaries and neighboring samples, BPM/sample-rate changes, repeated boundaries, long-running positions, and floating-point-to-integer error.

Do not call it sample-accurate without measured error.

## SOVEREIGN TAPE ENGINE

Build a modular tape subsystem with:

- transport
- speed
- formula
- calibration
- bias behavior
- magnetic nonlinearity/saturation
- head width
- head bump
- record/reproduce EQ
- crosstalk
- wow/flutter
- hysteresis/memory
- noise
- dropouts
- azimuth
- punch-in/punch-out behavior
- multitrack mode
- stereo mastering mode

Architecture:

`CLEAN SOURCE → TAPE MODEL → DSP → MIX/MASTER`

Four product gates:

1. TRACK TAPE
2. MIX TAPE
3. MASTER TAPE
4. GODSPEED TAPE

Godspeed controls:

`CHARACTER / WEIGHT / WIDTH / GLUE / AGE / SPEED`

Public engineering behavior from reference machines can inform the model, but the code must remain an original APEX implementation. Record source references and model assumptions separately from measured behavior.

## ARTIST LAB

Build an in-app guided laboratory that lets the artist personally test:

1. microphone input
2. recording/playback
3. channel routing
4. gain/clipping
5. round-trip latency
6. noise floor where measurable
7. pitch tracking
8. key/tonal hypotheses
9. harmony hypotheses
10. onset/rhythm extraction
11. 23-variant generation
12. variant audition/selection
13. DSP/tape processing
14. quantized launch
15. stem export
16. master export

Capture test conditions automatically where the platform permits:

- device
- input/output
- sample rate
- buffer size
- software build/commit
- test ID
- timestamp
- measurements
- result

## VERIFICATION STATE MACHINE

Every capability uses:

`SPECIFIED → INSPECTED → IMPLEMENTED → BUILT → UNIT_TESTED → INTEGRATED → RUNTIME_TESTED → MEASURED → EVIDENCE_RECORDED → VERIFIED → PROMOTED`

Failures/missing evidence remain `BLOCKED` or `UNVERIFIED`.

Never skip states in the evidence record.

## VERIFICATION MANIFEST

For each capability, emit a machine-readable manifest containing:

```text
capability_id
source_paths
commit_or_build_id
implementation_state
test_names
runtime_path
hardware_conditions
sample_rate
buffer_size
bpm
expected_metric
actual_metric
pass_fail
evidence_reference
timestamp
dependencies
limitations
```

## CLAIM-SPECIFIC MEASUREMENTS

Measure the claim you are making.

### Audio

- round-trip latency
- sample/channel routing
- clipping
- noise floor where measurable
- frequency response where measurable
- signal integrity
- LUFS
- true peak

### Musical intelligence

- pitch error
- note/event error
- key accuracy
- chord/harmony accuracy
- timing/onset error
- confidence calibration
- competing-hypothesis behavior

### Generation

- variant count
- render success
- lineage completeness
- diversity/distinctness
- deterministic/reproducible behavior where promised

### Tape

- frequency response
- nonlinear response
- harmonic behavior
- wow/flutter behavior
- noise behavior
- speed-dependent behavior
- model stability

### Scheduler

- target boundary
- timing error
- long-run drift
- parameter-change behavior

## IMPORTANT CORRECTION TO THE SUPPLIED TEST HARNESS

The existing synthetic sin/tanh harness is useful as a smoke/benchmark test, but it does **not** establish:

- router correctness
- lock-free behavior
- audio-device latency
- runtime loopback
- LUFS
- true peak
- clipping safety
- tape fidelity
- scheduler accuracy
- hardware compatibility
- MIDI synchronization
- end-to-end studio behavior

Preserve it if useful, but add component-specific tests and actual runtime evidence.

## BUILDER EXECUTION ORDER

### STEP 1 — Inspect

Map the repository and identify existing implementations before editing.

### STEP 2 — Establish contracts

Define stable interfaces for router, musical intent, hypotheses, variants, tape modules, scheduler, lab tests, audit/evidence, and export.

### STEP 3 — Build the minimum end-to-end path

Make this real first:

`MIC → RECORD → ROUTER → ANALYZE → MUSICAL INTENT → ONE VARIANT → AUDITION → EXPORT`

Do not begin by building 23 variants if the one-variant path is not executable.

### STEP 4 — Expand musical transformation

Add configurable variant generation and the canonical 23-result workflow.

### STEP 5 — Add tape/DSP gates

Integrate Track, Mix, Master, and Godspeed processing without destroying the clean source.

### STEP 6 — Add quantized transport

Connect the scheduler to the real runtime path and test measured timing.

### STEP 7 — Add the laboratory

Make the artist's actual session a guided, evidence-producing test.

### STEP 8 — Verify and promote

Run build/tests/runtime measurements. Persist evidence. Update the capability registry only for claims supported by the evidence.

## DEFINITION OF DONE

The implementation is complete only when the actual application can demonstrate, on the available studio setup:

`MIC → RECORD → ANALYZE → KEY/HARMONY HYPOTHESES → 23 VARIANTS → AUDITION → SELECT → ROUTE → DSP/TAPE → EXPORT → AUDIT`

and the evidence system can show what was actually tested.

The following are separate completion states:

`SOURCE IMPLEMENTED`
`BUILD VERIFIED`
`TEST VERIFIED`
`RUNTIME VERIFIED`
`HARDWARE VERIFIED`
`AUDIO VERIFIED`

Do not collapse them into one green badge.

## FAILURE BEHAVIOR

If a requirement cannot be verified:

1. Keep the implementation state truthful.
2. Record the exact failure or missing evidence.
3. Do not fabricate a pass.
4. Do not silently substitute a weaker test for the required test.
5. Continue with independent work that is not blocked.
6. Report the smallest concrete next action required for the blocked claim.

## FINAL BUILDER DIRECTIVE

You are not building a plugin collection. You are building a deterministic artist-operated laboratory.

Every output must be traceable to an input.
Every transformation must be reproducible or explicitly marked stochastic.
Every inference must preserve uncertainty when uncertainty exists.
Every generated result must retain lineage.
Every engineering claim must have corresponding evidence.

**Build the path. Measure the path. Record the evidence. Let the artist make the creative decision. Then promote only what the evidence supports.**
