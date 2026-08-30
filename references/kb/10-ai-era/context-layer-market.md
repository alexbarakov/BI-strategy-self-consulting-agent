---
id: context-layer-market
title: The context layer (the LLM wiki) - the market, the architecture, what is proven
type: evidence
source: "Course \"BI+AI strategy 26\", Day 8; expanded in references/evidence-2026.md §5"
confidence: mixed - separated by the type of evidence
blocks: [5]
---

## Data governance is not context governance

They govern different objects:
- **Data governance** - the data itself: quality, access, provenance, compliance
- **Context governance** - the meaning layer: definitions, domain knowledge, metadata, situational context. **What the agent reads in order to reason**

> **Clean data is not trusted data.** Correct numbers are not enough for an agent - it needs signals about freshness, ownership and changes to definitions, or it will be confidently wrong.

The 2026 market shift: the data catalog becomes the context platform.

## Why the catalog stopped coping

An agent is not a person: it will not ask a colleague, will not infer from context, and will not notice that a metric's definition changed six months ago.

- **The knowledge lives in people's heads** - naming rules, the standard filters, the known quirks of particular marts do not arrive through a database connection
- **More context is not better** - context rot: quality degrades as input grows; a model with a 200K window loses noticeable accuracy already at 50K tokens
- **Naive RAG does not save you** - dumping documents into a vector store is not governance

## Three different things that get constantly confused

| | Which question it answers | Consumer |
|---|---|---|
| **The data catalog** | "what do we have" - a list of objects and schemas, owners, tags, certification, lineage | **the human doing the searching** |
| **The semantic layer** | "how is this correctly computed" - metric and dimension definitions, a single place of computation, deterministic SQL generation | **the query engine** |
| **The context layer (the LLM wiki)** | "what does this mean and what should be believed" - plus unstructured knowledge (docs, threads, decisions), traps and "question -> SQL" examples, a plane of trust and freshness | **the agent, via MCP** |

**The context layer does not replace the first two; it is built on top of them.** Remove any one and the agent starts guessing.

## The reference architecture - five layers plus a loop

1. **Sources** - the warehouse (schemas, marts) · query logs and BI usage · documents · threads, tickets, decisions · code (dbt, SQL, pipelines)
2. **Collection** - connectors · lineage extraction down to the column · **mining the query history** · document parsing · event-driven synchronization
3. **Assembling knowledge** - entity resolution · **generating descriptions plus a human gate** · the glossary and metric definitions · "question -> SQL" pairs, traps · eval cases (the golden set)
4. **Storage** - the metadata graph and the semantic layer · chunk vectors with ACLs · status inferred to verified · freshness TTL, provenance, a single source of truth
5. **Serving** - **an MCP server: pull, not push** · the same policy engine humans get · **an ACL filter BEFORE the search** · returning only the relevant chunks · audit: who read what

**The feedback loop:** the agent writes back what it could not find and what contradicts, and raises quality flags · usage sets the priority for descriptions · eval catches a regression after a definition changes · **a failed test removes the verified status**.

*Not covered by any standard: the end-to-end chain of "prompt -> which chunks were retrieved -> which answer was given".*

## The passport of a knowledge atom

The mandatory fields on a node: **provenance** (where the fact was obtained) · **status** (inferred -> candidate -> verified -> deprecated) · **ssot_ref** (a reference to the source of truth - the formula is NOT copied) · **freshness** (created / verified / ttl; state fresh · aging · stale) · **source_object** (the source object plus its certification and health score) · **owner · eval · usage**.

Four root problems of a "raw" knowledge base that this closes: where the fact came from · whether it was checked by a human or inferred by a model · whether it has gone stale · whether it is a copy of a definition that has since diverged from the original.

**Trust is inherited:** if a mart loses its certificate, knowledge about it automatically drops to candidate.

## Three protocols, and what none of them solves

- **MCP** - how an agent requests context. Every player supports it. *"MCP carries context but does not produce it."* The risk: tool poisoning.
- **A2A** - how agents negotiate with each other; relevant once you have several agent systems, at an early stage.
- **OSI -> Apache Ossie** - a YAML format for exchanging metric definitions, "USB-C for semantics" rather than a new semantic layer; converters into dbt MetricFlow.

**What none of them covers:**
1. **Portability of entitlements.** Row-level security configured in one catalog does not apply when the same table is read through another. There is no industry format for exchanging policies - which is why in practice people pick **ONE catalog as the governance boundary**.
2. **The provenance of an answer.** The chain "prompt -> retrieved chunks -> answer" is not part of any standard.

## What is proven and what is narrative

**Independently proven:** quality degrades as input grows (checked across 18 models, declining at every step long before the window fills) · the decline is continuous rather than a cliff - the "cliff" claim comes from a different paper, where the threshold is **a share of the window (40-50%)**, not an absolute 51-64K tokens · model-written descriptions are wrong three times more often than human ones (19.6% versus 6.3% - *the cited source did not survive verification; do not quote this figure until it is checked against the full text*).

**Vendor-measured:** "38% better SQL accuracy" · "around 90% agent accuracy" · "87% of descriptions no worse than a human's" - the methodologies are not published, and independent checking finds three times as many errors.

**Marketing:** the "82% / 87% / 91%" surveys were commissioned by the people selling the platform and are internally contradictory (88% "the platform already exists" alongside 87% "the data is not ready") · "catalog becomes context platform" is a new name for the same metadata graph · "AI-native governance" is, in practice, auto-tags and auto-descriptions with the same error rate.

> **The practical conclusion: buy the architecture - where the context sits, whose entitlements apply, whether you can take the data out - not the claimed percentages.** Check any claimed figure on your own set of reference questions, or you are buying somebody else's measurement.

## The cost trap

Open-source solutions have a zero licence but cost **0.25-1 FTE of a platform engineer** for upgrades, fixing connectors and handling requests. For commercial ones the price is driven not by seat count but by **the number of connected sources**.

## How to assemble your own LLM wiki without buying a platform

The order matters more than the tool - each step only makes sense after the one before:

1. **Choose the governance boundary** - one catalog as the source of entitlements; every engine and agent goes through it
2. **Collect atoms, not documents** - each node with a passport
3. **Mine, do not write** - context is extracted from the query history and the dashboards; hand-written description only for the pilot domain
4. **A narrow human gate** - inferred becomes verified only through a human; **the metric is the share accepted without edits, not coverage**
5. **Serve over MCP with the filter** applied before the search, not after
6. **Close the loop** - a golden set, a regression when a definition changes, write-back from the agent

**The metrics:** the share of knowledge in verified status · the median age of a node · the share of agent answers carrying provenance · accuracy on the golden set before and after context is supplied · the share of descriptions accepted without edits.

**The anti-patterns:** dumping documents into a vector store and calling it a knowledge base · generating descriptions for everything and publishing them unchecked · giving the agent its own separate entitlement perimeter "so it does not get in the way".

## The operating model and the kill-gate

**The curator does not write context - they judge the machine's draft** (a gate, not authoring).

The target thresholds: domain bot accuracy 25% -> 80% · verified share at least 70% · false-accept rate under 5%.

The rules: **an atom's definition of done** - an empty field means not verified and not served · **verify is tied to eval** - you cannot mark as verified something that lowers accuracy · **deprecation is automated** - "nobody removed it" is impossible, a timeout removes it · **population is not trust is not effect** - three different metrics.

> **The kill-gate: if the accuracy gain from context is not significant, STOP.** Useless context knocks down trust in the whole AI agenda (governance theatre).

Links: [[context-governance]] · [[domain-knowledge-base]] · [[semantic-layer-evidence]] · [[data-catalog-pitfalls]] · [[plausible-but-wrong]]
