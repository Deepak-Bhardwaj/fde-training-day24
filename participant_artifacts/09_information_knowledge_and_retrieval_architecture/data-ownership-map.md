# Data Ownership Map

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer A: Enterprise Source Layer)
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To explicitly define the business and technical ownership of each data domain, ensuring clear accountability for data quality, access provisioning, and schema changes.

## Upstream dependency
Use the completed Stage 05 Ownership Map and Stage 06 Data/Knowledge Inventory.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/04_policy_authority/role_authorization_matrix.csv`

## Case challenge
Distinguish between the *Business Owner* (accountable for data accuracy and policy) and the *Technical Steward* (responsible for pipeline uptime and schema enforcement).

## Minimum content

| Data Domain | Source ID | Business Owner | Technical Steward | Access Boundary / Classification | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Vessel Identity & Schedule** | SRC-FMS | Fleet Operations Director | FMS Platform Team | Internal Use. Read by all operational contexts. | `source_inventory.csv` |
| **Navigational Observations** | SRC-AIS, SRC-TELEM | Vessel Technical / Master | Shore Platform / Edge Team | Internal Use. Telemetry restricted to vessel/fleet ops. | `source_inventory.csv` |
| **Port Constraints** | SRC-PORT | External Port Authority | Fleet Data Integration Team | External Source. Treated as untrusted until validated by ACL. | `source_inventory.csv` |
| **Weather Forecasts** | SRC-WX | External Provider | Fleet Data Integration Team | External Source. Licensed data, subject to vendor terms. | `source_inventory.csv` |
| **Maintenance & Technical Holds** | SRC-CMMS | Technical Operations Director | CMMS Platform Team | Internal Use. Critical safety data. High integrity required. | `source_inventory.csv` |
| **Cargo Properties & Windows** | SRC-CARGO | Cargo Operations Director | Cargo Platform Team | Confidential. Strict tenant isolation. Purpose-filtered access only. | `source_inventory.csv` |
| **Crew Availability & Rest** | SRC-CREW | Marine HR Director | HR Systems Team | Highly Restricted / PII. Minimized access. AI access prohibited. | `source_inventory.csv` |
| **Fleet Policies & Rules** | SRC-POLICY | Fleet Safety & Compliance | Compliance Systems Team | Internal Use. Versioned. Active status required for operational use. | `source_inventory.csv` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Crew data is classified as Highly Restricted/PII, mandating minimized access. | `source_inventory.csv` (SRC-CREW access_boundary: LIMITED/role based) | `permissible-use-access-matrix.md` | High confidence (explicit policy). |
| External sources (Port, WX) are treated as untrusted until validated by the ACL. | `fleet_operations_interview_notes.md` (semantic conflicts) | `ddd-context-map.md` | High confidence (SME interview). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The Technical Steward for SRC-CMMS can guarantee the 15-minute freshness threshold. | Legacy CMMS batch export schedules may conflict with this SLA. | Technical Operations | May require upgrading from batch to event-driven streaming for CMMS. | Stage 09 Batch/Stream/Runtime Data Flows. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture
Do not advance to the next sub-layer until this artifact is defensible.