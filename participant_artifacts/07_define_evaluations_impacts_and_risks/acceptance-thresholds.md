# Acceptance Thresholds

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 07 — Define Evaluations, Impacts & Risks
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
What must the future system prove before it is acceptable?

## Why this artifact exists
To define the strict, quantitative, and qualitative boundaries that determine whether the system passes or fails its evaluation. These are the "Go/No-Go" metrics for deployment.

## Upstream dependency
Use the completed Stage 03 KPI Tree, Stage 04 Go/No-Go Criteria, and Stage 07 Evaluation Scenarios.

## Evidence to inspect
- `evidence/04_policy_authority/role_authorization_matrix.csv`
- `evidence/01_enterprise_sources/source_inventory.csv`

## Case challenge
Set thresholds that are ambitious but grounded in the baseline data. Safety thresholds must be absolute (100% or 0%), while efficiency thresholds can have tolerance ranges.

## Minimum content

| Metric / Criterion | Baseline (Current State) | Acceptance Threshold (Future State) | Rationale / Evidence |
| :--- | :--- | :--- | :--- |
| **Safety: Unauthorized Executions** | N/A (Manual process) | **0%** (Absolute) | Any unauthorized execution violates Master's authority (BR-01). Zero tolerance. | `role_authorization_matrix.csv`, `go-no-go-kill-criteria.md` |
| **Safety: Technical Hold Violations** | ~5% (Estimated human error) | **0%** (Absolute) | Critical maintenance holds are hard feasibility constraints (BR-02). Zero tolerance. | `source_inventory.csv`, `go-no-go-kill-criteria.md` |
| **Efficiency: Time-to-Reconcile** | 45 minutes | **< 10 minutes** | Addresses the primary bottleneck identified by Fleet Controllers. | `baseline-dataset.csv` (M-01), `fleet_operations_interview_notes.md` |
| **Efficiency: Plan Feasibility Rate** | 78% | **> 95%** | Ensures late-arriving constraints (CMMS/Cargo) are integrated before plan presentation. | `baseline-dataset.csv` (M-02), `value-hypothesis.md` |
| **Resilience: Idempotency Success** | ~92% (8% duplicate rate) | **100%** | System must handle all duplicate/clock-drifted events without state corruption (BR-05). | `live_event_stream.jsonl`, `quality-profile.md` |
| **Resilience: Offline Functionality** | 0% (Shore-dependent) | **100% of Critical Functions** | Vessel edge must support disruption management during simulated 4-hour blackout (GS-14). | `fleet_operations_interview_notes.md`, `ctqs.md` |
| **Compliance: Decision Trace Completeness** | 40% | **100%** | Every executed plan must have a linked rationale, source freshness, and outcome for audit. | `fleet_operations_interview_notes.md`, `provenance-baseline.md` |
| **AI/NLP: Extraction Precision (if used)** | N/A | **> 90%** | If NLP is used for port notices, it must be highly accurate; low-confidence extractions must fallback to human review. | `data-gap-register.md` (DG-03) |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Safety metrics (unauthorized executions, hold violations) must be absolute zero. | `role_authorization_matrix.csv`, `source_inventory.csv` | `go-no-go-kill-criteria.md` | High confidence (explicit non-negotiable constraints). |
| Efficiency targets are derived directly from the Stage 03 baseline dataset. | `baseline-dataset.csv` | `value-hypothesis.md` | High confidence (empirical baseline). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The < 10 minute reconciliation target is achievable with the proposed deterministic engine architecture. | Exact processing latency of the constraint engine not yet benchmarked. | FDE Team / Shore Platform | If the engine is too slow, the threshold may need adjustment or architecture optimization. | Stage 08 PoC / Model / RAG Results (Performance benchmarking). |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Evaluation, impact and risk requirements
Do not advance to Stage 08 until the Stage 07 exit gate is defensible.