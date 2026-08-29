# APEX SOVEREIGN AUDIO STUDIO — MASTER SPECIFICATION

**Status:** CANONICAL DESIGN / BUILDER HANDOFF
**Priority:** AUDIO ONLY — CURRENT PHASE
**Future destination:** APEX 360 unified audio/video suite
**Verification law:** No-Fake-Green

## 1. Mission

Build a personal, artist-first sovereign audio studio. The immediate objective is to lock down the audio creation system so the artist can record, hear, analyze, transform, arrange, mix, master, and export without depending on a conventional DAW workflow for the core creative intelligence.

Video/vision features are deferred from this phase. The completed audio subsystem must later be portable into APEX 360 as its audio pillar.

The studio is not merely a plugin collection. It is a programmable audio creation environment with deterministic DSP, musical analysis, tape-character processing, AI-assisted transformation, quantized transport, routing, recording, and evidence-backed verification.

## 2. Artist-first interaction model

The primary loop is:

`CAPTURE → UNDERSTAND → TRANSFORM → HEAR → CHOOSE → BUILD → EXPORT`

The artist must be able to:

- Record vocals, humming, whistling, harmonies, instruments, Foley, and room material.
- Immediately audition the captured material.
- Ask the AI what the material suggests musically.
- Generate alternate musical interpretations without losing the original performance.
- Compare variants side-by-side.
- Keep the original recording and every selected/generated derivative as separate assets.
- Export clean stems, processed stems, MIDI/Music representations where applicable, and final mixes.

## 3. Harmony-to-Instrument Intelligence — CORE REQUIREMENT

### User action

The artist can sing or hum a melody/harmony into the microphone and say, for example:

> "I kind of hear this. Give me 23 different results. Try horns, flutes, strings, and other instruments."

The system must treat the vocal performance as a musical signal, not merely as audio to be replayed.

### Analysis pipeline

`MIC INPUT`
→ pitch tracking
→ note/event extraction
→ onset detection
→ timing/rhythm extraction
→ tonal-center estimation
→ key/scale hypothesis
→ interval analysis
→ chord/harmony hypothesis
→ phrase/contour representation
→ confidence scores
→ musical representation

The representation should preserve, where detectable:

- fundamental frequency / pitch
- note names
- cents deviation
- octave
- note duration
- onset/offset
- intervals
- melodic contour
- harmonic intervals
- chord candidates
- tonal center
- key candidates
- scale/mode candidates
- tempo/rhythm relationship
- phrase boundaries
- confidence per inference

Do not pretend ambiguous audio has one certain answer. Store competing hypotheses with confidence and allow the artist to choose or override them.

### Musical transformation

The analyzed performance becomes a reusable musical intent object that can drive:

- MIDI generation
- synthesized instruments
- sampled instruments
- orchestration
- harmony generation
- counter-melody generation
- chord voicing
- bass interpretation
- horn arrangements
- flute/woodwind arrangements
- string arrangements
- keyboard/piano arrangements
- guitar/bass interpretations
- percussion interpretations
- hybrid/neural instrument interpretations

### Variant generation

The default creative request supports **23 variants**. The number must be configurable, but 23 is the canonical example/test case.

Example result set:

1. Trumpet
2. Trombone
3. French horn
4. Saxophone
5. Flute
6. Clarinet
7. Oboe
8. Violin
9. Viola
10. Cello
11. Contrabass
12. Piano
13. Electric piano
14. Organ
15. Acoustic guitar
16. Electric guitar
17. Bass
18. Synth lead
19. Analog pad
20. Plucked synth
21. Mallet instrument
22. Hybrid/neural instrument
23. Full ensemble arrangement

The list is an example realization set, not a limitation. The AI must accept natural-language direction such as:

- "Make it darker."
- "Give me 23 versions but keep my exact rhythm."
- "Keep the melody and change only the instrument."
- "Turn this harmony into a horn section."
- "Try a flute version in the same key."
- "Give me three versions that sound like a film score."

Every transformation must preserve a link to the source performance and record the transformation parameters.

## 4. Tape Recorder Research → APEX Tape Engine

Do not build literal proprietary clones. Extract publicly documented engineering behaviors and implement an original modular tape subsystem.

### Reference architectures

**OTARI / MTR-series → TRACK / TRANSPORT**

The researched MTR-90III reference includes a professional 2-inch, 24-track architecture, 15/30 IPS, optional 7.5/15 IPS configuration, independent head azimuth adjustment, AES/NAB/IEC EQ options, punch-in/punch-out behavior, approximately 24 dB headroom, documented 70 dB S/N at 30 IPS under specified conditions, and published wow/flutter figures of approximately ±0.04% at 30 IPS and ±0.05% at 15 IPS.

**STUDER A80 → RECORD / MIX**

Reference characteristics include 1/4-inch and 1/2-inch configurations, 7.5/15 IPS and 15/30 IPS variants, NAB/CCIR equalization, and engineering behavior around tape speed, frequency response, noise, distortion, equalization, tape tension, and transport.

**AMPEX ATR-102 → MASTER / CHARACTER**

Reference characteristics include 1/4-inch and 1/2-inch head configurations, 3.75/7.5/15/30 IPS, multiple tape formulations, variable head width, speed-dependent frequency response and saturation, head-bump behavior, and tape coloration/distortion.

The existing research notes the useful musical distinction that 15 IPS generally emphasizes more low-frequency head bump/warmth while 30 IPS is generally cleaner/flatter with lower noise. Treat this as a reference behavior to model and measure, not as a guarantee of hardware equivalence.

### APEX tape modules

Implement independent modules for:

- TapeTransport
- TapeSpeed
- TapeFormula
- TapeLevelCalibration
- BiasModel
- TapeNonlinearity / MagneticSaturation
- HeadWidth
- HeadBump
- TapeEQ / RecordEQ / ReproduceEQ
- Crosstalk
- WowFlutter
- Hysteresis / memory behavior
- TapeNoise
- Dropouts
- Azimuth
- PunchInPunchOut
- StereoMasterMode
- MultitrackMode

### Four musical gates

**GATE 1 — TRACK TAPE**

Otari-inspired multitrack behavior for individual tracks.

**GATE 2 — MIX TAPE**

Studer-inspired recording/reproduction behavior on stems or mix buses.

**GATE 3 — MASTER TAPE**

ATR-inspired stereo mastering behavior.

**GATE 4 — GODSPEED TAPE**

APEX-original musical controls abstract the engineering underneath:

- CHARACTER: Clean → Destroy
- WEIGHT: Thin → Massive
- WIDTH: Focused → Wide
- GLUE: Separate → Unified
- AGE: Master → Vintage
- SPEED: 7.5 → 15 → 30 IPS

Gabby may translate artist language into underlying engineering parameters, while the artist retains direct control when desired.

## 5. Core audio signal architecture

`AUDIO INPUT`
→ `SOVEREIGN AUDIO ROUTER`
→ `TRACK TAPE`
→ `DSP / MIX BUS`
→ `MIX TAPE`
→ `MASTER BUS`
→ `MASTER TAPE`
→ `GODSPEED OUTPUT`
→ `DIGITAL MASTER`

Cross-cutting services:

- Harmony & Instrument Intelligence
- Move Music Scheduler
- Culinary/ASMR DSP
- AI generation/orchestration
- Gabby control
- Audit Feed
- Evidence storage
- Export system

## 6. Existing Stage 3–5 source claims — corrected status

The supplied source implementations are source-level material only until actually compiled and executed.

### SovereignAudioRouter

Target:

- 8 stereo auxiliary buses
- configurable gain
- playback state
- sample-position tracking
- bounded block processing
- no heap allocation in the processing function
- deterministic output initialization
- saturation stage
- null/size handling

Important engineering rule: atomics alone do not prove the entire audio path is lock-free or race-free. The producer/consumer ownership of the audio buffers must be established and tested.

### CulinaryASMRProcessor

Currently represented behavior:

- 80 Hz high-pass
- voice-sidechain detection
- ducking
- stereo-width processing

The current supplied source does **not** contain a dedicated high-frequency transient-enhancement stage. Do not label that feature implemented until such a stage exists and is tested.

### QuantizedScheduler

Target:

- configurable sample rate
- configurable BPM
- 1/16-note scheduling
- deterministic target sample position
- clip/track event generation

Test the exact boundary, immediately before, immediately after, multiple boundaries, BPM changes, sample-rate changes, and long-running sample positions. Measure floating-point-to-integer quantization error rather than calling the result automatically sample-accurate.

### Audio verification harness

The supplied harness only demonstrates that a synthetic sin/tanh loop executes and produces non-NaN samples. It does not prove the router, Culinary DSP, scheduler, audio-device latency, loopback, LUFS, true peak, clipping behavior, or hardware integration.

## 7. Verification architecture

No-Fake-Green is mandatory.

`SPECIFICATION`
→ `FILE/REPOSITORY INSPECTION`
→ `IMPLEMENTATION`
→ `BUILD`
→ `UNIT TEST`
→ `INTEGRATION TEST`
→ `RUNTIME EXECUTION`
→ `AUDIO MEASUREMENT`
→ `MEASURED EVIDENCE`
→ `AUDIT RECORD`
→ `VERIFIED`
→ `PROMOTION`

Required status distinctions:

- SOURCE IMPLEMENTED
- BUILD VERIFIED
- TEST VERIFIED
- RUNTIME VERIFIED
- HARDWARE VERIFIED
- AUDIO VERIFIED

Never promote one state merely because an earlier state passed.

## 8. Artist-controlled laboratory verification

The studio must be testable by the artist using the actual microphone, interface, speakers/headphones, DAW/device path, and app runtime available in the studio.

The verification interface should provide guided tests for:

- microphone input
- recording/playback
- round-trip latency
- channel routing
- gain staging
- clipping/overload
- noise floor
- frequency response where measurable
- pitch tracking
- key/tonal-center inference
- harmony detection
- timing/onset detection
- quantized launch
- tape processing
- stem export
- master export

The app should record test conditions and results into the audit trail. The artist is the final practical evaluator of musical usefulness, while objective measurements establish technical claims.

## 9. AI Builder instruction — EXACT HANDOFF

Build the **APEX SOVEREIGN AUDIO STUDIO** as a first-class audio creation runtime.

Do not build a generic DAW clone. Do not build a collection of disconnected plugins. Do not create duplicate subsystems when an existing APEX capability can satisfy the requirement.

Current scope is AUDIO ONLY. Defer video/vision work. The completed audio architecture must be portable into APEX 360 later.

Implement the system around these pillars:

1. Real-time Sovereign Audio Router.
2. Artist microphone capture and playback.
3. Harmony & Instrument Intelligence that converts singing/humming into a structured musical representation.
4. Key, pitch, note, interval, chord, tonal-center, scale, rhythm, onset, and phrase inference with confidence scores.
5. Natural-language AI transformation requests.
6. Configurable multi-variant generation with 23 variants as the canonical demonstration.
7. Instrument realization across horns, flutes/woodwinds, strings, keys, guitars, bass, synths, mallets, neural/hybrid instruments, and ensembles.
8. Preserve the original performance and maintain lineage for every generated variant.
9. Move Music quantized scheduling.
10. Culinary/ASMR DSP with truthful feature labels.
11. APEX Sovereign Tape Engine using original implementations derived from public engineering behavior references for Otari/MTR, Studer A80, and Ampex ATR-102.
12. Track, Mix, Master, and Godspeed Tape gates.
13. Audit Feed and evidence recording.
14. Artist-operated verification laboratory.
15. WAV/stem/master export and machine-readable project metadata.

Real-time audio threads must not allocate heap memory. Any shared-state design must document ownership and synchronization. Do not call a system lock-free unless the concurrency model proves it.

Do not claim true-peak, LUFS, latency, hardware, MIDI, transport, synchronization, or artifact-free behavior without corresponding measurements.

For every capability, produce:

`path → purpose → implementation status → test → runtime status → evidence → dependencies → relationships`

Before creating files, inspect the repository for existing equivalents of:

- SovereignAudioRouter
- CulinaryASMRProcessor
- QuantizedScheduler
- AudioHarness
- Harmony/Instrument Intelligence
- Tape/DSP modules
- AuditBus
- verification infrastructure
- MIDI/transport/audio-device infrastructure

Merge with existing implementations instead of creating duplicates.

## 10. Acceptance criteria

The build is not considered complete because source files exist.

The audio core is complete only when the actual runtime can demonstrate:

- record → playback
- vocal/hummed input → musical analysis
- analysis → key/note/harmony hypotheses
- analysis → 23 instrument realizations
- AI text direction → controlled musical variants
- variant audition → selection
- selected result → stem/export path
- router → DSP → tape → master path
- quantized clip launch
- audit evidence for each tested capability

The artist must be able to perform these operations from the studio without manually reconstructing the engineering pipeline.

## 11. Architectural identity

`APEX = CONTROL / GOVERNANCE`

`GABBY = ARTIST-FACING INTELLIGENCE / ORCHESTRATION`

`GODSPEED ENGINE = AUDIO RUNTIME`

`APEX SOVEREIGN AUDIO STUDIO = CREATIVE AUDIO EXPERIENCE`

`APEX 360 = FUTURE UNIFIED AUDIO + VIDEO SUITE`

The system must preserve provider independence and keep the musical source/performance owned by the project rather than bound to a particular AI model or external service.

## 12. Final lock

**Decision:** Bring the tape-engine architecture into the studio as a first-class signal-processing subsystem.

**Decision:** Make sung/hummed harmony analysis into instrument transformation a first-class creative capability.

**Decision:** Make 23-result orchestration a canonical demonstration of the AI musical transformation layer.

**Decision:** Keep audio as the current engineering scope; defer vision/video.

**Decision:** Carry the completed audio architecture into APEX 360 later.

**Decision:** Verification must follow evidence, not documentation claims.

**Status of this document:** CANONICAL BUILDER SPECIFICATION. The requirements above are the target. Individual runtime capabilities remain subject to the No-Fake-Green verification states defined above.
