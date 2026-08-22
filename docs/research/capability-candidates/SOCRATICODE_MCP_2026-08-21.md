# SocratiCode MCP — Capability Candidate

**Date recorded:** 2026-08-21  
**Source:** `giancarloerra/SocratiCode`  
**Source URL:** https://github.com/giancarloerra/SocratiCode  
**APEX status:** DISCOVERED / INSPECTED — not promoted to VERIFIED APEX capability

## Source evidence

SocratiCode is an open-source MCP server / plugin for local codebase intelligence. Current public package metadata identifies version **1.10.0**; the uploaded reference image shows an older **v1.2.0** UI, so the image version is treated as historical visual evidence rather than the current version. citeturn0search2turn0search1

The current project documents:

- local codebase indexing
- hybrid semantic + BM25 search
- polyglot dependency graphs
- symbol-level impact analysis and call-flow
- context artifacts
- cross-project and branch-aware search
- database/API/infrastructure knowledge
- MCP integration with Claude Code and other MCP hosts
- local Ollama embeddings with Docker-managed Qdrant by default
- optional OpenAI/LiteLLM/cloud embedding configurations

The project can be installed through `npx`, and its documentation also describes Claude Code plugin installation and MCP configuration. citeturn0search0turn0search1

## APEX relevance

This is a strong candidate for the APEX engineering/cognition layer because it addresses a recurring APEX problem: giving an AI agent structured, searchable understanding of a large codebase without repeatedly dumping entire repositories into context.

Potential APEX capability classes:

- codebase intelligence adapter
- semantic code search
- dependency/impact graph
- cross-project context retrieval
- branch/worktree-aware project context
- local-first indexing and embeddings
- MCP-compatible engineering tool surface
- context-efficiency layer for Gabby/Codex/other agents

The uploaded screenshot specifically depicts the server reporting Docker, Qdrant, Ollama, file watcher, cross-process coordination, a local project index, and quick commands such as `codebase_status`, `codebase_search`, `codebase_graph_query`, `codebase_context`, and `codebase_health`. Those are treated as claims/visual evidence from the supplied image, not as proof that the user's environment currently has SocratiCode installed.

## APEX architecture fit

```text
APEX / Gabby
    ↓
standardized code-intelligence capability contract
    ↓
SocratiCode adapter
    ↓
MCP
    ↓
local index + dependency graph + context artifacts
    ↓
Qdrant / Ollama (local-first default)
```

This aligns with APEX provider isolation: SocratiCode should be treated as a replaceable capability provider, not as canonical law or memory itself.

## Verification state

**Public-source verification:** YES — current public repository/package documentation inspected.  
**Screenshot evidence:** YES — supplied image shows an operational-looking v1.2.0 installation, but ownership/environment identity is not established by the image alone.  
**User-environment verification:** NO.  
**APEX installation verification:** NO.  
**Promotion to Verified Manual Index:** NOT AUTHORIZED.

## Important caveats

- Current public package version is newer than the version shown in the supplied screenshot; do not assume the screenshot's v1.2.0 tool surface matches the current release.
- Local-first behavior is the default architecture, but cloud embeddings can be explicitly configured; therefore "local" must be verified from actual configuration rather than assumed from the product name.
- The project is licensed AGPL-3.0-only according to its current public project documentation. Review license implications before embedding or modifying it inside a proprietary APEX distribution. citeturn0search8
- The project's own benchmark claims (for example, reduced tokens/calls and faster retrieval) are vendor/project claims and are not treated as APEX performance evidence until independently tested.

## APEX No-Fake-Green path

```text
DISCOVERED
  ↓
INSPECTED — repository/package/docs checked
  ↓
EVIDENCE — current public source + supplied screenshot
  ↓
PENDING USER/ENVIRONMENT VERIFICATION
  ↓
CONTROLLED TEST — index a non-sensitive APEX test project
  ↓
VERIFY — search accuracy, graph accuracy, watcher behavior, isolation, latency
  ↓
PROMOTE only if evidence passes
```

## Recommended registry treatment

Record SocratiCode as an **external code-intelligence capability candidate**. Do not duplicate its functionality inside APEX until capability reuse/integration has been evaluated against the existing APEX capability registry and actual environment.

The strongest next verification target is not a generic demo. It is a controlled test against an APEX repository/worktree where the expected dependency, symbol, file, and context relationships are already known.

## Sources

- GitHub repository: https://github.com/giancarloerra/SocratiCode
- npm package: https://www.npmjs.com/package/socraticode
- VS Code Marketplace: https://marketplace.visualstudio.com/items?itemName=GiancarloErra.socraticode
