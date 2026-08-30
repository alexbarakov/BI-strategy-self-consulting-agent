---
id: ai-cases-in-prod
title: Two production AI cases in analytics - the anatomy of a working solution
type: case
source: "Course \"BI+AI strategy 26\", the \"Content management\" session, part 2 - internal cases"
confidence: verifiable (internal measurements)
origin: "an internal case walked through on the course; the numeric thresholds are anonymized - calibrate from your own baseline"
blocks: [4.3, 5, 6]
---

Two cases taken through to production. The value is not in the results but in **the construction of the safeguards**: both systems are built around constraints rather than around what the model can do.

## Case 1. A personal digest for the top audience

**The problem.** Heads of verticals and categories and the C-level run into data delays, refresh dashboards by hand and switch between cuts; when a metric moves they go to the analysts with "why".

**The solution.** A bot with an admin panel inside the corporate messenger. Subscription to reports in your own cuts (vertical / macro category / local category). On a cron **after the data refreshes**, a personal digest: charts from BI, factor analysis by an internal LLM, a summary of threads from the incident channels, and a link to the dashboard for the relevant cut. Follow-up questions to the bot pass through a **judge gate against invented data**. A Python service, an internal model for secure data.

**The result.** Time to insight fell roughly thirtyfold - from tens of minutes to a couple - by saving the monitoring of readiness, the trip into BI, the filtering, the analysis and the correspondence with an analyst. Dozens of subscribers, dozens of reports a day, and most subscribers use the AI conclusions and summaries.

**What is well constructed here:** the trigger is tied to the data refresh event, not to a schedule set by guesswork; incident context is blended in automatically; answers to free-form questions pass a separate gate.

## Case 2. An agent that answers "why did the metric move"

**The problem.** Analysts and business developers spend **hours on each "why did the metric move" question**: manually assembling context from BI, the semantic layer, the metadata catalog, the messenger and the query engine before they can start thinking.

**The solution.** The agent answers in tens of minutes instead of hours, orchestrating about a dozen skills: a significance check · decomposition by segment · LMDI factor analysis of the funnel · parallel scanners over A/B tests and the messenger · external factors (weather, marketing, search queries). The output is a report with the top segments, the factors and two to four hypotheses about the cause.

**The key safeguard is RELATIVE-ONLY mode:** the model sees only percentages, percentage points and z-scores, never absolute values; all aggregation happens in Trino / DuckDB / Python. This protects against both leaking sensitive absolutes and hallucinating numbers.

**The result.** Working an anomaly through to a hypothesis got several times faster · **a substantial average time saving**, measured as baseline versus after on UAT · **explanation quality around two thirds** per a separate LLM judge - the authors phrase this as "room to grow" · metric-resolution accuracy measured on a golden dataset separately for the two modes, and noticeably lower in the strict mode than in the lenient one. Shipped as a plugin by a single team, with deterministic evals.

## What carries over into a strategy

1. **Compute in code, not in the model.** All aggregation outside the LLM; the model only receives relative values. That removes two risks at once - leakage and arithmetic hallucination.
2. **A judge gate is mandatory** for free-form questions, or the bot starts inventing data.
3. **Metrics measure delivery, not feeling.** The time saving was measured as baseline versus after on UAT; explanation quality is judged by a separate judge; metric resolution accuracy is measured on a golden dataset. Exactly what [[ai-time-saving-trap]] and `evidence-2026.md` §1 require.
4. **Quality around two thirds is normal for a start, and they say so out loud.** Honestly publishing an imperfect number is a sign that the measurement is real rather than fitted.
5. **The baseline was measured before launch.** Without measuring "how long this used to take", any percentage saving is meaningless.

Links: [[insight-management]] · [[ai-time-saving-trap]] · [[ai-ready-domain-score]] · [[ai-in-bi-approaches]]
