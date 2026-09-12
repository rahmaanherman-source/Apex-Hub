# APEX RUNTIME AUDIT — EVIDENCE, EXPOSURE SEVERITY & AUTOSCOPE CONTRACT

**Status:** CANONICAL / OWNER-AUTHORIZED
**Effective:** 2026-09-12

## 1. Purpose

This contract governs runtime, preview, production, credential, public-exposure, and non-destructive verification.

**Core law: CLAIM ≠ EVIDENCE.**

An audit finding is not verified because an agent, log line, screenshot, configuration declaration, or previous run says it is true. A verification requires observable evidence from the system being evaluated.

The audit must distinguish:
- observed fact
- supplied claim
- inference
- unverified condition
- verified condition

Never silently upgrade a claim into evidence.

---

# 2. Evidence Standard

Every verification MUST record:

1. **Verification ID**
2. **Claim being tested**
3. **Scope** — exact application, environment, endpoint, process, credential class, or configuration under test
4. **Method** — command, API request, browser test, DNS lookup, process inspection, repository inspection, etc.
5. **Timestamp**
6. **Expected result**
7. **Observed result**
8. **Evidence artifact** — sanitized output, response status/body summary, process identifier, DNS result, certificate details, commit/file reference, screenshot reference, or other reproducible artifact
9. **Evidence location** — where the artifact can be inspected
10. **Verdict** — VERIFIED / FAILED / UNVERIFIED / NOT APPLICABLE / BLOCKED
11. **Severity**, when a finding exists
12. **Remediation owner/action**, when required

Secrets MUST NOT be copied into evidence. Evidence must be sanitized while preserving enough information to reproduce or validate the finding.

### Evidence quality

**E0 — Claim only**
- Agent/user assertion.
- No independently observable evidence.
- Verdict cannot be VERIFIED.

**E1 — Indirect evidence**
- Configuration, source code, deployment metadata, or logs indicate the condition.
- Useful for diagnosis, but does not prove live behavior.

**E2 — Direct runtime evidence**
- Actual endpoint/process/API/system behavior observed.
- Sufficient for ordinary runtime verification when the test is reproducible.

**E3 — Corroborated evidence**
- Direct runtime evidence plus an independent second signal, such as DNS + HTTPS, process + endpoint, or API result + application state.
- Preferred for release-gate claims.

**E4 — Release evidence**
- E3 evidence plus environment identity, scope, timestamp, and artifact trail suitable for release/audit review.
- Required for production certification.

---

# 3. Verification Requirements — Endpoint Inventory

For EVERY reported endpoint verify all applicable fields.

| Field | Required evidence |
|---|---|
| URL | Exact observed URL from configuration/runtime |
| Environment | Explicit environment variable/deployment metadata AND runtime identity where possible |
| Port | Listening-process evidence or deployment/runtime configuration |
| Process | Actual process name/PID/owner or managed-runtime equivalent |
| Application | Endpoint response/application identity tied to source/deployment |
| Repository | Commit/build/deployment metadata connecting runtime to source |
| Routing | Actual request path/route response |
| Authentication | Positive authorized test AND negative/unauthorized test where safe |
| Authorization | Test that permitted role can act and unauthorized role cannot, where applicable |
| TLS/HTTPS | Certificate/hostname/protocol inspection and successful HTTPS request |
| Backend | Actual request reaching the intended backend, with safe non-mutating probe |
| Database | Safe read/health query or application-level database operation |
| External integrations | Real connection/handshake/API response, not configuration presence alone |
| Public exposure | External request from outside the origin/network boundary |
| Intended purpose | Canonical documentation/configuration mapping |
| Temporary/persistent | Tunnel/deployment lifecycle evidence |

**Endpoint verdict:** VERIFIED only when the applicable required fields have direct evidence. Otherwise UNVERIFIED or BLOCKED.

---

# 4. Local Runtime Verification

Claim: **“Server is running.”**

Required evidence:
- process/listener exists
- expected port is bound
- application responds locally
- response identifies the expected application/environment where feasible

Preferred E3:
- process/PID + successful local HTTP request

Do not accept a stale terminal message as proof.

---

# 5. Preview / Public HTTPS Verification

Claim: **“Preview is live.”**

Required evidence:
- externally reachable URL
- HTTPS succeeds
- certificate matches hostname
- expected application responds
- expected environment is identified
- authentication boundary is tested
- sensitive routes are checked for unintended exposure

For temporary tunnels:
- tunnel process/configuration
- origin target
- public access behavior
- shutdown/restart behavior
- access-control state

A trycloudflare.com URL is **PREVIEW/DEVELOPMENT by default**, never production merely because it is reachable.

---

# 6. Production Domain Verification

Claim: **“Production is deployed/live.”**

Required evidence:
- DNS resolution
- HTTPS response
- valid certificate/hostname
- expected production application identity
- correct deployment/environment
- authentication behavior
- authorization behavior where applicable
- backend connectivity
- database connectivity
- error/health behavior
- source/deployment identity

Production certification requires **E4** evidence.

A declared production URL without live corroboration is **UNVERIFIED**.

---

# 7. Credential Exposure Verification

Claim: **“Credentials are safe.”**

Required evidence:
- repository secret scan
- configuration/environment inspection
- generated/build artifact inspection where applicable
- logs/terminal-output inspection where applicable
- public endpoint/source-map/static-asset inspection where applicable
- classification of every discovered credential as REAL / TEST / DEMO / UNKNOWN

If a real credential appears in source, logs, public output, screenshots, browser-visible data, or other exposed material:

**CREDENTIAL ROTATION REQUIRED**

Never reproduce the secret in the report.

Evidence should contain:
- secret type
- location
- exposure path
- first/last known occurrence if available
- redacted fingerprint/identifier if useful
- rotation status

---

# 8. Public Exposure Verification

Check whether a public actor can reach:

- admin functionality
- internal APIs
- debug endpoints
- development tools
- database interfaces
- source maps
- test accounts
- internal services
- credentials/secrets
- privileged actions

Required evidence:
- exact exposed surface
- external request/test result
- authentication state used
- authorization result
- data/action returned
- reproduction path, sanitized

Do not test destructive actions merely to prove exposure. Use the least-invasive proof possible.

---

# 9. Non-Destructive Control Verification

Claim: **“Audit/agent protection prevents unsafe destructive changes.”**

Required evidence:
- applicable repository/agent policy
- actual attempted or simulated policy decision where safe
- confirmation that destructive machine-level commands are not automatically executed
- evidence that an explanation/approval boundary exists before destructive operations
- evidence of rollback/recovery path where applicable

Commands requiring special scrutiny include:
- Remove-Item
- rm
- del
- rmdir
- git reset
- git clean
- destructive database operations
- configuration deletion/reset

The audit must not perform a destructive test merely to generate evidence.

---

# 10. Machine-Level Workaround Verification

For any recommendation to modify/delete files outside the repository, verify:

1. exact path
2. process/tool owner
3. purpose
4. dependency relationship
5. claimed blocker
6. expected change
7. possible data/config loss
8. non-destructive alternative
9. reversibility
10. explicit authorization status

**Default verdict: BLOCKED pending review** when the operation is destructive and authorization/evidence is absent.

---

# 11. Runtime Claim Verification Matrix

| Claim | Minimum evidence | Release-grade evidence |
|---|---|---|
| Server running | E2 process + local response | E3 |
| Preview live | E2 external HTTPS response | E3 |
| Production deployed | E3 endpoint + deployment identity | E4 |
| Authentication works | E2 positive/negative auth tests | E3 |
| Authorization works | E2 role-boundary tests | E3 |
| Database connected | E2 safe DB operation | E3 |
| API connected | E2 real API response | E3 |
| Domain correct | E2 DNS + HTTPS | E3 |
| Credential safe | E2 secret-surface scan | E3/E4 |
| Public exposure controlled | E2 external exposure test | E3 |
| Non-destructive protection | E1 policy + safe behavior test | E3 |
| Production-ready | ALL applicable release gates | E4 |

---

# 12. Exposure Severity Levels

Severity measures **impact + exploitability + reachability + privilege + sensitivity**, not how inconvenient the finding is.

## SEV-0 — CRITICAL / IMMEDIATE CONTAINMENT

Use when there is active or highly probable compromise of a critical boundary.

Examples:
- production secret/credential publicly exposed and usable
- unauthenticated privileged administrative control
- public database/admin interface with meaningful access
- remote access to highly sensitive systems without required controls
- active compromise or confirmed unauthorized access

Required response:
- stop release
- contain exposure immediately where safe
- rotate/revoke credentials when applicable
- preserve evidence
- escalate for incident handling

## SEV-1 — HIGH / RELEASE BLOCKER

Serious exposure with meaningful unauthorized capability or sensitive-data access.

Examples:
- public internal API with privileged operations
- production admin route missing required authentication
- exposed real credential with uncertain usability
- authorization bypass
- sensitive customer/business data exposed without required boundary

Required response:
- release blocked
- remediation required before production certification
- verify remediation with E3/E4 evidence

## SEV-2 — MEDIUM / REMEDIATION REQUIRED

Material weakness with constrained impact or stronger compensating controls.

Examples:
- authenticated but overly broad internal endpoint
- preview environment exposes non-public development tooling
- sensitive debug information accessible under limited conditions
- temporary tunnel exposes an internal service that should be private but has an additional access layer

Required response:
- track remediation
- do not ignore
- production release depends on risk acceptance and applicable gates

## SEV-3 — LOW / HARDENING

Limited exposure or defense-in-depth weakness.

Examples:
- unnecessary metadata disclosure
- non-sensitive diagnostic endpoint
- overly verbose but non-sensitive error information
- preview configuration that increases exposure without direct sensitive access

