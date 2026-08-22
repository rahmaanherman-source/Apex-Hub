# APEX PLATFORM REGISTRY INDEX

**Purpose:** Lightweight reference map for external platforms that contain APEX/Godspeed projects, applications, designs, infrastructure, data, or integrations.

**Governance:** APEX No-Fake-Green verification gate.

**Promotion rule:** Only independently verified platform/app relationships may be promoted into the Verified Manual Index. Unverified items remain explicitly pending and are never presented as complete.

## STATUS LEGEND

- **VERIFIED** — existence/access and claimed APEX relationship checked with platform evidence.
- **PARTIAL** — platform/app evidence exists, but the full relationship or operational capability still needs verification.
- **UNVERIFIED** — no sufficient current evidence collected yet.
- **BLOCKED** — verification could not be completed with current access/tooling.

## VERIFIED MANUAL INDEX

| Platform | Verified APEX asset | What it is / role | Evidence | Status |
|---|---|---|---|---|
| GitHub | `rahmaanherman-source/Apex-Hub` | Canonical APEX hub/source repository; contains canonical law, memory, operations, and application material. | GitHub installed-repository result; repository is accessible with admin/maintain/push permissions. | **VERIFIED** |
| Replit | `Apex Sovereign Optimizer` | APEX/Godspeed-related application workspace. | Replit connected app search returned the editable app and its Repl ID. | **VERIFIED** |
| Base44 | `Apex Godspeed` | APEX/Godspeed application. Source inspection confirms APEX/Godspeed UI, Gabby, memory-state handling, and No-Fake-Green behavior in the application code. | Base44 app listing + live sandbox directory + source grep. | **VERIFIED** |
| Base44 | `APEX BRIDGE` | APEX bridge application present in the user's Base44 account. | Base44 authenticated app inventory. | **VERIFIED (EXISTENCE)** |
| Base44 | `GODSPEED Bulk-Connect` | Godspeed connectivity application present in the user's Base44 account. | Base44 authenticated app inventory. | **VERIFIED (EXISTENCE)** |
| Base44 | `APEX Access Control Pro` | APEX access-control application present in the user's Base44 account. | Base44 authenticated app inventory. | **VERIFIED (EXISTENCE)** |
| Jotform | `GODSPEED Intake – Bookmarks & Knowledge Ingestion` | Godspeed/APEX intake form for bookmark and knowledge ingestion. | Jotform authenticated asset search returned the form and form ID. | **VERIFIED** |
| Notion | `so we always remembere hjow to` | Durable APEX memory/reference page containing the APEX Architect status material. | Notion authenticated search returned the page and APEX content. | **VERIFIED** |

## PLATFORM INVENTORY — VERIFICATION STILL REQUIRED

These platforms were explicitly placed in the APEX ecosystem, but the current connected tooling did **not** produce enough evidence to promote a specific APEX application into the Verified Manual Index during this audit. They remain here so they are not forgotten, but they are **not green**.

| Platform | Current audit observation | Status |
|---|---|---|
| Vercel | The connected account/team is visible (`rahmaanherman-source's projects`), but the project-list call failed, so no specific APEX project was independently verified in this pass. | **BLOCKED** |
| Canva | Connected Canva search for `APEX` returned no matching design in the accessible search scope. | **UNVERIFIED** |
| OpenAI Developers | OpenAI developer access is connected, but the available developer connector is for API-key/developer configuration rather than an inventory of user applications; no specific APEX app was verified here. | **UNVERIFIED** |
| Supabase | Supabase is connected, but the currently loaded connector capability is documentation search rather than project inventory; no specific APEX project was verified here. | **UNVERIFIED** |
| Hugging Face | The connected Hugging Face namespace did not successfully expose the expected project-search operation in this audit. No specific APEX asset was promoted. | **BLOCKED** |
| Linear | Authenticated Linear search for `APEX` returned no active matching issue/project/document in this pass. | **UNVERIFIED** |
| Figma | Figma access is connected, but a specific file key was not available to perform file-level verification. No APEX file was promoted. | **UNVERIFIED** |
| Airtable | Authenticated Airtable inventory currently exposes an `Untitled base`; no APEX-specific base was identified from the available inventory. | **UNVERIFIED** |
| Lovable | Lovable access is present, but the project inventory requires the workspace identifier; no specific APEX project was promoted in this pass. | **UNVERIFIED** |

## GITHUB CANONICAL POINTERS

The current APEX-Hub law index is:

`docs/canonical/APEX_LAWS_INDEX.md`

The canonical durable memory slab is:

`docs/canonical/APEX_CANONICAL_MEMORY_SLAB.md`

The enforceable policy standard is:

`docs/canonical/APEX_ENFORCEABLE_POLICY_STANDARD.md`

The reality registry is:

`docs/operations/APEX_REALITY_REGISTRY.md`

The Platform Registry is this file.

## OPERATING RULE

The Platform Registry is deliberately small. It does **not** reproduce the contents of every application.

Use this path:

```text
PLATFORM REGISTRY
→ FIND REAL ASSET
→ OPEN AUTHORITATIVE SOURCE
→ READ MANUAL / DOCUMENTATION
→ CHECK CAPABILITY
→ COLLECT EVIDENCE
→ VERIFY
→ PROMOTE TO MANUAL INDEX
```

A green manual entry without evidence is a No-Fake-Green violation.

## CURRENT AUDIT RECORD

Audit performed against the connected platform access available in this ChatGPT session on 2026-08-21.

**Verified promotion commit:** `fc41205ee0e8f7d8d0b9e7102960b2f4824f2237`

This index records what was actually observed. It does not convert missing access into a false negative about whether the user may have an asset elsewhere; it simply prevents that asset from being represented as verified until evidence is obtained.
