# APEX REGRESSION MEMORY

**STATUS: LOCKED**

## Permanent memory

A marked, frozen, watermarked, owner-approved, verified UI/runtime state is a **reference floor**.

It is not merely a record saying "this was okay."

It means:

> **THIS WAS ACCEPTED. DO NOT GO BELOW THIS MARK.**

The system may improve above the mark. It may not silently degrade below it.

## Memory rule

```text
KEEP WHAT MATTERS.
MERGE WHAT'S THE SAME.
ADD WHAT'S NEW.
LINK WHAT'S CONNECTED.
LEAVE THE REST IN THE ARCHIVE.
```

The regression floor is something that matters and must remain active memory because it protects future decisions from repeating an already rejected downgrade.

## Baseline memory object

Each protected baseline should eventually record:

- baseline_id
- system/repository
- surface/component
- version or commit
- approval state
- verification evidence
- screenshot/reference evidence where applicable
- protected characteristics
- known limitations
- superseded_by, if any
- rollback/reference location

## Ratchet

```text
APPROVED BASELINE
      ↓
   WATERMARK
      ↓
      FLOOR
      ↓
EQUAL OR BETTER ONLY
      ↓
NEW APPROVED BASELINE
```

## Regression response

If a future change is below the remembered baseline:

1. Detect the difference.
2. Mark `REGRESSION`.
3. Stop release/publish when practical.
4. Compare with the remembered baseline.
5. Restore the baseline or produce an explicitly approved equal-or-better replacement.
6. Record the outcome.

Never normalize a regression simply because a newer implementation compiles or looks different.

## Canonical statement

> **A watermark is a mark in the ground. It tells APEX where the accepted floor is. The mark may move upward only through explicit approval and verification. It never moves downward by accident, simplification, responsive drift, redesign, dependency change, or AI-generated modification.**

**GODSPEED.**
