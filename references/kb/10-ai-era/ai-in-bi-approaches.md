---
id: ai-in-bi-approaches
title: Four approaches to AI in BI, and the Russian regulatory perimeter
type: pattern
source: "Course \"BI+AI strategy 26\", Day 1; \"AI in BI. Gromov's circle 2026\", russianbi.ru"
confidence: verifiable (the classification), vendor-measured (the vendor examples)
blocks: [5]
---

A spectrum from AI inside the platform core to an external autonomous agent. M. Lak's thesis, which the method accepts: **there is no silver bullet - the approach is chosen to fit the task and the regulatory perimeter**.

## The four approaches

| Approach | How it works | Strong | Careful |
|---|---|---|---|
| **Embedded** - a built-in service | AI in the BI core, working under the hood on any request, with no plugins. You open a dashboard and the AI explains the numbers right in the interface | reliability, legal cleanliness, deep integration | hard to swap the LLM without rebuilding the core, vendor lock-in |
| **Semantic layer** - on-prem over semantics | the AI core works only with meaning, never with raw data; everything on-prem. You ask for a metric in natural language and get an exact answer from the model, with no internet | complete data isolation, personal-data law compliance, works without a VPN | no charts (tables only), no proactive chains |
| **Assisted** - a UI helper | a plugin over the interface, helping with whatever is on screen right now. A side chat builds a chart from the current dashboard | simple and fast to roll out without changing the core | reactive, no multi-step autonomous chains |
| **Agentic** - an external AI-first agent | the agent lives outside and creates or changes reports, marts and SQL itself through MCP. "Assemble a sales report" and the agent writes the SQL and builds the dashboard | end-to-end automation, maximum flexibility | with a foreign LLM: sanctions risk and personal-data law exposure |

## The six layers where AI works in BI

1. **Access and comprehension** - natural-language querying, dashboard search, semantic search
2. **Data preparation** - ETL generation, cleansing, deduplication
3. **Semantics and metadata** - glossary, descriptions, lineage, synonyms
4. **Visualization and analysis** - NL2Viz, dashboard interpretation, root cause
5. **Planning and forecasting** - what-if, forecast models, optimization
6. **Quality and observability** - anomalies, proactive alerts, explanation

Each layer is assessed against the SPAR cycle and an autonomy level of 0 to 5 (Pascal Bornet's classification).

## The Russian perimeter: the choice is features by jurisdiction by geopolitics

- **Federal Law 152-FZ** - personal data must be localized in Russia; foreign cloud LLMs are off-limits for personal data
- **Federal Law 187-FZ (critical infrastructure)** - only Russian software from the register, for critical infrastructure
- **FSTEC order 117** - protection requirements, platform certification
- **Sanctions risk** - a foreign LLM with no Russian substitute carries a high risk of API blocking; on-prem plus a domestic LLM (GigaChat, YandexGPT, Qwen) is low

**The conclusion:** the approach is chosen to fit the type of organization (public sector / critical infrastructure -> large commercial -> small business), the regulatory perimeter and data maturity, not by a "best of" ranking.

## The global frame and the vendors' numbers

Gartner names three forces: AI-ready data and semantics · agentic analytics and decision intelligence · governance and AI TRiSM as the trust gate. The claimed figures (flagged: **vendor-measured**): 40% of agentic AI projects will be cancelled by end of 2027 because of cost, unclear value and weak risk control; 80% better accuracy and 60% lower GenAI cost when semantics is prioritized within AI-ready data, by 2027; 50% of agent failures by 2030 will come from insufficient runtime-enforcement governance.

Links: [[bi-toolset-landscape]] · [[ai-time-saving-trap]] · [[ai-ready-domain-score]] · [[data-utility-gap]]
