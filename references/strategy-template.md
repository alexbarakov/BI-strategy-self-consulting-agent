# The analysis frame — seven blocks

> **This is not the shape of the document.** The document is assembled along the six sections of
> `strategy-requirements.md` (context → vision → streams → initiatives → goals as metrics → risks).
> The seven blocks below are an instrument: you run the diagnosis and the working through them, the
> result is distributed across streams and initiatives, and the frame itself lives in the appendix
> (`appendix/91-Analysis-frame.md`). A block that reaches no stream is either unfinished analysis or
> a deliberate decision not to touch that area; the second is recorded under "what we do not do".

The canonical structure of a BI+AI strategy (the Data Nature method / Alex Barakov). Based on the **"BI Strategy Structure"** worksheet of the D&A Planner and on the course master deck. Seven substantive blocks across four phases. Reference files: `D&A Strategy & Tactics Planner [ENG].xlsx`, `BI Project Health Check.xlsx`.

## Phases (top level)

🔎 **AS-IS — analysis** = blocks **1–2** · 🛠️ **TO-BE — design** = blocks **3–6** · 🚀 **Transformation** = block **7**.
Show the phase map on the front page and in the diagnosis; mark each block with its phase in the breadcrumb.

## The shape of every block (important)

Not a "finished strategy" and not an empty menu, but **a dry, concrete draft plus the company's decisions**. In this order:

1. **Substance (dry draft).** Two to four sentences: what this block is about for this company, concretely, in as few words as possible. Grounded in the diagnosis.
2. **Contents.** A compact list of sub-elements (below), terse.
3. **Company questions → dependent projects.** A table: the question the company answers → which project or measure depends on that answer.
4. **Maturity gate.** Explicitly: what NOT to start without need or readiness; the condition "do this only if…". Never recommend a measure when there is no need or no foundation beneath it.
5. **Materials.** Links from the course material relevant to the block (session, Planner worksheet, Health Check category, internal wiki).

Rules: dry, concrete, no filler. Every measure is conditional, gated, never a default. The diagnosis is context; the choice belongs to the company.

---

## Block 1. Business foundation · AS-IS

**Contents:** business model and analytical use cases · data domain structure · map of data and analytics pains · metric tree · information supply-demand matrix · executive sponsorship.
**Materials:** Session 02 (BI Vision and supply-demand); Planner — `1. D&A PainPoints`, `1. Data Domains Classification`, `1. Info supply-demand matrix`; Health Check — category 1 (Connection with business).

## Block 2. D&A landscape assessment · AS-IS

**Contents:** the current D&A platform landscape · BI health and maturity assessment · BI and data tool usage analysis · industry landscape benchmarking · audit of data sources and their quality.
**Mandatory — a "🌐 External context: key trends" section**: Traditional → Agentic BI, headless BI (three layers), AI-ready governance, the evolution of Data Mesh into governed decentralization, and sobriety about AI. Generic, without the company's figures. A short version of the trends also goes into the 6-pager.
**Materials:** Session 03 (BI assessment and AI readiness); Health Check — all nine categories plus the AI-readiness overlay (`question-bank.md`); Planner — `1. Outside BI`, `1. Inside BI`.

## Block 3. Target operating model · TO-BE

**Contents:** the balance of centralization and self-service — operating model design · user classification · mapping personas to target interfaces and tools · practices for managing central BI · practices for managing self-service BI.
**Materials:** Session 04 (BI governance: self-service / guided / agentic); Planner — `1. User Classification and BI Models`, `2.3 SelfServ D&A Practices`, `2.4 Centralized D&A Practices`; Health Check — categories 4, 5.

**New in 2026:** there are now four channels — Centralized · Self-Service · Agentic · **Data app** (data entry, a scenario, an action). A data app requires the same attributes as a dashboard: an owner, certification, a health score. Plus **the agent as a separate identity** with its own keys and an allowlist of tools, rather than "the analyst's service account".

## Block 4. Process foundation · TO-BE

Three sub-blocks:

- **4.1 Data models management:** data source management · data quality management · data security management · metadata management · usage monitoring · participation in data governance. — Session 05; Planner `2.1 Data Mgmt processes/questionnaire`, `2.1 Critical data`; Health Check cat. 7.
- **4.1 new in 2026:** permissions at the level of a document fragment (checked before retrieval, not after) · deletion of derived objects, vectors included · contracts enforced through a CI gate on critical marts rather than run as a separate project.
- **4.2 BI report management:** development · validation · access management · promotion · certification · content usage monitoring. — Session 06; Planner `2.2 Content Mgmt Processes/questionnaire`; Health Check cat. 3.
- **4.2 new in 2026:** certification along two dimensions — **the object passport** (owner, health, description, usage; scales across all content) and **behavioural tests** (before/after release comparison, reconciliation against the source; expensive, therefore reserved for the critical core).
- **4.3 Insight management:** metric-to-decision modelling · insight generation · automation and delivery · advanced analytics · data literacy. — Sessions 06–07; AI analyst and insight bots.

## Block 5. Technology foundation · TO-BE

**Contents:** harmonizing the data and analytics platform · data engineering solution · **semantic layer (golden layer, metric store, glossary)** · subscription automation · integrations (messenger, DQ alerts, mobile) · **next-gen BI and the data assistant** · BI system administration and licence management.
**Materials:** Session 07 (the AI foundation: semantic layer, core, context) and Session 08 (agentic architecture, MCP, judge gates); `question-bank.md` cat. 6; Planner `2.5 BI & Around BI Tools`.

**New in 2026 — the context layer ("LLM wiki") on top of the triad.** Five layers: sources → collection → knowledge assembly → storage → serving on request, plus a feedback loop. The unit of storage is an atom with a passport (provenance, status, a reference to the original, a freshness TTL, an owner). The catalog is chosen as **the governance boundary**: a shared protocol does not carry permissions between catalogs. Serve the agent only what is relevant — because of context rot, "more context" makes the answer worse.

## Block 6. Operational foundation · TO-BE

**Contents:** regular management of the BI project · working standards · access permission matrix · BI service desk · BI competency matrix · BI project performance metrics · building and running the team.
**Materials:** Session 09 (BI operations, team, profession); Planner `3. Access Matrix`, `3. Regular Meetings`, `3. Rules and Standards`, `3. Newcomer onboarding plan`, `3. BI Project Metrics`; Health Check cat. 8, 9.

**New in 2026:** the block's metrics carry a prohibition on measuring the effect of AI by the team's self-assessment — measurement and self-assessment diverge to the point of changing sign. Only a golden set of questions, before and after.

## Block 7. Change management · Transformation

**Contents:** BI vision · planning strategic initiatives · tactical planning · goal setting. Also here: the action plan, the **stack-rank**, kill-gates, and the dual track.
**Materials:** Session 01 (the structure of a BI+AI strategy), Session 10 (metrics, kill-gates), Session 11 (action plan, dual track); Planner `4. Action plan`, `5. BI Vision`.

---

## Cross-cutting artifacts (front page or block 7)

- The diagnostic **scorecard** (0–4 maturity profile + top breaks) — keep it as its own page and link to it.
- The **stack-rank** of priorities (Governance → Trusted Data → AI readiness → BI Content → Self-service) with an explicit "what we freeze first".
- The **metric tree** (four Planner groups plus AI metrics).
- A **kill-gate** for at least one AI initiative.
- The **risk register** (the fragile chain AI → semantic layer → core → catalog; content chaos; governance without resource).
- The **dual track**: old BI plus new BI.
