# BI Strategy — self-consulting agent

A ready-to-run skill that builds a **BI+AI strategy** for a specific company: interview → maturity diagnosis → a linked mini-wiki covering every block. Grounded on the canonical method (BI Project Health Check + D&A Strategy & Tactics Planner, data nature / Alex Barakov) plus the AI layer of the «BI+AI Strategy 2026» course.

Working principle: **AI drafts — humans validate.** The skill does not invent; it instantiates known frameworks against the participant's own data, and every block is validated by the user before the next one starts.

**Companion:** [DG Board KB](https://github.com/alexbarakov/DG-strategy-self-consulting-agent) — the governance half of the same method. The two repositories are designed as a pair and share the same invariants.

## At a glance

| What | Size |
|---|---|
| Knowledge base — one topic per file, `[[wiki-links]]`, machine-readable graph | **66 atoms** |
| Theme graph — nodes, clusters, curated relations, Mermaid views | **66 nodes · 283 links · 10 diagrams** |
| Participant question base with answers, provenance-tagged | **101 Q&A** |
| Golden set — retrieval / answer quality / honest refusal | **143 positions** |
| Failure catalog — named failure modes with symptom triage | **75 in 7 families** |
| Numbers registry, every figure tagged by reliability | **93 rows** |
| Health Check diagnostic factors, 0–4 scale | **72 factors** |
| Strategy structure | **7 blocks** |
| Working templates (xlsx), ready to hand to the participant | **2** |

## Two ways to use this repository

**A. As a knowledge source (passive).** Add the repo or its URL to your agent's context and let it ground *other* tasks — answering BI/AI questions, reviewing a design, preparing a talk, sanity-checking a vendor claim. Nothing to install; the agent follows "How the agent uses it" below.

**B. As a strategy skill (active).** [`skills/bi-strategy/SKILL.md`](skills/bi-strategy/SKILL.md) runs the full procedure in three scenarios.

## Scenarios

| Scenario | When | What comes out |
|---|---|---|
| **CONSULT** | you have a concrete case or question | a grounded analysis with options and trade-offs, converging on a decision |
| **FORM** | you need a strategy | interview → diagnosis → 7 blocks → 6-pager, as a linked wiki |
| **AUDIT** | a strategy or program already exists | scorecard across the six required sections, disqualifiers, chain-break map, resequenced priorities, quick wins |

FORM asks for the mode up front — **Light** (~15 min: 8 context questions, self-assessment across 9 categories, scorecard and stack-rank) or **Full** (~45–60 min: factor-by-factor diagnosis, per-domain detail, every block expanded).

No artifact is finalized without three passes: a **mechanical check against `strategy-requirements.md`** (disqualifiers, Definition of Done, two-way traceability, wording tests), then the **judge stage** — an adversarial review in the voice of a sceptical head of analytics who has killed two BI projects — and the **anti-optimism pass** when targets are set.

## Quickstart

```bash
# globally
cp -R skills/bi-strategy ~/.claude/skills/

# or into a specific project
cp -R skills/bi-strategy <project>/.claude/skills/
```

Then in Claude Code: `/bi-strategy`, or just ask — "build my BI+AI strategy", "assess our BI maturity", "audit this strategy" (attach the document).

For any other agent: paste `SKILL.md` as instructions and give the repository as a knowledge source. Everything is grounded offline from `references/` — no internet and no internal systems required.

## How the agent uses it (instructions for the agent)

0. **Something is going wrong / diagnosing a project** — start at `references/kb/50-failure-catalog.md` (symptom triage across 75 named failure modes), pull arguments from `references/kb/51-numbers.md` (**never quote a `vendor` or `disputed` figure as fact**), probe with `references/question-bank.md`.
1. **Answering a BI/AI question** — open `references/kb/30-graph.yaml`, find the strategy block, read the atoms it lists. `key_evidence` holds the numbers worth arguing with, each carrying its evidence level. Atoms cross-link with `[[wiki-links]]`; follow them rather than re-deriving.
2. **Someone already asked this** — check `references/faq-participants.md` (101 questions with answers, each citing the atoms behind it) before composing a new answer.
3. **Building or auditing a strategy** — run the full procedure in [`SKILL.md`](skills/bi-strategy/SKILL.md); structure from `references/strategy-template.md`, output shape from `references/wiki-structure.md`.
4. **Grounding governance blocks** — pull from the companion per `references/companion-kb.md`; the machine-readable mapping is the `companion:` field in `references/knowledge-map.yaml`.
5. **Quoting a number** — take it from `references/evidence-2026.md` or from an atom, and **carry its evidence level with it**. A vendor-measured figure is never presented as fact.
6. **Producing the deliverable** — always **in the user's language**. This repository is the source, not the output template. Missing facts become explicit `[requires clarification]` markers naming the source that would close them — never invented numbers.

## Map

| Path | Content |
|---|---|
| `skills/bi-strategy/SKILL.md` | Entry point: scenarios, step order, rules |
| `references/kb/30-graph.md` | **Visual graph** — 10 Mermaid diagrams rendered natively by GitHub: cluster map, dependency chain, AI foundation, method spine, content lifecycle, delivery models, data & governance, people, failure triage, diagnostics |
| `references/kb/30-graph.yaml` | **Machine-readable graph** — strategy block → atoms, `key_evidence`, `anonymized_cases`, plus 66 typed nodes in 9 clusters and 44 curated relations. Start navigation here. Folder numbering is shared with the companion: the same number means the same role in both repositories |
| `references/kb/50-failure-catalog.md` | **Failure catalog** — 75 named ways a BI or AI initiative dies, in 7 families, with a symptom-triage table. The entry point when something feels wrong |
| `references/kb/51-numbers.md` | **Numbers registry** — every figure with a reliability tag and, where checked, the verification date. The tag travels with the number |
| `references/kb/60-roadmap.md` | What the KB is still missing and in what order to fix it — written from findings, not aspiration |
| `references/kb/10-ai-era/` | 44 atoms — concepts, cases and practices from nine course sessions: the AI foundation triad, the LLM assistant reference architecture, the context layer, the semantic layer with paired accuracy measurements, content certification, community, competencies, hiring in the AI era |
| `references/kb/11-method/` | 19 atoms — the canonical method, one worksheet of the Guide per atom: pains, domains, user classification, info supply-demand, data & content processes, self-service and centralized practices, access matrix, metrics, action plan, vision |
| `references/kb/20-catalog/` | BI Project Innovation Map — the catalog of every direction a BI project can contain, used as a completeness checklist |
| `references/kb/31-field/` | Field data: benchmark of 12 BI projects (2026) and the map of pain fronts. Calibration for "how do others look", **not industry statistics** |
| `references/faq-participants.md` | 101 participant questions with answers, tagged by provenance: ◆ real (pre-course survey n=12 and session interactive n=10) · ◇ raised by the author for group discussion · ○ derived from the KB |
| `references/70-golden-set/` | **Three-tier golden set**: retrieval (101, deterministic), answer quality (32, with `must_contain` / `must_not` and a judge), honest refusal (10). `build.py` regenerates tier 1 from the FAQ, `score.py` aggregates a run |
| `references/diagnostic.md` | Diagnosis model — Health Check + AI-readiness overlay |
| `references/question-bank.md` | 72 Health Check factors across 9 categories, 0–4 scale, with current and 1-year target |
| `references/strategy-template.md` | 7-block structure + block → materials mapping |
| `references/wiki-structure.md` | Wiki page templates and the 6-pager in FAQ form |
| `references/strategy-requirements.md` | **Acceptance spec for the deliverable**: six document sections (context → vision → streams → initiatives → goals as metrics → risks), a wording-precision requirement with six tests and a ban list, a 12-point Definition of Done and ten disqualifiers. Used as gate 0 in FORM and as the scorecard in AUDIT |
| `references/review-gates.md` | Quality gates: the judge stage and the anti-optimism rules for setting targets |
| `references/evidence-2026.md` | Verifiable 2026 material with sources: where AI actually works in data processes, data management trends, the context layer, next-gen report formats |
| `references/course-knowledge.md` | Concept library — generic grounding for recommendations, no company data |
| `references/knowledge-map.yaml` | Block → local files + companion files; entry point for navigation |
| `references/companion-kb.md` | How to plug DG Board KB in as the governance layer |
| `references/materials-links.md` | Which links are public and which the participant fills in themselves |
| `references/make-maturity-svg.py` | Maturity bar-chart generator |
| `references/*.xlsx` | BI Project Health Check and D&A Strategy & Tactics Planner — working templates to hand to the participant |

## Method invariants

Shared with the companion repository — the same rules hold on both sides.

- **Diagnose before prescribing.** A 0–4 maturity scorecard plus an AI-readiness overlay; name 2–3 breaks in the chain `core → semantic → context → AI accuracy → self-service`. The strategy is the repair plan for those breaks, not a wish list.
- **Stack-rank the freeze order:** governance & ownership → trusted data → AI readiness (the triad **certified core layer → semantic layer → domain knowledge base**, wrapped in **context governance**) → BI content → self-service and agentic interfaces last. Cuts are made right to left.
- **Kill-gates block launches** until prerequisites are met: no assistant without semantic coverage and a certified core; no semantic layer without a core beneath it; no self-service scaling without a governance gate; no agent write operations without its own identity, narrow keys and an audit trail.
- **Dual track:** old BI sustaining plus new AI exploring, ring-fenced from each other.
- **Rational target maturity.** The target line is calibrated to the company, not set at "best practice"; +1 level per year unless a funded reason says otherwise; every target discounted for dependency, capacity and adoption risk; what the strategy deliberately does *not* do is written down; the budget cut is rehearsed in advance into a published freeze list.
- **Judge pass before finalization.** An adversarial review across seven dimensions — priority, order, feasibility, complexity, concreteness, defensibility, honesty about risk — whose blocking findings must be fixed or turned into explicit named decisions, with a visible before/after of the rework. A pass that changes nothing means the judge was polite, not useful.
- **Guardrails:** AI drafts — humans validate · no number without a source · no over-optimism — a plan where everything succeeds is a plan nobody stress-tested.

## Evidence discipline

Numbers are sorted by **who measured them**, not by how loud the claim is:

Every quantity lives in `references/kb/51-numbers.md` with a tag saying how much to trust it — the same five-tag scale the companion uses, so numbers move between the repositories with their tag attached:

| Tag | Meaning | Quotable as fact |
|---|---|---|
| `measured` | measured in a named setting, method stated | yes, naming the setting |
| `benchmark` | a reproducible external benchmark or study | yes |
| `vendor` | the vendor's own measurement, or a seller-commissioned survey | **no** — only with who measured it named |
| `author-estimate` | the author's expert judgement, marked as such | as an estimate, not a fact |
| `disputed` | widely circulated, sourcing does not hold up | **no** |

**The tag travels with the number.** If a `vendor` figure reaches a deliverable, the sentence naming who measured it goes with it. Atom-level `confidence:` frontmatter is a separate thing — it marks fidelity to the source of that file, not the reliability of a single figure.

One rule stands separately: **the effect of AI is never measured by the team's self-assessment.** In a controlled experiment developers were 19% slower while being convinced they were 20% faster — so only measurement against a golden set of questions makes it into a strategy's metrics.

Case-study atoms carry anonymized thresholds: the mechanics transfer, the numbers do not. Set thresholds from your own baseline — a threshold borrowed from someone else's deck is either unreachable or already passed, and useless as a gate either way.

## Evaluation

Quality is measured, not asserted. `references/70-golden-set/` holds a three-tier golden set:

- **Tier 1 — retrieval (101).** Did the agent find the right atoms? Deterministic, no LLM, cheap enough to run on every change. Generated from the FAQ by `build.py` so the set cannot drift from its source.
- **Tier 2 — answer quality (32).** Did it say the right things and **avoid the wrong ones**? Judged by rubric, with a hard rule: a match against `must_not` overrides the judge's verdict, however many `must_contain` points the answer covered.
- **Tier 3 — honest refusal (10).** Questions where the correct behaviour is to decline — "what accuracy will we get", "what threshold should we set", "give me industry statistics". Without this tier the set measures recall only and rewards confident invention.

Fixation rule: the set is frozen before changes and **never reworded to match what the agent found** — rewording to fit the retrieval is fitting the test. Five positions are held blind. All positions carry `status: needs_review` until reviewed by the author; only `confirmed` counts.

Targets are deliberately absent. Run once, record the baseline, then watch it not fall.

## Caveats

- **The field benchmark is a sample of 12, and a biased one** — course participants who had already decided to work on strategy. Use it as "here is how others look", never as industry statistics.
- **Real participant questions are reconstructions.** Live session transcripts were not available; the ◆ questions are restored from the pre-course survey, the session-one interactive and the questions the author put on slides — faithful in substance, not verbatim quotes.
- **Numbers in case atoms are anonymized on purpose.** Where a figure was an internal measurement it is given as an order of magnitude ("roughly threefold", "about two thirds"). The construction is intact; the exact value is not yours to copy anyway.
- **Internal links in templates are placeholders** — the participant fills them in for their own organization. The skill never carries numbers or names from any reference strategy into a deliverable; those are a format example, not a data source.
- **Tier-1 golden set questions are worded in the KB's own language**, so they partly test string overlap rather than understanding. Tiers 2 and 3 are deliberately reworded in participant language. Paraphrases for tier 1 are outstanding work.
- Origin: method and materials — Alex Barakov / data nature. Course backing: «BI+AI Strategy 2026».

## Companion repository

[**DG Board KB**](https://github.com/alexbarakov/DG-strategy-self-consulting-agent) is the textual projection of the public Miro board «Data Governance Program Guide»: AI-era and classic Data Governance themes, a workshop template catalog, a failure catalog, a numbers registry and a diagnostic question bank.

| What you are building | Who leads | Role of the other |
|---|---|---|
| **BI** or **AI** strategy | **this skill** | DG Board KB grounds the governance blocks and the AI foundation |
| **Data Governance** | DG Board KB | this skill supplies the BI/AI stream |
| **D&A** or a mix | DG Board KB leads the structure | this skill supplies the substance of the BI/AI streams |

Conflict rule: on governance questions the companion wins, on BI/AI questions this skill does. The invariants match by construction; if they diverge, subject-matter ownership decides.

Block → what to read in the companion: `references/companion-kb.md`; machine-readable version: the `companion:` field in `references/knowledge-map.yaml`.

## Live demo

A finished wiki built by this skill (anonymized data, placeholder numbers): **https://alexbarakov.github.io/bi-strategy-demo/**

## Author

Method and materials — Alex Barakov / data nature: [data-nature.com](https://data-nature.com) · [t.me/datanature](https://t.me/datanature) · links channel [@datanaturelinks](https://t.me/datanaturelinks).
