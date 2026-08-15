# APEX HUB — SHOPIFY 2,000-PRODUCT MISSION

## Objective
Get the existing product catalog into Shopify with the correct product records and associated product images, then verify that the products are actually visible/usable in the store.

## Definition of done
- Catalog source identified and preserved.
- Product records normalized for Shopify.
- Image assets mapped to the correct products.
- Image URLs are accessible to Shopify where required.
- Products are created/updated without accidental duplication.
- Product images are attached to the correct products.
- Shopify API/webhook errors are captured.
- A sample is verified end-to-end before scaling the full catalog.
- Final product count and image attachment count are reconciled.

## Priority
This is a revenue-first implementation. Infrastructure work that does not directly help the catalog pipeline is out of scope for this phase.

## Pipeline
Catalog -> normalize -> image mapping -> accessible image URLs -> Shopify product payload -> create/update -> attach images -> verify -> reconcile -> publish.

## Guardrail
Do not claim the catalog is complete until the resulting Shopify records and image attachments have been independently verified.
