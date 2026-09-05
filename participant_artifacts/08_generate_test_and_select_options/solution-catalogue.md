# Solution Catalogue

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 08 — Generate, Test & Select Options
**Participant status:** COMPLETED
**Deliverable form:** Structured table / register

## Stage question
Which solution survives evidence, alternatives and trade-offs?

## Why this artifact exists
To catalog the viable architectural and technological patterns that could solve the defined problem, before narrowing down to a specific selected solution.

## Upstream dependency
Use the completed Stage 05 Bounded Contexts, Stage 07 Evaluation Strategy, and Stage 07 Risk Treatment Plan.

## Evidence to inspect
- `Participant_Case_Study.md` (Non-negotiable constraints)
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
Include a diverse range of options, including "do nothing" or "purely manual" baselines, to prove that the selected solution is genuinely the best fit for the evidence.

## Minimum content

| Option ID | Solution Pattern | Description | Pros | Cons | Viability | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **OPT-01** | **Status Quo (Manual)** | Continue current process: Controllers manually reconcile 9 sources via email/spreadsheets; Master approves via sat-com text. | Zero development cost. No new system risks. | 45-min reconciliation time. High error rate. Fails GS-14 (no offline decision support). | **Rejected** | `baseline-dataset.csv`, `fleet_operations_interview_notes.md` |
| **OPT-02** | **Pure Deterministic Engine** | Rule-based constraint engine ingests structured APIs. Generates recovery options. No AI/ML components. | 100% explainable. Zero hallucination risk. Low compute footprint (ideal for vessel edge). | Cannot parse unstructured Port Notice PDFs or legacy policy documents. Requires manual data entry for unstructured inputs. | **Viable (Baseline)** | `non-ai-alternative.md`, `ai-suitability-assessment.md` |
| **OPT-03** | **Hybrid: Deterministic Core + Bounded NLP** | Deterministic engine handles all feasibility logic. A bounded, isolated NLP component extracts structured constraints from unstructured Port/Policy documents, flagged as "Draft" for human review. | Automates the #1 bottleneck (semantic reconciliation). Maintains 100% deterministic safety for execution. | Requires NLP extraction accuracy >90%. Adds slight complexity to the ingestion ACL. | **Viable (Preferred)** | `fleet_operations_interview_notes.md`, `data-gap-register.md` (DG-03) |
| **OPT-04** | **Fully Autonomous Agentic System** | LLM-based agents monitor streams, negotiate with ports, and auto-execute recovery plans. | Theoretically fastest reaction time. | Violates BR-01 (Master Veto) and BR-03 (AI Non-Auth). High hallucination risk. Fails offline. | **Rejected (Prohibited)** | `role_authorization_matrix.csv`, `prohibited-use-check.md` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Fully autonomous systems are explicitly prohibited by non-negotiable constraints. | `Participant_Case_Study.md` (AI cannot issue navigational commands) | `go-no-go-kill-criteria.md` | High confidence (explicit mandate). |
| Hybrid approach addresses the specific bottleneck of unstructured port notices without compromising safety. | `fleet_operations_interview_notes.md` | `ai-suitability-assessment.md` | High confidence (SME interview). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: A bounded NLP component can achieve the >90% precision required for safe port notice extraction. | Live vendor API testing is out of scope for this synthetic phase. | FDE Team | Selection of OPT-03 is conditional on Stage 09/10 vendor SLA guarantees or fallback to OPT-02 (manual entry). | Stage 08 Build/Buy/Compose Assessment. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved solution and trade-offs
Do not advance to Stage 09 until the Stage 08 exit gate is defensible.