# APEX Vibe Translator

## Product Identity

**Working product name:** APEX Vibe Translator
**Former working name:** APEX Universal Translator
**Primary placement:** APEX Creator / Listen experience

## Product Promise

> You hear the world in its own voice. You understand it in yours. Nothing gets lost in between.

## Design Principle

**Don't translate the culture out. Translate the meaning in.**

The system preserves the original performance while adding understandable meaning. It does not automatically normalize accents, slang, humor, profanity, emotion, cultural references, or rhythmic character into flat corporate English.

## Listen Modes

### Mode 1 — Subtitles

- Original audio remains untouched.
- Translation appears synchronized to the line.
- Listener hears the original accent, emotion, rhythm, and music.
- Translation communicates intent and meaning.

### Mode 2 — Layered Voiceover

- Original vocal remains audible at a controlled level.
- Translated voice is layered above it.
- Music bed remains intact.
- User can perceive both original character and translated meaning.

### Mode 3 — Full Dub

- Translated voice replaces the original vocal.
- Available only when the listener explicitly selects a full-dub experience.

## Vibe-Preservation Translation Contract

Translate the meaning into the listener's language without flattening the source culture. Keep slang as slang. Keep attitude. If a line is funny, make it land as funny. If it is rude, preserve the register rather than sanitizing it. If it is poetic, preserve the poetry. Do not add explanations that were not requested. Match the register of the speaker and preserve rhythm where the translation is intended to sit in the music.

The target is **transposition of meaning and energy**, not literal word replacement.

## Register Profiles

The translator should support configurable profiles including:

- Street
- Poetic
- Funny
- Angry
- Romantic
- Hype
- Formal
- Conversational
- Educational

## Audio Architecture

```text
SOURCE AUDIO
    |
    +--> ORIGINAL VOCAL --------------------+
    |                                        |
    +--> SPEECH / LYRIC TRANSCRIPTION        |
                |                            |
                v                            |
        VIBE-PRESERVATION ENGINE             |
                |                            |
                v                            |
        TRANSLATED MEANING                   |
                |                            |
        +-------+-------+                    |
        |       |       |                    |
     SUBTITLE  LAYERED  FULL DUB             |
        |       |       |                    |
        +-------+-------+--------------------+
                        |
                        v
                  LISTEN OUTPUT
```

## Agent Parameters

Recommended runtime parameters:

```json
{
  "source_language": "auto",
  "target_language": "en",
  "mode": "subtitles",
  "vibe_mode": "street",
  "preserve_slang": true,
  "preserve_profanity": true,
  "preserve_attitude": true,
  "preserve_humor": true,
  "preserve_poetry": true,
  "preserve_rhythm": true,
  "original_audio_intact": true
}
```

## Product Boundary

The Vibe Translator is a listening/translation system. It does not require changing the source recording into a sanitized replacement. Original audio remains a first-class asset.

## Evaluation

Evaluate translations against:

- Meaning fidelity.
- Cultural/register fidelity.
- Slang preservation.
- Emotional fidelity.
- Rhythm/pocket compatibility.
- Listener comprehension.
- Original-vocal preservation.

The benchmark should compare all three modes and document where each mode gains or loses fidelity.
