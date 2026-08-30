---
id: critical-data-status
title: 2.1 The status of critical data by domain, and master data sources
type: method
source: "Guide 2.0, sheet \"2.1 Critical data\"; course, Day 2"
confidence: verifiable
blocks: [4.1, 5]
---

Recording the status: what is critical for us · how the critical part is represented as reliable, maintained tables in the warehouse · what is currently wrong with quality and what exactly we plan to do.

## The domain scorecard

`Domain / subdomain · business criticality (expert judgement, 1-10) · master data source coverage · the key marts for BI · data quality status · plans for the quarter / half-year / year`

The quality status grading from the course examples: "High - no critical problems" · "Medium - usable with limitations: completeness ~70%, no data from system X" · "Medium - freshness, nightly loads fail periodically".

## Master data source management

**Not to be confused with master data management.** This is about identifying, optimizing and owning the master sources and procedures inside the warehouse.

The registry: `master data source · domain · description · for whom · requester · data steward · owner · developer · schedule · DQ rules · SS rules · open issues`

What it buys you:
- the selection of marts best suited to analysing a specific domain
- **fewer duplicate sources**
- master data sources as the foundation for both the self-service data catalog and centralized reporting
- ownership, checks and monitoring focused on master data sources rather than on everything indiscriminately

The registry is better kept in the data catalog than in a spreadsheet.

## Why this is the gate for AI

This is the sheet that answers "what is the agent allowed to answer on". A certified core equals master data sources with confirmed ownership and a quality status. Without it, `no-semantic-without-core` does not pass.

Links: [[data-domains-classification]] · [[data-mgmt-processes]] · [[guide-structure]]
