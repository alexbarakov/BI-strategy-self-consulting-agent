# Requirements for the structure and content of a BI+AI strategy

An acceptance spec for the deliverable. It answers two questions: **when a section can be considered written**, and **what makes a document unacceptable**.

Six document sections plus a cross-cutting requirement on language. The order of sections is the order of reading, not the order of work: the analysis runs on the seven-block frame (`strategy-template.md`), and what the reader gets is what follows.

---

## Requirement 0. Precision of wording

Applies to every sentence in the document. This is not style: a vague formulation does not survive a committee and does not turn into a task, which makes it more expensive than an absent one.

### Six tests

| Test | The wording fails if |
|---|---|
| **Portability** | the sentence could be pasted into another company's strategy unchanged |
| **Quotation** | the claim falls apart once lifted out of its paragraph and quoted at a committee |
| **Adjective** | an adjective stands without a number or a consequence: "significant growth", "high quality", "low maturity" |
| **Monday** | after reading the section it is unclear what to do on Monday, and by whom |
| **Read aloud** | the phrasing is awkward to read out to a sponsor because it asserts nothing |
| **Arguability** | the claim cannot be disputed — which means it says nothing |

### Ban list

Phrases to delete or extend into something checkable: "improve efficiency" · "improve data quality" · "build a data culture" · "ensure transparency" · "synergy" · "optimize processes" · "accelerate time-to-insight" without saying for whom and from what to what · "establish processes" without saying which.

### Writing rules

- One sentence, one idea. A term is defined at first use.
- A number instead of an estimate of quantity: not "many dead reports", but how many.
- Every figure carries a reliability tag: `measured` / `benchmark` / `vendor` / `author-estimate` / `disputed`. The tag travels with the number.
- Missing data is recorded as `[requires clarification]` naming the source that would close it. An inspiring number placed to fill a hole will outlive the strategy and be quoted for a year.
- The document is written in the company's language. The method's material is a source, not an output template.

---

## Section 1. Context

Two subsections, both mandatory. The section answers "why now", and neither subsection answers it alone: trends without problems are a market review, problems without trends are an operations report.

### 1.1 External context: trends

**Minimum required:** five to eight trends, each with a source and an evidence level · for each — **what follows from it for us**.

**Sign it is complete:** every trend carries a consequence line tied to our situation. A trend without a consequence is deleted — it takes space and makes the document look like it is about the market.

**The usual substitution:** a retelling of vendor forecasts. A figure tagged `vendor` may appear, but with the measurer named, and it is never grounds for an initiative.

### 1.2 Internal context: problems

**Minimum required:** problems collected **across four role groups** — the central team, analysts in domains, the data management team, casual users · for each: symptom, evidence, **cost of inaction** · a 0–4 maturity scorecard · the two or three named breaks in the chain `core → semantic → context → AI accuracy → self-service`.

**Sign it is complete:** the problem is phrased so that it can be put to an owner who will either agree or dispute it with a fact. Each carries a cost of inaction, qualitative at minimum.

**The usual substitution:** pains collected only from your own team — then the strategy answers the most *interesting* pain rather than the most *expensive* one. The second substitution: "low maturity" instead of named breaks.

---

## Section 2. Vision — the summary

**It reads standalone.** The test is simple: someone who read only this section must understand where we are going, what we are solving and what is wanted from them.

**Minimum required:** where we are going and what that looks like at the planning horizon · which problems from section 1 we close · the streams, one line each · **what we deliberately do not do, and why** · **what decision is required from the sponsor** · the first step · the cost of inaction.

**Length:** one page. A section that does not fit on a page is not a summary.

**Sign it is complete:** there is an explicit ask of the sponsor — money, people, authority or a decision. A vision without an ask requires no answer and therefore does not get one.

**The usual substitution:** an inspiring paragraph about becoming a data-driven company. It fails the arguability test.

---

## Section 3. Streams of change

A stream is a direction of change uniting initiatives under one logic and one owner. There are usually four to seven: fewer is not a structure, more is not a set of priorities.

**Mandatory per stream:**

| Field | Requirement |
|---|---|
| Name | names the change, not the area: "moving consumption onto trusted objects", not "data" |
| Description | what changes and what the result looks like |
| **Justification** | which problem from 1.2 it closes and which trend from 1.1 it addresses — **by reference, not by implication** |
| Boundaries | what is deliberately out of scope |
| Owner | a name |
| Position in the queue | its place in the stack-rank and what freezes first under a cut |

**Traceability is required both ways:**
- every stream references at least one named problem;
- every significant problem is covered by at least one stream, and those left uncovered are listed explicitly with a reason.

**Sign it is complete:** the justification answers "why this stream rather than another", instead of describing its contents a second time.

**The usual substitution:** streams named after architecture layers or after the sections of a guide. That is a table of contents, not a set of changes.

---

## Section 4. Projects and initiatives

The portfolio. A table, because it exists to be compared and cut, not read end to end.

**Mandatory columns:**

`initiative` · `stream tags` · `owner` · `output by year` · `outcome by year` · `metric` · `kill-gate` · `dependencies`

### Output and outcome are kept strictly apart

- **Output — what was built.** A data mart, a policy, a dashboard, a trained group, a launched service. Verified by its existence.
- **Outcome — what changed.** A share of queries, a duration, people's behaviour, load removed. Verified by measurement.

An initiative without an outcome is work, not an initiative, and it enters the portfolio only as another initiative's dependency.

### Horizon requirements

Output and outcome are stated **by year** across the horizon. Year one is concrete; later years are indicative and marked as such. An outcome placed in year one without a baseline at the start does not count: there will be nothing to close it against.

### Other requirements

- Stream tags are multiple: an initiative may serve two streams, but it must not serve all of them.
- Every AI initiative carries a **kill-gate with a threshold measured on your own data**.
- Dependencies are named explicitly; an initiative standing ahead of its link in the chain is moved or gated.
- The outcome of an initiative references a goal from section 5 rather than introducing its own metric.
- An initiative without an owner is a line in a plan, not a change.

**The usual substitution:** the team's task list for the year, tagged after the fact. The tell: the initiatives have outputs only, no outcomes.

---

## Section 5. Goals as metrics

A goal is stated as a metric, not in words. A verbal goal belongs in section 2; only the measurable belongs here.

**Format per goal:** `metric` · `baseline` · `target` · `deadline` · `owner` · `how it is measured`.

**Mandatory requirements:**

- **A baseline is required.** With no measurement, the goal stays `[requires clarification]` until one exists rather than being replaced by a plausible number.
- Metrics cover the four groups: engagement · quality of service · process quality · business impact. Selection is **five primary and five secondary**; the rest are not taken.
- **+1 maturity level per year is the honest default.** A larger shift requires a named reason: funded capacity, an already-financed platform change, a regulatory deadline.
- Every goal is discounted against three risks: dependency on someone else's delivery, capacity, and the need to change people's behaviour.
- **The effect of AI is not measured by the team's self-assessment** — only by measurement against a golden set with a baseline fixed before the start.
- For every metric, name the ceiling and the "enough" mark: where the practical limit is and where the return flattens.

**Order rule.** The section is read after the portfolio but **formulated before it**: a goal exists independently of an initiative. Test — remove the initiative: the goal must remain. If it does not, it is not a goal but a description of work, and it belongs in section 4. A section 5 that turns out to be the sum of section 4 means the goals were derived from the plan rather than the plan from the goals.

**The usual substitution:** a metric without a baseline, and a metric that measures activity rather than result — call counts instead of solved tasks, certified objects instead of the share of consumption on them.

---

## Section 6. Risks

**Format:** `risk` · `likelihood and impact` · `mitigation` · `owner` · `trigger` — the observable sign that tells you it has materialised.

**Categories that must be considered** (included, or explicitly dismissed with a reason):

- the fragility of the chain: AI depends on semantics, semantics on the core, the core on the catalog and its owners;
- agents multiply the existing disorder rather than compensating for it;
- governance declared without an allocated resource;
- a key domain resting on a single person;
- losing part of the resource mid-year;
- a change of sponsor or of priority from above.

**A mandatory artifact of this section: the freeze list.** What dies first if a third of the resource is lost — published in advance, not drawn up at the moment of the cut. A strategy without a rehearsed cut does not survive the first budget review: it fails quietly everywhere at once.

**Sign it is complete:** every risk has a trigger. A risk without one will not be noticed in time.

**The usual substitution:** a risk register as a formality — "insufficient funding", "resistance to change" — with no mitigations and no owners.

---

## Cross-cutting traceability

The chain along which the document's integrity is checked:

```
trend (1.1) ─┐
             ├─→ stream (3) ─→ initiative (4) ─→ goal as metric (5)
problem (1.2)┘                     │
                                   └─→ risk (6) ─→ freeze list
```

**The orphan rule.** Every element of the document must be reachable along this chain. An element attached to nothing is either deleted or given an explicit reason to be there.

Checked in both directions: top-down, is every problem covered; bottom-up, is every initiative justified.

---

## Definition of Done

The document is ready to defend when all twelve hold.

1. Both context subsections are filled; every trend has a consequence, every problem a cost of inaction
2. Two or three chain breaks are named, rather than "low maturity overall"
3. The vision reads standalone, fits one page and contains an explicit ask of the sponsor
4. There is a "what we deliberately do not do" section with reasons
5. Every stream has a justification referencing a problem or a trend
6. Two-way traceability has been run; uncovered problems are listed explicitly
7. Every initiative has an owner, stream tags, and output and outcome by year
8. At least one AI initiative has a kill-gate with a threshold on your own data
9. Every goal has a baseline or a `[requires clarification]` marker
10. Every risk has a mitigation, an owner and a trigger; the freeze list is published
11. The wording pass is done: no phrases from the ban list remain
12. The judge stage is complete, blocking findings fixed or turned into explicit decisions, with before → after shown

---

## Disqualifiers

Any one of these sends the document back regardless of its size.

- **Streams without justification** — a set of directions unconnected to the problems.
- **Initiatives without outcomes** — a portfolio of work instead of a portfolio of change.
- **Goals without baselines** — nothing to close them against.
- **Initiatives without owners** — none of them will be done.
- **Trends without consequences** — a market review presented as context.
- **A vision without an ask of the sponsor** — it requires no answer and will not get one.
- **Figures without sources**, or vendor numbers presented as fact.
- **An AI initiative ahead of its link in the chain** without an explicit gate.
- **No freeze list.**
- **The text transfers to another company unchanged** — which means it is not about yours.

---

## What the document need not contain

- **A retelling of frameworks.** DAMA, TDWI and the rest are a source of structure, not the content of sections; a reference is enough.
- **A full catalog of practices.** Take three to five with a named driver; mark the rest as deliberately not taken.
- **Technical specifications.** The strategy names the decision and its justification; the detail lives in project documentation.
- **An economic model as a mandatory section.** It is needed when a budget is being defended; its absence does not make the strategy incomplete, but it does require an answer to why there is no business case. **If the "how much money is this" question is asked directly** — name the three lines where an effect is possible for BI at all (infrastructure freed · stopping production of content nobody reads · attaching to already-funded business cases) and say honestly that the rest does not count. "We will calculate it later" without that list reads as no answer.
- **A single hierarchical metric tree.** Metrics form a network; build links and levels, because a strict hierarchy will not hold.
- **A description of all seven blocks of the analysis frame.** The frame is an instrument; the document carries the result, not the working.

---

## Relationship to the analysis frame

`strategy-template.md` describes **how to analyse** — seven blocks from the business foundation to change management. This spec describes **what to show**. They map onto each other like this:

| Block of the frame | Where it lands in the document |
|---|---|
| 1. Business foundation · 2. Landscape assessment | Section 1.2 — internal context |
| 3. Target operating model | Section 3 — as its own stream, or as the frame for several |
| 4. Process foundation · 5. Technology · 6. Operations | Sections 3 and 4 — distributed across streams and initiatives |
| 7. Change management | Sections 4, 5, 6 — portfolio, goals, risks |
| Cross-cutting artifacts | Section 2 (stack-rank), 5 (metric tree), 6 (risk register and freeze list) |

A block of the frame that reaches no stream is either unfinished analysis or a deliberate decision not to touch that area. The second is recorded under "what we do not do".
