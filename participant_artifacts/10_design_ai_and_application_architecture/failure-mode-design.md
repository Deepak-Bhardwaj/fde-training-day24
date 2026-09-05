# Failure-Mode Design

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 10 — AI & Application Architecture
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
How will the AI-enabled application consume context, integrate, deploy and fail safely?

## Why this artifact exists
To define how the system behaves when components fail, degrade, or are subjected to adversarial conditions. In maritime operations, systems must "fail safe" (prioritizing human authority and conservative constraints) rather than "fail fast" (crashing and leaving the crew blind).

## Upstream dependency
Use the completed Stage 07 Risk Treatment Plan, Stage 09 Context Freshness Policy, and Stage 10 Deployment Topology.

## Evidence to inspect
- `Participant_Case_Study.md` (Golden Scenarios GS-06, GS-10, GS-14)
- `evidence/04_policy_authority/role_authorization_matrix.csv`

## Case challenge
Every failure mode must have a deterministic fallback that preserves the Master's ability to make safe decisions, even if the system's automation is completely disabled.

## Minimum content

| Failure Mode | Detection Mechanism | System Impact | Fallback / Degradation Behavior | Golden Scenario | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Prolonged Sat-com Blackout** | MQTT heartbeat timeout (> 15 mins). | Shore cannot send updates; Vessel cannot sync logs. | **Vessel Edge:** Continues operating autonomously on cached "Active Subgraph". Flags UI as "OFFLINE MODE".<br>**Shore:** Queues all graph mutations. Replays upon reconnect (GS-15). | GS-14 | `fleet_operations_interview_notes.md`, `graph-persistence-architecture.md` |
| **External LLM API Outage** | HTTP 5xx / Timeout > 30s. | NLP extraction of Port Notice PDFs fails. | **Shore:** PDF is routed directly to the Fleet Controller HITL Review Queue for manual entry. Core deterministic engine is completely unaffected. | GS-10 | `model-routing-design.md`, `risk-treatment-plan.md` |
| **CMMS Data Staleness** | `current_time - observed_ts > 15 mins`. | System cannot verify if a critical maintenance hold has been released. | **Fail-Safe:** System assumes the hold is STILL ACTIVE. Blocks any recovery option involving that asset. Alerts Chief Engineer. | GS-03 | `context-freshness-policy.md`, `business-rules.md` |
| **Prompt Injection in Port Notice** | Sanitization regex detects injection patterns, OR LLM output fails JSON schema validation. | NLP extraction returns malicious or invalid payload. | **Shore:** Payload is discarded. Document flagged as `HIGH_RISK` and routed to HITL. Deterministic engine never sees the raw text. | GS-09 | `prompt-context-design.md`, `risk-treatment-plan.md` |
| **Vessel Edge Hardware Failure** | IPC watchdog timer / OS crash. | Master loses local decision-support UI. | **Fail-Safe:** Master reverts to manual, paper-based or legacy radio procedures. Shore platform continues tracking the vessel via AIS and attempts to establish voice comms. | GS-10 | `dependencies.md` |

## Rationale
This failure-mode design proves that the system is inherently resilient. Because the core feasibility engine is deterministic and the vessel edge is self-sufficient, the failure of cloud services (LLM, Vector DB) or network links (Sat-com) never results in a safety