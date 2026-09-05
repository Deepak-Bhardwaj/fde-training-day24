# Critical-to-Quality Measures

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 03 — Frame Problem, Root Cause & Value
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
What evidence proves the problem, its causes and its value?

## Why this artifact exists
This artifact is part of the evidence needed to reach **Evidence-backed problem and measurable baseline**. It must be consistent with approved upstream artifacts.

## Upstream dependency
Use the completed Stage 01 Governance RACI and Stage 03 KPI Tree.

## Evidence to inspect
- `evidence/04_policy_authority/role_authorization_matrix.csv`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
Define the non-negotiable quality requirements (CTQs) that the future system must satisfy to be considered safe and compliant.

## Minimum content

| CTQ ID | CTQ Name | Requirement Definition | Measurement / Test Method | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **CTQ-01** | Authority Preservation | The system must NEVER auto-execute navigational commands or override the Master's authority. AI output is strictly non-authoritative. | Golden Scenario GS-08 (Unauthorized shore commit attempt), GS-02 (Master authority). | `role_authorization_matrix.csv`, `source_authority.yaml` |
| **CTQ-02** | Technical Hold Enforcement | Critical maintenance holds (CMMS) must act as absolute, hard feasibility constraints until authorized technical release by the Chief Engineer. | Golden Scenario GS-03 (Critical machinery hold). | `source_inventory.csv`, `role_authorization_matrix.csv` |
| **CTQ-03** | Temporal Idempotency | The system must handle duplicate/replayed events and clock drift idempotently without corrupting state. | Golden Scenario GS-07 (Duplicate event), GS-13 (Clock drift). | `live_event_stream.jsonl`, `source_inventory.csv` |
| **CTQ-04** | Offline Continuity | Vessel-side critical decision support must function without cloud/LLM connectivity. | Golden Scenario GS-10 (AI unavailable), GS-14 (Prolonged blackout). | `fleet_operations_interview_notes.md` |
| **CTQ-05** | Policy Version Integrity | The system must ONLY use ACTIVE policies for decision logic; superseded policies must be excluded from retrieval. | Golden Scenario GS-12 (Superseded policy trap). | `source_authority.yaml` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| AI output must be strictly non-authoritative. | `source_authority.yaml` (AI_OUTPUT precedence: NON_AUTHORITATIVE) | `governance-raci.md` | High confidence (explicit policy). |
| CMMS holds are absolute constraints. | `role_authorization_matrix.csv` (CHIEF_ENGINEER release_critical_maintenance_hold=YES) | `trust-boundaries.md` | High confidence (explicit policy). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The vessel edge can host the necessary deterministic logic for CTQ-04 without relying on remote LLMs. | Edge compute specs pending. | Shore Platform Team | Dictates the model routing and deployment topology in Stage 10. | Stage 10 AI & Application Architecture. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Evidence-backed problem and measurable baseline
Do not advance to Stage 04 until the Stage 03 exit gate is defensible.