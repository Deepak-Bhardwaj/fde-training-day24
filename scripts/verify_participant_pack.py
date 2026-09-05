from pathlib import Path
import csv,json,re,sys
try:
    import yaml
except Exception:
    yaml=None
ROOT=Path(__file__).resolve().parents[1]
EXPECTED={
  "01_mandate_and_field_immersion": [
    "engagement-charter.md",
    "scope.md",
    "outcome-statement.md",
    "sponsor-owner.md",
    "governance-raci.md",
    "stakeholder-and-affected-groups-map.md",
    "field-evidence-register.md"
  ],
  "02_discover_process_and_architecture": [
    "sipoc.md",
    "process-value-stream-map.md",
    "waste-register.md",
    "system-landscape.md",
    "brownfield-assessment.md",
    "current-state-c4-views.md",
    "dependencies.md",
    "data-flows.md",
    "trust-boundaries.md"
  ],
  "03_frame_problem_root_cause_and_value": [
    "scqa-problem-frame.md",
    "root-cause-analysis.md",
    "baseline-dataset.csv",
    "kpi-tree.md",
    "ctqs.md",
    "value-hypothesis.md",
    "counter-metrics.md",
    "success-failure-criteria.md"
  ],
  "04_triage_regulation_and_qualify_use_case": [
    "impact-regulatory-screen.md",
    "prohibited-use-check.md",
    "ai-suitability-assessment.md",
    "non-ai-alternative.md",
    "use-case-card.md",
    "value-risk-feasibility-matrix.md",
    "go-no-go-kill-criteria.md"
  ],
  "05_model_the_domain": [
    "ubiquitous-language-glossary.md",
    "domain-capability-map.md",
    "business-rules.md",
    "decision-model.md",
    "domain-events.md",
    "ownership-map.md",
    "ddd-context-map.md",
    "bounded-contexts.md"
  ],
  "06_qualify_data_and_knowledge": [
    "data-knowledge-inventory.md",
    "lineage.md",
    "quality-profile.md",
    "provenance-baseline.md",
    "permissible-use-access-matrix.md",
    "representativeness-assessment.md",
    "data-gap-register.md",
    "dataset-datasheets.md"
  ],
  "07_define_evaluations_impacts_and_risks": [
    "evaluation-strategy.md",
    "golden-set-specification.md",
    "evaluation-scenarios.md",
    "acceptance-thresholds.md",
    "ai-impact-assessment.md",
    "risk-harms-register.md",
    "risk-treatment-plan.md",
    "oversight-transparency-requirements.md"
  ],
  "08_generate_test_and_select_options": [
    "solution-catalogue.md",
    "reference-architecture-comparison.md",
    "poc-model-rag-results.md",
    "weighted-tradeoff-matrix.md",
    "build-buy-compose-assessment.md",
    "provider-comparison.md",
    "preliminary-adrs.md",
    "selected-solution.md"
  ],
  "09_information_knowledge_and_retrieval_architecture": [
    "enterprise-source-authority-and-freshness-model.md",
    "data-ownership-map.md",
    "source-to-canonical-mapping.md",
    "target-information-trust-boundaries.md",
    "data-contracts.md",
    "semantic-model.md",
    "canonical-entity-model.md",
    "canonical-identifier-strategy.md",
    "metric-dimension-semantic-map.md",
    "ontology.md",
    "taxonomies.md",
    "semantic-constraints.md",
    "knowledge-graph-schema.md",
    "entity-resolution-specification.md",
    "knowledge-extraction-specification.md",
    "entity-relationship-model.md",
    "provenance-evidence-linkage-model.md",
    "property-graph-vs-rdf-adr.md",
    "graph-logical-model.md",
    "graph-persistence-architecture.md",
    "graph-query-traversal-patterns.md",
    "graph-analytics-requirements.md",
    "graph-indexing-strategy.md",
    "hybrid-retrieval-architecture.md",
    "retrieval-source-adapters.md",
    "retrieval-routing-policy.md",
    "retrieval-ranking-fusion-policy.md",
    "retrieval-evidence-contract.md",
    "runtime-context-graph-architecture.md",
    "runtime-entity-state-model.md",
    "context-assembly-model.md",
    "event-state-temporal-model.md",
    "context-freshness-policy.md",
    "metadata-model.md",
    "lineage-integration.md",
    "evidence-identifier-model.md",
    "authority-freshness-metadata-profile.md",
    "transformation-provenance.md",
    "target-data-architecture.md",
    "logical-information-architecture.md",
    "physical-persistence-topology.md",
    "batch-stream-runtime-data-flows.md",
    "data-adrs.md",
    "semantic-adrs.md",
    "graph-adrs.md",
    "retrieval-adrs.md",
    "ontology-schema.json",
    "graph-schema.json",
    "vector-schema.json"
  ],
  "10_design_ai_and_application_architecture": [
    "target-c4-context-view.md",
    "target-c4-container-view.md",
    "target-c4-component-view.md",
    "ai-rag-integration-architecture.md",
    "model-routing-design.md",
    "api-contracts.md",
    "prompt-context-design.md",
    "deployment-topology.md",
    "failure-mode-design.md",
    "architecture-adrs.md"
  ],
  "11_design_agentic_and_multi_agent_orchestration": [
    "agent-suitability-assessment.md",
    "autonomy-level-adr.md",
    "agent-responsibility-map.md",
    "orchestration-topology.md",
    "agent-interaction-sequence-diagram.md",
    "state-machine-model.md",
    "tool-action-catalogue.md",
    "identity-permission-matrix.md",
    "shared-memory-design.md",
    "handoff-protocol.md",
    "termination-loop-controls.md",
    "human-approval-override-escalation-matrix.md"
  ]
}
errors=[]

