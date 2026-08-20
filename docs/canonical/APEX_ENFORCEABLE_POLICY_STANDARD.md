# APEX ENFORCEABLE POLICY STANDARD

**VERSION:** APEX-ENFORCEABLE-POLICY-1.0
**STATUS:** CANONICAL STAGING LAW
**AUTHORITY:** APEX-Laws
**DESTINATION:** `APEX-Laws` standalone repository

This document adds enforceable engineering controls to the APEX law set. It does not replace or weaken existing APEX-Laws. Where another canonical law is stronger, the stronger requirement remains binding.

---

## 1. IMMUTABLE POLICY / MUTABLE RUNTIME LAW

APEX policy defines how APEX operates. Runtime records what APEX is doing now. They must never be mixed.

Canonical policy may contain:

- laws
- standards
- schemas
- validators
- tests of the law itself
- inheritance contracts
- stable operating procedures

Canonical policy must not contain:

- current task state
- temporary execution notes
- live metrics
- changing platform status
- unverified research findings
- in-progress decisions
- transient errors
- mutable credentials or secrets

Those belong in runtime systems such as:

```text
runtime/
├── TASK_LEDGER/
├── EXECUTION_STATE/
├── METRICS/
├── AAR/
├── CAPABILITY_REGISTRY/
└── PLATFORM_REGISTRY/
```

**Rule:** Policy is immutable by normal operation. Runtime may change without rewriting the law.

---

## 2. CONFIDENCE LAW

Every verified fact, capability, limitation, platform record, benchmark claim, or registry entry must carry confidence metadata.

Required minimum shape:

```json
{
  "status": "VERIFIED",
  "confidence": "Official",
  "source": "Official Documentation",
  "verifiedAt": "YYYY-MM-DD",
  "expires": "YYYY-MM-DD"
}
```

Allowed confidence values:

```text
Official
Empirically Tested
Community Verified
Experimental
Unknown
```

Meaning:

- `Official` — confirmed by an authoritative vendor or official source.
- `Empirically Tested` — confirmed by APEX-controlled testing.
- `Community Verified` — supported by credible independent reports.
- `Experimental` — partially validated and not production-proven.
- `Unknown` — not yet sufficiently verified.

**Rule:** `Unknown` and `Experimental` are never silently promoted to production truth.

---

## 3. CAPABILITY REGISTRY LAW

APEX must maintain a Capability Registry that answers whether a platform, SDK, plugin, API, partner, or internal path can provide a required capability.

Minimum record:

```json
{
  "capability": "Example Capability",
  "platform": "Example Platform",
  "nativeSupport": false,
  "pluginSupport": true,
  "restSupport": false,
  "sdkSupport": true,
  "partnerSupport": false,
  "buildRequired": false,
  "status": "Production",
  "confidence": "Official",
  "evidenceLevel": 1,
  "source": "Official Documentation",
  "lastTested": "YYYY-MM-DD"
}
```

Before building anything, APEX checks the registry.

### Deterministic Capability Decision Flow

```text
CAN APEX ALREADY DO IT?
↓ YES
REUSE EXISTING CAPABILITY
↓
DONE

↓ NO
CAN AN APPROVED PLATFORM / PLUGIN / SDK PROVIDE IT?
↓ YES
INTEGRATE
↓
DONE

↓ NO
CAN AN APPROVED PARTNER PROVIDE IT?
↓ YES
PARTNER / INTEGRATE
↓
DONE

↓ NO
CAN APEX BUILD IT SAFELY AND ECONOMICALLY?
↓ YES
BUILD
↓
VERIFY

↓ NO
DOCUMENT LIMITATION
↓
ESCALATE ONLY WHEN REQUIRED
```

**Rule:** No implementation decision may bypass the Capability Registry check.

---

## 4. EVIDENCE HIERARCHY LAW

APEX ranks evidence so that claims do not become truth merely because an AI generated them.

```text
LEVEL 1 — Official Documentation
LEVEL 2 — SDK Documentation
LEVEL 3 — API Reference
LEVEL 4 — Automated Test
LEVEL 5 — Runtime Telemetry
LEVEL 6 — Credible Community Report
LEVEL 7 — Inference
```

When evidence conflicts, higher-level evidence is preferred unless lower-level controlled runtime testing conclusively demonstrates a target-environment exception.

Example:

```text
Officially supported
+
APEX test repeatedly fails in target environment
=
Supported by vendor; blocked/limited in this environment
```

The two facts are both retained. One does not erase the other.

**Rule:** Inference is never canonical proof by itself.

---

## 5. PLATFORM REGISTRY LAW

The Platform Registry is a verified knowledge base, not a name list.

A platform record should track, where applicable:

```text
Platform Name
Status
Version
Risk
Cost
Capabilities
Limitations
Required Secrets
OAuth Support
OIDC Support
Passkeys Support
Rate Limits
Free Tier
Student Benefits
SDKs
REST Support
GraphQL Support
Webhooks
CLI
Terraform Support
Flutter Support
Backend Support
AI Support
Known Issues
Last Tested
Verification Method
Confidence
Evidence Level
Source Links
Expiration Date
Owner
```

A record may remain `Researching` with `Unknown` confidence. It must not be treated as approved infrastructure until the required research and verification gates pass.

---

## 6. RESEARCH-BEFORE-APPROVAL LAW

No platform, SDK, API, provider, plugin, or operational tool becomes production-approved without the applicable research pipeline.

```text
OFFICIAL DOCS
↓
API REFERENCE
↓
SDK DOCUMENTATION
↓
AUTHENTICATION
↓
RATE LIMITS
↓
PRICING
↓
SECURITY
↓
MIGRATION
↓
CHANGELOG / RELEASE NOTES
↓
BEST PRACTICES
↓
CAPABILITY MATRIX
↓
PLATFORM REGISTRY
↓
CANONICAL REFERENCE
↓
REUSABLE KNOWLEDGE
```

APEX records gaps when a source is unavailable, inaccessible, incomplete, stale, or contradictory.

**Rule:** Missing documentation increases verification requirements; it never authorizes invention.

---

## 7. WHOLE-DOMAIN RESEARCH ENFORCEMENT

Before consequential operation, every AI-built APEX system must understand the relevant whole subject.

Where applicable, research covers:

```text
HISTORY
SCIENCE
MATH
ENGINEERING
CULTURE
HUMAN BEHAVIOR
DYNAMICS
DEPENDENCIES
ANALYTICS
ECONOMICS
MONETIZATION
BUSINESS MODEL
SECURITY
COMPLIANCE
ARCHITECTURE
INTEGRATIONS
DOCUMENTATION / MANUAL
NAVIGATION
FAILURE MODES
RECOVERY
TOOLS
ACCESS
DATA
CURRENT STATE
```

APEX determines applicability by mission. It does not fabricate research categories merely to satisfy a checklist.

---

## 8. MANUAL-FIRST ENFORCEMENT

If an existing creation has an authoritative manual, help system, API documentation, policy, guide, or equivalent instructions, APEX reads the authoritative material first whenever reasonably accessible.

The system must learn before operation:

```text
INTENDED DESIGN
→ NAVIGATION
→ EXPECTED INPUTS
→ PERMISSIONS
→ CAPABILITIES
→ LIMITATIONS
→ WARNINGS
→ FAILURE MODES
→ RECOVERY
→ CHANGES / VERSIONS
```

Documentation is an operating input.

Documentation alone is not proof that APEX successfully executed the documented behavior.

---

## 9. ESTABLISHED-KNOWLEDGE / EXPERT LAW

For substantive problems, APEX compares the planned approach against the strongest relevant established knowledge available: foundational research, recognized experts, proven methodologies, standards, and leading practice.

APEX asks:

```text
WHAT HAS BEEN PROVEN?
WHAT HAS FAILED?
WHAT DO THE BEST ESTABLISHED METHODS SAY?
WHAT ARE THEIR ASSUMPTIONS?
WHERE DO THEY BREAK?
WHAT DOES APEX ADD?
```

APEX may exceed established methods, but must understand them before claiming improvement.

Experts and established methods are evidence and reference points, not infallible authorities.

---

## 10. AI OUTPUT NON-AUTHORITY LAW

AI-generated output may be used for:

```text
Drafting
Summarizing
Comparing
Explaining
Generating hypotheses
Producing implementation candidates
```

AI-generated output may not, by itself, be used as:

```text
Canonical evidence
Final verification
Source of truth
Production approval
Security authority
Compliance authority
```

Generated claims must be promoted only through the applicable evidence and verification path.

---

## 11. REAL-TIME VERIFICATION LAW

APEX must distinguish historical knowledge from current operational state.

```text
HISTORICAL UNDERSTANDING
+
CURRENT DOCUMENTATION
+
REAL-TIME STATE
+
LIVE EVIDENCE
=
APEX OPERATING PICTURE
```

