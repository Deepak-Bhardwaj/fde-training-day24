# Graph Indexing Strategy

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer D: Graph Data Platform)
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To define the exact indexing strategy required to support the operational traversal patterns (GQ-01 through GQ-05) and analytical requirements within the defined latency SLAs.

## Upstream dependency
Use the completed Stage 09 Graph Query/Traversal Patterns, Graph Logical Model, and Graph Persistence Architecture.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `Participant_Runbook.md` (Rule: "Never manufacture PoC/model/RAG results")

## Case challenge
Indexes must be optimized for the specific query patterns. Over-indexing will slow down write operations (ingestion), while under-indexing will cause the deterministic engine to timeout. Live benchmarking is NOT RUN; strategy is based on architectural patterns.

## Minimum content

### Shore Platform Indexes (Enterprise Graph DB)
| Index Type | Target | Properties Indexed | Purpose / Supported Query | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **Node Uniqueness** | `Vessel`, `Constraint`, `PolicyRule` | `canonical_id`, `constraint_id`, `rule_id`+`version` | Enforce SC-05 (Identity Canonical) and prevent duplicate nodes. | `graph-logical-model.md` |
| **Edge Composite** | `[:CONSTRAINED_BY]` | `valid_until`, `authority_weight` | Support GQ-01 (Core Feasibility Check) temporal and authority filtering. | `graph-query-traversal-patterns.md` |
| **Node Property** | `Constraint`, `PolicyRule` | `type`, `status` | Support GQ-02 (Technical Hold Block) and GQ-03 (Policy Governance). | `semantic-constraints.md` |
| **Full-Text Search** | `PolicyRule`, `EvidenceRecord` | `text`, `raw_payload_excerpt` | Enable keyword search for historical policy retrieval (Hybrid Retrieval). | `hybrid-retrieval-architecture.md` |

### Vessel Edge Indexes (Lightweight Embedded Store)
| Index Type | Target | Properties Indexed | Purpose / Constraint | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **Node Primary Key** | `Constraint`, `PolicyRule` | `constraint_id`, `rule_id` | Fast lookup for active subgraph updates. | `graph-persistence-architecture.md` |
| **Temporal Filter** | `[:CONSTRAINED_BY]` | `valid_until` | Rapid expiration of stale constraints on edge. | `semantic-constraints.md` (SC-02) |
| *Note:* No full-text or complex composite indexes on edge to preserve CPU/Memory for offline operations. | | | | `ctqs.md` (Offline Continuity) |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Edge composite indexes are mandatory for GQ-01 to meet the <50ms SLA. | `graph-query-traversal-patterns.md` | `acceptance-thresholds.md` | High confidence (architectural necessity). |
| Vessel edge must minimize indexing overhead to preserve offline compute. | `fleet_operations_interview_notes.md` | `graph-persistence-architecture.md` | High confidence (hardware constraint). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The full-text search index on `PolicyRule` does not bloat the shore database beyond acceptable limits. | Exact text volume of fleet policies not quantified. | Shore Platform Team | If bloat is severe, full-text search may need to be offloaded to a dedicated search engine (e.g., Elasticsearch). | Stage 09 Hybrid Retrieval Architecture. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture