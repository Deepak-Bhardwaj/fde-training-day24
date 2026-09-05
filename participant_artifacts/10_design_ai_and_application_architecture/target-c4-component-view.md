# Target C4 Component View

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 10 — AI & Application Architecture
**Participant status:** COMPLETED
**Deliverable form:** Diagram + supporting table + rationale

## Stage question
How will the AI-enabled application consume context, integrate, deploy and fail safely?

## Why this artifact exists
To drill down into the internal components of a critical container. We will focus on the **Shore Ingestion ACL & NLP Extraction Service**, as this is where the Zero Trust boundary and the bounded AI integration live.

## Upstream dependency
Use the completed Stage 10 Target C4 Container View and Stage 09 Target Information Trust Boundaries.

## Evidence to inspect
- `evidence/04_policy_authority/source_authority.yaml`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
Show exactly how the system prevents untrusted, unstructured external data from polluting the canonical graph, and how the AI/NLP component is strictly bounded.

## Diagram Description (Level 3 Components: Ingestion ACL)
*(Text-based representation)*
- **API Gateway** -> **Schema Validator** -> **Provenance Enforcer** -> **Routing Decision**.
- **Routing Decision** -> (If Structured) -> **Graph Writer**.
- **Routing Decision** -> (If Unstructured/PDF) -> **NLP Extraction Worker** -> **Confidence Router**.
- **Confidence Router** -> (If >0.95) -> **Graph Writer**.
- **Confidence Router** -> (If <0.95) -> **HITL Review Queue**.

## Working scaffold

| Component Name | Responsibility | Interactions | Evidence |
| :--- | :--- | :--- | :--- |
| **Schema Validator** | Rejects payloads that do not match the Data Contracts (DC-TELEM-01, etc.). | Receives raw payload from API Gateway. | `data-contracts.md` |
| **Provenance Enforcer** | Attaches the mandatory Provenance Envelope (source_id, observed_ts, authority_weight). Rejects if metadata is missing. | Wraps payload. | `authority-freshness-metadata-profile.md` |
| **NLP Extraction Worker** | Calls external LLM API to extract structured fields from Port Notice PDFs. Returns `confidence_score`. | Calls External LLM API. | `knowledge-extraction-specification.md` |
| **Confidence Router** | Evaluates `confidence_score`. If < 0.95, routes to HITL. If >= 0.95, proceeds. | Routes payload. | `retrieval-adrs.md` (ADR-015) |
| **Graph Writer** | Applies semantic mapping, enforces uniqueness constraints, and writes to Canonical Graph DB. | Writes to DB. | `source-to-canonical-mapping.md` |
| **HITL Review Queue** | Stores low-confidence extractions for Fleet Controller manual review. | Exposes API to Fleet Controller UI. | `fleet_operations_interview_notes.md` |

## Rationale
This component view proves that the AI (NLP Extraction Worker) is strictly isolated behind a confidence-based gate. It cannot write directly to the Canonical Graph DB. It must pass through the Confidence Router, ensuring that human operators retain control over ambiguous data, satisfying the "AI is NON_AUTHORITATIVE" mandate.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| NLP extraction must be gated by a confidence threshold before writing to the graph. | `poc-model-rag-results.md` | `selected-solution.md` (ADR-003) | High confidence (explicit design condition). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The external LLM API latency is acceptable for the Ingestion ACL SLA. | LLM API latency NOT RUN. | Shore Platform Team | If latency is high, the NLP Worker must be fully asynchronous, decoupling ingestion from extraction. | Stage 10 API Contracts. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Complete base AI/application architecture