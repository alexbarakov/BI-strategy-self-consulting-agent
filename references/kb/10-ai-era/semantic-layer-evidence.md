---
id: semantic-layer-evidence
title: The semantic layer - three readings, paired accuracy measurements, the shift to text-to-semantic
type: evidence
source: "Course \"BI+AI strategy 26\", Day 8"
confidence: mixed - the source is stated for each figure
blocks: [5]
---

## Three readings of the term that get constantly confused

1. **LookML** - metrics inside the BI tool, serving dashboards. The oldest reading.
2. **dbt metrics** - definitions in the transformation layer, in git: MetricFlow, YAML, reviewed in a PR.
3. **Cube, AtScale** - a separate layer with its own runtime, standalone platforms.

> More often than not, "the semantic layer" is just a slide in the strategy that gets drawn and pushed to next year.

The damage from not having a layer was acceptable - **until the new wave of AI investment**. The segment has now split in two:

- **The semantic editor** - creating and managing metrics, dimensions and filters; SQL comes out the other end. It answers **what we compute**.
- **The semantic runtime and engine** - how to execute a query: the plan, entitlements, materialization, cache, cost. It answers **how we execute**. **This part is new.**

## Three ways to get a metric, and what each costs

| Way | Upside | Downside |
|---|---|---|
| **SQL against marts** | simple at first glance | easily turns into hard-to-read code; needs advanced skills (CTEs, window functions, CASE); mostly ad-hoc - a new question means new SQL |
| **The BI tool's UI or its language** (LookML) | simple, intuitive configuration, used in most BI tools, wide capabilities | **low reuse, vendor lock-in** |
| **A semantic layer** | a layer between the database and the business; business logic centralized declaratively in one place; the analytical back end separated from the consumers; advanced modelling patterns (dimensions, segments, joins, drill-downs); **accessible by API from BI, notebooks, REST and embedded** | requires a separate discipline of maintenance |

## What semantics does to accuracy - paired measurements

The method: one model, one set of questions, **only the presence of business semantics changes**.

| Scenario | Without semantics | With semantics |
|---|---|---|
| A corporate schema, 199 tables | 16.7% | **54.2%** |
| The same schema, hard questions | **0%** (not one is solved on the raw schema) | 38.7% |
| Pharma data, 60 queries | 8.3% | **78.3%** |
| A real warehouse, 2,730+ columns (column descriptions mined from query logs) | 36% | **52%** |
| A 2026-generation model: SQL generation versus the layer | 84.1% | **100%** |

Three conclusions from the table:

1. **The dirtier the schema, the bigger the effect.** On a teaching dataset the difference is a couple of points; on a corporate schema it is tens.
2. **The model barely matters.** Reasoning effort does not change accuracy once the layer is there. **The money is in context.**
3. **The errors differ in kind.** On an uncovered question the layer answers "I can't". SQL generation answers with **a confidently wrong number, silently**.

*A caveat from the source: some of the figures were published by vendors on their own question sets - read them as a direction, not as a promise about your accuracy.*

The anchor figures: **~40% text-to-SQL accuracy on real enterprise schemas** · **36% versus 86%** for one model on Spider 2.0 against an academic benchmark · **85-95% with a semantic layer**, and "failing honestly" instead of lying. A fresh signal is the dbt semantic layer 2026 benchmarks: near 100% on covered queries. **The layer only covers what has been modelled** - that is a limitation, not a caveat.

## Text-to-SQL is becoming text-to-semantic

The complexity has moved out of **defining** metrics and into **executing** them.

| The agent writes SQL every time | The agent asks the runtime for a metric |
|---|---|
| the model works out afresh where the data lives, how to join it, what the grain is, which formula to apply | "Give me Revenue by Country" - and that is all |
| every query is a new attempt to guess: worse accuracy, higher cost, no reproducibility | the runtime already knows where the data is, which joins, what grain, which formula and who may see what; **the same answer to the same question** |

The complexity has moved into two places:
- **The runtime** - turns a business request into an execution plan. Security, governance and row-level security move here too: **entitlements are applied while the query is assembled, not as a filter afterwards**. The agent physically cannot assemble a query against somebody else's data.
- **The execution engine** - what to materialize and what to compute on the fly; when to create a new aggregate and when to drop an old one. Materializing everything is not an option; materializing nothing makes for an expensive runtime.

*A vendor position, to be checked on your own schema. But the direction is confirmed by the independent paired measurements above.*

## Who the semantic layer is sold to now

1. **BI has stopped being the market** - the layer used to be built for BI tools; now the competitor is the cloud warehouses.
2. **The consumer is an agent.** Agents consume the layer directly: product, marketing, experimentation - with no human in the middle. **Not an insight for a human but a metric for an agent.**
3. **The interfaces have not settled** - it is unknown what wins: MCP, CLIs, desktop clients, skill hubs, portals, chats in messengers.

An assessment of the Russian market: solutions at this level appear not to exist; those that do are oriented at the old way of working with BI.

## An architectural reference

Airbnb's Minerva - **programmable denormalization over a normalized core**. A useful example of how the meaning layer relates to the physical model.

Links: [[ai-triad-prerequisites]] · [[unified-bi-platform]] · [[llm-assistant-architecture]] · [[glossary-vs-dictionary]]
