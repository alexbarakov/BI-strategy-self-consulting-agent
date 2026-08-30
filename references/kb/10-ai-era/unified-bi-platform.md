---
id: unified-bi-platform
title: A unified BI platform - three layers as one product
type: case
source: "Course \"BI+AI strategy 26\", Day 8 - internal practice"
confidence: verifiable (internal experience)
origin: "an internal case walked through on the course; the numeric thresholds are anonymized - calibrate from your own baseline"
blocks: [3, 4.2, 5]
---

The target platform model for the AI era: **creation · meaning · consumption** assembled into one product.

| Layer | What is in it |
|---|---|
| **Consumption** - the user gets an answer | the data portal as a single entry point · the "Report" with Monitor and Explore modes · the metric card, smart search · reporting as an engine |
| **Meaning / data** - what each metric means | the semantic layer (definitions) · the semantic engine (assembly) · the core layer (atomic facts) · **agent contracts for AI** |
| **Creation** - producing analytics | notebook mode (analysts) · report builder (the business) · the ad-hoc-to-production continuum · hybrid compute |

## Separating core, semantic layer and semantic engine

Three different questions, and the effects do not double-count:

- **The semantic layer is WHAT to compute.** Canonical metric definitions, derived calculations, valid join paths. **It materializes nothing.**
- **The semantic engine is HOW to serve it.** A runtime over the layer: assembling presentation marts, semantic assembly of SQL. **On the fly by default.**
- **The core layer is WHAT FROM.** Atomic facts and entities, integrated and deduplicated, a stable contract. **Always materialized.**

> **The default rule: a mart is NOT created - we compute on the fly.** Refusing unnecessary materialization is the engine's infrastructural win.

This rule is the direct opposite of the familiar "a mart per report", and deserves a separate discussion when transplanting it.

## Three principles of the experience

1. **One entrance.** The data portal is the single entry point; the user does not think about which tool to go to.
2. **One artifact.** A "report" instead of splitting dashboard from data app; Monitor or Explore mode is an implementation detail, not a choice the user makes.
3. **One path.** Ad-hoc -> dataset -> production is a smooth **change in the level of governance over one object**, with no migration of SQL or data.

Underneath, this is held up by the principle of **"reporting as an engine, not a product"** - by analogy with Chromium inside Chrome and Edge. The practical consequence: the visualization editor becomes a shared component for the SQL editor and for BI, and working with charts is identical across the platform's tools.

## The AI assistant inside a dashboard

The assistant is built into the BI tool's side panel and **understands the context of the open dashboard**: it answers questions about the data without going to another tool, respects the filters chosen (period, product, team) and does not ask the user to re-enter what is already set on the dashboard.

This is a good example of the right framing: context is taken from the interface state rather than requested from the user again.

## MCP quality as a product metric

A dedicated sprint goal: **bring the MCP server's error rate down to a low single-digit percentage**. Over the sprint the rate came down by roughly a third from where it started, close to the target.

What produced the effect: MCP began explaining to the agent what had happened and what to do next (checked against a sample of real engine errors) · dependency search moved from walking every dashboard to a single fast query, cutting that scenario's error rate by nearly an order of magnitude · statistics began to be collected **separately per tool and per error cause**.

What remains: roughly every second remaining error is a timeout or a temporary unavailability · most errors arise when executing SQL or working with datasets · a small but persistent share is the agent using an old tool name or a wrong identifier.

The next steps: do not hold long queries until timeout - return a task number immediately and fetch the result in a separate call · for transient failures, one automatic retry after the recommended pause · validate the tool name, the identifier and the required parameters before sending, keeping old names as compatible aliases.

**Why this matters for a strategy:** the MCP error rate is a measurable, controllable and comprehensible quality metric for agentic infrastructure that does not require judging "answer quality". It is worth setting up before any accuracy metrics.

## Which year metrics to put on top

The set that worked as the platform's annual shop window (the values are anonymized - what matters is the composition):

- **the share of tasks solved without an analyst** - rising
- **the share of analysts' time spent on investigation** rather than routine - rising
- **weekly active users of the AI assistant** - rising several times over
- **the time to create a "report"** - falling several times over
- **platform NPS** - rising

The composition of the set matters more than the numbers: two metrics about redistributing labour, one about AI adoption, one about speed, one about satisfaction. None is measured by self-assessment.

The author's closing conclusion: **"we were overrating the importance of the tool"** - data, context and AI work as one product.

Links: [[bi-tool-selection]] · [[semantic-layer-evidence]] · [[nextgen-report-formats]] · [[core-layer-project]]
