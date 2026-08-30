# BI+AI Strategy — Severnaya Pharmacy Chain

> Fictional company · three-year horizon · draft 1.1, after the gates · 2026-08-29
> ⚠️ A demonstration artifact of the skill. Figures are placeholders `<•>`; baselines are marked `[requires clarification]`.

## Where we are going

Within three years, decisions on purchasing, pricing and logistics are made on the same numbers — not on extracts each function computes its own way. Category analysts take data from a ready layer instead of ordering a data mart from the contractor and waiting weeks.

This is not about the tool. The tool will change during the migration; the value is created by a described and maintained data layer that outlives the platform switch.

## Which problems we are closing

| Problem | Who it hits | → |
|---|---|---|
| One metric is computed differently in categories and in finance | commerce, finance | [[01-Context#P1 · Metrics disagree]] |
| Every new data mart goes through the contractor: weeks and a separate invoice | all analysts | [[01-Context#P2 · Data marts via the contractor]] |
| No data owners — nobody to confirm the logic | the whole company | [[01-Context#P3 · No data owners]] |
| Nobody knows which executive uses what | BI team | [[01-Context#P4 · Usage is not measured]] |
| Loyalty personal data sits in the same marts as sales | compliance | [[01-Context#P6 · Personal data inside sales marts]] |

## Streams of change

| Stream | In one line | Owner |
|---|---|---|
| **S1 · Trusted data** | our own marts for sales and stock instead of tickets to the contractor | Head of IT |
| **S2 · Metric layer** | one definition per metric for the whole company, fixed in code | Head of BI |
| **S3 · Governed self-service** | category analysts work on certified sources themselves | Head of BI |
| **S4 · Platform migration** | move to the domestic BI tool without rewriting the logic from scratch | Head of IT |
| **S5 · Separating sensitive data** | loyalty personal data separated from sales in the model and in permissions | Compliance + IT |

→ in detail: [[02-Streams]]

## What we deliberately do not do

- **An AI sales assistant this year.** Not because it is unnecessary, but because there is nothing for it to answer from: no certified core, no metric layer. An assistant on today's data will confidently return wrong numbers, and that costs more than its absence. The opening gate is stated in [[04-Goals]].
- **A data catalog as a separate project.** While there are fewer than a hundred objects worth cataloguing, a register in the wiki is cheaper than a platform.
- **A data literacy programme.** We return to it once analysts have something to work with on their own.

## What we need from the sponsor

**One decision in November, before the budget cycle:**

1. **A data engineer on staff**, 1 FTE. Without one, the strategy stays a work plan for the contractor rather than a change in the company.
2. **An owner for the "sales" domain from commerce** — a name, 20% of their time, the authority to confirm metric logic.

Neither is money for tools. Both are people. The tooling side is covered inside the migration that is already running.

## First step and the cost of inaction

**90 days:** a register of master data sources for sales and stock · an adoption baseline for focus roles · agreed definitions for three disputed metrics.

**Cost of inaction:** the company enters the BI platform migration with undescribed data marts. The migration then becomes a rewrite of the logic from scratch, done by the same contractor at the price of a new project — and what comes out is the same untangled model on a new tool.

## Navigation

[[00-Company-profile]] · [[01-Context]] · [[02-Streams]] · [[03-Initiatives]] · [[04-Goals]] · [[05-Risks]] · [[appendix/90-Diagnostics|Diagnostics]] · [[appendix/91-Analysis-frame|Analysis frame]]
