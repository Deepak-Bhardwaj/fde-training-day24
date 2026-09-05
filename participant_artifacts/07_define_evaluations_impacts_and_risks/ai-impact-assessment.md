# AI Impact Assessment

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench  
**Stage:** 07 — Define Evaluations, Impacts & Risks  
**Participant status:** `TO COMPLETE`  
**Deliverable form:** Structured analysis / specification

## Stage question
What must the future system prove before it is acceptable?

## Why this artifact exists
This artifact is part of the evidence needed to reach **Evaluation, impact and risk requirements**. It must be consistent with approved upstream artifacts; do not silently redefine earlier facts, semantics, thresholds or decision rights.

## Upstream dependency
Use the completed Stage 06 artifacts and explicitly referenced earlier artifacts. Never copy them into this file simply to satisfy a checklist.

## Evidence to inspect
- `evidence/06_evaluations/golden_scenarios.json`
- `evidence/06_evaluations/expected_behaviors.json`
- `evidence/06_evaluations/evaluation_matrix.csv`
- `evidence/06_evaluations/acceptance_thresholds.yaml`
- `evidence/04_policy_authority/role_authorization_matrix.csv`
- `evidence/04_policy_authority/decision_constraints.yaml`

## Case challenge
Turn the supplied golden scenarios (GS-02, GS-03, GS-04, GS-05, GS-07, GS-08, GS-09, GS-14, GS-15) into hard gates and quality tests. A good average score cannot compensate for a hard safety/authority/privacy failure.

## Minimum content
- Affected group
- Benefit
- Harm
- Severity
- Likelihood
- Control
- Residual impact
- Review trigger

## Relevant non-negotiable constraints
- Critical maintenance holds are hard feasibility constraints until authorized technical release.
- Cloud/LLM availability must not be required for essential vessel operations.
- Vessel and shore state may diverge during connectivity loss and must reconcile safely on reconnect.

## Working scaffold
| Affected group | Benefit | Harm | Severity | Likelihood | Control | Residual impact | Review trigger |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

## Evidence and traceability
| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
|---|---|---|---|
| | | | |

## Open issues / assumptions
| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
|---|---|---|---|---|
| | | | | |

## Completion check
- [ ] Minimum content above is complete.
- [ ] Material claims cite exact evidence or are labelled assumptions.
- [ ] Conflicting/stale evidence is preserved rather than silently resolved.
- [ ] Human, deterministic and AI decision rights are distinguishable where relevant.
- [ ] The artifact does not contradict approved upstream artifacts.
- [ ] `NOT APPLICABLE`, if used, includes rationale, accountable approver and downstream consequence.

## Handoff
**Stage exit contribution:** Evaluation, impact and risk requirements

Do not advance to Stage 08 until the Stage 07 exit gate is defensible.
