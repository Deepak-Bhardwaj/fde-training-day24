# Context Freshness Policy

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer F: Runtime Context Graph)
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To define the explicit rules for when runtime context is considered too stale to be used for automated feasibility checking, and what degradation mode the system must enter.

## Upstream dependency
Use the completed Stage 06 Quality Profile and Stage 09 Event/State/Temporal Model.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
The system must not silently use expired data. It must actively detect staleness and escalate to human operators, preserving safety over automation.

## Minimum content

| Source / Constraint Type | Freshness Threshold | Stale Warning Trigger | Expired Action (Engine Behavior) | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **SRC-TELEM (Machinery)** | 5 minutes | > 3 minutes | Exclude from feasibility check. Flag vessel status as `UNKNOWN`. | `source_inventory.csv` |
| **SRC-CMMS (Maintenance)** | 15 minutes | > 10 minutes | **CRITICAL:** If hold was previously active, assume STILL ACTIVE (fail-safe). Alert Chief Engineer. | `source_inventory.csv`, `business-rules.md` |
| **SRC-PORT (API)** | 60 minutes | > 45 minutes | Downgrade authority to `UNVERIFIED`. Require manual Controller confirmation. | `source_inventory.csv` |
| **SRC-PORT (Signed Notice)** | Per document validity | N/A | Valid until `valid_until` date explicitly stated in the document. | `source_authority.yaml` |
| **SRC-WX (Weather)** | 90 minutes | > 75 minutes | Exclude from automated scoring. Display "Weather data stale" warning to Master. | `source_inventory.csv` |
| **SRC-POLICY (Rules)** | Version-based | N/A | `SUPERSEDED` policies are immediately excluded from the Runtime Context Graph. | `source_authority.yaml` |

### Degradation Modes
1. **Partial Degradation:** If non-critical sources (e.g., WX) are stale, the engine proceeds but flags the recovery option's confidence score as `REDUCED`.
2. **Full Degradation (Offline/Blackout):** If connectivity is lost, the system relies *only* on the cached Runtime Context Graph. Any new external constraints are ignored until reconnect.

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| CMMS holds must default to "still active" if data is stale, prioritizing safety. | `business-rules.md` (BR-02) | `acceptance-thresholds.md` | High confidence (non-negotiable constraint). |
| Port API data must be manually verified if it exceeds the freshness threshold. | `fleet_operations_interview_notes.md` | `retrieval-ranking-fusion-policy.md` | High confidence (SME interview). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The UI can clearly communicate "Partial Degradation" to the Master without causing alarm fatigue. | UI/UX design for degradation states is pending. | FDE Team / Master | Poor UX may lead to Masters ignoring staleness warnings. | Stage 10 Target C4 Views. |

## Completion check
- [x] Minimum content above is8 complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture