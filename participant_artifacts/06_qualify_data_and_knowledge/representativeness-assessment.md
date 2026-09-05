# Representativeness Assessment

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 06 — Qualify Data & Knowledge
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
Is the evidence trustworthy, permissible, traceable, representative and ready?

## Why this artifact exists
To evaluate whether the available baseline data and event streams adequately represent the full spectrum of operational realities, specifically the 15 Golden Scenarios (GS-01 to GS-15) that the system must handle.

## Upstream dependency
Use the completed Stage 03 Baseline Dataset and Stage 06 Data/Knowledge Inventory.

## Evidence to inspect
- `evidence/01_enterprise_sources/live_disruptions.csv`
- `evidence/01_enterprise_sources/live_event_stream.jsonl`
- `evidence/01_enterprise_sources/source_health_events.jsonl`
- `Participant_Case_Study.md` (Golden Scenarios)

## Case challenge
Identify where the data is sparse, biased, or entirely missing for critical edge cases. Do not assume the historical data covers all future risks.

## Minimum content

| Golden Scenario Category | Scenarios Covered | Data Representativeness | Gap / Bias Identified | Mitigation Strategy | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Nominal / Common Disruptions** | GS-01 (Port congestion), GS-05 (Stale port constraint) | **High.** Abundant historical data in `live_disruptions.csv`. | None. | Use as baseline for deterministic engine tuning. | `live_disruptions.csv` |
| **Severe Weather / Master Authority** | GS-02 (Severe weather), GS-06 (Weather source unavailable) | **Medium.** Weather data exists, but "source unavailable" events are rare in historical logs. | Lack of historical data for prolonged WX outages. | Inject synthetic WX outage events into the evaluation harness. | `source_health_events.jsonl` |
| **Technical / CMMS Constraints** | GS-03 (Critical machinery hold) | **Medium.** CMMS holds are recorded, but the exact temporal lag between hold issuance and FMS visibility is not fully captured. | Latency of CMMS-to-FMS propagation is assumed, not measured. | Define explicit SLA for CMMS sync in Stage 09. | `source_inventory.csv` |
| **Identity / Semantic Conflicts** | GS-04 (Vessel identity ambiguity), GS-11 (Conflicting berth) | **Low.** These are rare, high-impact edge cases. Historical data likely lacks sufficient examples of AIS vs. FMS conflicts. | Severe class imbalance; model/rules might overfit to "happy path" identity. | Rely on deterministic `source_authority.yaml` rules, not statistical learning, for identity resolution. | `source_authority.yaml` |
| **Connectivity / Offline / Reconnect** | GS-07 (Duplicate event), GS-13 (Clock drift), GS-14 (Prolonged blackout), GS-15 (Reconnect reconciliation) | **Low/Medium.** Telemetry stream shows some duplicates/drift, but prolonged blackouts are not well-represented in standard logs. | Lack of real-world data for multi-hour sat-com blackouts and the resulting state divergence. | Stage 07 must define synthetic stress tests for GS-14 and GS-15. | `source_health_events.jsonl` |
| **Adversarial / Injection** | GS-08 (Unauthorized commit), GS-09 (Prompt injection), GS-10 (AI unavailable), GS-12 (Superseded policy trap) | **Zero.** These are security and failure-mode scenarios. Historical operational data will not contain "prompt injections" or "unauthorized commits". | Entirely missing from historical data. | Must be explicitly simulated in Stage 07 evaluation scenarios. | `Participant_Case_Study.md` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Adversarial and connectivity scenarios are not represented in historical operational data. | Absence of such events in `live_disruptions.csv` and `live_event_stream.jsonl`. | `baseline-dataset.csv` | High confidence (empirical observation). |
| Identity conflicts are rare, requiring deterministic rules over probabilistic models. | `source_authority.yaml` (explicit precedence rules) | `quality-profile.md` | High confidence (explicit policy). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: Synthetic data generation for GS-14 (Prolonged blackout) will accurately mimic real vessel-edge state divergence. | Exact state-drift mechanics during a blackout are theoretical. | FDE Team | Stage 07 evaluation harness must be carefully calibrated to avoid false positives/negatives. | Stage 07 Evaluation Scenarios. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Data and knowledge readiness assessment
Do not advance to Stage 07 until the Stage 06 exit gate is defensible.