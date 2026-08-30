---
id: bi-tool-selection
title: Choosing a BI tool, and the Russian BI reality of 2022-26
type: method
source: "Course \"BI+AI strategy 26\", Day 8"
confidence: verifiable (the market survey), author estimate (the product characterizations)
blocks: [5]
---

## The fork after 2022

Three strategies companies choose between: **re-implement · look for "workarounds" · build your own**.

## A map of the Russian BI market's segments

| Segment | Examples | Upside | Downside |
|---|---|---|---|
| **"Fiercely centralized" heavy BI** | Foresight, Luxms, Visiology | custom visualizations, plenty of options for working with data, all of them have ETL, **no sanctions risk**, Russian-language support | requires JavaScript knowledge, high development and training costs - effectively no self-service; weak integration partners; the product may deflate; grown-up pricing, though there are budget packages |
| **Semi-self-service** | Modus, FlyBI, Analytics Workspace | drag-and-drop exists, charts get built, data can be prepared | anything harder needs JavaScript |
| **Quasi-Russian** | Delta BI | well-developed ETL and dashboarding features | no perpetual licensing, high risk |
| **Russian cloud** | DataLens | free, with plans for open source plus a set of paid features | a cloud solution at the level of Google Data Studio, **effectively no ETL** |
| **Chinese** | Fine BI | a decent commercial product, not perfect but not raw; prospects for development, **strongly customer-oriented** | grown-up pricing, exactly like the vendors who left; few Russian-language training materials |
| **Global open source** | Superset, Redash, Metabase | "free" with paid features, an English-speaking community exists | minimal functionality, simple but working; **no support - you need an in-house team** |
| **Departed vendors** | - | perpetual licences still work in places | you cannot buy; supply "workarounds" through third countries exist, but companies rate the risk as too high for further investment |

The key conclusion the method draws: **despite the existence of workarounds, the risks usually outweigh them** - and that consideration matters more than a feature comparison.

## A questionnaire for selecting a BI system

Comparison is non-trivial and **depends heavily on the comparison factors and their weights**. The mechanics: the project working group sets a factor's weight from business requirements (1-3), and the tool is scored from the pilot results (1-5).

Factors: data visualization (the variety and the speed of building visual objects) · ETL (the range of operations) · self-service features (the simplicity and breadth of no-code) · **AI functionality (insight generation, NLP)** · cross-platform support and a native mobile app · **built-in data governance features, a data catalog** · the range of statistical functions · built-in mapping · collaborative work on reports · storytelling · performance limitations on big data · row-level security capabilities · ease of embedding · the range of connectors · working with cubes · real time · cloud · interface simplicity · security · integrability · **price (licences plus support)**.

## Adjacent ecosystem topics

Several BI systems coexisting · insight management · conversational BI and chatbots · the semantic layer · the glossary · building and maintaining a metadata management system · mailings out of BI · embedding into corporate systems · BI in the cloud · mapping tools (a shared spreadsheet versus a mapping interface) · models of friendship between BI and the wiki · BI on mobile · **BI inside corporate messengers**.

Links: [[bi-toolset-landscape]] · [[unified-bi-platform]] · [[semantic-layer-evidence]] · [[ai-in-bi-approaches]]
