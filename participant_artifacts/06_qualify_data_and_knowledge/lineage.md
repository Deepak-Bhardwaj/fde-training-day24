# Lineage

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 06 — Qualify Data & Knowledge
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
Is the evidence trustworthy, permissible, traceable, representative and ready?

## Why this artifact exists
To document the end-to-end journey of critical data from its origin to its consumption in a recovery decision, ensuring no unapproved transformations or loss of provenance occur.

## Upstream dependency
Use the completed Stage 05 Domain Events, Stage 06 Data/Knowledge Inventory, and Stage 02 Data Flows.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
Focus on the critical path: how a raw external signal becomes a trusted constraint used in a recovery option.

## Minimum content

| Lineage Step | Source System / Actor | Transformation / Action | Destination System / Actor | Provenance Metadata Preserved | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Origin** | External Port Authority | Issues signed notice (PDF) and/or API update. | SRC-PORT | Document Hash, Issue Timestamp, Author. | `source_inventory.csv` |
| **2. Ingestion & ACL** | Shore Disruption Mgmt (ACL) | Parses API/Document. Resolves semantic conflict ("available" vs "confirmed") using `source_authority.yaml`. | Canonical Constraint View | SourceID, OriginalTimestamp, IngestionTimestamp, ResolutionRule. | `fleet_operations_interview_notes.md`, `ddd-context-map.md` |
| **3. Feasibility Check** | Deterministic Constraint Engine | Validates proposed recovery option against Canonical Constraint View (including CMMS holds). | Recovery Option Generator | PolicyVersion, ConstraintSourceID, EvaluationTimestamp. | `business-rules.md` (BR-02, BR-04) |
| **4. Human Review** | Fleet Controller UI | Presents feasible options with explicit evidence links to the Controller. | Fleet Controller | UI displays Source Freshness and Authority Weight for each constraint. | `fleet_operations_interview_notes.md` |
| **5. Execution & Audit** | Master / Vessel Command | Approves plan. Execution logs generated. | Compliance & Audit Context | MasterID, ApprovalTimestamp, VesselStateSnapshot, FinalOutcome. | `role_authorization_matrix.csv`, `domain-events.md` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Semantic resolution must occur at ingestion (Step 2) to prevent pollution of the core engine. | `fleet_operations_interview_notes.md` | `ddd-context-map.md` | High confidence (SME interview). |
| Audit trail (Step 5) must link the final outcome back to the original source freshness. | `fleet_operations_interview_notes.md` ("rationale, source freshness and later outcome are not linked") | `ctqs.md` | High confidence (SME interview). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The ACL can reliably extract structured constraints from unstructured PDF notices. | NLP extraction accuracy for maritime port notices not benchmarked. | FDE Team | If extraction fails, fallback to manual Controller entry is required. | Stage 09 Knowledge Extraction Specification. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Data and knowledge readiness assessment
Do not advance to Stage 07 until the Stage 06 exit gate is defensible.