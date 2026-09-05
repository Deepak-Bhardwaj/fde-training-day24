# Enterprise Source Authority & Freshness Model

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer A: Enterprise Source Layer)
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To formally define the precedence rules and temporal boundaries for all 9 enterprise data sources. This model is the absolute source of truth for the Anti-Corruption Layer (ACL) when resolving semantic or temporal conflicts.

## Upstream dependency
Use the completed Stage 05 Business Rules, Stage 06 Quality Profile, and Stage 08 Selected Solution.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
Define explicit, deterministic conflict resolution rules. Do not rely on "latest timestamp wins" if a lower-authority source updates more frequently than a higher-authority source.

## Minimum content

| Source ID | Source Name | Authority Precedence | Freshness Threshold | Conflict Resolution Rule | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **SRC-FMS** | Fleet Management / Voyage | HIGH (Canonical Identity) | 30 minutes | Overrides external identity observations (e.g., AIS aliases). | `source_authority.yaml` |
| **SRC-POLICY** | Fleet Policy Repository | HIGHEST (Active Rules Only) | Version/Status based | `status = ACTIVE` supersedes all. Superseded docs routed to Audit only. | `source_authority.yaml` |
| **SRC-PORT** | Port Systems / Notices | HIGH (Signed) / MEDIUM (API) | 60 minutes (or per notice) | Signed Notice PDF > Port API. API data flagged as "Unverified" if notice conflicts. | `source_inventory.csv`, `source_authority.yaml` |
| **SRC-CMMS** | CMMS | HIGH (Technical Constraints) | 15 minutes | Active maintenance holds are absolute feasibility blockers. No overrides. | `source_inventory.csv` |
| **SRC-TELEM** | Vessel Telemetry | OBSERVATION (Local Truth) | 5 minutes | Subject to clock drift. Deduplicated via composite key. Shore defers to vessel local state during blackout. | `source_inventory.csv`, `provenance-baseline.md` |
| **SRC-AIS** | AIS Provider | OBSERVATION (External) | 15 minutes | Lower precedence than SRC-FMS. Used for gap-filling, not canonical identity. | `source_inventory.csv`, `source_authority.yaml` |
| **SRC-WX** | Weather & Ocean | OBSERVATION (External) | 90 minutes | Forecast versioning applies. Stale data (>90m) flagged as "Unverified". | `source_inventory.csv` |
| **SRC-CARGO** | Cargo System | MEDIUM (Commercial Constraints) | 30 minutes | Purpose-filtered access. Cannot override safety/technical holds. | `source_inventory.csv` |
| **SRC-CREW** | Crew System | RESTRICTED (Personnel Constraints) | 60 minutes | Minimized access. AI strictly prohibited from using this for personnel decisions. | `source_inventory.csv` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Signed Port Notices hold higher precedence than Port API data. | `source_authority.yaml` (PORT_NOTICE_DOC precedence: HIGH_FOR_PORT_CONSTRAINT) | `quality-profile.md` | High confidence (explicit policy). |
| Telemetry is treated as observation subject to deduplication due to known edge flaws. | `source_inventory.csv` (SRC-TELEM known issues) | `provenance-baseline.md` | High confidence (explicit source metadata). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: The "Version/Status based" freshness for SRC-POLICY can be reliably detected via API webhooks or metadata. | Exact policy repo API capabilities not detailed. | Fleet Safety & Compliance | If undetectable, the system must poll at a fixed interval, risking brief windows of stale policy application. | Stage 09 Retrieval Source Adapters. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture
Do not advance to the next sub-layer until this artifact is defensible.