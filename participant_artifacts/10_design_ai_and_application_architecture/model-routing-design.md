# Model Routing Design

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 10 — AI & Application Architecture
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
How will the AI-enabled application consume context, integrate, deploy and fail safely?

## Why this artifact exists
To define the routing logic for AI/LLM model calls, ensuring that model usage is strictly bounded to the approved use cases (NLP extraction and embedding generation), and that the deterministic engine never invokes a probabilistic model.

## Upstream dependency
Use the completed Stage 08 Selected Solution (ADR-003), Stage 09 Knowledge Extraction Specification, and Stage 10 AI/RAG Integration Architecture.

## Evidence to inspect
- `evidence/04_policy_authority/source_authority.yaml`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
Explicitly define which components are allowed to call external LLM APIs, under what conditions, and what happens when the model is unavailable. The system must degrade gracefully, not fail catastrophically.

## Minimum content

### 1. Approved Model Call Paths
| Call Path | Trigger | Model Type | Location | Fallback on Failure | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Path A: Port Notice Extraction** | New PDF uploaded to Ingestion ACL | External LLM API (e.g., GPT-4o-mini) | Shore Platform only | Route PDF to HITL Review Queue for manual Controller entry. | `knowledge-extraction-specification.md` |
| **Path B: Policy Text Extraction** | New policy document versioned in SRC-POLICY | External LLM API | Shore Platform only | Flag document as "Unprocessed"; route to Compliance team for manual rule entry. | `retrieval-source-adapters.md` |
| **Path C: Embedding Generation** | New `RecoveryOption` or `PolicyRule` node created in Graph | Embedding Model (e.g., text-embedding-3-small) | Shore Platform only | Skip embedding; vector search for this entity is unavailable until batch re-embed. | `vector-schema.json` |

### 2. Prohibited Model Call Paths
| Prohibited Path | Reason | Enforcement Mechanism | Evidence |
| :--- | :--- | :--- | :--- |
| **Deterministic Engine -> LLM** | Feasibility checking must be 100% deterministic and explainable. | Network-level firewall rule: Engine container cannot reach LLM API endpoint. | `ai-suitability-assessment.md`, `retrieval-adrs.md` (ADR-014) |
| **Vessel Edge -> LLM** | Vessel edge must operate offline. No cloud dependency permitted. | Vessel edge container has no outbound internet access. | `ctqs.md` (Offline Continuity) |
| **Master UI -> LLM** | Master approval must be based on human judgment, not AI suggestion. | UI backend only calls Deterministic Engine and Graph DB. | `role_authorization_matrix.csv` |

### 3. Model Routing Policies
- **Rate Limiting:** LLM API calls are rate-limited to 100 requests/minute to prevent cost overruns and vendor throttling.
- **Timeout:** All LLM calls have a hard 30-second timeout. If exceeded, the request is treated as a failure and routed to the fallback path.
- **Retry:** Maximum 2 retries with exponential backoff. After 3 total attempts, the fallback path is triggered.
- **Logging:** Every LLM call (input hash, output hash, latency, confidence score) is logged to the Audit Context for compliance.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| The deterministic engine must never call an LLM API. | `source_authority.yaml` (AI_OUTPUT precedence: NON_AUTHORITATIVE) | `non-ai-alternative.md` | High confidence (explicit policy). |
| LLM failure must degrade to human-in-the-loop, not system failure. | `fleet_operations_interview_notes.md` | `risk-treatment-plan.md` (RH-03) | High confidence (SME interview). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The 30-second timeout is sufficient for complex multi-page Port Notice PDFs. | LLM latency for large documents NOT RUN. | Shore Platform Team | If insufficient, the NLP Worker must implement chunked extraction with partial result merging. | Stage 10 Prompt / Context Design. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Complete base AI/application architecture