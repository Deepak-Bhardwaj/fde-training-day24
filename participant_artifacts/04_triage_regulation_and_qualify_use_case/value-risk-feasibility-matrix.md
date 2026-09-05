# Value-Risk-Feasibility Matrix

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 04 — Triage Regulation & Qualify Use Case
**Participant status:** COMPLETED
**Deliverable form:** Structured table / register

## Stage question
Should AI be used at all, and under what impact/regulatory constraints?

## Why this artifact exists
To objectively score the approved use case across three critical dimensions to ensure the investment of engineering effort is justified and safe.

## Upstream dependency
Use the completed Stage 03 Value Hypothesis and Stage 04 Impact/Regulatory Screen.

## Evidence to inspect
- `evidence/01_enterprise_sources/live_disruptions.csv`
- `evidence/04_policy_authority/role_authorization_matrix.csv`

## Case challenge
Provide a realistic assessment. Do not inflate value or underestimate risk.

## Minimum content

| Dimension | Score (1-5) | Justification | Key Mitigations / Dependencies | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **Value** | **4** (High) | Reduces reconciliation time by ~78% (45m to <10m). Prevents costly infeasible plans (improves feasibility from 78% to >95%). Directly addresses the #1 pain point identified by Fleet Controllers. | Value realization depends on the deterministic engine accurately reflecting real-world constraints. | `baseline-dataset.csv`, `fleet_operations_interview_notes.md` |
| **Risk** | **3** (Medium-High) | The domain is safety-critical (maritime navigation). Incorrect recovery options could lead to safety incidents or commercial loss. However, risk is heavily mitigated by the strict non-authoritative, human-in-the-loop design. | 1. Master holds absolute veto. 2. AI is non-authoritative. 3. CMMS holds are hard constraints. 4. System fails safe (defaults to manual) if confidence is low. | `role_authorization_matrix.csv`, `ctqs.md` |
| **Feasibility** | **3** (Medium) | Data sources exist, but integrating them with strict temporal provenance and offline-first vessel-side capability is technically complex. Requires significant edge-compute architecture and robust sync logic. | 1. Vessel edge compute specs must be validated. 2. Clock drift reconciliation logic must be proven. 3. Sat-com bandwidth limits must be respected. | `brownfield-assessment.md`, `dependencies.md` |

## Overall Assessment
**PROCEED WITH CAUTION.** 
The use case delivers high operational value and addresses a critical bottleneck. The safety risks are inherent to the maritime domain but are effectively bounded by the strict governance and non-authoritative design. The primary challenge is technical feasibility, specifically the offline-first architecture and temporal provenance. 

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| The use case addresses the primary operational bottleneck (reconciliation time). | `fleet_operations_interview_notes.md` | `value-hypothesis.md` | High confidence (SME interview). |
| Technical feasibility is the primary risk to delivery, not regulatory blockers. | `dependencies.md`, `brownfield-assessment.md` | `impact-regulatory-screen.md` | High confidence (architecture assessment). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The technical feasibility of the offline-first edge architecture can be proven in Stage 10. | Edge hardware constraints not yet fully profiled. | Shore Platform Team | If infeasible, the use case scope may need to be reduced to shore-side only, lowering the overall value. | Stage 10 Deployment Topology. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved and justified use case
Do not advance to Stage 05 until the Stage 04 exit gate is defensible.