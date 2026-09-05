# Semantic Model

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer B: Semantic Foundation)
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To define the semantic layer that translates raw, heterogeneous data from the 9 enterprise sources into the unified business concepts defined in the Stage 05 Ubiquitous Language.

## Upstream dependency
Use the completed Stage 05 Ubiquitous-Language Glossary and Stage 09 Source-to-Canonical Mapping.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/02_documents/fleet_operations_interview_notes.md`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
Explicitly resolve semantic clashes at the model level. The model must not allow ambiguous terms (like "available") to exist without an explicit authority context.

## Minimum content

| Raw Source Concept | Canonical Semantic Concept | Semantic Translation Rule | Authority Context | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| Port API `berth_status = 'open'` | **Constraint.port_availability** | Mapped to `UNVERIFIED` state. Cannot be used for final feasibility without secondary validation. | MEDIUM (SRC-PORT API) | `fleet_operations_interview_notes.md` |
| Port Notice PDF `text contains 'berth confirmed'` | **Constraint.port_availability** | Mapped to `CONFIRMED` state. Overrides API `UNVERIFIED` state. | HIGH (SRC-PORT Notice) | `source_authority.yaml` |
| Telemetry `engine_temp > threshold` | **Disruption.machinery_alert** | Triggers a `DisruptionDetected` event. Does not automatically create a `TechnicalHold`. | OBSERVATION (SRC-TELEM) | `source_inventory.csv` |
| CMMS `work_order_status = 'critical_open'` | **Constraint.technical_hold** | Mapped to `ACTIVE_HOLD`. Acts as an absolute blocker in the deterministic engine. | HIGH (SRC-CMMS) | `business-rules.md` (BR-02) |
| FMS `voyage_status = 'delayed'` | **Disruption.schedule_deviation** | Mapped to a schedule deviation. Requires linking to a root cause (Weather, Port, or CMMS). | HIGH (SRC-FMS) | `source_authority.yaml` |
| Policy `document_text = 'master must...'` | **Rule.master_authority_constraint** | Extracted as a governance rule. Tagged with `version_id` and `status = ACTIVE`. | HIGHEST (SRC-POLICY) | `source_authority.yaml` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Port API "open" must be semantically downgraded to "UNVERIFIED" to prevent false positives. | `fleet_operations_interview_notes.md` | `target-information-trust-boundaries.md` | High confidence (SME interview). |
| Telemetry alerts are observations, not authoritative constraints, until validated. | `source_inventory.csv` (SRC-TELEM not authoritative for maintenance release) | `source-to-canonical-mapping.md` | High confidence (explicit source metadata). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The semantic translation rules can be fully codified in a deterministic rules engine without requiring ML inference. | Some edge cases in port notice text might be highly ambiguous. | FDE Team | If deterministic rules fail, the human-in-the-loop fallback queue will increase. | Stage 09 Knowledge Extraction Specification. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture
Do not advance to the next sub-layer until this artifact is defensible.