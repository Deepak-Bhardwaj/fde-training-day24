# Brownfield Assessment

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench

**Stage:** 02 — Discover Process & Architecture

**Participant status:** COMPLETED

**Deliverable form:** Structured analysis / specification

## Stage question
How does the real brownfield process and system operate today?

## Why this artifact exists
This artifact is part of the evidence needed to reach **Current-state process and architecture baseline**. It must be consistent with approved upstream artifacts.

## Upstream dependency
Use the completed Stage 01 artifacts and Stage 02 System Landscape.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
Assess the constraints, technical debt, and integration challenges of the current brownfield environment. Identify what must be preserved, what can be refactored, and what is a hard constraint.

## Minimum content
- Constraint Category
- Description
- Impact on Future Design
- Preservation Requirement
- Evidence

## Working scaffold

| Constraint Category | Description | Impact on Future Design | Preservation Requirement | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **Data Freshness & Temporal Provenance** | Sources have varying freshness thresholds (5 min to 60 min) and suffer from clock drift. | Future architecture must implement strict temporal provenance and reconciliation logic. | Must preserve source-specific freshness rules and handle clock drift idempotently. | `source_inventory.csv` (SRC-TELEM clock drift, SRC-PORT 60 min freshness) |
| **Semantic Conflicts** | Port API semantics conflict with signed notices; superseded policies remain searchable. | Retrieval and context assembly must explicitly filter by authority and version, not just recency. | Must preserve signed notice authority over API; must filter `SRC-POLICY` by `status=ACTIVE`. | `fleet_operations_interview_notes.md`, `source_authority.yaml` |
| **Authority & Decision Rights** | Master and Chief Engineer hold absolute authority; AI is non-authoritative. | System must never auto-execute navigational commands or override technical holds. | Must preserve human-in-the-loop approval for all safety-critical actions. | `role_authorization_matrix.csv`, `source_authority.yaml` |
| **Offline Continuity** | Vessel and shore state may diverge during connectivity loss. | Architecture must support offline-first operation on vessel and safe reconciliation on reconnect. | Must preserve vessel-side decision-making capability without cloud/LLM dependency. | `fleet_operations_interview_notes.md` ("vessel and shore teams can each be correct") |
| **Data Privacy & Access Boundaries** | Crew data is highly restricted; Cargo data has commercial sensitivity. | System must implement role-based access control and tenant isolation. | Must preserve data minimization for Crew; purpose-filtered access for Cargo. | `source_inventory.csv` (SRC-CREW, SRC-CARGO access boundaries) |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Temporal provenance is a hard constraint due to clock drift and duplicate delivery. | `source_inventory.csv` (SRC-TELEM known issues) | `system-landscape.md` | High confidence (explicit source metadata). |
| Signed port notices supersede API status; this is a non-negotiable authority rule. | `source_authority.yaml` (PORT_NOTICE_DOC precedence: HIGH_FOR_PORT_CONSTRAINT) | `system-landscape.md` | High confidence (explicit policy). |
| Offline continuity is required due to vessel-to-shore divergence. | `fleet_operations_interview_notes.md` | `process-value-stream-map.md` | High confidence (SME interview). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: Vessel-side edge compute can handle full context assembly offline. | Exact edge compute specs not detailed in evidence. | Shore Platform Team | If edge compute is limited, architecture must shift to lightweight sync, not full offline. | Stage 10 AI & Application Architecture (deployment topology). |

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