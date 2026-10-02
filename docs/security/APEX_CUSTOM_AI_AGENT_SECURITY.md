# APEX Custom AI Agent Security Standard

## Purpose

This document turns the custom-built AI-agent security principles supplied to the APEX program into an operational security baseline.

## Threat Model

Custom agents introduce risk at the boundaries between:

- LLM/foundation model
- Orchestrator
- Agent memory
- User identity
- Tools and APIs
- MCP servers
- Files and data stores
- External content
- Generated/executed code
- Other collaborating agents

Primary threats include:

- Indirect prompt injection.
- Memory leakage and manipulation.
- Logical policy gaps.
- Excessive privileges.
- Cross-service confused-deputy behavior.
- Unsafe MCP servers and tool selection.
- Credential exposure.
- Supply-chain compromise.
- Behavioral/intent drift.
- Unauthorized code execution.
- Data exfiltration through multimodal or unstructured channels.

## Security Principles

1. **Default deny.** Capabilities are not available unless explicitly granted.
2. **Unique agent identity.** Agents do not reuse human credentials when a workload identity is possible.
3. **Ephemeral credentials.** Secrets are short-lived, rotated, and protected at rest and in transit.
4. **Least privilege.** Agent access is constrained by the minimum resource/action set required.
5. **Explicit delegation.** When acting on behalf of a person, use an auditable delegation flow.
6. **Runtime enforcement.** Do not rely exclusively on prompts or model instructions for security policy.
7. **Independent gates.** Classification, routing, capability authorization, and execution are separate controls.
8. **Audit everything important.** Security decisions must be attributable to request, agent, tool, resource, and policy version.
9. **Sandbox generated code.** Agent-generated code must not execute directly in a privileged environment.
10. **Treat public MCP servers as untrusted until vetted.**

## Agent Discovery

Inventory custom agents using correlated signals:

- API traffic.
- Model API calls.
- Repository/code analysis.
- Runtime workload instrumentation.
- Endpoint discovery.
- Tokens and credential discovery.
- Existing AI governance registries.

Each registered agent should have an owner, purpose, environment, capabilities, identity, data classification, tools, MCP dependencies, and deployment status.

## Access Control

Prefer:

- Workload identities.
- Rotatable service credentials.
- Encrypted secret stores.
- PAM for privileged or multiagent workflows.
- ABAC/PBAC where dynamic authorization is required.
- Explicit user delegation for on-behalf-of workflows.

Never hard-code production credentials into agent source code.

## Multiagent Controls

Multiagent workflows can create privilege escalation and segregation-of-duties failures. Treat privileged collaborating agents as privileged identities. Each inter-agent handoff should be authorized, logged, and scoped.

## Secure Development Lifecycle

Required controls include:

- Version control.
- Peer review.
- Owner accountability.
- Secrets scanning.
- Dependency and supply-chain security.
- Agent framework vulnerability tracking.
- Input/message validation.
- TLS for remote model connections.
- Rate limiting.
- Error handling.
- Threat modeling.
- Security testing.

## Runtime Defense

Runtime controls supplement traditional application security controls. Required areas include:

- Prompt-injection detection.
- Jailbreak detection.
- Tool authorization.
- MCP allowlisting/gateway enforcement.
- Intent-drift detection.
- Behavioral anomaly detection.
- Data-loss controls.
- Sandbox enforcement.
- Security event logging.

Behavioral detection must be tuned for false positives and operational scale.

## Success Metrics

Track:

- Mean time to remediate agent exposures.
- Security-policy violations over time.
- Unauthenticated access attempts identified or blocked.
- Unauthorized tool invocations blocked.
- Credential rotation failures.
- MCP policy violations.
- Sandbox escapes or attempted escapes.

## Reference Architecture

```text
USER / EVENT
    |
    v
PRE-GENERATION CLASSIFIER
    |
    v
ROUTING POLICY
    |
    v
CAPABILITY CONTRACT
    |
    v
IDENTITY + AUTHORIZATION
    |
    v
TOOL / MCP GATEWAY
    |
    v
RUNTIME DEFENSE + AUDIT
    |
    v
EXECUTION SANDBOX / APPROVED SERVICE
```
