# Business Rules

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench  
**Stage:** 05 — Model the Domain  
**Participant status:** `TO COMPLETE`  
**Deliverable form:** Structured table / register

## Stage question
What does the business actually mean, decide and own?

## Why this artifact exists
This artifact is part of the evidence needed to reach **Domain and decision model**. It must be consistent with approved upstream artifacts; do not silently redefine earlier facts, semantics, thresholds or decision rights.

## Upstream dependency
Use the completed Stage 04 artifacts and explicitly referenced earlier artifacts. Never copy them into this file simply to satisfy a checklist.

## Evidence to inspect
- `evidence/03_semantic_evidence/identifier_crosswalk.csv`
- `evidence/03_semantic_evidence/relationship_clues.csv`
- `evidence/03_semantic_evidence/kpi_definition_candidates.csv`
- `evidence/03_semantic_evidence/source_schema_dictionary.csv`
- `evidence/03_semantic_evidence/conflicting_terms.csv`
- `evidence/02_documents/ai_decision_support_policy.md`
- `evidence/02_documents/offline_continuity_and_sync_policy.md`
- `evidence/02_documents/data_permissible_use_policy.md`
- `evidence/02_documents/superseded_fleet_recovery_policy_v3_7_REFERENCE_ONLY.md`
- `evidence/02_documents/fleet_recovery_policy_v4_1.md`
- `evidence/02_documents/navigation_and_command_authority_policy.md`
- `evidence/02_documents/external_message_trust_policy.md`
- `evidence/02_documents/cargo_and_safety_priority_policy.md`

## Case challenge
Resolve business meaning around Vessel, Voyage, Disruption, AIS Observation, Telemetry Observation. Preserve source-specific meanings where they are genuinely different rather than forcing false canonicalization.

## Minimum content
- Rule ID
- Rule
- Authority/source
- Deterministic/advisory
- Exception
- Version

## Relevant non-negotiable constraints
- AI cannot issue or execute navigational commands or replace the Master's command authority.
- Critical maintenance holds are hard feasibility constraints until authorized technical release.

## Working scaffold
| Rule ID | Rule | Authority/source | Deterministic/advisory | Exception | Version |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

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
**Stage exit contribution:** Domain and decision model

Do not advance to Stage 06 until the Stage 05 exit gate is defensible.
