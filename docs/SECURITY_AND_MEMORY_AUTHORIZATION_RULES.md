# APEX Security + Memory Authorization Rules

## 1. Credential handling
Credentials are secrets, not durable knowledge.

Never store or display API keys, passwords, OAuth secrets, service-account private keys, tokens, recovery codes, or similar secrets in conversation memory, source files, logs, prompts, dashboards, or generated audit reports.

Use the canonical secure credential store / Vault and authorized connection references. Agents should request a credential reference, perform the authorized action, return the result, and discard secret material from working context when no longer required.

## 2. Key rotation
When a credential may have been exposed, duplicated across systems, or is due for rotation:
1. Identify provider and credential reference without exposing the secret.
2. Identify dependent services.
3. Use the existing secure rotation mechanism.
4. Update dependent services through authorized secret references.
5. Re-test integrations.
6. Record rotation evidence without recording the new secret.
7. Mark the old credential retired/revoked only after external evidence confirms the replacement works.

Never paste a batch of keys into an AI prompt for the purpose of rotating them.

## 3. Conversation-to-memory authorization
Sensitive or personal information mentioned in a conversation must not automatically become durable Gabby/APEX memory.

Default state: NOT SAVED.

Durable memory requires explicit user authorization through a visible memory-control action. The UI should support:
- Save this
- Do not save
- Save category only
- Save temporarily
- Review before saving
- Delete/revoke saved memory

When a user asks to save information, store the minimum durable representation needed for continuity and preserve provenance/source reference where appropriate.

## 4. Memory status
Every durable memory item should have:
- memory ID
- source/provenance
- creation/update time
- confidence/verification status
- retention class
- authorization state
- related entities/connections
- superseded/revoked state

Temporary conversation content remains in the archive/history layer and does not automatically become durable operational memory.

## 5. Truth rule
Authorization to remember something does not make the information true. Memory authorization and truth verification are separate controls.

A saved claim can remain CLAIMED, PARTIAL, COMPUTED, VERIFIED, FAILED, or UNKNOWN.

## 6. Privacy rule
The system must make it obvious when information is being:
- used in the current conversation
- proposed for durable memory
- saved to durable memory
- shared with an external service
- removed from durable memory

No silent promotion from conversation to durable memory.
