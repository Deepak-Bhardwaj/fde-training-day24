# Domain Capability Map

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 05 — Model the Domain
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
What does the business actually mean, decide and own?

## Why this artifact exists
To identify the core business capabilities required to manage fleet disruptions, independent of the current broken systems or future technical architecture.

## Upstream dependency
Use the completed Stage 04 Use-Case Card and Stage 05 Ubiquitous Language Glossary.

## Evidence to inspect
- `evidence/02_documents/fleet_operations_interview_notes.md`
- `evidence/01_enterprise_sources/source_inventory.csv`

## Case challenge
Focus on *what* the business must do, not *how* it currently does it or *how* we will build it.

## Minimum content

| Capability Area | Specific Capability | Description | Business Value | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **1. Disruption Management** | 1.1 Disruption Detection | Ingest and identify deviation events from enterprise streams (AIS, Telemetry, Port, WX). | Early warning, reduced reaction time. | `source_inventory.csv` |
| | 1.2 Evidence Reconciliation | Resolve semantic and temporal conflicts across disparate data sources to form a unified constraint view. | Eliminates manual reconciliation waste; single source of truth. | `fleet_operations_interview_notes.md` |
| **2. Constraint Validation** | 2.1 Technical Hold Enforcement | Apply CMMS maintenance holds as absolute, non-negotiable feasibility gates. | Prevents unsafe or mechanically infeasible voyage plans. | `source_inventory.csv` (SRC-CMMS) |
| | 2.2 Policy Compliance Check | Validate recovery options against ACTIVE fleet policies only. | Ensures regulatory and operational compliance. | `source_authority.yaml` |
| **3. Recovery Planning** | 3.1 Option Generation | Synthesize valid, evidence-backed alternative courses of action based on reconciled constraints. | Provides controllers with viable choices, not just raw data. | `fleet_operations_interview_notes.md` |
| | 3.2 Feasibility Scoring | Rank options based on commercial, safety, and temporal constraints. | Optimizes for both safety and business value. | `kpi-tree.md` |
| **4. Authority & Execution** | 4.1 Human-in-the-Loop Approval | Route selected recovery options to the Master (or Chief Engineer for technical releases) for explicit approval. | Preserves Master's absolute command authority. | `role_authorization_matrix.csv` |
| **5. Resilience & Audit** | 5.1 Offline State Management | Maintain critical decision-support capabilities on the vessel edge during connectivity loss. | Ensures continuous safe operation during blackouts (GS-14). | `fleet_operations_interview_notes.md` |
| | 5.2 Decision Traceability | Link rationale, source freshness, and outcomes for every executed recovery option. | Enables effective post-event learning and safety audits. | `fleet_operations_interview_notes.md` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Evidence Reconciliation is a distinct, critical business capability. | `fleet_operations_interview_notes.md` ("slowest part is reconciling which version is current") | `root-cause-analysis.md` | High confidence (SME interview). |
| Offline State Management is mandatory, not optional. | `fleet_operations_interview_notes.md` (vessel/shore divergence) | `ctqs.md` | High confidence (SME interview). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: "Feasibility Scoring" can be fully deterministic without requiring ML optimization. | Complex multi-variable optimization might need heuristic approaches. | FDE Team | If deterministic scoring is too rigid, Stage 08 may need to evaluate specific optimization solvers. | Stage 08 Solution Catalogue. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Domain and decision model
Do not advance to Stage 06 until the Stage 05 exit gate is defensible.