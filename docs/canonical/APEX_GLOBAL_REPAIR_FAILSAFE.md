# APEX GLOBAL REPAIR FAIL-SAFE

**Status: CANONICAL — GLOBAL APEX/GABBY BEHAVIOR**  
**Purpose:** Prevent AI troubleshooting, repair, audit, and build flows from losing the user's place, repeating failed fixes, or making uncontrolled repository changes.

## 1. CORE LAW

When APEX/Gabby proposes a repair, the system must treat the repair as a **guided investigation**, not a one-shot instruction.

The user must always know:

- what was found;
- what fix is being attempted now;
- where they are in the investigation;
- how much time remains for the current step;
- how to stop the current step;
- how to continue to the next step;
- how to contact Gabby and report that the step did not work;
- what the next step will be if the current step fails;
- that their current place, evidence, and investigation history are preserved.

## 2. REQUIRED REPAIR STATE

Every repair investigation has a persistent state object, conceptually:

```text
RepairSession
  sessionId
  issueId
  title
  scope
  currentStep
  totalSteps
  steps[]
  evidence[]
  attemptedFixes[]
  failedFixes[]
  successfulFixes[]
  userNotes[]
  checkpoint
  timer
  status
  nextStep
  lastKnownGoodState
  sourceFiles[]
  auditEvents[]
```

The exact storage mechanism may vary by application, but the state must survive UI re-rendering, navigation, modal close/open, and ordinary refresh where the platform permits.

## 3. THE 60-SECOND FIX WINDOW

Every actionable repair step gets a default **60-second observation window** unless the repair itself requires a different duration.

At step start, show:

- `FIX #N` / `STEP N OF M`;
- concise diagnosis;
- exact action to perform;
- visible countdown from 60 seconds;
- `STOP` button;
- `CONTINUE` button;
- `CONTACT GABBY` button;
- `NEXT STEP READY` indicator.

The timer is a user-assistance window, not a hard destructive timeout. When it reaches zero, the system must **not** silently mutate the repository or automatically jump to a destructive action.

At zero:

```text
CURRENT STEP PAUSED

Did this fix work?
[ YES — VERIFY ] [ NO — NEXT STEP ] [ CONTACT GABBY ]
```

## 4. USER CONTROL

### STOP

Stops the current repair activity and freezes the investigation state.

STOP must preserve:

- current step;
- timer value;
- evidence;
- instructions already shown;
- attempted actions;
- next-step recommendation;
- exact investigation location.

### CONTINUE

Resumes the same step from the preserved state. It does not restart the investigation from Step 1.

### CONTACT GABBY

Opens Gabby in the same repair context with the session automatically attached. The user must not have to reconstruct what they were doing.

Gabby should receive:

```text
Issue
Current step
What the user was instructed to do
What was attempted
Observed result
Evidence
Previous failures
Next candidate fix
```

### NEXT STEP

Advances only after the current step is explicitly marked unsuccessful or otherwise determined not to resolve the issue.

The previous step remains in the audit history.

## 5. NEVER LOSE THE USER'S PLACE

The repair UI must use a checkpoint model.

Example:

```text
Investigation: Dock Labels Missing

STEP 1 / 4 — Check viewport overflow
[60s]

Status: IN PROGRESS
Evidence: screenshot-001

NEXT READY:
STEP 2 — Check CSS overflow/clipping
```

If the user leaves the screen and returns, reopen the exact checkpoint instead of resetting the investigation.

If Gabby is contacted during a step, return to the same step after the conversation.

If a fix fails, the system must say exactly where the investigation stopped and keep the next repair ready.

## 6. FALLBACK LADDER

Repairs must be ordered from least invasive to most invasive.

### FIX 1 — Observe / Verify

Check the runtime, viewport, state, configuration, or user-visible symptom before changing code.

### FIX 2 — Targeted Local Correction

Change only the smallest known source responsible for the defect.

### FIX 3 — Component-Level Correction

Correct the component or service boundary when the local correction is insufficient.

### FIX 4 — Integration / Configuration Correction

Inspect routing, build configuration, environment configuration, dependency wiring, API contracts, or provider connections.

### FIX 5 — Repository-Level Repair

Use only when evidence shows that the defect crosses component boundaries or the repository structure itself is responsible.

### FIX 6 — Recovery / Rollback

Return to the last known good state when a change introduces regression or evidence becomes contradictory.

### FIX 7 — STOP AND REPORT

If no supported repair path remains, stop. Report the exact investigation boundary, evidence examined, fixes attempted, and what is still unknown.

**No random changes. No blind repository rewrites. No endless mutation loop.**

## 7. EVIDENCE BEFORE ESCALATION

Before advancing to a materially different repair, record:

- exact symptom;
- expected behavior;
- observed behavior;
- file/component suspected;
- command or interaction performed;
- result;
- screenshot/log/error when available;
- whether the step changed source code;
- verification result.

A failed fix is useful evidence and must never be discarded.

## 8. PREPARE THE NEXT STEP BEFORE LEAVING THE CURRENT STEP

The next candidate repair must be computed/displayed before the current step ends.

The user should always see:

```text
CURRENT: Fix #1
NEXT: Fix #2 — ready
BACKUP: Last known good state saved
```

This prevents the user from losing their place and prevents Gabby from forgetting the investigation sequence.

## 9. NO-FAKE-GREEN REPAIR RULE

A repair is not successful because:

- code was edited;
- a file exists;
- a build command was launched;
- a screenshot looks correct;
- an AI said "fixed".

A repair is successful only after the relevant behavior is exercised and verified.

Required verification path:

`INSPECT → CHANGE → BUILD → TEST → RUN → INTERACT → VISUAL-CHECK → EVIDENCE → REPORT`

For deployment-related repairs:

`BUILD → TEST → DEPLOY → LIVE URL → OPEN → INTERACT → VERIFY`

## 10. REPOSITORY SAFETY

Before any source mutation:

1. identify the repository;
2. identify branch and current revision;
3. inspect relevant files;
4. identify the smallest safe change;
5. preserve a rollback/checkpoint;
6. make the change;
7. build/test;
8. verify runtime behavior;
9. record evidence.

Never overwrite unrelated working features to solve an isolated defect.

Never create duplicate Gabby runtimes, duplicate command systems, or competing repair states.

## 11. GLOBAL UI REQUIREMENTS

The repair controller must be usable on:

- desktop;
- tablet;
- phone;
- mouse;
- keyboard where supported;
- touch.

The controller must not cover the primary work area.

The UI must preserve the complete workspace and obey the canonical whole-workspace navigation contract.

## 12. AUDIT TRAIL

Every repair session records an append-only event sequence conceptually:

```text
SESSION_CREATED
STEP_STARTED
USER_ACTION_RECORDED
TIMER_STARTED
TIMER_PAUSED
USER_STOPPED
USER_CONTINUED
CONTACT_GABBY
STEP_FAILED
STEP_VERIFIED
STEP_ADVANCED
ROLLBACK
SESSION_PAUSED
SESSION_RESUMED
SESSION_COMPLETED
SESSION_BLOCKED
```

Each event should include timestamp, session ID, step number, actor, action, result, and available evidence.

## 13. GABBY BEHAVIOR CONTRACT

Gabby must:

- explain one actionable step at a time;
- preserve the full repair context;
- avoid hallucinating repository state;
- distinguish observed facts from hypotheses;
- never claim success without verification;
- never discard a failed attempt;
- prepare the next step before waiting;
- let the user stop without losing their place;
- let the user continue without restarting;
- let the user contact Gabby without re-explaining the problem;
- escalate only when evidence supports escalation.

## 14. ACCEPTANCE TESTS

A repair flow fails acceptance if any of the following occurs:

- the timer is absent when a timed observation window is required;
- STOP loses the investigation location;
- CONTINUE restarts from Step 1;
- CONTACT GABBY opens without the current repair context;
- NEXT STEP is unavailable after a failed fix;
- the next step is not preserved;
- failed attempts disappear from the audit history;
- the system silently mutates the repository when the timer expires;
- the AI claims success without runtime verification;
- the user must repeat information already captured in the session;
- an isolated repair breaks unrelated working functionality;
- the UI hides required repair controls on a smaller viewport.

## 15. REFERENCE FLOW

```text
USER REPORTS PROBLEM
        ↓
CREATE REPAIR SESSION
        ↓
INSPECT + CAPTURE EVIDENCE
        ↓
PREPARE FIX #1 + FIX #2
        ↓
START FIX #1
        ↓
60-SECOND USER WINDOW
   ↙        ↓        ↘
STOP    CONTINUE   CONTACT GABBY
   ↓        ↓        ↓
PAUSE    SAME STEP  SAME CONTEXT
        ↓
VERIFY RESULT
   ↙        ↘
YES         NO
 ↓           ↓
VERIFY     RECORD FAILURE
 ↓           ↓
DONE     ADVANCE TO FIX #2
             ↓
       60-SECOND WINDOW
             ↓
          REPEAT
             ↓
     EXHAUSTED / BLOCKED
             ↓
      EXACT STOP + REPORT
```

**APEX LAW:** Fix the problem without losing the person's place. Preserve evidence. Give the user control. Keep the next move ready. Verify before declaring victory.
