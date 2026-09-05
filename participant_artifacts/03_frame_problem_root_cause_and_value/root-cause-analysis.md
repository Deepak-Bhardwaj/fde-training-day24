# Root-Cause Analysis

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 03 — Frame Problem, Root Cause & Value
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
What evidence proves the problem, its causes and its value?

## Why this artifact exists
This artifact is part of the evidence needed to reach **Evidence-backed problem and measurable baseline**. It must be consistent with approved upstream artifacts.

## Upstream dependency
Use the completed Stage 01, Stage 02, and Stage 03 SCQA Problem Frame.

## Evidence to inspect
- `evidence/01_enterprise_sources/live_disruptions.csv`
- `evidence/01_enterprise_sources/live_event_stream.jsonl`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
Identify the root causes of the current process failures using the 5 Whys or similar structured method, grounded strictly in evidence.

## Minimum content

| Problem Symptom | Root Cause Category | Root Cause Description | Evidence |
| :--- | :--- | :--- | :--- |
| Recovery plans are frequently infeasible after formulation. | **Process / Data Latency** | Hard constraints (CMMS maintenance holds, Cargo windows) arrive late or are not synchronized with the FMS planning engine at the time of plan generation. | `fleet_operations_interview_notes.md`, `live_disruptions.csv` |
| Controllers spend excessive time reconciling data versions. | **Semantic Fragmentation** | Port systems use conflicting semantics between API status ("available") and signed legal notices ("confirmed"). Controllers must manually determine authority. | `fleet_operations_interview_notes.md`, `source_inventory.csv` |
| Vessel and shore teams operate on different realities during events. | **Temporal Misalignment** | Vessel telemetry suffers from clock drift and duplicate delivery. Without strict temporal provenance, shore and vessel systems cannot agree on the "current" state. | `live_event_stream.jsonl`, `source_inventory.csv` |
| Post-event learning and audits are ineffective. | **Architecture / Traceability** | Rationale, source freshness, and final outcomes are not linked in a unified decision trace. | `fleet_operations_interview_notes.md` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Clock drift in telemetry prevents accurate state reconciliation. | `live_event_stream.jsonl` (timestamp deltas), `source_inventory.csv` | `scqa-problem-frame.md` | High confidence (event stream data). |
| Semantic mismatch in port data forces manual human intervention. | `fleet_operations_interview_notes.md` | `waste-register.md` | High confidence (SME interview). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: CMMS asset ID mapping discrepancies are the primary reason for late constraint visibility. | Exact CMMS integration logs not provided. | Technical Operations | May require a dedicated entity resolution strategy in Stage 09. | Stage 09 Entity Resolution Specification. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Evidence-backed problem and measurable baseline
Do not advance to Stage 04 until the Stage 03 exit gate is defensible.