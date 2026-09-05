# Scope

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench

**Stage:** 01 — Mandate & Field Immersion

**Participant status:** COMPLETED

**Deliverable form:** Structured narrative + evidence table

## Stage question
Why are we here, what outcome matters, who owns it, and who is affected?

## Why this artifact exists
This artifact is part of the evidence needed to reach **Approved mandate and operating context**. It must be consistent with approved upstream artifacts; do not silently redefine earlier facts, semantics, thresholds or decision rights.

## Upstream dependency
Use the case pack and supplied evidence. No solution architecture is an input to Stage 01.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/02_documents/fleet_operations_interview_notes.md`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
Stay in the field problem and ownership space. Do not propose a model, graph database, agent or UI in this artifact.

## Minimum content

| In Scope | Out of Scope | Boundary conditions | Evidence basis |
| :--- | :--- | :--- | :--- |
| Evidence reconciliation across 9 enterprise sources (AIS, Telemetry, Port, Weather, FMS, CMMS, Cargo, Crew, Policy). Recovery option comparison and analysis. Offline continuity and vessel-to-shore state reconciliation. Idempotent handling of duplicate/replayed events. Validation against 15 Golden Scenarios (GS-01 to GS-15). | Live navigation or vessel command. Autonomous AI decision-making. Fabrication of PoC results, vendor facts, or regulatory classifications. Black-box decision traces. | Master's authority is absolute for navigation/safety. Chief Engineer's authority is absolute for technical releases. AI output is strictly non-authoritative. Data freshness thresholds must be respected per source. | `source_inventory.csv` (source authority and freshness limits), `source_authority.yaml` (AI precedence: NON_AUTHORITATIVE), `fleet_operations_interview_notes.md` (offline divergence issues). |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Evidence reconciliation is the core problem, not data access. | `fleet_operations_interview_notes.md` (Line: "slowest part is... reconciling which version is current") | `engagement-charter.md` | High confidence (SME interview). |
| AI cannot issue navigational commands. | `source_authority.yaml` (AI_OUTPUT precedence: NON_AUTHORITATIVE) | `engagement-charter.md` | High confidence (explicit policy). |
| Offline continuity is required due to vessel-to-shore divergence. | `fleet_operations_interview_notes.md` (Line: "vessel and shore teams can each be correct relative to different clocks") | `engagement-charter.md` | High confidence (SME interview). |
| Data freshness thresholds vary by source (e.g., Telemetry: 5 min, Port: 60 min). | `source_inventory.csv` (freshness_threshold column) | `engagement-charter.md` | High confidence (explicit source metadata). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: All 9 sources will be available for testing across all 15 Golden Scenarios. | Some scenarios explicitly test source unavailability (e.g., GS-06 Weather source unavailable). | FDE Team | If sources are unavailable, architecture must gracefully degrade and flag gaps. | Stage 07 Define Evaluations, Impacts & Risks (explicit coverage of GS-06, GS-14). |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.
- [x] `NOT APPLICABLE`, if used, includes rationale, accountable approver and downstream consequence.

## Handoff
**Stage exit contribution:** Approved mandate and operating context

Do not advance to Stage 02 until the Stage 01 exit gate is defensible.