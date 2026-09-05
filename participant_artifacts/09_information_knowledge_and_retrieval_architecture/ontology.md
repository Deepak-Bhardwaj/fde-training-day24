# Ontology

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer B: Semantic Foundation)
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To define the formal relationships, hierarchies, and graph structure between the canonical entities. This ontology forms the basis for the Knowledge Graph and the deterministic engine's relationship traversal.

## Upstream dependency
Use the completed Stage 05 Domain Events, Stage 09 Canonical Entity Model, and Stage 09 Semantic Model.

## Evidence to inspect
- `evidence/04_policy_authority/source_authority.yaml`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
The ontology must explicitly model authority and constraint relationships, not just physical or temporal ones. (e.g., A CMMS Hold *blocks* a Recovery Option).

## Minimum content

### Core Entity Relationships (Graph Edges)
- **Vessel** `operates_on` **Voyage** (1:N)
- **Voyage** `encounters` **Disruption** (1:N)
- **Disruption** `mitigated_by` **Recovery Option** (1:N)
- **Recovery Option** `constrained_by` **Constraint** (N:M)
- **Constraint** `derived_from` **Source Data** (1:1)
- **Policy Rule** `governs` **Recovery Option** (1:N)
- **Master** `approves` **Recovery Option** (1:1)
- **Chief Engineer** `releases` **Constraint (CMMS)** (1:1)

### Semantic Hierarchy & Authority Rules
1. **Constraint Hierarchy:** 
   - `Technical Hold (CMMS)` > `Safety Rule (Policy)` > `Port Constraint (Signed)` > `Cargo Window` > `Port Constraint (API)`.
   - *Rule:* A higher-tier constraint cannot be overridden by a lower-tier constraint.
2. **Identity Hierarchy:**
   - `Fleet Registry (SRC-FMS)` > `AIS Observation (SRC-AIS)`.
   - *Rule:* If an edge exists between `Vessel` and `AIS Observation`, and it conflicts with `Fleet Registry`, the `AIS Observation` edge is marked `INVALID`.
3. **Temporal Validity:**
   - All `constrained_by` edges have a `valid_from` and `valid_until` timestamp derived from the source's freshness threshold.
   - *Rule:* If `current_time > valid_until`, the edge is marked `STALE` and the constraint is excluded from the deterministic engine.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| The ontology explicitly models constraint hierarchy to enforce CMMS supremacy. | `source_authority.yaml`, `business-rules.md` | `canonical-entity-model.md` | High confidence (explicit policy). |
| Edges in the graph must carry temporal validity to handle data freshness. | `source_inventory.csv` (freshness thresholds) | `provenance-baseline.md` | High confidence (architectural necessity). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The graph database (or in-memory graph on the vessel edge) can efficiently traverse the `constrained_by` edges in real-time for feasibility checking. | Graph query performance on edge hardware not benchmarked. | Shore Platform Team | If traversal is too slow, the engine may need to flatten the graph into relational tables for the feasibility check. | Stage 09 Graph Query / Traversal Patterns. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture
Do not advance to the next sub-layer until this artifact is defensible.