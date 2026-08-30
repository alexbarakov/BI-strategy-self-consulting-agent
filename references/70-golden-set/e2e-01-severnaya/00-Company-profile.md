# 00. Company profile — Severnaya Pharmacy Chain

> A fictional company. The profile is the **input** to the skill: what a participant tells you in the interview. The strategy assembled from it is in the neighbouring files.

## Profile

| Parameter | Value |
|---|---|
| Industry | pharmacy retail |
| Scale | 620 stores across seven regions, 4,800 employees |
| Revenue | typical for a regional player; growth below market two years running |
| Company type | **not a technology company**: IT is a support function under the COO |
| Regulatory perimeter | controlled-substance circulation, mandatory serialization, personal data in the loyalty programme |

## Team and infrastructure

| What | How it is |
|---|---|
| Central BI team | 3 people: a lead and two report developers |
| Analysts in domains | ~15 across categories and logistics, ranging from confident SQL to manual Excel |
| Data engineers | **none in-house**; a contractor builds data marts on request, every change billed separately |
| Data Governance | no team, no role, no projects |
| ML / DS | none; demand forecasting is bought from a category contractor |
| Warehouse | exists, populated by the contractor |
| BI tool | legacy product of a vendor that left in 2022; a domestic replacement is being piloted in parallel |
| Semantic layer | none; metric definitions live inside the SQL of individual reports |
| Data catalog | none |
| AI assistant | none; ChatGPT tried for one-off tasks |

## Analytics demand

**Key consumers:** commercial director and category managers · logistics director · CFO · regional directors.

**How it works today.** Executives receive Excel extracts; some open dashboards. Category analysts build their own reports when their skill allows, otherwise they go to the BI team or the contractor. Which executives actually use what — **nobody knows, no usage statistics are collected**.

## What hurts — in participants' own words

> "And yes, average basket doesn't match between categories and finance. Every committee starts with a reconciliation."

> "Any new data mart is a ticket to the contractor. Two or three weeks and a separate invoice. The analysts gave up and pull extracts instead."

> "We argue about a metric's logic and there is nobody to confirm it. Whoever is more persistent wins."

> "I can't tell you how many executives open the reports. We don't count it."

## Constraints

- **Next year's budget is not allocated**; the decision is made in November.
- IT hiring is frozen; exceptions are approved personally by the COO.
- The BI platform migration has already started and runs **outside the BI team's control**.
- The data contractor is the sole holder of knowledge about how existing data marts work.

## Pressure from above

The commercial director returned from an industry conference and wants **an AI assistant that answers questions about sales** — "like everyone has" — by the end of the quarter.

## The sponsor's request, verbatim

> "We need a three-year BI strategy. And show where the AI is in it, otherwise we won't get it approved."

## Why this case was chosen for the run

Every factor below breaks one of the knowledge base's assumptions. A comfortable case proves nothing.

| Factor | What it tests |
|---|---|
| Non-tech company with no in-house engineering | the base is built on material from large technology companies |
| Regulatory perimeter with personal data | the failure catalog has no family for regulated industries |
| Break at the first link of the chain | everything to the right is unreachable — does the skill still propose AI first? |
| Direct pressure for "AI by end of quarter" | does the kill-gate survive the sponsor's request? |
| No allocated budget | does an explicit ask to the sponsor appear instead of a list of work? |
| Migration outside the team's control | how the method handles a dependency the team does not own |
