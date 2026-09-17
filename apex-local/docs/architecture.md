# APEX Local Architecture

VS Code/terminal and dashboard call the FastAPI backend. The orchestrator loads routing and security policy, selects an Ollama model, and exposes explicitly registered skills. SQLite provides persistent local memory. External business services are invoked only through skills and approval gates.

```mermaid
flowchart TB
 A[VS Code / Terminal] --> B[FastAPI :8000]
 C[Dashboard] --> B
 B --> D[Orchestrator]
 D --> E[Ollama]
 D --> F[SQLite Memory]
 D --> G[Skill Registry]
 G --> H[Shopify]
 G --> I[Stripe]
```
