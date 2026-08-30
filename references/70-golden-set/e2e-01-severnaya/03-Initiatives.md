[[index|← BI+AI Strategy]] · 🏢 Severnaya

# 03. Projects and initiatives

**Output** — what was built, verified by its existence. **Outcome** — what changed, verified by measurement.
An initiative without an outcome is work, not an initiative.

> ⚠️ Year 1 is concrete. Years 2 and 3 are indicative and will be refined at the six-month re-assembly.

| Initiative | Streams | Owner | Year 1 | Year 2 | Year 3 | Metric | Kill-gate |
|---|---|---|---|---|---|---|---|
| **Master data source register** for sales and stock | `S1` | Head of IT | A: register of ~15 objects, each with an owner and a schedule<br>O: share of analyst queries hitting register objects `<•>`% | A: register covers logistics<br>O: `<•>`% | — | share of queries on register objects | if after a quarter the share is below `<•>`%, the wrong objects were picked — rebuild the list from actual usage |
| **Data engineer on staff** | `S1` | Head of IT | A: hired and onboarded<br>O: share of marts built without the contractor `<•>`% | A: second role if the load is confirmed<br>O: `<•>`% | — | share of marts built in-house | **strategy gate:** not hired by March — S2, S3 and S4 are postponed and the strategy is re-assembled |
| **Data contracts on sales and stock** | `S1` | data engineer | A: contracts on 5 key objects, freshness threshold 24h<br>O: "data did not refresh" incidents `<•>` per quarter | A: coverage of the whole register<br>O: `<•>` | — | freshness incidents | — |
| **Adoption baseline** | `S1` | Head of BI | A: usage statistics collected, report by focus role<br>O: baseline fixed | A: quarterly review<br>O: focus-role share `<•>`% | O: `<•>`% | % of focus roles opening BI monthly | — |
| **Definitions of three disputed metrics** | `S2` | Head of BI | A: average basket, turnover and margin agreed and signed off by the domain owner<br>O: discrepancy between reports eliminated | A: `<•>` more metrics<br>O: — | — | metrics with a signed definition | if no domain owner is named by April the stream stops rather than being agreed "de facto" |
| **Metric layer on top of the register** | `S2` | data engineer | — | A: metrics computed in one place<br>O: share of reports on the layer `<•>`% | A: coverage of key domains<br>O: `<•>`% | share of reports using the layer | — |
| **Separating loyalty personal data** | `S5` | Compliance + IT | A: model split, permissions cut, analyst sees segments without identifiers<br>O: access to personal data only for roles in the matrix | A: permission audit<br>O: — | — | roles with access to personal data | **blocking:** self-service is not opened until this completes |
| **Self-service pilot in one category** | `S3` | Head of BI | A: one category working on certified sources<br>O: ad-hoc requests from that category at `<•>`% of today | A: `<•>` more categories<br>O: `<•>`% | A: scale-out<br>O: `<•>`% | share of ad-hoc closed by analysts themselves | if ad-hoc does not fall after the pilot, the cause is the data rather than access — return to S1 |
| **Migration to the new platform** | `S4` | Head of IT | A: move the reports built on the register | A: move the rest<br>O: legacy decommissioned | — | share of reports on the new platform | do not migrate objects outside the register — moving the untangled costs more than describing it |

## First 90 days

1. Master data source register for sales and stock — Head of IT, checkpoint 15 November
2. Adoption baseline for focus roles — Head of BI, checkpoint 1 December
3. Agreement on three disputed definitions — Head of BI, checkpoint 15 December
4. Hiring decision for the engineer — sponsor, November budget cycle

> **Deliberately not in the first 90 days:** anything from S2, S3 or S4. Until the hire is confirmed, starting them creates commitments there is nothing to meet.
