# Stakeholder and Affected-Groups Map

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench

**Stage:** 01 — Mandate & Field Immersion

**Participant status:** COMPLETED

**Deliverable form:** Structured analysis / specification

## Stage question
Why are we here, what outcome matters, who owns it, and who is affected?

## Why this artifact exists
This artifact is part of the evidence needed to reach **Approved mandate and operating context**. It must be consistent with approved upstream artifacts; do not silently redefine earlier facts, semantics, thresholds or decision rights.

## Upstream dependency
Use the case pack and supplied evidence. No solution architecture is an input to Stage 01.

## Evidence to inspect
- `evidence/04_policy_authority/role_authorization_matrix.csv`
- `evidence/02_documents/fleet_operations_interview_notes.md`
- `evidence/01_enterprise_sources/source_inventory.csv`

## Case challenge
Stay in the field problem and ownership space. Do not propose a model, graph database, agent or UI in this artifact.

## Minimum content

| Stakeholder Group | Role & Context | Primary Interest / Goal | Authority Level | Impact of Workbench |
| :--- | :--- | :--- | :--- | :--- |
| **Master & Bridge Team** | Vessel Command | Safe navigation, crew safety, final decision-making. | **Absolute** (Navigational & Safety) | **Direct:** Receives structured recovery options. System must never override their commands. |
| **Chief Engineer** | Vessel Technical | Machinery reliability, maintenance execution. | **Absolute** (Technical Release) | **Direct:** Their maintenance holds act as hard constraints. System must respect technical holds absolutely. |
| **Fleet Controller / Voyage Planner** | Shore Operations | Schedule adherence, commercial efficiency, fuel optimization. | **High** (Commercial / Routing) | **Direct:** Uses workbench to evaluate schedule impacts. Needs concise evidence-backed comparisons, not chatbot conversations. |
| **Safety & Compliance (Shore)** | Governance & Policy | Regulatory adherence, policy enforcement, auditability. | **High** (Policy & Governance) | **Direct:** Owns active policy repository. Audits workbench decision traces and post-event learning. |
| **Shore Platform Team** | IT / Infrastructure | System uptime, secure connectivity, offline-sync reliability. | **High** (Technical Architecture) | **Direct:** Responsible for deploying workbench and ensuring vessel-to-shore state reconciliation. |
| **Port Operations** | External / Port Authority | Berth allocation, pilotage scheduling, port safety. | **External** (Port Constraints) | **Indirect:** Receives updated ETAs. System must handle conflicting API vs signed notice semantics. |
| **Cargo / Commercial Ops** | Shore Commercial | Cargo integrity, delivery windows, customer priorities. | **Medium** (Commercial Priority) | **Indirect:** Workbench factors cargo constraints into recovery options without overriding safety. |
| **Vessel Crew** | Subject to rest hours and availability. | Crew welfare, rest compliance. | **Low** (Operational Constraint) | **Indirect:** System must respect crew rest constraints. AI is strictly prohibited from making personnel decisions. |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Controllers want concise evidence-backed recovery comparison, not a chatbot. | `fleet_operations_interview_notes.md` (Line: "Operators want a concise evidence-backed recovery comparison, not a chatbot conversation") | `scope.md` | High