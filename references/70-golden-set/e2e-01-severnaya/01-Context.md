[[index|← BI+AI Strategy]] · 🏢 Severnaya

# 01. Context

## 🌍 External context: trends

| Trend | Reliability | What follows for us |
|---|---|---|
| Text-to-SQL accuracy on real enterprise schemas is around 40%; with a semantic layer 85–95%, and on an uncovered question the system refuses honestly instead of inventing | `benchmark` | An assistant without a metric layer will return a plausible wrong answer. For us this sets the order: the layer before the assistant, not alongside it |
| Model answer quality degrades as the supplied context grows, well before the window is full | `benchmark` | "Load all our reports into the AI" does not work as a solution. Context has to be selected, which means it has to be described |
| Market priorities for 2026 put data quality and security above AI and GenAI | `benchmark` | Our investment order matches the industry one — that is defensible to the board |
| Foreign vendors leaving and forced BI platform migrations | `measured` | Our migration is already running. It will either cement the current mess on a new tool, or become the occasion to describe the model |
| Regulatory pressure on personal data processing | `measured` | The loyalty programme makes us a personal-data processor. Separating the data is a requirement, not hygiene |

## 🏠 Internal context: problems

Collected across four role groups.

### P1 · Metrics disagree

**Group:** analysts in domains, finance. **Evidence:** three different values of "average basket" in category, finance and marketing reports for the same period; the discrepancy is discussed at every commercial committee. **Cost of inaction:** promotion decisions are taken on a number the participants do not consider shared; committee time goes to reconciliation instead of decisions.

### P2 · Data marts via the contractor

**Group:** all analysts. **Evidence:** time from ticket to data mart `[requires clarification — export from the ticketing system]`; analysts say "two or three weeks". Every change is billed separately. **Cost of inaction:** analysts bypass the process and assemble data through extracts, which reproduces the metric discrepancy on the next turn.

### P3 · No data owners

**Group:** data management (does not exist as a function). **Evidence:** not a single domain has a named owner; a dispute about metric logic is settled by whoever is more persistent. **Cost of inaction:** there is physically nobody to agree a metric definition with, which makes the metric layer impossible to build — this blocks S2.

### P4 · Usage is not measured

**Group:** central BI team. **Evidence:** report usage statistics are not collected; the question "how many executives open reports at least monthly" has no answer. **Cost of inaction:** dead reports cannot be told from needed ones, so support can neither be reduced nor justified.

### P5 · Analyst skill varies widely

**Group:** analysts in domains. **Evidence:** fifteen people, from confident SQL to manual Excel. **Cost of inaction:** self-service opened to everyone at once produces a stream of reports of varying quality and adds untangled content on top of untangled data.

### P6 · Personal data inside sales marts

**Group:** compliance. **Evidence:** loyalty member identifiers are present in marts that category analysts can access. **Cost of inaction:** a finding at the first inspection, and no way to open self-service without widening access to personal data.

## 🩺 Diagnostics

Full scorecard — [[appendix/90-Diagnostics]]. In summary: no strong categories; content management and project management are mid-level; data management, data quality and governance are weak.

**Breaks in the chain `core → semantics → context → AI accuracy → self-service`:**

1. **No core layer.** Marts are built per task and never reused.
2. **No semantics.** Metric definitions live inside the SQL of individual reports.
3. **Context does not exist as a class** — and that is a consequence of the first two, not a separate problem.

The break is at the very first link. Everything to the right is unreachable while it stays open.

## What we deliberately leave uncovered

- **Mobile access to reports.** No demand; executives work from the office.
- **Demand forecasting.** The category contractor already provides it; we will not duplicate before a core layer exists.
