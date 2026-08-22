# Every Code — Capability Candidate

**Date recorded:** 2026-08-21  
**Source:** `just-every/code`  
**Source URL:** https://github.com/just-every/code  
**APEX status:** DISCOVERED / INSPECTED — not promoted to VERIFIED APEX capability

## Source claim reviewed

Every Code is a community fork of the OpenAI Codex CLI intended to remain compatible with upstream while adding developer-oriented orchestration and automation capabilities. The current public repository describes it as a local terminal coding agent with browser integration, multi-agent commands, theming, reasoning controls, MCP support, safety modes, Auto Drive, Auto Review, and Code Bridge. citeturn0search0turn0search1

The supplied reference claim focuses on three capabilities:

- **Auto Review:** background review watchers run in a separate worktree when a turn changes code, allowing review to proceed without blocking the main coding thread.
- **Auto Drive / Auto Review separation:** the repository documents that background reviews are decoupled from Auto Drive so `Esc` returns control immediately while review finalization continues.
- **Code Bridge:** a local bridge that streams errors, console output, screenshots, and control from running applications into Every Code and ships with an MCP server.

These capabilities are documented in the project's current README. citeturn0search0turn0search1

## APEX relevance

Every Code is a strong candidate for the APEX engineering-agent layer because it addresses several APEX requirements at once:

- local terminal-based coding agent
- background verification without blocking active work
- isolated worktree review
- multi-agent orchestration
- browser/application observation
- MCP extension surface
- long-session automation and bounded state handling
- provider-flexible agent orchestration
- explicit quality-first workflow

The strongest APEX concept is the **parallel execution + verification pattern**:

```text
APEX / Gabby
    ↓
engineering task
    ↓
Every Code / Auto Drive
    ├── primary implementation work
    └── Auto Review in isolated worktree
             ↓
        findings / ready-to-apply fixes
             ↓
        evidence / validation
```

That pattern is compatible with the APEX No-Fake-Green rule because review can operate as an independent verification path rather than being treated as proof merely because an agent generated code.

## Code Bridge relevance

Code Bridge is particularly relevant to the APEX Terminal / creation-studio direction because the project describes a local bridge that can stream application errors, console output, screenshots, and control into the coding agent through MCP. citeturn0search0turn0search1

Potential APEX capability class:

**running-application observability adapter**

Possible contract:

```text
Running App
   ↓
Code Bridge
   ↓
MCP
   ↓
Gabby / engineering agent
   ↓
observe → diagnose → propose/fix → test → verify
```

This should remain an adapter. APEX should own the capability contract and evidence model rather than making Every Code or Code Bridge canonical infrastructure.

## Provider isolation

Every Code supports multiple model/provider configurations and can orchestrate other AI CLI tools. Its repository also documents MCP support and a local configuration surface. citeturn0search0

APEX should therefore treat Every Code as a **replaceable engineering-agent provider**, not as a required dependency of the APEX control plane.

## Important caveats

- Every Code is a community fork of `openai/codex`; it is not OpenAI's official Codex distribution and the repository explicitly states that it is not affiliated with, sponsored by, or endorsed by OpenAI. citeturn0search0
- The repository is licensed Apache-2.0 according to its README. citeturn0search0turn0search2
- Public documentation proves the project's documented capabilities, not installation or configuration in the user's APEX environment.
- The project's own performance/reliability claims should be treated as project claims until independently tested against an APEX workload.
- Model names, versions, and implementation details are changing; the APEX registry should record the verified version/date rather than assuming the current README remains permanent.
- Auto Review is an engineering verification aid, not a substitute for APEX evidence requirements, tests, security review, or release gates.

## Verification state

**Public-source verification:** YES — current public repository/package information inspected.  
**User-environment verification:** NO.  
**APEX installation verification:** NO.  
**Controlled APEX test:** NOT YET PERFORMED.  
**Promotion to Verified Manual Index:** NOT AUTHORIZED.

## APEX No-Fake-Green path

```text
DISCOVERED
  ↓
INSPECTED — repository and current documentation checked
  ↓
EVIDENCE — documented Auto Review / Auto Drive / Code Bridge / MCP capabilities
  ↓
CHECK EXISTING APEX CAPABILITY REGISTRY
  ↓
VERIFY actual installation and configuration
  ↓
CONTROLLED TEST
  ├── isolated worktree review
  ├── Esc responsiveness during review
  ├── long-session stability
  ├── review linkage/evidence
  ├── Code Bridge application errors/console/screenshots
  └── MCP tool isolation and permissions
  ↓
PROMOTE only if the capability contract passes
```

## Recommended APEX registry treatment

Record Every Code as an **external engineering-agent / verification candidate** with these potential capability classes:

1. terminal coding agent
2. multi-agent orchestration
3. background code review
4. isolated-worktree verification
5. long-session automation
6. browser/application observation
7. MCP engineering tools
8. running-app observability through Code Bridge

Do **not** duplicate these capabilities inside APEX until reuse/integration has been evaluated against the existing Capability Registry.

## Suggested controlled test

Use a disposable APEX test repository containing known intentional defects and a small runnable application.

Measure:

- whether Auto Review actually runs in a separate worktree
- whether the primary session remains responsive while review runs
- whether `Esc` immediately returns control
- whether review findings remain linked to the correct branch/worktree
- whether fixes can be inspected before application
- whether Code Bridge reliably reports application errors, console events, and screenshots
- whether MCP permissions remain within the intended workspace boundary
- latency, token usage, failures, and false-positive/false-negative review findings

Only after those results are captured should the capability be promoted from candidate to verified integration.

## Sources

- GitHub repository: https://github.com/just-every/code
- npm package: https://www.npmjs.com/package/@just-every/code
