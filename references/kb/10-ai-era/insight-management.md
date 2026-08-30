---
id: insight-management
title: Insight management - three models and where the LLM fits
type: pattern
source: "Course \"BI+AI strategy 26\", the \"Content management\" session, part 2"
confidence: verifiable (the models), vendor-measured (the vendor concepts)
blocks: [4.3, 5]
---

**An insight** is a valuable realization, an addition to knowledge or a new piece of knowledge obtained from analysing data, which either starts a new investigation or leads to an action useful to the company.

## Three models of insight management

| Model | Metaphor | What the BI team does |
|---|---|---|
| **Direct** | "We cook the food and feed you" - a restaurant | take the use cases and metrics -> identify, for each metric, the value range that calls for a decision -> build a decision tree and what-if analysis -> **automate the detection of trigger events in the data** -> set up targeted delivery of a message to the manager describing the event and recommending a decision (an insight digest, an insight bot) |
| **Indirect** | "We teach you to cook" - a food market | building BI reports · finding and automating domain analytical scenarios, giving the user a tool to look for insights themselves · a data literacy programme · growing managers' ability and motivation to extract insight from reports · BI community management |
| **Delegated** | "We give you the plot, the tools and the seeds" | helping to build analytics teams that give their own management personal direct and indirect insight management (data analysts, insight managers) |

The three models are not stages but coexisting modes for different roles; picking a mode for a role works the same way as picking a BI model in [[ssbi-vs-guided]].

## The anti-dashboard concept and the LLM

Every large vendor is exploring new models of interaction with casual users. The author's assessment: **there are more questions than answers**, but one thing is clear -

> BI teams need to start thinking about how they will manage the metadata of their data models and their logic. Before long they may have to hand those models to some BI bot, whatever BI system the bot is integrated with, and **carry responsibility for the results**.

**The rule for choosing between the estimates.** The base carries two ceiling figures that differ fourfold: the participants' subjective 70-80% and the 15-25% from practice. The choice is not arbitrary - **with no semantic layer and no certified core, take the lower bound**: a high estimate usually means the basic data need is not yet met, not that the agent is ready to meet it.

A realistic ceiling: in the ideal scenario this could close **15-25% of a user's queries** - noticeably more modest than the 70-80% from the participants' subjective estimates in [[participants-2026-benchmark]]. The divergence is worth showing alongside.

## The architectural chain

`A request for "ready" analytics and metric alerts` <- **the BI insight bot** (a new UI shortening the time from data to insight) <- **the LLM** as possibly the best interface for extraction and delivery <- **the semantic layer** (the technical representation of unified metrics) plus **the metric glossary** (the business logic of those unified metrics).

The key point: the LLM sits **above** the semantic layer and the glossary, not instead of them. It is the same chain as in the `no-assistant-without-foundation` kill-gate.

## The evolution of solution classes

`Chatbots` (fixed rules, repeating tasks) -> `copilots` (smart, targeted help) -> `agents` (know the business, plan and reason, **take actions**, scale). The distinction of an agent fits in one line: agents do not merely help, they act. Hence the requirements around identity, narrow entitlements and an audit trail.

Links: [[ai-in-bi-approaches]] · [[ai-cases-in-prod]] · [[content-catalog-ux]] · [[bi-project-metrics]]
