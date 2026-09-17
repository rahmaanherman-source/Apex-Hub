# APEX Cloud Circuit Breaker

APEX is local-first. `local.*` routes use Ollama and never open a cloud window. `cloud.*` routes are explicit and never reached through silent fallback because `fallback_to_cloud` remains false.

## Window lifecycle

1. The orchestrator resolves a task route.
2. A local route calls Ollama directly.
3. A cloud route loads the provider configuration.
4. `CloudWindow` reads the configured secret only when the window opens.
5. If `require_confirm` is true, the user must approve the cloud window.
6. The provider adapter performs the actual cloud request inside the context manager.
7. Exiting the context clears the broker-held key reference and closes the window.

The current repository contains the gate and lifecycle, but **does not pretend that Leonardo or MiniMax provider APIs are implemented**. A provider adapter must be added explicitly before those routes can transmit data.

The configured model names are treated as configuration values, not proof that a provider currently offers those exact model IDs. Verify model availability before enabling production traffic.

## Latch clarification

The current Latch Desktop project is a local agent control plane/governance layer: it can wrap agent terminals, enforce tool/network policies, manage worktrees, monitor activity, and optionally sandbox sessions. It is **not the same thing as a secret vault**, and APEX should not describe it as an AES-256 secret broker without separate evidence.

Current Latch documentation/source describes Windows support and a local authorization server. Its documented setup is from source with Node.js 20+ and npm. See the official repository before installing or pinning a version.

Official source: https://github.com/latchagent/latch-core
Official site: https://www.runlatch.sh/
