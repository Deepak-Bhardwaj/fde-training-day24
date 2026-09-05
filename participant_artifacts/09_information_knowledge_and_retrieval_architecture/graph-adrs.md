# Graph ADRs

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer I: Architecture Decisions / Schemas)
**Participant status:** COMPLETED
**Deliverable form:** ADR / decision record

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To formally record the architectural decisions specific to the Property Graph implementation, focusing on edge properties, indexing, and idempotency.

## Upstream dependency
Use the completed Stage 09 Graph Logical Model, Entity/Relationship Model, and Evidence Identifier Model.

## Evidence to inspect
- `evidence/01_enterprise_sources/live_event_stream.jsonl`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
Graph databases are often misused as simple key-value stores. These ADRs must enforce the use of the graph's native strengths (relationship traversal, edge properties) to solve the maritime domain's specific temporal and authority challenges.

## Minimum content

### ADR-010: Edge Properties for Temporal and Authority Metadata
- **Status:** Accepted
- **Context:** A `Voyage` may be constrained by multiple conflicting `Constraint` nodes (e.g., a Port API saying "Open" and a Port Notice saying "Closed"). Storing authority and temporal validity only on the `Constraint` node makes it impossible to represent the *relationship* between the voyage and the specific source of the constraint.
- **Decision:** All `[:CONSTRAINED_BY]` edges must carry their own properties: `authority_weight`, `valid_until`, and `source_version`. 
- **Consequences:** (+) Allows the deterministic engine to filter out stale or low-authority constraints in a single, highly optimized graph traversal step (GQ-01). (+) Natively resolves semantic conflicts at the relationship level. (-) Increases the storage footprint of edges and requires composite edge indexing.
- **Evidence:** `semantic-constraints.md` (SC-01, SC-02), `graph-query-traversal-patterns.md`

### ADR-011: Deterministic SHA-256 Hashing for Evidence Idempotency
- **Status:** Accepted
- **Context:** The SRC-TELEM stream suffers from clock drift and duplicate delivery (GS-07). Relying on database auto-increment IDs or ingestion timestamps to identify unique events will result in duplicate constraints and corrupted state during network retries.
- **Decision:** Every raw `EvidenceRecord` is assigned a deterministic ID: `SHA-256(source_id + observed_timestamp + payload_hash)`. The database enforces a uniqueness constraint on this ID.
- **Consequences:** (+) Guarantees 100% idempotency. If a duplicate event arrives 5 minutes late due to sat-com lag, it is silently and safely discarded. (+) Works identically on the shore and the vessel edge without coordination. (-) Requires the edge CPU to compute SHA-256 hashes for high-frequency telemetry.
- **Evidence:** `canonical-identifier-strategy.md`, `quality-profile.md`

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Edge properties are mandatory to handle temporal and authority conflicts natively. | `fleet_operations_interview_notes.md` | `knowledge-graph-schema.md` | High confidence (architectural necessity). |
| Deterministic hashing is the only safe way to handle duplicate telemetry delivery. | `live_event_stream.jsonl` | `business-rules.md` (BR-05) | High confidence (explicit source metadata). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The chosen Property Graph DB supports efficient composite indexes on edge properties. | Vendor feature matrix verification NOT RUN. | Shore Platform Team | If unsupported, the engine must pull all edges into application memory to filter, destroying performance. | Stage 09 Graph Indexing Strategy. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture