# Bounded Contexts

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 05 — Model the Domain
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
What does the business actually mean, decide and own?

## Why this artifact exists
To provide a detailed narrative of each bounded context identified in the Context Map, defining its purpose, core entities, and the specific split between deterministic logic and non-authoritative AI assistance.

## Upstream dependency
Use the completed Stage 05 DDD Context Map, Business Rules, and Domain Capability Map.

## Evidence to inspect
- `evidence/04_policy_authority/role_authorization_matrix.csv`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
Clearly articulate what happens *inside* each context and how it enforces the non-negotiable constraints of the case study.

## Minimum content

### 1. Vessel Command & Edge Context
- **Purpose:** Manage real-time vessel state, execute approved plans, and maintain critical decision-support capabilities during connectivity loss (GS-14).
- **Core Entities:** Vessel State, Local Telemetry, Cached Canonical Constraints, Execution Logs.
- **Logic Split:** 100% Deterministic / Rule-Based. No LLM/AI execution permitted on the edge to ensure offline reliability and strict adherence to Master Authority.
- **Key Rule Enforced:** BR-01 (Master Veto), BR-02 (Technical Hold Absolute).
- **Evidence:** `fleet_operations_interview_notes.md`, `ctqs.md`

### 2. Shore Disruption Management Context
- **Purpose:** The core hub for Fleet Controllers to reconcile evidence, generate recovery options, and coordinate with the Master.
- **Core Entities:** Disruption, Recovery Option, Constraint View, Master Approval Record.
- **Logic Split:** Core feasibility checking is Deterministic. AI/NLP may be used strictly in the ingestion layer to parse unstructured port notices into structured constraints (marked NON_AUTHORITATIVE).
- **Key Rule Enforced:** BR-03 (AI Non-Authoritative), BR-04 (Active Policy Exclusivity).
- **Evidence:** `non-ai-alternative.md`, `use-case-card.md`

### 3. External Intelligence Context (Ingestion & ACL)
- **Purpose:** Interface with 3rd party providers (Port, WX, AIS) and translate their native formats/semantics into the canonical ubiquitous language.
- **Core Entities:** External Feed, Anti-Corruption Translation Rules, Source Health Status.
- **Logic Split:** Deterministic mapping and schema validation. 
- **Key Rule Enforced:** BR-05 (Temporal Idempotency), BR-06 (Canonical Identity Supremacy).
- **Evidence:** `source_inventory.csv`, `source_authority.yaml`

### 4. Compliance & Audit Context
- **Purpose:** Provide an immutable, reconstructable trail of all domain events, rationale, source freshness, and outcomes for post-event learning and safety audits.
- **Core Entities:** Decision Trace, Audit Log, Superseded Policy Archive.
- **Logic Split:** 100% Deterministic / Append-Only Storage.
- **Key Rule Enforced:** Strict separation of ACTIVE vs. SUPERSEDED policies to prevent retrieval traps (GS-12).
- **Evidence:** `fleet_operations_interview_notes.md`, `source_authority.yaml`

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| The Vessel Edge Context must be 100% deterministic to guarantee offline safety. | `ctqs.md` (Offline Continuity) | `prohibited-use-check.md` | High confidence (explicit constraint). |
| The Audit Context must isolate superseded policies to prevent retrieval traps. | `source_authority.yaml` | `dependencies.md` | High confidence (explicit policy). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The Shore Disruption Context can host the NLP extraction tool without violating data residency or latency requirements. | Cloud/On-prem hosting constraints for NLP tools not fully detailed. | Shore Platform Team | May require the NLP tool to be deployed as a sidecar or edge service. | Stage 10 Deployment Topology. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Domain and decision model
Do not advance to Stage 06 until the Stage 05 exit gate is defensible.