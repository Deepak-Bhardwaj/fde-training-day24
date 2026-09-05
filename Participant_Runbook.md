# Participant Runbook — Fleet Disruption & Voyage Recovery Intelligence Workbench

**Training boundary:** Synthetic training case only; not for navigation, vessel command or live fleet operations.

## Operating rule

Complete the stages in order. Do not begin with solution architecture, vendor selection, RAG or agents. Later stages must reference earlier decisions rather than recreating them.

## Before starting

1. Read `START_HERE.md` and `Participant_Case_Study.md`.
2. Inspect `evidence/01_enterprise_sources/source_inventory.csv` and the evidence README files.
3. Run `make verify` if Python is available.
4. Open `Participant_Artifact_Spine.md` and begin Stage 01.

## Stage gates

### 01. Mandate & Field Immersion
**Question:** Why are we here, what outcome matters, who owns it, and who is affected?
**Complete:** 7 artifacts in `participant_artifacts/01_mandate_and_field_immersion/`.
**Exit:** **Approved mandate and operating context**.

### 02. Discover Process & Architecture
**Question:** How does the real brownfield process and system operate today?
**Complete:** 9 artifacts in `participant_artifacts/02_discover_process_and_architecture/`.
**Exit:** **Current-state process and architecture baseline**.

### 03. Frame Problem, Root Cause & Value
**Question:** What evidence proves the problem, its causes and its value?
**Complete:** 8 artifacts in `participant_artifacts/03_frame_problem_root_cause_and_value/`.
**Exit:** **Evidence-backed problem and measurable baseline**.
Run `python scripts/profile_baseline.py` to independently check the supplied baseline fixture; your Stage 3 artifact still needs your own interpretation and calculation definitions.

### 04. Triage Regulation & Qualify Use Case
**Question:** Should AI be used at all, and under what impact/regulatory constraints?
**Complete:** 7 artifacts in `participant_artifacts/04_triage_regulation_and_qualify_use_case/`.
**Exit:** **Approved and justified use case**.

### 05. Model the Domain
**Question:** What does the business actually mean, decide and own?
**Complete:** 8 artifacts in `participant_artifacts/05_model_the_domain/`.
**Exit:** **Domain and decision model**.

### 06. Qualify Data & Knowledge
**Question:** Is the evidence trustworthy, permissible, traceable, representative and ready?
**Complete:** 8 artifacts in `participant_artifacts/06_qualify_data_and_knowledge/`.
**Exit:** **Data and knowledge readiness assessment**.

### 07. Define Evaluations, Impacts & Risks
**Question:** What must the future system prove before it is acceptable?
**Complete:** 8 artifacts in `participant_artifacts/07_define_evaluations_impacts_and_risks/`.
**Exit:** **Evaluation, impact and risk requirements**.
At minimum, explicitly cover stress scenarios GS-02, GS-03, GS-04, GS-05, GS-07, GS-08, GS-09, GS-14, GS-15.

### 08. Generate, Test & Select Options
**Question:** Which solution survives evidence, alternatives and trade-offs?
**Complete:** 8 artifacts in `participant_artifacts/08_generate_test_and_select_options/`.
**Exit:** **Approved solution and trade-offs**.
Never manufacture PoC/model/RAG results. `NOT RUN` is valid evidence; it becomes an explicit gap/condition on the selection decision.

### 09. Information, Knowledge & Retrieval Architecture
**Question:** How does enterprise evidence become canonical meaning, connected knowledge and runtime context?
**Complete:** 49 artifacts in `participant_artifacts/09_information_knowledge_and_retrieval_architecture/`.
**Exit:** **Approved information architecture**.

### 10. AI & Application Architecture
**Question:** How will the AI-enabled application consume context, integrate, deploy and fail safely?
**Complete:** 10 artifacts in `participant_artifacts/10_design_ai_and_application_architecture/`.
**Exit:** **Complete base AI/application architecture**.

### 11. Agentic & Multi-Agent Orchestration
**Question:** Is autonomy justified, bounded, permissioned, interruptible and testable?
**Complete:** 12 artifacts in `participant_artifacts/11_design_agentic_and_multi_agent_orchestration/`.
**Exit:** **Approved, bounded and testable agentic architecture**.
Complete `agent-suitability-assessment.md` first. A `NO AGENT` conclusion is acceptable; remaining Stage 11 files then document justified N/A boundaries.

## Optional application build

Only after Stage 11, you may use `99_optional_build_extension/` to turn the approved solution into an application concept. It is not a substitute for the 134 artifacts.

## Submission

Submit the complete `participant_artifacts/` tree. Keep original evidence unchanged.
