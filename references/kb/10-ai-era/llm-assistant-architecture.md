---
id: llm-assistant-architecture
title: A reference architecture for an LLM assistant - from sources to answer
type: method
source: "Course \"BI+AI strategy 26\", Day 7"
confidence: verifiable
blocks: [5]
---

Five layers, seven runtime steps and five cross-cutting loops. The diagram's colour logic: **blue is the guaranteed path** (the query is assembled from ready definitions) · **orange is the path with no guarantee** (the model writes the SQL) · red is access and risk · green is feedback.

## 1. Sources

Product databases (the facts of the business: orders, payments, statuses) · clickstream (events and sessions) · external systems (partner and service data) · reference data and MDM (single lists: customers, products, categories) · **the analysts' query logs - the raw material for column descriptions and reference pairs**.

That last source is usually forgotten and is the cheapest: the history of real queries already contains both the typical joins and the working definitions.

## 2. The warehouse

**The core layer** - single entities, keys, history; all the meaning described to its right rests on it · **the marts** - pre-computed aggregates for the domains · **contracts and data quality checkers** - they watch data quality (an important caveat: *answer quality is not what they watch*) · **roles in the warehouse** - the lower bound of access: what the agent cannot get around even if it picks the wrong layer.

## 3. The meaning layer - it stores no data, it describes what the data means

| Component | Purpose | What it gives |
|---|---|---|
| **The metadata catalog** | know what exists and what can be believed | the owner, freshness, certification status |
| **The business glossary** | one concept instead of ten synonyms | translating the user's words into the company's terms |
| **The ontology and relation graph** | stop guessing at links between entities | single IDs and **permitted join paths** |
| **The semantic layer** | compute a metric the same way always and everywhere | measures, dimensions, grain, aggregation rules and **access policies in code, not in the prompt** |
| **Reference queries and descriptions** | close the tail that has not been modelled | "question -> SQL" examples and column descriptions |

Plus two things: **cache and pre-aggregates**, so the answer comes back fast, and **versions and tests over the definitions**, so a metric cannot be changed unnoticed.

## 4. The assistant's runtime - seven steps from question to number

1. **The question and who asked it** - the roles and the domain arrive with the question, not afterwards
2. **Understand the question** - words into concepts, concepts into specific objects and paths
3. **Clarify** - if there are two readings, put the question back to the user
4. **Choose the route** - is the question covered by the semantic layer or not
5. **5a. Assemble the query (text-to-semantics)** - a compiler builds SQL from measures and dimensions, **the model does not write it**; **5b. Generate (text-to-SQL)** - the model writes the SQL, but with context from the meaning layer, retrying on error up to 3 times
6. **Apply entitlements inside the query** - the row filter is baked into the SQL rather than applied afterwards
7. **Execute and answer** - the number, a trust marker and provenance: which measure, which query, as of what date. **"I can't" is a valid answer**

Steps 5a and 5b are the heart of the construction: the zone covered by semantics comes with a guarantee, the uncovered zone is best effort, and the user has to see the difference.

## 5. Consumers

The business asks a question in words in a chat and **cannot check it** · the analyst speeds up their own work and finishes the answer by hand · dashboards read **the same definitions** the assistant does · external agents get the same layer through one interface.

## The cross-cutting loops - without which the construction does not survive a quarter

| Loop | Purpose | What it gives |
|---|---|---|
| **A. Offline validation** | do not let a regression into production | a score on the golden set before release, a stop signal for the rollout, the share of confidently wrong answers |
| **B. Online validation** | see what is happening in production | a trace of every answer from question to number, quality drift, cost, anomalies in result-set size |
| **C. Human error review** | turn failures into material for teaching the system | new cases into the golden set and confirmed reference queries |
| **D. Coverage management** | expand the guaranteed zone **by demand, not by the team's intuition** | a modelling queue drawn from the most frequent best-effort questions |
| **E. Access and security** | stop the assistant becoming a leak channel | minimal entitlements, query audit, review of changes to definitions |

Loop D is the most underrated: it turns the gap between "covered by semantics" and "actually asked about" into a managed work queue.

## Terms

- **Golden set** - a fixed list of questions with the right answers known in advance; the system is measured on it before rollout
- **Eval** - a run of the system over such a set with metrics computed; offline eval before release, online eval on live traffic
- **Loop** - a process closed on itself: the result of the work returns to the input and changes the system's behaviour
- **Best effort** - an answer mode with no guarantee; the opposite of a governed answer from a verified definition
- **Grain** - what one row means: a deal, a day per category, a stock snapshot; it determines what may be summed
- **Provenance** - the chain of an answer's origin: which metric, which query, as of what date

Links: [[ai-triad-prerequisites]] · [[plausible-but-wrong]] · [[context-governance]] · [[domain-knowledge-base]] · [[core-layer-project]]
