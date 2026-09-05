# Provider Comparison

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 08 — Generate, Test & Select Options
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
Which solution survives evidence, alternatives and trade-offs?

## Why this artifact exists
To evaluate potential vendor providers for the single "Buy" component identified in the Build/Buy/Compose Assessment: the bounded NLP extraction service for unstructured port notices and policy documents.

## Upstream dependency
Use the completed Stage 08 Build/Buy/Compose Assessment and Stage 07 Acceptance Thresholds.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `Participant_Runbook.md` (Rule: "Never manufacture PoC/model/RAG results")

## Case challenge
**CRITICAL:** Do not fabricate vendor benchmark scores, pricing, or SLA numbers. Evaluate providers based on publicly known capabilities and architectural fit. If specific vendor testing was not conducted, state `NOT RUN` explicitly.

## Minimum content

| Evaluation Criteria | Provider A: Enterprise Cloud LLM API (e.g., Azure OpenAI, AWS Bedrock) | Provider B: Specialized Maritime NLP Vendor (e.g., Veson, DNV) | Provider C: Open-Source Self-Hosted (e.g., Llama, Mistral) | Evidence / Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Extraction Precision (Target: >90%)** | Likely high for general document parsing. Maritime-specific terminology may require fine-tuning. | Potentially highest for maritime domain. Pre-trained on port notices and maritime regulations. | Variable. Requires significant fine-tuning on maritime corpus. | `acceptance-thresholds.md`, `data-gap-register.md` (DG-03) |
| **Offline Capability** | **FAIL.** Requires continuous internet connectivity. Cannot run on vessel edge during blackout (GS-14). | **FAIL.** Typically cloud-hosted SaaS. | **PASS.** Can be deployed on vessel edge if hardware permits. | `ctqs.md` (Offline Continuity) |
| **Data Residency & Privacy** | Data leaves MeridianBlue's environment. Requires strict DPA and data processing agreements. | Data leaves environment. Maritime-specific compliance (e.g., IMO regulations) may be pre-certified. | **PASS.** All data stays on-premises or on-vessel. | `impact-regulatory-screen.md` |
| **Latency & Throughput** | Low latency (<2s per document). High throughput. | Variable. Depends on vendor SLA. | Variable. Depends on edge hardware. | `dependencies.md` |
| **Live PoC / Benchmark** | **NOT RUN** | **NOT RUN** | **NOT RUN** | `Participant_Runbook.md` (No manufactured results) |

## Selection Recommendation
**Provider A (Enterprise Cloud LLM API)** is the recommended starting point for the **shore-side** NLP extraction component, with the following strict conditions:
1. The NLP service runs **only on the shore-side** (not on the vessel edge), preserving offline continuity.
2. A strict Data Processing Agreement (DPA) must be in place before any port notice data is sent to the provider.
3. The mandatory human-in-the-loop fallback (Fleet Controller review) must be implemented for any extraction with confidence < 95%.

**Provider C (Open-Source)** should be evaluated as a Phase 2 enhancement for vessel-edge deployment if compute permits.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Live vendor PoC was not conducted; evaluation is based on architectural fit and known capabilities. | `Participant_Runbook.md` | `poc-model-rag-results.md` | High confidence (explicit training mandate). |
| NLP must be shore-side only to preserve offline continuity. | `ctqs.md` | `reference-architecture-comparison.md` | High confidence (non-negotiable constraint). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: Provider A's DPA will satisfy MeridianBlue's data residency requirements for port notice data. | Legal review of vendor DPAs is out of scope for this training. | Executive Sponsor / Legal | If DPA is insufficient, the project must pivot to Provider C (self-hosted), increasing implementation complexity. | Stage 10 Architecture ADRs. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved solution and trade-offs
Do not advance to Stage 09 until the Stage 08 exit gate is defensible.