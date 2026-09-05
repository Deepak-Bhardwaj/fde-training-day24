# Data-Gap Register

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 06 — Qualify Data & Knowledge
**Participant status:** COMPLETED
**Deliverable form:** Structured table / register

## Stage question
Is the evidence trustworthy, permissible, traceable, representative and ready?

## Why this artifact exists
To formally log all known data gaps, missing metadata, or quality issues that could block the architecture design or evaluation phases, and to assign ownership for resolving them.

## Upstream dependency
Use the completed Stage 06 Quality Profile, Provenance Baseline, and Representativeness Assessment.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
Be brutally honest. A "NOT RUN" or "DATA MISSING" status is valid evidence. Do not hide gaps.

## Minimum content

| Gap ID | Data / Metadata Missing | Impact on System / Architecture | Severity (H/M/L) | Owner | Mitigation / Workaround | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **DG-01** | Exact sat-com bandwidth limits and latency profiles during degradation. | Cannot precisely size the vessel-edge cache or optimize payload compression for GS-14. | **HIGH** | Shore Platform Team | Design for worst-case (minimal text-only sync); implement adaptive payload shedding. | `dependencies.md` |
| **DG-02** | CMMS Asset ID mapping table (Vessel-local ID to Canonical Shore ID). | Deterministic engine cannot reliably enforce BR-02 (Technical Hold Absolute) if IDs don't match. | **HIGH** | Technical Operations | Fallback: Require manual Controller override if ID mapping fails; flag as "Unverified Hold". | `quality-profile.md` |
| **DG-03** | NLP extraction accuracy baseline for unstructured Port Notices (PDFs). | ACL cannot guarantee 100% accurate translation of port constraints into the canonical model. | **MEDIUM** | FDE Team | Fallback: Route low-confidence extractions to Fleet Controller for manual verification before use. | `lineage.md` |
| **DG-04** | Historical data for prolonged satellite blackouts (> 4 hours). | Evaluation harness lacks real-world baseline for testing GS-14 state divergence. | **MEDIUM** | FDE Team | Generate synthetic blackout scenarios based on theoretical drift models for Stage 07 testing. | `representativeness-assessment.md` |
| **DG-05** | Explicit list of "Essential Vessel Operations" for offline caching. | Vessel edge might cache too much (storage limits) or too little (safety risk). | **MEDIUM** | Master / Safety Officer | Conduct workshop with Master to define the minimum viable offline constraint set. | `prohibited-use-check.md` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| CMMS ID mapping is a critical blocker for automated feasibility checking. | `source_inventory.csv` (SRC-CMMS known issues: asset ID mapping) | `business-rules.md` (BR-02) | High confidence (explicit source metadata). |
| NLP extraction for port notices carries inherent accuracy risk. | `fleet_operations_interview_notes.md` (semantic conflicts) | `ddd-context-map.md` | High confidence (SME interview). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: DG-01 (sat-com limits) can be resolved via vendor SLAs before Stage 10 deployment design. | Vendor contracts are external to the FDE team. | Shore Platform Team | If unresolved, Stage 10 must default to ultra-conservative offline caching. | Stage 10 Deployment Topology. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Data and knowledge readiness assessment
Do not advance to Stage 07 until the Stage 06 exit gate is defensible.