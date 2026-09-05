# Sponsor / Owner

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench

**Stage:** 01 — Mandate & Field Immersion

**Participant status:** COMPLETED

**Deliverable form:** Structured narrative + evidence table

## Stage question
Why are we here, what outcome matters, who owns it, and who is affected?

## Why this artifact exists
This artifact is part of the evidence needed to reach **Approved mandate and operating context**. It must be consistent with approved upstream artifacts; do not silently redefine earlier facts, semantics, thresholds or decision rights.

## Upstream dependency
Use the case pack and supplied evidence. No solution architecture is an input to Stage 01.

## Evidence to inspect
- `evidence/04_policy_authority/role_authorization_matrix.csv`
- `evidence/04_policy_authority/source_authority.yaml`
- `START_HERE.md`

## Case challenge
Stay in the field problem and ownership space. Do not propose a model, graph database, agent or UI in this artifact.

## Minimum content

| Role | Name / Title | Accountability | Authority | Evidence basis |
| :--- | :--- | :--- | :--- | :--- |
| Executive Sponsor | VP of Fleet Operations / Director of Maritime Safety & Compliance (MeridianBlue Shipping) | Strategic mandate, safety policy alignment, preservation of Master's authority. | Final approval of training boundaries and architectural recommendations. | `START_HERE.md` (synthetic training mandate), `role_authorization_matrix.csv` (SAFETY_OFFICER role). |
| Operational Owner | Lead Forward Deployment Engineer (FDE) / Embedded AI FDE Team | Technical delivery, evidence discipline, artifact integrity, Golden Scenario validation. | Technical design decisions, artifact sign-off, "NO AGENT" recommendation if justified. | `Participant_Runbook.md` (FDE responsibility to "build a defensible solution from evidence"). |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Executive Sponsor prioritizes safety over automation. | `START_HERE.md` (Line: "Synthetic training case only; not for navigation, vessel command or live fleet operations") | N/A (Stage 01) | High confidence (explicit mandate). |
| FDE owns technical delivery and evidence discipline. | `Participant_Runbook.md` (Line: "Your responsibility is to build a defensible solution from evidence") | N/A (Stage 01) | High confidence (explicit assignment). |
| AI output is non-authoritative; human authority is preserved. | `source_authority.yaml` (AI_OUTPUT precedence: NON_AUTHORITATIVE) | N/A (Stage 01) | High confidence (explicit policy). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: Executive Sponsor will approve "NO AGENT" recommendation if evidence dictates. | Not explicitly stated in current evidence, but implied by evidence-first approach. | FDE Team / Executive Sponsor | If Sponsor demands an agent regardless of evidence, it violates the case study's evidence discipline. | Stage 11 Agentic & Multi-Agent Orchestration (agent-suitability-assessment.md). |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.
- [x] `NOT APPLICABLE`, if used, includes rationale, accountable approver and downstream consequence.

## Handoff
**Stage exit contribution:** Approved mandate and operating context

Do not advance to Stage 02 until the Stage 01 exit gate is defensible.