# APEX REPO FAILSAFE v1.0

**Status:** ACTIVE SPECIFICATION
**Purpose:** Prevent AI work from stopping early, skipping repositories, inventing missing information, overwriting verified work, or declaring incomplete work complete.

## GOLDEN RULE

> **NEVER STOP BECAUSE ONE THING IS BROKEN.**
>
> Find it. Classify it. Fix it when safe. Test it. Record it. Then keep moving through the entire system.
>
> Never invent what is unknown. Never call unverified work complete. Never throw away verified work. Never lose the evidence. Never leave a discovered gap unclassified.

---

## 1. SOURCE-OF-TRUTH LAW

Actual repository state outranks AI assumptions, old conversations, screenshots, unchecked dashboards, and generated summaries.

Canonical architecture and approved specifications define **what should exist**.

Actual code, configuration, tests, commits, and deployment evidence determine **what actually exists**.

Never confuse the two.

---

## 2. NO-FAKE-GREEN

These states are distinct:

- `UNKNOWN`
- `MISSING`
- `BLOCKED`
- `FAILED`
- `PARTIAL`
- `IMPLEMENTED`
- `TESTED`
- `VERIFIED`
- `DEPLOYED`
- `PRODUCTION_VERIFIED`

Never convert:

- `UNKNOWN` → `GREEN`
- claimed → verified
- code exists → works
- checkbox → proof
- build succeeds → feature verified

A failure remains a failure until evidence proves otherwise.

---

## 3. REPOSITORY DISCOVERY

Before modifying a system, enumerate every **authorized** repository in scope.

For each repository record:

1. Repository name and URL.
2. Default/current branch.
3. Current commit SHA.
4. Working/deployment state when available.
5. Language and framework.
6. Build system.
7. Test system.
8. Deployment target.
9. Major modules.
10. Integrations.
11. Configuration sources.
12. Canonical documentation.
13. Relationships to other repositories.

**No authorized repository may silently disappear from the audit.**

---

## 4. CROSS-REPOSITORY MAP

Build and maintain a dependency map:

`REPO → MODULE → SERVICE → API → DATABASE → AUTH → INTEGRATION → DEPLOYMENT`

Trace, when applicable:

- imports
- API calls
- environment variables
- database tables
- webhooks
- queues
- shared packages
- routes/deep links
- OAuth clients
- service accounts
- deployment configuration
- documentation references

If Repo A depends on Repo B, record the relationship. If Repo B is unavailable, mark the dependency `BLOCKED` or `MISSING`; do not invent it.

---

## 5. GAP DETECTION

For every requirement ask:

`EXPECTED → ACTUAL → EVIDENCE → GAP`

Classify every discovered gap as one of:

- `CODE_MISSING`
- `CODE_INCOMPLETE`
- `CODE_BROKEN`
- `CONFIG_MISSING`
- `CONFIG_INVALID`
- `DEPENDENCY_MISSING`
- `INTEGRATION_MISSING`
- `DOCUMENTATION_MISSING`
- `TEST_MISSING`
- `TEST_FAILING`
- `DEPLOYMENT_MISSING`
- `REFERENCE_BROKEN`
- `DUPLICATE`
- `LEGACY`
- `UNKNOWN`
- `HUMAN_INPUT_REQUIRED`

---

## 6. MISSING-CODE PROTOCOL

When required code is missing, do not immediately invent an implementation.

First determine:

- Is the requirement canonically specified?
- Does another authorized repository contain the implementation?
- Does another module already implement it?
- Is there a partial implementation?
- Is the missing code actually unnecessary because the architecture changed?
- Is a dependency preventing implementation?

Preferred order:

`EXISTING → REUSE`

`PARTIAL → COMPLETE`

`DUPLICATE → CANONICALIZE`

`LEGACY → MIGRATE/RETIRE ONLY WHEN AUTHORIZED`

`MISSING → IMPLEMENT`

`UNKNOWN → INVESTIGATE`

---

## 7. MISSING-INFORMATION PROTOCOL

Separate work into three categories.

### AI CAN DETERMINE

Investigate automatically.

### AI CAN RECOVER

Search authorized repositories, files, docs, history, and existing evidence.

### HUMAN MUST PROVIDE

Record `HUMAN_INPUT_REQUIRED` with the exact missing input and what it blocks.

A missing credential, approval, or external artifact must **not** stop unrelated audit work.

Example:

```text
BLOCKED: production credential
Blocks: live integration verification
Does NOT block: schemas, UI, local tests, documentation, unrelated repositories
```

---

## 8. REPAIR LOOP

