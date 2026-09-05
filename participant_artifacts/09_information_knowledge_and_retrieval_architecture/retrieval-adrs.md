# Retrieval ADRs

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer I: Architecture Decisions / Schemas)
**Participant status:** COMPLETED
**Deliverable form:** ADR / decision record

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To formally record the architectural decisions regarding the Hybrid Retrieval layer, specifically how the system balances structured graph facts with probabilistic vector search without compromising safety.

## Upstream dependency
Use the completed Stage 09 Hybrid Retrieval Architecture, Retrieval Routing Policy, and Semantic ADRs.

## Evidence to inspect
- `evidence/04_policy_authority/source_authority.yaml`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
Ensure these ADRs explicitly prevent the "hallucination" risk of vector search from polluting the deterministic safety engine.

## Minimum content

### ADR-014: Hard Isolation of Vector Store from Deterministic Engine
- **Status:** Accepted
- **Context:** The system uses a Vector Store for historical precedents and semantic context. However, the Deterministic Engine requires 100% explainable, auditable facts for feasibility checking (BR-02).
- **Decision:** The Deterministic Engine is physically and programmatically blocked from querying the Vector Store. It only receives data from the Property Graph via the Context Assembler. The Vector Store is exclusively used to enrich the Fleet Controller UI.
- **Consequences:** (+) Eliminates the risk of AI hallucinations causing safety violations. (+) Guarantees 100% auditability of the feasibility engine. (-) Controllers must manually bridge the gap between hard facts and semantic suggestions.
- **Evidence:** `retrieval-routing-policy.md`, `ai-suitability-assessment.md`

### ADR-015: Confidence-Based Routing for NLP Extractions
- **Status:** Accepted
- **Context:** Port Notices are ingested via NLP extraction, which carries an inherent risk of inaccuracy (DG-03). Automatically trusting all extractions could lead to invalid constraints entering the graph.
- **Decision:** The Ingestion ACL evaluates the `nlp_confidence_score` returned by the extraction model. If the score is < 0.95, the extraction is routed to the Fleet Controller's "Review Queue" (Human-in-the-Loop) and is NOT written to the active Property Graph until manually approved.
- **Consequences:** (+) Prevents low-confidence NLP errors from blocking valid voyages. (+) Provides a safe fallback when vendor SLAs are not met. (-) Increases controller workload during periods of poor NLP performance.
- **Evidence:** `knowledge-extraction-specification.md`, `poc-model-rag-results.md`

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Vector search must never influence the deterministic feasibility engine. | `source_authority.yaml` | `go-no-go-kill-criteria.md` | High confidence (explicit policy). |
| NLP extractions require a mandatory human fallback to maintain safety. | `poc-model-rag