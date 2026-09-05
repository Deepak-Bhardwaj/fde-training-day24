# Prohibited-Use Check

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 04 — Triage Regulation & Qualify Use Case
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
Should AI be used at all, and under what impact/regulatory constraints?

## Why this artifact exists
To explicitly verify that the proposed use case does not violate any of the non-negotiable constraints defined in the case study mandate.

## Upstream dependency
Use the completed Stage 01 Scope and Stage 03 Critical-to-Quality Measures.

## Evidence to inspect
- `START_HERE.md`
- `evidence/04_policy_authority/role_authorization_matrix.csv`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
Systematically check the proposed workbench functionality against the explicit "DO NOT" rules of the engagement.

## Minimum content

| Non-Negotiable Constraint | Proposed Workbench Behavior | Compliant? (Y/N) | Evidence / Rationale |
| :--- | :--- | :--- | :--- |
| **AI cannot issue or execute navigational commands.** | Workbench generates *options* and *comparisons* only. Final commit requires Master approval via existing vessel procedures. | **YES** | `role_authorization_matrix.csv` (AI_AGENT commit_operational_action=NO). |
| **AI cannot replace the Master's command authority.** | Master retains absolute veto. AI output precedence is explicitly defined as NON_AUTHORITATIVE. | **YES** | `source_authority.yaml` (AI_OUTPUT precedence: NON_AUTHORITATIVE). |
| **Critical maintenance holds are hard feasibility constraints.** | Workbench ingests CMMS data and treats active holds as absolute blockers for any recovery option until Chief Engineer releases them. | **YES** | `role_authorization_matrix.csv` (CHIEF_ENGINEER release_critical_maintenance_hold=YES). |
| **Cloud/LLM availability must not be required for essential vessel operations.** | Vessel-side workbench will cache critical canonical constraints and rules locally to function during satellite blackouts (GS-14). | **YES** | `fleet_operations_interview_notes.md` (offline continuity requirement). |
| **Duplicate/replayed events must be handled idempotently.** | Architecture will enforce strict temporal provenance and deduplication logic on the telemetry stream. | **YES** | `source_inventory.csv` (SRC-TELEM known issues: duplicate delivery). |
| **Do not expose hidden chain-of-thought.** | Decision traces will expose explicit evidence, rules, versions, actions, and outcomes, not raw model CoT. | **YES** | `Participant_Case_Study.md` (Evidence discipline rules). |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| All non-negotiable constraints are explicitly addressed and compliant. | `START_HERE.md`, `source_authority.yaml` | `scqa-problem-frame.md` | High confidence (direct mapping). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: "Essential vessel operations" can be clearly defined and bounded for offline caching. | Exact list of offline-critical features pending. | FDE Team / Master | Dictates the scope of the vessel-edge deployment in Stage 10. | Stage 10 Deployment Topology. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved and justified use case
Do not advance to Stage 05 until the Stage 04 exit gate is defensible.