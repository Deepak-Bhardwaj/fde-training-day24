# Batch / Stream / Runtime Data Flows

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench  
**Stage:** 09 — Information, Knowledge & Retrieval Architecture  
**Stage 9 sublayer:** H. Target Information Architecture  
**Participant status:** `TO COMPLETE`  
**Deliverable form:** Diagram + supporting table + rationale

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
This artifact is part of the evidence needed to reach **Approved information architecture**. It must be consistent with approved upstream artifacts; do not silently redefine earlier facts, semantics, thresholds or decision rights.

## Upstream dependency
Use the completed Stage 08 artifacts and explicitly referenced earlier artifacts. Never copy them into this file simply to satisfy a checklist.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/03_semantic_evidence/conflicting_terms.csv`
- `evidence/03_semantic_evidence/identifier_crosswalk.csv`
- `evidence/03_semantic_evidence/relationship_clues.csv`
- `evidence/04_policy_authority/source_authority.yaml`
- `evidence/04_policy_authority/data_access_rules.yaml`
- `evidence/05_history_feedback/operator_interactions.jsonl`
- `evidence/05_history_feedback/historical_decisions.jsonl`
- `evidence/05_history_feedback/voyage_outcomes.csv`
- `evidence/05_history_feedback/historical_incident_narratives.jsonl`
- `evidence/05_history_feedback/README.md`
- `evidence/05_history_feedback/authorized_overrides.csv`
- `participant_artifacts/05_model_the_domain`
- `participant_artifacts/06_qualify_data_and_knowledge`

## Case challenge
Design the target information architecture as a transformation of Stage 5–8 evidence; do not duplicate the Stage 6 inventory or redefine Stage 5 business language without an explicit decision.

## Minimum content
- Producer
- Consumer
- Data/event
- Timing
- Transform
- Security/trust boundary
- Failure/retry

## Relevant non-negotiable constraints
- AI cannot issue or execute navigational commands or replace the Master's command authority.
- Vessel and shore state may diverge during connectivity loss and must reconcile safely on reconnect.
- AIS observations do not automatically override canonical fleet identity.

## Working scaffold
| Producer | Consumer | Data/event | Timing | Transform | Security/trust boundary | Failure/retry |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

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
**Stage exit contribution:** Approved information architecture

Do not advance to Stage 10 until the Stage 09 exit gate is defensible.
