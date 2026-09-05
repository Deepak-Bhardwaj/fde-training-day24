# Batch / Stream / Runtime Data Flows

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer H: Target Information Architecture)
**Participant status:** COMPLETED
**Deliverable form:** Diagram + supporting table + rationale

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To categorize and define the movement patterns of data across the system, ensuring that high-frequency telemetry does not starve the bandwidth of critical safety constraints, and that batch processes do not lock the operational graph.

## Upstream dependency
Use the completed Stage 09 Physical Persistence Topology and Retrieval Source Adapters.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/01_enterprise_sources/live_event_stream.jsonl`

## Case challenge
Explicitly separate the continuous, high-volume streams from the critical, low-volume runtime requests. The deterministic engine's runtime queries must never be blocked by batch ingestion or stream backpressure.

## Working scaffold (Flow Categorization)

| Flow Category | Data Sources / Triggers | Pattern | Transport / Mechanism | SLA / Priority | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **High-Freq Stream** | SRC-TELEM (Machinery/Fuel), SRC-AIS (Position) | Continuous Event Stream | MQTT / Kafka | Best-effort. Subject to deduplication and aggregation at the ACL. | `source_inventory.csv` |
| **Critical Event Stream** | SRC-CMMS (Maintenance Holds), SRC-PORT (Signed Notices) | Low-volume, High-criticality Events | MQTT (QoS 2) / HTTPS | **Highest Priority.** Guaranteed delivery. Triggers immediate Context Assembly update. | `business-rules.md` (BR-02) |
| **Batch Sync** | SRC-POLICY (Superseded docs), SRC-CREW (Rest hours) | Scheduled / Nightly | SFTP / Batch API | Low priority. Runs during off-peak hours. Isolated from operational graph. | `source_inventory.csv` |
| **Runtime Request** | Fleet Controller UI, Deterministic Engine | Request / Response | Internal gRPC / REST | **Strict Latency (<50ms).** Reads from cached Runtime Context Graph. | `acceptance-thresholds.md` |
| **Shore-to-Vessel Sync** | Shore Canonical Graph -> Vessel Edge Graph | Delta Event Stream | MQTT over Sat-com | Asynchronous. Queued during blackout, flushed upon `ConnectivityRestored`. | `graph-persistence-architecture.md` |

## Rationale
By categorizing flows, we can apply Quality of Service (QoS) routing. A critical CMMS hold (Critical Event) will bypass the queue and immediately update the vessel edge's active subgraph. Conversely, high-frequency telemetry (Stream) is aggregated and deduplicated at the edge of the network, preventing the sat-com link from being overwhelmed by redundant engine temperature readings.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Critical safety events (CMMS) must have guaranteed delivery over sat-com. | `business-rules.md` (BR-02) | `data-gap-register.md` (DG-01) | High confidence (non-negotiable safety constraint). |
| Runtime engine queries must be isolated from ingestion backpressure. | `fleet_operations_interview_notes.md` | `acceptance-thresholds.md` | High confidence (architectural best practice). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The MQTT broker can correctly prioritize QoS 2 (CMMS) over QoS 1 (Telemetry) during sat-com congestion. | Broker prioritization logic under extreme load NOT RUN. | Shore Platform Team | May require implementing custom application-level priority queues before the MQTT publisher. | Stage 10 Failure-Mode Design. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture