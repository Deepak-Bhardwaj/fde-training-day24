# Source-to-Canonical Mapping

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer A: Enterprise Source Layer)
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To document the exact transformation rules applied by the Anti-Corruption Layer (ACL) to translate disparate, conflicting source schemas into the unified Canonical Entity Model defined in Stage 05.

## Upstream dependency
Use the completed Stage 05 Ubiquitous Language Glossary and Stage 09 Enterprise Source Authority Model.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
Explicitly define how semantic conflicts (e.g., "available" vs "confirmed") are resolved during mapping. Do not allow source schemas to dictate the canonical model.

## Minimum content

| Canonical Entity / Attribute | Source System | Source Field / Format | Transformation / Conflict Resolution Rule | Authority Weight Applied | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Vessel.canonical_id** | SRC-FMS | `vessel_mmsi` | Direct map. Primary source of truth. | HIGH | `source_authority.yaml` |
| **Vessel.canonical_id** | SRC-AIS | `ais_name` / `mmsi` | Fuzzy match against SRC-FMS. If ambiguous, flag as `identity_conflict` (GS-04). | OBSERVATION | `source_authority.yaml` |
| **Constraint.port_status** | SRC-PORT (API) | `berth_status` (enum) | Map to canonical enum. If "available", flag as `UNVERIFIED` pending notice check. | MEDIUM | `fleet_operations_interview_notes.md` |
| **Constraint.port_status** | SRC-PORT (Notice) | PDF Text Extraction | NLP extracts status. Overrides API if present. Map to canonical enum. | HIGH | `source_authority.yaml` |
| **Constraint.maintenance_hold** | SRC-CMMS | `work_order_status` | If `status == 'OPEN'` AND `criticality == 'HIGH'`, map to `ACTIVE_HOLD`. | HIGH | `source_inventory.csv` |
| **Event.observed_timestamp** | SRC-TELEM | `sensor_time` | Preserve original. Do not overwrite with ingestion time. Tag with `clock_drift_risk`. | OBSERVATION | `provenance-baseline.md` |
| **Policy.rule_text** | SRC-POLICY | Document Body | Filter by `metadata.status == 'ACTIVE'`. Superseded docs excluded from operational mapping. | HIGHEST | `source_authority.yaml` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Port API "available" must be downgraded to UNVERIFIED if a signed notice exists. | `fleet_operations_interview_notes.md` | `quality-profile.md` | High confidence (SME interview). |
| Telemetry `observed_timestamp` must be preserved, not overwritten, to handle clock drift. | `source_inventory.csv` (SRC-TELEM known issues) | `provenance-bbaseline.md` | High confidence (explicit source metadata). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The NLP extraction from PDF notices (SRC-PORT) can reliably map to the canonical `port_status` enum. | NLP accuracy for this specific mapping is unproven (NOT RUN). | FDE Team | Requires the human-in-the-loop fallback designed in Stage 08. | Stage 09 Knowledge Extraction Specification. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture
Do not advance to the next sub-layer until this artifact is defensible.