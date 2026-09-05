# Lineage

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench  
**Stage:** 06 — Qualify Data & Knowledge  
**Participant status:** `TO COMPLETE`  
**Deliverable form:** Structured narrative + evidence table

## Stage question
Is the evidence trustworthy, permissible, traceable, representative and ready?

## Why this artifact exists
This artifact is part of the evidence needed to reach **Data and knowledge readiness assessment**. It must be consistent with approved upstream artifacts; do not silently redefine earlier facts, semantics, thresholds or decision rights.

## Upstream dependency
Use the completed Stage 05 artifacts and explicitly referenced earlier artifacts. Never copy them into this file simply to satisfy a checklist.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/01_enterprise_sources/source_health_events.jsonl`
- `evidence/04_policy_authority/source_authority.yaml`
- `evidence/04_policy_authority/data_access_rules.yaml`
- `evidence/03_semantic_evidence/source_schema_dictionary.csv`

## Case challenge
Treat authority, permissible use, freshness, lineage, representativeness and known source defects as readiness dimensions—not merely file availability.

## Minimum content
- Data/fact
- Origin
- Transformations
- Stores
- Consumers
- Version/time
- Gap

## Relevant non-negotiable constraints
- AI cannot issue or execute navigational commands or replace the Master's command authority.
- Vessel and shore state may diverge during connectivity loss and must reconcile safely on reconnect.
- AIS observations do not automatically override canonical fleet identity.

## Working scaffold
| Data/fact | Origin | Transformations | Stores | Consumers | Version/time | Gap |
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
**Stage exit contribution:** Data and knowledge readiness assessment

Do not advance to Stage 07 until the Stage 06 exit gate is defensible.
