---
id: ai-triad-prerequisites
title: The triad of prerequisites for AI analytics, and the order to build it in
type: method
source: "Course \"BI+AI strategy 26\", Day 7"
confidence: verifiable
blocks: [5]
---

Three layers without which the agent guesses.

| Layer | What it is |
|---|---|
| **The semantic layer** | the layer of metrics and cuts - a single place of computation, consistency, *meaning lives in code* |
| **The trusted core layer** | certified marts plus a logical and conceptual data model ([[core-layer-project]]) |
| **The domain knowledge base** | the context on top: few-shots, traps, glossary, metric tree ([[domain-knowledge-base]]) |

**Without the triad:** rework, loss of metric consistency, [[plausible-but-wrong]].
**With it:** 85-95% accuracy and an honest refusal.

## The build order follows the most expensive pain, not "everything at once"

The triad is **not built in parallel**. You start with the layer that closes the domain's most expensive pain.

| What hurts | Where to start | Why |
|---|---|---|
| **Metric consistency** - "everyone has their own number" | **the semantic layer** | a single definition removes most of the discrepancies and the arguments about numbers |
| **Finding data and joining it** - analysts drown in marts and join by hand | **the core layer** | fewer marts, a clearer model, fewer join mistakes |
| **"The agent does not understand the domain"** - the data is there but the agent muddles the terms | **the domain knowledge base** | few-shots and a glossary give the fastest accuracy gain |

**The general rule: one layer at a time, with an eval before and after**, so you can see the real gain. Trying to build all three at once is a reliable way to finish none.

This same rule directly operationalizes the `no-assistant-without-foundation` kill-gate: the course assignment requires naming **who the gate is and at which kill threshold the initiative stops**.

## The exercise

Design the triad for one domain: what goes into the semantic layer (metrics, cuts) · what into the trusted core (marts, model) · what into the domain knowledge base (few-shots, traps, glossary) · who the gate is and at which kill threshold.

Links: [[core-layer-project]] · [[domain-knowledge-base]] · [[llm-assistant-architecture]] · [[ai-ready-domain-score]] · [[plausible-but-wrong]]
