# APEX Hub Object Model
# Canonical Entity & Relationship Specification

## Overview

APEX Hub is the operating system for everything.

This document defines the **canonical object model** for APEX Hub.  
Every service, module, and feature MUST use these entities and relationships.

---

## Core Principles

- Every object has:
  - `id`
  - `type`
  - `owner`
  - `organization_id`
  - `workspace_id`
  - `created_at`
  - `updated_at`
  - `status`
  - `tags`
  - `permissions`
  - `history`
  - `audit_trail`
  - `ai_notes`

- Every object is:
  - searchable
  - connected
  - auditable
  - automatable
  - explainable

---

## Core Entities

### 1. Organization

Represents a company, brand, or primary account.

**Fields:**

- `id`
- `name`
- `slug`
- `status` (active, suspended, closed)
- `billing_plan`
- `billing_status`
- `primary_contact_user_id`
- `settings` (JSON)
- `created_at`
- `updated_at`

### 2. Workspace

Logical area within an organization (team, project, brand).

**Fields:**

- `id`
- `organization_id`
- `name`
- `slug`
- `status`
- `settings` (JSON)
- `created_at`
- `updated_at`

### 3. User

Human or service identity.

**Fields:**

- `id`
- `organization_id`
- `email`
- `name`
- `role` (owner, admin, manager, operator, analyst, support, guest)
- `status`
- `preferences` (JSON)
- `last_login_at`
- `created_at`
- `updated_at`

### 4. Role

Reusable permission profile.

**Fields:**

- `id`
- `organization_id`
- `name`
- `description`
- `scopes` (JSON: read/write/manage/admin/billing/security)
- `created_at`
- `updated_at`

### 5. Permission

Object-level access control.

**Fields:**

- `id`
- `object_type`
- `object_id`
- `principal_type` (user, role, team, group)
- `principal_id`
- `scopes` (read, write, manage, admin)
- `created_at`
- `updated_at`

### 6. Customer

End customer of the organization.

**Fields:**

- `id`
- `organization_id`
- `workspace_id`
- `external_id` (Shopify, Stripe, etc.)
- `email`
- `name`
- `phone`
- `address` (JSON)
- `status`
- `tags`
- `metadata` (JSON)
- `created_at`
- `updated_at`

### 7. Product

Sellable item or service.

**Fields:**

- `id`
- `organization_id`
- `workspace_id`
- `external_id` (Shopify, Stripe)
- `name`
- `description`
- `type` (physical, digital, subscription, service)
- `status`
- `tags`
- `metadata` (JSON)
- `created_at`
- `updated_at`

### 8. Variant

Specific variation of a product.

**Fields:**

- `id`
- `product_id`
- `sku`
- `name`
- `attributes` (JSON: size, color, etc.)
- `price`
- `currency`
- `status`
- `inventory_quantity`
- `inventory_status`
- `metadata` (JSON)
- `created_at`
- `updated_at`

### 9. Inventory

Stock tracking.

**Fields:**

- `id`
- `organization_id`
- `workspace_id`
- `variant_id`
- `warehouse_id`
- `quantity`
- `status`
- `thresholds` (JSON)
- `metadata` (JSON)
- `created_at`
- `updated_at`

### 10. Warehouse

Location of inventory.

**Fields:**

- `id`
- `organization_id`
- `name`
- `address` (JSON)
- `status`
- `metadata` (JSON)
- `created_at`
- `updated_at`

### 11. Order

Customer order.

**Fields:**

- `id`
- `organization_id`
- `workspace_id`
- `customer_id`
- `external_id` (Shopify, Stripe)
- `status` (draft, pending, paid, fulfilled, cancelled, refunded)
- `line_items` (JSON)
- `subtotal`
- `tax`
- `shipping`
- `discounts` (JSON)
- `total`
- `currency`
- `payment_status`
- `fulfillment_status`
- `metadata` (JSON)
- `created_at`
- `updated_at`

### 12. Invoice

Billing document.

**Fields:**

- `id`
- `organization_id`
- `workspace_id`
- `customer_id`
- `order_id`
- `external_id` (Stripe invoice)
- `status` (draft, open, paid, void, uncollectible)
- `amount_due`
- `amount_paid`
- `currency`
- `due_date`
- `metadata` (JSON)
- `created_at`
- `updated_at`

### 13. Payment

Payment transaction.

**Fields:**

- `id`
- `organization_id`
- `workspace_id`
- `customer_id`
- `order_id`
- `invoice_id`
- `external_id` (Stripe payment_intent, charge)
- `status` (pending, succeeded, failed, refunded)
- `amount`
- `currency`
- `method` (card, bank, wallet, etc.)
- `metadata` (JSON)
- `created_at`
- `updated_at`

### 14. Subscription

Recurring billing.

**Fields:**

- `id`
- `organization_id`
- `workspace_id`
- `customer_id`
- `external_id` (Stripe subscription)
- `status` (active, trialing, past_due, cancelled)
- `plan_id`
- `start_date`
- `end_date`
- `renewal_date`
- `metadata` (JSON)
- `created_at`
- `updated_at`

### 15. Project

Internal project or initiative.

**Fields:**

- `id`
- `organization_id`
- `workspace_id`
- `name`
- `description`
- `status`
- `tags`
- `metadata` (JSON)
- `created_at`
- `updated_at`

### 16. Document

Structured document (contracts, SOPs, specs).

**Fields:**

- `id`
- `organization_id`
- `workspace_id`
- `title`
- `type`
- `status`
- `content` (JSON or markdown)
- `tags`
- `metadata` (JSON)
- `created_at`
- `updated_at`

### 17. Media

Files (images, video, audio, assets).

**Fields:**

- `id`
- `organization_id`
- `workspace_id`
- `filename`
- `url`
- `type`
- `size`
- `status`
- `tags`
- `metadata` (JSON)
- `created_at`
- `updated_at`

### 18. Automation

Workflow definition.

**Fields:**

- `id`
- `organization_id`
- `workspace_id`
- `name`
- `description`
- `status` (active, paused, draft)
- `triggers` (JSON)
- `conditions` (JSON)
- `actions` (JSON)
- `approvals` (JSON)
- `notifications` (JSON)
- `metadata` (JSON)
- `created_at`
- `updated_at`

### 19. Report

Analytics or data view.

**Fields:**

- `id`
- `organization_id`
- `workspace_id`
- `name`
- `description`
- `type` (dashboard, chart, table, export)
- `config` (JSON)
- `status`
- `tags`
- `metadata` (JSON)
- `created_at`
- `updated_at`

### 20. Integration

External system connection.

**Fields:**

- `id`
- `organization_id`
- `workspace_id`
- `provider` (Stripe, Shopify, Slack, etc.)
- `status` (connected, disconnected, error)
- `settings` (JSON)
- `scopes` (JSON)
- `metadata` (JSON)
- `created_at`
- `updated_at`

### 21. Device

Trusted device.

**Fields:**

- `id`
- `user_id`
- `organization_id`
- `fingerprint`
- `type`
- `status`
- `last_seen_at`
- `metadata` (JSON)
- `created_at`
- `updated_at`

### 22. Session

Login session.

**Fields:**

- `id`
- `user_id`
- `organization_id`
- `device_id`
- `ip_address`
- `user_agent`
- `status`
- `risk_score`
- `created_at`
- `expires_at`
- `terminated_at`
- `metadata` (JSON)

### 23. Activity

Event log entry.

**Fields:**

- `id`
- `organization_id`
- `workspace_id`
- `actor_type` (user, system, integration)
- `actor_id`
- `object_type`
- `object_id`
- `action` (created, updated, deleted, etc.)
- `context` (JSON)
- `created_at`

### 24. AuditEntry

Immutable audit record.

**Fields:**

- `id`
- `organization_id`
- `workspace_id`
- `actor_type`
- `actor_id`
- `object_type`
- `object_id`
- `change` (JSON diff)
- `reason`
- `created_at`

---

## Relationships (High Level)

- Organization → Workspaces (1:N)
- Organization → Users (1:N)
- Organization → Customers, Products, Orders, Invoices, Payments, Subscriptions, Projects, Documents, Media, Automations, Reports, Integrations (1:N)
- Workspace → Customers, Products, Orders, etc. (1:N)
- User → Sessions, Devices, Activity, AuditEntry (1:N)
- Product → Variants (1:N)
- Variant → Inventory (1:N)
- Customer → Orders, Invoices, Payments, Subscriptions (1:N)

---

## Global Object Registry

All objects must be registered in a **Global Object Registry** with:

- `object_type`
- `schema`
- `storage_location`
- `search_index`
- `permissions_model`
- `ai_context_model`

This registry powers:

- Universal Search
- Activity feeds
- AI assistance
- Automation triggers
- Analytics
- Governance

