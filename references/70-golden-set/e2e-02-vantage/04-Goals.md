[[index]] · Goals

# 📊 Section 4. Goals as metrics

Five primary and five secondary. The rest of the catalog is not taken.

**Read this section after the portfolio, but note it was written before it.** Test: remove the initiative and the goal must still stand. G1 through G5 survive that test — they describe the state of the company, not the work.

## Primary

| # | Metric | Baseline | Year 1 | Year 2 *(ind.)* | Owner | How it is measured |
|---|---|---|---|---|---|---|
| **G1** | Assistant accuracy inside the perimeter, on the golden set | `[requires clarification]` — closed by I1, day 30 | ≥85% | `<•>` | Head of Analytics | 60 questions from real logs, judged against the certified source; re-run on every definition change |
| **G2** | Share of ad-hoc questions **answered correctly** by the assistant | `[requires clarification]` — the existing 31% is a call share and is not this metric | `<•>`, set once G1 exists | `<•>` | Head of Analytics | correct answers over questions asked, not calls over calls |
| **G3** | Competing definitions of the twelve board metrics | **3** `measured` | **1** | 1 | Head of Data Platform | a quarterly hand audit across dbt, the BI layer and the assistant's few-shots |
| **G4** | Share of in-perimeter answers carrying provenance | **0%** `measured` | 100% | 100% | Assistant PM | an automatic check on the answer payload |
| **G5** | Share of queries hitting certified core objects | `[requires clarification]` — closed by query-log analysis | `<•>` | `<•>` | Data Platform lead | query log tagged against the certified object registry |

## Secondary

| # | Metric | Baseline | Year 1 | Owner | Group |
|---|---|---|---|---|---|
| G6 | Honest-refusal rate on out-of-perimeter questions | 0% — it answers everything | ≥95% | Assistant PM | quality of service |
| G7 | Access reviews that can answer "who read what" | 0 of 1 | 1 of 1 | Data Platform lead | process quality |
| G8 | Certified domains | 3 of 11 | 4 of 11 | Data Platform lead | process quality |
| G9 | Dashboards with a named owner | `[requires clarification]` | `<•>` | Data Platform lead | process quality |
| G10 | Ops leads keeping a parallel spreadsheet | `[requires clarification]` — a shared-drive audit closes it | `<•>` | Head of Analytics | business impact |

## Metric groups

**Engagement** — deliberately thin this year. Adoption of the assistant is already high and is not the problem; measuring it harder would flatter us. **Quality of service** — G1, G4, G6. **Process quality** — G3, G5, G7, G8, G9. **Business impact** — G2, G10.

The skew towards process quality is intentional and is a statement about the year: the company is not short of usage, it is short of things being true.

## Ceiling and "enough"

- **G1 · accuracy.** Ceiling is not 100%. The published range with a semantic layer is 85–95% `benchmark`; a target above that on our own schema would be a promise nobody can keep. **Enough is 85% plus an honest refusal outside the perimeter** — the refusal matters more than the last five points.
- **G3 · definitions.** Ceiling is 1 per metric, and it applies to twelve metrics, not to all of them. Attempting all of them is how this stalls.
- **G5 · certified consumption.** No universal threshold exists. Measure the current value, take the median across domains and target the best quartile. A threshold lifted from another company is either unreachable or already passed.
- **G8 · certified domains.** +1 domain in year one. Not 11 of 11: the remaining five have no demand behind them yet.

## The discount applied

Each goal was moved before it was fixed.

| Risk | Which goals it hit | What changed |
|---|---|---|
| **Dependency** — needs somebody else's delivery | G1, G2 | both depend on the CPO agreeing to restate the number. If that does not happen, G2 is not achievable in any unit and the strategy says so rather than carrying a target it cannot own |
| **Capacity** — funded or living on goodwill | G3, G5, G8 | headcount is frozen. G3 dropped from 20 metrics to 12; G8 from 3 new domains to 1 |
| **Adoption** — requires people to change behaviour | G6, G10 | narrowing the assistant asks 400 people to accept fewer answers. G6 is stated as a system property (it refuses) rather than a satisfaction target, because satisfaction with a narrowing is not something to promise |

**+1 maturity level per year** is applied throughout. The one exception is AI readiness, targeted at 1.4 → 2.5, and the named reason is that the assistant already exists and is already funded: the work is defining and measuring, not building.

## The opening gate on expansion

The assistant's perimeter widens beyond the twelve metrics when all three hold:

1. G1 ≥ 85% sustained over two consecutive measurements;
2. the target domain is in the certified core (G8);
3. its metrics have a single definition with a named owner (G3).

**The kill-gate that applies after each widening:** if accuracy inside the new perimeter falls below 85% on the golden set two months in, the perimeter shrinks back. The threshold does not move to accommodate the result — that is the one rule that makes every other number here worth reading.

---

→ [[index]] · [[03-Initiatives]] · [[05-Risks]]
