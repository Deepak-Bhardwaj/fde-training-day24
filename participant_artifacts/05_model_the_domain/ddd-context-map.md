# DDD Context Map

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 05 — Model the Domain
**Participant status:** COMPLETED
**Deliverable form:** Diagram + supporting table + rationale

## Stage question
What does the business actually mean, decide and own?

## Why this artifact exists
To visualize the boundaries between different sub-domains and define the integration patterns between them. This is critical for ensuring the vessel-side system can operate independently of the shore-side systems.

## Upstream dependency
Use the completed Stage 05 Ownership Map, Domain Events, and Stage 02 Current-State C4 Views.

## Evidence to inspect
- `evidence/02_documents/fleet_operations_interview_notes.md`
- `evidence/01_enterprise_sources/source_inventory.csv`

## Case challenge
Explicitly define where Anti-Corruption Layers (ACLs) are needed to protect the core domain from external semantic conflicts (e.g., Port API semantics).

## Diagram Description (Context Map)
*(Note: Text-based representation of the C4/DDD context map.)*

1. **[External Intelligence Context]** (Port, WX, AIS) --> *Customer-Supplier* --> **[Shore Disruption Management Context]**
2. **[Shore Disruption Management Context]** <-- *Conformist / Sync* --> **[Vessel Command & Edge Context]**
3. **[Vessel Command & Edge Context]** --> *Publish-Event (Audit)* --> **[Compliance & Audit Context]**
4. **[Shore Disruption Management Context]** --> *Publish-Event (Audit)* --> **[Compliance & Audit Context]**
5. **[External Intelligence Context]** -- *ACL (Semantic Translation)* --> **[Shore Disruption Management Context]**

## Working scaffold (Relationship Details)

| Upstream Context | Downstream Context | Relationship Pattern | Rationale / Translation Mechanism | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **External Intelligence** | **Shore Disruption Mgmt** | **Customer-Supplier + ACL** | External APIs have conflicting semantics (e.g., "available" vs "confirmed"). An Anti-Corruption Layer translates external payloads into the canonical ubiquitous language before ingestion. | `fleet_operations_interview_notes.md`, `source_inventory.csv` |
| **Shore Disruption Mgmt** | **Vessel Command & Edge** | **Conformist (Offline Sync)** | The vessel edge conforms to the shore's canonical constraint view when online. During blackouts, the vessel relies on its cached, conformist state to operate safely. | `fleet_operations_interview_notes.md` (divergence risk) |
| **Vessel Command & Edge** | **Shore Disruption Mgmt** | **Upstream/Downstream (Reconnect)** | Upon reconnect, the vessel acts as the upstream authority for its local execution state, pushing events to the shore for reconciliation. | `data-flows.md` |
| **All Operational Contexts** | **Compliance & Audit** | **Publish-Event (Open Host Service)** | All contexts publish immutable domain events (e.g., PlanApproved, HoldReleased) to the Audit context for reconstructable decision traces. | `fleet_operations_interview_notes.md` (weak post-event learning) |

## Rationale
The most critical boundary is between the Shore and the Vessel. Because connectivity is unreliable (GS-14), the Vessel Command context cannot be a mere "client" of the Shore context; it must be a fully autonomous bounded context that caches the necessary canonical state. The Anti-Corruption Layer at the External Intelligence boundary is mandatory to prevent the "semantic fragmentation" waste identified in Stage 02 from polluting the core deterministic engine.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| An ACL is required to handle Port API semantic conflicts. | `fleet_operations_interview_notes.md` | `waste-register.md` | High confidence (SME interview). |
| The Vessel context must be autonomous to support offline continuity. | `fleet_operations_interview_notes.md` | `ctqs.md` | High confidence (SME interview). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The "Compliance & Audit" context can ingest events from both vessel and shore without identity collisions. | Event ID generation strategy across disconnected zones not fully defined. | FDE Team | Requires a robust canonical identifier strategy in Stage 09. | Stage 09 Canonical Identifier Strategy. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Domain and decision model
Do not advance to Stage 06 until the Stage 05 exit gate is defensible.