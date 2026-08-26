# GODSPEED RAG Production Contract

The Cloud Run + Cloud SQL + Vertex AI concept is retained, but the original one-shot script is not production-safe as written.

## Required corrections

1. **Secrets** — never hard-code `DB_PASS`, HMAC secrets, API keys, or other credentials in shell scripts. Store them in Google Secret Manager and inject them into Cloud Run.
2. **Database connection** — use a Cloud SQL connector/socket or private IP with least-privilege credentials. Do not expose PostgreSQL publicly just to make the app work.
3. **Authentication** — replace a shared `x-emperor-seal` value derived from a browser-visible secret with authenticated service/user credentials. A static client-side HMAC secret is not an access-control boundary.
4. **RAG grounding** — retrieval and generation must remain separate. The model should receive retrieved document IDs/content and the application should return citations/metadata rather than claiming the model itself is the source of truth.
5. **Prompt injection** — retrieved documents are untrusted data. They must not be allowed to override system/developer instructions.
6. **Input limits** — enforce request size, query length, rate limits, timeouts, and database statement limits.
7. **Audit** — record request ID, authenticated principal, retrieval count, document IDs, model version, and latency. Do not log raw secrets or unnecessary personal data.
8. **Deployment** — use a reproducible build and deploy pipeline rather than piping credentials and SQL passwords into an interactive `gcloud sql connect` session.

## Target flow

```text
Client
  │ authenticated request
  ▼
APEX Gateway
  │
  ├── authorization
  ├── request ID
  └── rate limit
       │
       ▼
RAG Service (Cloud Run)
  │
  ├── PostgreSQL retrieval
  ├── citation assembly
  └── Vertex AI generation
       │
       ▼
Grounded response + source IDs
```

## Golden World integration

The Golden World application may consume the RAG service for lore/knowledge retrieval, but the game client must never contain Google Cloud service-account credentials, database passwords, or privileged Vertex AI credentials.
