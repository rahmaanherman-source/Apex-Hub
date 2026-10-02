# APEX Commerce — Shopify Admin API

This integration gives APEX a server/local-process boundary for Shopify Admin API access.

## Environment

Create a local `.env` or export variables in the trusted runtime:

```text
SHOPIFY_STORE_DOMAIN=your-store.myshopify.com
SHOPIFY_ADMIN_API_TOKEN=your-token
SHOPIFY_API_VERSION=2026-07
```

**Never commit the real token.** The token must not be placed in React/Vite client code, browser storage, source control, logs, screenshots, or chat.

## Current adapter

`shopify-admin.mjs` provides:

- `shopifyGraphQL(query, variables)` — authenticated GraphQL request boundary
- `getShop()` — connection/identity test
- `listProducts(first)` — catalog read test

The adapter intentionally keeps credentials on the trusted side of the application boundary.

## First test

From the repository root, after setting the environment variables:

```bash
node --input-type=module -e "import { getShop } from './integrations/shopify/shopify-admin.mjs'; console.log(await getShop())"
```

Then:

```bash
node --input-type=module -e "import { listProducts } from './integrations/shopify/shopify-admin.mjs'; console.log(await listProducts(10))"
```

## Permission boundary

Start with the smallest Shopify Admin API scopes needed by the application. Read-only catalog access should be established before adding write permissions. Order/customer permissions should be added only when the corresponding APEX workflow exists.

## Architecture

```text
APEX Creator / Gabby / Local AI
              |
              v
       APEX Commerce Adapter
              |
       credential boundary
              |
              v
       Shopify Admin API
```

This is an adapter, not a credential vault. Production credentials should continue to live in the APEX secret-management boundary (for example, Omni Vault or the trusted local runtime).
