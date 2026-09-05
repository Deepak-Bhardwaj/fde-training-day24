# Use-Case Card

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 04 — Triage Regulation & Qualify Use Case
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
Should AI be used at all, and under what impact/regulatory constraints?

## Why this artifact exists
To provide a single, comprehensive summary of the approved use case, its boundaries, and its success criteria for stakeholder alignment.

## Upstream dependency
Use all completed Stage 01, 02, and 03 artifacts, plus Stage 04 Impact/Regulatory Screen and Non-AI Alternative Assessment.

## Evidence to inspect
- `evidence/04_policy_authority/role_authorization_matrix.csv`
- `evidence/01_enterprise_sources/live_disruptions.csv`

## Case challenge
Summarize the use case without introducing new scope or technical architecture.

## Minimum content

| Element | Description | Evidence |
| :--- | :--- | :--- |
| **Use Case Name** | Disruption Evidence Reconciliation & Recovery Option Comparison | `scqa-problem-frame.md` |
| **Primary Actors** | Fleet Controller (Initiator/Reviewer), Master (Approver), Chief Engineer (Constraint Owner) | `governance-raci.md` |
| **Trigger** | Detection of a disruption event (e.g., port congestion, severe weather, CMMS hold) via enterprise source streams. | `sipoc.md` |
| **Pre-conditions** | 1. Access to enterprise data sources (or cached vessel-side state). 2. Active fleet policies loaded. 3. No active, unreleased critical CMMS holds blocking the specific voyage. | `dependencies.md`, `ctqs.md` |
| **Core Workflow** | 1. Ingest and reconcile conflicting/stale data from 9 sources using strict authority weighting. 2. Generate a unified, temporally proven constraint view. 3. Run deterministic feasibility checks against CMMS/Cargo/Policy. 4. Present ranked, evidence-backed recovery options to the Fleet Controller. 5. Controller selects option; Master approves. | `process-value-stream-map.md`, `non-ai-alternative.md` |
| **Post-conditions** | 1. Approved recovery plan logged with full decision trace (rationale, source freshness, outcome). 2. Vessel and shore state synchronized upon next connectivity window. | `data-flows.md`, `fleet_operations_interview_notes.md` |
| **Success Metrics** | 1. Time-to-reconcile < 10 minutes (Baseline: 45 mins). 2. Plan feasibility rate > 95% (Baseline: 78%). 3. 100% compliance with Master authority and CMMS hold constraints. | `kpi-tree.md`, `ctqs.md` |
| **Explicit Exclusions** | No autonomous execution. No chatbot UI. No bypassing of technical holds. No use of superseded policies. | `prohibited-use-check.md` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| The use case is strictly bounded to decision-support and evidence reconciliation. | `non-ai-alternative.md`, `prohibited-use-check.md` | `ai-suitability-assessment.md` | High confidence (explicit design choice). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The Fleet Controller UI will be accessible via existing shore-side web infrastructure. | UI/UX requirements not yet detailed. | FDE Team / Shore Platform | May require specific frontend framework decisions in Stage 10. | Stage 10 Target C4 Views. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved and justified use case
Do not advance to Stage 05 until the Stage 04 exit gate is defensible.