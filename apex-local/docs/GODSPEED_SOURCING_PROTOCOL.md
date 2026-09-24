# GODSPEED Sourcing Protocol — 10,000-Product Catalog

**Owner:** MAKEIT ALL COUNT LLC / APEX LIFE GLOBAL  
**Purpose:** Evidence-first sourcing and staging for a scalable catalog.

## Required commercial filters

1. Ships from the target market/region.
2. Shipping time must be **7 days or less** for the target destination.
3. Candidate must support at least **40% target margin** from supplier cost to retail price.
4. Prefer verified/high-quality suppliers and platform-supported fulfillment.
5. Supplier data is **staging input only**. Raw supplier titles/descriptions do not publish directly to Shopify.
6. Products pass APEX Omni Product Studio normalization before publication.
7. Inventory must be synchronized. APEX may enforce a configurable low-stock threshold (default target: 10 units) and pause/unpublish policy.

## Catalog structure

### Part 1 — Global Top 5,000
Select the highest-selling / strongest historical-demand candidates available from the connected source, subject to every required commercial filter. **Do not call an item a top seller unless the source provides evidence supporting that classification.**

### Part 2 — Wide Catalog 5,000
Expand across all available product categories. Allocate candidates across categories according to the available source inventory; do not fabricate an "even" allocation when the source cannot support it. Within each category, prefer products with documented sales/demand evidence and the same commercial filters.

## Required staging fields

- source_product_id
- category
- supplier_name
- product_title_raw
- product_title_normalized
- wholesale_cost
- recommended_retail_price
- margin_percent
- ships_from
- ship_to
- shipping_time_days
- fulfillment_status
- inventory_quantity
- supplier_rating (when provided)
- demand_evidence (when provided)
- source_url
- collected_at
- validation_status
- rejection_reason (when rejected)

## No-Fake-Green rules

- Never fabricate products, prices, inventory, shipping times, supplier ratings, fulfillment status, sales rank, or URLs.
- If the connected source cannot prove a constraint, mark it **UNVERIFIED** or **REJECTED** rather than assuming it passes.
- "Fulfilled by Syncee" is not inferred merely because a product appears in Syncee. Use the source's actual fulfillment/order-processing evidence.
- A 10,000-row target is a **target**, not proof that 10,000 qualifying products exist.
- Do not publish any product until staging validation and Omni Product Studio normalization pass.

## Execution sequence

1. Apply source-side filters available to the connected provider.
2. Collect candidates in batches.
3. Deduplicate by source product ID/SKU and normalized product identity.
4. Validate shipping, margin, supplier/fulfillment evidence, and inventory data.
5. Split qualifying candidates into Global Top and Wide Catalog datasets.
6. Send the qualifying dataset to APEX Product Graph / staging.
7. Normalize through Omni Product Studio.
8. Run final validation.
9. Only then make products eligible for Shopify publication.

## Current provider capability note

The connected Syncee sourcing interface exposes category, keyword, price, minimum margin, origin, destination, relevance/price sorting, and a top-selling weighting option. Syncee's help documentation also describes shipping-time filtering, supplier-location/shipping filters, product shipping details, import lists, and inventory synchronization. However, the current ChatGPT-connected search interface does **not** expose a numeric maximum-shipping-time filter or a direct "Fulfilled by Syncee" filter. Those constraints therefore require verification from returned product details/provider data before a candidate is accepted.

## Exact sourcing prompt

> I require a master catalog extraction of exactly 10,000 products **only if 10,000 qualifying products actually exist in the connected source**. Do not fabricate or extrapolate missing records.
>
> Target destination: [TARGET COUNTRY/REGION].
> 
> Required constraints for every accepted item:
> - Ships from: [TARGET COUNTRY/REGION].
> - Maximum shipping time: 7 days or less to the target destination.
> - Minimum target gross margin: 40% from supplier cost to recommended retail price.
> - Supplier: highly rated where rating evidence is available.
> - Fulfillment: verified platform-supported fulfillment status where evidence is available; do not infer this field.
> - Inventory: synchronized/current where the source supports inventory data.
>
> PART 1 — GLOBAL TOP 5,000
> Return the strongest documented sellers/demand candidates across all categories, subject to every required constraint. Do not claim "highest-converting" or "top-selling" without source evidence.
>
> PART 2 — WIDE CATALOG 5,000
> Expand across every available category. Allocate candidates across categories only where sufficient qualifying products exist. Do not fabricate an even allocation. Within each category, use the strongest documented demand/sales candidates available.
>
> For each accepted product provide:
> source product ID/SKU, category, supplier name, raw title, wholesale cost, recommended retail price, margin %, ships-from location, destination, shipping time, fulfillment status, inventory quantity, supplier rating, demand/sales evidence, source URL, and collection timestamp.
>
> Any field that cannot be verified must be marked UNVERIFIED. Any product that fails a required constraint must be rejected and excluded from the accepted 10,000. Return the actual accepted count and rejected/unverified counts. Never fill missing records with fabricated data.
