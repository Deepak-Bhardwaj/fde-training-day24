# Shared-Memory Design

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 11 — Agentic & Multi-Agent Orchestration
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
Is autonomy justified, bounded, permissioned, interruptible and testable?

## Why this artifact exists
In traditional multi-agent systems, "shared memory" refers to a volatile, LLM-managed context window. In this architecture, we replace volatile memory with a **deterministic, persistent Shared State** (the Canonical Graph DB and Vessel Edge Graph Store) to ensure 100% auditability, prevent hallucination, and support offline continuity.

## Upstream dependency
Use the completed Stage 09 Graph Persistence Architecture, Stage 11 Orchestration Topology, and Stage 11 Agent Responsibility Map.

## Evidence to inspect
- `evidence/02_documents/fleet_operations_interview_notes.md`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
Explicitly reject volatile LLM context windows as the system's "memory." All state must be grounded in the Property Graph with strict temporal provenance.

## Minimum content

### 1. The Shared State Architecture
Instead of a multi-agent shared memory, the system uses a dual-zone Shared State:
- **Shore Canonical Graph DB:** The single source of truth. Stores all active constraints, policies, and the full lineage of decisions.
- **Vessel Edge Graph Store:** A read-optimized, cached subset (the "Active Subgraph") synchronized via event-sourced delta sync.

### 2. Memory Access Patterns
| Actor / Component | Read Access | Write Access | Memory Consistency Model | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **Deterministic Orchestrator** | Full Shore Graph | No direct write (uses Ingestion ACL) | Strong consistency (ACID) | `target-information-trust-boundaries.md` |
| **Deterministic Engine** | Active Subgraph (Edge) or Full Graph (Shore) | No direct write | Eventual consistency (Edge), Strong (Shore) | `context-assembly-model.md` |
| **Fleet Controller (Human)** | Shore Graph + HITL Queue | Approve/Reject HITL items | Strong consistency | `role_authorization_matrix.csv` |
| **Master (Human)** | Vessel Edge Graph | Approve/Reject Plans | Eventual consistency (syncs on reconnect) | `graph-persistence-architecture.md` |

### 3. Why Not LLM Shared Memory?
- **Auditability:** L