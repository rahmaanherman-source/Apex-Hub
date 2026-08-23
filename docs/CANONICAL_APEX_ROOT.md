# APEX Canonical Root Control

**Status: CANONICAL ROOT PENDING VERIFICATION**

This repository is the proposed control plane for APEX, but no file in this repository may self-assert canonicality.

## Rule

`DECLARED TARGET != OBSERVED TREE != VERIFIED CANONICAL REPOSITORY`

## Required gates

1. Exact source-tree inventory.
2. Exact commit SHA binding.
3. Successful build and test evidence.
4. Deployment read-back evidence when deployment is claimed.
5. Explicit identity and authority binding.
6. Integration evidence for commerce, identity, AI, vault, command, and evidence/truth systems.

## No Fake Green

A component is GREEN only when its claimed state is backed by executable or externally readable evidence. Documentation, configuration, filenames, and declarations are not proof of execution.

## Reconciliation policy

Until the gates above pass, all other APEX repositories remain source candidates or satellite systems. No repository is promoted to canonical solely because of its name, documentation, or intended architecture.

## Commerce priority

Before scaling product inventory, prove one complete live transaction cycle:

`product -> storefront -> checkout -> payment -> order -> webhook -> reconciliation/audit`

Only after that cycle is independently evidenced should bulk commerce scaling be treated as GREEN.
