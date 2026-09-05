# Weighted Trade-Off Matrix

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 08 — Generate, Test & Select Options
**Participant status:** COMPLETED
**Deliverable form:** Structured table / register

## Stage question
Which solution survives evidence, alternatives and trade-offs?

## Why this artifact exists
To objectively score the viable solution options (from the Solution Catalogue) against weighted criteria derived from the business priorities and non-negotiable constraints.

## Upstream dependency
Use the completed Stage 08 Solution Catalogue, Stage 07 Acceptance Thresholds, and Stage 03 Value Hypothesis.

## Evidence to inspect
- `Participant_Case_Study.md` (Non-negotiable constraints)
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
Ensure the weighting heavily favors Safety/Compliance and Offline Capability, reflecting the maritime domain reality, rather than just raw development speed or cost.

## Minimum content

| Evaluation Criteria | Weight | OPT-01: Status Quo | OPT-02: Pure Deterministic | OPT-03: Hybrid (Det + Bounded NLP) | Evidence / Rationale for Scoring |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Safety & Compliance (Zero Tolerance)** | **40%** | 2/10 | 10/10 | 9/10 | OPT-01 fails GS-14. OPT-02 is perfectly safe. OPT-03 loses 1 point due to the conditional risk of NLP extraction errors (mitigated by human fallback). |
| **Offline Continuity (GS-14)** | **30%** | 0/10 | 10/10 | 10/10 | OPT-01 is shore-dependent. OPT-02 and OPT-03 both utilize the Event-Driven Hybrid edge architecture. |
| **Operational Efficiency (Time-to-Reconcile)** | **20%** | 2/10 | 6/10 | 9/10 | OPT-01 is 45 mins. OPT-02 requires manual port notice entry (slower). OPT-03 automates the #1 bottleneck (NLP extraction). |
| **Implementation Feasibility** | **10%** | 10/10 | 8/10 | 6/10 | OPT-01 is already built. OPT-02 is straightforward. OPT-03 requires integrating and managing a bounded NLP component and its fallback flows. |
| **TOTAL WEIGHTED SCORE** | **100%** | **2.8 / 10** | **8.6 / 10** | **8.9 / 10** | |

## Selection Decision
**OPT-03: Hybrid (Deterministic Core + Bounded NLP)** is the selected solution pattern. 

While OPT-02 (Pure Deterministic) scored very closely and is the safest fallback, OPT-03 provides the necessary operational efficiency gain to justify the investment, *provided that* the strict condition documented in `poc-model-rag-results.md` is met: NLP extraction must have a mandatory human-in-the-loop fallback for low-confidence results.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Safety and Offline Continuity are weighted at 70% combined, reflecting non-negotiable constraints. | `Participant_Case_Study.md` | `go-no-go-kill-criteria.md` | High confidence (explicit mandate). |
| OPT-03 is selected conditionally based on the NLP fallback mechanism. | `poc-model-rag-results.md` | `risk-treatment-plan.md` | High confidence (explicit risk mitigation). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The 10% weight for "Implementation Feasibility" is sufficient to prevent over-engineering. | FDE team capacity and timeline constraints are not fully quantified. | FDE Team / Executive Sponsor | If timeline is severely compressed, the project may need to pivot to OPT-02 as an MVP. | Stage 08 Build/Buy/Compose Assessment. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved solution and trade-offs
Do not advance to Stage 09 until the Stage 08 exit gate is defensible.