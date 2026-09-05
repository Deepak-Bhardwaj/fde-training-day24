# Selected Solution

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 08 — Generate, Test & Select Options
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
Which solution survives evidence, alternatives and trade-offs?

## Why this artifact exists
To provide the definitive, formal record of the selected solution, its architecture, its conditions, and the explicit trade-offs accepted. This document serves as the binding contract between the FDE team and the Executive Sponsor for all downstream design work.

## Upstream dependency
Use all completed Stage 01 through Stage 08 artifacts.

## Evidence to inspect
- `Participant_Case_Study.md` (Non-negotiable constraints)
- `evidence/04_policy_authority/role_authorization_matrix.csv`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
Summarize the entire solution selection journey in a single, defensible document. Do not introduce new scope or technical details that were not evaluated in earlier artifacts.

## Minimum content

### 1. Solution Name
**Fleet Disruption & Voyage Recovery Intelligence Workbench — Hybrid Deterministic Architecture**

### 2. Solution Summary
An event-driven, hybrid architecture that combines a **deterministic constraint engine** (for safety-critical feasibility checking) with a **bounded NLP extraction service** (for unstructured document parsing), deployed across a **shore-side platform** and a **vessel-edge runtime**. The system reconciles disruption evidence from 9 enterprise sources, enforces strict source authority and temporal provenance, and presents ranked, evidence-backed recovery options to Fleet Controllers and the Master for human approval.

### 3. Core Architectural Decisions
| ADR | Decision | Rationale |
| :--- | :--- | :--- |
| ADR-001 | Event-Driven Hybrid (Shore + Edge) | Offline continuity (GS-14) and safe reconciliation (GS-15). |
| ADR-002 | Deterministic Core | Zero hallucination risk for safety-critical constraints. |
| ADR-003 | Bounded NLP with Human Fallback | Automates #1 bottleneck while preserving safety. |
| ADR-004 | Temporal Provenance Envelope | Guarantees idempotency and auditability. |

### 4. Non-Negotiable Constraints Satisfied
| Constraint | How Satisfied |
| :--- | :--- |
| AI cannot issue navigational commands | AI is strictly NON_AUTHORITATIVE. Master holds absolute veto (BR-01). |
| CMMS holds are absolute | Deterministic engine enforces BR-02. No override capability exists. |
| Offline continuity required | Vessel edge runs deterministic engine on cached canonical data (ADR-001). |
| Idempotent event handling | Provenance envelope and composite key deduplication (ADR-004). |
| No hidden chain-of-thought | Decision traces expose evidence, rules, versions, actions, and outcomes only. |

### 5. Conditions & Dependencies
| Condition | Owner | Downstream Impact |
| :--- | :--- | :--- |
| NLP vendor must provide SLA >90% precision OR human fallback is mandatory. | FDE Team / Vendor | Stage 09 Retrieval Architecture must implement confidence-based routing. |
| Vessel edge compute must support deterministic engine + cached state. | Shore Platform Team | Stage 10 Deployment Topology must validate hardware specs. |
| CMMS Asset ID mapping must be resolved or manual fallback implemented. | Technical Operations | Stage 09 Entity Resolution must handle mapping discrepancies. |

### 6. Explicit Trade-Offs Accepted
| Trade-Off | Accepted Risk | Mitigation |
| :--- | :--- | :--- |
| Increased implementation complexity (Hybrid vs. Pure Deterministic) | Higher development cost and longer timeline. | Phased rollout: Phase 1 (Deterministic Core only), Phase 2 (Add NLP). |
| NLP extraction accuracy risk | Incorrect constraints could enter the engine. | Mandatory human-in-the-loop fallback for low-confidence extractions. |
| Provenance envelope payload overhead (~15%) | Increased bandwidth usage during sat-com sync. | Delta-sync and compression for vessel-to-shore event batches. |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| The selected solution satisfies all non-negotiable constraints. | `Participant_Case_Study.md` | `go-no-go-kill-criteria.md` | High confidence (explicit mapping). |
| The solution is conditionally viable based on NLP vendor SLA and edge compute. | `poc-model-rag-results.md`, `provider-comparison.md` | `weighted-tradeoff-matrix.md` | High confidence (explicit conditions). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The phased rollout (Phase 1: Deterministic, Phase 2: NLP) is acceptable to the Executive Sponsor. | Timeline and budget constraints not fully quantified. | Executive Sponsor | If Sponsor demands full capability in Phase 1, risk increases significantly. | Stage 10 Architecture ADRs (Phasing decision). |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved solution and trade-offs
Do not advance to Stage 09 until the Stage 08 exit gate is defensible.