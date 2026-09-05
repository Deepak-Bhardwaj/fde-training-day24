# Identity / Permission Matrix

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 11 — Agentic & Multi-Agent Orchestration
**Participant status:** COMPLETED
**Deliverable form:** Structured table / register

## Stage question
Is autonomy justified, bounded, permissioned, interruptible and testable?

## Why this artifact exists
To map every system identity (human and automated) to its exact permissions (Read, Write, Execute, Approve). This ensures the Principle of Least Privilege and guarantees that no automated identity can execute safety-critical actions.

## Upstream dependency
Use the completed Stage 06 Permissible-Use / Access Matrix and Stage 11 Tool / Action Catalogue.

## Evidence to inspect
- `evidence/04_policy_authority/role_authorization_matrix.csv`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
Clearly distinguish between "System Read/Write" (data management) and "System Execute" (physical world action). AI and automated systems must have ZERO "Execute" permissions.

## Minimum content

| Identity / Role | Read Canonical Graph | Write Canonical Graph | Execute Physical Actions | Approve Plans | Access HITL Queue | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Master** | YES (Vessel Edge) | NO | **YES** (Via vessel systems) | **YES** (Absolute) | NO | `role_authorization_matrix.csv` |
| **Chief Engineer** | YES | NO | YES (Technical only) | NO (Advisory) | NO | `role_authorization_matrix.csv` |
| **Fleet Controller** | YES | NO (Via HITL only) | NO | NO | **YES** (Review/Edit) | `role_authorization_matrix.csv` |
| **Safety Officer** | YES (Audit only) | NO | NO | NO | NO | `role_authorization_matrix.csv` |
| **Deterministic Orchestrator** | YES | NO | **NO** | **NO** | YES (Route to) | `tool-action-catalogue.md` |
| **Deterministic Engine** | YES (Active Subgraph) | NO | **NO** | **NO** | NO | `business-rules.md` |
| **Bounded NLP Service** | NO | NO (Direct) | **NO** | **NO** | NO | `model-routing-design.md` |
| **Ingestion ACL** | NO | YES (With Provenance) | **NO** | **NO** | NO | `target-information-trust-boundaries.md` |

### Key Permission Rules
1. **Zero Execute for AI/Automation:** No automated identity (Orchestrator, Engine, NLP Service) has `Execute Physical Actions` permission. Execution requires a human identity (Master).
2. **Zero Direct Write for AI:** The Bounded NLP Service cannot write directly to the Canonical Graph. It must pass through the Orchestrator -> HITL Queue -> Controller Approval -> Ingestion ACL.
3. **Approval is Exclusive:** Only the `Master` identity holds the `Approve Plans` permission. This cannot be delegated to any system or lower-level role.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Automated identities have zero permission to execute physical actions. | `role_authorization_matrix.csv` (AI_AGENT commit=NO) | `prohibited-use-check.md` | High confidence (explicit policy). |
| The NLP Service cannot write directly to the graph; it must use the HITL fallback. | `knowledge-extraction-specification.md` | `retrieval-adrs.md` (ADR-015) | High confidence (explicit design condition). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The API Gateway can reliably enforce these identity permissions at runtime without introducing excessive latency. | API Gateway performance under load NOT RUN. | Shore Platform Team | May require implementing permission checks at the application layer instead of the gateway. | Stage 10 API Contracts. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved, bounded and testable agentic architecture