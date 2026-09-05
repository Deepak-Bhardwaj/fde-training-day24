# Non-AI Alternative Assessment

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 04 — Triage Regulation & Qualify Use Case
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
Should AI be used at all, and under what impact/regulatory constraints?

## Why this artifact exists
To rigorously evaluate whether a purely deterministic, rules-based system could solve the core problem without introducing the complexity, opacity, and hallucination risks of AI/ML models.

## Upstream dependency
Use the completed Stage 03 Root-Cause Analysis and Stage 04 AI Suitability Assessment.

## Evidence to inspect
- `evidence/02_documents/fleet_operations_interview_notes.md`
- `evidence/01_enterprise_sources/source_inventory.csv`

## Case challenge
Avoid the "AI for the sake of AI" trap. If a deterministic system can solve the problem safely and effectively, AI must not be used.

## Minimum content

| Alternative Approach | Description | Pros | Cons | Verdict | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Purely Deterministic Constraint Engine** | A rules-based system that ingests structured data from all 9 sources, applies strict temporal provenance, and runs a constraint-satisfaction algorithm to generate recovery options. | 100% explainable. Zero hallucination risk. Easily runs offline on vessel edge. Fast execution. | Cannot parse unstructured port notices (PDFs) or extract rules from unstructured policy documents. Requires all inputs to be perfectly structured APIs. | **Selected for Core Logic** | `fleet_operations_interview_notes.md` (Controllers want concise, evidence-backed comparison, not a chatbot). |
| **Manual Spreadsheet Reconciliation (Current State)** | Controllers manually pull data from 9 systems and reconcile in Excel/Email. | Zero technical implementation cost. | 45-minute reconciliation time. High error rate. No audit trail. Fails during connectivity loss. | **Rejected (Baseline)** | `baseline-dataset.csv` (M-01, M-05). |
| **Fully Autonomous AI Agent** | An LLM-based agent that autonomously monitors streams, negotiates with port APIs, and executes recovery plans. | Theoretically fastest reaction time. | Violates Master's authority (GS-08). High hallucination risk. Fails offline. Unacceptable safety risk. | **Rejected (Prohibited)** | `role_authorization_matrix.csv`, `prohibited-use-check.md`. |

## Overall Conclusion
The core problem of **reconciling structured constraints and evaluating feasibility** MUST be solved by a deterministic, rules-based engine. AI is not suitable for the core decision logic. 

However, a **Hybrid Approach** is justified for the *ingestion layer*: AI (specifically NLP/LLM extraction) may be used strictly to parse unstructured port notices and policy documents into structured constraints, which are then fed into the deterministic engine. Even in this hybrid model, the AI output is NON_AUTHORITATIVE and must be validated against deterministic rules.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Controllers explicitly prefer concise, evidence-backed comparisons over conversational AI. | `fleet_operations_interview_notes.md` | `ai-suitability-assessment.md` | High confidence (SME interview). |
| Core feasibility checking requires deterministic rules, not probabilistic models. | `source_inventory.csv` (CMMS holds are hard constraints) | `ctqs.md` | High confidence (explicit policy). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The deterministic engine can be built and deployed on the vessel edge within the project timeline. | Edge compute specs and deployment pipeline not yet defined. | Shore Platform Team | If edge deployment is too slow, the hybrid model may need to rely on shore-side processing with delayed sync. | Stage 10 Deployment Topology. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved and justified use case
Do not advance to Stage 05 until the Stage 04 exit gate is defensible.