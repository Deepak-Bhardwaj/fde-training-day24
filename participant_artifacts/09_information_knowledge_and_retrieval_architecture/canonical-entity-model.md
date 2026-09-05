# Canonical Entity Model

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer B: Semantic Foundation)
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To define the exact attributes, data types, and mandatory metadata for the core business entities that will be stored in the canonical constraint store and cached on the vessel edge.

## Upstream dependency
Use the completed Stage 05 Domain Capability Map and Stage 09 Semantic Model.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
Every entity must inherently carry its temporal provenance and authority weight. An entity without provenance is invalid and must be rejected by the system.

## Minimum content

| Entity Name | Core Attributes | Mandatory Provenance Envelope | Authority Weight | Validation Rule | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Vessel** | `canonical_id`, `name`, `imo_number`, `current_status` | `source_id` (SRC-FMS), `ingestion_ts` | HIGH | `canonical_id` must match Fleet Registry. | `source_authority.yaml` |
| **Constraint (Port)** | `port_id`, `berth_id`, `status` (CONFIRMED/UNVERIFIED/CLOSED), `valid_until` | `source_id` (SRC-PORT), `observed_ts`, `document_hash` (if PDF) | HIGH / MEDIUM | `valid_until` cannot exceed 60 mins from `observed_ts`. | `source_inventory.csv` |
| **Constraint (CMMS)** | `asset_id`, `hold_type`, `severity`, `status` (ACTIVE/RELEASED) | `source_id` (SRC-CMMS), `observed_ts`, `engineer_id` | HIGH | `status == ACTIVE` blocks all feasibility checks. | `business-rules.md` (BR-02) |
| **Disruption** | `disruption_id`, `vessel_id`, `event_type`, `severity`, `root_cause_source` | `source_id`, `observed_ts`, `deduplication_hash` | OBSERVATION | Must be deduplicated via `deduplication_hash`. | `provenance-baseline.md` |
| **Recovery Option** | `option_id`, `disruption_id`, `proposed_actions`, `feasibility_score`, `ai_draft_flag` | `source_id` (Engine/AI), `generation_ts`, `policy_version_used` | NON_AUTHORITATIVE | `ai_draft_flag == true` requires Master approval. | `source_authority.yaml` |
| **Policy Rule** | `rule_id`, `text`, `category`, `status` (ACTIVE/SUPERSEDED) | `source_id` (SRC-POLICY), `version_id`, `effective_date` | HIGHEST | `status` must be ACTIVE to be loaded into deterministic engine. | `source_authority.yaml` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| The Provenance Envelope is a mandatory, non-nullable component of every entity. | `provenance-baseline.md` | `quality-profile.md` | High confidence (architectural mandate). |
| Recovery Options are inherently NON_AUTHORITATIVE regardless of their generation method. | `source_authority.yaml` | `ai-suitability-assessment.md` | High confidence (explicit policy). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The `document_hash` for Port Notices can be reliably generated and stored within the entity payload without exceeding size limits. | Exact PDF hash size vs. edge storage limits not benchmarked. | Shore Platform Team | May require storing only the hash reference in the entity, with the full document in blob storage. | Stage 10 Physical Persistence Topology. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture
Do not advance to the next sub-layer until this artifact is defensible.