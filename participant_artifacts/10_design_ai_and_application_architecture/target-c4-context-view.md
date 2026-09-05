# Target C4 Context View

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 10 — AI & Application Architecture
**Participant status:** COMPLETED
**Deliverable form:** Diagram + supporting table + rationale

## Stage question
How will the AI-enabled application consume context, integrate, deploy and fail safely?

## Why this artifact exists
To provide the highest-level (Level 1) view of the target system, showing the boundaries between the Workbench, the human actors, and the 9 external enterprise systems.

## Upstream dependency
Use the completed Stage 09 Target Data Architecture and Stage 08 Selected Solution.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/04_policy_authority/role_authorization_matrix.csv`

## Case challenge
Clearly delineate what is inside the system boundary and what is external. The system does not control the external sources; it only ingests and reacts to them.

## Diagram Description (Level 1 Context)
*(Text-based representation)*
- **Actors:** Master, Chief Engineer, Fleet Controller, Safety Officer.
- **Software System:** Fleet Disruption & Voyage Recovery Intelligence Workbench (split into Shore Platform and Vessel Edge).
- **External Systems:** AIS Provider, Port Systems, Weather Provider, CMMS, Cargo System, Crew System, Fleet Policy Repo, FMS.

## Working scaffold

| Element | Type | Description | Interactions | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **Master** | Person | Vessel Commander. Absolute authority over navigation. | Uses Vessel Edge UI to review and approve recovery options. | `role_authorization_matrix.csv` |
| **Chief Engineer** | Person | Vessel Technical Authority. | Releases CMMS maintenance holds via vessel systems. | `role_authorization_matrix.csv` |
| **Fleet Controller** | Person | Shore-based operator. | Uses Shore UI to monitor disruptions, review NLP extractions (HITL), and propose options. | `fleet_operations_interview_notes.md` |
| **Safety Officer** | Person | Shore-based compliance. | Uses Shore UI / Audit Store to review decision traces and post-event logs. | `oversight-transparency-requirements.md` |
| **Workbench (Shore)** | Software System | Heavy compute, NLP, full graph, vector store. | Ingests from 9 sources. Syncs delta state to Vessel Edge. | `reference-architecture-comparison.md` |
| **Workbench (Vessel Edge)**| Software System | Lightweight, deterministic, offline-capable. | Receives sync from Shore. Provides local decision support to Master. | `graph-persistence-architecture.md` |
| **External Sources (9)** | Software Systems | AIS, Port, WX, CMMS, Cargo, Crew, Policy, FMS, Telem. | Push/Stream data to Workbench (Shore). | `source_inventory.csv` |

## Rationale
This context view reinforces the non-negotiable constraint that the Workbench is strictly a decision-support tool. It ingests data from external systems and presents options to human actors (Master, Controller). It never auto-executes commands against external vessel navigation systems.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| The system boundary explicitly excludes vessel navigation execution. | `role_authorization_matrix.csv` (AI_AGENT commit=NO) | `prohibited-use-check.md` | High confidence (explicit policy). |

##