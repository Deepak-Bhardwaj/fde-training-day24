# Governance RACI

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench

**Stage:** 01 — Mandate & Field Immersion

**Participant status:** COMPLETED

**Deliverable form:** Structured narrative + evidence table

## Stage question
Why are we here, what outcome matters, who owns it, and who is affected?

## Why this artifact exists
This artifact is part of the evidence needed to reach **Approved mandate and operating context**. It must be consistent with approved upstream artifacts; do not silently redefine earlier facts, semantics, thresholds or decision rights.

## Upstream dependency
Use the case pack and supplied evidence. No solution architecture is an input to Stage 01.

## Evidence to inspect
- `evidence/04_policy_authority/role_authorization_matrix.csv`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
Stay in the field problem and ownership space. Do not propose a model, graph database, agent or UI in this artifact.

## Minimum content

| Activity / Decision | Master | Chief Engineer | Fleet Controller | Safety Officer | Commercial Planner | AI Agent |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Define Training Mandate & Scope** | I | I | C | **A** | I | I |
| **Approve Recovery Plan** | **A** | C | C (Coordination) | C (Escalation) | I | I |
| **Authorize Navigation Change** | **A** | I | I | I | I | I |
| **Release Critical Maintenance Hold** | I | **A** | I | I | I | I |
| **Commit Operational Action** | A (Ship Proc) | A (Tech Only) | A (Non-Nav) | I | I | **NO** |
| **Request AI Assistance** | R | R | R | R | R | N/A |
| **View Operational Context** | R | R | R | R | R (Limited) | R (Filtered) |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Master holds absolute authority over navigation and recovery approval. | `role_authorization_matrix.csv` (MASTER: approve_recovery_plan=YES, authorize_navigation_change=YES) | `engagement-charter.md`, `scope.md` | High confidence (explicit policy). |
| Chief Engineer holds absolute authority over critical maintenance holds. | `role_authorization_matrix.csv` (CHIEF_ENGINEER: release_critical_maintenance_hold=YES) | `engagement-charter.md` | High confidence (explicit policy). |
| AI Agent has zero authority to commit operational actions or approve plans. | `role_authorization_matrix.csv` (AI_AGENT: commit_operational_action=NO, approve_recovery_plan=NO) & `source_authority.yaml` (AI_OUTPUT precedence: NON_AUTHORITATIVE) | `scope.md` | High confidence (explicit policy). |
| Fleet Controller authority is limited to non-navigation coordination. | `role_authorization_matrix.csv` (FLEET_CONTROLLER: commit_operational_action=NON_NAVIGATION