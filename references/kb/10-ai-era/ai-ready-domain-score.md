---
id: ai-ready-domain-score
title: The AI-ready domain score - measurable AI readiness for a domain
type: metric
source: "Course \"BI+AI strategy 26\", Day 3; internal practice (the knowledge-base completeness dashboard)"
confidence: verifiable (an internal metric); internal - do not publish the numbers
blocks: [2, 5, 6]
---

The only **operationalized** AI-readiness metric in the course materials: not "rate your maturity 0 to 4" but a concrete composite score per domain, computed automatically.

## Structure: two parts

### Part 1. Knowledge base completeness - 11 criteria

A dashboard of domain knowledge base completeness tracks the contribution of teams and team leads. The knowledge object types counted: **FAQ · OBJ (objects) · GLS (glossary) · DOCS · LIN (lineage) · SQL · EVAL · metrics (M.T / M.N) · SKILL · EVAL coverage**. For each domain: how many subdomains, how many contributors, how many of the 11 criteria are closed.

Also counted: the number of contributors, the number of commits in the period, the number of knowledge items in the period and per author, and a ranking of contributors.

### Part 2. Four non-knowledge-base criteria

1. **Roles** - all three roles are named: BI partner, domain semantics curator, AI champion
2. **Metrics** - at least a set share of the domain's metrics are healthy
3. **Certified and healthy dashboard views** - at least a set share of dashboard **views** land on healthy, certified ones
4. **Certified and healthy datamart hits** - at least a set share of **queries** hit healthy, certified marts

The thresholds on points 2-4 differ from each other in the original case and sit noticeably below 100% - a deliberate decision: the goal is not "everything is certified" but "most consumption goes through the trusted".

## Why the construction works

Three properties maturity models usually lack:

1. **It is computed from facts, not self-assessment.** Views, queries and commits are telemetry, not a questionnaire. This maps directly onto the ban on measuring effect by self-assessment (`evidence-2026.md` §1).
2. **It measures the share of consumption, not the share of coverage.** This is critical: the share of *views* on certified content is nothing like the share of dashboards that are certified. The second can be inflated by certifying dead content; the first cannot.
3. **Roles are part of the score.** A domain with no named AI champion and no semantics curator cannot be "AI-ready", however much metadata sits in it. It is the same principle as "an initiative with no owner is a line in a plan".

## How to use it in a strategy

As a target metric for block 5 and as a gate: a domain is connected to the assistant once its score crosses the threshold.

**Thresholds are set from your own baseline, not transplanted.** The right way is to measure the current values across domains, take the median and set the goal at the level of the best quartile; there are no universal constants here. A threshold lifted from somebody else's presentation is either unreachable or already passed - and useless as a gate either way.

Links: [[maturity-models]] · [[ai-in-bi-approaches]] · [[critical-data-status]] · [[content-certification]] · [[bi-project-metrics]]
