# Metric / Dimension Semantic Map

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer B: Semantic Foundation)
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To map the operational KPIs defined in Stage 03 to the specific semantic dimensions and data sources required to calculate them. This ensures the evaluation harness can accurately measure system performance.

## Upstream dependency
Use the completed Stage 03 KPI Tree and Stage 09 Canonical Entity Model.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/01_enterprise_sources/live_disruptions.csv`

## Case challenge
Ensure that every metric is traceable to a specific, measurable event or entity state transition in the canonical model. "Vibes" cannot be measured.

## Minimum content

| KPI (from Stage 03) | Semantic Dimension | Required Entity / Event State Transition | Data Source(s) | Calculation Logic | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Time-to-Reconcile** | Time / Latency | `DisruptionDetected` event to `ConstraintViewUpdated` event. | SRC-TELEM, SRC-PORT, SRC-CMMS | `ConstraintViewUpdated.observed_ts` - `DisruptionDetected.observed_ts`. | `kpi-tree.md`, `domain-events.md` |
| **Plan Feasibility Rate** | Constraint / Feasibility | `RecoveryOptionGenerated` to `PlanApproved` (or `Rejected`). | Deterministic Engine, Master | Count(`PlanApproved`) / Count(`RecoveryOptionGenerated` where `feasibility_score > 0`). | `kpi-tree.md`, `decision-model.md` |
| **Idempotency Success** | Data Quality / Integrity | `SourceDataIngested` to `Ignored_Duplicate` log. | SRC-TELEM, Ingestion ACL | Count(`Ignored_Duplicate`) / Count(`SourceDataIngested` from SRC-TELEM). | `kpi-tree.md`, `canonical-identifier-strategy.md` |
| **Offline Continuity Uptime** | Resilience / Connectivity | `ConnectivityLost` to `ConnectivityRestored` (with local `PlanApproved` in between). | Vessel Edge, Comms | Boolean: Did vessel edge successfully generate and log a plan without shore sync? | `kpi-tree.md`, `domain-events.md` |
| **Decision Trace Completeness** | Audit / Compliance | `PlanApproved` event payload completeness. | Audit Context | Count(`PlanApproved` with full `source_freshness` and `rationale` payload) / Count(`PlanApproved`). | `kpi-tree.md`, `oversight-transparency-requirements.md` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Time-to-reconcile is strictly defined by the delta between two specific domain events. | `domain-events.md` | `baseline-dataset.csv` | High confidence (architectural definition). |
| Idempotency can be measured by tracking the ingestion layer's duplicate rejection rate. | `canonical-identifier-strategy.md` | `quality-profile.md` | High confidence (deterministic logic). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The Audit Context can reliably capture the full `source_freshness` payload without truncation during low-bandwidth syncs. | Payload size limits for audit events not fully defined. | Shore Platform Team | If truncated, the Decision Trace Completeness metric will artificially fail. | Stage 10 API Contracts. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture
Do not advance to the next sub-layer until this artifact is defensible.