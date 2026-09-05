# SIPOC

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench

**Stage:** 02 — Discover Process & Architecture

**Participant status:** COMPLETED

**Deliverable form:** Structured narrative + evidence table

## Stage question
How does the real brownfield process and system operate today?

## Why this artifact exists
This artifact is part of the evidence needed to reach **Current-state process and architecture baseline**. It must be consistent with approved upstream artifacts; do not silently redefine earlier facts, semantics, thresholds or decision rights.

## Upstream dependency
Use the completed Stage 01 artifacts and explicitly referenced earlier artifacts. Never copy them into this file simply to satisfy a checklist.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/01_enterprise_sources/live_disruptions.csv`
- `evidence/01_enterprise_sources/live_event_stream.jsonl`
- `evidence/01_enterprise_sources/source_health_events.jsonl`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
Reconstruct the actual current workflow and brownfield system from evidence; distinguish what the organization does today from what you wish it did.

## Minimum content
- Supplier
- Input
- Process step
- Output
- Customer/affected party
- Evidence

## Relevant non-negotiable constraints
- AI cannot issue or execute navigational commands or replace the Master's command authority.
- Critical maintenance holds are hard feasibility constraints until authorized technical release.

## Working scaffold

| Supplier | Input | Process step | Output | Customer/affected party | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| External Providers (WX, Port) | Weather forecasts, Port API status, signed notices | 1. Monitor external environment for disruptions | Alert/Flag of potential delay or constraint | Fleet Controller / Voyage Planner | `fleet_operations_interview_notes.md` ("slowest part is reconciling which version is current") |
| Vessel Telemetry / CMMS | Machinery signals, maintenance status | 2. Monitor internal vessel health | Identification of critical machinery holds or constraints | Chief Engineer / Fleet Controller | `source_inventory.csv` (SRC-TELEM, SRC-CMMS known issues: clock drift, asset mapping) |
| Fleet Controller | Disruption alerts, conflicting data snapshots | 3. Reconcile data versions and authority | "True" picture of current constraints (often delayed/manual) | Master / Commercial Ops | `fleet_operations_interview_notes.md` ("vessel and shore teams can each be correct relative to different clocks") |
| Shore Ops / AI tools (current state) | Reconciled constraints, schedule data | 4. Generate / Propose Recovery Options | List of potential routing or schedule adjustments | Master / Commercial Planner | `fleet_operations_interview_notes.md` ("plan can look commercially optimal but become infeasible...") |
| Master | Proposed recovery options | 5. Approve and execute recovery action | Navigational or schedule change | Port Ops / Cargo Ops / Crew | `role_authorization_matrix.csv` (MASTER approve_recovery_plan=YES) |
| Vessel / Shore Systems | Execution logs, outcome data | 6. Post-event review | Incident report / lessons learned (currently weak) | Safety & Compliance / Shore Platform | `fleet_operations_interview_notes.md` ("Post-event learning is weak because rationale... are not linked consistently") |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Reconciling data is currently a manual, slow step for controllers. | `fleet_operations_interview_notes.md` | `engagement-charter.md` | High confidence (SME interview). |
| Current post-event review is weak because rationale and outcomes are not linked. | `fleet_operations_interview_notes.md` | `outcome-statement.md` | High confidence (SME interview). |
| Port API semantics conflict with signed notices, causing manual reconciliation. | `fleet_operations_interview_notes.md` & `source_inventory.csv` | `scope.md` | High confidence (explicit known issue). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: Controllers currently use spreadsheets or ad-hoc chat to reconcile data. | Exact current UI/tools not specified in interview notes. | FLEET_CONTROLLER | Impacts the UI/UX baseline for Stage 02 process mapping. | Stage 02 System Landscape / C4 Views. |

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