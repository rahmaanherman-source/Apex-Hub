# APEX Shopify Product Source Registry

## Purpose

This is the canonical working registry for product sources, supplier networks, marketplaces, print-on-demand providers, and connector apps that can feed or synchronize product data with Shopify.

The registry distinguishes **product acquisition** from **sales-channel synchronization**. A marketplace that can sync a seller's existing catalog into Shopify is not automatically a supplier that gives APEX rights to resell its products.

## Operating rule

**No product enters the live catalog merely because an importer can technically copy it.** Before publication, APEX must establish:

1. source identity;
2. product rights / resale authorization or an applicable supplier relationship;
3. cost and expected margin;
4. SKU/variant data;
5. image/content rights;
6. fulfillment method;
7. inventory/price synchronization capability;
8. shipping and returns terms;
9. bulk-import limits;
10. test import and post-import verification.

## Current source/connector map

| Source / connector | Role | Product feed into Shopify | Bulk capability | Fulfillment model | Current status |
|---|---|---|---|---|---|
| **Printify** | POD supplier | Yes | Large catalog / product publishing; exact bulk limits require account/app verification | Print-on-demand | Candidate / verify live account |
| **Gelato** | POD supplier | Yes | Large catalog; exact bulk limits require account/app verification | Print-on-demand | Candidate / verify live account |
| **DSers** | Dropshipping connector | Yes | One-click listing and bulk product push/edit are advertised | Dropshipping / supplier fulfillment | Candidate / verify live account |
| **Faire** | Wholesale marketplace | Products ordered can sync to Shopify | Product selection/bulk features exist; Faire explicitly says it does **not** support dropshipping | Wholesale inventory | Candidate / wholesale, not dropship |
| **Syncee** | Supplier/dropship/wholesale network | Yes | Bulk/supplier catalog workflows | Depends on supplier | Candidate / verify supplier terms |
| **Etsy** | Marketplace / seller catalog | Yes through third-party connectors | Bulk import/sync available through Shopify apps | Depends on the Etsy seller/product rights | Connector candidate; not automatically a supplier |
| **Walmart** | Marketplace | Import/sync is possible through third-party Shopify apps; Shopify Marketplace Connect primarily syncs a Shopify catalog outward | Bulk import/sync exists in third-party apps | Depends on seller/source | Connector candidate; rights must be established |
| **Amazon** | Marketplace | Shopify Marketplace Connect syncs Shopify catalog to Amazon; third-party tools may import seller catalogs | Bulk channel management available | Depends on seller/source | Channel candidate; not automatically a supplier |
| **eBay** | Marketplace | Shopify Marketplace Connect / third-party apps support sync | Bulk/channel sync available | Depends on seller/source | Connector candidate; not automatically a supplier |
| **TikTok Shop** | Sales channel / marketplace | Shopify product sync apps exist | Bulk/product sync exists in current Shopify app ecosystem | Depends on seller/supplier | Channel candidate; not a supplier by itself |
| **Temu** | Marketplace | Third-party multichannel connectors exist | Depends on connector | Depends on source/terms | Research / verify rights before use |
| **Ipsy** | Beauty retailer/subscription brand | No verified supplier-to-Shopify product feed established in this registry | Not established | Not established as a dropship/wholesale feed | **UNVERIFIED — do not treat as a supplier** |

## What the user means by "give us products"

There are several materially different cases:

### A. Supplier gives APEX a catalog

Examples: POD suppliers, wholesale networks, dropship suppliers.

```text
Supplier catalog
      ↓
APEX importer
      ↓
Normalize SKU / price / variants / media
      ↓
Rights + margin gate
      ↓
Shopify draft
      ↓
Verification
      ↓
Publish
```

### B. Marketplace connector copies a catalog

Examples: Etsy, Walmart, eBay, Amazon.

Technical ability to import a listing does **not** automatically grant APEX permission to resell that listing. The source account, seller relationship, licensing, fulfillment, and marketplace terms must be established separately.

### C. Sales-channel connector publishes APEX's own products elsewhere

Examples: Shopify Marketplace Connect, TikTok Shop connectors, Walmart channel tools.

This is the reverse direction:

```text
APEX Shopify catalog
        ↓
Marketplace connector
        ↓
Amazon / Walmart / eBay / other channel
```

That increases distribution but does not create new supplier inventory.

## Bulk ingestion architecture

APEX should support multiple input modes behind one canonical importer:

