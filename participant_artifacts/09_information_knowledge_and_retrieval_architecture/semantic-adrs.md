# Semantic ADRs

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer I: Architecture Decisions / Schemas)
**Participant status:** COMPLETED
**Deliverable form:** ADR / decision record

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To formally record the architectural decisions regarding the semantic layer, data quality enforcement, and the strict isolation of AI/NLP outputs from deterministic safety logic.

## Upstream dependency
Use the completed Stage 09 Semantic Model, Retrieval Routing Policy, and Target Information Trust Boundaries.

## Evidence to inspect
- `evidence/04_policy_authority/source_authority.yaml`
- `evidence/01_enterprise_sources/source_inventory.csv`

## Case challenge
These ADRs must prove that the system is designed to prevent "garbage in, garbage out" and ensure that probabilistic AI models can never corrupt deterministic safety constraints.

## Minimum content

### ADR-008: Mandatory Provenance Envelope at Ingestion (Zero Trust)
- **Status:** Accepted
- **Context:** The 9 enterprise sources have varying levels of trust, freshness, and semantic consistency. Allowing raw data to enter the Canonical Zone without explicit metadata would make temporal conflict resolution (GS-05) and authority weighting impossible.
- **Decision:** The Ingestion ACL acts as a strict Zero Trust boundary. No data payload is written to the Canonical Zone unless it is wrapped in the mandatory Provenance Envelope (containing `source_id`, `observed_ts`, `authority_weight`, `freshness_state`).
- **Consequences:** (+) Guarantees that every node in the graph is auditable and temporally valid. (+) Enables automated expiration of stale constraints. (-) Increases ingestion latency and requires strict schema enforcement from all source adapters.
- **Evidence:** `authority-freshness-metadata-profile.md`, `target-information-trust-boundaries.md`

### ADR-009: Strict Isolation of Graph Facts and Vector Context
- **Status:** Accepted
- **Context:** The Hybrid Retrieval Architecture uses both the Property Graph (for facts) and the Vector Store (for semantic context/historical precedents). Mixing these in the deterministic engine's feasibility check would introduce hallucination risks and violate the Master's authority (BR-01).
- **Decision:** The Retrieval Router strictly isolates the two paths. The Deterministic Engine is physically and programmatically blocked from querying the Vector Store. The Fleet Controller UI receives both, but they are rendered in distinct, visually separated UI components.
- **Consequences:** (+) Eliminates the risk of AI hallucinations blocking a safe voyage or approving an unsafe one. (+) Preserves 100% explainability for the deterministic engine. (-) Controllers must mentally bridge the gap between the hard facts and the semantic suggestions.
- **Evidence:** `retrieval-routing-policy.md`, `ai-suitability-assessment.md`

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Zero Trust ingestion is required to handle conflicting source semantics. | `fleet_operations_interview_notes.md` | `ddd-context-map.md` | High confidence (SME interview). |
| Vector search must never influence the deterministic feasibility engine. | `source_authority.yaml` | `go-no-go-kill-criteria.md` | High confidence (explicit policy). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The UI design successfully prevents "alert fatigue" when displaying both hard facts and semantic suggestions. | UI/UX testing with Fleet Controllers NOT RUN. | FDE Team | Poor UX may lead controllers to ignore the semantic context entirely. | Stage 10 Target C4 Views. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture