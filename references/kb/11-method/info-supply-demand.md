---
id: info-supply-demand
title: 1.4 The information supply-demand matrix
type: method
source: "Guide 2.0, sheet \"1. Info supply-demand matrix\"; course, Day 2"
confidence: verifiable
blocks: [1, 2]
---

The central analytical exercise of the AS-IS: **who wants what from analytics, and what is actually available to whom**. Formally, it is the definition of the BI project's scope.

The course's thesis: *"You cannot meet needs you do not know about."* The method rejects the objection "I am just a BI manager, I administer the server and build reports on request": what the business needs is governed BI, a mix of self-service and centralized, that actually meets the needs.

## Four steps to assemble it

1. Which analytical needs exist -> the data domain classifier ([[data-domains-classification]])
2. For which management roles -> the role classifier ([[user-classification]])
3. Who needs what -> the domain-by-role matrix itself
4. For which tasks -> the base of analytics use cases

The matrix is built on the intersection of "domain/subdomain (down) by management role (across)". A cell may hold not a tick but **an estimate of the revenue effect** in money or points - which turns the matrix straight into a prioritization and a total revenue impact.

## The two scorecards that grow out of it

- **A data availability scorecard** - for each process group: `available in verified data sources` by `available in BI reports` -> a combined score of 0 to 1.
- **Reports availability by role / workplace coverage** - the same grid cut by role, with total workplace coverage along the bottom. Red means no report, yellow means there is one but it does not cover the requirement, green means it does.

## Use cases as the unit of demand

A use case is one example of applying specific data to a specific business goal; in practice it coincides with a user story: **"As a [role], I want to analyse [something] so that I can [make a decision]."** The case passport from the course: stakeholder and job title · domain · the key logic · the data needed · volumes · what falls under governance here · whether it was attempted before and why it failed · revenue growth drivers · potential savings · feasibility · effort · cost drivers · a cost forecast in FTE.

## Prioritization

The practical scale from the course (coarse): the report is needed by 3 roles `+3` · a CxO is among the requesters `+2` · the requester has no in-house resource to solve it `+2` · the automation effect is 2 FTE `+1`.

The formal alternative is **RICE**: `Reach x Impact x Confidence / Effort`. Impact: 3.0 massive / 2.0 high / 1.0 medium / 0.5 low / 0.25 minimal. Confidence: 1.0 we know for certain / 0.9 nearly certain / 0.7 a hypothesis / 0.5 intuition. A long list of cases with RICE scoring is realistically assembled by an LLM and read through by a human.

## The Pareto rule over domains

From the course: **20-40% of domains cover roughly 60-85% of the use cases**. Hence the order: a long list of cases -> prioritization -> which data they need -> which data products follow from the comparison.

## Where this ends up

Three slides in the BI team's annual report to management, compared against last year: who needs what and what exists -> what matters more -> the list of strategic projects -> the list of obstacles. The automated version: mapping reports to domains plus mapping users to roles equals live coverage monitoring you can drill into down to the individual report and user.

Links: [[guide-structure]] · [[data-domains-classification]] · [[user-classification]] · [[bi-project-metrics]] · [[action-plan]]
