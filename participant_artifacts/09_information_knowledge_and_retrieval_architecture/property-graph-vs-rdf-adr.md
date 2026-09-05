# Property Graph vs RDF ADR

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer D: Graph Data Platform)
**Participant status:** COMPLETED
**Deliverable form:** ADR / decision record

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To formally record the decision regarding the underlying graph database paradigm (Property Graph vs. RDF/OWL) for the Knowledge Graph, based on the specific performance and modeling requirements of the workbench.

## Upstream dependency
Use the completed Stage 09 Entity/Relationship Model and Knowledge Graph Schema.

## Evidence to inspect
- `evidence/02_documents/fleet_operations_interview_notes.md`
- `Participant_Runbook.md` (Rule: "Never manufacture PoC/model/RAG results")

## Case challenge
Evaluate the paradigms strictly against the need for edge properties (temporal validity, authority weight) and high-performance traversals for the deterministic engine.

## Minimum content

### ADR-005: Property Graph Paradigm over RDF for Knowledge Graph
- **Status:** Accepted
- **Context:** The Knowledge Graph must support complex, multi-hop traversals for the deterministic feasibility engine. Crucially, the relationships between entities (e.g., `[:CONSTRAINED_BY]`) must carry their own properties, specifically `valid_until` (temporal freshness) and `authority_weight` (conflict resolution). 
- **Options Considered:**
  1. **RDF (Resource Description Framework):** Excellent for strict ontologies, semantic web integration, and standardized SPARQL queries. However, RDF triples (Subject-Predicate-Object) do not natively support properties *on the edges*. Reifying edges to add properties significantly increases storage overhead and query complexity.
  2. **Property Graph (e.g., Neo4j, Amazon Neptune):** Natively supports nodes and relationships, where relationships can have their own properties and directions. Query languages (Cypher, Gremlin) are highly optimized for deep, multi-hop traversals.
- **Decision:** Adopt the **Property Graph** paradigm.
- **Consequences:** 
  - (+) Native support for edge properties (`valid_until`, `authority_weight`) perfectly matches our semantic constraints (SC-01, SC-02).
  - (+) Superior performance for the deep traversals required by the deterministic engine.
  - (+) Cypher/Gremlin are more intuitive for application developers than SPARQL.
  - (-) Less standardized schema enforcement compared to RDF/OWL (mitigated by strict application-level validation and data contracts).
  - (-) Live benchmarking of specific vendors is **NOT RUN**; selection is based on architectural fit.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Edge properties are a mandatory requirement for handling temporal and authority conflicts. | `semantic-constraints.md` (SC-01, SC-02) | `knowledge-graph-schema.md` | High confidence (architectural mandate). |
| Property Graphs natively support edge properties; RDF requires complex reification. | Industry standard graph database capabilities. | `entity-relationship-model.md` | High confidence (technical fact). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The lack of strict schema enforcement in Property Graphs will be mitigated by application-level validation. | Graph DB vendor schema plugins (e.g., Neo4j constraints) not fully evaluated. | Shore Platform Team | Requires rigorous unit testing of the ingestion ACL to prevent schema drift. | Stage 09 Data ADRs. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture