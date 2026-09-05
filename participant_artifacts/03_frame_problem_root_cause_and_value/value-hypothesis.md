# Value Hypothesis

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 03 — Frame Problem, Root Cause & Value
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
What evidence proves the problem, its causes and its value?

## Why this artifact exists
This artifact is part of the evidence needed to reach **Evidence-backed problem and measurable baseline**. It must be consistent with approved upstream artifacts.

## Upstream dependency
Use the completed Stage 03 SCQA Problem Frame, Root-Cause Analysis, and KPI Tree.

## Evidence to inspect
- `evidence/01_enterprise_sources/live_disruptions.csv`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
Formulate a testable hypothesis linking the proposed intervention (evidence reconciliation workbench) to the measurable business outcomes, grounded in the root causes identified.

## Minimum content

| Element | Description | Evidence |
| :--- | :--- | :--- |
| **Hypothesis Statement** | IF we implement an evidence-reconciliation workbench that enforces strict source authority, temporal provenance, and offline-first vessel-side continuity, THEN the time-to-reconcile disruption evidence will decrease from 45 minutes to < 10 minutes, AND the plan feasibility rate will increase from 78% to > 95%, BECAUSE controllers will have a unified, authority-weighted view of constraints and late-arriving CMMS/Cargo data will be automatically integrated as hard feasibility gates. | `baseline-dataset.csv`, `root-cause-analysis.md` |
| **Independent Variable** | Implementation of the evidence-reconciliation workbench with temporal provenance and authority weighting. | `scqa-problem-frame.md` |
| **Dependent Variables** | 1. Time-to-reconcile (minutes). 2. Plan feasibility rate (%). 3. Post-event audit completion rate (%). | `kpi-tree.md` |
| **Confounding Factors** | 1. Severe satellite blackouts preventing shore-sync (GS-14). 2. Sudden, unforecasted weather events (GS-02). 3. Manual delays in Chief Engineer releasing CMMS holds. | `live_disruptions.csv`, `source_health_events.jsonl` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Automating authority weighting will reduce manual reconciliation time. | `fleet_operations_interview_notes.md` | `root-cause-analysis.md` | High confidence (SME interview). |
| Enforcing CMMS/Cargo as hard gates will prevent infeasible plans. | `fleet_operations_interview_notes.md` | `waste-register.md` | High confidence (SME interview). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The baseline metrics (45 mins, 78%) are stable and representative of typical operations. | Historical data covers only a specific season; seasonal variations not analyzed. | FDE Team | If baselines fluctuate wildly, Stage 07 evaluation thresholds must be dynamic. | Stage 07 Define Evaluations, Impacts & Risks. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Evidence-backed problem and measurable baseline
Do not advance to Stage 04 until the Stage 03 exit gate is defensible.