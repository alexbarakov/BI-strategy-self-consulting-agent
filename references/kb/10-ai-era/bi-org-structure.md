---
id: bi-org-structure
title: Organizational development of BI - its place in the company, the structure, the analytics council
type: method
source: "Course \"BI+AI strategy 26\", Day 9"
confidence: verifiable
blocks: [3, 6]
---

The block's five live questions: where BI sits in the org structure · the structure of the BI department · the roles in the team · the competencies of a BI analyst-developer · hiring.

## Where BI sits - two models

| IT-centric | Business-centric |
|---|---|
| CIO / VP IT -> Head of DWH -> Head of BI · or VP corporate management / COO -> Head of BI | CDO / CAO -> Head of BI |
| **the traditional approach:** on its way out, technical, un-business-like | **the fashionable approach:** focused on service to the business, typical of large global companies |

## The target structure for "governed self-service plus centralized reporting"

`Executives -> Head of D&A -> the D&A centre`, holding three blocks:

- **The BI reporting office** (Head of BI Reporting Office): BI business analyst, BI business consultant, analysts - centralized certified reporting and support
- **The self-service BI office** (Head of Self-Service BI Office): BI user support manager, BI community manager, BI administrator - self-service services and support
- **The DWH team**: DWH architect, DWH developers, business analyst

The logic of the split: **separate heads for the report factory and self-service**, because their goals differ, and under a single owner one block always eats the other.

## The data and analytics council

A two-tier construction:
- **The working committee** - analytics managers from each business unit, the people who feel "the pain of bad data" every day. There can be subcommittees: a data governance committee, a digital transformation committee, a reporting committee, a prioritization board.
- **The executive committee** - the business sponsors. **Analysts are best distracted here as little as possible.**

**The eight processes the council runs:**

| Process | What it does |
|---|---|
| Standardize data | oversight of defining, documenting and managing the key data elements through glossaries and catalogs |
| Oversee data quality | standards and rules for quality that is fit for the purpose of use |
| **Govern reports** | processes for reviewing and certifying new corporate reports and changes to certified ones |
| **Govern algorithms** | review and certification of new algorithms, management of analytical models, monitoring of their accuracy |
| Establish data controls and policies | defining, documenting, managing and enforcing access, privacy and security policies |
| Prioritize projects | prioritizing requests for new applications, features and changes |
| Standardize technology | corporate standards for technology and tools |
| Foster data literacy | training and support programmes to grow data literacy |
| Increase awareness | marketing and communications to grow awareness and adoption |

**Govern algorithms** is a ready-made home for AI governance: model certification and accuracy monitoring get built into an organ that already exists rather than needing a new committee.

**What the executive tier does** (whatever it is called): communicates and sells the vision of modern analytics · represents departmental interests in setting the budget · aligns analytics decisions with the strategic initiatives · approves the processes, policies, roles and responsibilities of BI governance · **sets the example of using facts instead of intuition**, putting data and BI reports at the centre of every conversation.

## Roles: 50+ - you do not need them all

The D&A role catalog runs to over fifty. The method's instruction: **define your own** rather than roll out the catalog.

## Change-the-business / run-the-business and scrum in BI

The team splits into **change-the-business** and **run-the-business** subteams. The scrum construction: product owner plus business analyst / tech lead plus BI developers.

- **The product owner** - the point of contact for stakeholders, product backlog management, tracking activity across the run and change domains, **creating prototypes of every new dashboard and agreeing them with clients**, accepting sprint results before release, prioritizing the prototyped backlog, client meetings, people management. *Focus: clients, results, people.*
- **The BI tech lead as scrum master** - sprint planning and review, retrospectives, the sprint increment, demonstrating results, growing BI expertise, supporting service-desk tickets, coaching the team, maintaining warehouse and BI environment documentation, taking part in training as a data expert. *Focus: the team and the tasks.*
- **BI analysts / developers** - owning and executing the work, backlog refinement, quality-improvement initiatives. *Focus: the tasks.*
- **Business analysts** - gathering requirements, documenting projects. *Focus: requirements and process.*

The rhythm: fortnightly planning on Monday, a mid-sprint review, a retrospective on Friday, fortnightly backlog refinement, weekly warehouse sprint planning, daily joint stand-ups.

**A recorded experiment:** they dropped the daily; in its place, refinement moved from a shared meeting into the domains, plus a warm-up, plus a weekly slot for BI governance, and a two-hour rolling sprint planning.

Links: [[regular-meetings]] · [[bi-competency-matrix]] · [[bi-routine-calendar]] · [[centralized-bi-brand]]
