---
id: ai-adoption-waves
title: The four waves of the AI revolution inside the data function
type: pattern
source: "Course \"BI+AI strategy 26\", Day 7"
confidence: verifiable (observation of an in-house rollout)
blocks: [5, 7]
---

The observed sequence in which AI lands in an analytics function. Useful as a "where are we now" scale and as a warning: **you cannot skip a wave, but you can get stuck in one**.

| Wave | Duration | What happens |
|---|---|---|
| **1. Enthusiasm** | 1-2 months | local LLM agents, spontaneous MCP servers |
| **2. Ordering** | 2-4 months | an LLM gateway, an agreement with security, a skill hub |
| **3. Platformization** | 4-6 months | an MCP hub, JTBD registries, a domain knowledge base, AI champions |
| **4. Productization** | onward | agents inside the BI/data products, text-to-SQL and text-to-semantic, a semantic layer, an LLM wiki, an added-hours value model |

## What the local and cloud setups have in common

Wherever the models live, three elements stay the same: **MCP · skills · the domain knowledge base**.

> **MCP is the plumbing, not the meaning.** It is the control point and the place to constrain the handles: what is allowed and what is not.

The phrasing sets the right expectation: MCP solves connection and access control, not understanding of the domain. Meaning lives in the semantic layer and the domain knowledge base ([[ai-triad-prerequisites]]).

## What the MCP hub telemetry shows

The real usage profile of the hub shows that the top spots by unique users go not to analytical tools but to **general ones** (the issue tracker), followed by warehouse object search and metadata, the skill hub, BI queries, and SQL execution. A meaningful share of servers has a **double-digit call error rate** - a quality signal in its own right, worth putting on the dashboard next to the user count.

The practical conclusion: count not just calls but **unique users and the error share per server**. Calls rising without unique users rising is a sign of retries, not adoption.

Links: [[ai-triad-prerequisites]] · [[llm-assistant-architecture]] · [[ai-accelerator]] · [[ai-in-bi-approaches]]
