# Security Operations Architecture

```text
                    GABBY / APEX UI
                           |
                    AUTHORIZATION GATE
                           |
                    SCOPE REGISTRY
                           |
          +----------------+----------------+
          |                                 |
     ASSET INVENTORY                    TEST POLICY
          |                                 |
          +----------------+----------------+
                           |
                    SAFE CHECK ENGINE
                           |
              +------------+------------+
              |            |            |
          CONFIG       NETWORK       APP/API
           CHECKS       CHECKS        CHECKS
              |            |            |
              +------------+------------+
                           |
                     EVIDENCE LEDGER
                           |
                    FINDING TRIAGE
                           |
                 REMEDIATION / RETEST
                           |
                    VERIFIED REPORT
```

## Components

### Scope Registry
Stores authorization and permitted targets/test classes. It is the first execution gate.

### Asset Inventory
Tracks approved domains, applications, APIs, repositories, cloud resources, and other explicitly authorized assets.

### Safe Check Engine
Runs deterministic, non-destructive checks first. Examples include TLS configuration inspection, security-header checks, dependency/version inventory, exposed-service inventory, authentication configuration checks, and application security posture checks.

### Evidence Ledger
Append-only records connect each finding to the target, check, timestamp, tool/version, and evidence reference.

### Finding Lifecycle
`DISCOVERED → VALIDATING → CONFIRMED → REMEDIATION → RETEST → VERIFIED/CLOSED`

### Truth states

- GREEN / VERIFIED
- YELLOW / NEEDS REVIEW
- GRAY / UNKNOWN
- RED / FAILED or CONTRADICTED
- BLOCKED / AUTHORIZATION GATE

## Design principle

The system is an authorized defensive assessment platform, not an autonomous offensive agent. It should make it easier for an authorized security professional to find and fix weaknesses while making unauthorized targeting technically difficult by default.
