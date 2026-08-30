---
name: bi-strategy
description: Consults on, builds and audits a BI+AI strategy. Three scenarios - CONSULT (work a concrete case through options and trade-offs), FORM (build the strategy - interview, maturity diagnosis via BI Project Health Check, AI-readiness overlay, a six-section document), AUDIT (review an existing strategy - scorecard, chain breaks, resequenced priorities). Every artifact passes the judge stage. Triggers - "build my BI+AI strategy", "review our strategy", "advise me on this case", "assess our BI maturity", "/bi-strategy".
---

# BI+AI Strategy Builder

Builds a BI+AI strategy for a specific company: interview → maturity diagnosis → a strategy document covering every section. Grounded on the canonical Data Nature method (Health Check + D&A Planner) plus the AI layer of the «BI+AI Strategy 2026» course.

Working principle, and the course's own thesis: **AI drafts — humans validate.** The skill does not invent; it instantiates known frameworks against the participant's data. Every section is validated by the user.

## When to use

- The final course exercise — "a full BI+AI strategy draft"
- BI maturity and AI-readiness diagnosis
- Triggers: `/bi-strategy`, "build my strategy", "final homework", "assess our BI maturity"

## Reference material

- `references/course-knowledge.md` — **the course concept library**, grounding for competent recommendations (generic, no company-specific data). Lean on it in the "Recommendation" part of a section.
- `references/diagnostic.md` — the diagnosis model (BI Project Health Check + the course's AI-readiness overlay).
- `references/question-bank.md` — 72 Health Check factor questions.
- `references/strategy-template.md` — **the analysis frame** of 7 blocks (not the shape of the document) + block → materials mapping.
- `references/wiki-structure.md` — the page tree for the six document sections and a template for each (layout, tables, roadmap, metrics).
- `references/evidence-2026.md` — **verifiable 2026 material** with sources: where AI actually works in data processes, data management trends in the AI era, the context layer, next-gen report formats. Use it as a source of figures and as the "verifiable / vendor-measured / no data" filter.
- `references/kb/` — **an atomic knowledge base, 66 files: one file = one topic**, linked by Obsidian wiki-links. Entry point is `references/kb/30-graph.yaml`: find the strategy block by number and it lists the relevant atoms; `key_evidence` holds the numbers worth arguing with, each carrying its evidence level.
  - `kb/11-method/` — the canonical Data Nature method: each worksheet of the BI Strategy & Tactics Guide 2.0 as its own atom (pains, domains, user classification, info supply-demand, data and content processes, self-service and centralized practices, access matrix, metrics, action plan, vision).
  - `kb/20-catalog/` — BI Project Innovation Map: the catalog of every direction a BI project can take, used as a completeness checklist for the strategy.
  - `kb/31-field/` — field data: a benchmark of 12 BI projects (2026) and the map of pain fronts. Use it to calibrate "how do others look", **not as industry statistics**.
  - `kb/10-ai-era/` — concepts, cases and practices from nine course sessions: the AI foundation and its prerequisite triad, the LLM assistant reference architecture, the context layer, the semantic layer with paired accuracy measurements, content certification, community and competencies, hiring in the AI era.
  - `kb/30-graph.md` — **the visual theme graph**, 10 Mermaid diagrams: clusters, dependency chain, AI foundation, method spine, content lifecycle, delivery models, data, people, failure triage. Show it to the user when they need a map rather than a list.
  - `kb/50-failure-catalog.md` — **75 failure modes in 7 families** with symptom triage. Open it first when a participant arrives with "something is wrong with us" rather than with a formed question.
  - `kb/51-numbers.md` — **the numbers registry** with tags `measured` / `benchmark` / `vendor` / `author-estimate` / `disputed`. A figure may only be quoted together with its tag; `vendor` and `disputed` never as fact.
  - **Atoms listed under `anonymized_cases` in the graph are worked cases with anonymized thresholds.** The mechanics transfer; thresholds are set from your own baseline.
- `references/faq-participants.md` — **101 participant questions with answers**, grouped by the eleven sessions. Provenance is tagged: ◆ real (pre-course survey n=12 and session interactive n=10), ◇ raised by the author for group discussion, ○ derived from the knowledge base. Every answer cites the atoms behind it. Use it as discussion material and as a source of phrasing when a participant asks something similar.
- `references/70-golden-set/` — **the skill's golden set in three tiers**: retrieval (101 items, deterministic), answer quality (32 with `must_contain` / `must_not` and a judge), honest refusal (10 negative cases). Run it after changes to the KB or the templates. `build.py` regenerates tier 1 from the FAQ, `score.py` aggregates a run.
- `references/knowledge-map.yaml` — **the machine-readable map**: strategy block → which local files to read and what to take from the companion repository. Start navigation here.
- `references/strategy-requirements.md` — **the acceptance spec for the deliverable**: six sections (context → vision → streams → initiatives → goals as metrics → risks), the wording-precision requirement with six tests and a ban list, a 12-point Definition of Done, and the disqualifiers. Applied twice: as the check before delivery in FORM and as the scorecard in AUDIT.
- `references/review-gates.md` — **mandatory quality gates**: the judge stage and the anti-optimism rules for setting targets.
- `references/companion-kb.md` — how to plug in [DG Board KB](https://github.com/alexbarakov/DG-strategy-self-consulting-agent) as the governance layer.
- `references/materials-links.md` — which links to include (public ones) and which to leave as placeholders.
- `references/BI Project Health Check.xlsx`, `references/D&A Strategy & Tactics Planner [ENG].xlsx` — working templates (copied into `<Company>/templates/`, linked by relative path).

**The skill runs on the participant's own machine.** Everything is grounded offline from these files; **never substitute somebody else's internal links** — internal URLs are placeholders the participant fills in for their own company (see `materials-links.md`).

---

## Scenarios and routing

| Scenario | Triggers | Shape |
|---|---|---|
| **CONSULT** | "what's the better way to…", "does it make sense to…", "we have a case…", "advise me" — a concrete question, no document, no request to build | Dialogue: the case → grounded answers with options and trade-offs → **judge** → converge on a decision |
| **AUDIT** | "review our strategy", "give feedback on our BI programme", "tear this apart", or simply a document attached | **Scorecard across the six sections of `strategy-requirements.md`** (present / partial / absent + what is missing) → disqualifiers → chain breaks → resequencing → quick wins → **judge** |
| **FORM** | "build a BI+AI strategy", "final course homework" | Interview → diagnosis → analysis across the 7 frame blocks → assemble the document in six sections → **requirements check → judge → rework** → 6-pager |

Routing: a document with a request → AUDIT; a question → CONSULT; an explicit request to build → FORM. CONSULT escalates naturally: if the dialogue reveals that the case is a whole-programme problem, offer to move to AUDIT (if a strategy exists) or FORM (if not).

**The requirements are applied differently in the two scenarios.** In FORM, `strategy-requirements.md` is a checklist for accepting your own draft before delivery. In AUDIT it is the frame for assessing somebody else's document: the six sections give the scorecard its structure, the disqualifiers give blocking findings, and the wording tests turn a vague "it reads fuzzy" into a specific critique of specific sentences.

**Every scenario ends with the same stage — the judge** (`references/review-gates.md`). This is not polish: no artifact leaves the skill without passing it and showing what it changed.

**A case with a deadline.** If the case carries a hard external commitment ("we promised the board this quarter"), do not answer "you are not ready" — that advice is not taken, and the launch happens anyway, only unprepared. Give the minimum safe perimeter instead: which narrow domain to launch on, which gates are mandatory, and what to tell the sponsor honestly about the limits.

## Universal conventions (all scenarios)

- **The artifact is written in the user's language.** The reference files may be in another language; the artifact is in the language you are being spoken to in. Ask explicitly if the language is mixed or if the document's audience differs from the requester's. Established terms (self-service, kill-gate, stack-rank, semantic layer) stay in their usual form, noted once at the start of the document.
- **Name what is missing rather than invent it.** Instead of a plausible number, put a marker straight into the artifact:
  > `[missing data]` — to state a target self-service penetration we need the current share of active users by role. Source: a 90-day BI usage export. Without it the goal stays a range, not a number.

  Collect every marker into a closing list **"What must be measured"**, sorted by how much each one blocks decisions. A strategy with five honest gaps is stronger than one with five invented numbers. A vague phrase used instead of a number is the same gap, only hidden.
- **Invite documents as you go.** As soon as context starts forming (after the case is stated in CONSULT, after the first interview batch in FORM, while collecting inputs in AUDIT), offer: *"If you have existing material — a pain analysis, a landscape map, assessment results, a previous strategy, survey exports — send it now and I will ground the work on it instead of asking again."* Anything sent counts as the participant's data and is quoted, not re-asked.
- **Visualization at the end.** Offer to assemble the result as a single-file HTML: CONSULT — a one-pager of the decision; AUDIT — scorecard, chain-break map, resequenced roadmap; FORM — diagnosis, roadmap with the stack-rank, a board of kill-gates.

---

## Step 0. Mode and context

1. Ask for the mode (unless it was given):
   - **Light (~15 min):** diagnosis across the 9 categories at a coarse grain + strategy for the key sections. Suitable for everyone.
   - **Full (~45–60 min):** factor-by-factor diagnosis (closer to the 147 Health Check factors) + a developed strategy across all sections with initiatives and metrics. For those actually writing the strategy.

2. **Confirm the structure and the volume** (before the interview, not after):
   - show the list of sections and let them be cut or reordered — a strategy for a 200-person company need not carry all seven blocks of analysis;
   - volume: **6-pager** by default · a full wiki by section · section-by-section delivery with a review after each;
   - if this is not pure BI/AI but D&A or a mix with data management, plug in the companion (`references/companion-kb.md`).

3. Check for data that already exists:
   - a completed **pre-course survey** (profile, team, pains, what survived to production with AI) — reuse it, do not ask again;
   - a previously saved strategy draft — offer to update it or start fresh.

---

## Step 1. Interview

Ask through `AskUserQuestion`, in batches of two or three, never all at once. The goal is to collect exactly what the diagnosis and the sections need. Question-to-block mapping is in `references/strategy-template.md`.

**Light — the minimum set (~8 questions):**
1. Company context: size, industry, tech / non-tech profile, data maturity (data-informed / driven / led).
2. Team and infrastructure: which roles exist (warehouse, central BI, domain analysts, ML/DS, Data Governance, CDO), the BI tool, whether a semantic layer or metric store exists, whether a data assistant exists (production / pilot / none).
3. Demand: who the consumers are, % of business users opening BI at least monthly, the self-service share.
4. Foundation: whether a certified core layer exists, the share of certified data, the state of data quality.
5. Pains: the top one to three BI pains right now.
6. AI today: what was tried with AI/LLM and what survived to production; the % of ad-hoc that could plausibly go to AI.
7. Constraints: resource and budget, risk appetite, whether governance is resourced.
8. Ambition: what you want to achieve within 12 months.

**A mandatory self-assessment step (both Light and Full).** After the context questions, do not eyeball the maturity — ask the participant to score the categories 0–4. Take the wording from `references/question-bank.md` (real Health Check factors, never invented):
- **Light:** 9 category scores (one per category, anchored on its lead question) + 5 AI-readiness scores (AI-1…AI-5). Ask in batches of three or four through `AskUserQuestion`, with options 0/1/2/3/4 and anchors (No / Planned / Partially / Completed / Optimized). Where possible take a one-year target alongside.
- The scorecard is computed from **these scores**, not from guesses. Without this step the diagnosis is too thin to build a strategy on.
- **Keep the questions simple:** one idea per question, no jargon lists inside a single question. Options in plain language, identical everywhere: "Yes, established" (4) · "Mostly yes" (3) · "Partially" (2) · "No / barely" (1). Do not read Health Check terminology at the participant verbatim — translate it into human speech.

**Full — adds to Light:**
- A factor-by-factor pass (72 factors from `question-bank.md`), averages across the 9 categories and the 7 solution categories.
- A short 0–4 self-assessment per Health Check category (see `references/diagnostic.md`); a grid works well.
- Data domains and ownership, and a consumer map by role.
- The target balance of Centralized / Self-Service / Agentic channels and a realistic agentic maturity stage for the year.
- A candidate domain for the AI foundation triad (what goes into semantic / core / domain knowledge base, and who holds the gate).

Do not turn the interview into an interrogation: if there is no answer, mark `[requires clarification]` and move on.

---

## Step 2. Diagnosis

Follow `references/diagnostic.md`. It produces:
- **A maturity profile** — level (Beginning / Learning / Developing / Mastering, 0–4) across the 9 Health Check categories and the 7 solution categories.
- **An AI-readiness overlay** — scored on the course's layer (domain context completeness, semantic coverage, share of certified data, process readiness for "AI drafts — humans validate").
- **The break in the dependency chain** — where `core → semantic → context → AI accuracy → self-service` snaps; name the two or three most expensive breaks.
- **The position in the channel triangle** and a realistic agentic maturity stage for the year.

The diagnosis is the *input* to the strategy: weak categories and breaks dictate the priorities directly.

---

## Step 3. Producing the document

Assemble the wiki along the **six document sections** of `references/strategy-requirements.md`, taking the page layout from `references/wiki-structure.md`. The seven blocks in `references/strategy-template.md` are the analysis frame: you work through them, and what goes into the document is the result, distributed across streams and initiatives — the frame itself moves to the appendix.

For each section hold the shape:

> **Substance** (a dry draft, two to four sentences) → **Recommendation (draft)** (a concrete expert reading based on the diagnosis and the material, marked DRAFT) → **Contents** → **Company questions → dependent projects** (a table) → **Maturity gate** (what NOT to start without need or foundation) → **Materials and templates** (internal cross-links plus external ones: xlsx templates, sessions, wiki pages).

Format rules: **"Recommendation (draft)" is written as prose**, in the rhythm of a real strategy ("why it matters → what we do → where it leads"), but grounded in **the participant's own data and scores**. **Never carry figures, targets or names across from a reference strategy** — a reference gives you the shape and the register, not the numbers. Every measure is conditional, gated on maturity; never recommend doing something without a need or a foundation underneath it.

- **Light:** context, diagnosis (condensed), the AI foundation as the core, vision and plan with the stack-rank, plus the scorecard and the risk register.
- **Full:** all sections in full, with per-domain detail.

Mandatory cross-cutting artifacts:
- the diagnostic scorecard (maturity profile + top breaks);
- the **stack-rank** of priorities (Governance → Trusted Data → AI readiness → BI Content → Self-service) with an explicit "what we freeze first";
- the **metric tree** (four Planner groups: Engagement / Quality of service / Process quality / Business impact, plus AI metrics);
- a **kill-gate** for at least one AI initiative;
- a **risk register** (the fragile chain AI → semantic layer → core → catalog; agents multiply chaos; governance without resource);
- the **dual track**: old BI sustaining plus new AI exploring.

### Output — a linked wiki

Not one flat file but a **mini-wiki**: a front page plus section pages, linked with Obsidian wiki-links (native graph view and navigation). Structure and naming rules are in `references/wiki-structure.md`.

In short:
- A folder `BI-AI-Strategy — <Company>/` in the current working directory (or in the knowledge base, if run from a vault).
- `index.md` is **the front page and the vision summary**: where we are going, which problems we close, the streams one line each, what we deliberately do not do, the ask to the sponsor, the first step and the cost of inaction. It must read standalone.
- Section pages, each with a breadcrumb back to `index` and cross-links to related sections.
- Cross-links between sections (for example from a goal to the initiative that moves it, from a stated problem to the stream that closes it).

Order of work: assemble and show **the index first**, get an "ok", then expand section by section — show a page, take corrections, move on. That human gate is the defence against hallucination. Never generate the whole wiki at once without agreeing the scorecard.

At the end offer: (a) the blank Planner and Health Check xlsx as working files, (b) a slide version assembled from the wiki, (c) an export to a single HTML file for sharing outside Obsidian.

---

## Rules

- No generic advice — tie every recommendation to the participant's answers and to the framework. Not "implement data quality", but "your chain breaks between core and semantic, so the first step is a core layer on domain X with metric Y and kill-gate Z".
- Flag `[requires clarification]` wherever data is absent; never invent figures.
- Do not dump the whole document at once in Light mode — show the scorecard and the stack-rank, get an "ok", then expand.
- Hold the Data Nature baseline: the 0–4 scale, the Centralized vs Self-Governing dichotomy inside processes, and the goal form `Description | KPIs | Outcomes | Timing`.

## Evidence discipline (mandatory)

The source of figures is `references/evidence-2026.md` and `references/kb/51-numbers.md`. The rules:

1. **Tag the level of every figure:** verifiable / vendor-measured / no data. A vendor figure is never presented as fact — who measured it is always named alongside.
2. **"No data" ≠ "does not work".** It is an invitation to measure it yourself in shadow mode, not a verdict on the technology.
3. **The effect of AI is not measured by the team's self-assessment.** In a controlled study developers were 19% slower while being convinced they were 20% faster. What goes into the metrics is a measurement against a golden set, not a survey.
4. **Never carry across somebody else's targets.** Numbers from benchmarks and cases orient the conversation; in the roadmap they stay as placeholders `<•>`.
5. **Routing, not replacement.** When recommending AI inside a process, always state what stays deterministic and at what volume: the cheap layer on the mass, the model on the disputed cases.

---

## Gates before delivery (mandatory)

0. **Requirements check.** Run the artifact through `references/strategy-requirements.md`, in this order:
   - **Disqualifiers** — ten signs. Any one of them sends the document back regardless of its size; it does not reach the judge.
   - **Definition of Done** — twelve points, each answered "yes / no / not applicable, because".
   - **Traceability** — run it both ways: is every named problem covered by a stream, is every initiative justified by a reference to a problem or a trend. Orphans are deleted or given an explicit reason to exist.
   - **Wording precision** — six tests and the ban list. Phrases failing the portability or the arguability test are rewritten, not annotated.

   Show the result as a table: section · status · what is missing. This is a cheap mechanical pass, and it removes most findings before the judge ever reaches them.

1. **The judge.** Run the artifact through the judge stage from `references/review-gates.md`: seven dimensions, five to eight findings with severity, and a verdict of "I would sign this / I would not". Fix blocking findings or turn them into an explicit user decision. **Show what changed** (before → after) — a pass with no visible change means the judge was polite rather than useful.
2. **Anti-optimism.** Before any number enters the document: targets calibrated rather than maximal; +1 level per year by default; every target discounted for dependency, capacity and adoption risk; **what the strategy does not do** written down; the budget cut rehearsed and the freeze list published.
3. **Evidence discipline.** Every figure carries its level; vendor numbers are not presented as fact; the effect of AI is not measured by self-assessment.

## Installation

- **Claude Code:** clone the repository straight into the skills directory — `git clone <url> ~/.claude/skills/bi-strategy`. `SKILL.md` sits at the root, so the clone directory *is* the skill and the relative paths to `references/` resolve on their own.
- **Any other agent:** pass this file as instructions and the repository root as a knowledge source.
- **Paired work:** clone [DG Board KB](https://github.com/alexbarakov/DG-strategy-self-consulting-agent) alongside if you are building a D&A or mixed strategy.
