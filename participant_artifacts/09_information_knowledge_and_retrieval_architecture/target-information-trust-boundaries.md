# Target Information Trust Boundaries

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer A: Enterprise Source Layer)
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To define the security, validation, and trust boundaries in the *target* architecture, ensuring that untrusted external data is never allowed to pollute the canonical, safety-critical constraint engine.

## Upstream dependency
Use the completed Stage 02 Current-State Trust Boundaries and Stage 08 Selected Solution (ADR-001, ADR-004).

## Evidence to inspect
- `evidence/04_policy_authority/source_authority.yaml`
- `evidence/01_enterprise_sources/source_inventory.csv`

## Case challenge
Design boundaries that enforce the "Zero Trust" principle for external data, while maintaining the low-latency requirements of the deterministic engine.

## Minimum content

| Boundary Name | From (Lower Trust) | To (Higher Trust) | Trust Assumption | Enforcement Mechanism (Target State) | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **External Ingestion ACL** | External Providers (Port API, WX, AIS) | Shore Disruption Mgmt (Raw Zone) | Data is untrusted, potentially stale, or semantically conflicting. | Schema validation, temporal provenance tagging, and authority weighting applied immediately upon ingress. | `source_inventory.csv`, `provenance-baseline.md` |
| **Unstructured to Structured** | Raw Port Notice PDFs | Canonical Constraint Store | NLP extraction may contain hallucinations or errors. | NLP output is tagged `confidence_score`. If < 95%, routed to Fleet Controller for manual validation before entering Canonical Store. | `poc-model-rag-results.md`, `source_authority.yaml` |
| **Shore to Vessel Edge Sync** | Shore Canonical Store | Vessel Edge Cache | Shore data is authoritative, but connectivity is unreliable. | Data is signed and versioned. Vessel edge accepts sync only if version is newer and signature is valid. | `ddd-context-map.md`, `dependencies.md` |
| **Deterministic Engine Boundary** | Canonical Constraint Store | Recovery Option Generator | Data in Canonical Store is trusted, but must be actively validated against current rules. | Engine applies BR-01 through BR-06. Any violation immediately marks option as INFEASIBLE. | `business-rules.md` |
| **Execution Command Boundary** | Shore/Vessel UI | Vessel Execution Systems | No automated system is trusted to execute navigational commands. | Hard requirement for Master's cryptographic or procedural sign-off before any command is transmitted to vessel systems. | `role_authorization_matrix.csv` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| External data must pass through an ACL before reaching the canonical store. | `fleet_operations_interview_notes.md` | `ddd-context-map.md` | High confidence (SME interview). |
| NLP extraction requires a confidence-based human fallback to maintain trust. | `poc-model-rag-results.md` | `selected-solution.md` | High confidence (explicit design condition). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The cryptographic signing of shore-to-vessel sync payloads does not introduce prohibitive latency on the vessel edge. | Edge CPU constraints for crypto operations not fully profiled. | Shore Platform Team | May require lightweight signing algorithms or pre-computed hashes. | Stage 10 Deployment Topology. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture
Do not advance to the next sub-layer until this artifact is defensible.