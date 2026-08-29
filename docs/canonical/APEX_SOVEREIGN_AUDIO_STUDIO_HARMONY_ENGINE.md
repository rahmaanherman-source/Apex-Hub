# APEX Sovereign Audio Studio — Harmony & Instrument Intelligence

**Status:** CANONICAL PRODUCT/ENGINE REQUIREMENT  
**Scope:** APEX 360 Audio Studio  
**Primary purpose:** Give the artist a direct creation workflow in which a sung/hummed idea can be analyzed, harmonized, transformed into instrument arrangements, and auditioned as multiple musical alternatives without leaving the studio.

---

## 1. Product Principle

APEX Sovereign Audio Studio is being built **for the artist's actual creative workflow first**. The audio engine is the priority before broader APEX 360 vision work.

The system must let the artist record an idea with ordinary studio hardware (for example, a USB microphone), analyze the musical information contained in the performance, and immediately turn that idea into usable musical material.

The artist remains the creative authority. AI proposes; the artist selects, edits, rejects, records, and creates.

---

## 2. Core Creative Workflow

### Input

The artist may provide:

- sung melody
- hummed melody
- harmony/vocal stack
- whistle or other pitched vocalized idea
- short melodic phrase
- MIDI
- existing audio stem
- recorded instrument phrase

### Analysis

The engine should derive, where supported by the source signal:

- fundamental frequency / pitch trajectory
- note sequence
- timing/onset information
- tempo relationship
- probable key / tonal center
- scale/mode candidates
- intervals
- chord/harmony candidates
- rhythmic pattern
- phrase boundaries
- confidence scores

The engine must preserve uncertainty. A detected key, chord, or instrument classification is a **candidate result**, not a fact, until confidence/selection rules establish it.

### Generation

From one artist idea, the user can request multiple arrangements, including a target of **23 distinct results** for exploratory sessions.

Examples of arrangement families:

- horns
- flute / woodwind
- strings
- piano
- electric piano
- organ
- synth
- guitar
- bass
- mallet/percussion
- orchestral textures
- hybrid/experimental instruments

The system should be able to preserve the original musical contour while changing instrumentation, register, voicing, articulation, rhythm, or harmonic interpretation.

---

## 3. The "I Hear This" Interaction

The studio must support an artist-directed prompt such as:

> "I kind of hear this — give me 23 different results."

The system converts that request into a structured generation job rather than requiring the artist to know technical music-production terminology.

Each result should expose:

- instrument/arrangement identity
- detected key/tonal center
- tempo
- chord or note representation where available
- variation description
- confidence / analysis status
- audition control
- keep/reject/favorite action
- export/render action

The artist can then say or select things such as:

- "Give me more horns."
- "Keep the melody but change the chords."
- "Make it darker."
- "Try flute instead."
- "Give me five versions with the same rhythm."
- "Transpose it two semitones."

---

## 4. Music Is Structured Data

APEX should treat a musical idea as more than an audio waveform.

A useful internal representation is:

`Audio → Features → Notes/Intervals → Timing → Tonal Candidates → Harmony Candidates → Arrangement Graph → Rendered Audio`

Pitch can be represented as frequency and/or MIDI-style note numbers. Intervals, rhythmic subdivisions, voicings, and instrument mappings can therefore be computed, compared, transformed, and regenerated.

This is the scientific/engineering basis for the feature: the system does not need to "guess music from nothing" when the source contains measurable pitch, timing, spectral, and harmonic information.

---

## 5. Preserve the Artist's Original

Every creative transformation must be non-destructive.

Required asset lineage:

`RAW TAKE → ANALYSIS → MUSICAL REPRESENTATION → VARIANTS → SELECTED ARRANGEMENT → STEMS → MIX → EXPORT`

The original recording is never silently replaced.

The artist must be able to return to the raw performance and regenerate alternate interpretations.

---

## 6. Audio Engine Integration

This feature belongs inside the Sovereign Audio Studio core rather than being a detached chatbot feature.

It must integrate with:

- real-time audio routing
- vocal recording
- stem management
- quantized transport
- DSP processing
- monitoring
- arrangement/session state
- render/export
- APEX 360 orchestration
- audit/evidence recording

The previously supplied Stage 3–5 DSP components (summing router, Culinary ASMR processor, quantized scheduler, and test harness) are treated as **source implementations supplied for integration**, not automatically as runtime-verified components.

Verification remains claim-specific:

`SOURCE IMPLEMENTED → BUILD VERIFIED → TEST VERIFIED → RUNTIME VERIFIED → HARDWARE VERIFIED`

No status may be promoted merely because a source file or documentation says it passed.

---

## 7. Artist-Owned Control Surface

The first usable studio surface should make the following actions obvious:

1. **Record**
2. **Analyze**
3. **Find Key**
4. **Find Notes**
5. **Find Harmony**
6. **Generate 23**
7. **Audition**
8. **Compare**
9. **Keep**
10. **Turn Into Instrument**
11. **Create Stems**
12. **Export**

The interface should minimize configuration before the first creative result.

---

## 8. Tape / Recorder Direction

Analog tape and recorder behavior belongs in the studio as a **creative processing and capture layer**, not as a replacement for the clean source.

Future tape-oriented processing should be modeled as measurable parameters such as:

- tape speed
- saturation
- hysteresis/nonlinearity
- wow
- flutter
- noise floor
- frequency response
- head/record/replay coloration
- compression behavior
- bias-related coloration
- crosstalk
- transport instability

Any specific tape-machine specification must be sourced and recorded separately before being represented as a verified hardware/model profile.

---

## 9. Acceptance Criteria

A future implementation is successful when the artist can perform this end-to-end session:

1. Plug in a microphone.
2. Record a short melody/harmony.
3. Press **Analyze**.
4. Receive measurable pitch/note/timing information and tonal candidates.
5. Request multiple musical interpretations.
6. Generate up to 23 arrangement candidates for audition.
7. Hear the same idea expressed through different instruments/voicings.
8. Keep one or more candidates without destroying the original.
9. Convert the selected result into editable musical/stem material.
10. Continue writing/recording against the result.
11. Render/export the finished work.
12. Preserve the full asset lineage and audit record.

### Verification requirement

The artist's successful hands-on session is a valid **user acceptance test**, but it must be recorded as evidence separately from source-level claims and automated benchmarks.

---

## 10. APEX 360 Relationship

This audio system is a foundational subsystem of the eventual **APEX 360 suite**.

The intended relationship is:

`APEX 360 → Sovereign Audio Studio → Recording / Analysis / Harmony / Arrangement / DSP / Mixing / Export`

The studio should remain useful as a standalone creative environment while exposing clean capabilities to the broader APEX 360 control plane.

---

## 11. No-Fake-Green Rule

The following claims require actual evidence before being marked verified:

- pitch/key detection accuracy
- harmony detection accuracy
- instrument identification accuracy
- 23-result generation capability
- MIDI/note extraction
- timing/quantization accuracy
- real-time latency
- DSP signal integrity
- LUFS compliance
- true-peak compliance
- tape-model fidelity
- hardware I/O behavior
- microphone/driver compatibility
- DAW/MIDI synchronization
- end-to-end render/export

**Documentation is the specification. The artist's lab session and machine/runtime evidence establish whether the specification works.**

---

## 12. Canonical Product Decision

**LOCKED DIRECTION:** Build the audio studio around the artist's ability to capture an idea and immediately explore what that idea can become.

The differentiating loop is:

**CAPTURE → UNDERSTAND → TRANSFORM → HEAR → CHOOSE → BUILD → EXPORT**

The system is not merely an AI music generator. It is an artist-controlled musical reasoning and production instrument inside APEX 360.
