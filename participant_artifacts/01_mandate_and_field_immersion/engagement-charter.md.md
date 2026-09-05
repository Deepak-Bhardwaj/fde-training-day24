# Engagement Charter

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
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/02_documents/fleet_operations_interview_notes.md`
- `evidence/04_policy_authority/role_authorization_matrix.csv`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
Stay in the field problem and ownership space. Do not propose a model, graph database, agent or UI in this artifact.

## Minimum content

| Problem/opportunity | Business outcome | Engagement boundaries | Decision rights | Working assumptions | Evidence plan |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Reconciling disruption evidence is slow and error-prone due to conflicting, stale, or semantically ambiguous data sources during vessel-to-shore connectivity loss. | Safe, evidence-backed recovery options that preserve Master's authority and ensure offline continuity. | Synthetic training only. No live navigation/command. AI cannot issue navigational commands. Critical CMMS holds are absolute constraints. | Master holds absolute authority over navigation/recovery. Chief Engineer owns technical releases. FDE owns technical design integrity. | Port API semantics conflict with signed notices. AI output is strictly non-authoritative (recommendation only). | Inspect source inventory, interview notes, and role authorization matrix to map authority and data freshness limits. |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Reconciling data versions is the primary bottleneck, not data access. | `evidence/02_documents/fleet_operations_interview_notes.md` (Line: "slowest part is... reconciling which version is current") | N/A (Stage 01) | High confidence (direct SME interview). |
| AI output has zero authoritative precedence. | `evidence/04_policy_authority/source_authority.yaml` (AI_OUTPUT precedence: NON_AUTHORITATIVE) | N/A (Stage 01) | High confidence (explicit policy). |
| Master retains final approval and navigation change authority. | `evidence/04_policy_authority/role_authorization_matrix.csv` (MASTER: approve_recovery_plan=YES, authorize_navigation_change=YES) | N/A (Stage 01) | High confidence (explicit policy). |
| Port API semantics conflict with signed documents. | `evidence/02_documents/fleet_operations_interview_notes.md` (Line: "Port API fields use different meanings...") & `source_inventory.csv` (SRC-PORT known issues) | N/A (Stage 01) | Medium confidence (requires runtime version checking). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: Vessel-side workbench can operate fully offline for critical recovery comparisons. | Requires validation of edge compute constraints not yet detailed in evidence. | FDE Team / Shore Platform | If false, architecture must shift to ultra-low-bandwidth sync, not full offline. | Stage 10 AI & Application Architecture edge deployment specs. |
| Issue: Clock drift between SRC-TELEM and shore systems. | Noted in `source_inventory.csv`, but exact reconciliation logic not yet defined. | FDE Team | Impacts idempotency and duplicate event handling (GS-07, GS-13). | Stage 09 Information Architecture temporal provenance rules. |

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