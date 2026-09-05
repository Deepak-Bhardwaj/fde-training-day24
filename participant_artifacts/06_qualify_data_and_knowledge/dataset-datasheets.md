# Dataset Datasheets

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 06 — Qualify Data & Knowledge
**Participant status:** COMPLETED
**Deliverable form:** Structured table / register

## Stage question
Is the evidence trustworthy, permissible, traceable, representative and ready?

## Why this artifact exists
To provide standardized, transparent documentation for the core datasets used in this training case study, detailing their composition, collection methods, and known limitations.

## Upstream dependency
Use the completed Stage 06 Data/Knowledge Inventory and Representativeness Assessment.

## Evidence to inspect
- `evidence/01_enterprise_sources/live_disruptions.csv`
- `evidence/01_enterprise_sources/live_event_stream.jsonl`
- `evidence/01_enterprise_sources/source_health_events.jsonl`

## Case challenge
Treat these synthetic training datasets with the same rigor as production data. Document their biases and limitations explicitly.

## Minimum content

### Dataset 1: `live_disruptions.csv`
- **Motivation:** Provides the historical baseline of disruption events, types, and outcomes to measure current-state reconciliation time and plan feasibility.
- **Composition:** Tabular data containing DisruptionID, VesselID, EventType, StartTime, EndTime, ResolutionAction, Outcome.
- **Collection Process:** Synthetic generation based on typical maritime disruption patterns (weather, port, machinery).
- **Preprocessing:** None. Used as-is for baseline metric calculation (Stage 03).
- **Uses:** Training the deterministic engine's feasibility rules; establishing baseline KPIs.
- **Limitations:** Does not contain granular telemetry data; lacks representation of adversarial or multi-compounding disruptions. Represents a "happy path" historical view.

### Dataset 2: `live_event_stream.jsonl`
- **Motivation:** Simulates the real-time, high-frequency edge event stream from vessel telemetry and external APIs to test ingestion, deduplication, and temporal provenance.
- **Composition:** JSON Lines format. Each line is an event with `event_id`, `source_id`, `timestamp`, `payload`, `vessel_id`.
- **Collection Process:** Synthetic stream generator injecting known flaws: ~8% duplicate events, random clock drift (± 2 mins), and out-of-order delivery.
- **Preprocessing:** None. The system's ingestion layer must handle the flaws dynamically.
- **Uses:** Testing BR-05 (Temporal Idempotency), evaluating the ACL and deduplication logic.
- **Limitations:** Synthetic drift may not perfectly mimic real-world satellite latency spikes. Payloads are simplified compared to real NMEA or proprietary telemetry formats.

### Dataset 3: `source_health_events.jsonl`
- **Motivation:** Tracks the availability, latency, and error rates of the 9 enterprise sources to test the system's graceful degradation and offline fallback mechanisms.
- **Composition:** JSON Lines format. Events include `source_id`, `status` (UP/DEGRADED/DOWN), `latency_ms`, `timestamp`.
- **Collection Process:** Synthetic generator simulating intermittent API outages (especially SRC-WX and SRC-PORT) and sat-com blackouts.
- **Preprocessing:** None.
- **Uses:** Evaluating system behavior during GS-06 (Weather unavailable) and GS-14 (Prolonged blackout).
- **Limitations:** Blackout durations are capped in the synthetic data; real-world blackouts could be unbounded.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| The event stream contains intentional flaws (duplicates, drift) to test system resilience. | `live_event_stream.jsonl` structure, `source_inventory.csv` (known issues) | `quality-profile.md` | High confidence (explicit synthetic design). |
| Historical disruption data lacks adversarial or multi-compounding scenarios. | Analysis of `live_disruptions.csv` | `representativeness-assessment.md` | High confidence (empirical observation). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The synthetic datasets are sufficient to pass the Stage 07 evaluation harness without requiring live production data. | This is a synthetic training case; live data is explicitly out of scope. | FDE Team / Executive Sponsor | If evaluators demand live data, the training boundary is violated. | `START_HERE.md` (Synthetic training case only). |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Data and knowledge readiness assessment
Do not advance to Stage 07 until the Stage 06 exit gate is defensible.