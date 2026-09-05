# Graph Query / Traversal Patterns

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer D: Graph Data Platform)
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To define the exact traversal patterns the deterministic engine will use to query the Knowledge Graph for real-time feasibility checking, ensuring that temporal validity and authority weights are enforced at the database level.

## Upstream dependency
Use the completed Stage 09 Entity/Relationship Model, Graph Logical Model, and Semantic Constraints.

## Evidence to inspect
- `evidence/04_policy_authority/source_authority.yaml`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
Queries must be highly optimized for the deterministic engine. A feasibility check cannot afford to scan the entire graph; it must use targeted traversals with strict filtering predicates.

## Minimum content

| Pattern ID | Query Purpose | Start Node | Traversal Path | Filter Predicates | Golden Scenario Link | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **GQ-01** | **Core Feasibility Check** | `RecoveryOption` | `[:CONSTRAINED_BY]->(Constraint)` | `WHERE edge.valid_until > current_time() AND edge.authority_weight >= 'MEDIUM' AND node.status != 'EXPIRED'` | GS-05 (Stale data) | `semantic-constraints.md` (SC-02) |
| **GQ-02** | **Technical Hold Block** | `RecoveryOption` | `[:CONSTRAINED_BY]->(Constraint)` | `WHERE node.type = 'CMMS_HOLD' AND node.status = 'ACTIVE'` -> **Immediate INFEASIBLE** | GS-03 (Critical machinery hold) | `business-rules.md` (BR-02) |
| **GQ-03** | **Policy Governance Check** | `RecoveryOption` | `[:GOVERNS]<-(PolicyRule)` | `WHERE node.status = 'ACTIVE'` | GS-12 (Superseded policy trap) | `source_authority.yaml` |
| **GQ-04** | **Provenance Reconstruction** | `RecoveryOption` | `[:ATTESTED_BY]->(EvidenceRecord)` | `WHERE edge.evaluation_ts IS NOT NULL` | N/A (Audit) | `provenance-evidence-linkage-model.md` |
| **GQ-05** | **Identity Conflict Resolution** | `Vessel` | `[:OBSERVED_BY]<-(AIS_Observation)` | `WHERE edge.confidence_score < 0.95` -> Flag for Controller | GS-04 (Identity ambiguity) | `entity-resolution-specification.md` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| GQ-02 must short-circuit the feasibility check if an active CMMS hold is found. | `business-rules.md` (BR-02) | `go-no-go-kill-criteria.md` | High confidence (non-negotiable constraint). |
| GQ-03 must strictly filter by `status = 'ACTIVE'` to prevent retrieval traps. | `source_authority.yaml` | `quality-profile.md` | High confidence (explicit policy). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The graph DB query planner will efficiently use the composite edge index for GQ-01 without scanning unrelated edges. | Live query plan analysis is NOT RUN. | Shore Platform Team | If the planner fails to use the index, query latency will exceed the <50ms SLA. | Stage 09 Graph Indexing Strategy. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture