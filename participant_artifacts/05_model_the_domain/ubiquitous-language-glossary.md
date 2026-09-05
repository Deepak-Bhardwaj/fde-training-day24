# Ubiquitous-Language Glossary

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 05 — Model the Domain
**Participant status:** COMPLETED
**Deliverable form:** Structured table / register

## Stage question
What does the business actually mean, decide and own?

## Why this artifact exists
To establish a single, shared vocabulary across vessel crews, shore controllers, and engineering teams. This prevents the semantic conflicts (e.g., Port API "available" vs. Notice "confirmed") identified in Stage 02.

## Upstream dependency
Use the completed Stage 01 Governance RACI, Stage 02 System Landscape, and Stage 04 Use-Case Card.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/02_documents/fleet_operations_interview_notes.md`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
Define terms strictly based on business reality and policy, not technical implementation details.

## Minimum content

| Term | Definition | Synonyms / Anti-patterns | Authority / Source |
| :--- | :--- | :--- | :--- |
| **Disruption** | Any event that deviates from the planned voyage schedule or introduces new operational constraints (e.g., weather, machinery failure, port congestion). | Delay, Incident, Anomaly | `live_disruptions.csv` |
| **Recovery Option** | A proposed, evidence-backed alternative course of action to resolve a disruption (e.g., slow steaming, port skip, rerouting). | Plan, Fix, Solution | `fleet_operations_interview_notes.md` |
| **Technical Hold** | A mandatory restriction on vessel operation or voyage planning due to equipment condition, requiring explicit release by the Chief Engineer. | Maintenance flag, CMMS alert | `source_inventory.csv` (SRC-CMMS) |
| **Temporal Provenance** | The verifiable record of when a piece of data was observed at the source, when it was ingested, and its version history. | Timestamp, Log | `source_inventory.csv` (SRC-TELEM clock drift) |
| **Active Policy** | A fleet rule or guideline that is currently in effect and authorized for operational decision-making. Superseded policies are historical only. | Current rule, Latest doc | `source_authority.yaml` |
| **Master Authority** | The absolute, non-delegable right of the vessel Master to approve, modify, or reject any recovery option or navigational change. | Captain's call, Final say | `role_authorization_matrix.csv` |
| **Canonical Identity** | The single, authoritative source of truth for a vessel's identity and core metadata, overriding external observations. | True ID, Master Record | `source_authority.yaml` (FLEET_REGISTRY) |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| "Technical Hold" must be explicitly defined as a hard constraint, not a suggestion. | `source_inventory.csv` (SRC-CMMS authoritative for equipment condition) | `ctqs.md` | High confidence (explicit policy). |
| "Active Policy" must be distinguished from superseded documents to avoid retrieval traps. | `source_authority.yaml` (ACTIVE_FLEET_POLICY precedence: HIGHEST_FOR_POLICY) | `prohibited-use-check.md` | High confidence (explicit policy). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: All stakeholders will adopt this glossary and reject legacy, ambiguous terms (e.g., using "Plan" instead of "Recovery Option"). | Cultural adoption of new terminology is hard to enforce. | FDE Team / Fleet Controller | May require UI/UX enforcement (e.g., tooltips) in Stage 10. | Stage 10 Target C4 Views (UI specifications). |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Domain and decision model
Do not advance to Stage 06 until the Stage 05 exit gate is defensible.