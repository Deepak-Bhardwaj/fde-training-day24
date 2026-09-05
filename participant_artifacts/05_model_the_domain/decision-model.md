# Decision Model

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 05 — Model the Domain
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
What does the business actually mean, decide and own?

## Why this artifact exists
To map out the critical decisions made during a disruption, specifying who makes them, what information they require, and what the downstream consequences are.

## Upstream dependency
Use the completed Stage 04 Use-Case Card, Stage 05 Domain Capability Map, and Business Rules.

## Evidence to inspect
- `evidence/04_policy_authority/role_authorization_matrix.csv`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
Separate the *decision* from the *system*. The system provides information; humans (or deterministic rules) make the decisions.

## Minimum content

| Decision ID | Decision Name | Decision Maker | Required Information / Inputs | Constraints / Rules Applied | Downstream Consequence | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **D-01** | Reconcile Semantic Conflict | Deterministic Engine + Fleet Controller | Port API status, Signed Port Notice PDF, Source Authority weights. | BR-06 (Canonical Supremacy), `source_authority.yaml` precedence rules. | Unified, trusted constraint view is established. | `fleet_operations_interview_notes.md`, `source_authority.yaml` |
| **D-02** | Validate Plan Feasibility | Deterministic Constraint Engine | Proposed recovery option, Active CMMS holds, Cargo windows, Active Policies. | BR-02 (Technical Hold Absolute), BR-04 (Active Policy Exclusivity). | Plan is marked FEASIBLE or INFEASIBLE. Infeasible plans are discarded. | `source_inventory.csv`, `role_authorization_matrix.csv` |
| **D-03** | Select Recovery Option | Fleet Controller / Voyage Planner | List of FEASIBLE recovery options, ranked by commercial/safety score. | Must select an option that does not violate BR-01 or BR-02. | Selected option is prepared for Master approval. | `fleet_operations_interview_notes.md` |
| **D-04** | Approve Recovery Plan | Master (Vessel Commander) | Selected recovery option, rationale, source freshness data, current vessel state. | BR-01 (Master Veto Authority). AI output is strictly advisory (BR-03). | Plan is authorized for execution. Navigational changes are committed. | `role_authorization_matrix.csv` |
| **D-05** | Release Technical Hold | Chief Engineer | Maintenance completion report, safety verification. | Internal technical protocols. | CMMS hold is cleared. Voyage planning can now consider this vessel fully operational. | `role_authorization_matrix.csv` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| The Master is the sole decision-maker for final plan approval (D-04). | `role_authorization_matrix.csv` (MASTER approve_recovery_plan=YES) | `governance-raci.md` | High confidence (explicit policy). |
| Feasibility validation (D-02) must be deterministic, not AI-driven. | `non-ai-alternative.md`, `source_inventory.csv` | `ai-suitability-assessment.md` | High confidence (explicit design choice). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The Fleet Controller has the authority to pre-filter infeasible options before they reach the Master. | Exact delegation of pre-screening authority not explicitly detailed. | Fleet Controller / Safety Officer | If Controllers cannot pre-filter, the Master may be overwhelmed with infeasible options. | Stage 05 Ownership Map / Stage 11 Human Approval Matrix. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Domain and decision model
Do not advance to Stage 06 until the Stage 05 exit gate is defensible.