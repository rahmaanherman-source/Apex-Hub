# APEX Ground-Service Energy System
## Serviceability Contract v1.0

**Status:** DESIGN BASELINE

## Principle
Routine human service belongs at ground level.

## Component Contract
Every component that can require service shall declare: component ID; physical service location; function; inputs; outputs; normal operating state; fault states; dependencies; safe fallback; isolation procedure; replacement procedure; verification test; service history.

## Service-Location Rule
A component classified as routine-serviceable shall not be placed on the roof unless engineering review explicitly demonstrates that routine ground-level service is unnecessary because the component is designed as a long-life/passive element.

## Diagnostic Message Standard
SYSTEM / COMPONENT / FAULT / SEVERITY / SERVICE LOCATION / ROOF ACCESS REQUIRED YES-NO / SAFE STATE / ACTION / VERIFICATION

## Design Review Question
Can a technician diagnose and restore this subsystem from the ground without climbing onto the roof?

If the answer is no, the design requires justification or redesign before prototype approval.

## Versioning
This contract is subordinate to the APEX Hub Master Product Constitution and should integrate with the APEX identity, event, audit, health, and capability architecture.