# 11 stages / 134 artifacts
pa=ROOT/'participant_artifacts'
count=0
for stage,files in EXPECTED.items():
    d=pa/stage
    if not d.is_dir(): errors.append(f'Missing stage: {stage}'); continue
    actual={p.name for p in d.iterdir() if p.is_file()}
    for f in files:
        if f not in actual: errors.append(f'Missing artifact: {stage}/{f}')
    extra=actual-set(files)
    if extra: errors.append(f'Unexpected artifacts in {stage}: {sorted(extra)}')
    count += len(actual)
if count!=134: errors.append(f'Artifact count {count} != 134')

# machine-readable evidence parses
for p in ROOT.rglob('*.json'):
    try: json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'Invalid JSON {p.relative_to(ROOT)}: {e}')
for p in ROOT.rglob('*.csv'):
    try:
        rows=list(csv.reader(p.open(encoding='utf-8-sig',newline='')))
        if not rows: errors.append(f'Empty CSV {p.relative_to(ROOT)}')
        elif any(len(r)!=len(rows[0]) for r in rows[1:]): errors.append(f'Ragged CSV {p.relative_to(ROOT)}')
    except Exception as e: errors.append(f'Invalid CSV {p.relative_to(ROOT)}: {e}')
if yaml:
    for p in ROOT.rglob('*.yaml'):
        try: yaml.safe_load(p.read_text(encoding='utf-8'))
        except Exception as e: errors.append(f'Invalid YAML {p.relative_to(ROOT)}: {e}')

# golden scenario consistency
ed=ROOT/'evidence/06_evaluations'
gold=json.loads((ed/'golden_scenarios.json').read_text())
gids=[x.get('scenario_id') for x in gold]
if len(gids)!=len(set(gids)): errors.append('Duplicate golden scenario IDs')
mat=list(csv.DictReader((ed/'evaluation_matrix.csv').open(encoding='utf-8-sig',newline='')))
mentioned=set()
for row in mat:
    for v in row.values(): mentioned.update(re.findall(r'GS-\d+',str(v)))
if set(gids)-mentioned: errors.append(f'Golden scenarios missing from evaluation matrix: {sorted(set(gids)-mentioned)}')
exp=json.loads((ed/'expected_behaviors.json').read_text())
if isinstance(exp,dict) and isinstance(exp.get('scenarios'),dict): eids=set(exp['scenarios'])
elif isinstance(exp,dict) and isinstance(exp.get('scenarios'),list): eids={x.get('scenario_id') for x in exp['scenarios']}
elif isinstance(exp,list): eids={x.get('scenario_id') for x in exp}
else: eids={k for k in exp if str(k).startswith('GS-')} if isinstance(exp,dict) else set()
if set(gids)-eids: errors.append(f'Golden scenarios missing expected behavior: {sorted(set(gids)-eids)}')

# source IDs unique
inv=list(csv.DictReader((ROOT/'evidence/01_enterprise_sources/source_inventory.csv').open(encoding='utf-8-sig',newline='')))
idcol='source_id' if inv and 'source_id' in inv[0] else None
if idcol:
    ids=[x[idcol] for x in inv]
    if len(ids)!=len(set(ids)): errors.append('Duplicate source IDs in source inventory')

# no obsolete participant lifecycle markers
for p in [ROOT/'START_HERE.md',ROOT/'Participant_Case_Study.md',ROOT/'Participant_Runbook.md',ROOT/'Participant_Artifact_Spine.md']:
    t=p.read_text(errors='ignore').lower()
    for bad in ['participant_templates','architecture stages 1–8','15-template','8-layer']:
        if bad in t: errors.append(f'Obsolete lifecycle marker {bad} in {p.name}')

# no fake wildcard path prose in artifacts
for p in pa.rglob('*.md'):
    t=p.read_text(errors='ignore')
    if re.search(r'participant_artifacts/\d+_\*',t): errors.append(f'Pseudo-path in {p.relative_to(ROOT)}')
    for section in ['## Evidence to inspect','## Working scaffold','## Completion check','## Handoff']:
        if section not in t: errors.append(f'Missing section {section} in {p.relative_to(ROOT)}')

# required spine image
if not (ROOT/'reference_visuals/AI_FDE_Stages_1_11_Artifact_Spine.png').exists(): errors.append('Missing canonical spine image')

if errors:
    print('PARTICIPANT PACK VERIFICATION: FAIL')
    for e in errors: print('-',e)
    sys.exit(1)
print('PARTICIPANT PACK VERIFICATION: PASS')
print('11 stage directories')
print('134 required artifact files')
print('JSON/CSV/YAML parse checks passed')
print('golden-scenario cross-reference checks passed')
print('source-ID uniqueness check passed')
print('no obsolete mandatory lifecycle markers')
