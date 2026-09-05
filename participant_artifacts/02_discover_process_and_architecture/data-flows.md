# Data Flows

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench

**Stage:** 02 — Discover Process & Architecture

**Participant status:** COMPLETED

**Deliverable form:** Diagram + supporting table + rationale

## Stage question
How does the real brownfield process and system operate today?

## Why this artifact exists
This artifact is part of the evidence needed to reach **Current-state process and architecture baseline**. It must be consistent with approved upstream artifacts.

## Upstream dependency
Use the completed Stage 01 artifacts and Stage 02 System Landscape / C4 Views.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
Map the actual flow of data between systems, actors, and the vessel/shore boundary. Identify where data is transformed, delayed, or lost.

## Diagram Description (Current-State Data Flow)
*(Note: As this is a text-based artifact, the diagram is represented structurally below. In a visual tool, this would be a swimlane diagram separating External, Shore, Connectivity, and Vessel zones.)*

1. **External Zone:** Port API, WX API, AIS Stream push to Shore Platform.
2. **Shore Zone:** Shore Platform aggregates data -> FMS API -> Fleet Controller UI.
3. **Connectivity Zone:** Sat-com link (high latency, prone to blackout).
4. **Vessel Zone:** Vessel Telemetry Edge pushes to Shore Platform. Master receives recovery options via email/sat-com text -> Executes -> Logs outcome locally.

## Working scaffold

| Flow ID | Source | Destination | Data/Payload | Protocol/Pattern | Latency/Freshness | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **DF-01** | Port Authority | Shore Platform | Berth constraints (API JSON + Signed PDF) | API Polling + Manual Upload | Variable (up to 60 mins) | `source_inventory.csv` (SRC-PORT) |
| **DF-02** | Weather Provider | Shore Platform | Forecast snapshots | API Polling | Hourly (90 min threshold) | `source_inventory.csv` (SRC-WX) |
| **DF-03** | Vessel Telemetry Edge | Shore Platform | Machinery/fuel signals | Edge Event Stream | Seconds/Minutes (Clock drift risk) | `source_inventory.csv` (SRC-TELEM) |
| **DF-04** | Shore Platform (FMS) | Fleet Controller UI | Aggregated disruption view, draft recovery options | Internal API / Web UI | 30 mins (Manual update lag) | `fleet_operations_interview_notes.md` |
| **DF-05** | Fleet Controller | Master | Recovery plan options, constraint rationale | Email / Sat-com Text | High latency (connectivity dependent) | `fleet_operations_interview_notes.md` |
| **DF-06** | Master / Vessel Systems | Shore Platform | Execution logs, outcome data, local telemetry | Batch Sync on Reconnect | Delayed until reconnect (GS-14) | `fleet_operations_interview_notes.md` |

## Rationale
The current data flow is heavily asymmetric. Shore-side systems receive continuous (but sometimes stale or conflicting) streams from external providers and the vessel. However, the critical handoff of recovery options to the Master relies on high-latency, low-bandwidth sat-com text/email. Furthermore, the vessel's local execution logs and telemetry are only reconciled with the shore *after* connectivity is restored, meaning post-event learning is inherently delayed and fragmented. This flow explicitly violates the requirement for real-time, reconstructable decision traces.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Vessel-to-shore telemetry is a continuous stream but suffers from clock drift. | `source_inventory.csv` (SRC-TELEM) | `dependencies.md` | High confidence (explicit metadata). |
| The handoff of recovery options to the Master is high-latency and unstructured. | `fleet_operations_interview_notes.md` | `process-value-stream-map.md` | High confidence (SME interview). |
| Vessel execution logs are only reconciled post-event upon reconnect. | `fleet_operations_interview_notes.md` ("vessel and shore teams can each be correct relative to different clocks") | `brownfield-assessment.md` | High confidence (SME interview). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: Vessel local systems can store execution logs securely until reconnect. | Exact local storage capacity and security on vessel edge not detailed. | Vessel Technical / Shore Platform | If local storage is limited, critical evidence may be lost during prolonged blackouts (GS-14). | Stage 10 Deployment Topology (vessel edge storage specs). |

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