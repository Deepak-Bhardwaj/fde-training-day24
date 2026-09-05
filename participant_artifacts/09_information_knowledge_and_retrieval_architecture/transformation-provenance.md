# Transformation Provenance

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer G: Metadata / Lineage / Provenance)
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To define how the system tracks the exact logic, versions, and human interventions applied when transforming raw evidence into canonical knowledge. This ensures that if a canonical constraint is later found to be incorrect, the exact transformation step can be audited and rolled back.

## Upstream dependency
Use the completed Stage 09 Knowledge Extraction Specification, Source-to-Canonical Mapping, and Lineage Integration.

## Evidence to inspect
- `evidence/02_documents/fleet_operations_interview_notes.md`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
Transformations are not lossless. When an NLP model extracts a port constraint from a PDF, or an ACL maps a telemetry signal to a disruption, context is lost or altered. The system must record *how* the transformation occurred, not just the final result.

## Minimum content

### 1. Transformation Tracking Matrix
| Transformation Type | Source | Target | Tracked Metadata | Audit / Fallback Trigger | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **NLP Extraction** | Port Notice PDF | `Constraint` node | `nlp_model_version`, `extraction_confidence`, `raw_text_snippet` | If `confidence < 0.95`, flag for Human-in-the-Loop (HITL). | `knowledge-extraction-specification.md` |
| **ACL Semantic Mapping** | Port API JSON | `Constraint` node | `acl_rule_version`, `source_schema_version` | If source schema changes, mapping fails; alert Data Steward. | `source-to-canonical-mapping.md` |
| **Telemetry Aggregation** | SRC-TELEM Stream | `Disruption` node | `aggregation_window`, `deduplication_hash` | If duplicate hash detected, log as `Ignored_Duplicate`. | `canonical-identifier-strategy.md` |
| **Human-in-the-Loop (HITL)** | Controller Review | `Constraint` node | `approver_id`, `override_reason`, `original_nlp_confidence` | Immutable audit log entry. Overwrites NLP output with `authority_weight = HIGH`. | `fleet_operations_interview_notes.md` |

### 2. Provenance Chain Integrity
- Every canonical node must have a `[:DERIVED_FROM]` edge pointing to the `EvidenceRecord`.
- The `[:DERIVED_FROM]` edge MUST contain the `transformation_metadata` payload (e.g., `nlp_model_version`).
- If a transformation rule is updated (e.g., NLP model v2 is deployed), all new extractions use v2. Old extractions retain their v1 metadata, ensuring historical decisions can be reconstructed exactly as they were evaluated at the time.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| NLP extractions must retain the raw text snippet and model version for auditability. | `fleet_operations_interview_notes.md` | `oversight-transparency-requirements.md` | High confidence (SME interview). |
| Human overrides must be immutably logged with the approver's ID. | `role_authorization_matrix.csv` | `lineage-integration.md` | High confidence (explicit policy). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: Storing the `raw_text_snippet` for every NLP extraction does not exceed the graph database's property size limits. | Graph DB property size limits are NOT RUN. | Shore Platform Team | If limits are hit, the snippet must be stored in Blob Storage and referenced by URI. | Stage 10 Physical Persistence Topology. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture