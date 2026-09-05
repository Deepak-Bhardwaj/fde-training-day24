# Go / No-Go / Kill Criteria

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 04 — Triage Regulation & Qualify Use Case
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
Should AI be used at all, and under what impact/regulatory constraints?

## Why this artifact exists
To establish the explicit, binary gates that determine whether the project proceeds to Stage 05 (Domain Modeling), requires a pivot, or is killed entirely.

## Upstream dependency
Use all completed Stage 04 artifacts.

## Evidence to inspect
- `START_HERE.md`
- `evidence/04_policy_authority/role_authorization_matrix.csv`

## Case challenge
Define criteria that are measurable and enforceable. "Vibes" are not acceptable.

## Minimum content

| Criterion ID | Criterion Description | Type | Threshold / Condition | Consequence of Failure | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **G-01** | **Authority Preservation:** The system design must explicitly preserve the Master's absolute authority over navigational and safety-critical decisions. | **GO** | 100% of safety-critical actions require explicit human approval. AI output precedence is NON_AUTHORITATIVE. | **KILL:** If the design requires or implies autonomous execution. | `role_authorization_matrix.csv`, `prohibited-use-check.md` |
| **G-02** | **Offline Continuity:** The vessel-side workbench must be capable of supporting critical decision-making without cloud/LLM connectivity. | **GO** | Vessel edge can run the deterministic constraint engine and access cached canonical data during a simulated 4-hour blackout (GS-14). | **PIVOT:** If edge compute is insufficient, scope reduces to shore-side advisory only, lowering value. | `ctqs.md`, `fleet_operations_interview_notes.md` |
| **G-03** | **Technical Hold Enforcement:** Critical CMMS maintenance holds must act as absolute, un-bypassable feasibility constraints. | **GO** | 100% of generated recovery options respect active CMMS holds. No workaround or "override" capability exists for the AI/Controller. | **KILL:** If the system allows bypassing technical holds. | `source_authority.yaml`, `ctqs.md` |
| **G-04** | **Temporal Provenance:** The system must handle duplicate events and clock drift idempotently. | **GO** | System successfully processes the GS-07 (Duplicate event) and GS-13 (Clock drift) scenarios without state corruption. | **PIVOT:** If provenance cannot be enforced, data quality risks may invalidate the use case. | `source_inventory.csv`, `live_event_stream.jsonl` |
| **G-05** | **Value Realization Potential:** The projected improvement in reconciliation time and plan feasibility must be significant. | **GO** | Baseline metrics show >50% potential improvement in time-to-reconcile, and >15% improvement in feasibility. | **NO-GO:** If the bottleneck is purely human process and not data/system fragmentation, the workbench may not deliver ROI. | `baseline-dataset.csv`, `value-risk-feasibility-matrix.md` |

## Overall Stage 04 Decision
**GO.** 
The use case passes all critical Go criteria. The strict adherence to human authority, offline continuity, and deterministic core logic mitigates the inherent safety risks of the maritime domain. The project will proceed to Stage 05: Model the Domain.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| The use case is approved to proceed to domain modeling. | All Stage 04 artifacts | `use-case-card.md` | High confidence (explicit gate review). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The "GO" decision for offline continuity (G-02) will be technically validated in Stage 10. | Edge hardware specs pending. | Shore Platform Team | If G-02 fails in Stage 10, the project must pivot to a reduced scope. | Stage 10 Deployment Topology. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved and justified use case
Do not advance to Stage 05 until the Stage 04 exit gate is defensible.