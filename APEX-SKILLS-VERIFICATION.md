# APEX Skills + Verification Contract

This repository now treats Agent Skills as portable capability packages and separates **research**, **execution**, **evidence**, and **governance**.

## Truth rule
A registry entry is a claim. A status is not evidence. `VERIFIED` is allowed only when an executable check succeeds and the resulting evidence artifact is persisted and traceable to the tested capability/version.

## Status dimensions
- `test_status`: what the executable verification currently proves.
- `apex_status`: governance state. Runtime verification never silently promotes governance approval.

## Verification flow
`RESEARCHED -> CANDIDATE -> executable test -> evidence -> TESTED/VERIFIED`

A failed check records failure. Missing checks are skipped rather than treated as success. Synthetic responses, placeholder hashes, placeholder signatures, and hard-coded green statuses are prohibited.

## Agent Skills
Skills follow the published Agent Skills structure: a skill directory contains `SKILL.md`; frontmatter requires `name` and `description`; names must be lowercase and match the directory; longer material belongs in references/scripts/assets. The official documentation index is maintained at agentskills.io.

## What is real in this implementation
- The repository is real and the CI workflow is real.
- The validator is executable Python and fails on structural violations.
- The verification engine executes declared commands and records evidence.
- The Truth Gate checks both status and resolvable evidence files.
- The capability registry intentionally uses conservative `RESEARCHED/CANDIDATE` states until live tests prove more.

## What is deliberately NOT claimed
No external API, Godspeed engine, Golden World renderer, 3D pipeline, signature, deployment, or adapter is marked verified by this change unless a real executable check and evidence artifact prove it.

That is the APEX no-fake-green boundary.
