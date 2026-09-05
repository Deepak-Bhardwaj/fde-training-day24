# Authority / Freshness Metadata Profile

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer G: Metadata / Lineage / Provenance)
**Participant status:** COMPLETED
**Deliverable form:** Structured analysis / specification

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To define the exact, non-negotiable metadata envelope that must accompany every piece of data as it moves through the system. This profile enforces the trust boundaries and ensures the deterministic engine can make authority-weighted, temporally valid decisions.

## Upstream dependency
Use the completed Stage 09 Enterprise Source Authority Model, Context Freshness Policy, and Retrieval Evidence Contract.

## Evidence to inspect
- `evidence/01_enterprise_sources/source_inventory.csv`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
The metadata profile must be strictly enforced at the Ingestion ACL. If a data payload arrives without this complete metadata envelope, it must be rejected and logged as a data quality failure.

## Minimum content

### 1. The Mandatory Metadata Envelope (JSON Schema)
```json
{
  "provenance": {
    "source_id": "SRC-PORT | SRC-CMMS | SRC-TELEM | etc.",
    "observed_timestamp": "ISO8601",
    "ingestion_timestamp": "ISO8601",
    "source_version": "string (e.g., document hash or API version)",
    "authority_weight": "HIGHEST | HIGH | MEDIUM | OBSERVATION | NON_AUTHORITATIVE"
  },
  "freshness": {
    "threshold_minutes": 60,
    "current_state": "FRESH | STALE | EXPIRED | UNVERIFIED",
    "valid_until": "ISO8601"
  },
  "transformation": {
    "acl_rule_version": "string",
    "nlp_confidence_score": 0.98,
    "hitl_override": false
  }
}