# Domain Events

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 05 — Model the Domain
**Participant status:** COMPLETED
**Deliverable form:** Structured table / register

## Stage question
What does the business actually mean, decide and own?

## Why this artifact exists
To define the significant occurrences within the domain that trigger state changes or require action. These events form the backbone of the system's reactive architecture and audit trail.

## Upstream dependency
Use the completed Stage 05 Business Rules, Decision Model, and Ubiquitous Language Glossary.

## Evidence to inspect
- `evidence/01_enterprise_sources/live_event_stream.jsonl`
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/02_documents/fleet_operations_interview_notes.md`

## Case challenge
Ensure every event carries strict temporal provenance and is designed for idempotent processing to handle telemetry clock drift and duplicate deliveries.

## Minimum content

| Event Name | Trigger / Cause | Key Payload / Data | Authority / Owner | Idempotency / Provenance Rule | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **DisruptionDetected** | Threshold breach in telemetry, port notice, or weather alert. | DisruptionID, VesselID, EventType, SourceID, ObservedTimestamp. | Deterministic Engine | Must be deduplicated by (VesselID, EventType, TimeWindow). | `live_event_stream.jsonl` |
| **SourceDataIngested** | Raw data received from an external or internal source. | SourceID, RawPayload, IngestionTimestamp, SourceFreshnessThreshold. | Ingestion Adapter | Tagged with strict ingestion time; handles out-of-order delivery. | `source_inventory.csv` |
| **SemanticConflictResolved** | System detects and resolves conflicting data (e.g., Port API vs Notice). | ConflictID, WinningSourceID, LosingSourceID, ResolutionRuleApplied. | Deterministic Engine | Resolution must follow `source_authority.yaml` precedence. | `fleet_operations_interview_notes.md` |
| **ConstraintViewUpdated** | The unified, reconciled view of vessel constraints is refreshed. | VesselID, ActiveCMMSHolds, CargoWindows, PolicyVersion, Timestamp. | Shore Platform / Vessel Edge | Replaces previous view; acts as the single source of truth for planning. | `process-value-stream-map.md` |
| **RecoveryOptionGenerated** | System drafts a potential recovery plan based on constraints. | OptionID, DisruptionID, ProposedActions, FeasibilityScore, AI_Draft_Flag. | Deterministic Engine / AI (Non-Auth) | Marked explicitly as NON_AUTHORITATIVE if AI-assisted. | `non-ai-alternative.md` |
| **PlanApproved** | Master explicitly signs off on a specific recovery option. | OptionID, MasterID, ApprovalTimestamp, VesselStateSnapshot. | Master (Human) | Immutable audit record; triggers execution workflow. | `role_authorization_matrix.csv` |
| **TechnicalHoldReleased** | Chief Engineer clears a critical CMMS maintenance hold. | HoldID, VesselID, EngineerID, ReleaseTimestamp, MaintenanceReportRef. | Chief Engineer (Human) | Hard unblocks the constraint engine for future planning. | `role_authorization_matrix.csv` |
| **ConnectivityRestored** | Vessel-to-shore sat-com link is re-established after a blackout. | VesselID, BlackoutDuration, PendingLocalEventsCount. | Vessel Edge Comms | Triggers safe state reconciliation and batch sync of offline logs. | `fleet_operations_interview_notes.md` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| All events must support idempotent processing to handle telemetry flaws. | `source_inventory.csv` (SRC-TELEM duplicate delivery) | `business-rules.md` (BR-05) | High confidence (explicit source metadata). |
| PlanApproved is the ultimate trigger for execution; no prior AI event can execute. | `role_authorization_matrix.csv` | `decision-model.md` | High confidence (explicit policy). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The event bus can handle the payload size of "VesselStateSnapshot" during low-bandwidth reconnects. | Sat-com bandwidth limits for event payloads not fully quantified. | Shore Platform Team | May require payload compression or delta-sync logic in Stage 10. | Stage 10 Deployment Topology / API Contracts. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Domain and decision model
Do not advance to Stage 06 until the Stage 05 exit gate is defensible.