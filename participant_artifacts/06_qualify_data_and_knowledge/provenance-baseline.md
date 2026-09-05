# Provenance Baseline

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 06 — Qualify Data & Knowledge
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
Is the evidence trustworthy, permissible, traceable, representative and ready?

## Why this artifact exists
To establish the minimum metadata requirements for every piece of data ingested into the system, ensuring that temporal provenance and source authority can be reconstructed at any time (especially for post-event audits).

## Upstream dependency
Use the completed Stage 05 Domain Events, Stage 06 Lineage, and Quality Profile.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
Define a strict, non-negotiable provenance schema that survives the journey from external source to final audit log, even across vessel-to-shore connectivity blackouts.

## Minimum content

### Core Provenance Metadata Schema
Every ingested event or constraint MUST contain the following fields:
1. **`source_id`**: The authoritative source identifier (e.g., SRC-TELEM, SRC-PORT).
2. **`observed_timestamp`**: The exact time the event occurred at the source (vessel time, port time, etc.).
3. **`ingestion_timestamp`**: The time the system received and processed the event.
4. **`source_version`**: The version or hash of the source document/state (critical for SRC-POLICY and SRC-PORT notices).
5. **`authority_weight`**: The precedence level of this source per `source_authority.yaml` (e.g., HIGH, OBSERVATION, NON_AUTHORITATIVE).

### Handling Provenance Challenges
- **Clock Drift (GS-13):** The system will record both `observed_timestamp` and `ingestion_timestamp`. Reconciliation logic will use a sliding time window based on the source's `freshness_threshold` to align vessel and shore timelines.
- **Duplicate Events (GS-07):** The ingestion layer will generate a deterministic hash of (`source_id`, `observed_timestamp`, `payload_hash`). Duplicates will be logged as "Ignored_Duplicate" in the Audit Context, preserving the original event's provenance.
- **Offline Execution (GS-14):** Events generated on the vessel edge during a blackout will be tagged with `connectivity_state = OFFLINE` and batch-synced upon reconnect, maintaining their original `observed_timestamp`.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Provenance must include both observed and ingestion timestamps to handle drift. | `source_inventory.csv` (SRC-TELEM clock drift) | `quality-profile.md` | High confidence (explicit source metadata). |
| Offline events must retain original timestamps to ensure accurate post-event reconstruction. | `fleet_operations_interview_notes.md` (vessel/shore divergence) | `ddd-context-map.md` | High confidence (SME interview). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: All external providers (WX, Port) provide reliable `observed_timestamp` in their payloads. | Some legacy APIs may only provide ingestion time. | FDE Team / External Providers | If missing, the system must default `observed_timestamp` = `ingestion_timestamp` and flag as "Low Provenance Confidence". | Stage 09 Retrieval Source Adapters. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Data and knowledge readiness assessment
Do not advance to Stage 07 until the Stage 06 exit gate is defensible.