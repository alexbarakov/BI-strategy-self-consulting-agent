---
id: core-layer-project
title: The core layer of certified marts - the vision, health criteria, the start
type: case
source: "Course \"BI+AI strategy 26\", Day 6 - an internal project"
confidence: verifiable (an internal project)
origin: "an internal case walked through on the course; the numeric thresholds are anonymized - calibrate from your own baseline"
blocks: [4.1, 5]
---

The most fully worked example in the materials of what an AI-foundation initiative looks like when taken through to goals and metrics.

## The vision

Build a layer of certified marts (the core layer) as a trusted source for all consumers: **the data is ready on time · the data can be believed · the data is convenient to use · the data can be used by an AI assistant · resources are spent efficiently**.

The fourth point stands on the same line as the rest rather than as a separate AI initiative. That is the right packaging: **the same work covers both the analysts and the agent**.

What it gives:
- analysts - finding trustworthy data faster, fewer joins, more reliable refreshes
- the company - saving on CPU and storage consumption by limiting growth and encouraging reuse
- GenAI products - answering more accurately, thanks to better health of the marts under the metrics and dashboards, and better metadata

The upshot: raise the velocity of analytics projects · lower total cost (technical - CPU/RAM/storage; human - search, ad-hoc, creation, support) · raise the domain's readiness for an AI analyst ([[ai-ready-domain-score]]).

## What the warehouse and BI do together

Identify and mark the layer of trusted marts across the key entities · build roadmaps and improvement backlogs (to-be architecture, tasks) · fix responsibility for development and support · automate what can be automated.

## What the consumer gets

The catalog shows a **trust status: candidate / certified / degraded**. Certified carries default guarantees: an owner and contacts · a freshness SLA · baseline data quality thresholds · lineage · rules for changes (a contract). The principle is **reuse first**: new marts, dashboards and ad-hoc work are built from the core rather than from scratch.

The target layer architecture: `sandbox (the self-service zone) -> tech datamarts (3NF, denormalized facts, dimensions, reference data for reuse) -> presentation datamarts (enriched wide marts through views with consistent naming) -> the semantic layer (models: facts, dimensions, enrichments; SQL plus YAML) -> trusted BI content: metrics, dashboards, the AI analyst, SQL queries`.

## Health: the MVP set of criteria

**The principle:** satisfy binary, controllable assurance criteria and watch the control metrics move.

Four groups:
- **Ready on time** - the mart computes by the stated time, and fast
- **Can be believed** - covered by data contracts, no incidents
- **Convenient to use** - we read the necessary minimum optimally, the metadata is filled in
- **Efficient on resources** - we store only what is needed and use resources optimally

An example of the expanded check set on a dataset: error rate below a threshold · not a duplicate · built on the target engine · does not use temporary or dev schemas · **has an active owner** · has a refresh schedule · has been edited within the last year · the upstream mart refreshed within a few days.

What matters is not the specific threshold values but their property: every criterion is **binary and controllable** - for each there is an action that closes it.

## Integrations - one source of truth for the statuses

Core / certified / degraded badges in the search and on the mart's card in the data catalog, with filtering and detail on click · **the same status on dashboards and metrics** - one trust process · semantic layer objects certified by default · data contracts as part of the health score, with per-field coverage and a subscription to upstream contracts.

The key point: one status, visible in every tool. Otherwise certification turns into a local flag inside a single tool.

## Operational and business goals

Operational (on a two-year horizon, each with an interim and a final target): **reduce the share of user queries with two or more joins** · **raise the share of analysts' queries hitting core-layer tables** · keep the total number of marts under control.

The business goal is to lower total cost: technical, tied to platform billing (**marts are resources the domains pay for**), and human.

Both metrics are good because they measure behaviour (the share of queries, the share of hits) rather than the existence of an artifact.

## How to enter a domain

**Core data preparation** (the domain's BI partner): validate the list of core candidates (usage plus manual selection) and, after a health-scoring run, fix what can be fixed independently · analyse the analysts' current pain and how well the model reflects their needs and processes · prepare for the deep dive and book resource for it, allowing for migration.

**Core data deep dive:** a domain project team of BI plus data engineering is formed · an audit of the domain's data model, an analysis of the pain and the processes · slicing a backlog and a roadmap focused on cases with business value · pick the fruit and take it through to effect · move into the normal roadmap working mode. The target duration is **one quarter**.

## How to get around the "there is no low-hanging fruit" problem

Five rules for the start:
- **Do not begin with the most painful marts** - they are expensive and slow and win you no glory; the project stalls on the first hard case without having shown value
- **Begin with the most reused entities** - cross-domain objects (customer, listing, deal) give the most reuse per unit of effort
- **Presentation first, tech second** - a core presentation layer delivers visible benefit to analysts and to AI faster; technical optimization can follow
- **Health score as the leading signal** - it suggests core-layer candidates before any manual selection: go by the data rather than guess
- **Tie the work to AI readiness** - every new core mart immediately raises the domain's AI-ready score

Links: [[critical-data-status]] · [[ai-ready-domain-score]] · [[infra-billing]] · [[dg-launch-path]] · [[data-catalog-pitfalls]]
