# The course's concept library (the primer for recommendations)

A generic distillation of the frameworks from the "Building a BI+AI strategy" course - so that the recommendations in each block are competent when run for any participant, without relying on a specific company's data. **The numbers here are industry-wide or teaching reference points, not a company's targets**; the participant sets their own targets (the roadmap carries `<•>` placeholders).

## The cross-cutting frame
- **"AI generates the draft, a human checks it."** There is no deterministic answer in analytics and no automatic verification, so a human gate is required.
- **The dual strategy:** "old BI" (well-understood practices: core, certification, health score) plus "new BI" (experiments: semantic-first, agents) under kill-gates. The answer to AI FOMO.
- **A strategy is a chain of dependencies, not a list of features.** An AI feature cannot be placed ahead of its link.

## Day 1 - trends and sobriety
- **Traditional to agentic BI:** conversational AI as the main interface for ad-hoc and self-service; dashboards become niche monitoring. **Headless BI** = 3 layers (data products + semantic layer + AI interface).
- **The AI bubble:** roughly 95% of pilots do not scale; GenAI is a seniority-biased change (junior hiring falls). Cargo cult versus aircraft that actually fly.
- **The middle-ground scenario (as a frame):** the effect so far is small; core, semantics, governance and agents are growing; seniors vibe-code better; the effect shows up in new tasks (100% instead of a sample); the main walls are the review bottleneck and insufficient context.

## Day 2 - demand and consumers
- **The agent is a new class of consumer**; it needs machine-readable semantics (keys, valid ranges, freshness, owner), not "go ask Masha".
- **Four types of ad-hoc uncertainty:** phrasing / finding the object / trust / interpretation - each automatable to a different degree.
- **Data versus hype:** users ask for search and trust to be fixed far more often than for conversational AI to be added.

## Day 3 - assessment plus AI readiness
- **Two maturity axes:** classical BI maturity by AI readiness.
- **The AI-ready domain score** (generically): roles plus the health of metrics, marts and dashboards plus the completeness of the domain knowledge base plus the readiness of processes for "AI generates, a human checks"; zones green / yellow / red / critical.
- **Maturity by company size:** small and non-tech companies should not build their own GenAI infrastructure - grow core BI plus one pilot; leaders split resource across governance, R&D and infrastructure.

## Day 4 - BI channels
- **The triangle of centralized, self-service and agentic.** AI cannibalizes manual ad-hoc work and one-off dashboards, not certified reporting.
- **Four agentic stages:** interoperability -> composability -> managed autonomy -> multi-agent. The anti-pattern: "an agent is a chatbot with no tools".
- **The Jevons paradox:** cheaper content means more chaos. The defence: reuse by default, and an AI-produced object treated as a temporary draft with automatic archiving.

## Day 5 - data management
- **The core layer is AI's healthy diet:** certified marts (ownership, SLA, data quality, metadata), reuse instead of "one more mart".
- **The dependency chain:** core -> metric certification (semantics) -> domain context -> AI accuracy -> self-service.
- **AI in data management already:** generating quality checks and descriptions; compute over 100% rather than a sample; the new bottleneck is the flow of incidents (an incident/eval agent is needed).

## Day 6 - content management
- **AI slop:** content multiplies faster than it can be reviewed; certification and archiving become defensive infrastructure.
- **The health score:** penalties (no owner, unused, abandoned, duplicates) times multipliers (high weekly active users, used by executives); this is a trust signal for the agent too.
- **Bot-driven critique, a feedback bot, and the data visualization caveat** (only go deep if the dashboard is operational AND long-lived; 95% of the time it is big numbers, bars and tables), with target audience as a content field.

## Day 7 (the AI foundation) - semantics, core, context
- **The triad of prerequisites:** the semantic layer plus a trusted core plus the domain knowledge base (few-shots). Without it, text-to-SQL guesses.
- **Reference figures (with provenance; details in `evidence-2026.md`):** on the corporate schemas of Spider 2.0, GPT-4o scores 10.1% against 86.6% on the academic Spider 1.0, and the paper's headline comparison is o1-preview at 21.3% against 91.2%. The uplift from a semantic layer (up to 90-98%) is claimed by a vendor benchmark on its own question set - there is no direct public comparison against Spider 2.0. Independently: context from a knowledge graph raised a model from 16% to 54%.
- **A taxonomy of text-to-SQL failures:** entity resolution ("which ones exactly"); joins and fan-out; missing filters; time granularity and time zones; window logic and dead code. Cured by semantics, known joins, few-shots and a judge gate.
- **Context rot:** quality degrades as the supplied text grows, long before the window fills; the decline is continuous rather than a cliff, and the paper that reports a cliff puts its threshold at a share of the window (40-50%), not an absolute token count. The consequence: serve on request rather than pile it in ahead of time, and cut off the similar-but-not-right.
- **Context as a layer:** "MCP is the plumbing, not the meaning." What does not work: catalogs as shelves, ontologies (an SME bottleneck), auto-documentation at ~75% (it poisons). What works: mining the query history plus a narrow human gate plus verified "question -> SQL" pairs.
- **The context management system:** the context unit (inferred -> candidate -> verified -> deprecated, provenance, freshness TTL, a reference to the single source of truth); the trust plane SERVE_AS_FACT / WITH_CAVEAT / WITHHOLD; a PreToolUse hook so the agent cannot write SQL without context.

