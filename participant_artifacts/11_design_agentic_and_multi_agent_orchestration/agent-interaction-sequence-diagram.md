# Agent Interaction / Sequence Diagram

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 11 — Agentic & Multi-Agent Orchestration
**Participant status:** COMPLETED
**Deliverable form:** Diagram + supporting table + rationale

## Stage question
Is autonomy justified, bounded, permissioned, interruptible and testable?

## Why this artifact exists
To map the exact sequence of interactions between the Deterministic Orchestrator, the Bounded NLP Service (the only "agent-like" component), the Human-in-the-Loop (Fleet Controller), and the Master. This proves that no autonomous, multi-agent negotiation occurs.

## Upstream dependency
Use the completed Stage 11 Orchestration Topology and Stage 10 Target C4 Component View.

## Evidence to inspect
- `Participant_Case_Study.md` (Non-negotiable constraints)
- `evidence/04_policy_authority/role_authorization_matrix.csv`

## Case challenge
Show exactly where the human interrupts, reviews, and approves the workflow. The sequence must prove that the system cannot bypass the Master's authority.

## Diagram Description (Sequence Flow)
*(Text-based representation of the interaction sequence)*
1. **Trigger:** `DisruptionDetected` event received by **Deterministic Orchestrator**.
2. **Orchestrator** calls **Context Assembler** -> Returns Active Subgraph.