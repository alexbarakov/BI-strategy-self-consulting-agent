# The wiki output — page structure

The strategy is assembled as **a linked mini-wiki across the six sections** of `strategy-requirements.md`: a vision front page, five section pages and an appendix. Pages are joined with Obsidian wiki-links (graph view, click-through) and export to a site (MkDocs) or a single HTML file.

**The seven blocks of the analysis frame (`strategy-template.md`) are not the structure of the document.** They are an instrument: their result is distributed across streams and initiatives, and the frame itself lives in the appendix, linked from wherever detail is needed.

## Folder and files

Folder: `BI-AI-Strategy — <Company>/`.

```
index.md                  — Vision: the summary, reads standalone, plus navigation
01-Context.md             — external (trends) and internal (problems) + scorecard
02-Streams.md             — streams of change: description, justification, boundaries, owner
03-Initiatives.md         — portfolio: stream tags, output/outcome by year, gates
04-Goals.md               — goals as metrics: baseline, target, deadline, owner
05-Risks.md               — register with triggers + the freeze list
appendix/
  90-Diagnostics.md       — 0–4 maturity profile, AI readiness, chain breaks
  91-Analysis-frame.md    — the seven blocks: what each established and where it went
```

**Light mode:** `index`, `01-Context`, `02-Streams`, `04-Goals`, `05-Risks`, `appendix/90-Diagnostics`. Initiatives collapse into a table inside `02-Streams`; the analysis frame is not exported.

**Single source rule.** The portfolio lives in `03-Initiatives`, the metrics in `04-Goals`, the risks in `05-Risks`. Other pages link to them and never copy.

---

## `index.md` — the vision as a summary

The front page *is* the vision section. Test: someone who read only this page understands where you are going, what you are solving and what is wanted from them.

```markdown
# BI+AI Strategy — <Company>
> <profile · horizon · date · draft status>

## Where we are going
<two to four sentences: what the target state looks like at the planning horizon. No "improve efficiency".>

## Which problems we close
<three to five lines, each linking to a specific problem in [[01-Context]]>

## Streams of change
| Stream | In one line | Owner |
|---|---|---|
| <name> | <what changes> | <name> |
→ in detail: [[02-Streams]]

## What we deliberately do not do
<a list with reasons. A mandatory section: it is also the answer to "so where is our AI">

## What we need from the sponsor
<the explicit ask: money, people, authority or a decision — stating exactly what is to be decided>

## First step and the cost of inaction
<90 days: what we do and on which kill-gate we stop · what it costs to do nothing>

## Navigation
[[01-Context]] · [[02-Streams]] · [[03-Initiatives]] · [[04-Goals]] · [[05-Risks]] · [[appendix/90-Diagnostics|Diagnostics]]
```

Length: one page. A section that does not fit on a page is not a summary.

---

## `01-Context.md`

Two subsections. Trends carry a **consequence line for this company** — a trend without one is deleted. Problems are collected across four role groups, and each carries **evidence and a cost of inaction**.

Close the page with the chain breaks stated concretely (not "low maturity") and with a list of problems deliberately left uncovered, each with a reason.

---

## `02-Streams.md`

Open with the stack-rank and the freeze order, then one section per stream:

**Description** — what changes and what the result looks like.
**Justification** — which problem it closes and which trend it addresses, **by reference, not by implication**; it must answer "why this stream rather than another".
**Boundaries** — what is deliberately out of scope.
**Owner** — a name. **Dependencies** — on which streams.

Close with a two-way traceability table: problem → covering stream, and problems with no stream listed explicitly with a reason.

---

## `03-Initiatives.md`

A table, because it exists to be compared and cut:

`initiative` · `stream tags` · `owner` · `Year 1` · `Year 2` · `Year 3` · `metric` · `kill-gate` · `depends on`

In each year cell: **A** for output (what was built) and **O** for outcome (what changed), with number targets as placeholders `<•>` until a baseline exists.

Requirements: year one concrete, later years marked as indicative · an outcome in year one requires a baseline at the start · every AI initiative carries a kill-gate with a threshold on your own data · an initiative ahead of its link in the chain is moved or gated.

Finish with a "first 90 days" list — three to five items with owners and check dates, and an explicit note on what is deliberately *not* in it.

---

## `04-Goals.md`

`stream` · `metric` · `baseline` · `Year 1` · `Year 2` · `Year 3` · `owner` · `how it is measured`

Baselines are either measured or written as `[requires clarification]` with the source that would close them — never replaced by a plausible number.

Add three blocks: **the metric groups** (engagement, quality of service, process quality, business impact), **ceiling and sufficiency** per metric, and **the discount** applied for dependency, capacity and adoption risk. Where an AI assistant is deferred, state its **opening gate** here — the conditions under which it is reconsidered, and the kill-gate that applies after launch.

---

## `05-Risks.md`

`risk` · `likelihood / impact` · `mitigation` · `owner` · `trigger`

The trigger is the observable sign that the risk has materialised; a risk without one will not be noticed in time.

Close with **the freeze list** — what dies first if a third of the resource is lost, published in advance. Name explicitly what is never frozen, and why.

---

## Appendix

**`90-Diagnostics.md`** — the maturity profile as a table rather than prose: `level (🟢/🟡/🔴 + score) | categories | what it means`, grouped into strong / medium / weak. Plus the AI-readiness overlay and the chain breaks.

**`91-Analysis-frame.md`** — the seven blocks, two lines each: what was established and which stream or initiative it went into. A block that went nowhere is either unfinished analysis or a deliberate decision not to touch the area; the second moves into "what we do not do" on the front page.

---

## Presentation

- **Emoji in headings:** 🌍 external context · 🏠 internal · 🩺 diagnostics · 🧭 streams · 🗺️ initiatives · 📊 goals · ⚠️ risks · 🔑 first step.
- **Callouts** as blockquotes, which stays portable in Obsidian: `> ⚠️ **Draft** — validate with the team`. MkDocs converts them into admonitions.
- Tables for anything enumerable; line breaks inside cells with `<br>`.
- Separate with `##` and `---`; do not run pages as a wall of text.
- xlsx templates go into `<Company>/templates/` and are linked by relative path.

## Evidence discipline on the pages

- Every figure carries its tag: `measured` · `benchmark` · `vendor` · `author-estimate` · `disputed`. The tag travels with the number.
- Never present a vendor figure as fact: "who measured it, and on whose data" goes alongside.
- Write "no data" plainly and propose a measurement instead of substituting an estimate.
- The source of figures is `evidence-2026.md` and `kb/51-numbers.md`; put inline links to primary sources rather than only a materials block at the end.

## Rules

- Obsidian links; every page links back to `index` and across to related sections.
- Drafts are marked explicitly: `> ⚠️ Draft`.
- The single source is never copied — it is linked.
- Navigation statuses: ✅ / 🟡 / ⬜.
- Before delivery, run the check in `strategy-requirements.md`: disqualifiers → Definition of Done → traceability → wording precision.
