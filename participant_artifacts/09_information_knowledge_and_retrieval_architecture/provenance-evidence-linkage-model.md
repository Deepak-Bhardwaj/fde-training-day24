# Provenance / Evidence Linkage Model

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer C: Connected Knowledge)
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To define how every node and edge in the Knowledge Graph is cryptographically and logically linked back to its raw, ingested evidence. This ensures that any decision can be fully reconstructed and audited, satisfying the "Decision Trace Completeness" KPI.

## Upstream dependency
Use the completed Stage 06 Provenance Baseline and Stage 09 Entity/Relationship Model.

## Evidence to inspect
- `evidence/02_documents/fleet_operations_interview_notes.md`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
Provenance cannot be an afterthought. The linkage model must guarantee that it is impossible to have a `Constraint` or `PolicyRule` in the graph without a verifiable link to the exact source document or telemetry payload that created it.

## Minimum content

### 1. The `EvidenceRecord` Node
Every piece of ingested raw data is stored as an immutable `EvidenceRecord` node.
- **Properties:** `record_id` (UUID), `source_id`, `raw_payload_hash` (SHA-256), `observed_ts`, `ingestion_ts`, `authority_weight`, `document_uri` (if applicable).

### 2. Linkage Relationships
- **`[:DERIVED_FROM]`**: Connects a canonical `Constraint`, `PolicyRule`, or `Disruption` node to its source `EvidenceRecord`.
  - *Properties:* `extraction_confidence` (for NLP), `transformer_version`.
- **`[:ATTESTED_BY]`**: Connects a `RecoveryOption` or `PlanApproved` event to the specific `EvidenceRecord` nodes that were evaluated during its generation.
  - *Properties:* `evaluation_ts`, `engine_version`.

### 3. Audit & Reconstruction Flow
1. **Query:** Safety Officer requests audit of `RecoveryOption` X.
2. **Traverse:** Follow `[:ATTESTED_BY]` edges from Option X to all `EvidenceRecord` nodes used.
3. **Verify:** Check `raw_payload_hash` against the original source system (or blob storage) to prove the data was not altered in transit.
4. **Context:** Follow `[:DERIVED_FROM]` edges from the `EvidenceRecord` nodes to the canonical