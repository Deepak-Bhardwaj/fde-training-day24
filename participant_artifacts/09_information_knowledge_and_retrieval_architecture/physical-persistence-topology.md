# Physical Persistence Topology

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer H: Target Information Architecture)
**Participant status:** COMPLETED
**Deliverable form:** Diagram + supporting table + rationale

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To define the physical infrastructure, hardware, and database technologies required to host the logical data architecture, specifically addressing the severe bandwidth and compute constraints of the vessel edge during satellite blackouts.

## Upstream dependency
Use the completed Stage 09 Target Data Architecture and Stage 08 Selected Solution (ADR-001).

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
The physical topology must prove that the vessel edge can operate autonomously on constrained hardware (e.g., industrial marine PCs) without relying on cloud connectivity, while the shore platform can handle enterprise-scale workloads.

## Diagram Description (Physical Topology)
*(Text-based representation)*
- **[Shore Data Center / Cloud]**
  - **Enterprise Graph Cluster:** 3-node ACID-compliant Property Graph DB (Primary + Read Replicas).
  - **Vector DB:** Managed SaaS or self-hosted vector store for embeddings.
  - **Object Storage:** S3-compatible blob store for raw PDFs and telemetry payloads.
  - **Time-Series DB:** Immutable append-only store for the Audit Log.
- **[Satellite Comms Link]**
  - **MQTT / AMQP Broker:** Handles message queuing, delta-sync, and offline buffering for vessel comms.
- **[Vessel Edge Hardware]**
  - **Marine-grade Industrial PC:** Limited CPU/RAM, no internet access.
  - **Embedded DB:** SQLite with graph-traversal extensions or embedded RocksDB.
  - **Local NVMe Storage:** High-write endurance drive for the local Audit Buffer.

## Working scaffold (Physical Specifications)

| Component | Shore Physical Tech | Vessel Edge Physical Tech | Rationale / Constraint | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **Canonical Store** | Enterprise Property Graph (e.g., Neo4j Enterprise) | Embedded SQLite + Custom Graph Index | Shore needs ACID and clustering. Edge needs zero-footprint, read-optimized local storage. | `graph-persistence-architecture.md` |
| **Semantic Context** | Managed Vector Database | **NONE** (Vector search disabled offline) | Edge lacks compute for embedding generation/search. Falls back to cached Graph facts only. | `hybrid-retrieval-architecture.md` |
| **Raw Evidence** | S3 / MinIO Object Storage | Local File System (Rolling 30-day buffer) | Edge stores raw payloads locally until sync; Shore uses object storage for infinite retention. | `provenance-evidence-linkage-model.md` |
| **Audit Log** | Time-Series DB (e.g., InfluxDB) | Local SQLite (Append-only) | Edge buffers audit events locally; Shore maintains permanent regulatory record. | `bounded-contexts.md` |
| **Sync Transport** | Kafka / MQTT Broker | MQTT Client (QoS 1) | MQTT is highly resilient to the intermittent, high-latency nature of VSAT/LEO sat-com. | `dependencies.md` |

## Rationale
This polyglot physical topology ensures that the shore platform is optimized for heavy analytics, NLP extraction, and full historical lineage, while the vessel edge is ruthlessly optimized for survival. By stripping the Vector DB and heavy analytics from the edge, we guarantee that the deterministic engine can run at full speed even on a low-power marine PC during a multi-day blackout (GS-14).

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| The vessel edge must use an embedded, lightweight database to survive offline. | `fleet_operations_interview_notes.md` | `go-no-go-kill-criteria.md` (G-02) | High confidence (non-negotiable constraint). |
| MQTT is the optimal transport protocol for unreliable satellite links. | `dependencies.md` (Sat-com bandwidth limits) | `data-gap-register.md` (DG-01) | High confidence (industry standard for IoT/Marine). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The local NVMe drive on the vessel edge has sufficient write-endurance for the high-frequency local audit buffer. | Exact telemetry write-volume vs. NVMe TBW (Terabytes Written) limits NOT RUN. | Vessel Technical | If endurance is exceeded, the local audit buffer must be aggressively truncated or compressed. | Stage 10 Deployment Topology. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture