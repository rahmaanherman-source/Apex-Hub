# APEX Morning Briefing — Learning & Drive Mode

## Purpose

The APEX Morning Briefing is an operational briefing, not a generic content feed. It should tell the owner what deserves attention today and, when useful, recommend a small amount of education that can be consumed during slower periods or hands-free while driving.

## Daily briefing structure

1. **TODAY'S PRIORITIES** — active work that matters most.
2. **WHAT CHANGED** — verified changes since the prior briefing.
3. **WATCH / ATTENTION** — verified blockers, risks, deadlines, or anomalies.
4. **MONEY / OPPORTUNITIES** — revenue lanes or opportunities that deserve attention.
5. **GABBY'S OBSERVATIONS** — recurring friction, repeated mistakes, or skills that appear to need strengthening.
6. **TODAY'S LEARNING — MAX 1–3 ITEMS** — only recommend education when it is relevant and useful; do not overwhelm the owner.
7. **IDEAS CAPTURED** — ideas heard or recorded separately from problems.
8. **DRIVE / LISTEN LATER** — an optional audio-first queue for appropriate educational material.

## Learning recommendation law

Gabby may recommend a tutorial when:

- the owner has repeatedly encountered the same technical or operational difficulty;
- a current APEX task depends on a skill the owner appears to be learning;
- a relevant official course/tutorial is available;
- there is meaningful new material worth understanding;
- activity is low enough that learning is a sensible use of time.

Gabby should NOT recommend learning merely to fill space. The queue is intentionally small.

## Activity-aware recommendations

Learning recommendations are contextual, not compulsive:

- **High operational activity:** prioritize execution; optionally save one relevant tutorial for later.
- **Low activity / waiting period:** suggest one or two useful lessons that advance an identified skill.
- **No meaningful learning need:** say nothing about learning.

Never interrupt an active revenue operation simply because a tutorial exists.

## Separate idea detection from struggle detection

APEX must not classify every user statement as a problem.

Use explicit categories:

- `LEARNING` — educational material or skill development.
- `STRUGGLE` — repeated friction or difficulty observed from actual interaction evidence.
- `IDEA` — a new concept, opportunity, or creative thought.
- `TASK` — an action requested or committed to.
- `OPPORTUNITY` — a potential revenue, business, or strategic opportunity.
- `NOTE` — useful context that does not require action.

An idea must remain an idea unless the owner asks to turn it into a task.

## Drive Mode

Drive Mode is audio-first and hands-free. When the owner is driving, APEX should avoid encouraging screen interaction.

A Drive Queue may contain:

- title;
- source/provider;
- duration;
- topic;
- why it matters;
- progress;
- whether it is appropriate for audio-only consumption;
- optional account/course context when legitimately available.

Example:

> **APEX DRIVE QUEUE — 27 min**
> - Vercel deployment fundamentals — 9 min
> - Google Cloud / BigQuery fundamentals — 11 min
> - Stripe payments/webhooks — 7 min
>
> **Why:** these map directly to active APEX work.

Do not encourage watching video while the owner is driving. Prefer audio, podcasts, spoken tutorials, or listen-later playback.

## Account-linked learning

When an educational provider exposes an authorized account connection, APEX may associate:

`ACCOUNT → COURSE → PROGRESS → SKILL → APEX TASK`

Only use account data after authorization. Never infer account access from a public URL, and never expose credentials to Gabby or the frontend.

A recommendation can say:

> “You already started this course. You're 42% through it. Today's lesson addresses the skill currently relevant to APEX.”

Only state progress when the connected provider actually supplies that evidence.

## Source priority

Prefer:

1. official provider education;
2. authorized course/account content;
3. high-quality educational sources;
4. other useful media when it clearly advances the owner's objective.

APEX should store source, title, duration, topic, URL/deep link, and evidence/observation time where available.

## Morning briefing learning rule

The briefing should explain **why** each recommendation is being surfaced:

- “You hit this deployment issue twice.”
- “This is directly relevant to today's Google Cloud work.”
- “Activity is light right now; this 12-minute lesson is useful background.”
- “You mentioned this as an idea, so I saved it separately rather than treating it as a problem.”

## NO FAKE GREEN

Learning recommendations are never proof of system capability.

Likewise:

`COMMIT OBSERVED != COMMIT SIGNATURE VERIFIED`

A commit SHA proves that a commit object was observed. Cryptographic signature verification requires actual signature/status evidence. Do not report `I_SIG VERIFIED` merely because a commit SHA exists.

## Safety / distraction rule

When Drive Mode is active:

- audio-first;
- hands-free controls;
- no requirement to visually browse the dashboard;
- defer non-urgent UI interactions;
- never encourage watching video while driving.

## Acceptance criteria

- Morning briefing includes the learning section only when useful.
- Maximum recommended daily learning items: 3.
- Learning recommendations are tied to observed work/context.
- Ideas and struggles remain separate classifications.
- Drive Queue supports audio-first consumption.
- Account-linked progress is shown only when actually authorized and observed.
- Recommendations never block revenue work.
- No educational recommendation can mutate APEX operational truth.
