# Handoff Protocol

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 11 — Agentic & Multi-Agent Orchestration
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
Is autonomy justified, bounded, permissioned, interruptible and testable?

## Why this artifact exists
To define the strict, asynchronous protocol for handing off control and state between the Shore Orchestrator, the Vessel Edge, and Human operators, ensuring no data is lost and no unauthorized actions occur during network partitions.

## Upstream dependency
Use the completed Stage 11 Shared-Memory Design, Stage 10 API Contracts, and Stage 09 Event/State/Temporal Model.

## Evidence to inspect
- `Participant_Case_Study.md` (GS-14: Prolonged satellite blackout, GS-15: Reconnect reconciliation)
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
The handoff protocol must be resilient to intermittent connectivity. It cannot rely on synchronous, blocking HTTP calls between shore and vessel.

## Minimum content

### 1. Shore-to-Vessel Handoff (Constraint Updates)
- **Trigger:** New `Constraint` or `PolicyRule` validated in Shore Canonical Graph.
- **Mechanism:** Shore Orchestrator publishes a `GraphMutationEvent` to the MQTT Broker.
- **Payload:** Compressed Protobuf containing `entity_id`, `action` (CREATE/UPDATE/DELETE), `valid_until`, and `source_version`.
- **Vessel Action:** Vessel Edge MQTT Client receives event, validates signature, and applies idempotent update to the local Edge Graph Store. Acknowledges receipt.

### 2. Vessel-to-Shore Handoff (Execution & Approval)
- **Trigger:** Master approves a `RecoveryOption` via Vessel Edge UI.
- **Mechanism:** Vessel Edge generates a `PlanApproved` domain event, signs it with the Master's identity token, and writes to the Local Audit Buffer.
- **Sync:** If online, publishes immediately via MQTT (QoS 2). If offline (GS-14), stores locally.
- **Reconnect (GS-15):** Upon `ConnectivityRestored`, the Vessel Edge flushes the Local Audit Buffer to the Shore Audit Log. The Shore Orchestrator updates the Canonical Graph to reflect the `EXECUTED` state.

### 3. Human-to-System Handoff (HITL & Approval)
- **Fleet Controller:** Reviews HITL queue. Clicks "Approve". System transitions state from `DRAFT` to `FEASIBLE` and publishes to Master UI.
- **Master:** Reviews option. Clicks "Approve" (with procedural/crypto sign-off). System transitions state to `APPROVED` and triggers execution.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Vessel-to-shore handoff must be asynchronous and queue locally during blackouts. | `fleet_operations_interview_notes.md` | `graph-persistence-architecture.md` | High confidence (SME interview). |
| Master approval requires cryptographic/procedural sign-off to prevent spoofing (GS-08). | `role_authorization_matrix.csv` | `identity-permission-matrix.md` | High confidence (explicit policy). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The MQTT broker can handle the burst of queued events from multiple vessels reconnecting simultaneously after a widespread sat-com outage. | Broker burst-load testing NOT RUN. | Shore Platform Team | May require implementing exponential backoff and rate-limiting on the vessel-side MQTT client. | Stage 10 Failure-Mode Design. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved, bounded and testable agentic architecture