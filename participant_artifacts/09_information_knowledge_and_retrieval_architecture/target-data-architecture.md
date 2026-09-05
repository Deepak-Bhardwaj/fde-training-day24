# Target Data Architecture

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer H: Target Information Architecture)
**Participant status:** COMPLETED
**Deliverable form:** Diagram + supporting table + rationale

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To provide the definitive, high-level blueprint of the data stores, their physical locations (Shore vs. Vessel Edge), and the synchronization mechanisms that connect them, fulfilling the Event-Driven Hybrid architecture selected in Stage 08.

## Upstream dependency
Use the completed Stage 08 Selected Solution (ADR-001) and Stage 09 Graph Persistence Architecture.

## Evidence to inspect
- `evidence/02_documents/fleet_operations_interview_notes.md`
- `evidence/01_enterprise_sources/source_inventory.csv`

## Case challenge
The architecture must clearly separate the heavy, AI-assisted, historical shore-side stores from the lightweight, deterministic, offline-capable vessel-edge stores.

## Diagram Description (Target Data Topology)
*(Text-based representation)*
- **[Shore Platform]**
  - **Canonical Property Graph DB:** Stores full Knowledge Graph, active constraints, policies, and operational lineage.
  - **Vector Store:** Stores embeddings of historical precedents and unstructured policy text.
  - **Blob Storage:** Stores raw source documents (PDFs, telemetry payloads) referenced by `EvidenceRecord`.
  - **Append-Only Audit Log:** Immutable time-series store for all domain events and graph mutations.
- **[Sync Layer]**
  - **Event Bus (Kafka/MQTT):** Transports `GraphMutationEvent` and `DomainEvent` streams. Handles delta-sync and conflict resolution.
- **[Vessel Edge]**
  - **Embedded Graph Store:** Lightweight, read-optimized store holding only the "Active Subgraph" (Current Voyage, Active Constraints).
  - **Local Audit Buffer:** Stores offline execution logs and Master approvals until reconnect.

## Working scaffold (Store Specifications)

| Store Name | Location | Technology Pattern | Data Scope | Sync / Update Mechanism | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Canonical Graph** | Shore | Enterprise Property Graph (ACID) | Full history, all nodes/edges, operational lineage. | Direct writes from ACL and Engine. | `reference-architecture-comparison.md` |
| **Vector Store** | Shore | Vector Database | Historical precedents, unstructured text embeddings. | Batch sync from Graph DB `RecoveryOption` nodes. | `hybrid-retrieval-architecture.md` |
| **Blob Storage** | Shore | Object Storage (S3/MinIO) | Raw source documents, telemetry payloads. | Referenced by `EvidenceRecord.document_uri`. | `provenance-evidence-linkage-model.md` |
| **Audit Log** | Shore | Append-Only Time-Series DB | Immutable stream of all domain events. | Shore and Vessel write locally; Vessel syncs on reconnect. | `bounded-contexts.md` |
| **Edge Graph** | Vessel | Lightweight Embedded Graph | **Active Subgraph Only.** Current Voyage, ACTIVE Constraints. | Consumes `GraphMutationEvent` stream from shore. | `graph-persistence-architecture.md` |
| **Edge Audit** | Vessel | Local File / SQLite | Offline execution logs, Master approvals. | Batch uploads to Shore Audit Log upon `ConnectivityRestored`. | `domain-events.md` |

## Rationale
This topology perfectly aligns with the non-negotiable constraints. The Shore Platform handles the heavy lifting (NLP, historical search, full audit), while the Vessel Edge is stripped down to the absolute minimum required for safe, deterministic decision-making during a blackout (GS-14). The Event Bus ensures that when connectivity returns, the vessel's offline actions are safely merged into the shore's ACID-compliant graph without data loss (GS-15).

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| The vessel edge must be restricted to an "Active Subgraph" to ensure offline viability. | `fleet_operations_interview_notes.md` | `go-no-go-kill-criteria.md` (G-02) | High confidence (non-negotiable constraint). |
| Raw evidence must be offloaded to Blob Storage to prevent graph database bloat. | `provenance-evidence-linkage-model.md` | `graph-logical-model.md` | High confidence (architectural best practice). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The Event Bus can guarantee ordered delivery of `GraphMutationEvent` streams to the vessel edge, even after a prolonged blackout. | Event bus ordering guarantees during network partitions are NOT RUN. | Shore Platform Team | If ordering is lost, the vessel edge may apply constraints out of sequence, requiring complex conflict resolution. | Stage 10 Failure-Mode Design. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture