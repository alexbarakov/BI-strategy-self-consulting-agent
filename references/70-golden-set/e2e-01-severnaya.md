---
id: e2e-01-severnaya
type: end-to-end-run
purpose: an end-to-end FORM run on an invented company - what is tested is the skill, not the document
company: "Severnaya Apteka" (invented)
date: 2026-08-29
---

# End-to-end run 01 - "Severnaya Apteka"

Golden set tiers 1-3 test recall of knowledge. This file tests what the skill exists for: **does a defensible strategy come out of it**. The case was chosen to be awkward on purpose - a convenient one shows nothing.

---

## Part 1. The inputs

**The company.** A regional pharmacy chain, 620 stores across seven regions, 4,800 employees. Not a technology company: IT is a support function reporting to the operations director.

**What makes the case awkward:**

| Factor | Value |
|---|---|
| Industry | regulated: pharmaceutical circulation, labelling, customer personal data in the loyalty programme |
| BI stack | a legacy system whose vendor left in 2022; a Russian replacement is being piloted in parallel |
| Warehouse | exists, but the marts are built by a contractor on request; there is no in-house engineering team |
| BI team | 3 people centrally plus ~15 analysts across the categories and logistics, at varying levels |
| Data governance | neither a team nor a role |
| Semantic layer | none; the metrics live in the reports' SQL |
| Adoption | nobody measures it; "the executives look at Excel extracts" |
| Pressure from above | after a conference, the commercial director wants "an AI helper that answers questions about sales" - by the end of the quarter |
| Budget | not allocated for next year; the decision comes in November |

**The requester's ask, verbatim:** "We need a three-year BI strategy. And show us where the AI is in it, or we will not get it approved."

---

## The artifact

The strategy itself is in the folder [`e2e-01-severnaya/`](e2e-01-severnaya/): the company portrait as the input, the document's six sections, two appendices, and the build into one portable file, [`strategy.html`](e2e-01-severnaya/strategy.html). It is assembled by `build-html.py` with no dependencies.

The folder holds the version **after the gates** - the one that passed the requirements check and the judge. What follows analyses how it differed on the first pass.

## Part 2. What the skill produced on the first pass

A draft across the six sections. Abridged here - what matters in full are the phrasings the gates later acted on.

### index - the vision

> **Where we are going.** In three years, decisions about purchasing, pricing and logistics are made on the same numbers rather than on extracts each function computes its own way. Category analysts get their data from a ready layer instead of assembling it through requests to a contractor.
>
> **The problems we are closing.** Metrics diverge between the categories and finance · the time from a question to a number is measured in days because it goes through the contractor · nobody knows which executives use what.
>
> **The streams:** trusted data · the metric layer · governed self-service · the platform migration.
>
> **What we deliberately are not doing.** An AI sales assistant this year. The reason is below, in the goals section.
>
> **What is required from the sponsor.** A decision in November: a dedicated data engineer on the payroll and an owner for the "sales" domain from the commercial side - at 20% of their time, named.
>
> **The first step and the cost of inaction.** 90 days: a registry of master sources for sales and stock, and an adoption measurement. Doing nothing, the company enters the BI platform migration with no documented marts, and the migration turns into rewriting the logic from scratch.

### 01 - Context

Trends: the shift from dashboards to natural-language questions · the semantic layer as a precondition of agent accuracy · regulatory pressure on personal data · vendors leaving and the forced migration · the rising share of self-service in mature companies.

Problems across the four role groups: metrics diverge · dependence on the contractor for any mart · no data owners · no measurement of usage · category analysts at varying levels · loyalty personal data sits in the same marts as sales.

Breaks in the chain: **no core layer** (marts are built per task) · **no semantics** · context does not exist as a class.

### 02 - Streams

Four: trusted data · the metric layer · governed self-service · the platform migration. Each with a description, a justification linked to a problem, boundaries and an owner.

### 03 - Initiatives

Nine initiatives tagged by stream, with outputs and outcomes by year, and kill-gates.

### 04 - Goals

Metrics across the four groups, with baselines mostly marked `[to be clarified]`.

### 05 - Risks

The fragility of the chain · the contractor as a single point of failure · governance with no resource · the migration eating a year · a change of priority after November.

---

## Part 3. Gate 0 - the requirements check

A pass against `strategy-requirements.md`. **Five findings, two of them blocking.**

### Disqualifiers

| Sign | Result |
|---|---|
| Streams with no justification | passed |
| Initiatives with no outcome | **VIOLATED** - three of nine carry only an output |
| Goals with no baseline | formally passed: marked `[to be clarified]` |
| Initiatives with no owners | **VIOLATED** - two name "the BI team" rather than a person |
| Trends with no consequences | passed |
| A vision with no ask of the sponsor | passed |
| Numbers with no source | passed |
| An AI initiative ahead of its link in the chain | passed - the assistant is put beyond the horizon with an explicit reason |
| No freeze list | **VIOLATED** - it was absent |
| The text transplants to another company | passed |

**Three violations -> the document went back for rework and never reached the judge.**

### Definition of done

Items 7 (an output and an outcome by year for every initiative) and 10 (the freeze list) were unmet, and 6 partially (two problems were not covered by a stream and not listed explicitly).

### Traceability

Running it in both directions found two orphans:
- the problem "loyalty personal data sits in the same marts as sales" is not covered by any stream and is not named as deliberately uncovered;
- the initiative "training the category analysts" is not tied to any problem - it got into the plan by inertia.

### Sharpness of wording

Two phrasings failed the portability test: "raise data quality across the key domains" and "develop the data culture". The first was rewritten as "cover the sales and stock marts with data contracts, with a freshness threshold of one day"; the second was deleted, because there was neither an initiative nor a metric behind it.

### After the rework

The violations were closed: outcomes added, owners named individually, the freeze list published, the personal data problem turned into a fifth stream, "separating sensitive data", and the training initiative tied to the self-service stream. **Gate 0 passed on the second attempt.**

---

## Part 4. The judge

Seven dimensions. Three findings, one blocking.

**Blocking - priority.** The strategy answers the pain "metrics diverge", but the company's most expensive pain is a different one: **dependence on the contractor**, which makes any mart cost weeks and contractual money. A metric layer on top of a contractor model will speed nothing up. → The stream order was rebuilt: "trusted data" and in-house engineering competence move ahead of the metric layer.

**Serious - feasibility.** Nine initiatives for a team of three plus a contractor. Even with the engineer hired, the first year realistically closes three. → Six were moved into years two and three explicitly rather than dissolved into "the roadmap".

**Worth fixing - defensibility.** The document does not answer "what is this in money". → A caveat was added: the economic effect is computed separately, before the November decision, and the three lines where it can exist at all are named.

**The judge's verdict:** "I would sign this as it stands - provided the engineer's hire is confirmed before the start. Without that it is a work plan for the contractor, not a company strategy."

---

## Part 5. What the run said about the skill itself

The main result of the test. Five findings, four of them about the base rather than the document.

**1. Regulated industries are not covered.** The loyalty personal data problem only surfaced during the traceability check. The failure catalog has no family for regulation - that is already recorded in `kb/60-roadmap.md` as B3, and the run confirmed it in practice: the skill did not propose it, the gate found it.

**2. The field benchmark does not apply and misleads.** The n=12 sample is technology companies with teams of 10-400 analysts. For a pharmacy chain, "a median warehouse team of ~12" reads as a norm they do not have and never will. The atom needs a caveat: the benchmark is valid for the tech perimeter, and for non-tech it inflates expectations.

**3. The contradiction about the ad-hoc ceiling showed up.** Asked "how much will the assistant close", the base gives 70-80% (participants' self-assessment) and 15-25% (the practical ceiling). For a company with no semantics the honest answer is closer to the lower bound, but the base has no rule for choosing between them - only the two figures side by side. A rule is needed: **with no semantic layer, take the lower bound**.

**4. The contractor delivery model for marts is described nowhere.** The whole base assumes the marts are built by an in-house team. A company whose engineering is outsourced is a common case, and there is neither an atom nor a line in the failure catalog for it. This is a new roadmap item.

**5. The absence of an economic model is noticeable.** The judge raised it as a finding, and it had to be worked around with a caveat. The decision not to build a twin skill stands, but the requirements should say explicitly what to do when the money question is asked: the three lines where an effect is possible, and an honest "the rest is not computed".

---

## Part 6. The run's verdict

| What was tested | Result |
|---|---|
| The skill assembles a document across the six sections | yes |
| Gate 0 catches defects mechanically | yes - three disqualifiers and two orphans on the first pass |
| Gate 0 does not let the document reach the judge before it is fixed | yes |
| The judge finds what a checklist cannot | yes - the wrong stream priority |
| The document passes after rework | yes, on the second attempt |
| The base covers an awkward non-tech case | **partially** - four gaps, see part 5 |

**The main conclusion.** The mechanism works: the gates caught exactly what they were built for, and in the right order - the cheap check removed five findings before the judge reached them, and the judge spent its effort on what a checklist cannot catch.

**The main defect.** The knowledge base is skewed towards a large technology company with its own engineering. On a case with no in-house development team and inside a regulatory perimeter, the skill produces a correct frame but suggests thresholds and practices that do not fit that company. The cure is not new atoms about AI but caveats about the boundary of applicability on the existing ones.
