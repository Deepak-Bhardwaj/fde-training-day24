# AI Suitability Assessment

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 04 — Triage Regulation & Qualify Use Case
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
Should AI be used at all, and under what impact/regulatory constraints?

## Why this artifact exists
To objectively evaluate whether AI/ML is the right tool for this specific problem, or if a deterministic, rules-based system is more appropriate, safe, and efficient.

## Upstream dependency
Use the completed Stage 03 Root-Cause Analysis and Stage 04 Impact/Regulatory Screen.

## Evidence to inspect
- `evidence/02_documents/fleet_operations_interview_notes.md`
- `evidence/01_enterprise_sources/source_inventory.csv`

## Case challenge
Avoid the "hammer looking for a nail" anti-pattern. Justify AI use strictly based on the nature of the problem (e.g., semantic ambiguity, unstructured data) rather than hype.

## Minimum content

| Assessment Criteria | Evaluation | Verdict (Suitable / Not Suitable / Partially Suitable) | Evidence / Rationale |
| :--- | :--- | :--- | :--- |
| **Problem involves unstructured or ambiguous data?** | YES. Port API semantics conflict with signed PDF notices. Policy documents are unstructured. | **Partially Suitable** | AI (specifically NLP/LLM for extraction) is suitable for parsing unstructured notices, but deterministic rules must resolve the final authority. (`fleet_operations_interview_notes.md`) |
| **Problem requires pattern recognition at scale?** | NO. The core issue is reconciling known, structured constraints (CMMS, Cargo, Time), not discovering hidden patterns. | **Not Suitable** | A deterministic constraint-satisfaction engine is better suited for feasibility checking than an AI model. |
| **High cost of error (Safety/Critical)?** | YES. Incorrect recovery options can lead to safety incidents or commercial loss. | **Not Suitable for Autonomy** | AI must be strictly bounded to *decision-support* (drafting options), with human-in-the-loop validation. (`role_authorization_matrix.csv`) |
| **Data quality and provenance are sufficient?** | PARTIALLY. Telemetry has clock drift; policies have superseded versions. | **Partially Suitable** | AI retrieval is only suitable IF strict metadata filtering (active status, temporal provenance) is applied first. (`source_inventory.csv`) |

## Overall Suitability Conclusion
**AI is PARTIALLY SUITABLE, strictly as a Decision-Support and Information Retrieval augmentation.** 
AI should **NOT** be used for:
1. Autonomous decision-making or plan execution.
2. Core feasibility checking (this must be a deterministic rules engine).

AI **SHOULD** be considered for:
1. Extracting structured constraints from unstructured port notices or policy documents.
2. Semantic search and retrieval of relevant historical disruption precedents, provided strict authority and freshness filters are applied.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| AI is unsuitable for autonomous execution due to high safety stakes. | `role_authorization_matrix.csv` | `prohibited-use-check.md` | High confidence (explicit policy). |
| Deterministic rules are better for feasibility checking than AI. | `fleet_operations_interview_notes.md` (need for concise, evidence-backed comparison) | `root-cause-analysis.md` | High confidence (SME interview). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The team has access to a reliable, low-latency NLP extraction tool for port notices. | Specific vendor/tool capabilities not yet assessed. | FDE Team | May require a "Build vs Buy" assessment in Stage 08. | Stage 08 Build/Buy/Compose Assessment. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved and justified use case
Do not advance to Stage 05 until the Stage 04 exit gate is defensible.