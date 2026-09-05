# API Contracts

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 10 — AI & Application Architecture
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
How will the AI-enabled application consume context, integrate, deploy and fail safely?

## Why this artifact exists
To define the strict API contracts between the major application containers, ensuring that components can evolve independently without breaking the system, and that the vessel-to-shore sync protocol survives satellite blackouts.

## Upstream dependency
Use the completed Stage 09 Data Contracts, Stage 09 Retrieval Evidence Contract, and Stage 10 Target C4 Container View.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
APIs must be designed for the worst-case scenario: high latency, intermittent connectivity, and payload size constraints over satellite links.

## Minimum content

### 1. Shore-Internal APIs (gRPC / REST)
| API Endpoint | Method | Consumer | Producer | Payload | SLA | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `/v1/context/assemble` | POST | Deterministic Engine, Fleet UI | Context Assembler | Request: `{vessel_id, voyage_id}`. Response: Active Subgraph JSON. | < 50ms | `context-assembly-model.md` |
| `/v1/retrieval/query` | POST | Fleet Controller UI | Retrieval Router | Request: `{query_text, intent}`. Response: Graph facts + Vector context. | < 100ms | `retrieval-evidence-contract.md` |
| `/v1/ingestion/submit` | POST | Source Adapters | Ingestion ACL | Request: Raw payload + Provenance Envelope. Response: `evidence_id` or rejection. | < 200ms | `authority-freshness-metadata-profile.md` |
| `/v1/hitl/review` | GET/POST | Fleet Controller UI | HITL Review Queue | GET: Pending extractions. POST: Approve/Reject/Edit. | < 500ms | `knowledge-extraction-specification.md` |

### 2. Vessel-to-Shore Sync APIs (MQTT over Sat-com)
| Topic / Channel | Direction | Payload | QoS | Priority | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `vessel/{id}/graph-delta` | Shore -> Vessel | `GraphMutationEvent` (Node created, Edge updated) | QoS 1 | Medium | `graph-persistence-architecture.md` |
| `vessel/{id}/critical-alert` | Shore -> Vessel | Critical CMMS hold or Policy update | QoS 2 | **Highest** | `batch-stream-runtime-data-flows.md` |
| `vessel/{id}/execution-log` | Vessel -> Shore | `PlanApproved`, `PlanExecuted` events | QoS 1 | High | `domain-events.md` |
| `vessel/{id}/heartbeat` | Vessel -> Shore | Connectivity status, edge graph version | QoS 0 | Low | `physical-persistence-topology.md` |

### 3. API Versioning & Compatibility
- All APIs follow semantic versioning (`/v1/`, `/v2/`).
- **Backward Compatibility Rule:** The Shore Platform must support `v1` for at least 6 months after `v2` is deployed, because the Vessel Edge may be running an older version during prolonged deployments at sea.
- **Payload Compression:** All MQTT payloads over sat-com are compressed using Protocol Buffers (Protobuf) to minimize bandwidth usage.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Critical alerts (CMMS) must use QoS 2 for guaranteed delivery over sat-com. | `business-rules.md` (BR-02) | `batch-stream-runtime-data-flows.md` | High confidence (non-negotiable safety constraint). |
| API backward compatibility is mandatory due to vessel deployment cycles. | `fleet_operations_interview_notes.md` | `dependencies.md` | High confidence (SME interview). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: Protobuf compression reduces MQTT payload size by >50% compared to JSON. | Compression ratio benchmarking NOT RUN. | Shore Platform Team | If compression is insufficient, the sync protocol may need to implement delta-only diffing. | Stage 10 Deployment Topology. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Complete base AI/application architecture