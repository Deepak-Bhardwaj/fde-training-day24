# Logical Information Architecture

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer H: Target Information Architecture)
**Participant status:** COMPLETED
**Deliverable form:** Diagram + supporting table + rationale

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To map the logical flow of data from the moment it leaves the 9 enterprise sources to the moment it is consumed by the Deterministic Engine or the Fleet Controller UI. This ensures that trust boundaries, provenance tagging, and authority weighting are enforced at every logical step.

## Upstream dependency
Use the completed Stage 09 Target Data Architecture, Retrieval Routing Policy, and Context Assembly Model.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
The logical flow must explicitly separate the "Raw Zone" (untrusted, unstructured) from the "Canonical Zone" (trusted, structured, provenance-tagged). No raw data ever reaches the Deterministic Engine.

## Diagram Description (Logical Data Flow)
*(Text-based representation)*
1. **Sources:** 9 Enterprise Systems (AIS, Telem, Port, WX, FMS, CMMS, Cargo, Crew, Policy).
2. **Ingestion ACL (The Trust Boundary):** Validates schema, attaches Provenance Envelope, resolves identity, applies authority weights.
3. **Raw Zone:** Blob Storage (PDFs, raw payloads).
4. **Canonical Zone:** Property Graph (Structured facts) + Vector Store (Semantic context).
5. **Context Assembler:** Isolates the "Active Subgraph" for a specific Vessel/Voyage.
6. **Consumers:** 
   - Deterministic Engine (Receives ONLY Graph facts).
   - Fleet Controller UI (Receives Graph facts + Vector context).

## Working scaffold (Zone Definitions & Rules)

| Logical Zone | Components | Entry Rules | Exit Rules | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **1. Source Zone** | External APIs, Edge Streams | N/A (External) | Must pass through Ingestion ACL. | `source_inventory.csv` |
| **2. Ingestion ACL** | Schema Validators, NLP Extractors, Identity Resolvers | Rejects payloads missing Provenance Envelope. | Writes to Raw Zone and Canonical Zone. Tags `authority_weight`. | `target-information-trust-boundaries.md` |
| **3. Raw Zone** | Blob Storage | Receives `raw_payload` and `document_uri`. | Read-only access for Audit and HITL review. | `provenance-evidence-linkage-model.md` |
| **4. Canonical Zone** | Property Graph, Vector Store | Receives structured nodes/edges with `[:DERIVED_FROM]` lineage. | Graph facts routed to Engine. Vector context routed to UI. | `hybrid-retrieval-architecture.md` |
| **5. Context Assembly** | Active Subgraph Generator | Filters by `valid_until`, `authority_weight`, `status=ACTIVE`. | Outputs strictly formatted JSON to Consumers. | `context-assembly-model.md` |
| **6. Consumer Zone** | Deterministic Engine, Fleet UI | Engine: Graph facts only. UI: Facts + Context. | Engine outputs `RecoveryOption`. UI displays to human. | `retrieval-routing-policy.md` |

## Rationale
This logical architecture enforces the "Zero Trust" principle for external data. By mandating that all data passes through the Ingestion ACL and receives a Provenance Envelope before entering the Canonical Zone, we guarantee that the Deterministic Engine only ever evaluates data that has been explicitly validated for freshness and authority. The strict separation of Graph facts and Vector context at the Consumer Zone prevents AI hallucinations from polluting safety-critical feasibility checks.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Raw data must never bypass the Ingestion ACL to reach the Canonical Zone. | `fleet_operations_interview_notes.md` (semantic conflicts) | `ddd-context-map.md` | High confidence (architectural mandate). |
| The Deterministic Engine must be isolated from Vector search results to prevent probabilistic safety failures. | `source_authority.yaml` (AI_OUTPUT precedence) | `ai-suitability-assessment.md` | High confidence (explicit policy). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The Ingestion ACL can process the combined throughput of all 9 sources without creating a bottleneck that violates freshness SLAs. | Ingestion throughput benchmarking is NOT RUN. | Shore Platform Team | If bottlenecked, the ACL may need to be horizontally scaled or prioritized (e.g., CMMS > WX). | Stage 10 Deployment Topology. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture