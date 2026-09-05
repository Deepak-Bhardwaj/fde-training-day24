# Hybrid Retrieval Architecture

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer E: Hybrid Retrieval)
**Participant status:** COMPLETED
**Deliverable form:** Diagram + supporting table + rationale

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To define how the system retrieves context for both the deterministic engine (structured facts) and the Fleet Controller UI (historical precedents, unstructured policy context), combining Graph traversal, Vector search, and Keyword matching.

## Upstream dependency
Use the completed Stage 08 Selected Solution (ADR-003) and Stage 09 Graph Indexing Strategy.

## Evidence to inspect
- `evidence/02_documents/fleet_operations_interview_notes.md`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
Retrieval is for *context generation*, not *decision making*. The deterministic engine makes the final feasibility decision based on graph facts. Vector/keyword retrieval only provides supporting context to the human operator.

## Diagram Description (Retrieval Flow)
*(Text-based representation)*
1. **User Query / Engine Request** -> **Retrieval Router**
2. **Router** splits request:
   - **Path A (Structured Facts):** Query Property Graph (e.g., "What are Vessel X's active constraints?").
   - **Path B (Semantic Context):** Query Vector Store (e.g., "Show me past recovery options for severe weather in the North Sea").
   - **Path C (Keyword Match):** Query Full-Text Index (e.g., "Find policy document mentioning 'hazardous cargo'").
3. **Fusion Layer** combines results, strictly prioritizing Graph Facts over Vector suggestions.
4. **Output** -> Deterministic Engine (Facts only) OR Controller UI (Facts + Context).

## Working scaffold (Retrieval Routing)

| Query Type | Example | Primary Source | Secondary Source | Fusion / Priority Rule | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Operational Fact** | "Is Berth 4 confirmed?" | Property Graph (`[:CONSTRAINED_BY]`) | None | Graph fact is absolute. | `source_authority.yaml` |
| **Historical Precedent** | "How did we handle a similar CMMS hold last year?" | Vector Store (Embeddings of past `RecoveryOption` nodes) | Property Graph (Link to actual past option) | Vector provides summary; Graph provides the exact historical record. | `fleet_operations_interview_notes.md` |
| **Policy Keyword** | "What is the rule for crew rest after a diversion?" | Full-Text Index (`PolicyRule.text`) | Vector Store (Semantic expansion) | Full-text match on `status = 'ACTIVE'` rules only. | `source_authority.yaml` |

## Rationale
By separating structured facts (Graph) from semantic context (Vector), we prevent the "hallucination" risk of LLMs from polluting the deterministic engine's feasibility checks. The Controller gets the best of both worlds: hard, auditable facts for decision-making, and rich, semantic search for historical learning.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Vector search must never override graph facts in the deterministic engine. | `source_authority.yaml` (AI_OUTPUT precedence: NON_AUTHORITATIVE) | `ai-suitability-assessment.md` | High confidence (explicit policy). |
| Historical precedents are valuable for controllers but must be clearly separated from active constraints. | `fleet_operations_interview_notes.md` | `oversight-transparency-requirements.md` | High confidence (SME interview). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The vector store can be kept in sync with the graph's `RecoveryOption` nodes without significant lag. | Embedding generation pipeline latency not benchmarked. | Shore Platform Team | If lag is high, controllers may not see the most recent historical precedents. | Stage 10 AI / RAG Integration Architecture. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture