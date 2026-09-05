# Runtime Context Graph Architecture

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer F: Runtime Context Graph)
**Participant status:** COMPLETED
**Deliverable form:** Diagram + supporting table + rationale

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To define how the system dynamically assembles the "Active Subgraph" (the specific slice of the Knowledge Graph relevant to a current Vessel, Voyage, and Disruption) for the Deterministic Engine to evaluate.

## Upstream dependency
Use the completed Stage 09 Graph Persistence Architecture and Entity/Relationship Model.

## Evidence to inspect
- `evidence/02_documents/fleet_operations_interview_notes.md`
- `evidence/01_enterprise_sources/source_inventory.csv`

## Case challenge
The full Knowledge Graph is too large and contains too much irrelevant data for real-time feasibility checking. The architecture must efficiently isolate the exact context needed for a specific decision, both on the shore and on the vessel edge.

## Diagram Description (Context Assembly Flow)
*(Text-based representation)*
1. **Trigger:** `DisruptionDetected` event for `Vessel X`, `Voyage Y`.
2. **Context Assembler:** Queries the full Knowledge Graph.
3. **Isolation Rules:**
   - Fetch `Vessel X` and `Voyage Y` nodes.
   - Fetch all `[:CONSTRAINED_BY]` edges where `valid_until > current_time`.
   - Fetch all `[:GOVERNS]` edges for `ACTIVE` policies relevant to `Voyage Y`'s cargo/region.
4. **Output:** A lightweight, in-memory "Runtime Context Graph" passed to the Deterministic Engine.
5. **Edge Caching:** This exact subgraph is serialized and synced to the Vessel Edge for offline use (GS-14).

## Working scaffold (Context Isolation Rules)

| Context Dimension | Isolation Logic | Purpose | Evidence |
| :--- | :--- | :--- | :--- |
| **Vessel / Voyage** | Strict match on `canonical_id` and `voyage_id`. | Prevents cross-vessel constraint leakage. | `semantic-constraints.md` (SC-05) |
| **Temporal Validity** | `valid_until > current_time()` | Ensures only active, non-expired constraints are evaluated. | `semantic-constraints.md` (SC-02) |
| **Policy Relevance** | Match policy `category` to voyage `cargo_type` or `region`. | Prevents irrelevant rules from blocking feasible options. | `source_authority.yaml` |
| **Authority Filter** | Exclude edges where `authority_weight < MEDIUM` (unless explicitly requested for UI context). | Reduces noise for the deterministic engine. | `source_authority.yaml` |

## Rationale
By dynamically assembling a targeted Runtime Context Graph, we decouple the massive, historical Knowledge Graph from the high-performance, real-time Deterministic Engine. This architecture is what makes the vessel-edge offline continuity (GS-14) possible: the edge doesn't need the whole database, just the specific, active subgraph for its current voyage.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| The deterministic engine requires a targeted subgraph, not the full knowledge graph, for real-time performance. | `fleet_operations_interview_notes.md` | `graph-persistence-architecture.md` | High confidence (architectural necessity). |
| The vessel edge must cache this specific subgraph to operate during blackouts. | `fleet_operations_interview_notes.md` | `go-no-go-kill-criteria.md` (G-02) | High confidence (non-negotiable constraint). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The Context Assembler can build the subgraph in < 20ms to leave enough time for the engine's feasibility check. | Context assembly latency is NOT RUN. | Shore Platform Team | If too slow, the isolation rules may need to be pre-computed and materialized as views. | Stage 10 AI / RAG Integration Architecture. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture