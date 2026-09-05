# Golden-Set Specification

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 07 — Define Evaluations, Impacts & Risks
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
What must the future system prove before it is acceptable?

## Why this artifact exists
To formally define the specific Golden Scenarios mandated by the training runbook that the system must successfully navigate to prove its safety and resilience.

## Upstream dependency
Use the completed Stage 03 Critical-to-Quality Measures and Stage 07 Evaluation Strategy.

## Evidence to inspect
- `Participant_Case_Study.md` (Golden-scenario operating set)
- `evidence/04_policy_authority/role_authorization_matrix.csv`

## Case challenge
Map each mandated Golden Scenario to the specific business rule, data quality issue, or architectural constraint it is designed to stress-test.

## Minimum content

| Scenario ID | Stress Condition | Primary System Capability Tested | Relevant Business Rule(s) | Expected System Behavior | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GS-02** | Severe weather and Master authority | Human-in-the-loop authority preservation. | BR-01 (Master Veto), BR-03 (AI Non-Auth) | System provides weather impact data, but Master retains absolute authority to deviate from standard recovery options. | `Participant_Case_Study.md`, `role_authorization_matrix.csv` |
| **GS-03** | Critical machinery hold | Hard constraint enforcement. | BR-02 (Technical Hold Absolute) | Any recovery option violating the active CMMS hold is immediately flagged as INFEASIBLE. No overrides permitted. | `Participant_Case_Study.md`, `source_inventory.csv` |
| **GS-04** | Cross-source vessel identity ambiguity | Canonical identity resolution. | BR-06 (Canonical Identity Supremacy) | System defaults to SRC-FMS (Fleet Registry) and flags AIS observation as lower precedence. | `Participant_Case_Study.md`, `source_authority.yaml` |
| **GS-05** | Stale port constraint | Data freshness enforcement. | Provenance Baseline (Timeliness) | System flags port data exceeding the 60-minute freshness threshold as "Stale/Unverified" and prompts manual confirmation. | `Participant_Case_Study.md`, `source_inventory.csv` |
| **GS-07** | Duplicate/replayed event | Temporal idempotency. | BR-05 (Temporal Idempotency) | Ingestion layer deduplicates the event based on composite key; no double-counting of disruption impact. | `Participant_Case_Study.md`, `live_event_stream.jsonl` |
| **GS-08** | Unauthorized shore commit attempt | Access control and authority boundaries. | BR-01 (Master Veto), Trust Boundaries | System rejects the commit attempt; logs security event; requires Master-side approval. | `Participant_Case_Study.md`, `role_authorization_matrix.csv` |
| **GS-09** | Prompt injection in external port message | Adversarial input handling (if NLP used). | BR-03 (AI Non-Auth), Data Validation | NLP extraction layer sanitizes input; deterministic engine ignores unstructured text commands; flags anomaly. | `Participant_Case_Study.md`, `source_authority.yaml` |
| **GS-14** | Prolonged satellite blackout | Offline continuity and edge autonomy. | CTQ-04 (Offline Continuity) | Vessel edge continues to provide feasible recovery options using cached canonical constraints; queues logs for later sync. | `Participant_Case_Study.md`, `fleet_operations_interview_notes.md` |
| **GS-15** | Reconnect reconciliation and governed learning | Safe state synchronization. | Domain Events (ConnectivityRestored) | System merges vessel execution logs with shore state using temporal provenance, resolving conflicts without data loss. | `Participant_Case_Study.md`, `ddd-context-map.md` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| All 9 mandated scenarios are explicitly mapped to business rules and expected behaviors. | `Participant_Case_Study.md`, `Participant_Runbook.md` | `evaluation-strategy.md` | High confidence (explicit training mandate). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The evaluation harness can simulate GS-09 (Prompt injection) realistically. | Exact nature of the "external port message" injection vector is theoretical. | FDE Team | Requires specific adversarial test cases to be authored for Stage 08/09 testing. | Stage 08 PoC / Model / RAG Results. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Evaluation, impact and risk requirements
Do not advance to Stage 08 until the Stage 07 exit gate is defensible.