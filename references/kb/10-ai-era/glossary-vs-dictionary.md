---
id: glossary-vs-dictionary
title: The glossary, the data dictionary and the three levels of metadata
type: method
source: "Course \"BI+AI strategy 26\", Day 8"
confidence: verifiable
blocks: [4.1, 5]
---

## Three levels of defining metadata

Conceptual · logical · technical - each with its own metadata forms, its own relationships and **its own roles working with them**. The conceptual level is also called the semantic or business level; it is valid for a specific use case.

## The glossary versus the data dictionary

**A data glossary** is a set of business terms and their definitions, and nothing more.

**A data dictionary** enriches each database with metadata; it is a collection of information about schemas, tables and columns: data type · size · default values · constraints · relation to other data · **the column's meaning and purpose** · whether the information is PII.

Per DAMA, a data dictionary is where business and/or technical terms and definitions are held; it is usually designed for a limited set of metadata, centred on the names and definitions of physical data and related objects.

The practical conclusion: **these are two different artifacts with different owners**, and trying to keep them in one place usually breaks both.

## How the glossary reaches the user

A working arrangement from practice: the master glossary lives in the governance platform -> **a smart-terms macro in the corporate wiki** highlights the terms right inside page text through a search-and-highlight engine -> from the highlight you can raise a service-desk ticket to the data steward.

The point of the construction: **the term reaches the user at the moment of reading** instead of requiring a trip to a separate system. It is the same "in the flow of work" principle as in [[data-catalog-pitfalls]].

The same on a dashboard: the metric description is pulled up next to the field right in the report interface - a pretty name plus a full definition with the calculation formula and its caveats.

## The metric tree - an honest warning

> **A properly hierarchical tree is exactly what you will not get.**

A useful correction to the standard expectation: metrics are connected as a network, not a tree, and attempting a strict hierarchy ends either in a stretch or in the work stalling. What is worth building is relations and levels, not a single tree.

Links: [[semantic-layer-evidence]] · [[data-catalog-pitfalls]] · [[domain-knowledge-base]] · [[data-mgmt-processes]]
