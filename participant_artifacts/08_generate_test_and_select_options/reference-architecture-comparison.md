# Reference-Architecture Comparison

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 08 — Generate, Test & Select Options
**Participant status:** COMPLETED
**Deliverable form:** Diagram + supporting table + rationale

## Stage question
Which solution survives evidence, alternatives and trade-offs?

## Why this artifact exists
To compare high-level architectural patterns against the non-negotiable constraints, specifically focusing on offline continuity (GS-14) and safe reconciliation (GS-15).

## Upstream dependency
Use the completed Stage 05 DDD Context Map and Stage 07 Risk Treatment Plan.

## Evidence to inspect
- `evidence/02_documents/fleet_operations_interview_notes.md`
- `evidence/01_enterprise_sources/source_inventory.csv`

## Case challenge
Evaluate architectures based on their ability to survive connectivity loss, not just their performance in a connected, ideal state.

## Diagram Description (Architectural Patterns)
*(Text-based representation)*
- **Pattern A: Shore-Centric Monolith.** All logic, data, and UI reside in the cloud. Vessel is a "dumb terminal" relying on continuous sat-com.
- **Pattern B: Event-Driven Hybrid (Shore + Edge).** Shore handles heavy ingestion, NLP extraction, and fleet-wide analytics. Vessel Edge runs a lightweight, deterministic constraint engine with cached canonical data, operating autonomously during blackouts.
- **Pattern C: Fully Decentralized Mesh.** Every vessel runs a full replica of the shore platform, including heavy NLP/LLM components.

## Working scaffold

| Architecture Pattern | Offline Capability (GS-14) | Reconciliation Safety (GS-15) | Compute Footprint | Verdict | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Pattern A: Shore-Centric** | **FAIL.** Vessel loses all decision support during blackout. | N/A (Fails prior) | Low (Vessel) / High (Shore) | **Rejected** | `fleet_operations_interview_notes.md` (vessel/shore divergence) |
| **Pattern B: Event-Driven Hybrid** | **PASS.** Vessel Edge runs deterministic engine on cached canonical constraints. | **PASS.** Temporal provenance and event-sourcing allow safe, idempotent merge on reconnect. | Medium (Vessel) / High (Shore) | **Selected** | `ddd-context-map.md`, `ctqs.md` |
| **Pattern C: Decentralized Mesh** | **PASS.** Full capability offline. | **RISKY.** High risk of state divergence and complex conflict resolution. | Very High (Vessel) | **Rejected** | `data-gap-register.md` (DG-01: vessel compute limits) |

## Rationale
Pattern B (Event-Driven Hybrid) is the only architecture that satisfies the non-negotiable constraint of offline continuity without introducing the massive compute burden and state-divergence risks of a fully decentralized mesh. It cleanly separates the heavy, AI-assisted ingestion (Shore) from the safety-critical, deterministic execution (Vessel Edge), aligning perfectly with the Bounded Contexts defined in Stage 05.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Shore-centric architectures fail the mandatory offline continuity requirement. | `fleet_operations_interview_notes.md` | `risk-treatment-plan.md` (RH-04) | High confidence (SME interview). |
| Event-driven hybrid architecture supports safe, idempotent reconciliation via temporal provenance. | `source_inventory.csv` (SRC-TELEM) | `provenance-baseline.md` | High confidence (architectural pattern match). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The vessel edge has sufficient compute to run the deterministic constraint engine and cache the canonical state. | Exact hardware specs pending. | Shore Platform Team | If edge compute is lower than expected, the cached state must be aggressively minimized. | Stage 10 Deployment Topology. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved solution and trade-offs
Do not advance to Stage 09 until the Stage 08 exit gate is defensible.