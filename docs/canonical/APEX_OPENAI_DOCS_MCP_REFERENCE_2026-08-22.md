# APEX — OpenAI Developer Docs MCP Reference

**Status:** Canonical staging / source-ingested
**Source:** User-supplied OpenAI Docs MCP documentation
**Verification:** Requires current official-source verification before promotion to independently verified platform truth

## Purpose

APEX should use the official OpenAI Developer Docs MCP as a documentation retrieval source when working on OpenAI API, plugins, ChatGPT, Codex, or related OpenAI platform questions.

The supplied documentation describes a read-only documentation MCP server at:

`https://developers.openai.com/mcp`

It provides documentation search and page content. It does **not** execute OpenAI API calls on behalf of the agent.

## Supported agent integrations in the supplied source

### Codex

CLI configuration:

```bash
codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp
codex mcp list
```

The supplied source also describes `~/.codex/config.toml` configuration and recommends an `AGENTS.md` instruction telling the agent to use the OpenAI Developer Docs MCP for OpenAI-related work.

### VS Code / Copilot Agent mode

The supplied source describes an HTTP MCP configuration in `.vscode/mcp.json`:

```json
{
  "servers": {
    "openaiDeveloperDocs": {
      "type": "http",
      "url": "https://developers.openai.com/mcp"
    }
  }
}
```

### Cursor

The supplied source describes:

```json
{
  "mcpServers": {
    "openaiDeveloperDocs": {
      "url": "https://developers.openai.com/mcp"
    }
  }
}
```

### Claude Code

The supplied source describes:

```bash
claude mcp add --transport http openaiDeveloperDocs https://developers.openai.com/mcp
claude mcp list
```

It also describes user scope:

```bash
claude mcp add --transport http --scope user openaiDeveloperDocs https://developers.openai.com/mcp
```

and `/mcp` for connection inspection.

## APEX policy

For OpenAI-specific implementation or capability questions:

```text
QUESTION
→ OPENAI DOCS MCP
→ OFFICIAL SOURCE
→ CAPABILITY / EVIDENCE RECORD
→ IMPLEMENTATION
→ TEST
→ VERIFY
```

The Docs MCP is **evidence retrieval**, not an execution provider.

Do not infer that an API is connected merely because the Docs MCP is connected.

Do not mark a capability `EXECUTED`, `TESTED`, or `VERIFIED` from documentation retrieval alone.

## OpenAI Docs Skill

The supplied source recommends pairing the Docs MCP with the OpenAI Docs Skill from the official OpenAI skills repository. APEX should record this as an integration candidate and verify the current official repository/version before installation.

## Capability Registry classification

```yaml
provider: OpenAI
capability_family: developer_documentation
capability: OpenAI Docs MCP
transport: streamable_http
endpoint: https://developers.openai.com/mcp
access: read_only
execution: false
search: true
page_content: true
status: source_ingested
verificationRequired: true
```

## No-Fake-Green

`DOCUMENTED` means the source describes the capability.

`CONFIGURED` means the local agent configuration contains it.

`CONNECTED` means the agent can establish the MCP connection.

`EXECUTED` applies to an actual downstream operation, not documentation retrieval.

`TESTED` requires a controlled test.

`VERIFIED` requires evidence supporting the specific claim.
