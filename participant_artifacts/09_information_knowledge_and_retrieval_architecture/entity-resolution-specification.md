# Entity Resolution Specification

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer C: Connected Knowledge)
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To define the deterministic rules for resolving identity conflicts when the same real-world entity is represented differently across multiple source systems (e.g., AIS aliases, CMMS asset ID mismatches).

## Upstream dependency
Use the completed Stage 09 Canonical Identifier Strategy and Stage 06 Quality Profile.

## Evidence to inspect
- `evidence/04_policy_authority/source_authority.yaml`
- `evidence/01_enterprise_sources/source_inventory.csv`

## Case challenge
Entity resolution must be deterministic and rule-based, not probabilistic. The system must never "guess" an identity; it must rely on explicit authority precedence or flag the conflict for human review.

## Minimum content

| Entity Type | Conflicting Sources | Resolution Rule | Fallback / Human Escalation | Golden Scenario Link | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Vessel Identity** | SRC-AIS (Alias/MMSI) vs. SRC-FMS (Registry) | **Strict Precedence:** SRC-FMS `canonical_id` is absolute truth. AIS identity is stored only as an `OBSERVATION` linked to the FMS canonical ID. | If AIS cannot be matched to any FMS vessel, flag as `UNKNOWN_VESSEL` and alert Fleet Controller. | GS-04 (Cross-source vessel identity ambiguity) | `source_authority.yaml` |
| **Port Location** | SRC-PORT (API Name) vs. SRC-PORT (Notice PDF) | **Standardization:** Map both to UN/LOCODE. If fuzzy match confidence < 95%, flag as `PORT_IDENTITY_CONFLICT`. | Route to Fleet Controller for manual UN/LOCODE mapping before constraint is applied. | GS-11 (Conflicting berth evidence) | `fleet_operations_interview_notes.md` |
| **CMMS Asset** | SRC-TELEM (Vessel Local ID) vs. SRC-CMMS (Shore ID) | **Mapping Table:** Use the Tech Ops maintained mapping table. | If mapping is missing or ambiguous, the constraint is marked `UNVERIFIED_ASSET` and excluded from automated feasibility (requires manual Chief Engineer review). | GS-03 (Critical machinery hold) | `source_inventory.csv` (Asset ID mapping issue) |
| **Policy Document** | SRC-POLICY (Version A) vs. SRC-POLICY (Version B) | **Version Control:** Highest `version_number` with `status = ACTIVE` wins. | If two documents have the same version number but different hashes, flag as `POLICY_CORRUPTION` and halt ingestion. | GS-12 (Superseded policy trap) | `source_authority.yaml` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Vessel identity resolution is strictly deterministic based on FMS registry. | `source_authority.yaml` | `business-rules.md` (BR-06) | High confidence (explicit policy). |
| CMMS asset mapping failures must block automated feasibility to prevent safety risks. | `source_inventory.csv` | `risk-treatment-plan.md` | High confidence (explicit risk mitigation). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The UN/LOCODE mapping table for ports is maintained and accessible to the ACL. | Port data governance is external to MeridianBlue. | Fleet Data Integration Team | If unavailable, port identity resolution will fail frequently, increasing manual workload. | Stage 09 Data Ownership Map. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture