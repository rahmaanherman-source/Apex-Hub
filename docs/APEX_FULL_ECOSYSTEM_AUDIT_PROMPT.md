# APEX Full Ecosystem Audit Prompt

## Purpose
Perform a source-grounded, evidence-first audit of the entire authorized APEX ecosystem before new building. Inventory what exists, what is connected, what is duplicated, what is missing, what is broken, and what can produce revenue now.

## Non-negotiable truth rules
- No opinion is evidence.
- No authority is evidence merely because the source is MAC, an architect, developer, AI, company, news outlet, or documentation.
- Do not convert sentiment, reputation, or reported claims into truth.
- Every material claim must have provenance and an evidence status.
- Never mark GREEN without the required evidence actually being observed or independently reproduced.
- Never invent a missing count, connection, deployment, credential, product, order, or test result.
- Separate CLAIMED, DOCUMENTED, OBSERVED, COMPUTED, INDEPENDENTLY VERIFIED, FAILED, and UNKNOWN.
- A verification percentage measures verification coverage/evidence strength under the defined rubric; it does NOT mean a literal percentage of truth.
- Contradictory evidence is valuable. Reopen the case, record the contradiction, determine which evidence survives, and improve the verification rule if the gate missed something.
- Do not protect previous conclusions. Protect the integrity of the verification process.
- Preserve working systems. Reuse verified connections. Do not rebuild completed work.

## Audit scope
Audit every authorized source available to the execution environment, including:
1. GitHub repositories, branches, recent commits, issues, PRs, docs, code, tests, deployment configs, and integration artifacts.
2. APEX Hub, APEX Heritage, APEX Gabby, APEX Omni Product Studio, and production repositories.
3. Shopify commerce/product/import/sync/webhook/publishing components.
4. Golden World/game projects, character systems, configuration files, prompts, assets, and prototypes.
5. Google AI Studio projects, prompts, builds, models, assets, deployments, and usage/credit information where accessible.
6. Google Cloud, Supabase, DigitalOcean, Vercel, Cloudflare, Azure/Microsoft, OpenAI, GitHub, Stripe, and other authorized connected systems where access is available.
7. Authorized Drive/files/archives and prior project source material.
8. Existing APEX memory/Heritage artifacts and source-verification records.
9. Existing URLs and external resources that are explicitly authorized for audit.

## Security rule
NEVER output, store, copy, expose, or commit API keys, passwords, OAuth client secrets, service-account private keys, tokens, recovery codes, or other credentials.

For credentials, report only:
- provider
- credential/reference identifier if non-secret
- location/class of secret store
- status: present/missing/expired/unknown
- rotation requirement
- dependent systems

If rotation is required, use the existing secure rotation mechanism. Do not print secrets. After rotation, verify dependent services without exposing the new secret.

## Inventory format
For every discovered system/resource create an inventory record:
- System/resource name
- Owner/repository/source
- URL or internal reference
- Purpose
- Current state
- Last meaningful change
- Dependencies
- Inputs
- Outputs
- Connections
- Credentials reference (never secret)
- Evidence links
- Tests/evidence available
- Duplicates/overlap
- Missing pieces
- Blockers
- Revenue relevance
- Recommended action: KEEP / MERGE / CONNECT / FIX / REUSE / ARCHIVE
- Verification status
- Verification coverage percentage with rubric

## APEX Truth Gate
For every material claim:
CLAIM -> SOURCE -> TEST -> INDEPENDENT CHECK -> CONTRADICTION SEARCH -> FALSIFICATION ATTEMPT -> SCORE -> SEAL.

Use these statuses:
- GREEN VERIFIED: all required verification criteria passed.
- YELLOW PARTIAL: some criteria passed; required evidence remains missing.
- BLUE COMPUTED: independently calculated/reproduced but not necessarily externally validated.
- PURPLE CLAIMED: assertion exists without sufficient evidence.
- RED FAILED: verification test failed.
- BLACK UNKNOWN: insufficient evidence to evaluate.

Run the Anti-Ego test:
1. Remove author identity.
2. Remove MAC's opinion.
3. Remove AI opinion.
4. Remove architect/developer authority.
5. Recalculate independently where applicable.
6. Check provenance.
7. Search for contradiction.
8. Attempt falsification.
9. State what evidence would prove the claim wrong.
10. Re-evaluate without knowing who proposed it.

If the result changes because of who said it, fail Anti-Ego verification.

## Math/science validation
For mathematical, scientific, engineering, or quantitative claims:
- Extract inputs and assumptions.
- Check units/dimensions.
- Recalculate independently.
- Identify formula/source.
- Check whether evidence is theoretical, simulated, experimentally reproduced, peer-reviewed, standardized, deployed, or merely claimed.
- Search authoritative/primary sources where appropriate.
- Search for contradictory evidence.
- Report exactly what is validated and what remains unknown.

Never label a claim 80% true simply because 80% of checks passed. Report 80% verification coverage and explain the remaining uncertainty.

## Commerce-first audit
The immediate commercial objective is the existing 2,000-product path.

Do NOT start by rebuilding Shopify or setting up new accounts.
Audit the existing pipeline:
SOURCE CATALOG -> PRODUCT STUDIO -> PRODUCT DATA + IMAGE -> SHOPIFY PAYLOAD -> CREATE/UPDATE -> PUBLISH -> STOREFRONT VISIBILITY.

Determine actual counts for:
- source products
- valid product records
- valid images
- Shopify-ready records
- created/updated products
- published products
- rejected products
- products missing images
- products blocked by data/variant/price/SKU issues

Run a controlled batch using the existing pipeline and report hard evidence. Do not claim 2,000 complete unless the evidence proves it.

## Revenue-first priority
After inventory, identify the shortest verified path to money using assets that already exist. Do not spend time rebuilding infrastructure that is already present. Prioritize:
1. Existing product catalog + product images + publishing pipeline.
2. Existing Shopify connection.
3. Existing payment/checkout infrastructure.
4. Existing free distribution channels.
5. Existing Golden World/game/movie/content assets that can be monetized without duplicating work.

## Deliverables
Produce:
1. MASTER SYSTEM INVENTORY
2. CONNECTION MAP
3. DUPLICATE/OVERLAP MAP
4. IMPLEMENTED vs DOCUMENTED vs MISSING matrix
5. BLOCKER LIST ordered by money impact
6. TRUTH/VERIFICATION REGISTER
7. SECURITY/CREDENTIAL ROTATION REGISTER (no secrets)
8. 2,000-PRODUCT PIPELINE COUNT
9. REVENUE-READY ASSET LIST
10. GOLDEN WORLD ASSET INVENTORY
11. GOOGLE AI STUDIO ASSET/PROJECT INVENTORY
12. CLOUD/INFRASTRUCTURE INVENTORY
13. MEMORY/ARCHIVE INVENTORY
14. TOP 10 NEXT ACTIONS
15. SINGLE HIGHEST-PRIORITY ACTION TODAY

## Output discipline
Be concise but complete. Use evidence links for every important assertion. Explicitly label unknowns. Do not generate noise. Do not recommend a new tool when an existing connected tool already performs the job.

## Final rule
If the audit discovers that a prior APEX conclusion was wrong, record:
- what was believed
- what evidence disproved it
- how the Truth Gate missed it
- what verification rule/test should be added
- what downstream memories or decisions must be reopened

Disproof is a successful knowledge event, not a failure.
