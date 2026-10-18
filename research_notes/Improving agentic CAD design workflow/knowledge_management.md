# Knowledge Management for AI Design Agents (ThinkToCad)

## How do engineering knowledge bases structure knowledge (ontologies, knowledge graphs, taxonomies)?

### Takeaway
Engineering knowledge bases for AI agents are best organized as structured knowledge graphs (entities + typed relations) plus taxonomies of mechanisms/constraints, mirroring Karniadakis' "Graph Ontologist" pattern; a lightweight YAML graph plus per-entity markdown files is sufficient for small toolkits.

### Cited Findings
- Karniadakis et al. (arXiv:2511.03179) build two domain-specific knowledge graphs from literature via a "Graph Ontologist" agent that extracts (node1, node2, edge) triples; the Systems Engineer KG has ~700 nodes, the Design Engineer KG ~50 nodes, both filtered to degree >= 10. — [arXiv:2511.03179](https://arxiv.org/abs/2511.03179)
- The same paper stores KGs as CSV (nodes + relationships), chunked with metadata (chunk ID, source reference, row range) and embedded into a vector store for similarity retrieval. — [arXiv:2511.03179](https://arxiv.org/abs/2511.03179)
- Karniadakis et al. argue KGs "go beyond simple text-based information retrieval" and allow discovery of novel connections between ontologically linked concepts; they also provide transparency/explainability by tracing recommendations to graph edges. — [arXiv:2511.03179](https://arxiv.org/abs/2511.03179)
- Ontology engineering (Wikipedia) defines ontologies as TBox (concept classes), ABox (individuals), and RBox (roles/properties) axioms, typically formalized in OWL/RDF and description logics, with tools like Protégé. — [Wikipedia: Ontology engineering](https://en.wikipedia.org/wiki/Ontology_engineering)
- The manufacturing-ontology literature cited in that article (Pouchard, Ivezic, Schlenoff, NIST) targets distributed collaboration in manufacturing, explicitly motivating ontology engineering for engineering knowledge. — [Wikipedia: Ontology engineering](https://en.wikipedia.org/wiki/Ontology_engineering)
- Siemens AEI (arXiv:2604.07784) builds offline memory stores that include knowledge graphs plus retrieval stores and relational workflow records from heterogeneous artifacts (slide decks, reports, recordings). — [arXiv:2604.07784](https://arxiv.org/abs/2604.07784)
- ThinkToCad's own `knowledge/README.md` partitions knowledge into Declarative (mechanisms/, constraints/), Procedural (graph.yaml), Experiential (lessons/, memory/), with `graph.yaml` holding typed edges (requires, conflicts_with, replaces, alternative_to, constrained_by, verified_by, sourced_from). — local: `knowledge/README.md`, `knowledge/graph.yaml`

### Inferences
- For a small mechanical toolkit, a full OWL/RDF ontology is overkill; the ThinkToCad YAML graph + per-entity markdown files already implements a pragmatic "lightweight ontology" (entities + typed relations + attributes), which matches the Karniadakis triple pattern at lower cost.
- Different agents/roles should get different graph slices (e.g., a "designer" subgraph vs. a "reviewer" subgraph), as Karniadakis does with two KGs of differing scope (~700 vs ~50 nodes).
- Degree-filtering (keep nodes with degree >= 10) is a useful hygiene rule to keep the graph compact and navigable.

### Gaps
- I did not find primary-source details on MASON/MSDL/Core Manufacturing Simulation Data specifics beyond the Wikipedia ontology-engineering reference; their exact class hierarchies and relation sets were not retrieved. Treat MASON/MSDL as background context, not cited fact.

## RAG vs GraphRAG vs Hierarchical RAG (HERA): when to use each?

### Takeaway
Use flat RAG (dense/BM25/hybrid) for open-domain factoid or homogeneous-tabular corpora; use GraphRAG when multi-hop relational reasoning over a knowledge graph matters; use corpus navigation (Corpus2Skill-style hierarchical skills) for bounded single-domain corpora with a recoverable topical taxonomy; use HERA's experience-guided multi-agent RAG when queries need adaptive multi-step orchestration and continual behavior improvement.

### Cited Findings
- Microsoft GraphRAG (repo README) is "a data pipeline and transformation suite that extracts meaningful, structured data from unstructured text using LLMs" into knowledge-graph memory structures to enhance LLM outputs; arXiv paper 2404.16130. — [github.com/microsoft/graphrag](https://github.com/microsoft/graphrag)
- Corpus2Skill (arXiv:2604.14572) positions itself against GraphRAG/HiRAG: those "build knowledge graphs with community-level summaries but rely on graph retrieval at query time," whereas Corpus2Skill materializes a browsable skill tree and replaces retrieval with agentic navigation. — [arXiv:2604.14572](https://arxiv.org/abs/2604.14572)
- Corpus2Skill's 11-dataset study: navigation significantly wins on 5 datasets, ties on 3, loses on 3; it helps on "single-domain corpora with a recoverable topical taxonomy" but flat retrieval stays preferable on "open-domain factoid pools or homogeneous-tabular corpora that defeat top-level clustering" (HAGRID, TatQA, CUAD). — [arXiv:2604.14572](https://arxiv.org/abs/2604.14572)
- HERA (arXiv:2604.00901) is a "Hierarchical Evolving RAG" framework: it jointly evolves multi-agent orchestration (query-specific agent topologies via reward-guided sampling + experience accumulation) and role-specific agent prompts (credit assignment + dual-axes adaptation) over a frozen LLM. — [arXiv:2604.00901](https://arxiv.org/abs/2604.00901)
- HERA achieves "an average improvement of 38.69% over recent baselines" on six knowledge-intensive benchmarks while maintaining token efficiency; it uses an Experience Library with Profile-Insight-Utility (c, z, u) entries updated via ADD/MERGE/PRUNE/KEEP. — [arXiv:2604.00901](https://arxiv.org/abs/2604.00901)
- Corpus2Skill's compile phase: embed documents, K-Means cluster (branching ratio p, max top-level K), LLM-summarize each cluster, verify-and-repartition confusable/mixed clusters, cross-reference documents whose top-1/top-2 cosine gap < margin τ, surface exemplars, build entity_index.json for lateral jumps; depth grows O(log_p N). — [arXiv:2604.14572](https://arxiv.org/abs/2604.14572)
- RAPTOR (cited in Corpus2Skill) recursively clusters and summarizes chunks into a tree retrieved by collapsed-tree vector search; Corpus2Skill shares the embed-cluster-summarize loop but materializes it as navigable files and replaces fixed traversal with agentic navigation. — [arXiv:2604.14572](https://arxiv.org/abs/2604.14572)

### Inferences
- ThinkToCad's corpus is small, single-domain, and topically structured (mechanisms, constraints, lessons) — exactly the regime where Corpus2Skill-style hierarchical navigation helps; flat dense retrieval alone would underperform for multi-mechanism design queries.
- HERA-style experience libraries are overkill for a single-agent toolkit but the Profile-Insight-Utility memory record and ADD/MERGE/PRUNE/KEEP consolidation policy are directly reusable for ThinkToCad's `memory/lessons/`.
- GraphRAG's entity/community summarization is the closest analog to ThinkToCad's `graph.yaml` edges; if ThinkToCad grows beyond ~hundreds of entities, migrating graph.yaml to a real KG store with community summaries would be warranted.

### Gaps
- I did not retrieve primary sources for LightRAG or HippoRAG specifics; their exact retrieval mechanisms (e.g., HippoRAG's Personalized PageRank, LightRAG's dual-level retrieval) are not cited here and should be verified before claiming.

## How do systems capture and reuse "lessons learned" / experiential knowledge?

### Takeaway
Experiential knowledge is captured as structured records of both successes and failures (attempt YAMLs, reasoning logs, trajectory insights) and reused via retrieval at decision time; the most transferable pattern for ThinkToCad is HERA's Profile-Insight-Utility experience entries plus AEI's per-study reasoning logs, combined with ThinkToCad's existing lessons/ folder format.

### Cited Findings
- ThinkToCad's `knowledge/lessons/README.md` specifies one markdown file per lesson with Date, Design, Status (failed|succeeded), What happened, Root cause, Fix/rule going forward; "Failed attempts are as valuable as successes." — local: `knowledge/lessons/README.md`
- ThinkToCad's `memory/README.md` stores per-design attempt YAMLs (mechanism, status, verification: interference/clearance/mass, timestamp) under `memory/designs/<name>/attempt_N.yaml`, plus `memory/lessons/`. — local: `memory/README.md`
- Siemens AEI (arXiv:2604.07784): in RL tuning, "an agent-built memory accumulated through successive training studies, in which the agent records parameter changes, observed reward and stability responses, inferred sensitivity patterns, and the reasoning associated with each intervention"; each study produces "a structured reasoning log that records the hyperparameters applied, the outcomes observed, the prior cases or heuristics consulted, and the recommendation that followed." — [arXiv:2604.07784](https://arxiv.org/abs/2604.07784)
- AEI also uses "a human-authored knowledge base that externalizes expert intuitions, diagnostic heuristics, and parameter-sensitivity rules that would otherwise remain implicit." — [arXiv:2604.07784](https://arxiv.org/abs/2604.07784)
- HERA (arXiv:2604.00901): experience entries (c, z, u) where c = query characteristics/type, z = natural-language insight, u = empirical success rate; updated via ADD (distinct), MERGE (similar/complementary), PRUNE (conflicting or low-utility), KEEP (unchanged); retrieval balances utility u and diversity. — [arXiv:2604.00901](https://arxiv.org/abs/2604.00901)
- Karniadakis (arXiv:2511.03179): tacit expert knowledge is "difficult to articulate or codify"; institutional memory is at risk during personnel transitions; the Systems Engineer reviews designs against requirements using its KG, providing qualitative + quantitative feedback. — [arXiv:2511.03179](https://arxiv.org/abs/2511.03179)
- AEI (arXiv:2604.07784): "historical engineering data are rarely used in a systematic way... similar failure modes are repeatedly encountered while valuable institutional knowledge remains implicit." — [arXiv:2604.07784](https://arxiv.org/abs/2604.07784)

### Inferences
- ThinkToCad's current attempt YAML is too thin (only mechanism/status/verification/timestamp); adding "reasoning consulted," "failure mode," "fix/rule," and a utility/success-rate field would make lessons retrievable and ranked, mirroring HERA's u and AEI's reasoning logs.
- Capturing both failed and successful attempts (already ThinkToCad policy) aligns with HERA's "insights from both successful and failed trajectories" and AEI's treatment of failed runs as informative states.

### Gaps
- No source here measures how much experiential memory improves design success in mechanical CAD specifically; the cited gains are on QA/benchmarks (HERA) and airfoil (Karniadakis).

## How do they handle knowledge versioning, trust levels, and provenance?

### Takeaway
Versioning/trust/provenance are handled mainly through traceability (workflow traces, requirement links, source references in chunks) and consolidation (merge/prune with utility scoring); ThinkToCad can adopt a "source + version + trust tier" header on every knowledge file and git-tracked history, but no cited system offers a complete provenance standard for small toolkits.

### Cited Findings
- Karniadakis (arXiv:2511.03179): KG chunks carry metadata (chunk ID, source reference, row range); KGs derived from 50 papers spanning 1940s-2010s, enabling traceability to source literature. — [arXiv:2511.03179](https://arxiv.org/abs/2511.03179)
- Siemens AEI (arXiv:2604.07784): MBSE use case emphasizes traceability — "requirements, models, simulation outputs, and workflow history" linked; agent generates "a traceability report in Teamcenter showing which requirements, parameters, and analyses are affected by the proposed change." — [arXiv:2604.07784](https://arxiv.org/abs/2604.07784)
- AEI (arXiv:2604.07784): "traceability across evolving engineering environments, where requirements, models, and implementation artifacts must remain connected over extended development cycles." — [arXiv:2604.07784](https://arxiv.org/abs/2604.07784)
- HERA (arXiv:2604.00901): utility score u measures empirical success rate; PRUNE removes conflicting or low-utility insights; consolidation provides a lightweight trust/quality gate. — [arXiv:2604.00901](https://arxiv.org/abs/2604.00901)
- Corpus2Skill (arXiv:2604.14572) limitation: "Compilation and corpus churn" — recompilation cost when corpus changes; implies versioning/rebuild concerns at scale. — [arXiv:2604.14572](https://arxiv.org/abs/2604.14572)
- ThinkToCad mechanisms already include a "Sources" field (e.g., `linkages.md`) and constraints cite workshop capability; graph edges include `sourced_from`. — local: `knowledge/mechanisms/four_bar_linkage.md`, `knowledge/graph.yaml`

### Inferences
- A pragmatic trust model for ThinkToCad: tier 1 = verified by tool (FreeCAD/MATLAB pass), tier 2 = from cited standard/textbook, tier 3 = heuristic/workshop note, tier 4 = LLM-inferred (unverified). Store as a `trust:` field in frontmatter.
- Git history already provides versioning for files; adding a `version:`/`last_verified:` date and `source:` URI to each markdown file gives provenance without a database.
- The `verified_by` edge type in graph.yaml already encodes provenance (which tool validated an entity) and should be populated consistently.

### Gaps
- No cited system defines a formal versioning/trust standard for small toolkits; AEI/HERA address traceability and utility but not document-level provenance schemas. This is largely an open design choice for ThinkToCad.

## What is "Corpus2Skill" (distilling knowledge into agent skills)?

### Takeaway
Corpus2Skill is a compile-then-navigate architecture that distills a bounded corpus into a hierarchical filesystem of "skills" (SKILL.md/INDEX.md files) which an LLM agent browses with progressive disclosure instead of running vector search; it is directly applicable to turning ThinkToCad's knowledge/ folder into a navigable skill tree.

### Cited Findings
- Corpus2Skill (arXiv:2604.14572): "an offline compiler distills the corpus into a hierarchical skill directory, and at serve time an LLM agent navigates it, drilling from a bird's-eye view through progressively finer summaries down to documents and backtracking when a branch is unproductive." — [arXiv:2604.14572](https://arxiv.org/abs/2604.14572)
- It "requires no embedding index or vector DB at serve time"; navigation files stay small (typically under 2 KB each); depth grows O(log_p N) (e.g., WixQA N=6221, p=10 -> 3 levels, ~30 summaries/query). — [arXiv:2604.14572](https://arxiv.org/abs/2604.14572)
- Progressive disclosure (Anthropic Skills API): metadata (name + one-line description, ~100 tokens) pre-loaded; full SKILL.md loaded on selection; resources stay on disk until accessed. — [arXiv:2604.14572](https://arxiv.org/abs/2604.14572)
- Shift from procedural to informational skills: prior skills encode "how to perform a task"; Corpus2Skill repurposes them to encode "what a corpus contains" (topical partitions). — [arXiv:2604.14572](https://arxiv.org/abs/2604.14572)
- Agent skills formalized as tuple S=(C, π, T, R): applicability condition, execution policy, termination condition, reusable interface (Jiang et al., 2026, cited in Corpus2Skill). — [arXiv:2604.14572](https://arxiv.org/abs/2604.14572)
- Two serve-time tools: code_execution (browse SKILL.md/INDEX.md via ls/cat/grep) and get_document(doc_id) (full text); plus entity_index.json for lateral jumps and "## Related skills" blocks from entity-Jaccard overlap. — [arXiv:2604.14572](https://arxiv.org/abs/2604.14572)
- Scope guideline: helps on single-domain corpora with recoverable topical taxonomy; flat retrieval preferable on open-domain factoid or homogeneous-tabular corpora. — [arXiv:2604.14572](https://arxiv.org/abs/2604.14572)

### Inferences
- ThinkToCad could compile its knowledge/ directory into a Corpus2Skill-style forest: top-level skills per category (mechanisms, constraints, lessons), INDEX.md rows per entity, get_document retrieving full markdown; this matches the existing OpenCode/Claude "skills" convention already present in the repo.
- ThinkToCad's existing SKILLS.md and skills/ folder suggest the codebase already leans toward skill-based packaging, making Corpus2Skill a natural fit rather than a new paradigm.

### Gaps
- Corpus2Skill's compile pipeline assumes a larger corpus (N=6221); for ThinkToCad's ~100 mechanisms, manual curation may beat automated clustering; no cited evidence for the crossover point.

## How do knowledge bases grow automatically from design outcomes?

### Takeaway
Automatic growth happens via experience libraries that consolidate trajectory insights (HERA ADD/MERGE/PRUNE/KEEP with utility scoring) and agent-built memory logs (AEI), plus ThinkToCad's stated policy of writing a lesson/attempt record after every design; the growth policy should be explicit about what gets added, merged, pruned, and never silently overwritten.

### Cited Findings
- HERA (arXiv:2604.00901): experience library updated online via ADD (insert distinct), MERGE (combine similar/complementary), PRUNE (remove conflicting/low-utility), KEEP (unchanged); each entry has utility u = empirical success rate. — [arXiv:2604.00901](https://arxiv.org/abs/2604.00901)
- HERA (arXiv:2604.00901): "improved reasoning behaviors from prompt evolution enhance the quality of stored experiences, which in turn reinforce subsequent reasoning" — a positive feedback loop between growth and quality. — [arXiv:2604.00901](https://arxiv.org/abs/2604.00901)
- Siemens AEI (arXiv:2604.07784): offline phase turns "design artifacts, simulation logs, workflow traces, and human feedback" into "reusable engineering memory, including retrieval stores, knowledge graphs, and relational workflow records." — [arXiv:2604.07784](https://arxiv.org/abs/2604.07784)
- AEI (arXiv:2604.07784): multimodal pipeline (text/table extraction, context-aware figure interpretation via VLM with surrounding narration, ASR transcripts aligned to slides) builds the memory store D from heterogeneous artifacts. — [arXiv:2604.07784](https://arxiv.org/abs/2604.07784)
- ThinkToCad `KNOWLEDGE_AGENT.md` (local): "After every design, save... mechanism, status, verification... Failed attempts are as valuable as successful ones"; memory/designs/<name>/attempt_N.yaml. — local: `KNOWLEDGE_AGENT.md`, `memory/README.md`
- ThinkToCad `KNOWLEDGE_AGENT.md`: runtime loop Spec -> Build -> Validate -> Learn -> Improve -> Repeat; memory.save(contract, result, verification). — local: `KNOWLEDGE_AGENT.md`
- Corpus2Skill (arXiv:2604.14572) limitation: "Compilation and corpus churn" — recompilation needed when corpus changes; automatic incremental growth is not solved by static compile-then-navigate. — [arXiv:2604.14572](https://arxiv.org/abs/2604.14572)

### Inferences
- ThinkToCad's "knowledge grows with each design" policy should be operationalized as: (1) after each validated design, append an attempt YAML; (2) on failure, append a lesson markdown with root cause + rule; (3) periodically consolidate lessons (MERGE duplicates, PRUNE contradicted rules) using a utility count; (4) recompile the skill tree only when the corpus changes materially.
- Treating failed runs as first-class memory (already ThinkToCad policy) is the single most evidence-backed growth practice across cited systems.

### Gaps
- No cited system demonstrates automatic growth improving mechanical design outcomes end-to-end; growth policies are evaluated on QA/retrieval, not CAD.

## Frameworks for knowledge-guided multi-agent design (Karniadakis, Siemens AEI)

### Takeaway
Both Karniadakis and Siemens AEI converge on the same anatomy — structured knowledge base + specialized agents + toolchain feedback loop + memory + human oversight — but differ in emphasis: Karniadakis uses role-specific knowledge graphs with a Generator-Critic loop for conceptual design; AEI frames engineering as constrained, history-aware sequential decision processes with offline memory construction and online workflow-state estimation/control.

### Cited Findings
- Karniadakis (arXiv:2511.03179): three agents — Graph Ontologist, Design Engineer, Systems Engineer; Design Engineer samples/optimizes NACA airfoils using the design KG + tools (AeroSandbox, NeuralFoil); Systems Engineer generates requirements and reviews designs (incl. multimodal vision) using its own KG; iterative feedback until Manager validates; then optimize. — [arXiv:2511.03179](https://arxiv.org/abs/2511.03179)
- Karniadakis (arXiv:2511.03179): "The kernel is the referee" spirit — tools (AeroSandbox/NeuralFoil) judge performance; KGs provide transparency/explainability. — [arXiv:2511.03179](https://arxiv.org/abs/2511.03179)
- Siemens AEI (arXiv:2604.07784): workflow modeled as W=(S,O,A,Z,C,T,U); memory z_t = M(q_t, H_t, D); workflow-energy heuristic E_t(a)=α Ĝ_t(a)+β V̂_t(a)+γ Ĉ_t(a) ranks interventions; "agents act as workflow controllers, toolchains provide feedback." — [arXiv:2604.07784](https://arxiv.org/abs/2604.07784)
- AEI (arXiv:2604.07784): offline phase builds DD from artifacts/logs/traces/feedback into retrieval stores, KGs, relational workflow records; online phase estimates workflow state, retrieves prior experience, reasons over constraints/trade-offs, selects interventions; recommendation-centered (human retains authority). — [arXiv:2604.07784](https://arxiv.org/abs/2604.07784)
- AEI (arXiv:2604.07784): Sense-Reason-Act over MBSE toolchains (Teamcenter/Amesim) with traceability reports; suspension design and RL tuning use cases. — [arXiv:2604.07784](https://arxiv.org/abs/2604.07784)
- ThinkToCad `KNOWLEDGE_AGENT.md` maps to the same anatomy: Knowledge Base (3 types), Agent (retrieve/plan/execute/evaluate/learn), Tools (build123d/freecad/matlab/git), Feedback Loop (kernel is referee), Memory (per-design attempts + lessons). — local: `KNOWLEDGE_AGENT.md`

### Inferences
- ThinkToCad already implements the consensus anatomy; the main gaps vs. these frameworks are (a) role-specific knowledge slices (Karniadakis), (b) workflow-state/energy ranking of interventions (AEI), (c) multimodal memory construction (AEI), and (d) experience-library consolidation with utility scoring (HERA).
- AEI's recommendation-centered (human-in-the-loop) operating mode matches ThinkToCad's single-engineer reality better than fully autonomous control.

### Gaps
- Neither Karniadakis nor AEI reports quantitative validity gains on mechanical CAD; Karniadakis is airfoil-only, AEI is automotive/vision; transfer to small agricultural machinery is unvalidated.