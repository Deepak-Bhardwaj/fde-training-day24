# Agent Responsibility Map

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 11 — Agentic & Multi-Agent Orchestration
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
Is autonomy justified, bounded, permissioned, interruptible and testable?

## Why this artifact exists
To explicitly define what responsibilities, if any, are assigned to automated or "agentic" components, and to explicitly list the responsibilities that are strictly reserved for human actors or deterministic code.

## Upstream dependency
Use the completed Stage 11 Autonomy-Level ADR and Stage 05 Decision Model.

## Evidence to inspect
- `evidence/04_policy_authority/role_authorization_matrix.csv`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
Prevent "responsibility creep" where an AI component is implicitly expected to handle tasks it was not designed or permitted to handle.

## Minimum content

| Responsibility / Task | Assigned To | Rationale / Constraint | Evidence |
| :--- | :--- | :--- | :--- |
| **Feasibility Checking** | **Deterministic Engine** (NOT an Agent) | Requires 100% explainable, binary logic. Probabilistic agent reasoning is unacceptable. | `business-rules.md` (BR-02) |
| **Recovery Option Generation** | **Deterministic Engine** (NOT an Agent) | Must strictly adhere to active constraints and policy rules without hallucination. | `non-ai-alternative.md` |
| **Final Plan Approval** | **Master** (Human) | Absolute, non-delegable authority. | `role_authorization_matrix.csv` |
| **Technical Hold Release** | **Chief Engineer** (Human) | Absolute, non-delegable authority. | `role_authorization_matrix.csv` |
| **Port Notice Data Extraction** | **Bounded NLP Service** (Not Agentic) | Deterministic API call with strict schema validation and confidence gating. Not an autonomous agent. | `knowledge-extraction-specification.md` |
| **Post-Event Audit Report Drafting** | **Bounded Assistant (Shore Only)** | Low-risk, administrative task. Output is strictly marked `DRAFT` and requires Safety Officer review before saving. | `agent-suitability-assessment.md` |
| **Real-time Telemetry Monitoring** | **Deterministic Rules Engine** (NOT an Agent) | Requires deterministic threshold checking, not probabilistic pattern recognition. | `source_inventory.csv` |

## Explicit "NOT APPLICABLE" Declaration
Per the Participant Runbook: *"the correct engineering decision may be to use no agent or no multi-agent system."* 

**Multi-Agent Orchestration is explicitly NOT APPLICABLE to the core operational workflow.** The complexity, unpredictability, and lack of determinism in multi-agent frameworks (e.g., AutoGen, CrewAI) directly violate the non-negotiable constraints of this maritime case study (GS-02, GS-03, GS-08). The system relies on a **Deterministic Workflow Orchestrator**, not agents.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Multi-agent orchestration is NOT APPLICABLE to the core workflow. | `Participant_Runbook.md` | `agent-suitability-assessment.md` | High confidence (explicit training mandate). |
| Final plan approval is exclusively the Master's responsibility. | `role_authorization_matrix.csv` | `decision-model.md` | High confidence (explicit policy). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: Stakeholders will formally accept the "NOT APPLICABLE" designation for multi-agent orchestration. | Industry pressure to adopt "agentic AI" may conflict with safety-first engineering. | Executive Sponsor | Requires firm defense of the deterministic architecture during Stage 11 exit gate review. | Stage 11 Handoff Protocol. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved, bounded and testable agentic architecture