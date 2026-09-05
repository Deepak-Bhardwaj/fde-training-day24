# Current-State Trust Boundaries

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench

**Stage:** 02 — Discover Process & Architecture

**Participant status:** COMPLETED

**Deliverable form:** Structured narrative + evidence table

## Stage question
How does the real brownfield process and system operate today?

## Why this artifact exists
This artifact is part of the evidence needed to reach **Current-state process and architecture baseline**. It must be consistent with approved upstream artifacts; do not silently redefine earlier facts, semantics, thresholds or decision rights.

## Upstream dependency
Use the completed Stage 01 artifacts and Stage 02 System Landscape / C4 Views.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/04_policy_authority/role_authorization_matrix.csv`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
Identify where data, authority, and system trust change levels in the current architecture. Highlight where current boundaries fail to enforce the non-negotiable constraints of the case.

## Minimum content
- Boundary Name
- From (Lower Trust / External)
- To (Higher Trust / Internal)
- Current Trust Assumption
- Enforcement Mechanism (Current State)
- Evidence

## Working scaffold

| Boundary Name | From | To | Current Trust Assumption | Enforcement Mechanism (Current State) | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **External Provider Ingestion** | Port API, WX API, AIS Stream | Shore Platform / FMS | External data is treated as factual observation, not absolute truth. | Manual semantic reconciliation by Fleet Controller; API schema validation. | `source_inventory.csv`, `source_authority.yaml` |
| **AI / Tool Output to Human** | Recovery Option Generator / AI Tools | Fleet Controller / Master | AI output is a draft/recommendation, never authoritative. | Human-in-the-loop review; Master holds absolute veto/approval authority. | `role_authorization_matrix.csv` (AI_AGENT commit=NO), `source_authority.yaml` |
| **Shore to Vessel Command** | Shore Platform / Fleet Controller | Vessel Systems / Master | Shore can suggest, but cannot execute or override vessel command. | Sat-com messaging; Master manually inputs approved changes to vessel systems. | `role_authorization_matrix.csv` (MASTER authorize_navigation_change=YES) |
| **Policy Engine to Execution** | Fleet Policy Repository | FMS / Recovery Generator | Only ACTIVE policies are authoritative; superseded are historical. | Manual filtering by Controller; system lacks automated version/status enforcement. | `source_authority.yaml` (ACTIVE_FLEET_POLICY precedence: HIGHEST) |
| **Vessel Edge to Shore Core** | Vessel Telemetry Edge | Shore Platform | Vessel data is authoritative for local state, but subject to clock drift. | Timestamp validation; manual reconciliation upon reconnect. | `source_inventory.csv` (SRC-TELEM clock drift) |
| **Commercial Data to Operations** | Cargo System, Crew System | FMS / Voyage Planner | Commercial/Personal data is restricted by purpose and tenant. | Role-based access control (RBAC); purpose-filtered views. | `source_inventory.csv` (SRC-CARGO, SRC-CREW access boundaries) |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| AI output is strictly non-authoritative; humans must approve all actions. | `source_authority.yaml` (AI_OUTPUT precedence: NON_AUTHORITATIVE) & `role_authorization_matrix.csv` | `brownfield-assessment.md` | High confidence (explicit policy). |
| Shore systems cannot execute navigational commands; Master retains absolute authority. | `role_authorization_matrix.csv` (MASTER authorize_navigation_change=YES; AI_AGENT=NO) | `governance-raci.md` | High confidence (explicit policy). |
| Superseded policies remain searchable, creating a trust boundary risk in retrieval. | `source_inventory.csv` (SRC-POLICY known issues) | `dependencies.md` | High confidence (explicit source metadata). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: Current RBAC for Cargo/Crew data is strictly enforced at the database level. | Exact RBAC implementation details not provided in evidence. | Marine HR / Cargo Ops | If RBAC is weak, future architecture must implement strict tenant isolation and purpose-filtering at the retrieval layer. | Stage 06 Qualify Data & Knowledge (Permissible-Use / Access Matrix). |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.
- [x] `NOT APPLICABLE`, if used, includes rationale, accountable approver and downstream consequence.

## Handoff
**Stage exit contribution:** Current-state process and architecture baseline

Do not advance to Stage 03 until the Stage 02 exit gate is defensible.