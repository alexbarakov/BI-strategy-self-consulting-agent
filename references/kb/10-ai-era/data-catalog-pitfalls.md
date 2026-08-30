---
id: data-catalog-pitfalls
title: The data catalog - when to roll it out, the classic failures, and MCP as the turning point
type: pattern
source: "Course \"BI+AI strategy 26\", Day 6"
confidence: verifiable
blocks: [4.1, 5]
---

## When it is time to roll one out

Growth in the size and complexity of a data platform always drives time to value down:

`[Project Delivery Date] - [Project Committed Date] = [Time to Value]`

**There is a point at which the aggregate efficiency loss of the company's power users exceeds the cost of a data catalog solution.** This can be measured with experiments if you want it to be - and the method suggests measuring rather than deciding by feel.

## The ghost town - a catalog with no descriptions and no metadata

The most frequent failure. Three antidotes:

1. **Automate as far as you can.** Get as much metadata automatically as possible. There is no reason anyone should be filling in keys for each individual dataset by hand. And this is not all about ML: domain and stewards can be computed algorithmically and pre-filled.
2. **Documentation is entered in the flow of work with the asset.** A pattern that works is **documentation checks in CI/CD that break the build** when documentation is missing.
3. **Curate the top 20%.** You cannot boil the ocean; knowing which tables are queried and which reports are viewed most often sets the curation scope.

## Fragmentation of the golden path

> Your catalog is too broad and not deep enough, which fragments the UX.

Users end up working out which tool is for what, and the data team ends up supporting both options. **The antidote: deliberately choose the golden path and switch off the duplicating functions**, so that one option remains on offer.

Three classic fragmentation points:
- **Discussions** - in the messenger or in the catalog. *Do not believe in the data catalog's built-in messenger. That is self-deception.*
- **The knowledge base** - articles in the wiki or in the catalog. Pick one and integrate it into the other.
- **Queries** - in the BI tool, in the IDE, or through the catalog.

## The open questions you will have to answer yourself

- How much content should be in there: enough to find **everything**, or set up so that the **certified** is what gets found?
- A tool for power users, or for casual users too?
- Should the report catalog be grown inside it - where the user is casual and extra functionality gets in the way of finding reports?
- How to draw people in: **compulsion** (a table does not get put on a schedule without a card with metadata filled in) or **incentive** (saturating it with value, making sharing easier)?
- Which product metrics to use, and how to assemble a team that will grow them?

The first question is a philosophical fork: "find everything" and "find the trusted" call for different ranking and a different UX.

## What matters in lineage

1. Breadth of native integrations
2. **Column-level linkage**
3. ...and only then, looks

## The turning point: MCP plus the data catalog

The Model Context Protocol is an open standard for integrating LLMs with external tools and sources - a standardized way for AI applications to obtain and use information from different systems (the course's analogy: the way USB-C gives devices a standard connector).

The author's assessment: **MCP plus the data catalog is a game changer**. The catalog stops being a shop window for humans and becomes the context interface for an agent - meaning all the investment in metadata pays back a second time. It also moves the ghost town from "unpleasant" to "blocking": an empty catalog means the agent has nothing to read.

Links: [[core-layer-project]] · [[data-team-pain-points]] · [[data-mgmt-processes]] · [[ai-in-data-processes]]
