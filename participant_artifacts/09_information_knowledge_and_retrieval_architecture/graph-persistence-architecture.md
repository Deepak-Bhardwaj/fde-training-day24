# Graph Persistence Architecture

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer D: Graph Data Platform)
**Participant status:** COMPLETED
**Deliverable form:** Diagram + supporting table + rationale

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To define how the Knowledge Graph is physically stored, backed up, and synchronized between the shore-side platform and the vessel-edge runtime, ensuring offline continuity (GS-14) and safe reconciliation (GS-15).

## Upstream dependency
Use the completed Stage 08 Selected Solution (ADR-001: Event-Driven Hybrid) and Stage 09 Graph Logical Model.

## Evidence to inspect
- `evidence/02_documents/fleet_operations_interview_notes.md`
- `evidence/01_enterprise_sources/source_inventory.csv`

## Case challenge
The vessel edge cannot host a full, enterprise-scale graph database. The persistence architecture must define a lightweight, read-optimized graph store for the vessel that can safely sync with the shore's ACID-compliant graph database.

## Diagram Description (Persistence Topology)
*(Text-based representation)*
- **Shore Platform:** Full Property Graph DB (e.g., Neo4j Enterprise Cluster). ACID compliant. Stores all nodes, edges, and `EvidenceRecord` history.
- **Vessel Edge:** Lightweight Embedded Graph Store (e.g., SQLite with graph extensions, or a lightweight embedded DB). Read-optimized. Stores only the "Active Subgraph" (Active Constraints, Current Voyage, Cached Policies).
- **Sync Mechanism:** Event-Sourced Delta Sync. Shore publishes graph mutations (Node created, Edge updated) to the event bus. Vessel edge consumes events and applies them idempotently.

## Working scaffold (Persistence Details)

| Component | Technology Pattern | Data Scope | Sync / Update Mechanism | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **Shore Knowledge Graph** | Enterprise Property Graph DB (ACID) | Full history. All nodes, edges, and `EvidenceRecord` payloads. | Direct writes from Ingestion ACL and Deterministic Engine. | `reference-architecture-comparison.md` |
| **Vessel Edge Graph** | Lightweight Embedded Graph Store | **Active Subgraph Only.** Current Voyage, ACTIVE Constraints (not expired), ACTIVE Policies. | Consumes `GraphMutationEvent` stream from shore. Applies idempotently using `record_id`. | `ddd-context-map.md`, `ctqs.md` |
| **Blob Storage (Shore)** | Object Storage (S3/MinIO) | Raw source documents (Port Notice PDFs, Telemetry payloads). | Referenced by `EvidenceRecord.document_uri`. | `provenance-evidence-linkage-model.md` |
| **Audit Log Store** | Append-Only Time-Series DB | Immutable stream of all domain events and graph mutations. | Shore and Vessel edge both write to their local audit logs; synced on reconnect. | `bounded-contexts.md` |

## Rationale
By restricting the vessel edge to the "Active Subgraph," we drastically reduce the storage and compute footprint, ensuring the deterministic engine can run efficiently on constrained hardware during a blackout (GS-14). The event-sourced sync ensures that if connectivity is lost, the vessel's local graph remains consistent, and any mutations made offline (e.g., Master approving a plan) are safely merged into the shore graph upon reconnect without conflict (GS-15).

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| The vessel edge must run a lightweight, read-optimized graph store to support offline continuity. | `fleet_operations_interview_notes.md` | `go-no-go-kill-criteria.md` (G-02) | High confidence (non-negotiable constraint). |
| Event-sourced delta sync is required to handle safe reconciliation after blackouts. | `fleet_operations_interview_notes.md` (vessel/shore divergence) | `provenance-baseline.md` | High confidence (SME interview). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The "Active Subgraph" definition (excluding expired constraints and superseded policies) reduces the graph size by >80%, making it viable for edge storage. | Exact graph size metrics not calculated. | Shore Platform Team | If the subgraph is still too large, the caching strategy must be aggressively pruned to only include constraints relevant to the current Voyage. | Stage 10 Deployment Topology. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture