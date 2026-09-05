# Dependencies

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench

**Stage:** 02 — Discover Process & Architecture

**Participant status:** COMPLETED

**Deliverable form:** Structured table / register

## Stage question
How does the real brownfield process and system operate today?

## Why this artifact exists
This artifact is part of the evidence needed to reach **Current-state process and architecture baseline**. It must be consistent with approved upstream artifacts; do not silently redefine earlier facts, semantics, thresholds or decision rights.

## Upstream dependency
Use the completed Stage 01 artifacts and Stage 02 System Landscape / C4 Views.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
Catalog the critical external and internal dependencies of the current brownfield process, including their failure modes and freshness constraints.

## Minimum content
- Dependency Name
- Type (External/Internal/Infrastructure)
- Provider/Owner
- SLA/Freshness Threshold
- Failure Mode
- Impact on Process
- Evidence

## Working scaffold

| Dependency Name | Type | Provider/Owner | SLA/Freshness Threshold | Failure Mode | Impact on Process | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Port API & Notices** | External | External Port Authority | 60 mins (or per signed notice) | API outage; semantic mismatch with signed PDF notices. | Controllers cannot verify berth availability; must default to conservative routing. | `source_inventory.csv` (SRC-PORT), `fleet_operations_interview_notes.md` |
| **Weather & Ocean Data** | External | External Provider | 90 mins | License expiration; provider outage; forecast versioning delays. | Inability to assess severe weather stress (GS-02, GS-06); Master must rely on local observation. | `source_inventory.csv` (SRC-WX) |
| **Vessel Telemetry Stream** | Internal/Edge | Vessel Technical | 5 mins | Clock drift; duplicate delivery; sat-com blackout. | Shore platform receives stale or duplicated machinery signals; reconciliation fails (GS-13, GS-14). | `source_inventory.csv` (SRC-TELEM) |
| **Satellite Connectivity (VSAT/LEO)** | Infrastructure | Comms Provider | Continuous | Prolonged blackout; high latency. | Vessel and shore state diverge; shore cannot send updated constraints; vessel operates offline (GS-14). | `fleet_operations_interview_notes.md` |
| **Fleet Policy Repository** | Internal | Fleet Safety & Compliance | Version/Status based | Superseded documents remain searchable. | Retrieval systems surface outdated rules, leading to invalid recovery options (GS-12). | `source_inventory.csv` (SRC-POLICY), `source_authority.yaml` |
| **CMMS Asset Mapping** | Internal | Technical Operations | 15 mins | Asset ID mapping discrepancies between vessel and shore. | Critical maintenance holds are misidentified or ignored, violating hard feasibility constraints (GS-03). | `source_inventory.csv` (SRC-CMMS) |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Port API outages and semantic mismatches are a known, recurring dependency risk. | `fleet_operations_interview_notes.md` & `source_inventory.csv` | `system-landscape.md` | High confidence (SME interview). |
| Telemetry stream suffers from clock drift and duplicate delivery, requiring idempotent handling. | `source_inventory.csv` (SRC-TELEM known issues) | `brownfield-assessment.md` | High confidence (explicit source metadata). |
| Superseded policies remain searchable, creating a retrieval dependency trap. | `source_inventory.csv` (SRC-POLICY known issues) | `brownfield-assessment.md` | High confidence (explicit source metadata). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: Satellite connectivity blackouts are bounded in duration (e.g., < 4 hours). | Exact SLA for VSAT/LEO uptime not provided in evidence. | Shore Platform Team | If blackouts are unbounded, offline-first architecture must be 100% autonomous for longer periods. | Stage 10 Deployment Topology (offline continuity specs). |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.
- [x] `NOT APPLICABLE`, if used, includes rationale, accountable approver and downstream consequence.

## Handoff
**Stage exit contribution:** Current-state process and architecture baseline

Do not advance to Stage 03 until the Stage 02 exit gate is defensible.