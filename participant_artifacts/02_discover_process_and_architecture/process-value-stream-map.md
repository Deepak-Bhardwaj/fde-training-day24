# Process / Value-Stream Map

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench

**Stage:** 02 — Discover Process & Architecture

**Participant status:** COMPLETED

**Deliverable form:** Structured analysis / specification

## Stage question
How does the real brownfield process and system operate today?

## Why this artifact exists
This artifact is part of the evidence needed to reach **Current-state process and architecture baseline**. It must be consistent with approved upstream artifacts; do not silently redefine earlier facts, semantics, thresholds or decision rights.

## Upstream dependency
Use the completed Stage 01 artifacts and explicitly referenced earlier artifacts.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
Map the exact steps, actors, and systems used today to handle a disruption, identifying wait times and rework.

## Minimum content
- Step
- Actor
- System
- Input/output
- Wait/rework
- Decision/handoff
- Evidence

## Working scaffold

| Step | Actor | System | Input/output | Wait/rework | Decision/handoff | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1. Disruption Detection | Fleet Controller | FMS / Port API | Alert of port congestion or weather event | Wait: Port API freshness is up to 60 mins. | Handoff: Controller to Shore Platform for investigation. | `source_inventory.csv` (SRC-PORT freshness threshold). |
| 2. Data Gathering | Fleet Controller | AIS, WX, CMMS, Cargo | Pulls data from 5+ disparate systems | Wait: Systems are not unified. Rework: Checking multiple screens. | Handoff: Controller begins manual reconciliation. | `fleet_operations_interview_notes.md` |
| 3. Semantic Reconciliation | Fleet Controller | Spreadsheets / Email | Attempts to resolve API "available" vs signed notice "confirmed". | Wait/Wait: High wait time due to manual checking. Rework: High risk of human error. | Decision: Determine which constraint is authoritative. | `fleet_operations_interview_notes.md` ("reconciling which version is current") |
| 4. Recovery Formulation | Fleet Controller / Planner | Ad-hoc analysis tools | Drafts a recovery plan (e.g., slow steaming, port skip). | Wait: Checking feasibility against late-arriving CMMS/Cargo constraints. | Handoff: Plan sent to Master for approval. | `fleet_operations_interview_notes.md` ("plan can look commercially optimal but become infeasible") |
| 5. Master Approval | Master | Vessel Systems / Comms | Reviews proposed plan against local reality. | Wait: Connectivity latency between shore and vessel. | Decision: Master approves or modifies plan. | `role_authorization_matrix.csv` |
| 6. Execution & Post-Event | Crew / Shore | Various logging systems | Vessel executes change; logs outcome. | Rework: Post-event learning is lost because rationale and outcomes aren't linked. | Handoff: Safety & Compliance for audit. | `fleet_operations_interview_notes.md` ("Post-event learning is weak") |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Semantic reconciliation between API and signed docs is a major bottleneck. | `fleet_operations_interview_notes.md` | `sipoc.md` | High confidence (SME interview). |
| Plans often look optimal commercially but fail on late-arriving technical/cargo constraints. | `fleet_operations_interview_notes.md` | `sipoc.md` | High confidence (SME interview). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: Current communication between vessel and shore relies on standard email/sat-com. | Specific comms protocols (e.g., NMEA, specific sat-com vendors) not detailed. | FDE Team | Limits exact definition of current state latency in C4 views. | Stage 02 Current-State C4 Views / Data Flows. |

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