# Ownership Map

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 05 — Model the Domain
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
What does the business actually mean, decide and own?

## Why this artifact exists
To explicitly map every core domain entity to its authoritative owner, ensuring that data writes and decision rights are strictly governed and do not overlap in conflicting ways.

## Upstream dependency
Use the completed Stage 01 Governance RACI, Stage 04 Impact/Regulatory Screen, and Stage 05 Business Rules.

## Evidence to inspect
- `evidence/04_policy_authority/role_authorization_matrix.csv`
- `evidence/04_policy_authority/source_authority.yaml`
- `evidence/01_enterprise_sources/source_inventory.csv`

## Case challenge
Prevent "shared ownership" anti-patterns. Every entity must have exactly one authoritative writer, even if multiple systems read it.

## Minimum content

| Domain Entity / Data Concept | Authoritative Owner (Writer) | Read-Only Consumers | Access Boundary / Restrictions | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **Vessel Navigational State** | Master / Bridge Team | Shore Platform, Fleet Controller, Audit System | Vessel-side absolute; shore can only observe, not write. | `role_authorization_matrix.csv` |
| **Critical Maintenance Holds** | Chief Engineer | Deterministic Engine, Fleet Controller, Master | Read by all planning systems; write restricted to Technical Ops. | `source_inventory.csv` (SRC-CMMS) |
| **Active Fleet Policy** | Fleet Safety & Compliance | Deterministic Engine, Retrieval Layer, Audit System | Versioned; only ACTIVE status is readable by planning engines. | `source_authority.yaml` |
| **Recovery Option Drafts** | Deterministic Engine / AI (Non-Auth) | Fleet Controller, Master | AI drafts are marked NON_AUTHORITATIVE; Controller can edit/select. | `source_authority.yaml`, `non-ai-alternative.md` |
| **Approved Recovery Plan** | Master (via Fleet Controller coordination) | Vessel Execution Systems, Audit System, Port Ops | Immutable once approved; triggers execution. | `role_authorization_matrix.csv` |
| **Crew Rest / Availability** | Marine HR / Crew System | Deterministic Engine (Constraint Check only) | Highly restricted; AI is prohibited from making personnel decisions. | `source_inventory.csv` (SRC-CREW) |
| **Cargo Constraints / Priorities** | Cargo Operations | Deterministic Engine, Fleet Controller | Commercial sensitivity; strict tenant isolation required. | `source_inventory.csv` (SRC-CARGO) |
| **Port Constraints (Signed)** | External Port Authority | Shore Platform, Deterministic Engine | Supersedes Port API; treated as high-trust external input. | `source_authority.yaml` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Vessel Navigational State is exclusively owned by the Master. | `role_authorization_matrix.csv` (MASTER authorize_navigation_change=YES) | `trust-boundaries.md` | High confidence (explicit policy). |
| Crew data is strictly isolated and cannot be used for AI personnel decisions. | `source_inventory.csv` (SRC-CREW access boundary) | `impact-regulatory-screen.md` | High confidence (explicit policy). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The "Deterministic Engine" is treated as a system actor, but its logic is ultimately owned by the FDE/Safety team. | System ownership vs. business ownership distinction. | FDE Team / Safety Officer | Requires clear handoff from FDE to Shore Platform for ongoing maintenance. | Stage 10 Architecture ADRs. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Domain and decision model
Do not advance to Stage 06 until the Stage 05 exit gate is defensible.