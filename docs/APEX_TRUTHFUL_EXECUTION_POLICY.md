# APEX Truthful Execution & Audit Policy

**Status:** CANONICAL / NON-NEGOTIABLE
**Scope:** Entire APEX Hub repository, all modules, agents, UI, workers, queues, integrations, audits, exports, credential operations, and future modules.

## Builder / Copilot Instruction

Treat this document as a permanent APEX engineering law. Do not weaken, bypass, reinterpret, or remove it when adding future modules.

### 1. NO FAKE COMPLETION

APEX MUST NEVER report an operation as completed unless the underlying operation actually executed and produced verifiable evidence.

Never simulate completion with:
- frontend timers
- fabricated percentages
- fake queue states
- placeholder success responses
- mock verification presented as production verification
- hard-coded green/healthy states
- invented provider connectivity
- invented deployment status
- invented export artifacts

If the real operation is not implemented, report exactly:

`NOT_IMPLEMENTED`

If the operation cannot run because an external provider, permission, credential, worker, or dependency is unavailable, report:

`BLOCKED — PROVIDER/DEPENDENCY ACTION REQUIRED`

If execution starts and fails, report:

`FAILED — <actual reason>`

Only report:

`COMPLETED`

when execution succeeded and evidence exists.

### 2. AUDIT MEANS TRUTH

When a user requests an audit, APEX must inspect actual system evidence rather than infer health from configuration or diagrams.

A configuration that says a service is connected is NOT proof that the service is live.

A diagram that shows a connection is NOT proof that the connection works.

A credential existing in a vault is NOT proof that the credential is valid.

A UI component existing is NOT proof that its backend capability exists.

A job record existing is NOT proof that the job executed.

Every audit result must distinguish:
- VERIFIED — evidence obtained
- UNVERIFIED — not enough evidence
- NOT_IMPLEMENTED — capability absent
- BLOCKED — dependency/provider/permission prevents execution
- FAILED — execution attempted and failed
- COMPLETED — execution succeeded with evidence

### 3. REAL EXECUTION OVER UI THEATER

UI progress is allowed only when it reflects a real durable operation.

For exports, media processing, catalog generation, deployments, credential rotation, synchronization, imports, or other long-running operations, the production flow must be:

`User Command → CommandBus/API → Durable Job → Real Worker/Executor → Real Events/Progress → Real Artifact/State Change → Verification → Final Status`

A frontend animation MUST NOT claim that work occurred when no durable worker performed the work.

If the worker is not connected yet, expose the real blocked/unimplemented state instead of simulating progress.

### 4. DO NOT BLOCK MONEY-MAKING WORK WITHOUT A VALID REASON

APEX should execute legitimate user-authorized work as directly as possible.

Do NOT introduce arbitrary friction, artificial approval gates, decorative confirmation steps, or unnecessary manual operations that do not protect:
- security
- authorization
- data integrity
- provider requirements
- irreversible/destructive actions
- financial correctness
- legal/compliance requirements

If a real safety or integrity boundary exists, explain the exact reason and provide the fastest valid path forward.

The objective is **safe execution, not bureaucracy**.

### 5. CREDENTIALS AND KEY OPERATIONS

The Credential & Key Operations Center must follow the same truth rules.

Never display a credential as valid merely because metadata exists.

For every provider/key, track evidence-backed state such as:
- provider
- credential type
- key/reference ID (never the secret itself)
- created/rotated timestamp when available
- last verified timestamp
- last-used evidence when available
- dependencies
- environment
- status
- rotation eligibility
- revocation eligibility
- verification evidence

A credential older than the configured rotation threshold is a **rotation candidate**, not automatically safe to destroy.

For destructive revocation:
1. inventory the credential;
2. identify dependencies;
3. create/obtain the replacement where supported;
4. verify the replacement;
5. migrate dependencies;
6. verify the migrated service;
7. revoke the old credential only when evidence shows it is no longer required and the operation is authorized;
8. record the complete audit trail.

### 6. 60-DAY STALE-CREDENTIAL POLICY

The requested default policy is a 60-day stale/rotation review threshold.

Do NOT interpret `older than 60 days` as permission to blindly delete an active credential.

Instead:
- identify credentials older than 60 days;
- mark them `STALE / ROTATION REVIEW`;
- show dependencies and evidence;
- rotate where safe and supported;
- revoke only after the replacement and dependency migration are verified;
- preserve the audit record.

### 7. SHOPIFY / CSV EXPORT TRUTH

When APEX generates a Shopify CSV, the file must be a real generated artifact, not a UI-only representation.

Before declaring the export ready:
- generate the actual CSV;
- validate encoding and headers;
- validate required product/variant fields;
- validate handles, SKUs, options, variants, prices, inventory fields, images, and other applicable fields;
- detect malformed rows and broken relationships;
- report validation failures before download;
- provide the actual file artifact;
- record the export version and validation result.

If APEX cannot generate the real file, say so. Never provide a fake download state or claim Shopify compatibility without validation.

### 8. MEDIA EXPORT TRUTH

For CSV, JSON, MP4, images, reels, batch exports, and catalog assets:

A displayed progress percentage must correspond to actual durable work.

A completed export must have:
- an actual artifact;
- a real storage/reference location;
- integrity/validation evidence where applicable;
- a recorded job ID or execution ID;
- an auditable completion state.

### 9. FUTURE MODULES MUST INHERIT THIS POLICY

Every new module added to APEX Hub must explicitly comply with this policy.

Before marking a module complete, the builder must answer:

1. What real operation does this module perform?
2. What system actually performs it?
3. What evidence proves execution?
4. What happens if the dependency is missing?
5. What happens if execution fails?
6. What state does the user see in each case?
7. Are any UI states simulated rather than evidence-backed?
8. Are there tests proving that false success cannot be reported?

If these questions cannot be answered, the module is not production-complete.

### 10. DEFINITION OF DONE

A feature is NOT DONE merely because:
- the component renders;
- TypeScript compiles;
- the button exists;
- a timer reaches 100%;
- a mock API returns success;
- a diagram shows the desired architecture;
- a configuration file contains the expected values.

A feature is DONE when the real execution path exists, the important failure paths are handled, and evidence proves the claimed result.

### 11. REQUIRED AUDIT LANGUAGE

Use precise language in APEX UI, logs, reports, and agent responses.

Preferred:
- `VERIFIED`
- `UNVERIFIED`
- `NOT_IMPLEMENTED`
- `BLOCKED`
- `FAILED`
- `COMPLETED`
- `ROTATION REQUIRED`
- `ROTATION REVIEW`
- `DEPENDENCY MIGRATION REQUIRED`

Avoid ambiguous success language such as:
- `Looks good`
- `Connected` without verification
- `Ready` without evidence
- `Done` when only UI work completed
- `Exported` when only an export job was queued

### 12. ENFORCEMENT

Builders and AI coding agents working in this repository must read this policy before implementing or modifying execution-oriented features.

When a requested feature conflicts with this policy, preserve truthful execution and explain the concrete blocker rather than silently implementing a fake substitute.

**APEX LAW:**

> If it happened, prove it.
> If it did not happen, say it did not happen.
> If it cannot happen yet, say why.
> If it failed, show the failure.
> Never turn a placeholder into a lie.
