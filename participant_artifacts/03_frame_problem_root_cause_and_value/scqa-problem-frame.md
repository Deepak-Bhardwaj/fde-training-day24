# SCQA Problem Frame

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 03 — Frame Problem, Root Cause & Value
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
What evidence proves the problem, its causes and its value?

## Why this artifact exists
This artifact is part of the evidence needed to reach **Evidence-backed problem and measurable baseline**. It must be consistent with approved upstream artifacts.

## Upstream dependency
Use the completed Stage 01 and Stage 02 artifacts.

## Evidence to inspect
- `evidence/01_enterprise_sources/live_disruptions.csv`
- `evidence/01_enterprise_sources/live_event_stream.jsonl`
- `evidence/01_enterprise_sources/source_health_events.jsonl`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
Frame the problem strictly using observed evidence. Do not propose a solution, model, or architecture in this artifact.

## Minimum content

| Element | Description | Evidence |
| :--- | :--- | :--- |
| **Situation** | MeridianBlue Shipping operates a complex fleet relying on 9 disparate enterprise data sources (AIS, Telemetry, Port, Weather, FMS, CMMS, Cargo, Crew, Policy) to manage voyages and disruptions. | `source_inventory.csv`, `system-landscape.md` |
| **Complication** | During disruptions, controllers face severe delays and errors due to semantic conflicts (e.g., Port API vs. signed notices), temporal misalignment (telemetry clock drift), and late-arriving hard constraints (CMMS holds). Vessel and shore state diverge during connectivity loss, and post-event learning is fragmented. | `fleet_operations_interview_notes.md`, `live_disruptions.csv`, `waste-register.md` |
| **Question** | How can vessel and shore teams reconcile disruption evidence and compare recovery options while preserving the Master’s command authority, ensuring offline continuity, and maintaining reconstructable decisions? | `engagement-charter.md`, `governance-raci.md` |
| **Answer** | By establishing an evidence-backed decision-support capability that enforces strict source authority, temporal provenance, and human-in-the-loop governance, rather than relying on manual reconciliation or autonomous AI execution. | `brownfield-assessment.md`, `trust-boundaries.md` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Semantic conflicts and temporal misalignment are the primary drivers of reconciliation delays. | `fleet_operations_interview_notes.md`, `live_event_stream.jsonl` | `process-value-stream-map.md` | High confidence (SME interview + event stream analysis). |
| Late-arriving constraints (CMMS/Cargo) cause commercially optimal plans to become infeasible. | `fleet_operations_interview_notes.md`, `live_disruptions.csv` | `waste-register.md` | High confidence (SME interview). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The frequency of connectivity blackouts is high enough to require full offline vessel-side capability. | Exact VSAT/LEO uptime SLA not fully quantified in `source_health_events.jsonl`. | Shore Platform Team | Dictates the edge-compute requirements in Stage 10. | Stage 10 Deployment Topology. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Evidence-backed problem and measurable baseline
Do not advance to Stage 04 until the Stage 03 exit gate is defensible.