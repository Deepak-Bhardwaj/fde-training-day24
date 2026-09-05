# Entity / Relationship Model

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer C: Connected Knowledge)
**Participant status:** COMPLETED
**Deliverable form:** Diagram + supporting table + rationale

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To provide a detailed, implementation-ready mapping of the entities and their relationships within the Knowledge Graph, ensuring the deterministic engine can efficiently traverse the model to evaluate recovery options.

## Upstream dependency
Use the completed Stage 09 Knowledge Graph Schema and Ontology.

## Evidence to inspect
- `evidence/04_policy_authority/source_authority.yaml`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
The model must explicitly support the "Constraint Hierarchy" defined in the ontology, allowing the engine to quickly identify if a lower-tier constraint (e.g., Cargo Window) is being improperly prioritized over a higher-tier constraint (e.g., CMMS Hold).

## Diagram Description (Logical ER Model)
*(Text-based representation of the core graph topology)*
- **(Vessel)** -[:OPERATES_ON {valid_from, valid_until}]-> **(Voyage)**
- **(Voyage)** -[:ENCOUNTERS {detected_at, source_id}]-> **(Disruption)**
- **(Voyage)** -[:CONSTRAINED_BY {authority_weight, valid_until, source_version}]-> **(Constraint)**
- **(RecoveryOption)** -[:CONSTRAINED_BY {authority_weight, valid_until}]-> **(Constraint)**
- **(RecoveryOption)** -[:MITIGATED_BY {status, master_approval_ts}]-> **(Disruption)**
- **(PolicyRule)** -[:GOVERNS {policy_version}]-> **(RecoveryOption)**
- **(Master)** -[:APPROVES {approval_ts, vessel_state_hash}]-> **(RecoveryOption)**
- **(ChiefEngineer)** -[:RELEASES {release_ts, maintenance_report_ref}]-> **(Constraint)**

## Working scaffold (Relationship Traversal Patterns)

| Traversal Purpose | Start Node | Relationship Path | End Node | Filter / Condition | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Feasibility Check** | RecoveryOption | `[:CONSTRAINED_BY]` | Constraint | `WHERE valid_until > current_time AND authority_weight >= MEDIUM` | `semantic-constraints.md` (SC-02) |
| **Technical Hold Block** | RecoveryOption | `[:CONSTRAINED_BY]` | Constraint | `WHERE type = 'CMMS_HOLD' AND status = 'ACTIVE'` -> Immediate INFEASIBLE | `business-rules.md` (BR-02) |
| **Policy Compliance** | RecoveryOption | `[:GOVERNS