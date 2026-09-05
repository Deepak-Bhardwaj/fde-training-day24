# Field Evidence Register

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench

**Stage:** 01 — Mandate & Field Immersion

**Participant status:** COMPLETED

**Deliverable form:** Structured table / register

## Stage question
Why are we here, what outcome matters, who owns it, and who is affected?

## Why this artifact exists
This artifact is part of the evidence needed to reach **Approved mandate and operating context**. It must be consistent with approved upstream artifacts; do not silently redefine earlier facts, semantics, thresholds or decision rights.

## Upstream dependency
Use the case pack and supplied evidence. No solution architecture is an input to Stage 01.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
Stay in the field problem and ownership space. Do not propose a model, graph database, agent or UI in this artifact.

## Minimum content

| Source ID | Name | Authoritative FOR... | NOT Authoritative FOR... | Freshness Threshold | Known Issues / Risks |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **SRC-AIS** | AIS Provider | Reported position observations from the provider. | Navigation commands or voyage identity without resolution. | 15 minutes | Coverage gaps; aliases; provider terms. |
| **SRC-TELEM** | Vessel Telemetry | Observed machinery and fuel signals. | Maintenance release or navigation decisions. | 5 minutes | Clock drift; duplicate delivery. |
| **SRC-PORT** | Port Systems / Notices | Port-issued berth/pilot constraints (subject to version/status). | Vessel command authority. | 60 mins (unless signed notice states otherwise) | Inconsistent semantics; conflicting API vs. signed notice. |
| **SRC-WX** | Weather & Ocean | Provider forecast snapshots. | Final navigational decisions. | 90 minutes | License restrictions; outages; forecast versioning. |
| **SRC-FMS** | Fleet Mgmt / Voyage | Planned voyage and commercial schedule. | Real-time safety state. | 30 minutes | Manual updates (prone to human delay). |
| **SRC-CMMS** | CMMS | Equipment condition and maintenance holds. | Navigation commands. | 15 minutes | Asset ID mapping discrepancies. |
| **SRC-CARGO** | Cargo System | Cargo properties, priorities, and windows. | Safety overrides by itself. | 30 minutes | Commercial sensitivity; strict tenant isolation required. |
| **SRC-CREW** | Crew System | Crew availability and rest