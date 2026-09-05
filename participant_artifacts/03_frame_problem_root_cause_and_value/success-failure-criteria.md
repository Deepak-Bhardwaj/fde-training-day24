# Success / Failure Criteria

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 03 — Frame Problem, Root Cause & Value
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
What evidence proves the problem, its causes and its value?

## Why this artifact exists
This artifact is part of the evidence needed to reach **Evidence-backed problem and measurable baseline**. It must be consistent with approved upstream artifacts.

## Upstream dependency
Use the completed Stage 03 KPI Tree, CTQs, and Counter-Metrics.

## Evidence to inspect
- `evidence/01_enterprise_sources/live_disruptions.csv`
- `evidence/04_policy_authority/role_authorization_matrix.csv`

## Case challenge
Define the explicit, binary criteria that will determine if the overall engagement and the future system design are considered a success or a failure.

## Minimum content

| Category | Success Criteria | Failure Criteria | Evidence |
| :--- | :--- | :--- | :--- |
| **Safety & Authority** | 100% of navigational and safety-critical recovery actions require explicit Master approval. System never auto-executes commands. | ANY scenario (e.g., GS-02, GS-08) results in the system bypassing Master authority or auto-executing a command. | `role_authorization_matrix.csv` |
| **Technical Integrity** | Critical CMMS maintenance holds are respected as absolute constraints in 100% of generated recovery options. | ANY scenario (e.g., GS-03) results in a recovery option that violates an active technical hold. | `source_authority.yaml` |
| **Data Resilience** | System handles duplicate events (GS-07) and clock drift (GS-13) idempotently without state corruption. | System state is corrupted, or duplicate events cause double-counting of disruptions/delays. | `live_event_stream.jsonl` |
| **Offline Continuity** | Vessel-side workbench successfully supports critical decision-making during prolonged satellite blackout (GS-14) and reconciles safely on reconnect (GS-15). | Vessel operations are halted, or unsafe divergence occurs during connectivity loss. | `fleet_operations_interview_notes.md` |
| **Information Integrity** | System exclusively uses ACTIVE policies for decision logic; superseded policies are never surfaced as active rules (GS-12). | System retrieves and applies a superseded policy, leading to an invalid recovery option. | `source_inventory.csv` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Bypassing Master authority is an absolute failure condition. | `role_authorization_matrix.csv` | `ctqs.md` | High confidence (explicit policy). |
| Safe reconciliation on reconnect is mandatory. | `fleet_operations_interview_notes.md` | `scqa-problem-frame.md` | High confidence (SME interview). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The 15 Golden Scenarios adequately cover all critical failure modes. | Scenarios are synthetic; real-world edge cases may exist. | FDE Team / Safety Officer | May require adding supplementary evaluation scenarios in Stage 07. | Stage 07 Evaluation Scenarios. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Evidence-backed problem and measurable baseline
Do not advance to Stage 04 until the Stage 03 exit gate is defensible.