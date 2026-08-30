---
id: dg-launch-path
title: A rational path to launching data governance - natural governance and three stages
type: method
source: "Course \"BI+AI strategy 26\", Day 6"
confidence: verifiable
blocks: [4.1, 7]
---

The method advises **not starting with a formal programme**. The route is built so that a budget refusal does not kill the direction.

## The fork at the start

The question: "do we need a formal, dedicated data governance function?" Until the answer is obvious, you run **common-sense governance at the level of individual teams**: small quick-win projects of the first order that can be delivered in weeks.

From there, two branches:
- **budget approved** -> form the governance office, `land and expand with a DG program`
- **budget refused** -> keep developing common-sense governance, restart through an MVP later

The "refused" branch is not a dead end but a full route. This matters: governance started from the bottom survives the budget cycle.

## What is needed to move past the MVP

The condition is stated explicitly: **at least 2 of 4** -
- interest from other business domain owners
- a business domain owner willing to take part in the MVP
- support from the COO / CTO / CFO / CEO
- support from the ML / warehouse / product analytics teams

Plus the entry conditions: an analysis of the pain and the drivers, visible incidents, business drivers; and picking **one most critical business domain**, or one secondary one to run it in.

## Three maturity stages

| Stage | Name | Content |
|---|---|---|
| **1** | "A splendid minimum" | designing the domain structure · fixing owners and other roles on the objects · criticality classification · building the MVP case and packaging the result |
| **2** | "A sensible addition" | the metric tree and the business ontology · building the semantic layer · developing and maintaining the rules · introducing data contracts · a full pain analysis |
| **3** | "The lot of the mature" | standardizing operations · a public governance status · reporting and metric monitoring · **architectural oversight and a governance committee** · working incidents and improving quality · selecting and developing the tooling |

The stage names carry an instruction of their own: stage 1 is obliged to be modest and finished rather than large and unfinished.

## The field picture: how governance is actually set up in real companies

Reviewing several Russian companies shows stable patterns:

- **More often than not there is no separate governance team.** Governance is "dissolved into the processes" and lives as a set of projects inside the platform team; frequently these are part-time people developing the catalog and data quality.
- **There is no CDO role** in most; the function is de facto performed by the head of the data platform or a global head of data and analytics.
- **Domains are carved up and data engineers distributed, but the governance rules are kept central** - the typical intermediate construction on the way to data mesh.
- **A "partner" or curator role inside a domain** appears earlier than a formal governance office.
- **Data stewards are more often centralized**; attempts to establish owner and curator roles inside domains frequently fail to take - "nobody there ever started doing it".
- **A change of CDO can pause the whole programme**, with a turn back towards decentralization.
- **The conflict with culture** is named directly: formalizing rules and imposing roles gets rejected in companies with a strong culture of autonomy.
- The mature configuration, where it exists: a separate six-person team - 2 on tools enablement, 2 on compliance, **1 on AI and ML governance**, 1 manager; a sponsor at C-1 to C-3 level; a separate compliance committee with legal, government relations and technical security.

The practical conclusion for a strategy: **plan for the "there will be no formal governance" option** and design governance to work as a set of checks embedded in the processes rather than as an office.

Links: [[data-mgmt-processes]] · [[data-team-pain-points]] · [[core-layer-project]] · [[action-plan]]
