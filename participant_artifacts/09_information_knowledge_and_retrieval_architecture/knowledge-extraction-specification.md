# Knowledge Extraction Specification

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer C: Connected Knowledge)
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To define the pipeline for extracting structured knowledge from unstructured enterprise documents (Port Notices, Fleet Policies) using the bounded NLP component approved in Stage 08.

## Upstream dependency
Use the completed Stage 08 Selected Solution (ADR-003) and Stage 09 Knowledge Graph Schema.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `Participant_Runbook.md` (Rule: "Never manufacture PoC/model/RAG results")

## Case challenge
Explicitly define the confidence thresholds and human-in-the-loop fallbacks. Do not assume the NLP model is 100% accurate. Treat all extracted text as evidence, not instruction.

## Minimum content

### 1. Target Documents
- **Port Notices (PDF):** Extract `Port_ID`, `Berth_Status`, `Effective_Date`, `Expiry_Date`.
- **Fleet Policies (Word/PDF):** Extract `Rule_Category`, `Rule_Text`, `Status` (ACTIVE/SUPERSEDED).

### 2. Extraction Pipeline
1. **Ingestion:** Document received via API or manual upload.
2. **Sanitization:** Input stripped of malicious payloads to prevent prompt injection (GS-09).
3. **NLP Extraction:** Bounded LLM API extracts structured fields based on predefined schema.
4. **Confidence Scoring:** LLM returns a `confidence_score` (0.0 to 1.0) for each extracted field.
5. **Routing:**
   - If `confidence_score >= 0.95`: Automatically written to Knowledge Graph as `Constraint` or `PolicyRule`.
   - If `confidence_score < 0.95`: Routed to Fleet Controller "Review Queue" in UI.

### 3. Human-in-the-Loop (HITL) Fallback
- Controllers review the raw PDF alongside the NLP extraction.
- Controller can `Approve` (writes to graph with `source_id = SRC-PORT`), `Reject` (discards extraction), or `Edit` (corrects fields, then writes).
- All HITL actions are logged in the Audit Context with `approver_id`.

### 4. Live PoC Status
- **Status:** **NOT RUN**
- **Rationale:** Adhering to evidence discipline. NLP accuracy for maritime port notices is unproven in this synthetic environment.
- **Condition:** The 0.95 threshold is a placeholder and must be calibrated during vendor SLA negotiations in Stage 10.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| NLP extraction requires a mandatory human fallback for low-confidence results. | `poc-model-rag-results.md` | `selected-solution.md` (ADR-003) | High confidence (explicit design condition). |
| Input sanitization is required to prevent prompt injection from external documents. | `Participant_Case_Study.md` (GS-09) | `risk-treatment-plan.md` (RH-03) | High confidence (explicit security requirement). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The 0.95 confidence threshold balances automation efficiency with safety. | Optimal threshold requires live vendor testing (NOT RUN). | FDE Team | If too high, controller fatigue increases. If too low, safety risk increases. | Stage 10 Model Routing Design. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture