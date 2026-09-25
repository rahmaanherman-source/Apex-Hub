# APEX Ground-Service Energy System
## Blueprint v1.0

**Status:** DESIGN BASELINE — BLUEPRINT FIRST
**Architecture principle:** Nothing that routinely requires human service shall require routine rooftop access.

## 1. Purpose
Define the physical, electrical, control, service, diagnostic, and safety architecture for an APEX rooftop energy system whose routine service is performed from ground level.

This is an architecture specification, not construction instructions. Final electrical, structural, fire, wind-loading, battery, and grid-interconnection designs must be engineered and verified before deployment.

## 2. Core Design Laws
1. **Roof = longevity.** Rooftop hardware prioritizes environmental protection, passive operation, monitoring, and long service intervals.
2. **Ground = replacement.** Routine-service electronics and interfaces are consolidated into an accessible ground-level cabinet.
3. **Software = diagnosis.** Software identifies equipment, health, faults, service location, and recovery procedure.
4. **Safety = independent.** Fundamental safety functions do not depend on AI, cloud connectivity, or internet availability.
5. **Modularity = replaceability.** Serviceable functions are modularized so a failed module can be replaced without replacing the entire system.
6. **Fallback = normal building operation.** Failure of the energy subsystem must not unnecessarily disable conventional HVAC operation.

## 3. System Architecture
ROOFTOP → protected conduit → GROUND SERVICE ZONE → HVAC / STORAGE / APEX NETWORK

ROOFTOP: mechanical energy capture, generator/alternator, mechanical transmission if required, environmental/temperature/vibration sensing, protected cable termination, structural mounting.

GROUND CABINET: 01 Main Disconnect; 02 Generator Input / Rectification; 03 Electrical Protection; 04 Energy Management Controller; 05 Storage / BMS Interface; 06 Metering; 07 Communications; 08 HVAC Interface; 09 Local Service / Test Interface.

## 4. Rooftop Module
Only equipment justified by the energy-generation mechanism or sensing requirements belongs on the roof.

Candidate rooftop functions: mechanical energy capture; generator/alternator; mechanical transmission; environmental sensing; generator temperature; vibration/condition monitoring; rotation/state sensing; protected cable termination; structural mounting and environmental enclosure.

Explicit exclusions from routine rooftop service: user interface, primary control computer, routine-access batteries, routine-access replaceable electronics, cloud-dependent control equipment, consumer controls.

## 5. Ground Energy Control Cabinet
The cabinet is the primary service location.

01 Main disconnect / isolation
02 Generator input and rectification / conditioning as applicable
03 Overcurrent, surge, grounding/bonding and protective functions as engineered
04 Local energy-management controller
05 Storage / BMS interface
06 System-appropriate metering
07 Communications / telemetry
08 HVAC interface
09 Local diagnostics and service interface

Exact topology depends on generator output, storage architecture, building interface, and whether the system is isolated or grid-connected.

## 6. APEX Energy Brain
The Energy Brain is the local controller responsible for deterministic local operation, state management, diagnostics, and coordination. It is separate from the thermostat and separate from cloud AI.

Local responsibilities: read sensors; track system state; apply operating limits; coordinate energy flows; monitor faults; record events; expose service diagnostics; maintain fallback behavior; provide authorized local service access.

## 7. APEX Climate Node
The thermostat becomes a human-facing climate and energy interface rather than the system's sole brain.

Candidate functions: indoor temperature, outdoor temperature, HVAC demand, energy generation status, storage state, consumption, system health, fault notifications, service status, energy history, user controls.

The Climate Node must not be a single point of failure for fundamental HVAC or energy safety.

## 8. Control Hierarchy
LEVEL 0 — HARDWARE / MECHANICAL SAFETY
LEVEL 1 — LOCAL ENERGY BRAIN
LEVEL 2 — APEX INTELLIGENCE
LEVEL 3 — REMOTE SERVICE / CLOUD

Level 0: independently engineered protective mechanisms.
Level 1: safe local operation without internet access.
Level 2: optimization, forecasting, diagnostics, anomaly detection, and energy-management assistance.
Level 3: telemetry, service notifications, fleet management, diagnostics, authorized remote configuration, and maintenance planning.

## 9. Serviceability Contract
Every serviceable component must have: unique component ID; defined physical location; defined function; health state; failure state; diagnostic evidence; safe fallback; replacement procedure; verification procedure; service history.

Example diagnostic: FAULT MODULE 04 / Energy Controller / Communication failure / Service Location Ground Cabinet / Roof Access NOT REQUIRED / Action Diagnose or replace Module 04 / System Safety ACTIVE / HVAC Fallback AVAILABLE.

## 10. Failure Philosophy
Climate Node failure → local HVAC fallback remains available.
Cloud unavailable → local system continues operating.
AI unavailable → deterministic controller continues operating.
Communications failure → local control continues; fault logged.
Roof generator unavailable → building retains normal HVAC operation.
Individual cabinet module failure → isolate and replace module where safe.
Sensor failure → defined degraded/failsafe state.
Storage fault → isolate storage according to engineered protection strategy.

## 11. Diagnostics
Every device should expose: DEVICE ID, LOCATION, FUNCTION, STATE, HEALTH, FAULT CODE, FAULT SEVERITY, FIRST OBSERVED, LAST OBSERVED, DEPENDENCIES, SAFE FALLBACK, SERVICE ACTION, VERIFICATION TEST, SERVICE HISTORY.

This data model should feed the APEX audit/event architecture rather than become an isolated monitoring system.

## 12. Physical Service Design
The ground cabinet should provide clear module identification, service labels, appropriate test points, modular service architecture where appropriate, protected connectors, disconnect/isolation points, status indicators, QR/NFC service identity where useful, and local diagnostic access.

Routine service should be possible without rooftop access whenever the fault is located in the ground-service domain.

## 13. Safety Requirements
Final engineering must address, as applicable: electrical isolation; overcurrent protection; grounding and bonding; surge protection; generator overspeed/overtemperature protection; mechanical containment; structural attachment; wind loading; weather exposure; battery protection/BMS; fire protection; emergency shutdown; grid interconnection and anti-islanding where applicable; applicable electrical/building/mechanical/fire codes.

No grid-connected implementation should be treated as a prototype wiring exercise; it requires appropriate engineering and approval.

## 14. Engineering Sequence
1. Freeze requirements.
2. Define energy-source mechanism.
3. Define energy-flow topology.
4. Define rooftop mechanical envelope.
5. Define ground cabinet architecture.
6. Define control hierarchy.
7. Define serviceability contract.
8. Define electrical protection architecture.
9. Define sensing and telemetry contract.
10. Define HVAC interface and fallback behavior.
11. Perform structural, electrical, thermal, and environmental analysis.
12. Build bench prototype.
13. Instrument and measure.
14. Perform controlled subsystem tests.
15. Conduct design review before field installation.

## 15. Non-Goals for v1
No power-output claim without measurement.
No assumption that the rooftop mechanism can power full building HVAC load.
No grid-interconnection claim.
No final component ratings until generator and electrical topology are frozen.
No rooftop service requirement as a design shortcut.

## 16. Acceptance Principle
A design is not ground-serviceable merely because the controller is downstairs. It must demonstrate that expected routine failure modes can be diagnosed, isolated, serviced, and verified from the ground service zone without routine rooftop access.

**APEX Ground-Service Energy System — Blueprint v1.0**