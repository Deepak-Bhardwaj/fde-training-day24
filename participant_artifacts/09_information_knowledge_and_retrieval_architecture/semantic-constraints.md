# Semantic Constraints

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer B: Semantic Foundation)
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To define the invariants and structural rules that must always hold true within the canonical semantic layer. These constraints are enforced by the database schema and the deterministic engine to prevent invalid state transitions.

## Upstream dependency
Use the completed Stage 05 Business Rules and Stage 09 Canonical Entity Model.

## Evidence to inspect
- `evidence/04_policy_authority/source_authority.yaml`
- `evidence/04_policy_authority/role_authorization_matrix.csv`

## Case challenge
These are not business rules (which govern operator behavior); these are *semantic constraints* (which govern data integrity and system logic).

## Minimum content

| Constraint ID | Semantic Invariant | Enforcement Mechanism | Violation Consequence | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **SC-01: Authority Precedence** | A canonical entity cannot be overwritten by a source with lower authority precedence. | ACL validates `source_authority.yaml` before write. | Write rejected; logged as `AuthorityConflict`. | `source_authority.yaml` |
| **SC-02: Temporal Freshness** | No `Constraint` node can be traversed by the deterministic engine if `current_time > valid_until`. | Engine applies temporal filter before feasibility check. | Constraint excluded from evaluation; marked `EXPIRED`. | `provenance-baseline.md` |
| **SC-03: Technical Hold Absolute** | If a `Constraint` has `type = CMMS_HOLD` and `status = ACTIVE`, any `RecoveryOption` linked to that asset is automatically `INFEASIBLE`. | Deterministic engine hard-codes this check. | Option feasibility score set to 0. | `business-rules.md` (BR-02) |
| **SC-04: Policy Status Gate** | A `PolicyRule` node can only be linked via a `[:GOVERNS]` edge if its `status = ACTIVE`. | Graph write constraint / Engine filter. | Link rejected; rule ignored in feasibility check. | `source_authority.yaml` |
| **SC-05: Identity Canonical** | A `Vessel` node must have exactly one `canonical_id` sourced from `SRC-FMS`. | Schema uniqueness constraint. | Ingestion of conflicting AIS identity rejected as canonical; stored only as observation. | `source_authority.yaml` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| SC-03 is a hard semantic constraint, not just a business guideline. | `business-rules.md` (BR-02) | `go-no-go-kill-criteria.md` | High confidence (explicit non-negotiable constraint). |
| Temporal validity is a structural requirement of the semantic layer. | `provenance-baseline.md` | `canonical-identifier-strategy.md` | High confidence (architectural mandate). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The graph database supports native temporal constraints (valid_from/valid_until) without requiring complex custom triggers. | Graph DB vendor capabilities not fully benchmarked. | Shore Platform Team | May require application-level temporal filtering, increasing engine latency. | Stage 09 Graph Query / Traversal Patterns. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture