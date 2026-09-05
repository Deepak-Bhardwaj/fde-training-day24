# Graph Logical Model

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer D: Graph Data Platform)
**Participant status:** COMPLETED
**Deliverable form:** Diagram + supporting table + rationale

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To translate the conceptual Entity/Relationship Model into a strict, implementation-ready logical model, defining exact data types, mandatory properties, uniqueness constraints, and indexes for the Property Graph database.

## Upstream dependency
Use the completed Stage 09 Entity/Relationship Model and ADR-005 (Property Graph).

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
Define the physical constraints that will prevent invalid data from entering the graph, enforcing the semantic constraints at the database level.

## Working scaffold (Node & Edge Specifications)

### Node Specifications
| Node Label | Mandatory Properties (Type) | Uniqueness Constraint | Indexes | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **Vessel** | `canonical_id` (String), `imo_number` (String) | `canonical_id` | `imo_number` | `source_authority.yaml` |
| **Constraint** | `constraint_id` (String), `type` (Enum), `status` (Enum) | `constraint_id` | `type`, `status` | `canonical-entity-model.md` |
| **PolicyRule** | `rule_id` (String), `version` (Int), `status` (Enum) | `rule_id` + `version` | `status` | `source_authority.yaml` |
| **EvidenceRecord** | `record_id` (String), `raw_payload_hash` (String), `ingestion_ts` (DateTime) | `record_id` | `raw_payload_hash` | `provenance-evidence-linkage-model.md` |

### Edge Specifications
| Relationship Type | Start Node | End Node | Mandatory Properties (Type) | Indexes | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CONSTRAINED_BY** | Voyage / RecoveryOption | Constraint | `authority_weight` (Enum), `valid_until` (DateTime) | Composite: `valid_until`, `authority_weight` | `semantic-constraints.md` |
| **GOVERNS** | PolicyRule | RecoveryOption | `policy_version` (Int) | None | `ontology.md` |
| **DERIVED_FROM** | Constraint / PolicyRule | EvidenceRecord | `extraction_confidence` (Float) | None | `provenance-evidence-linkage-model.md` |

### Database Constraints & Triggers
1. **Temporal Expiration Trigger:** A scheduled job runs every 60 seconds to update the `status` of any `Constraint` node to `EXPIRED` if `current_time > MAX(valid_until)` across its incoming `[:CONSTRAINED_BY]` edges.
2. **Authority Write Constraint:** The database will reject any write to a `Constraint` node if the incoming `authority_weight` is lower than the existing node's `authority_weight` (enforcing SC-01).

## Rationale
By pushing constraints like uniqueness and authority precedence down to the database level, we reduce the burden on the application-level ACL and guarantee data integrity even if the application logic is bypassed or buggy.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Database-level constraints are required to enforce authority precedence (SC-01). | `semantic-constraints.md` | `target-information-trust-boundaries.md` | High confidence (security best practice). |
| Temporal expiration must be handled efficiently to prevent stale data in traversals. | `source_inventory.csv` (freshness thresholds) | `provenance-baseline.md` | High confidence (architectural necessity). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The chosen Property Graph DB supports composite indexes on edge properties for efficient temporal filtering. | Vendor feature matrix not fully verified (NOT RUN). | Shore Platform Team | If unsupported, the engine must pull all edges and filter in application memory, degrading performance. | Stage 09 Graph Query / Traversal Patterns. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture