# Risk Treatment Plan

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 07 — Define Evaluations, Impacts & Risks
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
What must the future system prove before it is acceptable?

## Why this artifact exists
To define the specific preventative, detective, and responsive controls required to mitigate the harms identified in the Risk/Harms Register to an acceptable level.

## Upstream dependency
Use the completed Stage 07 Risk/Harms Register and Stage 05 Business Rules.

## Evidence to inspect
- `Participant_Case_Study.md` (Golden Scenarios)
- `evidence/04_policy_authority/role_authorization_matrix.csv`

## Case challenge
Ensure every critical and high-severity risk has a concrete, testable treatment plan. "We will be careful" is not a treatment.

## Minimum content

| Risk ID | Treatment Strategy | Control Type | Implementation Detail | Owner | Residual Risk | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **RH-01** (Safety / Nav) | **Preventative & Responsive** | Hard Constraint & Human Veto | Deterministic engine blocks any plan violating CMMS holds. UI requires explicit Master digital sign-off. System logs all attempts. | Master / Chief Engineer | **Low** | `business-rules.md` (BR-01, BR-02) |
| **RH-02** (Operational / Fin) | **Detective & Preventative** | Temporal Provenance & ACL | System flags data exceeding freshness thresholds (e.g., >60m for Port). ACL enforces Signed Notice > API precedence. | Fleet Controller / Shore Platform | **Medium** | `source_authority.yaml`, `provenance-baseline.md` |
| **RH-03** (Adversarial) | **Preventative** | Input Sanitization & Non-Auth AI | NLP extraction layer sanitizes unstructured text. Deterministic engine ignores raw text commands. Low-confidence extractions routed to human. | FDE Team / Security | **Low** | `ai-impact-assessment.md`, `golden-set-specification.md` (GS-09) |
| **RH-04** (Resilience) | **Preventative** | Offline-First Edge Architecture | Vessel edge caches canonical constraints and deterministic rules. Operates autonomously during blackout. Syncs safely on reconnect. | Shore Platform / Vessel Tech | **Low** | `ddd-context-map.md`, `dependencies.md` |
| **RH-05** (Privacy) | **Preventative** | Strict RBAC & Purpose Filtering | API gateway enforces role-based access. AI agent tokens are strictly purpose-filtered and denied access to SRC-CREW. | Marine HR / IT Security | **Low** | `permissible-use-access-matrix.md` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Human veto (Master) is the ultimate preventative control for navigational safety. | `role_authorization_matrix.csv` | `governance-raci.md` | High confidence (explicit policy). |
| Offline-first architecture is the only viable treatment for prolonged blackout risks. | `fleet_operations_interview_notes.md` | `ctqs.md` | High confidence (SME interview). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The residual risk for RH-02 (Operational) is acceptable given the reliance on human review of flagged stale data. | Human fatigue or alert blindness could lead to ignored flags. | Fleet Controller | May require UI/UX design to make stale data flags impossible to ignore (e.g., blocking UI progression). | Stage 10 Target C4 Views (UI design). |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Evaluation, impact and risk requirements
Do not advance to Stage 08 until the Stage 07 exit gate is defensible.