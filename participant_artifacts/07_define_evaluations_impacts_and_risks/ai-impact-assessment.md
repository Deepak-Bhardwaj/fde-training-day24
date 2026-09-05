# AI Impact Assessment

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 07 — Define Evaluations, Impacts & Risks
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
What must the future system prove before it is acceptable?

## Why this artifact exists
To evaluate the specific operational, safety, and workforce impacts of introducing AI/ML components into the maritime workflow, given the strict boundary that AI is NON_AUTHORITATIVE.

## Upstream dependency
Use the completed Stage 04 AI Suitability Assessment, Stage 05 Business Rules, and Stage 07 Evaluation Strategy.

## Evidence to inspect
- `evidence/04_policy_authority/source_authority.yaml`
- `evidence/02_documents/fleet_operations_interview_notes.md`
- `evidence/04_policy_authority/role_authorization_matrix.csv`

## Case challenge
Since the core decision engine is deterministic, this assessment must focus strictly on the bounded AI use cases (e.g., NLP extraction for unstructured port notices) and the systemic impact of the workbench on human operators.

## Minimum content

| Impact Area | Description of Impact | Severity (H/M/L) | Mitigation / Design Constraint | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **Safety & Navigation** | If NLP extraction misinterprets a port notice, it could feed incorrect constraints to the deterministic engine. | **HIGH** | AI output is strictly NON_AUTHORITATIVE. Low-confidence extractions are flagged for manual Controller review. Deterministic engine requires explicit validation. | `source_authority.yaml`, `fleet_operations_interview_notes.md` |
| **Operator Workflow (Controllers)** | Shift from manual data gathering to reviewing system-generated, evidence-backed constraint views. | **MEDIUM** | UI must explicitly show the source, freshness, and authority weight of every constraint. Controllers retain the ability to manually override non-safety-critical data. | `fleet_operations_interview_notes.md` |
| **Operator Workflow (Master)** | Master receives structured, ranked recovery options instead of raw data dumps. | **LOW (Positive)** | Reduces cognitive load. Master retains absolute veto authority (BR-01). System never auto-executes. | `role_authorization_matrix.csv` |
| **Data Privacy (Crew)** | Risk of crew rest/availability data being exposed or used for automated personnel scheduling. | **HIGH** | AI and automated systems are explicitly prohibited from accessing or acting on SRC-CREW data for personnel decisions. Strict purpose-filtering applied. | `source_inventory.csv`, `permissible-use-access-matrix.md` |
| **Post-Event Learning** | Shift from unstructured, lost rationale to fully linked, reconstructable decision traces. | **LOW (Positive)** | System automatically generates audit logs linking rationale, source freshness, and outcomes, satisfying the Safety Officer's requirements. | `fleet_operations_interview_notes.md` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| AI impact on safety is bounded because AI cannot execute or override human authority. | `source_authority.yaml` (AI_OUTPUT precedence: NON_AUTHORITATIVE) | `prohibited-use-check.md` | High confidence (explicit policy). |
| NLP extraction carries a risk of misinterpretation that must be mitigated by human review. | `fleet_operations_interview_notes.md` (semantic conflicts) | `data-gap-register.md` (DG-03) | High confidence (SME interview). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: Fleet Controllers will trust the system's constraint view enough to reduce their manual verification time. | Trust in automated systems requires cultural shift and proven reliability. | FDE Team / Fleet Controller | If trust is low, controllers may revert to manual checks, negating the efficiency gains. | Stage 10 Target C4 Views (UI/UX design for trust/transparency). |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Evaluation, impact and risk requirements
Do not advance to Stage 08 until the Stage 07 exit gate is defensible.