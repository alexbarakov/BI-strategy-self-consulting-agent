---
id: ssbi-workflow
title: The self-service operating model - workflow, tools by role, metrics
type: method
source: "Course \"BI+AI strategy 26\", Day 3"
confidence: verifiable
blocks: [3, 4.3, 6]
---

Six steps to launching self-service, after identify and classify from [[user-classification]].

## Step 3. Define the self-service workflow - in both directions

**Left to right: curate -> create -> consume.** The centralized team curates the sources, power users create, everyone consumes.

**Right to left: propose -> prototype -> promote.** If a report proves popular, power users submit it to the governance committee. The report serves as **the prototype of a new mass, cross-functional report**. The committee checks the embedded indicators and data definitions against the corporate standards. The BI team works out how to "productionize" a mass report with adequate scalability, security and reliability.

The reverse direction is the one usually missing: without it a good self-service report stays local forever.

## Step 4. Mapping roles onto tools

| Role | Tools |
|---|---|
| **Data consumers** | ready reports in BI, for making decisions |
| **Data explorers** | customizing reports and creating new ones from pre-built models - report templates and published data sources; **data wrangling tools** - lightweight data preparation, built into BI or standalone, to add spreadsheet data to a source or quickly assemble a select |
| **Data analysts** | data preparation tools for combining sources, then visual discovery for analysis and visualization |
| **Data scientists** | code (Java, Python, SQL), ML tooling |

**The main mistake is giving data consumers the analysts' tools.** They take fright at all the buttons and menu items, never give the tool a chance, and pick up the phone to ask a local analyst or IT to build the report. The reverse works too.

## Steps 5-6. Grant entitlements and start continuous training

A BI community chat · a BI/DWH school · marathons and courses · **internal certification as a condition of access to tools and environments** · a BI champion programme · a BI doctor service · BI forums and events.

## Self-service metrics - two things usually get tracked

1. **Penetration of self-service scenarios among non-analysts** - the share of creators / explorers
2. **The number of ad-hoc requests in channels and Jira tickets per non-analyst** in the channel; plus an analysis of the "losses" from waiting for answers and from context switching

## How to grow self-service

Grow the layer of **certified datasets** for self-service - wide, comprehensible, high quality · workshops with the business teams · grow BI champions · run marathons.

## Where self-service is heading

GenAI bots (agents, concierges, assistants) · a global rise in data literacy · ready frameworks (what lives where, the tools, the centres of expertise) · self-service ETL with no-code transformations · ready sources in the form of data catalogs with descriptions · pre-built boards ready for editing.

## The evolution of org models: federate to accelerate

Hybrid models are more often effective. Excessive centralization creates bottlenecks and a lack of business buy-in; decentralization risks approaches that do not connect. **A hybrid preserves the centralized capabilities and decision rights** (particularly over data management and standards) while the analyst groups stay embedded in the business and carry responsibility.

It requires: business engagement · matrix reporting and co-locating part of the resource · strong governance processes for data and reports · strong leadership and communication.

A separate observation: **early in the governance journey it makes sense to work more centrally** - it is easier to build and control a central team and to ensure quality. Over time, as the business grows more experienced, the centre returns to a facilitator's role and hands over more autonomy.

Links: [[ssbi-vs-guided]] · [[ssbi-failure-causes]] · [[user-classification]] · [[selfservice-practices]]