Required response:
- remediate during normal hardening cycle
- document disposition

## SEV-4 — INFORMATIONAL

No meaningful security exposure; documentation, hygiene, or observability improvement.

Examples:
- missing runtime label
- incomplete inventory metadata
- stale non-sensitive documentation

Required response:
- document and improve as appropriate

### Severity override

Any finding involving:
- real credentials
- privileged actions
- personal/customer data
- production secrets
- database access
- unauthorized administrative access

must be reviewed at **SEV-1 or higher** unless evidence conclusively establishes lower impact.

---

# 13. AutoScope Boundary

## Definition

**AUTOSCOPE is the maximum boundary the audit/agent may inspect automatically without obtaining a new authorization decision.**

### INSIDE AUTOSCOPE

The audit may automatically inspect, read, test, and correlate:

- the explicitly named APEX repository
- repository source/configuration
- repository documentation
- git history/metadata needed for verification
- build/deployment metadata available through authorized integrations
- local processes and listeners relevant to the named application
- local application endpoints relevant to the named application
- explicitly reported preview URLs belonging to the named application
- DNS/TLS information for explicitly reported APEX domains
- public HTTP behavior of explicitly reported APEX endpoints
- non-destructive health/read-only API/database checks required for verification
- logs and runtime output already exposed through authorized tooling
- credentials **for exposure detection/classification only**; never disclose their values

### OUTSIDE AUTOSCOPE

Do NOT automatically:

- modify or delete files outside the repository
- delete credentials/configuration
- rotate/revoke credentials
- alter DNS
- change domains
- modify Cloudflare/tunnel configuration
- change firewall/network policy
- alter production infrastructure
- change cloud IAM/permissions
- install software
- uninstall software
- alter operating-system settings
- modify databases
- delete or mutate production/customer data
- send external messages/emails
- publish production changes
- purchase services
- create paid resources
- execute destructive commands
- access unrelated repositories/accounts/projects
- inspect unrelated private data
- expand testing to third-party systems merely because they are connected

### Scope expansion rule

If verification reveals a dependency outside AUTOSCOPE:

1. identify the dependency
2. explain why it matters
3. record it as OUT-OF-SCOPE / BLOCKED
4. request or await explicit authorization before modifying or deeply inspecting it

**Do not silently expand scope because doing so would make the audit easier.**

### Read-only does not mean harmless

Even a read-only operation may be OUTSIDE AUTOSCOPE if it accesses unrelated private systems, personal data, unrelated accounts, or third-party infrastructure.

---

# 14. Evidence Preservation & Sanitization

Evidence must be:
- timestamped
- reproducible where practical
- tied to the exact scope
- sanitized for secrets
- retained long enough to support the audit decision

Never place raw:
- API keys
- passwords
- session tokens
- private keys
- recovery codes
- field PINs

into reports, commits, issue comments, screenshots, or audit feeds.

Use redaction such as:
sk-…REDACTED
PIN-REDACTED
token:[REDACTED]

Do not store a reversible encoding as a substitute for redaction.

---

# 15. Audit Finding Schema

Every finding should contain:

- **ID**
- **Severity**
- **Title**
- **Claim**
- **Scope**
- **Environment**
- **Observed condition**
- **Expected condition**
- **Evidence level**
- **Evidence reference**
- **Exposure path**
- **Affected asset**
- **Credential/data sensitivity**
- **Exploitability**
- **Reachability**
- **Privilege**
- **Remediation**
- **Verification required after remediation**
- **Status**

---

# 16. Release Gate

Production-ready certification is prohibited unless all applicable gates are supported by release-grade evidence.

| Gate | PASS condition |
|---|---|
| LOCAL | Runtime verified |
| PREVIEW | External HTTPS/runtime verified |
| PRODUCTION | Production endpoint + deployment identity verified |
| AUTHENTICATION | Required boundaries verified |
| AUTHORIZATION | Required privilege boundaries verified |
| BACKEND | Real backend connectivity verified |
| DATABASE | Safe database operation verified |
| CREDENTIAL SAFETY | No unresolved SEV-0/SEV-1 credential exposure |
| PUBLIC EXPOSURE | No unresolved blocking exposure |
| NON-DESTRUCTIVE CONTROL | Unsafe automatic changes prevented |
| EVIDENCE | Required evidence attached to every applicable verification |
| AUTOSCOPE | No silent scope expansion |
| AUDIT TRAIL | Findings and dispositions recorded |

**Certification statement:**

> PRODUCTION READY may be issued only when the applicable release gates are PASS and the evidence trail supports those decisions. If evidence is missing, the correct state is UNKNOWN/UNVERIFIED—not PASS.

---

# 17. Governing Principle

**If the system cannot show evidence, the audit cannot call it verified.**

**If the audit needs to leave AUTOSCOPE, it stops at the boundary instead of silently crossing it.**

**If exposure exists, severity is determined by actual impact and reachability—not by whether the endpoint was intended to be temporary.**