```text
CSV / XLSX
JSON / API
Supplier feed
XML feed
Marketplace connector
POD catalog
Manual product URL
        ↓
SOURCE ADAPTER
        ↓
CANONICAL PRODUCT SCHEMA
        ↓
DEDUPLICATION
        ↓
RIGHTS / SOURCE CHECK
        ↓
MARGIN / PRICING CHECK
        ↓
IMAGE + CONTENT VALIDATION
        ↓
SHOPIFY DRAFT BATCH
        ↓
IMPORT TEST
        ↓
PUBLISH BATCH
        ↓
POST-PUBLISH VERIFICATION
```

## Canonical product record

```json
{
  "source": "printify",
  "source_product_id": "...",
  "supplier": "...",
  "title": "...",
  "description": "...",
  "images": [],
  "variants": [],
  "sku": "...",
  "cost": 0.0,
  "price": 0.0,
  "currency": "USD",
  "inventory": null,
  "fulfillment": "pod|dropship|wholesale|owned",
  "shipping_profile": "...",
  "rights_status": "verified|review|unverified",
  "source_status": "verified|review|unverified",
  "shopify_status": "draft|active|blocked",
  "import_batch_id": "..."
}
```

## Bulk policy

**Bulk is allowed only after the adapter has passed a small-batch test.**

Recommended progression:

```text
1 product
   ↓
5 products
   ↓
25 products
   ↓
100 products
   ↓
500 products
   ↓
2000+ products where source/API limits permit
```

The 2,000-product target is a **business target**, not evidence that every supplier or Shopify connector permits a 2,000-item operation in one request.

The importer must discover and respect:

- API rate limits;
- batch-size limits;
- pagination;
- variant limits;
- image limits;
- payload limits;
- supplier licensing/terms;
- Shopify API limits;
- retry/idempotency rules;
- duplicate SKU handling.

## Financial safety

Product ingestion must never silently create customer charges or supplier charges.

Importing a catalog is a **data operation**. Ordering inventory is a **financial operation**. They require separate authorization paths.

APEX must preserve the customer-protection rule:

> Never double-charge customers or create avoidable duplicate billing. Identify the account/service/payment source and require explicit confirmation where APEX controls the duplicate-charge decision.

## Verification states

```text
DISCOVERED
    ↓
SOURCE_IDENTIFIED
    ↓
RIGHTS_REVIEW
    ↓
TEST_IMPORTED
    ↓
DATA_VALIDATED
    ↓
MARGIN_VALIDATED
    ↓
SHOPIFY_VERIFIED
    ↓
BULK_AUTHORIZED
    ↓
PUBLISHED
```

A source remains `UNVERIFIED` until the relevant external account/feed/API operation is actually tested.

## Research notes — current external evidence

- Shopify's Marketplace Connect connects Shopify catalogs to Amazon, Target Plus, Walmart, and eBay; Shopify's help documentation notes that new Etsy connections are not currently available through Marketplace Connect. citeturn2search2
- The Shopify App Store currently lists Etsy connectors capable of bulk product import/sync; one current example is Etsy Integration - DPL. citeturn0search9
- DSers currently advertises product importing and bulk product push/edit for AliExpress/1688/Alibaba/US/TikTok-related sourcing workflows. citeturn1search11turn1search14
- Faire's Shopify app syncs ordered products, orders, and inventory, but its listing explicitly says Faire does not support dropshipping. Its seller-side app also advertises product selection and bulk upload. citeturn0search0turn0search1
- Printify's Shopify app currently advertises more than 1,300 custom products and no-inventory POD fulfillment. citeturn1search13
- Gelato's Shopify app currently advertises hundreds of POD products, global fulfillment, and a free-to-install model with production/shipping charges when products are printed. citeturn1search0
- Shopify's current marketplace app ecosystem includes product-sync and bulk-sync connectors for TikTok Shop, Etsy, Walmart, eBay, Amazon, and other channels. citeturn2search4turn2search6

## Next implementation target

Build one **APEX Product Intake tab** that exposes every source through the same interface:

```text
PRODUCT SOURCES
├── POD
│   ├── Printify
│   └── Gelato
├── DROPSHIP / SUPPLIER NETWORKS
│   ├── DSers
│   └── Syncee
├── WHOLESALE
│   └── Faire
├── MARKETPLACE IMPORT / CONNECTORS
│   ├── Etsy
│   ├── Walmart
│   ├── Amazon
│   ├── eBay
│   ├── TikTok Shop
│   └── Temu
└── BEAUTY / SPECIALTY SOURCES
    └── Ipsy — UNVERIFIED until a legitimate supplier/catalog feed is established
```

Every tab should show **SOURCE → ACCESS REQUIREMENT → PRODUCT COUNT → BULK LIMIT → COST → RIGHTS STATUS → TEST STATUS → LAST SYNC → ERROR LOG**.
