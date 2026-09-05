# State-Machine Model

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 11 — Agentic & Multi-Agent Orchestration
**Participant status:** COMPLETED
**Deliverable form:** Diagram + supporting table + rationale

## Stage question
Is autonomy justified, bounded, permissioned, interruptible and testable?

## Why this artifact exists
To define the strict, deterministic state transitions for the core operational entity (`RecoveryOption`). This ensures the system cannot enter invalid or unsafe states (e.g., executing a plan without Master approval).

## Upstream dependency
Use the completed Stage 09 Runtime Entity State Model and Stage 11 Autonomy-Level ADR.

## Evidence to inspect
- `evidence/04_policy_authority/role_authorization_matrix.csv`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
Every state transition must have an explicit guard (a required identity, a required system state, or a required human action). No transition can be triggered autonomously by the system.

## Diagram Description (RecoveryOption State Machine)
*(Text-based representation)*
- **[DRAFT]** --(Engine generates)--> **[FEASIBLE]**
- **[DRAFT]** --(Engine fails check)--> **[INFEASIBLE]**
- **[FEASIBLE]** --(Controller selects)--> **[PENDING_APPROVAL]**
- **[PENDING_APPROVAL]** --(Master signs)--> **[APPROVED]**
- **[PENDING_APPROVAL]** --(Master vetoes)--> **[REJECTED]**
- **[APPROVED]** --(Vessel systems confirm)--> **[EXECUTED]**

## Working scaffold (State Transitions & Guards)

| Current State | Target State | Trigger / Action | Mandatory Guard / Pre-condition | Allowed Actor | Evidence |
| :--- | :--- | :--- | :--- | :--- |