# Preliminary ADRs

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 08 — Generate, Test & Select Options
**Participant status:** COMPLETED
**Deliverable form:** ADR / decision record

## Stage question
Which solution survives evidence, alternatives and trade-offs?

## Why this artifact exists
To formally record the key architectural decisions made during solution selection, including the context, options considered, and rationale for each choice.

## Upstream dependency
Use all completed Stage 08 artifacts.

## Evidence to inspect
- `Participant_Case_Study.md` (Non-negotiable constraints)
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
Each ADR must be self-contained and defensible. Future engineers should be able to understand *why* a decision was made without re-reading the entire artifact spine.

## Minimum content

### ADR-001: Event-Driven Hybrid Architecture over Shore-Centric Monolith
- **Status:** Accepted
- **Context:** The workbench must support vessel-side decision-making during prolonged satellite blackouts (GS-14). A shore-centric architecture would leave the vessel without any decision support during connectivity loss.
- **Decision:** Adopt an Event-Driven Hybrid architecture (Pattern B) where the shore handles heavy ingestion and NLP, and the vessel edge runs a lightweight deterministic constraint engine with cached canonical data.
- **Consequences:** (+) Satisfies offline continuity (CTQ-04). (+) Enables safe reconciliation via temporal provenance (GS-15). (-) Increases implementation complexity. (-) Requires vessel-edge compute provisioning.
- **Evidence:** `reference-architecture-comparison.md`, `fleet_operations_interview_notes.md`

### ADR-002: Deterministic Core over AI-Driven Feasibility Checking
- **Status:** Accepted
- **Context:** The core feasibility logic (CMMS holds, policy compliance, cargo constraints) must be 100% explainable and auditable. AI/ML models introduce hallucination risk and opacity that is unacceptable for safety-critical constraints.
- **Decision:** The constraint engine will be purely deterministic and rule-based. AI/NLP is restricted to the ingestion layer for unstructured document parsing only.
- **Consequences:** (+) Zero hallucination risk for safety-critical logic. (+) 100% explainable to auditors. (-) Cannot handle unstructured inputs natively (requires NLP augmentation).
- **Evidence:** `non-ai-alternative.md`, `ai-suitability-assessment.md`

### ADR-003: Bounded NLP with Mandatory Human Fallback
- **Status:** Accepted (Conditional)
- **Context:** Port notices arrive as unstructured PDFs with conflicting semantics vs. the API. Manual reconciliation is the #1 bottleneck (45 mins). NLP extraction can automate this, but carries accuracy risk.
- **Decision:** Deploy a bounded NLP extraction service (shore-side only) with a mandatory human-in-the-loop fallback. Any extraction below 95% confidence is routed to the Fleet Controller for manual verification before entering the deterministic engine.
- **Consequences:** (+) Reduces reconciliation time significantly. (+) Maintains safety via human fallback. (-) Adds a dependency on vendor SLA. (-) Requires UI design for the fallback workflow.
- **Evidence:** `poc-model-rag-results.md`, `provider-comparison.md`

### ADR-004: Temporal Provenance Envelope on All Ingested Events
- **Status:** Accepted
- **Context:** Telemetry suffers from clock drift and duplicate delivery (SRC-TELEM). Port data has variable freshness. Without strict provenance, the system cannot guarantee idempotent processing or safe reconciliation.
- **Decision:** Every ingested event must carry a provenance envelope containing `source_id`, `observed_timestamp`, `ingestion_timestamp`, `source_version`, and `authority_weight`. Deduplication is enforced via a deterministic composite key hash.
- **Consequences:** (+) Guarantees idempotency (BR-05). (+) Enables safe offline reconciliation (GS-15). (-) Increases payload size (~15% overhead). (-) Requires all external adapters to extract and preserve source timestamps.
- **Evidence:** `provenance-baseline.md`, `quality-profile.md`

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| All 4 ADRs are directly traceable to non-negotiable constraints and evidence. | `Participant_Case_Study.md` | `weighted-tradeoff-matrix.md` | High confidence (explicit mapping). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: ADR-003's 95% confidence threshold is the correct balance between automation and safety. | Optimal threshold requires live vendor testing. | FDE Team | If too high, too many extractions fall back to manual review, reducing efficiency. If too low, unsafe data enters the engine. | Stage 09 Retrieval Ranking / Fusion Policy. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved solution and trade-offs
Do not advance to Stage 09 until the Stage 08 exit gate is defensible.