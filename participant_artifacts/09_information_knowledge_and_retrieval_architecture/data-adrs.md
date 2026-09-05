# Data ADRs

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer I: Architecture Decisions / Schemas)
**Participant status:** COMPLETED
**Deliverable form:** ADR / decision record

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To formally record the critical architectural decisions regarding data storage, movement, and polyglot persistence that underpin the information architecture.

## Upstream dependency
Use the completed Stage 09 Physical Persistence Topology and Target Data Architecture.

## Evidence to inspect
- `evidence/02_documents/fleet_operations_interview_notes.md`
- `Participant_Runbook.md`

## Case challenge
Ensure these ADRs explicitly justify the complexity of a polyglot system against the non-negotiable constraints of the maritime domain.

## Minimum content

### ADR-006: Polyglot Persistence over Single-Database Monolith
- **Status:** Accepted
- **Context:** The system must handle structured relational facts (Constraints), unstructured semantic context (Policies/Precedents), massive raw payloads (Telemetry/PDFs), and immutable audit logs. A single database type cannot efficiently handle all four without severe performance or cost penalties.
- **Decision:** Adopt Polyglot Persistence: Property Graph (Facts), Vector DB (Semantics), Object Storage (Raw), Time-Series DB (Audit).
- **Consequences:** (+) Each store is optimized for its specific workload. (+) Prevents graph bloat from raw telemetry. (-) Increases operational complexity and requires robust data contracts between stores.
- **Evidence:** `target-data-architecture.md`, `provenance-evidence-linkage-model.md`

### ADR-007: Event-Sourced Delta Sync for Vessel Edge
- **Status:** Accepted
- **Context:** The vessel edge must maintain an up-to-date "Active Subgraph" despite prolonged, unpredictable satellite blackouts (GS-14). Traditional database replication (e.g., primary-replica) fails completely when the network is partitioned for days.
- **Decision:** The shore platform publishes all graph mutations as an immutable event stream. The vessel edge consumes these events and applies them idempotently. During a blackout, the edge queues its own local mutations (e.g., Master approvals) and replays them to the shore upon reconnect (GS-15).
- **Consequences:** (+) Guarantees safe reconciliation after blackouts. (+) Edge only stores the delta, saving storage. (-) Requires strict idempotency and deterministic hashing across both zones.
- **Evidence:** `graph-persistence-architecture.md`, `event-state-temporal-model.md`

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Polyglot persistence is required to separate raw evidence from canonical facts. | `provenance-evidence-linkage-model.md` | `graph-logical-model.md` | High confidence (architectural necessity). |
| Event-sourcing is the only viable pattern for offline-first maritime sync. | `fleet_operations_interview_notes.md` | `go-no-go-kill-criteria.md` (G-02) | High confidence (non-negotiable constraint). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The operations team has the skills to manage a polyglot stack (Graph + Vector + Time-Series). | Current Shore Platform Team skill set not fully detailed. | Executive Sponsor | May require targeted hiring or managed cloud services (e.g., Neo4j Aura, Pinecone) to reduce operational burden. | Stage 10 Deployment Topology. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture