# System Landscape

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench

**Stage:** 02 — Discover Process & Architecture

**Participant status:** COMPLETED

**Deliverable form:** Structured narrative + evidence table

## Stage question
How does the real brownfield process and system operate today?

## Why this artifact exists
This artifact is part of the evidence needed to reach **Current-state process and architecture baseline**. It must be consistent with approved upstream artifacts; do not silently redefine earlier facts, semantics, thresholds or decision rights.

## Upstream dependency
Use the completed Stage 01 artifacts and explicitly referenced earlier artifacts.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/02_documents/fleet_operations_interview_notes.md`
- `evidence/03_systems/system_registry.csv` (if available)

## Case challenge
Catalog the actual systems used today, their owners, update patterns, and integration points. Distinguish between what exists and what is aspirational.

## Minimum content
- System Name
- Owner
- Physical Type (API, Database, Stream, Document)
- Update Pattern
- Integration Points
- Known Issues
- Evidence

## Working scaffold

| System Name | Owner | Physical Type | Update Pattern | Integration Points | Known Issues | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **AIS Provider** | Fleet Data | API/Stream | Stream | FMS, Shore Platform | Coverage gaps; aliases; provider terms | `source_inventory.csv` |
| **Vessel Telemetry** | Vessel Technical | Edge Event Stream | Seconds/Minutes | CMMS, Shore Platform | Clock drift; duplicate delivery | `source_inventory.csv` |
| **Port Systems/Notices** | External Port | API + Documents | Variable | FMS, Voyage Planner | Inconsistent semantics; conflicting API vs signed notice | `source_inventory.csv`, `fleet_operations_interview_notes.md` |
| **Weather & Ocean** | External Provider | API | Hourly | FMS, Voyage Planner | License; outages; forecast versioning | `source_inventory.csv` |
| **Fleet Management/Voyage** | Fleet Operations | Database/API | Transactional | AIS, Port, WX, CMMS, Cargo, Crew | Manual updates | `source_inventory.csv` |
| **CMMS** | Technical Operations | Database/API | Event/Transactional | Vessel Telemetry, FMS | Asset ID mapping | `source_inventory.csv` |
| **Cargo System** | Cargo Operations | Database/API | Transactional | FMS, Voyage Planner | Commercial sensitivity; tenant isolation | `source_inventory.csv` |
| **Crew System** | Marine HR | Database/API | Transactional | FMS, Voyage Planner | Personal data; highly restricted | `source_inventory.csv` |
| **Fleet Policy Repository** | Fleet Safety & Compliance | Versioned Documents | Versioned | All systems (read-only reference) | Superseded documents remain searchable | `source_inventory.csv`, `source_authority.yaml` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Nine disparate enterprise sources exist today, each with different update patterns. | `source_inventory.csv` | `sipoc.md`, `process-value-stream-map.md` | High confidence (explicit inventory). |
| Port systems have conflicting semantics between API and signed notices. | `fleet_operations_interview_notes.md` & `source_inventory.csv` | `waste-register.md` | High confidence (SME interview). |
| Telemetry suffers from clock drift and duplicate delivery. | `source_inventory.csv` | `process-value-stream-map.md` | High confidence (explicit known issue). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: All 9 systems are currently accessible to the FDE team for integration testing. | Access permissions and API keys not detailed in evidence. | Shore Platform Team | If systems are not accessible, Stage 09/10 architecture must rely on synthetic data or mocks. | Stage 06 Qualify Data & Knowledge (data readiness assessment). |

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