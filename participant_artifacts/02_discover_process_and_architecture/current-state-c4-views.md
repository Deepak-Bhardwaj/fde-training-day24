# Current-State C4 Views

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench

**Stage:** 02 — Discover Process & Architecture

**Participant status:** COMPLETED

**Deliverable form:** Diagram + supporting table + rationale

## Stage question
How does the real brownfield process and system operate today?

## Why this artifact exists
This artifact is part of the evidence needed to reach **Current-state process and architecture baseline**. It must be consistent with approved upstream artifacts.

## Upstream dependency
Use the completed Stage 01 artifacts and Stage 02 System Landscape.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
Provide C4 model views (Context, Container, Component) of the current-state architecture. Since we cannot draw diagrams in markdown, provide structured text descriptions of the diagrams and the supporting rationale.

## Minimum content
- C4 Level
- Elements
- Relationships
- Rationale
- Evidence

## Working scaffold

### C4 Level 1: System Context

| Element | Type | Description | Relationships |
| :--- | :--- | :--- | :--- |
| **Fleet Controller** | Person | Shore-based operator managing voyage schedules and disruptions. | Uses FMS, Port Systems, Weather API. |
| **Master** | Person | Vessel commander with absolute authority over navigation. | Receives recovery options from Fleet Controller. |
| **Fleet Management System (FMS)** | Software System | Central hub for voyage planning and schedule management. | Integrates with AIS, Port, WX, CMMS, Cargo, Crew. |
| **External Port Systems** | Software System | Provides berth/pilot constraints via API and signed notices. | Sends constraints to FMS. |
| **Weather & Ocean Provider** | Software System | Provides forecast snapshots. | Sends weather data to FMS. |
| **AIS Provider** | Software System | Provides vessel position observations. | Sends AIS data to FMS. |

### C4 Level 2: Container View

| Container | Type | Description | Relationships |
| :--- | :--- | :--- | :--- |
| **FMS Web UI** | Web Application | UI used by Fleet Controllers to view schedules and disruptions. | Calls FMS API. |
| **FMS API** | Application | Backend API for voyage planning and data aggregation. | Reads from AIS, Port, WX, CMMS, Cargo, Crew databases. |
| **Vessel Telemetry Edge** | Edge Application | Collects machinery/fuel signals on vessel. | Streams data to Shore Platform. |
| **Shore Platform Sync** | Application | Reconciles vessel and shore state on reconnect. | Receives telemetry stream; updates FMS. |

### C4 Level 3: Component View (FMS API)

| Component | Type | Description | Relationships |
| :--- | :--- | :--- | :--- |
| **Disruption Aggregator** | Component | Pulls data from 9 sources and attempts to build a unified view. | Calls Port Adapter, WX Adapter, CMMS Adapter, etc. |
| **Port Adapter** | Component | Fetches port constraints from API and signed notices. | Returns conflicting data to Disruption Aggregator. |
| **Recovery Option Generator** | Component | Drafts recovery plans based on aggregated constraints. | Sends draft to Fleet Controller for review. |

## Rationale

The current-state architecture is highly fragmented, with the FMS API acting as a central aggregator but suffering from semantic conflicts (e.g., Port API vs signed notices) and temporal misalignment (clock drift in telemetry). The vessel-side edge collects telemetry but relies on shore-side sync for reconciliation, creating a divergence risk during connectivity loss. The Master is not directly integrated into the FMS UI; instead, recovery options are communicated via email/sat-com, introducing latency and potential misinterpretation.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| FMS API is the central aggregator but suffers from semantic conflicts. | `fleet_operations_interview_notes.md` | `system-landscape.md` | High confidence (SME interview). |
| Vessel telemetry relies on shore-side sync, creating divergence risk. | `fleet_operations_interview_notes.md` | `brownfield-assessment.md` | High confidence (SME interview). |
| Master is not directly integrated into FMS UI; communication is via email/sat-com. | Assumption based on interview notes mentioning "vessel and shore teams can each be correct" | `process-value-stream-map.md` | Medium confidence (inferred from divergence issue). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: Current FMS UI is web-based and accessible to Fleet Controllers. | Exact UI technology stack not detailed in evidence. | FDE Team | Limits exact definition of current state for Stage 10 target architecture. | Stage 10 AI & Application Architecture (target C4 views). |

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