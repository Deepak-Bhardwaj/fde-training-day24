# Termination / Loop Controls

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 11 — Agentic & Multi-Agent Orchestration
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
Is autonomy justified, bounded, permissioned, interruptible and testable?

## Why this artifact exists
In autonomous agentic systems, "loop controls" prevent LLMs from getting stuck in infinite reasoning or tool-calling loops. In this **deterministic** architecture, loop controls translate to strict workflow timeouts, retry limits, and human interruptibility to prevent system hangs or resource exhaustion.

## Upstream dependency
Use the completed Stage 11 State-Machine Model, Stage 10 Model Routing Design, and Stage 10 Failure-Mode Design.

## Evidence to inspect
- `Participant_Case_Study.md` (Non-negotiable constraints)
- `evidence/01_enterprise_sources/source_inventory.csv`

## Case challenge
Explicitly state that autonomous agentic loops are NOT APPLICABLE, and define the deterministic termination conditions for the workflow orchestrator and bounded tools.

## Minimum content

### 1. Agentic Loop Controls: NOT APPLICABLE
Per the Stage 11 Agent Suitability Assessment, multi-agent frameworks and autonomous LLM reasoning loops are explicitly rejected for the core workflow. Therefore, traditional agentic loop controls (e.g., max reasoning steps, self-correction loops) are **NOT APPLICABLE**.

### 2. Deterministic Workflow Termination Controls
Instead of agentic loops, the Deterministic Orchestrator enforces strict termination boundaries:

| Workflow Step | Termination / Timeout Condition | Fallback Action on Termination | Evidence |
| :--- | :--- | :--- | :--- |
| **NLP Extraction** | Hard timeout of 30 seconds OR 3 consecutive HTTP 5xx errors. | Abort NLP. Route raw PDF directly to Fleet Controller HITL Queue. | `model-routing-design.md` |
| **Context Assembly** | Query exceeds 50ms SLA. | Return partial/cached subgraph with `STALE_DATA` warning flag to the Engine. | `context-assembly-model.md` |
| **Feasibility Checking** | Deterministic engine traversal exceeds 100ms. | Abort check. Mark `RecoveryOption` as `INFEASIBLE` (fail-safe). | `business-rules.md` |
| **Master Approval Wait** | No response from Master within defined operational window (e.g., 2 hours, depending on disruption severity). | Workflow remains in `PENDING_APPROVAL` state. System alerts Shore Fleet Controller to establish voice/radio contact with the vessel. | `role_authorization_matrix.csv` |

### 3. Human Interruptibility (The Ultimate Kill Switch)
At any point in the workflow, a human operator with the appropriate authority can terminate the process:
- **Fleet Controller:** Can manually cancel a `DRAFT` or `PENDING_APPROVAL` option at any time.
- **Master:** Holds absolute, immediate veto power (`REJECTED` state) over any proposed plan, instantly terminating the workflow for that option.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Agentic loop controls are NOT APPLICABLE because autonomous agents are not used. | `Participant_Runbook.md` | `agent-suitability-assessment.md` | High confidence (explicit training mandate). |
| The Master's veto acts as the ultimate, immediate termination control. | `role_authorization_matrix.csv` | `autonomy-level-adr.md` | High confidence (explicit policy). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The 30-second NLP timeout is sufficient for the largest expected Port Notice PDFs. | Large document processing latency NOT RUN. | Shore Platform Team | If insufficient, the NLP service must be refactored to process pages asynchronously. | Stage 10 Prompt / Context Design. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved, bounded and testable agentic architecture