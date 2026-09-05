# Counter-Metrics

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 03 — Frame Problem, Root Cause & Value
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
What evidence proves the problem, its causes and its value?

## Why this artifact exists
This artifact is part of the evidence needed to reach **Evidence-backed problem and measurable baseline**. It must be consistent with approved upstream artifacts.

## Upstream dependency
Use the completed Stage 03 KPI Tree and Critical-to-Quality Measures.

## Evidence to inspect
- `evidence/04_policy_authority/role_authorization_matrix.csv`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
Define counter-metrics to ensure that optimizing for the primary KPIs (speed, feasibility) does not inadvertently violate safety, authority, or compliance constraints.

## Minimum content

| Primary KPI Optimized | Counter-Metric Name | Definition | Target / Threshold | Rationale | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Time-to-Reconcile | **Unauthorized Automated Actions** | Number of recovery options or navigational changes executed without explicit Master approval. | MUST BE 0 | Optimizing for speed must never bypass human authority. | `role_authorization_matrix.csv` |
| Plan Feasibility Rate | **False Positive Constraint Blocks** | Number of times the system incorrectly blocks a commercially optimal plan due to stale or misinterpreted CMMS/Cargo data. | < 2% | Over-indexing on feasibility might lead to overly conservative, commercially damaging plans. | `source_inventory.csv` |
| Offline Continuity | **Stale Data Execution Rate** | Number of decisions made on vessel using data that exceeds the source freshness threshold (e.g., >90 min old weather). | < 5% | Ensuring offline capability must not result in acting on dangerously stale information. | `source_inventory.csv` |
| Post-Event Audit Rate | **Decision Trace Completeness** | Percentage of executed recovery plans that have a fully linked, reconstructable trace (rationale + source freshness + outcome). | 100% | Speed of execution must not compromise auditability and post-event learning. | `fleet_operations_interview_notes.md` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| AI must never execute unauthorized actions, regardless of speed optimizations. | `role_authorization_matrix.csv` (AI_AGENT commit=NO) | `ctqs.md` | High confidence (explicit policy). |
| Acting on stale data during offline operations is a critical safety risk. | `source_inventory.csv` (freshness thresholds) | `brownfield-assessment.md` | High confidence (explicit source metadata). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The system can accurately detect and flag "stale data" in real-time without excessive false positives. | Exact clock-drift tolerance thresholds not fully defined. | FDE Team | May require dynamic freshness thresholds based on source health. | Stage 09 Context Freshness Policy. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Evidence-backed problem and measurable baseline
Do not advance to Stage 04 until the Stage 03 exit gate is defensible.