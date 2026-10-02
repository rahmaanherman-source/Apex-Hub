#!/usr/bin/env node
/**
 * APEX Commerce -> Shopify Admin API adapter.
 *
 * SECURITY CONTRACT:
 * - Run this module only in a trusted server/local process.
 * - Never expose SHOPIFY_ADMIN_API_TOKEN to browser/client code.
 * - Never commit .env files or real credentials.
 * - Keep Shopify permissions limited to the scopes actually required.
 */

const API_VERSION = process.env.SHOPIFY_API_VERSION || '2026-07';
const SHOP_DOMAIN = process.env.SHOPIFY_STORE_DOMAIN;
const TOKEN = process.env.SHOPIFY_ADMIN_API_TOKEN;

function requireConfig() {
  if (!SHOP_DOMAIN) throw new Error('Missing SHOPIFY_STORE_DOMAIN');
  if (!TOKEN) throw new Error('Missing SHOPIFY_ADMIN_API_TOKEN');
  if (!/^[a-z0-9][a-z0-9-.-]*\.myshopify\.com$/i.test(SHOP_DOMAIN)) {
    throw new Error('SHOPIFY_STORE_DOMAIN must be a *.myshopify.com hostname');
  }
}

export async function shopifyGraphQL(query, variables = {}) {
  requireConfig();

  const response = await fetch(
    `https://${SHOP_DOMAIN}/admin/api/${API_VERSION}/graphql.json`,
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-Shopify-Access-Token': TOKEN,
      },
      body: JSON.stringify({ query, variables }),
    },
  );

  const body = await response.json();

  if (!response.ok) {
    throw new Error(`Shopify HTTP ${response.status}: ${JSON.stringify(body)}`);
  }

  if (body.errors?.length) {
    throw new Error(`Shopify GraphQL error: ${JSON.stringify(body.errors)}`);
  }

  return body.data;
}

export async function listProducts(first = 20) {
  const query = `
    query Products($first: Int!) {
      products(first: $first) {
        nodes {
          id
          title
          handle
          status
          totalInventory
        }
      }
    }
  `;

  const data = await shopifyGraphQL(query, { first });
  return data.products.nodes;
}

export async function getShop() {
  const query = `
    query Shop {
      shop {
        id
        name
        myshopifyDomain
        primaryDomain { host }
      }
    }
  `;

  const data = await shopifyGraphQL(query);
  return data.shop;
}
