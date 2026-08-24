# APEX Model Fabric Runbook

## Discovery

Probe real local runtimes and record exact model identity, tag/version, digest where available, runtime, endpoint, path, hardware node, source, and license evidence. A catalog entry is never an installation claim.

## Admission

For every candidate verify: installed, healthy, enabled, capability tested, license/commercial-use status appropriate to the task, privacy policy, and hardware admission. Measure actual VRAM/RAM rather than trusting catalog minimums.

## VRAM policy

Reserve `max(2048 MB, 15% of total VRAM)` from free VRAM. Estimate weights + KV/context + workload overhead + latent/workflow memory + safety margin. Admit only when the estimate fits. If not: smaller verified model, lower quantization, reduce context/batch, reduce media size/duration, queue, permitted CPU/offload, block, then authorized cloud escalation.

## Routing

Hard filters precede ranking. Local is the default. A cloud adapter is never called merely because local selection failed. The router returns `CLOUD_ESCALATION` and records the local-gap evidence. Approval must cover provider, task/data class, egress, estimated cost, and execution scope.

## Audit

Emit `model.discovered`, `model.health_checked`, `model.capability_tested`, `model.benchmarked`, `model.license_reviewed`, `model.enabled`, `model.route_selected`, `model.fallback`, `model.no_route`, and cloud escalation events as appropriate. Thread the same `correlation_id` across intent → router → adapter → result → outcome.

## Truth gate

Material claims require current verified evidence. For publication, payment, deployment, or irreversible action, unsupported or stale evidence blocks execution. AI-generated text is never itself canonical evidence.

## Reboot

Preserve immutable evidence; reload the active project slab; verify source hashes/freshness; flag contradictions; retrieve current sources; supersede stale derived facts without erasing history; rebuild context; rerun evaluation gates.

## Continuous evaluation

Re-run the evaluation pack when model digest/version, prompt, knowledge corpus, retrieval configuration, tools, context envelope, policy threshold, product/category, or market changes. Record grounding, unsupported-claim rate, schema validity, latency, cost, tool safety, and failures.

## Operational statuses

- `CATALOG ONLY`
- `DISCOVERED LOCAL`
- `VERIFIED LOCAL`
- `LOCAL DEGRADED`
- `CLOUD ESCALATION`
- `BLOCKED`
- `FAILED`

Never display `VERIFIED`, `HEALTHY`, `ORDERABLE`, `LIVE`, or equivalent status without corresponding evidence.
