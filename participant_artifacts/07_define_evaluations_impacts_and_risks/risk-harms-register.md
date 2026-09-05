# Risk / Harms Register

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 07 — Define Evaluations, Impacts & Risks
**Participant status:** COMPLETED
**Deliverable form:** Structured table / register

## Stage question
What must the future system prove before it is acceptable?

## Why this artifact exists
To systematically catalog all potential harms (safety, financial, environmental, privacy, reputational) that could result from system failure, misuse, or edge-case scenarios.

## Upstream dependency
Use the completed Stage 07 Acceptance Thresholds, Golden-Set Specification, and Stage 04 Impact/Regulatory Screen.

## Evidence to inspect
- `Participant_Case_Study.md` (Golden Scenarios)
- `evidence/04_policy_authority/role_authorization_matrix.csv`
- `evidence/01_enterprise_sources/source_inventory.csv`

## Case challenge
Focus on severe, high-impact harms. Do not dilute the register with minor inconveniences. Every harm must map to a specific failure mode or Golden Scenario.

## Minimum content

| Risk ID | Harm Category | Description of Potential Harm | Trigger / Failure Mode | Severity | Likelihood | Golden Scenario Link | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **RH-01** | **Safety / Navigational** | Vessel executes an unsafe maneuver or violates a critical maintenance hold, leading to casualty or environmental damage. | System bypasses Master authority (GS-08) or ignores active CMMS hold (GS-03). | **Critical** | Low (if controls hold) | GS-03, GS-08 | `role_authorization_matrix.csv`, `business-rules.md` |
| **RH-02** | **Operational / Financial** | Vessel routes to a port that is actually closed, or attempts a maneuver violating cargo constraints, resulting in massive demurrage or cargo damage. | System relies on stale port data (GS-05) or misinterprets semantic conflicts (GS-11). | **High** | Medium | GS-05, GS-11 | `source_inventory.csv`, `fleet_operations_interview_notes.md` |
| **RH-03** | **Adversarial / Security** | Malicious actor injects instructions via external port messages, causing the system to generate unsafe or unauthorized recovery options. | Prompt injection in unstructured text parsed by NLP (GS-09). | **High** | Low | GS-09 | `Participant_Case_Study.md`, `source_authority.yaml` |
| **RH-04** | **Resilience / Safety** | Vessel loses connectivity and is unable to make safe, informed decisions during a disruption, leading to operational paralysis. | Prolonged sat-com blackout prevents shore-side support, and vessel edge lacks cached constraints (GS-14). | **Critical** | Medium | GS-14 | `fleet_operations_interview_notes.md`, `dependencies.md` |
| **RH-05** | **Privacy / Compliance** | Crew personal data or commercial cargo data is exposed to unauthorized systems or used for automated personnel decisions. | RBAC failure or AI overreach accessing SRC-CREW/SRC-CARGO. | **High** | Low | N/A | `source_inventory.csv`, `permissible-use-access-matrix.md` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Safety and navigational harms are the highest severity risks in this domain. | `role_authorization_matrix.csv` (Master's absolute authority) | `impact-regulatory-screen.md` | High confidence (maritime domain reality). |
| Adversarial injection via external messages is a recognized threat vector. | `Participant_Case_Study.md` (GS-09) | `ai-impact-assessment.md` | High confidence (explicit training scenario). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The likelihood of RH-01 (Safety) is Low *only if* the deterministic constraints are perfectly implemented. | Implementation perfection is theoretical until Stage 08/09 testing. | FDE Team | Requires rigorous unit and integration testing of the constraint engine. | Stage 08 PoC / Model / RAG Results. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Evaluation, impact and risk requirements
Do not advance to Stage 08 until the Stage 07 exit gate is defensible.