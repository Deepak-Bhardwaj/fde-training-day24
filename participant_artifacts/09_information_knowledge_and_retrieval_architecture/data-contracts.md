# Data Contracts

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer A: Enterprise Source Layer)
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To formally define the schema, SLA, and versioning agreements between data producers (source systems) and consumers (the Workbench), preventing silent breaking changes.

## Upstream dependency
Use the completed Stage 09 Source-to-Canonical Mapping and Stage 06 Provenance Baseline.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/01_enterprise_sources/live_event_stream.jsonl`

## Case challenge
Define contracts that explicitly include the temporal provenance envelope required by the architecture, not just the business payload.

## Minimum content

| Contract ID | Provider | Consumer | Schema Version | SLA / Freshness | Breaking Change Policy | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **DC-TELEM-01** | SRC-TELEM (Vessel Edge) | Shore Ingestion ACL | v1.2 (JSON) | 99.9% uptime, < 5 min latency | Must be backward compatible. New fields allowed; removal requires 30-day deprecation notice and version bump. | `source_inventory.csv`, `live_event_stream.jsonl` |
| **DC-PORT-01** | SRC-PORT (External) | Shore Ingestion ACL | v2.0 (API + PDF) | 99.0% uptime, < 60 min latency | API changes must be documented in developer portal. PDF format changes require NLP model retraining (triggers human fallback). | `source_inventory.csv` |
| **DC-CMMS-01** | SRC-CMMS (Internal) | Deterministic Engine | v1.0 (Event Stream) | 99.5% uptime, < 15 min latency | `criticality` and `status` enums are strictly controlled by Technical Operations. Changes require FDE team approval. | `source_inventory.csv` |
| **DC-CANONICAL-01** | Shore Canonical Store | Vessel Edge Cache | v1.0 (Protobuf) | Sync upon reconnect, or hourly if online | Schema is immutable for 6 months. Vessel edge must be able to parse v1.0 even if shore upgrades to v1.1. | `ddd-context-map.md` |
| **DC-POLICY-01** | SRC-POLICY (Internal) | Retrieval Layer | v1.0 (JSON/Text) | Real-time on `status` change | `status` field is mandatory. Any document without `status = ACTIVE` or `SUPERSEDED` is rejected by the contract validator. | `source_authority.yaml` |

## Evidence and traceability

| Claim / decision | Evidence file + record / policy version / scenario | Upstream artifact | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| Telemetry contract must enforce backward compatibility to prevent vessel edge sync failures. | `live_event_stream.jsonl` structure | `target-information-trust-boundaries.md` | High confidence (architectural best practice). |
| Policy contract strictly requires the `status` field to prevent retrieval traps. | `source_authority.yaml` | `quality-profile.md` | High confidence (explicit policy). |

## Open issues / assumptions

| Issue / assumption | Why unresolved | Owner | Downstream impact | Closure evidence |
| :--- | :--- | :--- | :--- | :--- |
| Assumption: External providers (SRC-PORT, SRC-WX) will adhere to the 30-day deprecation notice for API changes. | Vendor contracts are managed by Procurement, not the FDE team. | Executive Sponsor / Legal | If vendors break contracts silently, the ACL must implement aggressive schema validation and alerting. | Stage 09 Retrieval Source Adapters. |

## Completion check
- [x] Minimum content above is complete.
- [x] Material claims cite exact evidence or are labelled assumptions.
- [x] Conflicting/stale evidence is preserved rather than silently resolved.
- [x] Human, deterministic and AI decision rights are distinguishable where relevant.
- [x] The artifact does not contradict approved upstream artifacts.

## Handoff
**Stage exit contribution:** Approved information architecture
Do not advance to the next sub-layer until this artifact is defensible.