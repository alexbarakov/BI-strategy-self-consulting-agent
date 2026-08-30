---
id: e2e-02-vantage
type: end-to-end-run
purpose: an end-to-end FORM run on an invented company - the AI assistant is already in production ahead of its foundation
company: "Vantage Mobility" (invented)
date: 2026-08-30
---

# End-to-end run 02 — "Vantage Mobility"

Run 01 tested a company with neither a team nor tools. This one is the inversion: **strong engineering, forty analysts, and an AI assistant that has been in production for eight months ahead of its own foundation.** The kill-gate that would have stopped that launch was never applied, and the launch cannot now be undone.

The case was picked to attack four things run 01 never touched: a commitment already announced publicly, a hiring freeze, a hard external deadline, and a company with no centralized reporting to fall back on.

---

## Part 1. The inputs

Full profile: [`e2e-02-vantage/00-Company-profile.md`](e2e-02-vantage/00-Company-profile.md).

**The company.** A car-subscription scale-up, 1,300 people, 11 countries, Series D. Engineering is strong: own platform, dbt, CI/CD, tracing, an in-house MCP layer. Forty analysts embedded in squads. Central BI is six people and it is a platform team, not a report factory.

**What makes the case awkward:**

| Factor | Value |
|---|---|
| The assistant | **already in production, 8 months, ~400 business users** |
| Its measurement | 31% of ad-hoc questions start there — **by call volume, not correctness** |
| Its identity | one service account with read across the whole warehouse |
| Its context | few-shot examples, editable and unowned — the de facto semantic layer |
| Semantic layer | none. Three competing definitions of the twelve board metrics |
| Trusted core | 3 domains of 11 |
| Governance | 1 person at 50%, no mandate, no signed policy |
| Centralized reporting | effectively absent, and not going to be built |
| Headcount | **frozen** |
| **Public commitment** | announced at the June investor day: **"50% of ad-hoc analytics handled by AI by end of 2027"** |
| Deadline | a board review in four months will ask for progress against it |

**The requester's ask, verbatim:** "We already have the AI. We need the strategy that makes it work, and we need it to line up with what we told the market. Do not tell me to switch it off."

## The artifact

The strategy is in [`e2e-02-vantage/`](e2e-02-vantage/): the company profile as input, the six document sections, two appendices, and the single-file build [`strategy.html`](e2e-02-vantage/strategy.html). The folder holds the version **after the gates**; what follows is what the first pass looked like.

---

## Part 2. What the skill produced on the first pass

The draft came out structurally sound — six sections, five streams, eight initiatives — and it made three mistakes worth recording, because each is the kind a competent draft makes rather than a careless one.

**It used an available number as a baseline.** G2 read "raise the share of ad-hoc handled by the assistant from 31% to 80%". The 31% is a *call* share. Using it as the baseline for a correctness goal is exactly the substitution the skill's own rules forbid — and it happened because the number was there and looked like the right shape.

**It ordered the streams by rank rather than by calendar.** The semantic layer came first because the stack-rank puts trusted data ahead of AI readiness. Correct by the rank, wrong for a company whose board review is in four months and whose semantic work will not be finished by then.

**It quietly added a data catalog.** No problem in section 1 stood behind it. It entered because a catalog is what the material talks about a lot.

---

## Part 3. Gate 0 — the requirements check

Run against `strategy-requirements.md`. **Six findings, two blocking.**

### Disqualifiers

| Sign | Result |
|---|---|
| Streams without justification | passed |
| Initiatives without outcomes | passed |
| **Goals without baselines** | **VIOLATED** — G2 used a call share as the baseline for a correctness goal |
| Initiatives without owners | passed |
| **Trends without consequences** | **VIOLATED** — two of six trends carried no consequence line |
| A vision without an ask of the sponsor | passed |
| Figures without sources | passed |
| An AI initiative ahead of its link in the chain | passed — the assistant is already live, and the retroactive gate is explicit in S3 |
| No freeze list | passed |
| The text transfers to another company | passed |

**Two violations → returned for rework; it did not reach the judge.**

### Definition of Done

Failed: point 9 (a baseline or an explicit `[requires clarification]` for every goal — G2 had a wrong one, which is worse than a missing one) and point 1 (every trend carries a consequence). Point 10 passed partially: R6, the sponsor-change risk, had no trigger.

### Traceability

Both directions. Two findings:

- **An orphan initiative:** the data catalog pilot referenced no problem. Deleted, and moved into "what we deliberately do not do" so the deletion is visible rather than silent.
- **An uncovered problem:** P7, governance at 0.5 FTE with no mandate, was covered by no stream. Under a hiring freeze it cannot honestly be covered. Rather than declaring a governance function that nothing resources, it was recorded as **explicitly uncovered**, with the mandate narrowed to twelve metrics. That line is now the least comfortable one in [[02-Streams]] — and it is a correct outcome of the check, not a defect.

### Wording precision

Two phrasings failed the portability test: *"improve trust in data"* and *"establish processes for working with metrics"*. Both are on the ban list. The first became "reduce competing definitions of the twelve board metrics from 3 to 1"; the second was deleted — there was no initiative behind it.

### After rework

Baselines corrected to `[requires clarification]` with the closing source named; consequence lines added to T5 and T6; a trigger added to R6; the catalog deleted; P7 recorded as uncovered with a reason. **Gate 0 passed on the second attempt.**

---

## Part 4. The judge

Seven dimensions. Four findings, one blocking.

**Blocking — priority.** The document treats the semantic layer as the answer. But the company's most expensive problem is not that metrics disagree — it is that **it has publicly promised a number on a metric it has never measured**, and the board review is in four months. The semantic work will not be finished by then; a restated commitment can be. Quoted: *"S1 first, because trusted data outranks AI readiness."* Correct by the rank, and it loses the calendar.

→ **Rework:** S4 (honest measurement) moved ahead of S1 in time while keeping its lower rank, with the reason stated in [[02-Streams]] instead of hidden. Item 2 in the first 90 days — agree the restated commitment — moved to day 20, before any engineering starts.

**Serious — feasibility.** Five streams, eight initiatives, six platform people and a hiring freeze. Year one realistically closes two streams.

→ **Rework:** S2's domains 5–6 and all of S5 moved into year two explicitly and marked indicative, rather than being left to dissolve into "the roadmap".

**Serious — defensibility.** *"We narrow the perimeter"* has no number attached, and 400 users are about to get fewer answers. Executives will read it as a rollback and the strategy has no answer ready.

→ **Rework:** a section added to [[03-Initiatives]] — the cost of narrowing: what share of today's questions falls outside perimeter 1, where those questions go instead, and a turnaround for them. The number is `[requires clarification]` until day 30, and the narrowing is not announced before it exists.

**Worth fixing — honesty about risk.** Nothing in the register covered the assistant being right inside the perimeter while the eight domains outside it stay wrong — and looking equally authoritative to a user.

→ **Rework:** R5 added, with provenance in the answer and a visible perimeter as the mitigation.

**The judge's verdict:** *"I would sign this — provided the commitment is restated with the CPO before the semantic work starts. Without that you spend four months building the right thing and still fail the board review on the wrong number."*

---

## Part 5. What the run said about the skill

The point of the exercise. Six findings; five are about the knowledge base rather than the document.

**1. There is no atom for "the gate was never applied".** The whole base frames kill-gates as pre-launch: `no-assistant-without-foundation` stops a launch. It says nothing about the case where the launch already happened, works, is funded and cannot be switched off — which in 2026 is at least as common as the greenfield one. `plausible-but-wrong` describes the risk and `ai-triad-prerequisites` the correct order; neither offers a retroactive form. The whole of S3 in this document — narrow, guarantee, refuse, measure — had to be constructed rather than retrieved. **New roadmap item.**

**2. A publicly committed number has no play in the base.** `vision-statement` warns that an inspiring number outlives the strategy and gets quoted for a year — but only from the author's side, as advice not to write one. Here the number is already external, said at an investor day by the sponsor. Renegotiating a public commitment is a governance and communication move, and the base has no material on it. It became the single most important item in this strategy and the base contributed nothing to it. **New roadmap item.**

**3. The failure catalog has no family for "the correct decision that looks like a retreat".** Narrowing the assistant is right and will be read as a rollback. Family F covers champion burnout, capacity, culture; nothing covers the political cost of a correct technical decision. That is a distinct failure mode with its own mitigation — produce the number before the announcement — and it is missing. **New roadmap item.**

**4. The channel triangle assumes centralized reporting exists.** `ssbi-vs-guided` states that self-service cannot reach a single version of the truth without a centralized function — true, and unusable here: this company never had a factory team and will not build one. Following the base literally would produce "build centralized reporting", which would be rejected within a week. The workaround used — reach the single version through definitions with owners rather than through a team — is not in the base. **New roadmap item.**

**5. `ai-ready-domain-score` cannot be computed for a company with no knowledge base.** Its first part is knowledge-base completeness. For this company that is zero, which makes the composite meaningless as a current-state measure while still being a good target. The diagnostics page says so instead of producing a number. Minor, but the atom should carry the caveat rather than leaving it to be discovered. **A caveat, not a new atom.**

**6. What worked, and is worth recording.** `context-governance`'s verify-gate-with-an-explicit-time-budget mapped directly onto the two borrowed metric owners at 20%, including the rule that overrunning the budget is a platform problem rather than a personal one. That atom did real work here without adaptation. So did the `must_not` discipline: the first draft's "raise from 31% to 80%" is precisely the trap that golden-set item gs2-02 exists to catch, and the requirements check caught it in the artifact.

---

## Part 6. The run's verdict

| What was tested | Result |
|---|---|
| The skill assembles a document across the six sections | yes |
| Gate 0 catches defects mechanically | yes — two disqualifiers, one orphan initiative, one uncovered problem, two banned phrasings |
| Gate 0 blocks the document before the judge | yes |
| The judge finds what the checklist cannot | yes — rank-versus-calendar, the unpriced narrowing |
| The deadline rule is honoured (a safe perimeter, not "you are not ready") | yes — the assistant is neither switched off nor defended; it is narrowed and measured |
| The skill resists an available-but-wrong number | **no on the first pass**, yes at the gate |
| The base covers a company whose AI is already live | **no** — four gaps, see part 5 |

**The main conclusion.** The gates did the work again, and this time the more interesting catch was the judge's: the draft ordered its streams correctly by the stack-rank and wrongly by the calendar. A checklist cannot see that, because nothing in the document was formally missing.

**The main defect.** The base is written for companies that have not started yet. Every gate, every chain and every stack-rank assumes the AI has not launched. For a company where it launched a year ago, works, and has been promised to investors, the skill produces a correct frame and no material — the strategy's centre of gravity, the restated commitment, was assembled from first principles rather than from the base. That is the gap worth closing before the next run.

**Compared with run 01.** Run 01 found the base skewed towards a large technology company with its own engineering. This run found the complementary skew: **towards a company at the start.** Both are the same underlying bias — the base describes the situation the author was in, well, and the situations around it thinly.
