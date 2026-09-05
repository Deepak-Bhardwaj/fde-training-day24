# Agent Suitability Assessment

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 11 — Agentic & Multi-Agent Orchestration
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
Is autonomy justified, bounded, permissioned, interruptible and testable?

## Why this artifact exists
To objectively evaluate whether autonomous or multi-agent systems are suitable for any part of the workbench, or if deterministic automation and human-in-the-loop workflows are the safer, more effective choice.

## Upstream dependency
Use the completed Stage 04 AI Suitability Assessment, Stage 05 Business Rules, Stage 07 Risk Treatment Plan, and Stage 10 Failure-Mode Design.

## Evidence to inspect
- `Participant_Case_Study.md` (Non-negotiable constraints, GS-02, GS-08)
- `evidence/04_policy_authority/role_authorization_matrix.csv`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
Avoid the "agentic hype" trap. Autonomy introduces unpredictability, hallucination risks, and complex debugging. In a safety-critical maritime domain, unpredictability is unacceptable.

## Minimum content

| Evaluation Criteria | Assessment | Verdict (Suitable / Not Suitable) | Evidence / Rationale |
| :--- | :--- | :--- | :--- |
| **Safety-Critical Execution** | Agents cannot be trusted to execute navigational changes or override CMMS holds. The cost of error is catastrophic (casualty, environmental damage). | **NOT SUITABLE** | `role_authorization_matrix.csv` (MASTER authorize_navigation_change=YES, AI_AGENT=NO). `business-rules.md` (BR-01, BR-02). |
| **Deterministic Feasibility Checking** | Evaluating if a recovery option violates a constraint requires 100% explainable, binary logic. Probabilistic agent reasoning is inherently opaque. | **NOT SUITABLE** | `non-ai-alternative.md`, `retrieval-adrs.md` (ADR-014). |
| **Offline Continuity (GS-14)** | Multi-agent frameworks require significant compute and often rely on cloud-based LLM APIs. This violates the vessel edge offline constraint. | **NOT SUITABLE** | `ctqs.md` (Offline Continuity), `deployment-topology.md`. |
| **Administrative / Reporting Tasks** | Drafting post-event audit reports or summarizing historical precedents for the Fleet Controller. Low safety impact, high human review. | **PARTIALLY SUITABLE** (Strictly Bounded) | Can be handled by a single, highly constrained "Report Drafting Assistant" agent, but ONLY on the shore platform, with mandatory human approval before saving. |

## Overall Suitability Conclusion
**NO AGENT / NO MULTI-AGENT SYSTEM is suitable for the core operational workflow.** 

The core workflow (ingestion, constraint resolution, feasibility checking, and recovery option generation) **MUST** be executed by a **Deterministic Workflow Orchestrator** (e.g., event-driven state machine), not an agentic framework. 

A single, highly bounded "Assistant" agent may be considered *only* for shore-side, non-critical administrative tasks (e.g., drafting post-event audit summaries), and even then, it must operate under strict human-in-the-loop supervision.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Autonomous execution is explicitly prohibited by non-negotiable constraints. | `Participant_Case_Study.md` | `prohibited-use-check.md` | High confidence (explicit mandate). |
| Deterministic orchestration is required for explainable feasibility checking. | `ai-suitability-assessment.md` | `selected-solution.md` | High confidence (explicit design choice). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: Stakeholders will accept a "NO AGENT" conclusion for the core workflow despite industry hype. | Cultural expectation of "AI automation" may conflict with safety reality. | Executive Sponsor / FDE Team | Requires clear communication that "Deterministic Automation" is the superior, safer choice for this domain. | Stage 11 Autonomy-Level ADR. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved, bounded and testable agentic architecture
Do not advance to the next artifact until this assessment is defensible.