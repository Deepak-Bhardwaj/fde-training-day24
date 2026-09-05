# Event / State / Temporal Model

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer F: Runtime Context Graph)
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To define how the system models time and state transitions to handle clock drift (GS-13), out-of-order delivery, and offline/online state divergence (GS-14, GS-15) without corrupting the canonical truth.

## Upstream dependency
Use the completed Stage 06 Provenance Baseline and Stage 09 Runtime Entity State Model.

## Evidence to inspect
- `evidence/01_enterprise_sources/live_event_stream.jsonl`
- `evidence/01_enterprise_sources/source_inventory.csv`

## Case challenge
Relying solely on system ingestion time is insufficient due to telemetry clock drift. The model must separate "when it happened" from "when we saw it" and resolve conflicts deterministically.

## Minimum content

### 1. Temporal Dimensions
Every state-changing event must record three distinct timestamps:
- **`observed_ts`**: When the event occurred at the source (e.g., vessel sensor time).
- **`ingestion_ts`**: When the shore platform or edge system received the event.
- **`processed_ts`**: When the deterministic engine evaluated the event.

### 2. Conflict Resolution Rules (Out-of-Order / Drift)
- **Rule 1 (Idempotency):** If an event arrives with a `deduplication_hash` that already exists in the `EvidenceRecord` store, it is logged as `Ignored_Duplicate` and discarded.
- **Rule 2 (Late Arrival):** If an event arrives with `observed_ts` significantly in the past (beyond the source's `freshness_threshold`), it is tagged `STALE` and routed to the Audit Context, but does *not* retroactively alter the current `Runtime Context Graph`.
- **Rule 3 (Vessel/Shore Divergence):** During reconnect (GS-15), if the vessel edge executed an action based on a local state that the shore later marks as `EXPIRED`, the shore's `ACTIVE` state takes precedence for *future* planning, but the vessel's historical execution log is preserved immutably in the Audit Context with a `divergence_flag`.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Late-arriving telemetry must not retroactively invalidate already-executed, Master-approved plans. | `fleet_operations_interview_notes.md` (vessel/shore divergence) | `risk-treatment-plan.md` (RH-04) | High confidence (SME interview). |
| Deduplication must rely on a deterministic hash, not ingestion order. | `live_event_stream.jsonl` (duplicate delivery) | `canonical-identifier-strategy.md` | High confidence (architectural necessity). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The "significantly in the past" threshold can be uniformly defined per source without causing false positives. | Exact clock drift variance across all vessel hardware is unknown. | Vessel Technical | May require dynamic drift tolerance windows based on historical source health. | Stage 09 Quality