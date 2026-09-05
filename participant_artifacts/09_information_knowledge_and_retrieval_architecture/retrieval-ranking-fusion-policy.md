# Retrieval Ranking / Fusion Policy

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer E: Hybrid Retrieval)
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To define how results from multiple retrieval sources (Graph, Vector, Keyword) are merged, ranked, and presented to the consumer (Deterministic Engine or Fleet Controller UI).

## Upstream dependency
Use the completed Stage 09 Retrieval Routing Policy and Enterprise Source Authority Model.

## Evidence to inspect
- `evidence/04_policy_authority/source_authority.yaml`
- `evidence/01_enterprise_sources/source_inventory.csv`

## Case challenge
When merging results, the fusion policy must strictly enforce the authority hierarchy and temporal freshness. A highly relevant vector suggestion can NEVER override a stale graph fact.

## Minimum content

### 1. Hierarchy of Truth (Fusion Priority)
When the same real-world concept is retrieved from multiple stores, the following priority dictates the final output:
1. **Property Graph (Active Constraints):** Highest priority. Represents verified, temporally valid, authoritative facts.
2. **Full-Text Index (Active Policies):** High priority. Represents current, approved governance rules.
3. **Vector Store (Historical Precedents):** Low priority. Represents probabilistic suggestions or historical context.
4. **Vector Store (Unstructured Drafts):** Lowest priority. Represents unverified NLP extractions.

### 2. Ranking Factors (Within the same tier)
If multiple results exist within the same tier (e.g., multiple active constraints from the Graph), they are ranked by:
1. **Authority Weight:** `HIGHEST` > `HIGH` > `MEDIUM` > `OBSERVATION`.
2. **Temporal Freshness:** Closer to `current_time` ranks higher.
3. **Source Specificity:** Signed Notice > API Observation.

### 3. Fusion Output Rules
- **For Deterministic Engine:** The fusion layer ONLY passes Property Graph facts. Vector results are stripped and discarded before reaching the engine.
- **For Fleet Controller UI:** The fusion layer passes Graph facts as "Primary Constraints" and Vector results as "Supporting Context", clearly separated in the UI payload.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Graph facts must always outrank vector suggestions in the fusion hierarchy. | `source_authority.yaml` | `hybrid-retrieval-architecture.md` | High confidence (explicit policy). |
| Temporal freshness is a primary ranking factor for operational constraints. | `source_inventory.csv` (freshness thresholds) | `provenance-baseline.md` | High confidence (architectural necessity). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The fusion algorithm can execute the priority hierarchy in < 10ms to meet the overall < 50ms engine SLA. | Fusion algorithm latency is NOT RUN. | Shore Platform Team | If too slow, the fusion logic may need to be simplified or pushed to the application layer. | Stage 10 AI / RAG Integration Architecture. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture