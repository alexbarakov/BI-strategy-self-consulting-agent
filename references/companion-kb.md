# Companion: DG Board KB — the governance layer under a BI+AI strategy

**Repository:** https://github.com/alexbarakov/DG-strategy-self-consulting-agent
**Entry point:** its `README.md` · machine-readable theme graph: `30_graph/objects.yaml`
**What it is:** a textual projection of the public Miro board "Data Governance Program Guide" — AI-era and classic data governance themes, one file per theme, plus a catalog of workshop templates and a source library.

The two repositories are designed as a pair and share the same invariants: the stack-rank and the freeze order, kill-gates, "AI drafts — humans validate", and the chain `core → semantic → context → AI accuracy → self-service`.

---

## When to plug it in

| What you are building | Who leads | The companion's role |
|---|---|---|
| **BI** or **AI** strategy | **this skill** | grounds the governance blocks and the AI foundation |
| **DG** (data management) | companion | this skill supplies the BI/AI stream |
| **D&A** or a mix | companion leads the structure | this skill supplies the substance of the BI/AI streams |

**Conflict rule:** on governance questions the companion wins, on BI/AI questions this skill does. The invariants match by construction; where they diverge, subject-matter ownership decides.

## How to connect it

- **Both repositories cloned side by side** — read the companion's files by relative path and cite them as a source.
- **This skill alone** — give the agent the companion's URL as an additional knowledge source; with no access, work from the local `references/` and mark honestly where the grounding is thinner.

Do not copy the companion's content wholesale into your artifacts: link to the file and quote what you need. Its files are cut one theme apiece, which makes precise citation easy.

---

## Map: strategy block → what to read in the companion

The machine-readable version lives in `knowledge-map.yaml` (the `companion` field on each block).

| Block | Companion files |
|---|---|
| **1. Business foundation** | `11_dg_program_themes/getting-started.md` — the "5 of 12" test: do you need a programme at all, or will common sense do · `dg-kitchen-research.md` — field observations |
| **2. Landscape assessment** | `maturity-and-metrics.md` — the maturity model and metrics · `dg-frameworks.md` — frameworks and standards |
| **3. Target operating model** | `roles-and-operating-model.md` · `domains-and-data-mesh.md` — domain slicing |
| **4.1 Data models management** | `data-quality.md` · `data-catalog.md` · `domains-and-data-mesh.md` · `10_ai_era_themes/certified-core-layer.md` |
| **4.2 BI report management** | `10_ai_era_themes/bi-content-management.md` — the BI content funnel |
| **4.3 Insight management** | `data-literacy.md` · `10_ai_era_themes/llm-assistant-architecture.md` |
| **5. Technology foundation** | `semantic-layer.md` · `semantic-metric-layer-v2.md` · `certified-core-layer.md` · `domain-knowledge-base.md` · `context-governance.md` · `llm-assistant-architecture.md` · `enterprise-ontology.md` |
| **6. Operational foundation** | `skills-hub.md` — managing skills and agents · `roles-and-operating-model.md` · `maturity-and-metrics.md` |
| **7. Change management** | `dg-program-roadmap.md` — the programme roadmap · `ai-governance.md` |

**Cross-cutting, useful in any block:**
- `12_templates/templates.md` — workshop templates with direct deep-links to the board: pain analysis, domain classifier, vision statement, scope and goal configurators, canvases. Offer them when the participant needs an instrument rather than a description.
- `10_ai_era_themes/library.md` — the canonical reading library by theme.
- `40_sources.md` — verification status for every external link.
- `50_failure_catalog.md` — 45 named ways a DG programme dies, with symptom triage.
- `51_numbers.md` — the numbers registry on the same five-tag scale this skill uses.

---

## What to take from it, and what not to

**Take:**
- definitions and "key terms" — so you do not invent your own terminology;
- the "numbers for arguing with optimists" blocks — for defending priorities and budget;
- the "from the course" sections — thresholds, anti-patterns and field stories absent from public sources;
- workshop templates — when what is needed is an instrument, not text.

**Do not take:**
- figures the author himself flagged as "industry mythology / vendor marketing" — that flag travels with the figure and is never removed;
- board object statuses as facts about the market — they reflect the board's state on the build date;
- English phrasing straight into a deliverable: the companion is written in English, and **the artifact is produced in the user's language**. It is a source, not an output template.

**Consistency with local material.** Where a companion figure disagrees with `evidence-2026.md` or `kb/51-numbers.md`, priority goes to the one with a named primary source and a stated evidence level. Both sides must carry their reliability tag.
