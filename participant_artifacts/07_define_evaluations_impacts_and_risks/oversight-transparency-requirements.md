# Oversight / Transparency Requirements

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 07 — Define Evaluations, Impacts & Risks
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
What must the future system prove before it is acceptable?

## Why this artifact exists
To define the exact transparency, explainability, and auditability requirements that allow human operators (Master, Controller, Safety Officer) to effectively oversee, trust, and audit the system's recommendations and actions.

## Upstream dependency
Use the completed Stage 03 Value Hypothesis, Stage 05 Decision Model, and Stage 07 Risk Treatment Plan.

## Evidence to inspect
- `evidence/02_documents/fleet_operations_interview_notes.md`
- `evidence/04_policy_authority/role_authorization_matrix.csv`

## Case challenge
Transparency is not just about logging; it's about presenting the *right* information to the *right* human at the *right* time to enable informed decision-making. Avoid black-box AI outputs.

## Minimum content

| Requirement ID | Stakeholder | Transparency / Oversight Requirement | Implementation Mechanism | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **OT-01** | **Fleet Controller** | **Constraint Explainability:** Must see exactly *why* a recovery option is feasible or infeasible, including the specific source and freshness of every constraint applied. | UI displays a "Constraint Evidence Card" for each option, linking to SourceID, ObservedTimestamp, and Authority Weight. | `fleet_operations_interview_notes.md` ("rationale, source freshness... not linked") |
| **OT-02** | **Master** | **Actionable Clarity:** Must clearly distinguish between system drafts/AI recommendations and actionable, approved plans. | UI explicitly labels AI/NLP outputs as "DRAFT / NON-AUTHORITATIVE". Execution buttons are only enabled after explicit Master approval flow. | `source_authority.yaml`, `role_authorization_matrix.csv` |
| **OT-03** | **Safety Officer / Audit** | **Reconstructable Decision Traces:** Must be able to replay any historical disruption event and see the exact system state, data freshness, and human approvals at the time of decision. | Compliance & Audit Context stores immutable domain events (PlanApproved, HoldReleased) with full payload and temporal provenance. | `fleet_operations_interview_notes.md`, `provenance-baseline.md` |
| **OT-04** | **Chief Engineer** | **Hold Visibility:** Must have absolute visibility into how the system is interpreting and enforcing CMMS maintenance holds. | Dedicated "Technical Holds" dashboard showing active holds, mapped asset IDs, and any feasibility blocks triggered by those holds. | `source_inventory.csv` (SRC-CMMS) |
| **OT-05** | **All Operators** | **System Health & Data Degradation:** Must be immediately alerted if the system is operating on stale data, disconnected from shore, or experiencing source outages. | Prominent UI banner indicating "OFFLINE MODE", "STALE DATA (Source X)", or "SOURCE OUTAGE (WX)". | `source_health_events.jsonl`, `dependencies.md` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Controllers require explicit linkage between rationale, source freshness, and outcomes to trust the system. | `fleet_operations_interview_notes.md` | `value-hypothesis.md` | High confidence (SME interview). |
| AI outputs must be visually and programmatically distinguished from authoritative data. | `source_authority.yaml` | `ai-impact-assessment.md` | High confidence (explicit policy). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The "Constraint Evidence Card" UI element can be rendered efficiently on the vessel-side low-bandwidth UI. | Vessel UI bandwidth and rendering capabilities not fully defined. | Shore Platform Team | May require simplified text-based transparency on the vessel, with full UI on shore. | Stage 10 Deployment Topology / Target C4 Views. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Evaluation, impact and risk requirements
Do not advance to Stage 08 until the Stage 07 exit gate is defensible.