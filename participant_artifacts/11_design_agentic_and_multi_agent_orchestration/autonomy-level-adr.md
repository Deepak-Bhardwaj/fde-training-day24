# Autonomy-Level ADR

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 11 — Agentic & Multi-Agent Orchestration
**Participant status:** COMPLETED
**Deliverable form:** ADR / decision record

## Stage question
Is autonomy justified, bounded, permissioned, interruptible and testable?

## Why this artifact exists
To formally record the decision regarding the level of autonomy permitted in the system, ensuring it aligns with maritime safety regulations and the project's non-negotiable constraints.

## Upstream dependency
Use the completed Stage 11 Agent Suitability Assessment and Stage 05 Business Rules.

## Evidence to inspect
- `evidence/04_policy_authority/role_authorization_matrix.csv`
- `Participant_Case_Study.md` (Non-negotiable constraints)

## Case challenge
Define autonomy using a recognized framework (e.g., SAE Levels 0-5 adapted for maritime decision support) and explicitly reject levels that violate safety constraints.

## Minimum content

### ADR-019: Restriction to Level 1 (Decision Support) / Level 2 (Human-in-the-Loop Automation)
- **Status:** Accepted
- **Context:** The workbench must assist Fleet Controllers and Masters in resolving disruptions. However, the maritime domain demands absolute accountability, explainability, and human authority (Master's Veto). Autonomous agents (Level 3+) introduce probabilistic behavior and hallucination risks that are unacceptable for safety-critical feasibility checking or execution.
- **Options Considered:**
  1. **Level 3+ (Conditional/High Automation):** Agents autonomously generate, evaluate, and execute recovery options. *Rejected:* Violates BR-01 (Master Veto) and BR-02 (Technical Hold Absolute). Fails GS-08 (Unauthorized shore commit).
  2. **Level 2 (Human-in-the-Loop Automation):** System generates options and pre-fills forms, but requires explicit human approval for every state transition. *Accepted for Shore UI.*
  3. **Level 1 (Decision Support):** System provides ranked, evidence-backed options and highlights constraints. Human makes all selections and approvals. *Accepted as the primary operational mode, especially for the Vessel Edge.*
- **Decision:** The system will operate strictly at **Level 1 (Decision Support)** for the Vessel Edge and **Level 2 (Human-in-the-Loop Automation)** for the Shore Platform. **No autonomous execution (Level 3+) is permitted under any circumstance.**
- **Consequences:** 
  - (+) Guarantees 100% compliance with Master's authority and safety regulations.
  - (+) Ensures all decisions are fully explainable and auditable.
  - (-) Requires more manual clicks from the Fleet Controller/Master compared to a fully autonomous system (an acceptable trade-off for safety).

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Level 3+ autonomy is explicitly prohibited due to Master's absolute authority. | `role_authorization_matrix.csv` | `agent-suitability-assessment.md` | High confidence (explicit policy). |
| Level 1/2 ensures the system remains interruptible and testable. | `Participant_Case_Study.md` | `go-no-go-kill-criteria.md` | High confidence (explicit mandate). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: Fleet Controllers will not experience "automation bias" and blindly approve Level 2 pre-filled options without reviewing the evidence. | Human factors testing NOT RUN. | FDE Team / Safety Officer | UI must be designed to force active review (e.g., requiring the Controller to check a box confirming they reviewed the constraint evidence). | Stage 11 Human Approval / Override Escalation Matrix. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved, bounded and testable agentic architecture