# Tool / Action Catalogue

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 11 — Agentic & Multi-Agent Orchestration
**Participant status:** COMPLETED
**Deliverable form:** Structured table / register

## Stage question
Is autonomy justified, bounded, permissioned, interruptible and testable?

## Why this artifact exists
To explicitly list every tool, API, or action that the Deterministic Orchestrator (and the Bounded NLP Service) is permitted to invoke. This prevents "tool hallucination" or unauthorized API calls.

## Upstream dependency
Use the completed Stage 10 API Contracts and Stage 11 Orchestration Topology.

## Evidence to inspect
- `evidence/04_policy_authority/role_authorization_matrix.csv`
- `Participant_Case_Study.md` (GS-08: Unauthorized shore commit attempt)

## Case challenge
In an agentic system, an LLM might "hallucinate" a tool call. In our deterministic orchestrator, the tool catalogue is hardcoded. The orchestrator cannot invoke any tool not explicitly listed here.

## Minimum content

| Tool / Action Name | Invoked By | Target System / API | Purpose | Permission / Guard | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Fetch Active Context** | Orchestrator | Context Assembler (`/v1/context/assemble`) | Retrieve the isolated subgraph for a specific voyage. | Read-only. Requires valid `vessel_id` and `voyage_id`. | `api-contracts.md` |
| **Run Feasibility Check** | Orchestrator | Deterministic Engine (Local) | Evaluate a `RecoveryOption` against active constraints. | Read-only graph traversal. Cannot modify state. | `business-rules.md` |
| **Extract Port Notice** | Orchestrator | Bounded NLP Service (External LLM) | Parse unstructured PDF into structured JSON. | Strict timeout (30s). Input sanitized. Output validated against JSON schema. | `prompt-context-design.md` |
| **Route to HITL** | Orchestrator | HITL Review Queue (`/v1/hitl/review`) | Queue low-confidence NLP extractions for human review. | Write-only to queue. Cannot bypass queue to write to Graph. | `knowledge-extraction-specification.md` |
| **Publish Options to UI** | Orchestrator | Fleet Controller UI (Event Bus) | Display feasible options to the human operator. | Event publish only. Cannot execute actions. | `api-contracts.md` |
| **Sync Graph Delta** | Shore Orchestrator | Vessel Edge (MQTT) | Send updated constraints to the vessel edge cache. | QoS 1/2. Compressed payload. | `api-contracts.md` |

### Explicitly Prohibited "Tools" (Anti-Catalogue)
| Prohibited Action | Reason for Prohibition | Enforcement Mechanism | Evidence |
| :--- | :--- | :--- | :--- |
| **Execute Navigational Command** | Violates Master's absolute authority (GS-08). | Network-level firewall blocks Orchestrator from vessel navigation systems. | `role_authorization_matrix.csv` |
| **Override CMMS Hold** | Violates Technical Hold Absolute rule (BR-02). | Deterministic Engine hardcodes this check; no API exists to override it. | `business-rules.md` |
| **Direct Write to Canonical Graph** | Bypasses the Ingestion ACL and Provenance Enforcer. | Orchestrator only has access to the HITL Queue and Context Assembler, not the Graph DB directly. | `target-information-trust-boundaries.md` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| The orchestrator's tool catalogue is strictly hardcoded and cannot be dynamically expanded. | `Participant_Case_Study.md` | `orchestration-topology.md` | High confidence (architectural mandate). |
| Executing navigational commands is explicitly prohibited. | `role_authorization_matrix.csv` | `prohibited-use-check.md` | High confidence (explicit policy). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The firewall rules effectively block the Orchestrator from accessing vessel navigation systems. | Network security audit NOT RUN. | IT Security | Requires strict network segmentation between the Shore Platform and vessel operational networks. | Stage 10 Deployment Topology. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved, bounded and testable agentic architecture