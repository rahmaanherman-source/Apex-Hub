# APEX / GODSPEED — 2,000 PRODUCT REVENUE MISSION

**Status:** Active canonical execution plan  
**Operating loop:** REMEMBER → REBUILD → REBOOT → VERIFY

## Mission

Move the verified product catalog from the existing source material into a Shopify-ready, evidence-backed import pipeline and then into the real store without inventing product data or falsely claiming completion.

## Source of Truth

Primary source identified in the working record:

`godspeed_2000_products copy.pdf`

The source must be read and counted before any claim is made about the actual number of products.

## Execution Pipeline

```text
SOURCE PDF
   ↓
READ ENTIRE SOURCE
   ↓
COUNT ACTUAL RECORDS
   ↓
NORMALIZE PRODUCT DATA
   ↓
VALIDATE
   ↓
CLASSIFY
   ├── READY
   ├── REVIEW
   ├── DUPLICATE
   ├── MISSING DATA
   └── BLOCKED
   ↓
shopify_test_10.csv
   ↓
REAL SHOPIFY IMPORT
   ↓
READ-BACK
   ↓
VERIFY
   ↓
shopify_test_100.csv
   ↓
REAL SHOPIFY IMPORT
   ↓
READ-BACK
   ↓
VERIFY
   ↓
FULL CATALOG IMPORT
   ↓
READ-BACK
   ↓
VERIFY
   ↓
REVENUE
```

## Non-Negotiable Rules

- Do not invent products.
- Do not invent suppliers.
- Do not invent prices.
- Do not invent SKUs.
- Do not invent product URLs.
- Do not invent image URLs.
- Do not silently fill missing source data.
- Do not overwrite existing Shopify products during the first proof batch.
- Do not delete existing Shopify data.
- Do not claim an import happened unless the real Shopify connection confirms it.
- Do not claim a product is verified until a read-after-write check succeeds where applicable.
- Do not use placeholder/example counts as real counts.

## First Proof

The first proof batch is **10 products**.

Acceptance requires:

1. Ten source-derived products exist in the generated CSV.
2. Shopify accepts the import.
3. The imported products exist in the real store.
4. Product data is read back.
5. Expected vs. actual data is compared.
6. Evidence is recorded.
7. Only then is the batch VERIFIED.

## Second Proof

After the 10-product path is verified:

1. Generate `shopify_test_100.csv`.
2. Import the 100-product batch.
3. Read the products back.
4. Compare expected vs. actual.
5. Record failures individually.
6. Fix and retest failures.
7. Only then proceed to the remaining catalog.

## Full Catalog

Generate `shopify_full_catalog.csv` or sequentially split import files when required by the target platform's file-size constraints.

Never split variant/image relationships incorrectly.

## Exact Reporting

Every run must report:

- TOTAL SOURCE RECORDS
- VALID
- READY FOR IMPORT
- REVIEW
- DUPLICATES
- MISSING PRICE
- MISSING SKU
- MISSING IMAGE
- MISSING URL
- IMPORT BLOCKERS
- IMPORTED
- FAILED
- VERIFIED
- REMAINING

Percentages must always state their denominator.

Example:

`18 / 20 products verified = 90% verified`

Never present a percentage without explaining what it measures.

## Read-After-Write Verification

Where an authorized API path exists:

```text
CREATE / IMPORT
   ↓
READ BACK
   ↓
COMPARE
   ↓
EVIDENCE
   ↓
VERIFIED
```

Evidence should include safe identifiers and timestamps, never secrets.

## UI Requirement

The existing Product Vault and Command Hub should be reused rather than replaced.

The Product Vault must expose real counts and real states:

- SOURCE
- PROCESSING
- VALIDATING
- READY
- REVIEW
- FAILED
- IMPORTED
- VERIFIED
- REMAINING

No fake progress bars.
No fake completion.
No static example counts presented as live data.

## Phone / Google AI Studio Workflow

Google AI Studio may be used from the phone to process the source PDF and generate/validate the catalog files.

The mobile workflow is:

```text
PHONE
 ↓
GOOGLE AI STUDIO
 ↓
ATTACH SOURCE PDF
 ↓
RUN EXTRACTION + VALIDATION PROMPT
 ↓
DOWNLOAD GENERATED CSV FILES
 ↓
SHOPIFY ADMIN
 ↓
IMPORT 10
 ↓
READ-BACK / VERIFY
```

AI Studio is the **catalog preparation and validation surface** unless a real, authorized Shopify integration is explicitly configured and proven. Do not claim that AI Studio itself has placed products into Shopify merely because it generated a CSV.

## Current Next Action

**Run the source PDF through Google AI Studio and obtain the exact source/product counts plus `shopify_test_10.csv`.**

Do not proceed to 100 or the full catalog until the 10-product path is proven.

## Completion Standard

```text
REMEMBER
   ↓
REBUILD
   ↓
REBOOT
   ↓
VERIFY
```

The revenue mission is complete only when the real product data has been imported, read back, verified, and the real store reflects the expected state.

**NO FAKE GREEN.**
