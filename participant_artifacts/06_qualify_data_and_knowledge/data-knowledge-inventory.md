# Data / Knowledge Inventory

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 06 — Qualify Data & Knowledge
**Participant status:** COMPLETED
**Deliverable form:** Structured table / register

## Stage question
Is the evidence trustworthy, permissible, traceable, representative and ready?

## Why this artifact exists
To catalog all data and knowledge assets required by the domain model, mapping them to their authoritative sources, formats, and update patterns.

## Upstream dependency
Use the completed Stage 05 Bounded Contexts, Ownership Map, and Stage 01 Field Evidence Register.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
Map data assets strictly to the business domain entities defined in Stage 05. Do not invent data sources that do not exist in the evidence.

## Minimum content

| Domain Entity / Knowledge Asset | Authoritative Source (Source ID) | Physical Format | Update Pattern | Primary Consumer Context | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Vessel Identity & Metadata** | SRC-FMS (Fleet Registry) | Database/API | Transactional | All Contexts (Canonical Truth) | `source_inventory.csv`, `source_authority.yaml` |
| **Position Observations** | SRC-AIS | API/Stream | Stream (15 min freshness) | Shore Disruption Mgmt, Audit | `source_inventory.csv` |
| **Machinery/Fuel Signals** | SRC-TELEM | Edge Event Stream | Seconds/Minutes | Vessel Command, Shore Disruption | `source_inventory.csv` |
| **Port Berth/Pilot Constraints** | SRC-PORT | API + Documents (PDF) | Variable (60 min freshness) | Shore Disruption Mgmt (via ACL) | `source_inventory.csv`, `fleet_operations_interview_notes.md` |
| **Weather/Ocean Forecasts** | SRC-WX | API | Hourly (90 min freshness) | Shore Disruption Mgmt | `source_inventory.csv` |
| **Maintenance Holds** | SRC-CMMS | Database/API | Event/Transactional (15 min) | Vessel Command, Shore Disruption | `source_inventory.csv` |
| **Cargo Properties/Windows** | SRC-CARGO | Database/API | Transactional (30 min) | Shore Disruption Mgmt (Restricted) | `source_inventory.csv` |
| **Crew Availability/Rest** | SRC-CREW | Database/API | Transactional (60 min) | Shore Disruption Mgmt (Restricted) | `source_inventory.csv` |
| **Fleet Recovery/Authority Rules** | SRC-POLICY | Versioned Documents | Versioned (Status-based) | All Contexts (Read-Only) | `source_inventory.csv`, `source_authority.yaml` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Fleet Registry is the canonical source for vessel identity, overriding AIS. | `source_authority.yaml` (FLEET_REGISTRY precedence: HIGH) | `business-rules.md` (BR-06) | High confidence (explicit policy). |
| Port constraints exist in two conflicting formats (API and Documents), requiring an ACL. | `source_inventory.csv` (SRC-PORT known issues) | `ddd-context-map.md` | High confidence (explicit source metadata). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The "Versioned Documents" in SRC-POLICY can be reliably parsed into machine-readable rules. | Exact format of policy documents (e.g., PDF vs. structured XML) not fully detailed. | FDE Team / Fleet Safety | May require manual rule extraction or advanced NLP in Stage 09. | Stage 09 Knowledge Extraction Specification. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Data and knowledge readiness assessment
Do not advance to Stage 07 until the Stage 06 exit gate is defensible.