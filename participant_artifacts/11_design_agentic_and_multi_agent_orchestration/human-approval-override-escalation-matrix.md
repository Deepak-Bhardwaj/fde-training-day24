# Human Approval / Override / Escalation Matrix

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 11 — Agentic & Multi-Agent Orchestration
**Participant status:** COMPLETED
**Deliverable form:** Structured table / register

## Stage question
Is autonomy justified, bounded, permissioned, interruptible and testable?

## Why this artifact exists
To define the exact conditions under which human operators must approve, can override, or must escalate a system-generated recommendation. This is the ultimate safeguard ensuring the system remains strictly Level 1/Level 2 autonomy.

## Upstream dependency
Use the completed Stage 05 Decision Model, Stage 11 State-Machine Model, and Stage 10 Failure-Mode Design.

## Evidence to inspect
- `evidence/04_policy_authority/role_authorization_matrix.csv`
- `Participant_Case_Study.md` (GS-02: Severe weather and Master authority, GS-08: Unauthorized shore commit)

## Case challenge
Prevent "automation bias" by explicitly defining scenarios where the human *must* override the system, and ensuring the system cannot bypass human approval under any circumstances.

## Minimum content

| Scenario / Trigger | System Action | Required Human Approval | Override Capability | Escalation Path | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **NLP Extraction Confidence < 0.95** | Routes to HITL Queue. Blocks automatic graph write. | **Fleet Controller** must manually review, edit, and approve the extracted data. | Controller can Reject or completely rewrite the extraction. | Escalate to Shore Data Steward if source format is consistently failing. | `knowledge-extraction-specification.md` |
| **Recovery Option Generation** | Engine generates ranked feasible options. | **Fleet Controller** selects the preferred option to present to the Master. | Controller can Reject all options and request manual workarounds. | Escalate to Fleet Operations Director if no feasible options exist. | `decision-model.md` |
| **Plan Execution Authorization** | Option is in `PENDING_APPROVAL` state. | **Master** must provide explicit cryptographic/procedural sign-off. | **Absolute Veto:** Master can Reject the plan entirely. | Escalate to Shore Fleet Controller via voice/radio for alternative options. | `role_authorization_matrix.csv` |
| **CMMS Technical Hold Detected** | Engine marks option as `INFEASIBLE`. | **NONE** (System blocks automatically). | **NONE.** System cannot be overridden to bypass a critical hold. | Chief Engineer must physically inspect and formally release the hold in CMMS. | `business-rules.md` (BR-02) |
| **Stale Data Warning (e.g., WX > 90m)** | Flags option with `REDUCED_CONFIDENCE`. | **Master / Controller** must explicitly acknowledge the stale data warning before proceeding. | Human can choose to proceed with caution or abort. | Escalate to external provider or wait for data refresh. | `context-freshness-policy.md` |

### Explicit "No Override" Zones
To prevent unauthorized shore commits (GS-08) or safety violations, the following system behaviors are **HARD-LOCKED** and cannot be overridden by any human or automated actor:
1. An AI/NLP output cannot be promoted to `AUTHORITATIVE` status.
2. A `RecoveryOption` cannot transition to `EXECUTED` without a valid `Master` identity signature.
3. An `ACTIVE` CMMS hold cannot be ignored by the feasibility engine.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| The Master holds absolute veto power, serving as the ultimate override. | `role_authorization_matrix.csv` | `autonomy-level-adr.md` | High confidence (explicit policy). |
| CMMS holds are hard constraints with zero override capability. | `business-rules.md` (BR-02) | `semantic-constraints.md` (SC-03) | High confidence (non-negotiable constraint). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The UI clearly communicates the "No Override" zones to prevent operators from attempting futile workarounds. | UI/UX usability testing NOT RUN. | FDE Team | Poor UX may lead to operator frustration or attempts to bypass the system via shadow IT. | Stage 10 Target C4 Views. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved, bounded and testable agentic architecture

**FINAL CASE STUDY EXIT:** All 134 artifacts across 11 stages are complete. The Fleet Disruption & Voyage Recovery Intelligence Workbench architecture is fully specified, defensible, and strictly aligned with all non-negotiable constraints.