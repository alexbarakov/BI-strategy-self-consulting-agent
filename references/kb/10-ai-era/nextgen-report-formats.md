---
id: nextgen-report-formats
title: The dashboard is no longer the only form of finished analytics
type: pattern
source: "Course \"BI+AI strategy 26\", Day 8"
confidence: verifiable
blocks: [3, 4.2, 5]
---

A third format now stands beside the dashboard - the **data app**: not a picture to look at but an interface where you can enter data, trigger a recalculation and call an agent.

## Three formats - how they differ in purpose

| Format | Purpose | Properties |
|---|---|---|
| **Dashboard** | monitoring and a general map of the process | read-only · long-lived · a mass audience |
| **Data app** | data entry, a scenario, an action | read-write · parameters · calls an agent |
| **Notebook** | a one-off investigation | code and output · a single author · short-lived |

## What they are built with - three approaches (a different dimension: each covers several formats)

**Reactive notebooks** - marimo, Hex, Deepnote. Cover the notebook and the data app. Cells recompute along their dependencies, so there is no hidden state; marimo sits on disk as an ordinary `.py`: reviewable in git, runnable both as a script and as an app. *What you pay:* the author needs Python skills and you need your own runtime; Hex's format is closed - you cannot take it out into git.

**Code-first frameworks** - Streamlit, Dash, Evidence, Observable. Cover the dashboard and the data app. Full control over the interface; Evidence and Observable build a static site out of SQL and markdown, which is cheap to host. *What you pay:* they cover only the interface - authentication, entitlements, deployment and writes remain your problem.

**Warehouse-native** - Sigma, Databricks Apps, Streamlit-in-Snowflake. Cover the dashboard and the data app, **including writes**. Entitlements are inherited from the warehouse and enforced at query level; writes go into warehouse tables, and metric definitions come from the catalog. *What you pay:* you build from the vendor's blocks - less freedom.

## How this lands in a strategy

The data app is a **fourth channel** alongside centralized, self-service and agentic. The key question when adding it is not "which framework" but **who is answerable for entitlements and writes**: that is exactly where the three approaches diverge fundamentally, and the framework choice effectively predetermines the governance model.

Links: [[unified-bi-platform]] · [[ssbi-vs-guided]] · [[centralized-practices]]
