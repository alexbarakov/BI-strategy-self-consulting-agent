[[index]] · Company profile

# Vantage Mobility — the input to the run

> A fictional company. The profile is the synthetic interview transcript the FORM run was executed against.

## The company

A car-subscription scale-up: customers take a car on a monthly subscription instead of buying or leasing it. Founded 2019, 1,300 employees, live in 11 European countries. Series D, an investor day held in June 2026.

Not a company with a data problem in the usual sense. Engineering is strong, the warehouse is modern, and every product squad has its own analyst. The problem is that nothing means the same thing twice.

## What makes the case awkward

| Factor | Value |
|---|---|
| Engineering | strong: own platform, dbt, CI/CD, tracing, an MCP layer built in-house |
| Analysts | ~40, embedded in product and ops squads, reporting into the squads |
| Central BI | 6 people, a **platform** team — they do not build reports for the business |
| Data governance | 1 person at 50% of their time, no mandate, no policy signed |
| Semantic layer | none. Metric logic lives in dbt models, in the BI tool's own layer, and in the assistant's few-shot examples |
| Trusted core | 3 domains of 11 |
| **AI assistant** | **already in production, 8 months, ~400 business users** |
| Assistant usage | 31% of ad-hoc questions go to it first — measured **by call volume**, not by correctness |
| Trust | falling: ops leads keep parallel spreadsheets because the assistant and the dashboard disagree on "active subscriptions" |
| Assistant identity | runs under one service account with read access to the whole warehouse |
| Eval | none. No golden set, no accuracy measurement, no refusal path — it answers everything |
| Content | ~900 dashboards, no certification, no archiving, no owner field |
| Headcount | **frozen** until the next funding round |
| Tooling budget | exists — the assistant is already paid for |
| **Public commitment** | at the June investor day the CPO announced: **"50% of ad-hoc analytics handled by AI by the end of 2027"** |
| Deadline | a board review in four months will ask for progress against that number |

## The requester's ask, verbatim

> "We already have the AI. We need the strategy that makes it work, and we need it to line up with what we told the market. Do not tell me to switch it off."

## Self-assessment, 0–4 (collected in the interview)

| Category | Now | Target in a year |
|---|---|---|
| 1 · Connection with business | 2.5 | 3 |
| 2 · Adoption and satisfaction | 2.0 | 3 |
| 3 · BI content management | 1.5 | 2 |
| 4 · Self-service delivery | 3.0 | 3 |
| 5 · Guided delivery / support | 1.5 | 2 |
| 6 · BI platform governance | 1.5 | 2.5 |
| 7 · Data quality management | 2.0 | 3 |
| 8 · Security and compliance | 2.5 | 3 |
| 9 · Project management | 3.0 | 3 |
| **AI readiness (overlay)** | **1.4** | **2.5** |

Scored by the head of the data platform together with the head of analytics; the two disagreed on category 2 and settled on the lower number, because adoption of the assistant is measured by calls.

## What was measured and what was not

**Measured:** the number of dashboards (912) · the number of assistant calls and their growth · the share of ad-hoc questions starting in the assistant (31%) · the three competing definitions of "active subscription" (found by hand during the interview).

**Not measured:** the assistant's accuracy · how many ops leads keep parallel spreadsheets · the share of queries hitting certified objects · time from question to trusted answer.

Everything in the second list becomes `[requires clarification]` in the goals, and the first 90 days exist to close it.

---

→ [[index]] · [[01-Context]] · [[appendix/90-Diagnostics|Diagnostics]]
