# Waste Register

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench

**Stage:** 02 — Discover Process & Architecture

**Participant status:** COMPLETED

**Deliverable form:** Structured table / register

## Stage question
How does the real brownfield process and system operate today?

## Why this artifact exists
This artifact is part of the evidence needed to reach **Current-state process and architecture baseline**. It must be consistent with approved upstream artifacts.

## Upstream dependency
Use the completed Stage 01 artifacts and the Stage 02 Process Map.

## Evidence to inspect
- `evidence/02_documents/fleet_operations_interview_notes.md`
- `evidence/01_enterprise_sources/source_inventory.csv`

## Case challenge
Identify the Lean wastes (TIMWOODS: Transport, Inventory, Motion, Waiting, Overproduction, Overprocessing, Defects, Skills) present in the current brownfield process.

## Minimum content
- Waste Category
- Process Step
- Description
- Impact (Cost/Time/Safety)
- Evidence

## Working scaffold

| Waste Category | Process Step | Description | Impact (Cost/Time/Safety) | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **Waiting** | Data Gathering & Reconciliation | Controllers wait for Port API updates (up to 60 mins) and manually reconcile conflicting versions. | High Time impact; delays commercial recovery decisions. | `source_inventory.csv` (SRC-PORT), `fleet_operations_interview_notes.md` |
| **Defects** | Recovery Formulation | Recovery plans formulated without late-arriving CMMS or Cargo constraints, leading to infeasible plans. | High Cost/Safety impact; requires re-planning mid-voyage. | `fleet_operations_interview_notes.md` ("plan can look commercially optimal but become infeasible") |
| **Motion / Transport** | Data Gathering | Controllers switch between 5+ disparate screens (AIS, WX, CMMS, Cargo, FMS) to build a single picture. | High Time/Effort impact; cognitive overload during high-stress disruptions. | `source_inventory.csv` (9 disparate sources) |
| **Skills (Underutilization)** | Post-Event Review | Master and Chief Engineer insights on *why* a recovery option succeeded or failed are not captured systematically. | High Long-term Cost impact; organization fails to learn from disruptions. | `fleet_operations_interview_notes.md` ("Post-event learning is weak") |
| **Overprocessing** | Semantic Reconciliation | Humans manually checking to see if "available" means the same thing in Port API as in signed notices. | High Time impact; purely deterministic work done by humans. | `fleet_operations_interview_notes.md` ("Port API fields use different meanings") |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Semantic reconciliation is overprocessing and a major waste of controller time. | `fleet_operations_interview_notes.md` | `process-value-stream-map.md` | High confidence (SME interview). |
| Formulating plans that are immediately infeasible due to late data is a defect. | `fleet_operations_interview_notes.md` | `process-value-stream-map.md` | High confidence (SME interview). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The cost of waiting for reconciliation translates directly to fuel waste or port demurrage fees. | Exact financial metrics for delays not provided in evidence. | FDE Team / Commercial Planner | Limits exact quantification of ROI in Stage 03. | Stage 03 Value Hypothesis / Baseline Dataset. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.
- [x] `NOT APPLICABLE`, if used, includes rationale, accountable approver and downstream consequence.

## Handoff
**Stage exit contribution:** Current-state process and architecture baseline

Do not advance to Stage 03 until the Stage 02 exit gate is defensible.