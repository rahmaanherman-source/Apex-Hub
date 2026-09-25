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


## 13A. Environmental, Thermal, Building-Envelope, and Site-Factor Matrix

The system shall not be designed from nominal temperature alone. The engineering model must account for the combined environmental and building-envelope conditions that can change energy production, equipment temperature, structural loading, HVAC demand, sensor readings, serviceability, and component life.

### A. Temperature extremes and thermal cycling

Evaluate at minimum:

- High ambient conditions, including **100°F-class outdoor conditions** and higher design extremes where applicable.
- Direct solar loading on rooftop enclosures, metal surfaces, cables, mounts, and walls.
- Radiant heat from roofs, walls, pavement, adjacent equipment, and exhaust.
- Low-temperature operation and freeze conditions.
- Rapid day/night temperature changes.
- Seasonal thermal cycling.
- Temperature differences between sun-exposed and shaded components.
- Temperature rise inside sealed enclosures.
- Heat generated by electrical components.
- Heat conducted through mounting hardware and wall penetrations.
- Thermal expansion/contraction of dissimilar materials.
- Temperature-dependent sensor drift and generator performance.

A component's ambient rating shall not be treated as its actual operating temperature without an enclosure and heat-transfer analysis.

### B. Building-wall / thermal-chimney interface

If an energy-capture, heat-transfer, airflow, or thermal-chimney-style board/panel is mounted against or through a building wall, the design must explicitly model the temperature on **both sides of the wall**.

The system shall account for:

- Indoor conditioned-air temperature.
- Outdoor ambient temperature.
- Solar-heated exterior wall temperature.
- Interior wall-surface temperature.
- Wall cavity temperature where accessible/relevant.
- Insulation thickness and thermal resistance.
- Thermal bridges through fasteners and framing.
- Air leakage around penetrations.
- Moisture migration.
- Condensation/dew-point conditions.
- Stack/pressure effects.
- Exterior wind pressure and suction.
- Airflow direction and recirculation.
- HVAC intake/exhaust locations.
- Nearby doors, windows, vents, chimneys, and mechanical equipment.
- Whether the wall is in sun or shade during each operating period.

**Design rule:** A wall-mounted thermal/air-energy interface must never assume that the temperature immediately outside the wall equals the free-air ambient temperature, or that the temperature immediately inside the wall equals the thermostat reading.

Where the exact wall/interface concept is still being finalized, it shall remain a separately identified engineering variable rather than being silently assumed.

### C. Airflow and wind environment

Evaluate:

- Free-stream wind.
- Turbulence caused by roof edges and parapets.
- Building wake effects.
- Corner acceleration.
- Wind direction changes.
- Gusts.
- Seasonal prevailing winds.
- Airflow around neighboring buildings.
- Rooftop obstacles.
- Chimney/stack effects.
- HVAC exhaust and intake interference.
- Recirculation.
- Pressure differential across the building envelope.

The energy-capture mechanism shall be characterized under real turbulent building airflow, not only ideal laboratory airflow.

### D. Water, humidity, ice, snow, and condensation

Evaluate:

- Rain exposure.
- Wind-driven rain.
- Standing water.
- Drainage paths.
- Splashback.
- Condensation.
- Dew point.
- Freeze/thaw cycles.
- Ice accumulation.
- Snow accumulation.
- Snow shedding.
- Water intrusion at cable entries and enclosure seams.
- Moisture trapped between dissimilar materials.
- Corrosion caused by persistent moisture.

Cable entries and penetrations must have engineered water-management details; sealing alone is not a substitute for drainage design.

### E. Solar, UV, and material aging

Evaluate:

- UV exposure.
- Solar heating.
- Albedo/reflected radiation.
- Roof surface temperature.
- Paint/coating degradation.
- Polymer aging.
- Cable-jacket aging.
- Seal/gasket aging.
- Adhesive aging.
- Galvanic corrosion.
- Coating compatibility.
- Expansion mismatch between metal, polymer, glass, composites, and structural materials.

Any adhesive or epoxy used in the final design must be selected from verified environmental, vibration, temperature, substrate, and service-life requirements rather than assumed suitable from a generic outdoor rating.

### F. Mechanical loading

Evaluate:

- Static weight.
- Wind pressure.
- Wind uplift.
- Gust loading.
- Cyclic fatigue.
- Vibration.
- Generator imbalance.
- Resonance.
- Fastener fatigue.
- Thermal expansion.
- Snow/ice loading.
- Maintenance loads.
- Cable movement.
- Structural attachment loads.
- Roof/wall framing capacity.
- Equipment-induced vibration transmitted into the building.

The structural system shall be evaluated as a building attachment, not merely as a machine frame.

### G. Electrical and electromagnetic environment

Evaluate:

- Generator output variation.
- Startup/shutdown transients.
- Overvoltage.
- Overcurrent.
- Short-circuit conditions.
- Surge exposure.
- Lightning environment.
- Grounding/bonding.
- Cable voltage drop.
- Conductor heating.
- Connector heating.
- Electromagnetic interference.
- Sensor noise.
- Communications loss.
- Battery fault conditions where storage is used.

### H. HVAC interaction

The system shall account for the fact that the building's energy demand changes with environmental conditions.

Monitor and correlate:

- Indoor temperature.
- Outdoor temperature.
- Humidity.
- HVAC demand.
- Heating/cooling runtime.
- Supply/return conditions where instrumentation supports it.
- Building occupancy schedules where authorized.
- Solar exposure.
- Energy generation.
- Energy consumption.
- Storage state.
- Peak demand periods.

The controller should distinguish **energy generation problems** from **building-load problems**. A hot day can simultaneously increase HVAC demand and change rooftop equipment temperature.

### I. Sensor placement and truth model

Sensors shall be placed so they measure the condition they are intended to represent.

The design must distinguish:

- Free-air outdoor temperature.
- Rooftop surface temperature.
- Enclosure internal temperature.
- Generator temperature.
- Wall exterior temperature.
- Wall interior temperature.
- Indoor room temperature.
- Cable/connector temperature where required.
- Bearing/mechanical temperature where applicable.

No single temperature sensor should be treated as representative of the entire system.

### J. Serviceability under environmental conditions

Ground-level serviceability must include the conditions under which technicians actually work:

- Extreme heat.
- Cold.
- Rain.
- Snow/ice.
- Wet equipment.
- Reduced visibility.
- Night service.
- Electrical isolation.
- Safe cabinet access.
- Replacement-part storage.
- Condensation after cabinet opening.
- Temporary environmental protection during service.

The service cabinet shall be positioned so routine maintenance does not require rooftop access and does not place technicians unnecessarily in hazardous environmental conditions.

### K. Site survey requirement

Before prototype installation, record:

1. Building orientation.
2. Roof/wall geometry.
3. Wall construction.
4. Insulation and thermal-envelope characteristics where known.
5. Roof membrane/material.
6. Nearby structures.
7. Parapets and roof edges.
8. HVAC intakes/exhausts.
9. Chimneys/vents.
10. Trees and other wind obstructions.
11. Solar exposure by time of day/season.
12. Prevailing wind conditions.
13. Drainage paths.
14. Snow/ice exposure.
15. Service access path.
16. Electrical service location.
17. Grounding/bonding provisions.
18. Structural attachment points.
19. Indoor/outdoor temperature measurement locations.
20. Any wall-mounted thermal/airflow board or chimney-interface geometry.

### L. Measurement contract

Before claiming performance, capture synchronized measurements for:

**Environment → Mechanical State → Electrical State → Building Load → Storage State → Control State**

Each measurement record should include:

- Timestamp
- Sensor/device ID
- Calibration/verification ID where applicable
- Location
- Units
- Measurement
- Operating state
- Relevant environmental conditions
- Data-quality/status flag

This prevents a favorable single measurement from being mistaken for system-level performance.


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