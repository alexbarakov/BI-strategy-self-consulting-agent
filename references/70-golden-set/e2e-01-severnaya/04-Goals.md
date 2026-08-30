[[index|← BI+AI Strategy]] · 🏢 Severnaya

# 04. Goals as metrics

A goal is stated as a metric. Verbal goals live in [[index]]; only the measurable belongs here.

> **Order rule.** This section is read after the portfolio but **formulated before it**. Test: remove the initiative — the goal must remain. All goals below pass it: they describe a state of the company, not a volume of work.

| Stream | Metric | Baseline | Year 1 | Year 2 | Year 3 | Owner | How measured |
|---|---|---|---|---|---|---|---|
| S1 | Share of data marts built without the contractor | 0% | `<•>` | `<•>` | `<•>` | Head of IT | development backlog |
| S1 | Share of analyst queries hitting register objects | `[requires clarification]` | `<•>` | `<•>` | `<•>` | data engineer | query logs |
| S1 | "Data did not refresh" incidents per quarter | `[requires clarification]` | `<•>` | `<•>` | `<•>` | data engineer | data contracts |
| S1 | Time from ticket to data mart | `[requires clarification — export from the ticketing system]` | `<•>` | `<•>` | `<•>` | Head of IT | ticketing system |
| S2 | Metrics with a signed definition | 0 | 3 | `<•>` | `<•>` | Head of BI | glossary |
| S2 | Share of reports computing the metric through the layer | 0% | — | `<•>` | `<•>` | data engineer | report code |
| S3 | Share of focus roles opening BI at least monthly | `[requires clarification — measured in the first 90 days]` | `<•>` | `<•>` | `<•>` | Head of BI | platform statistics |
| S3 | Share of ad-hoc closed by the analyst alone | `[requires clarification]` | `<•>` | `<•>` | `<•>` | Head of BI | request log |
| S5 | Roles with access to personal identifiers | `[requires clarification — permission audit]` | `<•>` | `<•>` | `<•>` | Compliance | permission matrix |
| S4 | Share of reports on the new platform | 0% | `<•>` | `<•>` | 100% | Head of IT | inventory |

**Metric groups.** Engagement — focus-role share and share of self-served ad-hoc. Quality of service — time from ticket to data mart, freshness incidents. Process quality — metrics with a signed definition, share of reports on the layer. Business impact — share of marts built without the contractor (direct saving on the contract) and roles with access to personal data (regulatory risk removed).

## Ceiling and sufficiency

| Metric | Practical ceiling | Where the return flattens |
|---|---|---|
| Share of marts without the contractor | not 100%: legacy stays with the contractor until decommissioned | once sales, stock and logistics are covered |
| Share of focus roles in BI | not 100%: some executives get their numbers at the committee, and that is fine | at `<•>`% — beyond it the cost of engagement grows faster than the benefit |
| Metrics with a definition | not every metric, only the disputed and cross-functional ones | when committee arguments stop |

**Deliberate refusal.** We do not improve or measure the "data literacy" category in this horizon: without data people can work with on their own, training does not convert.

## Discounting the goals

Every goal is written down against three risks:

| Risk | What it discounts |
|---|---|
| Dependency on someone else's delivery | the platform migration runs outside BI's control; S4 goals and part of S1 depend on its timing |
| Capacity | all Year 1 goals assume one engineer is hired; without them only the adoption baseline is achievable |
| Adoption | S3 goals require analysts to stop making extracts, and that is not configured through permissions |

## Gate for opening the AI assistant

The sales assistant is placed beyond the horizon. **All three conditions must hold to reconsider:**

1. The master data source register covers sales and stock, with objects under data contracts
2. Key metric definitions are signed off by the domain owner and moved into the layer
3. A golden set of questions with known correct answers exists — at least several dozen

**Kill-gate after launch:** if accuracy on the golden set does not exceed `<•>`%, the assistant stays a draft tool for analysts and is not published to the business.

> The effect of AI is measured only on a golden set with a baseline fixed before the start. Team self-assessment and a feeling that "it got easier" are not evidence.

## If asked "how much money is this"

The economic model is built separately, before the November decision. Three lines where the effect is real for us:

1. **Stopping payment for data marts under the contract** — a direct saving that needs no attribution argument
2. **Stopping the production of reports nobody reads** — computable once adoption is measured
3. **Attaching to already-funded commercial initiatives** — the share is negotiated, not calculated

Everything else — faster decisions, "analyst time", higher quality — is not counted and does not enter the model.
