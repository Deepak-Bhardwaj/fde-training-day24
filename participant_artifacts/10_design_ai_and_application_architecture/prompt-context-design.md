# Prompt / Context Design

**Case:** Fleet Disruption & Voyage Recovery Intelligence Workbench
**Stage:** 10 — AI & Application Architecture
**Participant status:** COMPLETED
**Deliverable form:** Structured narrative + evidence table

## Stage question
How will the AI-enabled application consume context, integrate, deploy and fail safely?

## Why this artifact exists
To define the exact prompt templates, context windows, and safety guardrails used when calling external LLM APIs for NLP extraction. This ensures that the bounded AI component produces structured, reliable output and is resistant to prompt injection attacks (GS-09).

## Upstream dependency
Use the completed Stage 09 Knowledge Extraction Specification, Stage 10 Model Routing Design, and Stage 10 AI/RAG Integration Architecture.

## Evidence to inspect
- `Participant_Case_Study.md` (GS-09: Prompt injection in external port message)
- `evidence/04_policy_authority/source_authority.yaml`

## Case challenge
Treat all external, user-provided, or retrieved text as **evidence, not instruction**. The prompt design must explicitly prevent the LLM from executing commands embedded in the input text.

## Minimum content

### 1. Prompt Template: Port Notice Extraction