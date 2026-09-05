# Orchestration Topology

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 11 — Agentic & Multi-Agent Orchestration
**Participant status:** COMPLETED
**Deliverable form:** Diagram + supporting table + rationale

## Stage question
Is autonomy justified, bounded, permissioned, interruptible and testable?

## Why this artifact exists
To define the actual mechanism that coordinates the steps of the disruption recovery workflow, proving that a deterministic orchestrator is used instead of a probabilistic multi-agent framework.

## Upstream dependency
Use the completed Stage 11 Agent Responsibility Map and Stage 10 Target C4 Container View.

## Evidence to inspect
- `Participant_Case_Study.md` (Non-negotiable constraints)
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
Clearly distinguish between "Orchestration" (deterministic sequencing of predefined steps) and "Agentic Orchestration" (autonomous goal-seeking, dynamic tool selection, and multi-agent negotiation).

## Diagram Description (Deterministic Orchestration Topology)
*(Text-based representation)*
- **Trigger:** `DisruptionDetected` event.
- **Orchestrator (Shore):** Deterministic Workflow Engine (e.g., Temporal, Airflow, or custom state machine).
  - Step 1: Call Context Assembler API (fetch active subgraph).
  - Step 2: Call Deterministic Engine (generate feasible options).
  - Step 3: If NLP extraction confidence < 0.95, pause workflow and route to HITL Queue.
  - Step 4: Publish `RecoveryOptionsGenerated` event to Fleet Controller UI.
- **Human Intervention:** Fleet Controller reviews, selects an option.
- **Orchestrator (Vessel Edge):** Local Event-Driven State Machine.
  - Step 1: Receive selected option via MQTT.
  - Step 2: Present to Master UI.
  - Step 3: Await `PlanApproved` event (cryptographic/procedural sign-off).
  - Step 4: Log to Local Audit Buffer.

## Working scaffold (Orchestrator vs. Agent Comparison)

| Feature | Deterministic Orchestrator (Selected) | Multi-Agent Framework (Rejected) | Rationale for Selection | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **Execution Path** | Predefined, explicit state machine. | Dynamic, emergent, LLM-directed. | Predictability is required for safety audits. | `autonomy-level-adr.md` |
| **Tool Use** | Explicit, hardcoded API calls. | Autonomous, LLM-decided tool selection. | Prevents hallucinated or unauthorized API calls (GS-08). | `model-routing-design.md` |
| **Interruptibility** | Immediate halt on human input or timeout. | Difficult to reliably interrupt mid-reasoning. | Master veto must be absolute and immediate. | `role_authorization_matrix.csv` |
| **Testability** | 100% reproducible given same inputs. | Probabilistic, non-deterministic outputs. | Required for Stage 07 Golden Scenario testing. | `evaluation-strategy.md` |
| **Offline Capability** | Lightweight, runs on vessel edge. | Heavy compute, requires cloud LLM APIs. | Violates CTQ-04 (Offline Continuity). | `deployment-topology.md` |

## Rationale
By explicitly choosing a Deterministic Orchestrator over a Multi-Agent Framework, the architecture guarantees that every step of the recovery process is predefined, permissioned, interruptible, and 100% testable. This directly satisfies the Stage 11 exit criteria while adhering to the non-negotiable constraint that AI cannot replace human authority.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Deterministic orchestration is required to ensure 100% testability against Golden Scenarios. | `evaluation-strategy.md` | `agent-suitability-assessment.md` | High confidence (architectural necessity). |
| Multi-agent frameworks are rejected due to offline and predictability constraints. | `ctqs.md`, `Participant_Case_Study.md` | `orchestration-topology.md` | High confidence (explicit mandate). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The chosen deterministic orchestrator (e.g., Temporal) can be successfully deployed and maintained on the vessel edge IPC. | Edge deployment of workflow engines NOT RUN. | Shore Platform Team | If too heavy, the vessel edge must use a simpler, custom event-driven state machine. | Stage 10 Deployment Topology. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved, bounded and testable agentic architecture