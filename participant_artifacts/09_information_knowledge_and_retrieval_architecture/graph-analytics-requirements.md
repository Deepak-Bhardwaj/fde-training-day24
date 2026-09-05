# Graph Analytics Requirements

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer D: Graph Data Platform)
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To define the analytical queries required for post-event learning, fleet-wide trend analysis, and compliance auditing. These are distinct from the real-time operational traversals defined in the Query Patterns.

## Upstream dependency
Use the completed Stage 03 KPI Tree, Stage 07 Oversight/Transparency Requirements, and Stage 09 Graph Query Patterns.

## Evidence to inspect
- `evidence/02_documents/fleet_operations_interview_notes.md`
- `evidence/01_enterprise_sources/live_disruptions.csv`

## Case challenge
Analytics must run on the shore-side platform using read-replicas or batch exports. They must NEVER run on the vessel edge, as they would consume resources required for offline operational continuity.

## Minimum content

| Analytics Requirement | Description | Execution Environment | Frequency | Output / Action | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Disruption Root Cause Distribution** | Aggregate `[:ENCOUNTERS]` edges by `event_type` and `source_id` to identify which sources cause the most delays. | Shore Platform (Batch) | Weekly | Dashboard for Fleet Operations Director. | `fleet_operations_interview_notes.md` |
| **Constraint Expiration Audit** | Identify `Constraint` nodes that were marked `EXPIRED` but were still referenced in `RecoveryOption` generation (indicates temporal logic failure). | Shore Platform (Batch) | Daily | Alert to Safety Officer if count > 0. | `oversight-transparency-requirements.md` |
| **Recovery Option Success Rate** | Calculate the ratio of `RecoveryOption` nodes with `status = 'EXECUTED'` vs `'INFEASIBLE'` or `'REJECTED'`. | Shore Platform (Batch) | Monthly | Input for Stage 03 Value Hypothesis validation. | `kpi-tree.md` |
| **Policy Override Attempts** | Count instances where a lower-authority source attempted to overwrite a higher-authority `PolicyRule` (blocked by SC-01). | Shore Platform (Real-time Log) | Continuous | Security/Compliance alert. | `semantic-constraints.md` (SC-01) |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Post-event learning requires aggregating historical graph data that is too heavy for the vessel edge. | `fleet_operations_interview_notes.md` ("Post-event learning is weak") | `graph-persistence-architecture.md` | High confidence (SME interview). |
| Analytics must be isolated from the real-time operational graph to prevent resource contention. | `ctqs.md` (Offline Continuity) | `reference-architecture-comparison.md` | High confidence (architectural best practice). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The shore platform has a dedicated read-replica or data warehouse for analytics to avoid impacting the operational graph. | Infrastructure budget for read-replicas not confirmed. | Shore Platform Team | If no replica exists, analytics must run on a delayed batch export (T-1 data). | Stage 10 Physical Persistence Topology. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture