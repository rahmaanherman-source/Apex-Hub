# APEX COMMAND CENTER — ONE-SPOT REAL-TIME OPERATIONS & ANALYTICS

## Purpose

APEX needs one internal command center so the owner does not have to inspect Shopify, Stripe, GitHub, deployments, AI providers, queues, analytics, logs, and system health individually.

The Command Center is the **single operational view**. It does not replace the underlying services; it aggregates their verified state.

## Primary Rule

**ONE SPOT → ALL SIGNALS → ONE TRUTH STATE → ONE NEXT ACTION.**

Do not require the owner to remember which service contains which metric.

## TOP-LEVEL AREAS

1. **MISSION / MONEY**
   - revenue today / period
   - orders
   - gross sales
   - refunds
   - fees
   - net revenue when available
   - conversion rate
   - average order value
   - products live
   - products pending
   - products failed
   - current revenue blocker

2. **COMMERCE**
   - catalog count
   - Shopify publication queue
   - publication success/failure/retry rates
   - storefront availability
   - cart events
   - checkout starts/completions
   - order events
   - fulfillment state where connected

3. **PAYMENTS**
   - Stripe connection state
   - successful payments
   - failed payments
   - refunds/disputes when available
   - webhook delivery state
   - webhook processing latency
   - idempotency/error state

4. **AI / AGENTS**
   - local model availability
   - active provider/model
   - task routing
   - queue depth
   - successful tasks
   - failed tasks
   - estimated cost when provider exposes it
   - quota/balance state only when actually verifiable
   - tutorial/video generation jobs
   - generation output status

5. **SYSTEM HEALTH**
   - API health
   - frontend health
   - database health
   - queue/worker health
   - deployment health
   - GitHub CI status
   - latency
   - error rate
   - uptime/availability where measured

6. **SECURITY / VAULT**
   - Vault availability
   - credential reference status
   - authorization status
   - expiring/invalid connections
   - security events
   - NEVER display secret values

7. **ANALYTICS**
   - traffic
   - sessions/users where connected
   - product views
   - add-to-cart
   - checkout
   - purchases
   - acquisition/source
   - campaign performance
   - landing-page performance
   - product performance
   - geographic/device breakdowns when available

8. **OPERATIONS / QUEUES**
   - active jobs
   - waiting jobs
   - completed jobs
   - failed jobs
   - retryable jobs
   - dead-letter jobs
   - oldest job age
   - worker throughput
   - current bottleneck

9. **TRUTH / AUDIT**
   - EXISTS
   - CONNECTED
   - AUTHORIZED
   - FUNCTIONAL
   - EXECUTED
   - ACCEPTED
   - LIVE
   - VERIFIED
   - PERFORMING
   - PROFITABLE

10. **OWNER ACTIONS**
   - show only actions requiring human intervention
   - provide exact service
   - exact account/resource
   - exact error
   - exact destination/deep link
   - exact action
   - return-to-task state after intervention

## REAL-TIME MODEL

The Command Center should use event-driven updates where supported and short polling only where event/webhook streams are unavailable.

Every displayed metric must carry:

- source
- timestamp / freshness
- status
- confidence/truth state

A stale metric must visibly say **STALE**, not look current.

## UNIFIED EVENT MODEL

Normalize incoming service events into a common envelope:

`event_id, source, resource, event_type, timestamp, correlation_id, truth_state, payload_reference, processing_state`

Keep raw provider payloads in the appropriate source/archive layer; the Command Center consumes normalized events and references.

## ALERTS

Do not create noisy alerts for everything.

Prioritize:

- money stopped
- checkout/payment failure
- webhook failure
- publication queue failure
- deployment failure
- security/authentication failure
- worker/queue stall
- major traffic/conversion anomaly
- provider quota/balance problem when verified
- owner approval required

Each alert must explain **why it matters** and the **next action**.

## PERCENTAGES

Percentages must be computed from real measurements.

Examples:

- catalog readiness = valid products / submitted products
- publication completion = successfully published / intended products
- checkout conversion = completed checkouts / checkout starts
- payment success = successful payments / payment attempts
- queue success = completed jobs / attempted jobs
- system health = defined health checks passing / total health checks

Do not use the legacy `129,600% EFFICIENCY` string as an operational measurement. It can remain a mission/status phrase, but all dashboard percentages must have explicit denominators and timestamps.

## DASHBOARD LAYOUT

### Header

`GODSPEED | SYSTEM HEALTH | MONEY | ALERTS | LAST VERIFIED`

### Mission Strip

`Revenue | Orders | Conversion | Live Products | Queue | Critical Blocker`

### Main Grid

`Commerce | Payments | AI | System`

`Analytics | Operations | Security | Truth`

### Bottom

`Owner Actions | Recent Events | Audit Trail`

## MANUAL / OFFLINE MODE

The dashboard must remain useful when a provider is temporarily unreachable.

Show:

- last known value
- last verified timestamp
- source
- stale/offline state
- queued actions

Never silently substitute old values for live values.

## COMMAND CENTER PRINCIPLE

The owner should be able to open APEX and immediately answer:

**What is making money?**
**What is broken?**
**What is running?**
**What is waiting?**
**What needs me?**
**What changed?**
**What is verified?**
**What should happen next?**

No service-hopping for ordinary oversight.

## ACCEPTANCE TEST

The Command Center is not complete until a single screen can show the connected state and freshness of the major APEX services and identify the highest-priority next action without requiring the owner to inspect each provider separately.
