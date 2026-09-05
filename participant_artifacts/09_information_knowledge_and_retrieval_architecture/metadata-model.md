# Metadata Model

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer G: Metadata / Lineage / Provenance)
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To define the schema for metadata that describes the data itself (data about data), enabling governance, quality tracking, and automated lifecycle management (e.g., archival, expiration).

## Upstream dependency
Use the completed Stage 06 Provenance Baseline and Stage 09 Retrieval Evidence Contract.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
The metadata model must be lightweight enough to not bloat the graph, but rich enough to satisfy the strict audit and transparency requirements of maritime operations.

## Minimum content

### 1. Core Metadata Entities
- **`DataSource`**: Represents a source system (e.g., SRC-CMMS).
  - *Properties:* `source_id`, `owner`, `update_pattern`, `default_freshness_threshold`.
- **`DataQualityProfile`**: Represents the expected quality of a source.
  - *Properties:* `source_id`, `known_issues` (list), `last_audit_date`.
- **`AccessPolicy`**: Represents RBAC/ABAC rules for a data domain.
  - *Properties:* `domain`, `allowed_roles`, `purpose_filter`, `ai_access_allowed` (boolean).

### 2. Metadata-to-Data Relationships
- **`[:GOVERNED_BY]`**: Connects a `Constraint` or `PolicyRule` node to its `AccessPolicy`.
- **`[:HAS_QUALITY_PROFILE]`**: Connects a `DataSource` to its `DataQualityProfile`.
- **`[:ORIGINATED_FROM]`**: Connects an `EvidenceRecord` to its `DataSource`.

### 3. Lifecycle Management via Metadata
- **Archival:** When a `PolicyRule` transitions to `SUPERSEDED`, its metadata `access_policy` is updated to `AUDIT_ONLY`, and it is removed from the active Runtime Context Graph.
- **Deprecation:** If a `DataSource` is decommissioned, its `DataQualityProfile` is marked `DEPRECATED`, triggering alerts for any active `[:ORIGINATED_FROM]` edges.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Metadata must explicitly define whether AI is allowed to access a data domain. | `source_inventory.csv` (SRC-CREW ai_access = NO) | `permissible-use-access-matrix.md` | High confidence (explicit policy). |
| Data quality profiles must be linked to sources to inform the deterministic engine of known risks. | `source_inventory.csv` (known_issues column) | `quality-profile.md` | High confidence (architectural necessity). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The metadata model can be queried efficiently alongside the operational graph without performance degradation. | Graph DB metadata query performance is NOT RUN. | Shore Platform Team | May require a separate, dedicated metadata catalog (e.g., DataHub) if graph performance suffers. | Stage 09 Graph Persistence Architecture. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture