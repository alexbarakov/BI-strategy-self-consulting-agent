---
id: data-domains-classification
title: 1.2 Domain classification of data and ownership
type: method
source: "Guide 2.0, sheet \"1. Data Domains Classification\"; course, Day 2"
confidence: verifiable
blocks: [1, 4.1]
---

**The load-bearing element of the whole method.** The domain structure is the starting point for most of the practices that follow: the access matrix by domain, the data quality assessment by domain, availability by domain, the information supply-demand matrix, the communication plan by domain.

A data domain is a delimited area of data tied to a business function or line. It reflects where the data comes from and who it is meant for; it is run by a specialist team responsible for its collection, quality and use. Domains decentralize responsibility for data.

## The structure of the sheet

Filled in to the **top two levels** (domain -> subdomain), with each row carrying:

`System · Domain · Subdomain · Description · Level of Detail · Data Owner (Sign off) · Business Data Steward · Tech Data Steward · Sensitivity type · Criticality level · Last review date`

The three roles are kept distinct deliberately: **the data owner signs off**, the business data steward is answerable for meaning, and the tech data steward for implementation.

## Classification by significance - what we lose if it disappears

| Type | Definition | Examples |
|---|---|---|
| **Strategic** | unique, created in-house, a source of competitive advantage | customer data, risk profile models |
| **Critical** | materially affects external reporting, risk management, key functions | finance, supply chain, counterparties, pricing |
| **Cross-functional** | the same data in two or more processes; definitions, quality and format must stay in sync | sales and costs; customer data; orders |
| **Local** | not for regulatory reporting and not for cross-functional communication | everything else |

Plus a **domain significance matrix**: domains are laid out on the axes of business value and sensitivity.

## Adjacent: the enterprise data ontology

The next maturity level is a semantic model describing the domain's entities, their attributes and their relations in a machine-readable graph (Customer -> Places -> Order -> Contains -> Product). An ontology describes **kinds** of entities, not instances. The course references FIBO, banking data models, knowledge graphs for utilities, and taxonomy-to-ontology work (Enterprise Knowledge).

## Why this is critical in the AI era

An agent does not guess where a domain's boundary lies. Without an explicit carve-up and clear ownership it does not know whose answer counts as correct or whom to ask for confirmation. Domains are a precondition for [[critical-data-status]] and for the domain knowledge base in the AI foundation.

Links: [[guide-structure]] · [[critical-data-status]] · [[info-supply-demand]] · [[access-matrix]] · [[data-mgmt-processes]]
