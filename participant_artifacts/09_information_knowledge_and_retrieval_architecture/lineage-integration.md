# Lineage Integration

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer G: Metadata / Lineage / Provenance)
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To define how data lineage is automatically captured, stored, and exposed throughout the pipeline, ensuring that every decision can be traced back to its exact source, transformation, and evaluation.

## Upstream dependency
Use the completed Stage 06 Lineage and Stage 09 Provenance/Evidence Linkage Model.

## Evidence to inspect
- `evidence/02_documents/fleet_operations_interview_notes.md`
- `evidence/04_policy_authority/role_authorization_matrix.csv`

## Case challenge
Lineage cannot be an afterthought or a manual process. It must be baked into the ingestion ACL, the deterministic engine, and the audit logging mechanisms.

## Minimum content

### 1. Lineage Capture Points
- **Ingestion:** When raw data enters the ACL, an `EvidenceRecord` is created, capturing `source_id`, `raw_payload_hash`, and `ingestion_ts`.
- **Transformation:** When the NLP extractor or mapping rules convert raw data to a canonical `Constraint`, a `[:DERIVED_FROM]` edge is created, capturing the `transformer_version` and `extraction_confidence`.
- **Evaluation:** When the deterministic engine evaluates a `RecoveryOption`, it generates an `[:ATTESTED_BY]` edge linking the option to all `EvidenceRecord` nodes that influenced the feasibility score.
- **Execution:** When the Master approves, the `PlanApproved` event captures the `master_id` and `vessel_state_hash`, closing the lineage loop.

### 2. Lineage Storage Strategy
- **Operational Lineage:** Stored as explicit edges (`[:DERIVED_FROM]`, `[:ATTESTED_BY]`) in the Property Graph for fast, real-time traversal during feasibility checks.
- **Historical Lineage:** Periodically exported to an immutable, append-only Audit Log Store (e.g., time-series DB or blockchain ledger) for long-term regulatory compliance (ISM Code).

### 3. Lineage Query API
- Provides a `GET /lineage/{entity_id}` endpoint for the Fleet Controller UI and Safety Officers.
- Returns a JSON tree showing the full ancestry of a decision, including source freshness and transformation confidence at each step.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Lineage must link the final outcome back to the original source freshness to satisfy audit requirements. | `fleet_operations_interview_notes.md` | `oversight-transparency-requirements.md` (OT-03) | High confidence (SME interview). |
| Operational lineage must be stored in the graph for real-time access, while historical lineage goes to an immutable store. | `bounded-contexts.md` (Compliance & Audit Context) | `graph-persistence-architecture.md` | High confidence (architectural best practice). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The `GET /lineage/{entity_id}` API can assemble the full ancestry tree in < 100ms for complex, multi-hop decisions. | Lineage query performance is NOT RUN. | Shore Platform Team | If too slow, the UI may need to display lineage in paginated chunks or pre-compute common paths. | Stage 10 API Contracts. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture