# Permissible-Use / Access Matrix

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 06 — Qualify Data & Knowledge
**Participant status:** COMPLETED
**Deliverable form:** Structured table / register

## Stage question
Is the evidence trustworthy, permissible, traceable, representative and ready?

## Why this artifact exists
To explicitly define who (or what system) can access which data, for what specific purpose, and under what restrictions. This is critical for enforcing data privacy (Crew), commercial confidentiality (Cargo), and preventing AI overreach.

## Upstream dependency
Use the completed Stage 01 Governance RACI, Stage 04 Impact/Regulatory Screen, and Stage 06 Data/Knowledge Inventory.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/04_policy_authority/role_authorization_matrix.csv`

## Case challenge
Ensure that access boundaries are strictly enforced at the retrieval layer. AI and automated systems must never have broader access than their explicitly defined purpose.

## Minimum content

| Role / System Actor | SRC-CREW (Crew Data) | SRC-CARGO (Cargo Data) | SRC-CMMS (Maintenance) | SRC-POLICY (Rules) | SRC-TELEM / AIS (Telemetry) | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Master** | LIMITED (Rest hours only) | YES (Voyage context) | YES (Vessel status) | YES (Active only) | YES | `role_authorization_matrix.csv` |
| **Chief Engineer** | NO | LIMITED (Hazmat only) | YES (Full) | YES (Active only) | YES (Machinery only) | `role_authorization_matrix.csv` |
| **Fleet Controller** | LIMITED (Rest constraints) | YES (Schedule context) | YES (Hold status) | YES (Active only) | YES | `role_authorization_matrix.csv` |
| **Safety Officer** | MINIMIZED (Audit only) | LIMITED (Incident only) | YES (Audit) | YES (All versions) | YES (Audit) | `role_authorization_matrix.csv` |
| **AI Agent / NLP Tool** | NO (Strictly Prohibited) | PURPOSE_FILTERED (Feasibility only) | PURPOSE_FILTERED (Constraint check) | YES_ACTIVE_ONLY | PURPOSE_FILTERED | `source_inventory.csv`, `source_authority.yaml` |
| **Audit System** | MINIMIZED (Hash/Log only) | MINIMIZED (Hash/Log only) | YES (Immutable log) | YES (Archive) | YES (Immutable log) | `fleet_operations_interview_notes.md` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| AI is strictly prohibited from accessing Crew data for any reason. | `source_inventory.csv` (SRC-CREW: not authoritative for AI employment, retrieval_use=MINIMIZED) | `impact-regulatory-screen.md` | High confidence (explicit policy). |
| Cargo data access for AI must be strictly purpose-filtered to feasibility checking. | `source_inventory.csv` (SRC-CARGO: retrieval_use=YES_WITH_PURPOSE) | `trust-boundaries.md` | High confidence (explicit policy). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The retrieval layer can dynamically apply these purpose-filters based on the calling system's identity token. | Exact IAM/RBAC implementation for the retrieval layer not yet detailed. | Shore Platform Team | Requires strict API gateway enforcement in Stage 10. | Stage 10 API Contracts / Identity / Permission Matrix. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Data and knowledge readiness assessment
Do not advance to Stage 07 until the Stage 06 exit gate is defensible.