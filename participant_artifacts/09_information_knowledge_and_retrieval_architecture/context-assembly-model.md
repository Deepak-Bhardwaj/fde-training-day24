# Context Assembly Model

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer F: Runtime Context Graph)
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To define the exact mechanism by which the system dynamically assembles the "Active Subgraph" (Runtime Context) for a specific vessel and voyage, ensuring the deterministic engine receives only relevant, valid, and high-authority data.

## Upstream dependency
Use the completed Stage 09 Runtime Context Graph Architecture and Retrieval Evidence Contract.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
The assembly model must be highly performant (< 20ms) and strictly filter out expired, superseded, or low-authority data before it ever reaches the feasibility engine.

## Minimum content

### 1. Assembly Trigger & Inputs
- **Trigger:** `DisruptionDetected` event or Fleet Controller manual request.
- **Inputs:** `vessel_canonical_id`, `voyage_id`, `current_timestamp`.

### 2. Assembly Pipeline (Shore & Edge)
1. **Anchor Lookup:** Fetch `Vessel` and `Voyage` nodes by `canonical_id`.
2. **Constraint Expansion:** Traverse `[:CONSTRAINED_BY]` edges from `Voyage`.
   - *Filter:* `edge.valid_until > current_timestamp` AND `edge.authority_weight >= 'MEDIUM'`.
3. **Policy Expansion:** Traverse `[:GOVERNS]` edges.
   - *Filter:* `node.status == 'ACTIVE'` AND `node.category` matches voyage region/cargo.
4. **Payload Serialization:** Package the filtered subgraph into the Retrieval Evidence Contract JSON format.

### 3. Caching Strategy (Vessel Edge)
- **Cache Scope:** Only the serialized payload for the *current active voyage*.
- **Invalidation:** Triggered by `ConnectivityRestored` event (fetches latest delta) or local `Constraint` expiration timer.
- **Fallback:** If cache is missing or corrupted, system defaults to "Manual Mode" and alerts the Master.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Context assembly must strictly filter by temporal validity and authority weight. | `source_inventory.csv` (freshness thresholds), `source_authority.yaml` | `runtime-context-graph-architecture.md` | High confidence (architectural mandate). |
| Vessel edge must cache this context to support offline continuity (GS-14). | `fleet_operations_interview_notes.md` | `go-no-go-kill-criteria.md` (G-02) | High confidence (non-negotiable constraint). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: