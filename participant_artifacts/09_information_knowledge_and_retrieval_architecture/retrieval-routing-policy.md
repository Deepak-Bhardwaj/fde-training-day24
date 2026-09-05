# Retrieval Routing Policy

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer E: Hybrid Retrieval)
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To define the deterministic rules for routing incoming queries to the correct underlying store (Property Graph, Vector Store, or Full-Text Index). This ensures that safety-critical operational facts are never subjected to probabilistic vector search.

## Upstream dependency
Use the completed Stage 09 Hybrid Retrieval Architecture and Semantic Constraints.

## Evidence to inspect
- `evidence/04_policy_authority/source_authority.yaml`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
The routing policy must be strictly deterministic. If a query is identified as an "Operational Fact" (e.g., "Is this CMMS hold active?"), it MUST be routed exclusively to the Property Graph. Vector search is strictly prohibited for safety-critical feasibility checks.

## Minimum content

| Query Intent / Classification | Routing Target | Routing Logic / Trigger | Prohibited Actions | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **Operational Fact (Safety/Feasibility)** | **Property Graph ONLY** | Query contains canonical entity IDs (Vessel, Constraint, PolicyRule) and requests current state. | MUST NOT route to Vector Store. Probabilistic search is forbidden for feasibility. | `business-rules.md` (BR-02), `source_authority.yaml` |
| **Historical Precedent (Learning)** | **Vector Store + Graph Link** | Query asks "How did we handle..." or searches for similar past disruptions. | MUST NOT return vector results as active constraints. Must be clearly labeled "Historical Context". | `fleet_operations_interview_notes.md` |
| **Policy Keyword Search** | **Full-Text Index (Graph)** | Query contains keywords targeting policy text (e.g., "hazardous cargo rules"). | MUST filter results to `status = 'ACTIVE'` only. Superseded policies must be excluded unless explicitly requested for audit. | `source_authority.yaml` |
| **Unstructured Document Context** | **Vector Store** | Query targets the raw text of Port Notices or Policy Documents for semantic understanding. | MUST NOT execute any actions based on vector output. Output is strictly NON_AUTHORITATIVE. | `knowledge-extraction-specification.md` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Safety-critical feasibility checks must never use vector search. | `source_authority.yaml` (AI_OUTPUT precedence: NON_AUTHORITATIVE) | `ai-suitability-assessment.md` | High confidence (explicit policy). |
| Historical precedents must be visually and programmatically separated from active constraints. | `fleet_operations_interview_notes.md` | `oversight-transparency-requirements.md` | High confidence (SME interview). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The query classifier can accurately distinguish between "Operational Fact" and "Historical Precedent" with >99% accuracy. | Intent classifier accuracy is NOT RUN. | FDE Team | Misclassification could lead to vector search being used for feasibility, violating safety constraints. | Stage 10 Prompt / Context Design. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture