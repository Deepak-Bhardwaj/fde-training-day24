# Impact / Regulatory Screen

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 04 — Triage Regulation & Qualify Use Case
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
Should AI be used at all, and under what impact/regulatory constraints?

## Why this artifact exists
To ensure the proposed use case complies with maritime regulations, data privacy laws, and internal fleet policies before any technical design begins.

## Upstream dependency
Use the completed Stage 01 Governance RACI, Stage 03 Critical-to-Quality Measures, and Case Study constraints.

## Evidence to inspect
- `evidence/04_policy_authority/role_authorization_matrix.csv`
- `evidence/04_policy_authority/source_authority.yaml`
- `evidence/01_enterprise_sources/source_inventory.csv`

## Case challenge
Identify all regulatory, safety, and compliance impacts of the workbench. Do not propose technical mitigations yet; simply screen and categorize the risks.

## Minimum content

| Regulatory / Policy Domain | Potential Impact of Workbench | Severity (H/M/L) | Mitigation Strategy (High-Level) | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **Maritime Safety (SOLAS / Master's Authority)** | Risk of AI suggesting or executing unauthorized navigational changes during disruptions. | **HIGH** | Strict human-in-the-loop. AI output is explicitly marked as NON_AUTHORITATIVE. Master holds absolute veto. | `role_authorization_matrix.csv`, `source_authority.yaml` |
| **Data Privacy (GDPR / Maritime Labor)** | Crew system data (rest hours, personal info) could be exposed or misused by automated systems. | **HIGH** | Strict purpose-filtered access. AI is prohibited from making personnel/employment decisions. Data minimization applied. | `source_inventory.csv` (SRC-CREW) |
| **Commercial Confidentiality** | Cargo priorities and customer data could leak across tenant boundaries during recovery planning. | **MEDIUM** | Role-based access control (RBAC) and strict tenant isolation at the retrieval layer. | `source_inventory.csv` (SRC-CARGO) |
| **Audit & Compliance (ISM Code)** | Post-event learning is currently weak; new system must ensure reconstructable decision traces for safety audits. | **MEDIUM** | System must log rationale, source freshness, and outcomes for every generated recovery option. | `fleet_operations_interview_notes.md` |
| **Environmental (MARPOL)** | Suboptimal recovery options could lead to increased fuel consumption or emissions. | **LOW** | Workbench must include fuel/emission constraints in the feasibility check of recovery options. | `source_inventory.csv` (SRC-TELEM) |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| AI is strictly prohibited from making personnel decisions. | `source_inventory.csv` (SRC-CREW: not authoritative for AI employment) | `ctqs.md` | High confidence (explicit policy). |
| Master holds absolute authority; AI cannot override. | `role_authorization_matrix.csv` (MASTER authorize_navigation_change=YES, AI_AGENT=NO) | `trust-boundaries.md` | High confidence (explicit policy). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: Current RBAC for Crew/Cargo data is sufficient for the new workbench. | Exact RBAC implementation details pending. | Marine HR / Cargo Ops | May require custom data masking at the retrieval layer in Stage 09. | Stage 09 Permissible-Use / Access Matrix. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved and justified use case
Do not advance to Stage 05 until the Stage 04 exit gate is defensible.