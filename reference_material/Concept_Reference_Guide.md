# Participant Reference Guide — Concepts, Not Answers

This guide explains architecture responsibilities. It is not a prescribed solution for **Fleet Disruption & Voyage Recovery Intelligence Workbench**.

| Responsibility | Question to answer | Common failure |
|---|---|---|
| Enterprise sources | What evidence exists, who owns it, and how fresh/authoritative is it? | Treating every source as equally authoritative |
| Semantic foundation | What does the business mean consistently? | Canonicalizing genuinely different concepts into one field |
| Connected knowledge | Which entities/facts are related and with what provenance/time? | Calling a JSON object a knowledge graph |
| Graph platform | What relationships require persistent traversal? | Adding graph technology without a query need |
| Hybrid retrieval | Which evidence mechanism fits each question? | Using vector similarity as authority |
| Runtime context | What subset matters now for this actor/task/time? | Dumping the entire corpus into a prompt |
| AI/application | How is context consumed through controls/contracts? | Leaving authorization to prompt wording |
| Agentic orchestration | Is autonomy actually justified and bounded? | Using multiple agents because the framework supports them |

## Technology selection rule
Choose products only after responsibilities, constraints, query patterns, controls and failure modes are known. Reuse an existing enterprise platform where it satisfies the requirement; avoid one specialist product per box without evidence.
