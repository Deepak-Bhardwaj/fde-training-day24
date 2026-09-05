# Target C4 Container View

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 10 — AI & Application Architecture
**Participant status:** COMPLETED
**Deliverable form:** Diagram + supporting table + rationale

## Stage question
How will the AI-enabled application consume context, integrate, deploy and fail safely?

## Why this artifact exists
To break down the Workbench into its major technical containers (applications, data stores, communication mechanisms), split across the Shore Platform and the Vessel Edge.

## Upstream dependency
Use the completed Stage 10 Target C4 Context View and Stage 09 Physical Persistence Topology.

## Evidence to inspect
- `evidence/02_documents/fleet_operations_interview_notes.md`
- `evidence/01_enterprise_sources/source_inventory.csv`

## Case challenge
Explicitly separate the heavy, cloud-dependent shore containers from the lightweight, offline-capable vessel edge containers.

## Diagram Description (Level 2 Containers)
*(Text-based representation)*
- **Shore Platform:** Ingestion ACL, NLP Extraction Service, Canonical Graph DB, Vector DB, Context Assembler, Fleet Controller UI.
- **Vessel Edge:** Edge Graph Store, Deterministic Engine, Master UI, Local Audit Buffer.
- **Integration:** Event Bus (MQTT over Sat-com).

## Working scaffold

| Container Name | Location | Technology / Pattern | Responsibility | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **Ingestion ACL** | Shore | API Gateway + Rules Engine | Validates schemas, attaches Provenance Envelope, enforces Zero Trust. | `target-information-trust-boundaries.md` |
| **NLP Extraction Service** | Shore | Worker + External LLM API | Parses Port Notice PDFs. Returns confidence scores. | `knowledge-extraction-specification.md` |
| **Canonical Graph DB** | Shore | Enterprise Property Graph | Stores full Knowledge Graph, active constraints, lineage. | `graph-persistence-architecture.md` |
| **Vector DB** | Shore | Vector Database | Stores embeddings for historical precedents and policy text. | `hybrid-retrieval-architecture.md` |
| **Context Assembler** | Shore | API Service | Isolates the "Active Subgraph" for a specific voyage. | `context-assembly-model.md` |
| **Fleet Controller UI** | Shore | Web Application | Displays facts + vector context. Hosts HITL Review Queue. | `oversight-transparency-requirements.md` |
| **Edge Graph Store** | Vessel | Embedded SQLite/RocksDB | Stores the "Active Subgraph" cache. Read-optimized. | `graph-persistence-architecture.md` |
| **Deterministic Engine** | Vessel | Local Service | Runs feasibility checks (GQ-01, GQ-02) using local graph. | `business-rules.md` |
| **Master UI** | Vessel | Local Web / Thin Client | Displays options, captures Master cryptographic/procedural approval. | `role_authorization_matrix.csv` |
| **Event Bus (MQTT)** | Sat-com | MQTT Broker (QoS 1/2) | Handles delta-sync, offline buffering, and priority routing. | `physical-persistence-topology.md` |

## Rationale
This container view proves that the Vessel Edge is entirely self-sufficient for core operations. If the Shore Platform, NLP Service, or Vector DB go down, the Vessel Edge continues to operate using its cached Edge Graph Store and Deterministic Engine. The Event Bus acts as the resilient bridge between the two zones.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| The Vessel Edge containers are completely independent of Shore containers for core operations. | `fleet_operations_interview_notes.md` | `go-no-go-kill-criteria.md` (G-02) | High confidence (non-negotiable constraint). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The MQTT broker can handle the burst traffic of a full graph sync after a multi-day blackout. | Broker throughput under extreme burst conditions NOT RUN. | Shore Platform Team | May require implementing rate-limiting or chunked sync protocols. | Stage 10 Failure-Mode Design. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Complete base AI/application architecture