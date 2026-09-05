# AI / RAG Integration Architecture

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 10 — AI & Application Architecture
**Participant status:** COMPLETED
**Deliverable form:** Diagram + supporting table + rationale

## Stage question
How will the AI-enabled application consume context, integrate, deploy and fail safely?

## Why this artifact exists
To explicitly define how AI (NLP Extraction) and RAG (Vector Retrieval) are integrated into the application, ensuring they are strictly bounded, shore-side only, and physically isolated from the deterministic safety engine.

## Upstream dependency
Use the completed Stage 09 Hybrid Retrieval Architecture, Stage 09 Retrieval ADRs, and Stage 10 Target C4 Component View.

## Evidence to inspect
- `evidence/04_policy_authority/source_authority.yaml`
- `Participant_Case_Study.md` (GS-09 Prompt Injection)

## Case challenge
Detail the exact boundaries of AI/RAG. How do we prevent prompt injection? How do we ensure RAG doesn't leak into the feasibility engine?

## Minimum content

### 1. AI Integration: NLP Extraction (Shore-Side Only)
- **Scope:** Parsing unstructured Port Notice PDFs and Fleet Policy documents into structured constraints.
- **Deployment:** Shore Platform only. **Strictly prohibited on Vessel Edge** to preserve offline continuity and compute.
- **Input Sanitization:** All PDF text is stripped of executable macros and sanitized before being sent to the external LLM API to prevent Prompt Injection (GS-09).
- **Output Handling:** The LLM returns structured JSON + `confidence_score`. The AI output is tagged `authority_weight = NON_AUTHORITATIVE` until it passes the 0.95 confidence threshold and/or HITL approval.

### 2. RAG Integration: Historical Precedents (Shore-Side Only)
- **Scope:** Retrieving semantically similar past `RecoveryOption` nodes to provide context to the Fleet Controller.
- **Deployment:** Shore Platform Vector DB.
- **Hard Isolation:** The Retrieval Router physically blocks the Deterministic Engine (both Shore and Edge) from querying the Vector DB. 
- **UI Integration:** The Fleet Controller UI displays RAG results in a distinct "Historical Context" panel, visually separated from the "Active Constraints" panel.

### 3. Failure Modes for AI/RAG
- **LLM API Outage:** NLP Extraction fails. Port Notices are routed directly to the HITL Review Queue for manual Controller entry. System continues operating.
- **Vector DB Outage:** RAG retrieval fails. Fleet Controller UI displays a "Historical Context Unavailable" warning. Deterministic engine and core operations are completely unaffected.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| AI/RAG components are strictly shore-side to protect vessel offline continuity. | `ctqs.md` (Offline Continuity) | `provider-comparison.md` | High confidence (non-negotiable constraint). |
| RAG results must be visually and programmatically isolated from active constraints. | `source_authority.yaml` | `retrieval-adrs.md` (ADR-014) | High confidence (explicit policy). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The input sanitization logic can effectively detect and strip novel prompt injection techniques from PDF text. | Adversarial testing of PDF sanitization NOT RUN. | FDE Team / Security | May require implementing a secondary, heuristic-based anomaly detector on the LLM output. | Stage 10 Failure-Mode Design. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Complete base AI/application architecture