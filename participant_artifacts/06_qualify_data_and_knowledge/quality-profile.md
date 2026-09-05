# Quality Profile

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 06 — Qualify Data & Knowledge
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
Is the evidence trustworthy, permissible, traceable, representative and ready?

## Why this artifact exists
To define the specific data quality dimensions (accuracy, completeness, timeliness, consistency) for each critical source and the deterministic mitigations required to handle known defects.

## Upstream dependency
Use the completed Stage 06 Data/Knowledge Inventory and Stage 01 Field Evidence Register.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/01_enterprise_sources/live_event_stream.jsonl`

## Case challenge
Do not assume data is clean. Explicitly profile the known issues and define the system's required response to poor-quality data.

## Minimum content

| Source ID | Quality Dimension | Current Profile / Known Issue | Required System Mitigation | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **SRC-TELEM** | **Timeliness / Consistency** | Subject to clock drift and duplicate delivery. | Ingestion layer must apply temporal deduplication logic (composite key: SourceID, EventID, OriginalTimestamp). Out-of-order events must be flagged. | `source_inventory.csv`, `live_event_stream.jsonl` |
| **SRC-PORT** | **Accuracy / Consistency** | API fields use different meanings for "available" vs signed notice "confirmed". | ACL must enforce `source_authority.yaml` precedence: Signed Notice > API. API-only data must be flagged as "Unverified". | `source_inventory.csv`, `fleet_operations_interview_notes.md` |
| **SRC-AIS** | **Completeness** | Coverage gaps and aliases. | System must fall back to SRC-FMS (Canonical Identity) when AIS is missing or ambiguous (GS-04). | `source_inventory.csv`, `source_authority.yaml` |
| **SRC-POLICY** | **Accuracy** | Superseded documents remain searchable. | Retrieval layer must apply a hard filter: `WHERE status = 'ACTIVE'`. Historical docs routed to Audit Context only. | `source_inventory.csv`, `source_authority.yaml` |
| **SRC-CMMS** | **Accuracy** | Asset ID mapping discrepancies between vessel and shore. | Entity resolution step required to map vessel-local asset IDs to canonical shore IDs before feasibility checking. | `source_inventory.csv` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Telemetry requires explicit deduplication due to known edge stream flaws. | `live_event_stream.jsonl` (duplicate events observed) | `business-rules.md` (BR-05) | High confidence (empirical data). |
| Policy retrieval must strictly filter by active status to avoid GS-12 trap. | `source_inventory.csv` (SRC-POLICY known issues) | `prohibited-use-check.md` | High confidence (explicit source metadata). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The entity resolution logic for SRC-CMMS asset IDs can be maintained deterministically without manual intervention. | Mapping table update frequency not defined. | Technical Operations | If mapping drifts, feasibility checks may incorrectly pass or fail. | Stage 09 Entity Resolution Specification. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Data and knowledge readiness assessment
Do not advance to Stage 07 until the Stage 06 exit gate is defensible.