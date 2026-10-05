# APEX Build Law — Repair Before Expansion

**Fix the existing action before adding another action.** Completion requires working behavior plus executable evidence.

Inspect first. Snapshot first. Make the smallest requested change. Preserve working behavior. Run the real build/tests. If a regression appears, stop and revert to the last known-good state rather than fixing forward blindly.

Evidence: `DOCUMENTED` → `SCAFFOLDED` → `RUNNABLE` → `BENCHMARKED` → `VERIFIED`.
Failure states: `BLOCKED` | `UNVERIFIED`.

Never mark simulated, skipped, inferred, or unexecuted checks green. Record defects, repairs, tests, commands, preserved behavior, and blockers.

Repair the real bottleneck before adding more surface area.
