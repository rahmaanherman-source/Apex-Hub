# APEX Authorized Security Operations

## Purpose

A defensive security operations layer for systems that APEX is explicitly authorized to assess. The goal is to discover weaknesses, preserve evidence, measure risk, and produce remediation-ready findings before criminals can exploit them.

## Operating boundary

This system is for assets owned by APEX, explicitly authorized customer assets, or environments covered by written authorization. Every assessment must have a scope, authorization reference, start/end window, and permitted test classes before active testing is enabled.

## Core loop

REMEMBER → AUDIT → REBUILD → REBOOT → VERIFY

Security-specific execution:

DISCOVER → SCOPE → ENUMERATE → CHECK → EVIDENCE → TRIAGE → REMEDIATE → RETEST → REPORT

## No-Fake-Green rule

A control is not GREEN because a scan ran. GREEN requires evidence that the required security property was actually observed. UNKNOWN, BLOCKED, and NOT-IN-SCOPE are distinct states.

## Safety rules

- Default mode is passive/non-destructive.
- No exploit execution, credential theft, persistence, evasion, destructive testing, or denial-of-service behavior by default.
- Active testing requires an explicit authorized scope and test profile.
- Secrets are never written to reports, logs, browser state, or source control.
- Findings retain provenance: asset, check, timestamp, evidence reference, and verification state.
- Remediation must be followed by a real retest.

## Initial capabilities

1. Authorization/scope registry
2. Asset inventory
3. Security check registry
4. Evidence ledger
5. Finding lifecycle
6. Remediation tracking
7. Retest verification
8. Executive and technical reporting
9. Local-first operation

## Future integrations

The architecture can later connect to approved scanners and cloud/security providers, but integrations do not override scope or authorization controls.
