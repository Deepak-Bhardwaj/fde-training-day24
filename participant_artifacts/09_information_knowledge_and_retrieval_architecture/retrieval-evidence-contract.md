# Retrieval Evidence Contract

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 09 — Information, Knowledge & Retrieval Architecture (Sub-layer E: Hybrid Retrieval)
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
How does enterprise evidence become canonical meaning, connected knowledge and runtime context?

## Why this artifact exists
To define the strict API contract for the Retrieval Layer, ensuring that every piece of context returned to the Deterministic Engine or UI includes the mandatory Provenance Envelope and Authority Metadata.

## Upstream dependency
Use the completed Stage 06 Provenance Baseline and Stage 09 Retrieval Ranking/Fusion Policy.

## Evidence to inspect
- `evidence/02_documents/fleet_operations_interview_notes.md`
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
The contract must prevent "black box" context. If the UI displays a constraint, the user must be able to see exactly where it came from, when it was observed, and its authority level.

## Minimum content

### 1. Standard Retrieval Response Payload
Every response from the Retrieval Layer must conform to this structure:
```json
{
  "query_id": "uuid",
  "retrieval_timestamp": "ISO8601",
  "results": [
    {
      "entity_id": "string",
      "entity_type": "Constraint | PolicyRule | HistoricalPrecedent",
      "payload": { ... },
      "provenance": {
        "source_id": "SRC-PORT | SRC-CMMS | etc.",
        "observed_timestamp": "ISO8601",
        "ingestion_timestamp": "ISO8601",
        "authority_weight": "HIGHEST | HIGH | MEDIUM | OBSERVATION | NON_AUTHORITATIVE",
        "freshness_state": "FRESH | STALE | EXPIRED | UNVERIFIED"
      },
      "retrieval_metadata": {
        "source_store": "GRAPH | VECTOR | KEYWORD",
        "confidence_score": 0.0 to 1.0
      }
    }
  ]
}