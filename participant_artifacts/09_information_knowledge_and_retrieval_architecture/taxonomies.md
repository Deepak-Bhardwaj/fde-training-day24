# Taxonomies

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer B: Semantic Foundation)
**Participant status:** COMPLETED
**Deliverable form:** Structured table / register

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To define the controlled vocabularies and enumerations used across the canonical model. Strict taxonomies prevent semantic drift and ensure the deterministic engine can reliably evaluate constraints without ambiguity.

## Upstream dependency
Use the completed Stage 05 Ubiquitous-Language Glossary and Stage 09 Semantic Model.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
Ensure every taxonomy explicitly supports the temporal provenance and authority weighting required by the architecture. 

## Minimum content

| Taxonomy Name | Enumerated Values | Definition / Usage Rule | Evidence |
| :--- | :--- | :--- | :--- |
| **Source Authority Level** | `HIGHEST`, `HIGH`, `MEDIUM`, `OBSERVATION`, `NON_AUTHORITATIVE` | Dictates conflict resolution. `HIGHEST` (Active Policy) overrides all. `NON_AUTHORITATIVE` (AI drafts) cannot be executed. | `source_authority.yaml` |
| **Constraint Severity** | `CRITICAL_HOLD`, `HIGH`, `MEDIUM`, `LOW` | `CRITICAL_HOLD` maps directly to CMMS active holds. Acts as an absolute feasibility blocker (BR-02). | `source_inventory.csv` (SRC-CMMS) |
| **Disruption Event Type** | `WEATHER`, `PORT_CONSTRAINT`, `MACHINERY_ALERT`, `SCHEDULE_DEVIATION`, `IDENTITY_CONFLICT` | Used to trigger specific recovery option generation logic. `IDENTITY_CONFLICT` triggers GS-04 resolution. | `live_disruptions.csv` |
| **Recovery Option Status** | `DRAFT`, `FEASIBLE`, `INFEASIBLE`, `PENDING_APPROVAL`, `APPROVED`, `REJECTED`, `EXECUTED` | `DRAFT` and `PENDING_APPROVAL` cannot be executed. Only `APPROVED` by Master transitions to `EXECUTED`. | `role_authorization_matrix.csv` |
| **Policy Document Status** | `ACTIVE`, `SUPERSEDED`, `DRAFT` | Only `ACTIVE` policies are loaded into the deterministic engine. `SUPERSEDED` are routed to Audit only (GS-12). | `source_authority.yaml` |
| **Data Freshness State** | `FRESH`, `STALE`, `EXPIRED`, `UNVERIFIED` | `STALE` triggers UI warning. `EXPIRED` removes constraint from feasibility check. `UNVERIFIED` requires manual Controller override. | `source_inventory.csv` (Freshness thresholds) |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| The `CRITICAL_HOLD` taxonomy value must trigger an absolute block in the engine. | `business-rules.md` (BR-02) | `canonical-entity-model.md` | High confidence (explicit policy). |
| Policy status must be strictly binary for operational use (ACTIVE vs not). | `source_authority.yaml` | `quality-profile.md` | High confidence (explicit policy). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: All source adapters will correctly map their native enums to these canonical taxonomies upon ingestion. | Legacy source systems may require custom mapping scripts. | FDE Team / Source Owners | Increases implementation effort in Stage 10. | Stage 09 Retrieval Source Adapters. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture