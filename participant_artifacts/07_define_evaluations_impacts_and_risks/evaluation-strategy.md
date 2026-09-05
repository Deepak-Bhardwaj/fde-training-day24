# Evaluation Strategy

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 07 — Define Evaluations, Impacts & Risks
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
What must the future system prove before it is acceptable?

## Why this artifact exists
To define the overarching methodology for validating that the workbench meets all safety, regulatory, and operational requirements before any deployment.

## Upstream dependency
Use the completed Stage 03 KPI Tree, Stage 04 Go/No-Go Criteria, Stage 05 Business Rules, and Stage 06 Data Gap Register.

## Evidence to inspect
- `Participant_Case_Study.md` (Golden Scenarios)
- `evidence/04_policy_authority/role_authorization_matrix.csv`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
Define a rigorous evaluation strategy that separates the testing of the *deterministic core* from any auxiliary AI/NLP components. Do not evaluate AI on safety-critical execution, as it is strictly non-authoritative.

## Minimum content

| Evaluation Dimension | Methodology | Target Components | Evidence Basis |
| :--- | :--- | :--- | :--- |
| **Deterministic Logic Verification** | Unit and integration testing of the constraint engine against known rules (e.g., BR-02 Technical Holds). | Constraint Engine, Rule Validator | `business-rules.md`, `source_inventory.csv` |
| **Golden Scenario Stress Testing** | Simulation of specific, high-risk operational states to verify system behavior under stress. | Entire Workbench (End-to-End) | `Participant_Case_Study.md` (GS-02, 03, 04, 05, 07, 08, 09, 14, 15) |
| **Temporal Provenance & Idempotency** | Injection of duplicated, out-of-order, and clock-drifted events into the ingestion layer to verify deduplication. | Ingestion ACL, Event Bus | `live_event_stream.jsonl`, `quality-profile.md` |
| **Offline Continuity Validation** | Simulated network partition (sat-com blackout) to verify vessel-edge fallback and subsequent safe reconciliation. | Vessel Command Context, Sync Layer | `fleet_operations_interview_notes.md`, `dependencies.md` |
| **Human-in-the-Loop Usability** | Tabletop exercises with SMEs (Fleet Controllers, Masters) to validate that recovery options are concise, evidence-backed, and clearly marked as non-authoritative. | Fleet Controller UI, Master Approval Flow | `fleet_operations_interview_notes.md` |
| **AI/NLP Extraction Accuracy** | Separate, isolated evaluation of any NLP component used for parsing unstructured port notices, measuring precision/recall against a human-annotated baseline. | External Intelligence Context (ACL) | `lineage.md`, `data-gap-register.md` (DG-03) |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Evaluation must explicitly cover mandated Golden Scenarios. | `Participant_Runbook.md` (Stage 07 requirements) | `representativeness-assessment.md` | High confidence (explicit training mandate). |
| AI components must be evaluated separately from the deterministic core. | `non-ai-alternative.md`, `source_authority.yaml` | `ai-suitability-assessment.md` | High confidence (explicit design choice). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: We have access to a simulation environment capable of injecting network blackouts (GS-14). | Exact testing infrastructure capabilities not yet defined. | Shore Platform Team | May require building a custom mock/simulation harness for Stage 08/09. | Stage 08 PoC / Model / RAG Results (or "NOT RUN" with rationale). |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Evaluation, impact and risk requirements
Do not advance to Stage 08 until the Stage 07 exit gate is defensible.