For every safe executable repair:

`FIND → UNDERSTAND → PATCH → TEST → VERIFY → RECORD → CONTINUE`

If a test fails:

`FAIL → TRACE → FIX → TEST AGAIN`

One failed repair must never terminate the overall audit.

---

## 9. PRESERVE VERIFIED WORK

Never unnecessarily:

- restart a completed module
- replace working code
- create duplicate services
- create duplicate intelligence systems
- overwrite verified architecture
- delete historical evidence
- replace a working integration merely because a newer approach exists
- regenerate verified assets

**Advance only the unresolved delta.**

---

## 10. CANONICALIZATION

When duplicates are discovered, do not automatically delete them.

First identify:

- canonical implementation
- duplicate implementation
- consumers
- dependencies
- historical significance
- migration requirements

Then:

`DISCOVER → CLASSIFY → CANONICALIZE → MIGRATE → VERIFY → RETIRE DUPLICATE`

Preserve history.

---

## 11. TEST AND EVIDENCE GATE

A checkbox is not a test.

For every important requirement identify the smallest test capable of proving the claim:

- unit test
- integration test
- acceptance test
- runtime test
- deployment test

Run broader regression tests when appropriate.

A claim may only become `VERIFIED` when evidence supports it.

---

## 12. AUDIT LEDGER

Every audit run should update a machine-readable ledger. Recommended fields:

```json
{
  "id": "APEX-REPO-0001",
  "repository": "Apex-Hub",
  "requirement": "...",
  "expected_state": "...",
  "actual_state": "...",
  "status": "VERIFIED",
  "evidence": [
    "commit:<sha>",
    "file:<path>",
    "test:<command/result>",
    "runtime:<result>"
  ],
  "action_taken": "...",
  "remaining_gap": null,
  "last_verified": "YYYY-MM-DDTHH:MM:SSZ"
}
```

Evidence must point to something that can actually be inspected.

---

## 13. AI HANDOFF PROTOCOL

Every AI session that changes an APEX repository must leave a handoff containing:

```text
WHAT I INSPECTED
WHAT I CHANGED
WHAT I TESTED
WHAT PASSED
WHAT FAILED
WHAT IS BLOCKED
WHAT EVIDENCE EXISTS
WHAT REMAINS
WHAT THE NEXT AI SHOULD DO
```

Do not report completion with vague language such as "looks done" or "should work."

Use measurable state:

`37 VERIFIED / 3 FAILED / 2 BLOCKED / 0 UNKNOWN`

---

## 14. HUMAN INPUT QUEUE

When human input is required, capture:

```text
H-001
Need: <exact input>
Reason: <why it is required>
Where used: <system/module>
Blocks: <specific verification/task>
Does NOT block: <parallel work that can continue>
```

This allows the human to supply only the missing piece while AI continues the rest of the audit.

---

## 15. CONTINUE_AUDIT COMMAND

When work is interrupted, resume from the ledger instead of restarting.

```text
CONTINUE_AUDIT

1. Read the current audit ledger.
2. Find the first unresolved item.
3. Inspect its evidence.
4. Repair it if safely executable.
5. Test it.
6. Record the result.
7. Move to the next unresolved item.
8. If blocked by human input, record BLOCKED and continue all other executable work.
9. Repeat until no executable unresolved work remains.
```

---

## 16. AUDIT COMPLETION GATE

At the end of an audit, report:

```text
APEX REPOSITORY AUDIT

Repositories discovered:       XX
Repositories audited:          XX
Repositories inaccessible:     X

Requirements discovered:       XXX

VERIFIED:                       XXX
IMPLEMENTED / UNVERIFIED:      XX
PARTIAL:                        XX
FAILED:                         XX
MISSING:                        XX
BLOCKED:                        XX
UNKNOWN:                        XX

Duplicate systems:             X
Broken references:             X
Missing tests:                 X
Missing documentation:         X
Missing configuration:         X

Repairs performed:             XX

Human input required:
1. ...
2. ...

Next executable task:
...

AUDIT COMPLETE: YES / NO
```

`AUDIT COMPLETE: YES` is forbidden unless every discovered item has been classified and every non-blocked executable item has been resolved and verified.

---

## 17. OPERATING PRINCIPLE

**Do not restart. Do not guess. Do not disappear into one failure.**

Discover the full system. Feed the audit. Find the gaps. Repair what can be repaired. Preserve what already works. Isolate what is blocked. Record evidence. Continue until the unresolved executable delta is exhausted.

**GODSPEED = VERIFIED PROGRESS, NOT PERFORMATIVE COMPLETION.**
