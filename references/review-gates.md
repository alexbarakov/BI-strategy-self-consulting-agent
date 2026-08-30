# Quality gates: the judge and anti-optimism

Two mandatory passes before any artifact is delivered. The first stops an unexecutable strategy from going out; the second stops one drawn for the best case.

**A mechanical check comes before the judge.** `strategy-requirements.md` covers everything checkable: the presence of sections, traceability, owners, baselines and triggers, precision of wording. The judge does not spend findings on that — it takes a document that has already passed the check and looks for what a checklist cannot catch: a wrong priority, an unaffordable plan, a defence that will not hold.

---

# 1. The judge — the closing stage of every scenario

Never hand over the first draft. Between draft and final sits an adversarial review **in the voice of a sceptical head of analytics who has shut down two BI projects and paid for a third**. The one the CFO will ask "why does this cost so much", and the domains will ask "why should we do your job".

The judge's task is not to polish phrasing but to find where the strategy is unexecutable, unprioritised or empty.

**The judge's stance.** Assume good intentions and poor odds. Judge usefulness, not effort: "would I sign this, would I give people, would I defend it at the budget committee?" One killer question beats ten fair ones. If a section is good, say so briefly and move on: a review that criticises everything devalues itself entirely.

## Seven dimensions — a verdict on each (`ok` / `weak` / `blocking`)

1. **Priority.** Does the strategy answer the company's most expensive pain — or the author's most interesting one? What happens if nothing is done.
2. **Order.** Has an AI initiative been placed ahead of its link in the chain. Will every launch pass its kill-gate.
3. **Feasibility.** Are there people and time for this, or do the initiatives live on goodwill. Who exactly owns each one.
4. **Complexity.** Has something been assembled that nobody will maintain a year from now. Are we building a platform where a process would do.
5. **Concreteness.** Is it clear what to do on Monday. Do the goals have a baseline and a way to measure, rather than "improve quality".
6. **Defensibility.** Will it survive "why do we need this" from the business and "why so long" from management. Are there numbers, and whose.
7. **Honesty about risk.** Are the real ways to fail named, or is the risk register a formality. What we do when it fails.

## The judge's output

Five to eight findings, each with:
- severity: `blocking` / `serious` / `worth fixing`;
- the exact quote or section it attacks;
- what would make the section pass.

Plus one verdict line: *"As it stands I would / would not sign this, because…"*.

## Scaling by scenario

- **FORM** — all seven dimensions against the whole document.
- **AUDIT** — the same lens turned on your own report: are the findings prioritised, are they actionable, will the recipient understand what to do on Monday.
- **CONSULT** — a short version covering only the recommended option: can this team afford it, is the first step concrete, what will break it.

## The rework cycle — the reason the stage exists

What is found goes back into the draft before finalisation:

1. Blocking findings are either fixed or turned into an explicit user decision ("we keep this knowingly, because…").
2. Serious ones are fixed or moved into the limitations section.
3. Show the user **what changed**: before → after, briefly. A pass with no visible change is a sign the judge was polite rather than useful.

---

# 2. Anti-optimism: how to set target maturity

Seven rules. Apply them before any number enters the document.

**1. The target is calibrated, not maximal.** Levels 3–4 across every category are not a target but a symptom of an unread diagnosis. Calibration — company size, the business's dependence on data, the industry's pace — pulls the target line down to what this company will actually justify.

**2. Name the ceiling and the "enough" mark for every category.** Where the practical limit is and where the return flattens: "~80% is the target; even critical data is never governed to 100%, and 100% is not needed". If a category can sit at its current level for a year, write that down. **A deliberate decision not to improve something is a strategic decision worth recording.**

**3. Plus one level per year is the honest default.** A shift larger than one level requires a named reason: allocated capacity, an already-financed platform change, a regulatory deadline. Without a reason, plan +1 and explain why. A reference point: a target of 20% penetration delivered 2% in a year when the capacity was never allocated.

**4. Discount the plan, not just the estimate.** Every goal inherits the risk of its assumptions. Before fixing numbers, apply and show three corrections:
- dependency risk — does this stand on somebody else's delivery that you do not control;
- capacity risk — is the work funded or living on enthusiasm;
- adoption risk — does the result require people to change their behaviour.

A goal that survives all three unchanged is usually a goal nobody checked.

**5. Write down what the strategy does NOT do.** A mandatory section: which capabilities stay as they are, which initiatives are deliberately absent from this horizon, and why. A deliberately excluded stream with a gate that will open it later is a stronger artifact than a stream included "because it is a trend". It is also the honest answer to "so where is our AI".

**6. Measurable modesty beats inspiring vagueness.** "Raise the share of consumption on certified objects from 0% to 30%" beats "achieve a data-driven culture". If the baseline is unknown, the goal stays `[missing data]` until it is measured. Do not let an inspiring number into the document to close a hole.

**7. Rehearse the cut.** Ask directly: "if you lose a third of the resource mid-year, what dies?" The answer becomes the published freeze list. Strategies without a rehearsed cut do not survive the first budget review — they simply fail quietly everywhere at once.

---

# 3. The "declared but not resourced" flag (for AUDIT)

The most common real state is not "partial" but **described well and backed by nothing**: roles named without time, goals set without capacity, policies written without an owner.

Do not average that silently into a one. Score the substance and attach a `[declared, not resourced]` flag to the dimension, then carry every flagged dimension into the gap list. Unresourced governance is the single most reliable predictor of programme failure. Half points are acceptable when they genuinely help (1.5 = the design is sound, the execution is not), but the flag matters more than the decimal.
