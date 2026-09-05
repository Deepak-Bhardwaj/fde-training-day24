# Architecture ADRs

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 10 — AI & Application Architecture
**Participant status:** COMPLETED
**Deliverable form:** ADR / decision record

## Stage question
How will the AI-enabled application consume context, integrate, deploy and fail safely?

## Why this artifact exists
To formally record the final, critical architectural decisions regarding the application layer, deployment, and integration patterns that bring the information architecture to life.

## Upstream dependency
Use all completed Stage 10 artifacts.

## Evidence to inspect
- `Participant_Case_Study.md` (Non-negotiable constraints)
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
These ADRs must justify the complexity of the hybrid deployment and the strict isolation of AI components against the reality of maritime operations.

## Minimum content

### ADR-016: MQTT Event Sourcing over VSAT for Vessel-to-Shore Sync
- **Status:** Accepted
- **Context:** The vessel operates in environments with prolonged, unpredictable satellite blackouts (GS-14). Traditional REST/HTTP polling or database replication fails completely when the network is partitioned for days.
- **Decision:** Adopt MQTT (QoS 1/2) over the sat-com link for event-sourced delta sync. The shore publishes graph mutations; the vessel consumes them and queues its own local mutations (e.g., Master approvals) for replay upon reconnect.
- **Consequences:** (+) Highly resilient to intermittent connectivity. (+) Guarantees safe reconciliation after blackouts (GS-15). (-) Requires strict idempotency and deterministic hashing across both zones.
- **Evidence:** `api-contracts.md`, `event-state-temporal-model.md`

### ADR-017: Vessel Edge Compute Profile (No AI / No Vector Search)
- **Status:** Accepted
- **Context:** The vessel edge must operate autonomously on constrained, ruggedized hardware without internet access. Running LLM inference or vector similarity searches locally is computationally prohibitive and introduces unmanageable hallucination risks offline.
- **Decision:** The Vessel Edge container profile is strictly limited to the Embedded Graph Store, Deterministic Engine, Master UI, and MQTT Client. AI/NLP and Vector components are deployed exclusively on the Shore Platform.
- **Consequences:** (+) Guarantees offline continuity (CTQ-04) and zero hallucination risk on the vessel. (+) Minimizes hardware footprint and power consumption. (-) Vessel edge cannot process new unstructured port notices while offline; must rely on last known shore-synced state.
- **Evidence:** `deployment-topology.md`, `model-routing-design.md`

### ADR-018: 6-Month API Backward Compatibility for Vessel Software
- **Status:** Accepted
- **Context:** Vessel software updates require physical deployment or complex over-the-air (OTA) updates that are often delayed due to port schedules, crew availability, or safety approvals. The Shore Platform will evolve much faster than the Vessel Edge.
- **Decision:** All Shore-to-Vessel APIs and MQTT payloads must maintain strict backward compatibility for a minimum of 6 months after a new version is deployed. The Shore Platform must support older vessel edge versions concurrently.
- **Consequences:** (+) Prevents "bricking" vessel operations due to failed or delayed OTA updates. (+) Allows shore to iterate rapidly on NLP and analytics without risking vessel stability. (-) Increases the maintenance burden on the Shore Platform to support multiple API schema