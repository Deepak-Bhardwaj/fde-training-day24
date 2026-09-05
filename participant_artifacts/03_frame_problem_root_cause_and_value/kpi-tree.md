# KPI Tree

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 03 — Frame Problem, Root Cause & Value
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
What evidence proves the problem, its causes and its value?

## Why this artifact exists
This artifact is part of the evidence needed to reach **Evidence-backed problem and measurable baseline**. It must be consistent with approved upstream artifacts.

## Upstream dependency
Use the completed Stage 03 SCQA Problem Frame and Baseline Dataset.

## Evidence to inspect
- `evidence/01_enterprise_sources/live_disruptions.csv`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
Define a hierarchical tree of Key Performance Indicators (KPIs) that measure the success of the future state without violating non-negotiable constraints.

## Minimum content

| KPI Level | KPI Name | Definition | Baseline (Current State) | Target (Future State) | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Level 1 (Outcome)** | Operational Resilience & Safety | The ability to safely execute recovery options during disruptions without violating authority or technical holds. | Qualitative (Ad-hoc) | 100% compliance with Golden Scenarios | `engagement-charter.md` |
| **Level 2 (Driver)** | Time-to-Reconcile | Time taken from disruption detection to a unified, authority-weighted constraint view. | 45 minutes | < 10 minutes | `baseline-dataset.csv` (M-01) |
| **Level 2 (Driver)** | Plan Feasibility Rate | Percentage of generated recovery plans that remain feasible after all constraints (CMMS, Cargo) are applied. | 78% | > 95% | `baseline-dataset.csv` (M-02) |
| **Level 2 (Driver)** | Offline Continuity Uptime | Percentage of time the vessel-side workbench can operate fully without shore connectivity. | 0% (Fully dependent on shore) | 100% for critical functions | `fleet_operations_interview_notes.md` |
| **Level 3 (Diagnostic)** | Semantic Conflict Resolution Time | Time taken to resolve API vs. Signed Notice mismatches. | High (Manual) | < 1 minute (Automated authority weighting) | `fleet_operations_interview_notes.md` |
| **Level 3 (Diagnostic)** | Temporal Provenance Compliance | Percentage of ingested events with valid source and ingestion timestamps. | ~92% (Due to clock drift/duplicates) | 100% | `live_event_stream.jsonl` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Time-to-reconcile is currently ~45 minutes. | `fleet_operations_interview_notes.md` | `baseline-dataset.csv` | High confidence (SME interview). |
| Plan feasibility is currently ~78% due to late constraints. | `live_disruptions.csv` | `root-cause-analysis.md` | Medium confidence (historical logs). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: A target of < 10 minutes for reconciliation is technically feasible with current edge compute. | Edge compute limits not fully defined. | Shore Platform Team | May require adjusting the target or upgrading vessel hardware. | Stage 10 Deployment Topology. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Evidence-backed problem and measurable baseline
Do not advance to Stage 04 until the Stage 03 exit gate is defensible.