# AI Security Research Notes

## Scope

This file captures security themes supplied for the APEX security program. It is a research/requirements note, not a verification of every example or statistic in the source material.

## Custom-Built Agent Security Themes

The supplied research emphasizes:

- Custom agents combine probabilistic model behavior with software privileges.
- Standard application security remains necessary but does not cover every agent-specific risk.
- Agent discovery should correlate traffic, API monitoring, repositories, workloads, endpoints, tokens, and governance registries.
- Agents should have unique identities and short-lived credentials.
- Multiagent systems can create excessive privileges and segregation-of-duties problems.
- Secure development requires version control, peer review, secrets scanning, supply-chain controls, input validation, TLS, rate limiting, and error handling.
- Threat models should explicitly consider agentic memory, malicious input, logical policy gaps, DLP gaps, and MCP exposure.
- Public MCP servers should be treated as untrusted until independently vetted.
- Runtime defense should combine deterministic policy enforcement with behavioral anomaly detection and drift detection.
- Agent-generated code should execute in a sandbox.

## Indirect Prompt Injection

External content can contain instructions that an agent may ingest as data and incorrectly treat as commands. Email, documents, web pages, tickets, and tool results are examples of untrusted content channels.

APEX response:

1. Separate data from instructions.
2. Validate tool intent before execution.
3. Enforce capability authorization outside the model.
4. Require explicit confirmation for sensitive actions.
5. Log the source and chain of instructions.
6. Apply runtime controls even when the prompt appears benign.

## Memory Leakage / Manipulation

Agent memory can create an authorization boundary separate from the primary database. A user's confidential information can persist in short-term or long-term memory and later be surfaced to another user if session and access controls are weak.

APEX response:

- Session isolation.
- User/tenant-scoped memory.
- Data classification before retention.
- Retention limits.
- Memory read/write authorization.
- Audit trails for sensitive memory operations.
- DLP controls.

## Logical Policy Gaps

Natural-language policy is not a sufficient enforcement mechanism. If an action must be prohibited, enforce it through code, permissions, sandboxing, policy hooks, or gateway controls.

## Information Leakage Through Ordinary Sensors

The supplied research material highlights a broader security lesson: ordinary media can contain unintended information, including environmental clues, reflections, acoustic signatures, and metadata. APEX security reviews should therefore consider side channels created by cameras, microphones, screenshots, documents, and other multimodal inputs.

Examples described in the supplied material include:

- Geolocation inference from ordinary photographs.
- Scene information reflected in eyes or other reflective surfaces.
- Keystroke inference from acoustic recordings.
- Voice impersonation used as part of social engineering or fraud.

These examples reinforce the need to classify multimodal inputs as potentially information-rich even when the user did not intentionally provide the information.

## AI Evaluation / Sandbagging Research

The supplied material also raises the possibility of models behaving differently under evaluation conditions. This is a research concern rather than an assertion that every model behaves this way in ordinary use.

APEX implication:

- Avoid trusting a single benchmark.
- Use independent evaluations.
- Test both normal and adversarial conditions.
- Compare model behavior across environments.
- Preserve evaluation logs and prompts.
- Use deterministic external controls for security-sensitive actions.

## Voice Fraud / Social Engineering

Voice cloning can strengthen an existing social-engineering narrative. The security boundary should not depend on recognizing a familiar voice as proof of identity.

APEX controls:

- Out-of-band verification for financial actions.
- Transaction limits.
- Dual approval for high-value actions.
- Strong identity and authorization checks.
- Audit logs.
- No voice-only authorization for sensitive transactions.

## Forward-Deployed AI Engineering Theme

The supplied business material describes AI transformation as process reengineering rather than simply “adding AI.” The workflow is:

1. Find work worth automating.
2. Map the existing process.
3. Identify systems of record.
4. Identify exceptions and handoffs.
5. Measure cycle time and accuracy.
6. Rebuild the workflow around appropriate agent capabilities.
7. Preserve human-led trust moments.
8. Monitor outcomes and iterate.

This maps directly to the APEX business/agent architecture: the system should transform a defined workflow, not merely attach an AI chatbot to it.
