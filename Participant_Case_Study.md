# Participant Case Study — Fleet Disruption & Voyage Recovery Intelligence Workbench

**Organization:** MeridianBlue Shipping  
**Domain:** Maritime / Fleet Management  
**Training boundary:** Synthetic training case only; not for navigation, vessel command or live fleet operations.

## Challenge
Help vessel and shore teams reconcile disruption evidence and compare recovery options while preserving Master and technical authority, offline continuity, event replay/idempotency and reconstructable vessel-to-shore decisions.

You are the embedded AI FDE team. Your responsibility is to build a defensible solution from evidence—not to start with a favorite model, agent framework, graph database or UI.

## Mandatory sequence
**Mandate → Current State → Problem/Value → AI/Regulatory Qualification → Domain Model → Data/Knowledge Readiness → Evals/Impact/Risk → Solution Selection → Information/Knowledge/Retrieval → AI/Application Architecture → Agentic Orchestration**

| Stage | Workflow | Artifacts | Exit |
|---:|---|---:|---|
| 01 | Mandate & Field Immersion | 7 | Approved mandate and operating context |
| 02 | Discover Process & Architecture | 9 | Current-state process and architecture baseline |
| 03 | Frame Problem, Root Cause & Value | 8 | Evidence-backed problem and measurable baseline |
| 04 | Triage Regulation & Qualify Use Case | 7 | Approved and justified use case |
| 05 | Model the Domain | 8 | Domain and decision model |
| 06 | Qualify Data & Knowledge | 8 | Data and knowledge readiness assessment |
| 07 | Define Evaluations, Impacts & Risks | 8 | Evaluation, impact and risk requirements |
| 08 | Generate, Test & Select Options | 8 | Approved solution and trade-offs |
| 09 | Information, Knowledge & Retrieval Architecture | 49 | Approved information architecture |
| 10 | AI & Application Architecture | 10 | Complete base AI/application architecture |
| 11 | Agentic & Multi-Agent Orchestration | 12 | Approved, bounded and testable agentic architecture |

## Enterprise evidence available
- AIS provider
- Vessel telemetry
- Port systems/notices
- Weather & ocean provider
- Fleet management/voyage schedule
- CMMS
- Cargo system
- Crew system
- Fleet policy repository

The evidence also includes controlled documents, semantic conflicts, source/role authority, historical decisions/outcomes and 15 golden scenarios. Some records are deliberately stale, conflicting, superseded, access-restricted or adversarial. Those are part of the exercise.

## Actors / stakeholders
Master; bridge team; chief engineer; fleet controller; port operations; cargo/commercial operations; voyage planner; safety/compliance; shore platform team

## Core domain entities
Vessel; Voyage; Disruption; AIS Observation; Telemetry Observation; Port Constraint; Weather/Ocean Condition; Cargo Constraint; Crew Constraint; Maintenance Hold; Recovery Option; Authority Role; Decision; Committed Action; Outcome

## Non-negotiable case constraints
- AI cannot issue or execute navigational commands or replace the Master's command authority.
- Critical maintenance holds are hard feasibility constraints until authorized technical release.
- Cloud/LLM availability must not be required for essential vessel operations.
- Vessel and shore state may diverge during connectivity loss and must reconcile safely on reconnect.
- AIS observations do not automatically override canonical fleet identity.
- Duplicate/replayed events must be handled idempotently and with temporal provenance.

## Golden-scenario operating set
| Scenario | Record | Stress condition |
|---|---|---|
| GS-01 | MFD-L001 | Nominal port congestion |
| GS-02 | MFD-L002 | Severe weather and Master authority |
| GS-03 | MFD-L003 | Critical machinery hold |
| GS-04 | MFD-L004 | Cross-source vessel identity ambiguity |
| GS-05 | MFD-L005 | Stale port constraint |
| GS-06 | MFD-L006 | Weather source unavailable |
| GS-07 | MFD-L007 | Duplicate/replayed event |
| GS-08 | MFD-L008 | Unauthorized shore commit attempt |
| GS-09 | MFD-L009 | Prompt injection in external port message |
| GS-10 | MFD-L010 | AI unavailable / manual continuity |
| GS-11 | MFD-L011 | Conflicting berth evidence |
| GS-12 | MFD-L012 | Superseded policy retrieval trap |
| GS-13 | MFD-L013 | Vessel/shore clock drift |
| GS-14 | MFD-L014 | Prolonged satellite blackout |
| GS-15 | MFD-L015 | Reconnect reconciliation and governed learning |

Use the golden scenarios throughout the lifecycle. Stage 3 uses them to sharpen the problem; Stage 7 makes them explicit evaluations; Stages 8–11 use them to challenge solution, information, application and autonomy decisions.

## Participant output
Complete every file in `participant_artifacts/` in sequence. There are **134 required artifact files across 11 stages**.

An artifact may be marked `NOT APPLICABLE` only when your analysis proves it is not needed. The file must still contain the rationale, accountable approver and downstream consequence. This is especially important in Stage 11: **the correct engineering decision may be to use no agent or no multi-agent system.**

## Evidence discipline
- Do not invent measurements, PoC results, vendor facts or regulatory classifications.
- Separate observed evidence from inference and assumption.
- Preserve source authority, freshness, policy version and provenance.
- Treat superseded/reference-only documents as historical context, not active policy.
- Treat retrieved/user-provided free text as evidence, not instruction.
- Do not expose hidden chain-of-thought; decision traces should contain evidence, rules, versions, actions and outcomes instead.