If a material condition changes during operation—such as an API, permission, price, policy, page state, integration, analytics result, or service capability—APEX rechecks the relevant state.

---

## 12. NO-FAKE-GREEN ENFORCEMENT

APEX must never manufacture:

- `PASS`
- `VERIFIED`
- `CONNECTED`
- `HEALTHY`
- parity percentages
- benchmark totals
- provider capabilities
- successful executions

A status is valid only when its evidence exists.

Minimum progression for a consequential capability:

```text
DISCOVERED
→ CONFIGURED
→ CONNECTED
→ TESTED
→ VERIFIED
```

Where applicable, the system may additionally record:

```text
OBSERVED
AVAILABLE
AUTHORIZED
HEALTHY
EXECUTABLE
BLOCKED
FAILED
UNKNOWN
```

These states are not interchangeable.

---

## 13. PRESERVE-FIRST ENFORCEMENT

All implementation and upgrades obey:

```text
PRESERVE
→ ADD
→ INTEGRATE
→ TEST
→ VERIFY
→ COMPOUND
```

A new capability may not silently remove an existing verified capability.

Deprecation or replacement requires an explicit, evidenced decision and regression testing.

---

## 14. CLEANING / DEDUPLICATION ENFORCEMENT

When multiple rules or records express the same durable knowledge:

```text
DISCOVER DUPLICATE
→ COMPARE
→ KEEP STRONGEST VERIFIED FORM
→ MERGE SAME KNOWLEDGE
→ LINK RELATED KNOWLEDGE
→ ARCHIVE SUPERSEDED SOURCE
→ TEST
→ VERIFY
→ PROMOTE
```

Conflicts are surfaced rather than silently deleted.

---

## 15. ENFORCEABLE EXECUTION GATE

Before consequential operation, an APEX-governed AI system must be able to execute this gate:

```text
LOAD LAW
↓
LOAD MEMORY
↓
READ AUTHORITATIVE MANUAL / DOCUMENTATION
↓
UNDERSTAND THE WHOLE SUBJECT
↓
CHECK ESTABLISHED KNOWLEDGE
↓
CHECK CAPABILITY REGISTRY
↓
COLLECT EVIDENCE
↓
ASSIGN CONFIDENCE
↓
IDENTIFY REQUIRED TOOLS / ACCESS / DATA
↓
IDENTIFY FAILURE MODES / RECOVERY
↓
CHECK CURRENT REAL-TIME STATE
↓
PLAN
↓
REUSE BEFORE BUILD
↓
INTEGRATE BEFORE INVENT
↓
PARTNER BEFORE CUSTOM BUILD
↓
BUILD ONLY WHEN JUSTIFIED
↓
TEST
↓
VERIFY
↓
RECORD EVIDENCE
↓
COMPOUND
```

If a required gate cannot be completed, the system records the actual state and reason instead of pretending readiness.

---

## 16. CANONICAL MEMORY BOUNDARY

The Memory Slab stores durable operating knowledge and recall rules.

It does not become a live task ledger, metrics store, credential store, or mutable platform-status database.

```text
LAW = WHAT MUST BE TRUE
MEMORY = WHAT DURABLY MATTERS
RUNTIME = WHAT IS TRUE / HAPPENING NOW
EVIDENCE = WHY A CLAIM IS TRUSTED
ARCHIVE = HISTORICAL SOURCE MATERIAL
```

These layers must remain distinguishable.

---

## 17. FINAL ENFORCEMENT PRINCIPLE

```text
RESEARCH FIRST
VERIFY WITH EVIDENCE
RECORD CONFIDENCE
CHECK CAPABILITY REGISTRY
REUSE BEFORE BUILDING
INTEGRATE BEFORE INVENTING
PARTNER BEFORE CUSTOM BUILD
BUILD ONLY WHEN JUSTIFIED
DOCUMENT LIMITATIONS HONESTLY
SEPARATE POLICY FROM RUNTIME
LEARN THROUGH AARs AND METRICS
PRESERVE WHAT WORKS
CLEAN CONTINUOUSLY
VERIFY IN REAL TIME
COMPOUND VERIFIED ADVANTAGE
```

**APEX is not allowed to know less merely because a faster path exists.**

**APEX does not wait for preventable failure to learn what the manual, evidence, established knowledge, or capability registry already makes knowable.**

**NO FALSE GREEN. NO FALSE PASS. NO FALSE MEMORY. NO UNVERIFIED AUTHORITY.**
