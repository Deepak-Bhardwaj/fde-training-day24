# Deployment Topology

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 10 — AI & Application Architecture
**Participant status:** COMPLETED
**Deliverable form:** Diagram + supporting table + rationale

## Stage question
How will the AI-enabled application consume context, integrate, deploy and fail safely?

## Why this artifact exists
To define the physical and network infrastructure required to host the Event-Driven Hybrid architecture, specifically addressing the severe constraints of the maritime environment (ruggedized hardware, intermittent satellite connectivity, and strict offline requirements).

## Upstream dependency
Use the completed Stage 09 Physical Persistence Topology, Stage 10 Target C4 Container View, and Stage 08 Selected Solution (ADR-001).

## Evidence to inspect
- `evidence/02_documents/fleet_operations_interview_notes.md`
- `evidence/01_enterprise_sources/source_inventory.csv`

## Case challenge
The topology must prove that the Vessel Edge is entirely self-sufficient for core operations, while the Shore Platform is optimized for heavy compute and historical analytics.

## Diagram Description (Physical & Network Topology)
*(Text-based representation)*
- **[Shore Data Center / Cloud]**
  - **Compute Cluster:** Kubernetes (or managed containers) hosting Ingestion ACL, NLP Workers, Context Assembler, and Fleet UI.
  - **Data Tier:** Enterprise Property Graph DB (Cluster), Vector DB, Object Storage (S3), Time-Series Audit DB.
  - **Network Edge:** MQTT Broker and API Gateway exposed to the internet.
- **[Satellite Communications Link]**
  - **Transport:** VSAT / LEO (e.g., Starlink Maritime, Inmarsat FleetXpress). High latency, intermittent, bandwidth-constrained.
  - **Protocol:** MQTT over TLS. QoS 1 for standard sync, QoS 2 for critical CMMS alerts.
- **[Vessel Edge Environment]**
  - **Hardware:** Ruggedized Marine IPC (e.g., Intel Core i7, 16GB RAM, 512GB NVMe SSD). No internet access.
  - **Compute:** Docker containers hosting Edge Graph Store (SQLite/RocksDB), Deterministic Engine, Master UI, and MQTT Client.
  - **Local Network:** Connects to vessel NMEA 0183/2000 telemetry gateways and local CMMS nodes.

## Working scaffold (Deployment Specifications)

| Component | Shore Deployment | Vessel Edge Deployment | Rationale / Constraint | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **Canonical Store** | Managed Enterprise Graph DB (High Availability) | Embedded SQLite + Custom Graph Index | Shore needs ACID/clustering. Edge needs zero-footprint, read-optimized local storage. | `graph-persistence-architecture.md` |
| **Semantic Context** | Managed Vector Database | **NONE** (Disabled) | Edge lacks compute for embedding/search. Falls back to cached Graph facts only. | `hybrid-retrieval-architecture.md` |
| **NLP Extraction** | Worker calling External LLM API | **NONE** (Prohibited) | Edge must operate offline. LLM calls require internet. | `model-routing-design.md` |
| **Audit Log** | Time-Series DB (Infinite retention) | Local SQLite (Rolling 30-day buffer) | Edge buffers locally; Shore