# Retrieval Source Adapters

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer E: Hybrid Retrieval)
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To define the specific adapter logic for each of the 9 enterprise sources, detailing how their raw data is routed into the Hybrid Retrieval Architecture (Graph, Vector, or Relational stores).

## Upstream dependency
Use the completed Stage 09 Source-to-Canonical Mapping, Hybrid Retrieval Architecture, and Knowledge Extraction Specification.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
Every adapter must enforce the Provenance Envelope and the Authority Precedence rules before writing to any store. No source data enters the system without its metadata intact.

## Minimum content

| Source ID | Data Type | Primary Target Store | Adapter Logic / Transformation | Fallback / Error Handling | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **SRC-FMS** | Structured (JSON/API) | Property Graph | Direct map to `Vessel` and `Voyage` nodes. Enforce `canonical_id` uniqueness. | Reject if `canonical_id` is missing. | `source-to-canonical-mapping.md` |
| **SRC-PORT** | Mixed (API + PDF) | Graph + Vector | API -> `Constraint` node (UNVERIFIED). PDF -> NLP Extraction -> `Constraint` node (CONFIRMED) + Vector embedding for search. | If NLP confidence < 0.95, route to Controller Review Queue. | `knowledge-extraction-specification.md` |
| **SRC-TELEM** | Stream (JSONL) | Property Graph | Aggregate high-frequency signals into time-bucketed `Disruption` or `Observation` nodes. Apply deduplication hash. | Drop duplicates; log to Audit. | `canonical-identifier-strategy.md` |
| **SRC-WX** | Structured (API) | Property Graph | Map to `Constraint` (Weather). Apply 90-min freshness threshold. | If API timeout, mark existing WX constraints as `STALE`. | `source_inventory.csv` |
| **SRC-CMMS** | Event (Stream) | Property Graph | Map `critical_open` work orders to `Constraint` nodes with `type = CMMS_HOLD`. | If asset ID mapping fails, mark as `UNVERIFIED_ASSET`. | `entity-resolution-specification.md` |
| **SRC-CARGO** | Structured (DB) | Property Graph | Map to `Constraint` (Cargo). Apply strict RBAC tenant isolation tags. | Reject if tenant ID is missing or mismatched. | `permissible-use-access-matrix.md` |
| **SRC-CREW** | Structured (DB) | Relational (Isolated) | **NO GRAPH INGESTION.** Data remains in isolated HR relational store. Only `rest_hours_available` metric is exposed to engine via secure API. | AI/Graph adapters are strictly blocked from accessing this source. | `source_inventory.csv` |
| **SRC-POLICY** | Unstructured (Doc) | Graph + Vector | Parse doc. If `status = ACTIVE`, create `PolicyRule` node (Graph) + embedding (Vector). If `SUPERSEDED`, Vector only (Archive). | Reject if `status` field is missing. | `knowledge-extraction-specification.md` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| SRC-CREW data must never enter the Property Graph or Vector store to protect PII. | `source_inventory.csv` (SRC-CREW access_boundary) | `permissible-use-access-matrix.md` | High confidence (explicit policy). |
| SRC-POLICY superseded documents are retained in Vector for historical search but excluded from Graph operational logic. | `source_authority.yaml` | `quality-profile.md` | High confidence (explicit policy). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The secure API exposing `rest_hours_available` from SRC-CREW can be implemented without leaking underlying PII. | HR Systems Team API design not yet reviewed. | Marine HR / IT Security | If PII leaks, it violates maritime labor privacy regulations. | Stage 10 API Contracts. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture