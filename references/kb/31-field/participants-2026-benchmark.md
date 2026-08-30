---
id: participants-2026-benchmark
title: A field benchmark - 12 Russian BI projects, July-August 2026
type: benchmark
source: "Pre-course survey for \"BI+AI strategy 26\", Google Forms, 12 responses, 31.07-07.08.2026"
confidence: verifiable (participant self-report)
anonymity: "Most respondents allowed disclosure only in aggregate, without the company name. No company names appear in this file; when used in artifacts, aggregates only."
blocks: [1, 2, 3, 5, 6]
---

> **The boundary of applicability.** The sample consists entirely of technology companies and large retail with their own development teams. For a non-tech company, and for a company with no engineering of its own, these numbers **inflate expectations**: a median of "a warehouse team of ~12" reads as a norm that such a company does not have and never will. Comparing against the distribution is fine; setting goals from it is not. Checked in the end-to-end run in `70-golden-set/e2e-01-severnaya.md`.

A live reference for calibrating a diagnostic: what real BI projects in Russia look like as of mid-2026. The sample is small (n=12) and biased - these are participants in a strategy course, meaning people who have already started caring. Use it as "here is what everyone else has", **not as industry statistics**.

## The sample profile

- **Industries:** IT (4), retail (4), banking (3), energy (1)
- **Company size:** from 101-500 employees to 25,000+; half are 10,000+
- **Level in BI:** 7 of 12 say "expert, I can teach and deliver end to end", 5 say "I know it well, I have project experience"
- **Level in AI:** 1 builds agentic systems · 3 have introduced AI scenarios into their team's processes · 2 use it regularly and usefully · 4 have tried off-the-shelf assistants · 2 say "I only hear about it"

## Team sizes - medians and spread

| Role | Spread | Comment |
|---|---|---|
| Warehouse / data platform | 3 - 100 | median ~12 |
| Builders of BI solutions (BI/data analysts) | 3 - 400 | median ~10; in two cases the analysts **outnumber the warehouse team several times over** |
| Business users of BI | 27 - 40,000 | median ~2,500 |
| ML / DS engineers | 0 - 300 | median ~8 |
| **Data governance** | **0 - 11, median 2** | in 4 of 12 companies there is **no governance team at all** |
| GenAI platform / agent infrastructure | 0 - 97 | in 7 of 12 it is zero |

**The most telling ratio:** the governance team is almost always an order of magnitude smaller than the BI team, and is frequently zero. That is empirical confirmation of the "declared but not resourced" pattern from `review-gates.md` §3.

## The semantic layer - the state of it

| Status | Companies |
|---|---|
| none / not planned | 6 |
| in progress, under development, "we are trying to build one" | 4 |
| partially there (metrics in the A/B system only) | 1 |
| "yes, actively developing it" | 1 |

**Not one company has a mature semantic layer in full.** Which is precisely why the `no-assistant-without-foundation` kill-gate is not theoretical caution.

## An AI assistant over data

| Status | Companies |
|---|---|
| none / none planned | 5 |
| research, prototypes, "maybe" | 4 |
| pilots or several solutions | 2 |
| solutions running in production | 1 |

## What was tried with AI and what survived to production

**Survived:**
- MCP for analysing and building dashboards - in production, with a growing audience
- ad-hoc as a chatbot scenario - in production, works within limits
- automatic presentations with LLM summarization
- personalized HTML reports built from dashboards
- internal skills: gathering requirements, prototyping, speeding a dashboard up
- a chatbot answering questions about dashboards

**Did not survive:**
- Wren AI - "we tried it, it did not survive" (at another company it is in pilot)
- RAG over metrics - "in production, does not really work"
- text-to-SQL and text-to-dashboard prototypes in Superset - never taken to production
- automatic A/B test summaries - "we did not have the artifacts to hand for the context: the metric tree, metric priorities, prompts for grey-zone A/B tests"

**How to read this:** what survived works **on top of an existing structure** (dashboards, documentation, requirement templates). What did not survive required the model to reconstruct the semantics itself. That last quote about A/B tests is direct empirical confirmation of the context-layer thesis.

## Adoption - the share of target business users opening BI at least monthly

The answers: 20% · 30% · 40% · 42% ("we learned to compute adoption automatically, so the number is exact") · 54% · 60% · 70-90% · ~80%. Plus three answers giving an absolute user count instead of a percentage - a diagnostic sign in itself: **the metric is not being computed**.

The practical conclusion for a diagnostic: if a participant cannot name a percentage, that is a finding for block 2, not a gap in the questionnaire.

## How much ad-hoc could go to AI - a subjective estimate

The spread is 20% to 90%. The median is ~70-80%. The two most honest formulations:

> "It depends on the data domain: somewhere 80%, somewhere 30-40%."

> "70%. But that high estimate reflects the fact that the basic data need is not yet met. As the needs get more complex the percentage will probably be lower."

Use it as a warning: a high estimate of AI's potential often signals low maturity of demand rather than high readiness.

## What is being driven right now - the top initiatives

The semantic layer and metric standardization (5 of 12) · text-to-SQL / text-to-result / smart intake of requests (5) · automatic archiving of junk reports and tidying production (2) · a single platform for LLM ad-hoc with an autonomous agent inside narrow bounds · a data portal as a single entry point · smart search in BI and scheduled dashboard warming · faster data delivery through auto-generated ETL pipelines · competency matrices and training · import substitution.

## The most requested course topics

1. **AI readiness of data: the semantic layer, the core layer, domain context** - 9 of 12
2. The AI-plus-BI trend and the shift to agentic analytics - 8
3. The structure of a BI strategy and goal setting - 8
4. Content and governance in the AI era (certification, health score, AI slop) - 7
5. Agent architecture and eval - MCP, skills, judge gates, the mathematics of accuracy - 7
6. The team, the profession, the future of the BI role - 5

Links: [[pain-fronts-2026]] · [[painpoints-analysis]] · [[selfservice-practices]] · [[bi-project-metrics]]
