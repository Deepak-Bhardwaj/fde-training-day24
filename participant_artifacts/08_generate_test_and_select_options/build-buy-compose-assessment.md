# Build / Buy / Compose Assessment

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 08 — Generate, Test & Select Options
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
Which solution survives evidence, alternatives and trade-offs?

## Why this artifact exists
To evaluate whether each major component of the selected Hybrid architecture (OPT-03) should be built in-house, purchased from a vendor, or composed from existing enterprise systems.

## Upstream dependency
Use the completed Stage 08 Weighted Trade-Off Matrix, Stage 05 Bounded Contexts, and Stage 06 Data Gap Register.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
Avoid the "Not Invented Here" bias. If an existing enterprise system (e.g., FMS, CMMS) already provides a capability, compose with it rather than rebuilding. If a commodity vendor solves a bounded problem (e.g., NLP extraction), buy rather than build.

## Minimum content

| Component | Build | Buy | Compose | Recommendation | Rationale | Evidence |
| :--- | :---: | :---: | :---: | :--- | :--- | :--- |
| **Deterministic Constraint Engine** | **YES** | No | No | **BUILD** | Core business logic (BR-01 through BR-06) is highly specific to MeridianBlue's authority model and policy rules. No off-the-shelf product enforces Master Veto or CMMS Absolute Holds out of the box. | `business-rules.md`, `non-ai-alternative.md` |
| **Ingestion ACL & Semantic Translation** | **YES** | No | Partial | **BUILD (with Compose)** | The Anti-Corruption Layer must translate 9 specific source formats into the canonical ubiquitous language. The translation rules are proprietary to this domain. However, compose with existing source APIs (SRC-AIS, SRC-PORT, etc.). | `ddd-context-map.md`, `source_inventory.csv` |
| **NLP Extraction (Port Notices / Policies)** | No | **YES** | No | **BUY (Bounded)** | Parsing unstructured PDFs is a commodity NLP task. Building a custom maritime NLP model is out of scope and high-risk. Buy a vendor API with strict SLA (>90% precision) and mandatory human fallback. | `ai-suitability-assessment.md`, `data-gap-register.md` (DG-03) |
| **Event Bus & Temporal Provenance** | **YES** | No | No | **BUILD** | The idempotency and clock-drift reconciliation logic (BR-05) is a core differentiator. Commodity event buses (e.g., Kafka) can be used as infrastructure, but the provenance envelope and deduplication logic must be custom-built. | `provenance-baseline.md`, `quality-profile.md` |
| **Vessel Edge Runtime** | **YES** | No | Partial | **BUILD (with Compose)** | The offline-first deterministic engine must run on constrained vessel hardware. Compose with existing vessel telemetry edge infrastructure (SRC-TELEM), but build the constraint cache and local UI. | `reference-architecture-comparison.md`, `dependencies.md` |
| **Compliance & Audit Store** | No | No | **YES** | **COMPOSE** | MeridianBlue likely already has an audit/logging infrastructure (ISM Code compliance). Compose with existing systems; add the decision-trace schema as a new event type. | `fleet_operations_interview_notes.md`, `bounded-contexts.md` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| The constraint engine must be custom-built due to the unique authority model. | `business-rules.md` (BR-01 through BR-06) | `non-ai-alternative.md` | High confidence (domain-specific logic). |
| NLP extraction is a commodity task best served by a vendor with SLA guarantees. | `data-gap-register.md` (DG-03) | `poc-model-rag-results.md` | High confidence (industry standard). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: MeridianBlue's existing audit infrastructure can ingest the new decision-trace event schema without major refactoring. | Existing audit system specs not detailed in evidence. | Shore Platform Team | If incompatible, the Audit Context may need to be built rather than composed, increasing scope. | Stage 10 AI & Application Architecture (Integration contracts). |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved solution and trade-offs
Do not advance to Stage 09 until the Stage 08 exit gate is defensible.