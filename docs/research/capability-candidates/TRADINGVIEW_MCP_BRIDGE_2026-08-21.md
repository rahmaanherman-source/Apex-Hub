# TradingView MCP Bridge — Capability Candidate

**Date recorded:** 2026-08-21  
**Source:** `tradesdontlie/tradingview-mcp`  
**Source URL:** https://github.com/tradesdontlie/tradingview-mcp  
**APEX status:** DISCOVERED / INSPECTED — not promoted to VERIFIED APEX capability

## What was observed

TradingView MCP Bridge is an open-source MCP server that connects an MCP-capable AI client to a locally running TradingView Desktop instance through Chrome DevTools Protocol (CDP). The repository documents chart-state inspection, live quote/market-data reads from the local chart, Pine Script development, chart navigation, drawings, alerts, replay workflows, screenshots, multi-pane layouts, monitoring, and a CLI interface.

The project documents a local architecture:

`AI/MCP client → MCP server (stdio) → CDP localhost:9222 → TradingView Desktop`

The project currently documents 84 MCP tools across 15 categories in its wiki, while the README contains some older tool-count text in places; this count discrepancy is evidence to resolve against the repository's current source before relying on a specific tool inventory.

## APEX relevance

Potential capability classes:

- financial/charting workspace integration
- MCP desktop-application control
- real-time chart-state inspection
- Pine Script development and debugging
- screenshot-based visual verification
- local-only application bridge patterns
- tool/agent context reduction through compact structured outputs

This is especially relevant to APEX's provider-isolation and capability-registry architecture because the bridge demonstrates a pattern where APEX/Gabby could use a standardized adapter contract while the underlying desktop provider remains replaceable.

## Verification state

**Source-level verification:** YES — the public repository and documentation were inspected.  
**User-owned APEX asset verification:** NO — no evidence in this record establishes that the user's TradingView account, Desktop installation, or MCP server is installed/configured.  
**Operational verification in the user's environment:** PENDING.  
**Promotion to Verified Manual Index:** NOT AUTHORIZED.

## Important constraints / caveats

- The repository states that it is not affiliated with TradingView.
- A valid TradingView subscription and the TradingView Desktop application are required for the documented workflow.
- The bridge operates against the locally running desktop application using CDP and requires explicit remote-debugging configuration.
- The repository states that it does not bypass TradingView access controls or paywalls.
- The repository describes the integration as an interface layer rather than a trading bot and warns that use must comply with TradingView terms and applicable data/exchange licensing.
- The repository accesses undocumented internal TradingView application interfaces, which may change or break with TradingView updates.
- Do not treat this source as authorization to execute real trades or automated financial decision-making.

## APEX No-Fake-Green path

```text
DISCOVERED
  ↓
INSPECTED — public repo/docs checked
  ↓
EVIDENCE — source repository + documented architecture
  ↓
PENDING USER/ENVIRONMENT VERIFICATION
  ↓
VERIFIED only after local installation/configuration and a controlled health check
  ↓
MANUAL INDEX only after the verified capability is documented
```

## Recommended capability-registry treatment

Record as an **external capability candidate / adapter pattern**, not as an APEX-owned platform or verified installation.

Do not copy the upstream project into APEX merely to record it. Preserve the authoritative upstream repository as the source of truth and keep APEX's local record lightweight.

## Evidence

- GitHub repository README: https://github.com/tradesdontlie/tradingview-mcp/blob/main/README.md
- GitHub wiki: https://github.com/tradesdontlie/tradingview-mcp/wiki
- Getting Started: https://github.com/tradesdontlie/tradingview-mcp/wiki/Getting-Started
