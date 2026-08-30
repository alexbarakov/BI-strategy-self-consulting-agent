---
id: context-governance
title: Context governance - the context unit, the trust plane, the gate roles
type: method
source: "Course \"BI+AI strategy 26\", Day 7 - internal practice"
confidence: verifiable (internal measurements)
origin: "an internal case walked through on the course; the numeric thresholds are anonymized - calibrate from your own baseline"
blocks: [5, 6]
---

The level after populating the domain knowledge base: **the agent physically cannot write SQL without context** - not by agreement but by infrastructure.

## The atom - the context unit

Statuses: **inferred -> candidate -> verified -> deprecated**. Each unit carries provenance, a freshness TTL and **a reference to the source of truth instead of a copy**.

## The trust plane

Three serving modes, determined by the unit's status, its freshness and the query's risk:
- **SERVE_AS_FACT** - hand it over as fact
- **SERVE_WITH_CAVEAT** - hand it over with a caveat
- **WITHHOLD** - do not hand it over

The risk rule, stated explicitly: **a number going onto a board is high risk**. That is, the same context can be sufficient for an exploratory question and insufficient for publication in a report.

## The PreToolUse hook - turning practice into infrastructure

The agent physically cannot call a SQL-writing tool without going through context. The effect, as phrased: **adoption moves from "the agent decided to" into "the infrastructure"**. It is the same principle as "an access matrix with no implementation mechanism is a declaration" ([[access-matrix]]).

## Three principles

1. **The single source of truth is referenced, not duplicated** - a copy goes stale silently
2. **Extraction does not trust itself** - extracted knowledge does not become fact automatically
3. **Population is not trust is not effect** - three different quantities that cannot be measured with one metric

The third principle is the most practical: it explains why in [[domain-knowledge-base]] completeness, the `confirmed` status and the bot's accuracy are counted separately.

## The measured effect on simple queries

Context delivered under governance instead of "everything into the prompt" produced, in the case walked through, a multiple improvement on simple queries along three axes at once: **the volume of tokens supplied fell roughly threefold · the number of agent steps threefold · the response time by an order of magnitude** (from minutes to seconds).

What matters here is not the absolute value but the fact that it is not only cost that wins but latency and step count too: governed context improves the economics and the quality at the same time. Your own values are measured on your own set of typical queries.

## Context governance: who holds the gate

| Role | What they hold |
|---|---|
| **BI partner** | the domain's verify gate with **an explicit weekly time budget** (in the case walked through, under an hour a week); if the queue eats more, the platform is what gets fixed |
| **Metrics curator** | the domain's semantics |
| **GenAI champion** | the owner of the AI direction in the domain |

**The gate's load is a platform health metric.** This is the most elegant construction in the block: the gate is not merely assigned, it has a time budget, and going over that budget is not the person's problem but a signal to the platform. Without such a rule the verify gate quietly turns into a bottleneck and stops working.

The three roles in that table are the same ones the Roles criterion in [[ai-ready-domain-score]] requires.

## Types of context

A separate course exercise: **analyse the available context types and sources, remove what is redundant, and adapt the target context map to yourself**. The layers the reference model distinguishes: LLM model context · business context · domain context · data context · user context - with a context engine above them, and metadata blended in layer by layer.

Links: [[domain-knowledge-base]] · [[llm-assistant-architecture]] · [[ai-ready-domain-score]] · [[plausible-but-wrong]]
