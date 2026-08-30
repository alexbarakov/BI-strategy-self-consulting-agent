---
id: user-classification
title: 1.3 Classification of BI users and consumption models
type: method
source: "Guide 2.0, sheet \"1. User Classification and BI Models\"; course, Day 2 (after Wayne Eckerson)"
confidence: verifiable
blocks: [1, 3]
---

The principle from the course: **"If you are not documenting your business users, you have no basis for a strategy. You are effectively driving blind."** Two steps - identify (find everyone who uses data and reports) and classify (sort them by how they consume and produce analytics).

## Two groups and four categories (Eckerson)

**Casual users** - use data to do their job. They need a "silver service": data and reports fitted to their role.
- **Data customers** - read visualizations, put data in context, create nothing
- **Data explorers** - have the time and the experience to extend their own dashboards

**Power users** - are paid to analyse data full time. They need genuine self-service: creating datasets and reports without IT.
- **Data analysts** - go through the full cycle from source to report
- **Data scientists** - highly literate, build ML models, visualize, work autonomously

Separately, **self-service support** - BI admins, engineers, architects, data curators.

## What gets filled in

1. **The classifier of management roles**: role · description · identification logic (AD groups) · focus data areas · the priority BI service (view what exists / build reports yourself / build reports and sources) · self-service BI potential (high/medium/low).
2. **Headcount by category** - total / actual / the year's growth plan, cut by department. The practical output: auto-populated AD groups for granting rights to self-service tools.
3. **The right BI model per department** - current status, potential, data competencies, self-service champions, constraints.
4. **The pros and cons of the models** for this particular company: self-service BI · guided analytics · delegated.

## The questions that decide the category

Do they want to just view static reports · to click through into detail · to edit and rebuild an analysis · to build analytical models themselves · to save their own edits · to assemble reports from ready blocks · to go through the full cycle starting from preparing the source.

Links: [[guide-structure]] · [[info-supply-demand]] · [[selfservice-practices]] · [[centralized-practices]] · [[access-matrix]]