## Day 5+ - data management in the AI era (new)
- **The catalog became a control point** rather than a search shop window: it hands engines their keys and holds the entitlements. The common protocol does not standardize entitlements or lineage - policies do not transfer between catalogs. The practice: one catalog as the governance boundary.
- **The agent is a new identity:** private access plus untrusted input plus an outbound channel is exploitable. It needs its own identity, narrow keys, a tool allowlist and behavioural monitoring.
- **The unit of governance is a chunk of a document:** entitlements from the database do not travel into the vectors, and they have to be checked before the search, not after.
- **Deletion is broken:** a soft delete in vector databases leaves the vector physically recoverable. Asking the vendor about this is mandatory.
- **Contracts:** the specification won, the enforcement did not. Start with a CI gate on the critical marts, not with a "let us roll out contracts" project.
- **The economics:** the bill grows from unused objects and from policy, not from the volume of analytics.

## Day 6+ - certification along two dimensions (new)
- **The object passport** (owner, health, description, usage) scales across all content but is blind to substantive errors.
- **Behavioural tests** (before-and-after comparison at release, reconciliation against the source, performance) catch regressions but are expensive per object.
- The working combination: passports everywhere, tests on the critical core. For AI answers it is the same pair - the health score as a source filter and a reference set as the test.

## Day 4+ - the data app as a fourth channel (new)
- **Three formats:** the dashboard (monitoring) -> the data app (input, a scenario, an action) -> the notebook (a one-off investigation).
- **Three approaches to building them:** reactive notebooks, code-first frameworks, warehouse-native. That is a different dimension - each covers several formats.
- **The watershed:** does the artifact write back, and who applies the entitlements. A notebook without reactivity is a draft: of 1.45 million notebooks on GitHub, 24% ran without errors and 4% reproduced their result.
- A data app needs the same attributes a dashboard does: an owner, certification, a health score.

## Day 8 - agent architecture
- **The layers:** MCP servers -> the orchestrator plus atomic skills -> a judge gate and guardrails (RELATIVE-ONLY: direction, not absolutes) -> eval infrastructure (a golden set, a judge runner).
- **The mathematics of accuracy:** 7 steps at 90% each gives under 50% at the output. Fewer steps, more determinism, a judge at the end.
- **Legacy BI:** an AI strategy for an old tool starts with the architecture (breaking up the monolith), not with a chat box. Build versus buy: a thin layer of your own over a commodity.

## Day 9 - the team and the profession
- **The shift in a BI developer's work:** dashboards, warehouse work and ad-hoc fall; core, semantics, the domain knowledge base and agent development rise. Factory teams compress and the junior-to-middle tier thins out; a "human intermediary" is needed.
- **The business data engineer / analytics engineer** - a role per business unit (metadata, quality, core). **Vibe coding** is mandatory tooling (the optimum is around 30-50% AI-written code; seniors do it better; review is the bottleneck).
- **The playbook setup-to-evaluate:** in the first half, the environment for everyone with no quotas; in the second, adoption in review and grades. The AI accelerator drives it from the bottom.

## Day 10 - metrics and kill-gates
- **Metrics for the AI streams:** auto-response rate, accuracy on the golden set, hallucination rate, extra FTE capacity, cost per successful task.
- **Honest eval:** "a metric is only as good as its judge is strict"; population is not trust is not effect (read coverage and false-accept together).
- **The kill-gate:** a metric, a threshold and a STOP for every initiative. **The economics:** net = saved hours times rate minus (tokens plus subscriptions plus people); without subtracting the denominator, everything pays back.

## Day 11 - the action plan and the vision
- **The stack rank:** governance -> trusted data -> AI readiness -> BI content -> self-service (cut right to left).
- **The risk register:** the fragile chain of AI to semantic layer to core to catalog; agents multiply chaos; governance with no resource.
- **The closing thesis:** the meaning is in the present; build an AI-ready architecture and keep watching.

## Where AI works in data processes (the map; details and references in `evidence-2026.md`)
- **Works:** classifying sensitive data, entity matching, schema matching, parsing complex tables.
- **Works only under verification:** SQL translation between dialects, descriptions and metadata, pipeline code.
- **Overrated or unproven:** a verdict on an incident's cause, generating quality rules, cleansing and synthesizing tabular data.
- **The regularity:** the closer the task is to "make sense of meaning" the better; the closer to "give a guarantee" the worse. Everywhere, routing wins over replacement.

## Expert reinforcements (for the recommendations)
- **Reversibility of bets:** reversible ones - make them boldly; irreversible ones (headcount, abandoning the core, publishing AI answers) - through a kill-gate.
- **A provenance footer:** the source plus freshness plus the owner in every answer - a cheap defence against silent failures.
- **Observability as P0:** without tracing and success labelling you cannot prove an effect or gate an eval.
- **"Ready by score is not answering correctly":** the AI-ready score measures completeness, not production accuracy -> an eval gate before announcing a domain.
- **ADKAR for AI:** the typical failure is doing knowledge and ability while skipping awareness and desire.
- **AI is an amplifier, not an accelerator:** it gives a mature pipeline speed and chaos more chaos. Introducing AI raises both delivery speed and instability; the bottleneck moves into review.
- **The perception gap:** self-assessed speed-up and measured speed-up can point in opposite directions - measure the effect only on a reference set.
