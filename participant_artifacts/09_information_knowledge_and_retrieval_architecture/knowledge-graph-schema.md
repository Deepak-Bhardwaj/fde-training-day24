# Knowledge Graph Schema

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer C: Connected Knowledge)
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To define the property graph schema (Nodes, Edges, and Properties) that will store the connected knowledge. This schema enables the deterministic engine to traverse relationships (e.g., Voyage -> Disruption -> Constraint) efficiently.

## Upstream dependency
Use the completed Stage 09 Ontology and Semantic Constraints.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
The graph schema must natively support temporal provenance and authority weighting on the *edges*, not just the nodes, to handle conflicting constraints from different sources.

## Minimum content

### Node Labels (Entities)
- **`Vessel`**: `canonical_id`, `name`, `imo_number`
- **`Voyage`**: `voyage_id`, `schedule_status`, `origin`, `destination`
- **`Disruption`**: `disruption_id`, `event_type`, `severity`, `detected_at`
- **`Constraint`**: `constraint_id`, `type` (PORT/CMMS/CARGO), `status`, `authority_weight`
- **`PolicyRule`**: `rule_id`, `text`, `version`, `status` (ACTIVE/SUPERSEDED)
- **`RecoveryOption`**: `option_id`, `feasibility_score`, `ai_draft_flag`, `status`

### Relationship Types (Edges) & Properties
- **`[:OPERATES_ON]`**: Vessel -> Voyage. *Properties:* `valid_from`, `valid_until`.
- **`[:ENCOUNTERS]`**: Voyage -> Disruption. *Properties:* `detected_at`, `source_id`.
- **`[:CONSTRAINED_BY]`**: Voyage/RecoveryOption -> Constraint. *Properties:* `authority_weight`, `valid_until`, `source_version`. (Crucial for handling GS-05 stale data).
- **`[:GOVERNS]`**: PolicyRule -> RecoveryOption. *Properties:* `policy_version`.
- **`[:MITIGATED_BY]`**: Disruption -> RecoveryOption. *Properties:* `status` (DRAFT/APPROVED), `master_approval_ts`.

### Graph-Specific Indexes
- **Temporal Index:** On `valid_until` for all `[:CONSTRAINED_BY]` edges to enable rapid expiration filtering.
- **Authority Index:** On `authority_weight` to quickly resolve semantic conflicts (e.g., SRC-PORT Notice vs API).

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Edges must carry temporal and authority properties to resolve conflicts. | `fleet_operations_interview_notes.md` (semantic conflicts) | `semantic-constraints.md` (SC-01, SC-02) | High confidence (architectural necessity). |
| Policy rules must be explicitly linked to options they govern. | `source_authority.yaml` | `ontology.md` | High confidence (explicit policy). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The chosen graph database supports efficient multi-property edge indexing for temporal queries. | Graph DB vendor selection pending (Stage 09 Property Graph vs RDF ADR). | Shore Platform Team | If unsupported, query performance for freshness checks will degrade. | Stage 09 Property Graph vs RDF ADR. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture