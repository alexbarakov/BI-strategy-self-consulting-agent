---
id: numbers-registry
title: Numbers registry - every figure in the base with its level of trust
type: index
purpose: find the figure you need and know in the same second whether it survives a challenge
---

# Numbers registry

Every quantity that appears in the knowledge base, in one place, with a reliability tag and the atom that holds its context. The point is speed: an agent building an argument should find the number **and see immediately** whether it can be relied on in public.

## The five reliability tags

| Tag | Meaning | Quotable as fact |
|---|---|---|
| `measured` | measured in a named setting, method stated | yes, naming the setting |
| `benchmark` | a reproducible external study or benchmark | yes |
| `vendor` | the vendor's own measurement, or a seller-commissioned survey | **no** - only with the measurer named |
| `author-estimate` | the author's expert judgement, marked as such | as an estimate, not a fact |
| `disputed` | widely circulated, the sourcing does not hold up | **no** |

The scale matches the companion's registry at [DG Strategy](https://github.com/alexbarakov/DG-strategy-self-consulting-agent) - figures move between the repositories with their tag attached.

**The transfer rule.** The tag travels with the number. If a `vendor` figure reaches an artifact, the sentence naming who measured it goes with it. The mark is never dropped in paraphrase.

**On anonymized cases.** Some measurements are given as an order of magnitude ("roughly threefold", "about two thirds") rather than an exact figure, deliberately. Such rows are tagged `measured` with a caveat in the source column: the mechanics transfer, the threshold is set from your own baseline.

---

## The BI content lifecycle

| Value | Claim | Tag | Source | Atom |
|---|---|---|---|---|
| 88% | of reports die within 3 months | `benchmark` | analysis of 34.305 dashboards, Roman Bunin | [[bi-value-illusion]] |
| 10% | live on minimal traffic - single or double digits of users per month | `benchmark` | same source | [[bi-value-illusion]] |
| 2% | deliver a stable, intended result | `benchmark` | same source | [[bi-value-illusion]] |
| ~50 days | median dashboard lifetime | `benchmark` | same source | [[bi-value-illusion]] |
| 136 days | the same in units with mature practices | `benchmark` | same source | [[bi-value-illusion]] |
| 22–25% | share of BI/analytics users, survey average 2015-2022 | `benchmark` | BARC / Eckerson Group | [[bi-value-illusion]] |
| 12.5–15% | the same, median - no growth over seven years | `benchmark` | BARC / Eckerson Group | [[bi-value-illusion]] |

## Demand and coverage

| Value | Claim | Tag | Source | Atom |
|---|---|---|---|---|
| 20–40% | of domains cover 60-85% of use cases | `benchmark` | the Pareto rule over domains, course material | [[info-supply-demand]] |
| +3 / +2 / +2 / +1 | prioritization scoring: three roles / a CxO among requesters / no in-house resource / a 2 FTE effect | `author-estimate` | practice, a coarse scale | [[info-supply-demand]] |
| 3.0 / 2.0 / 1.0 / 0.5 / 0.25 | the Impact scale in RICE | `benchmark` | canonical RICE | [[info-supply-demand]] |
| 1.0 / 0.9 / 0.7 / 0.5 | the Confidence scale in RICE | `benchmark` | canonical RICE | [[info-supply-demand]] |
| ~70% | an example of domain completeness at "usable with limitations" | `author-estimate` | a worked example on the worksheet | [[critical-data-status]] |

## The semantic layer and text-to-SQL accuracy

| Value | Claim | Tag | Source | Atom |
|---|---|---|---|---|
| ~40% | text-to-SQL accuracy on real enterprise schemas | `benchmark` | a summary across independent measurements | [[semantic-layer-evidence]] |
| **10.1% versus 86.6%** | GPT-4o on Spider 2.0 versus Spider 1.0 | `benchmark` | [spider2-sql.github.io](https://spider2-sql.github.io/), [arXiv 2411.07763](https://arxiv.org/abs/2411.07763) · **verified 2026-08-29** | [[semantic-layer-evidence]] |
| **21.3% versus 91.2%** | o1-preview in a code-agent frame on Spider 2.0 versus Spider 1.0 - the paper's headline comparison | `benchmark` | same source · verified 2026-08-29 | [[semantic-layer-evidence]] |
| 85–95% | accuracy with a semantic layer, with an honest refusal instead of a lie | `benchmark` | paired measurements | [[semantic-layer-evidence]] |
| 16.7% → 54.2% | a corporate schema of 199 tables, without semantics -> with semantics | `benchmark` | paired measurement, data.world | [[semantic-layer-evidence]] |
| 0% → 38.7% | the same schema, hard questions: none are solved on the raw schema | `benchmark` | paired measurement | [[semantic-layer-evidence]] |
| 8.3% → 78.3% | pharma data, 60 queries | `benchmark` | JAMIA Open | [[semantic-layer-evidence]] |
| 36% → 52% | a real warehouse, 2.730+ columns; column descriptions mined from query logs | `benchmark` | MotherDuck | [[semantic-layer-evidence]] |
| 84.1% → 100% | a 2026-generation model: SQL generation versus the layer | `vendor` | a semantic-layer vendor's own measurement | [[semantic-layer-evidence]] |
| near-100% | dbt semantic layer 2026 benchmarks on covered queries | `vendor` | dbt Labs | [[semantic-layer-evidence]] |

## AI in data processes

| Value | Claim | Tag | Source | Atom |
|---|---|---|---|---|
| 52.7% → 95.0% | PII classification: regex versus the model, 1.000 documents | `benchmark` | independent measurement | [[ai-in-data-processes]] |
| 0% | the share regex catches in the "confidential" category | `benchmark` | same source | [[ai-in-data-processes]] |
| 35.5% → 95.4% | deduplication precision: blocking plus the LLM only on disputed pairs | `benchmark` | independent measurement | [[ai-in-data-processes]] |
| $0.04 | the cost of processing a dataset under that scheme | `benchmark` | same source | [[ai-in-data-processes]] |
| 88.7% versus 51–56% | schema matching against COMA and CUPID, only on complex schemas | `benchmark` | independent measurement | [[ai-in-data-processes]] |
| 90.2% versus 64.6% | parsing complex tables and scans with variable layout | `benchmark` | independent measurement | [[ai-in-data-processes]] |
| до 99% | ordinary OCR on fixed forms - cheaper and more accurate than the model | `benchmark` | same source | [[ai-in-data-processes]] |
| 76% → 87% | SQL translation between dialects: raw versus translation with execution feedback | `benchmark` | independent measurement | [[ai-in-data-processes]] |
| 19.6% versus 6.3% | error rate in descriptions: model versus human | `disputed` | **the 2026-08-29 check did not confirm this**: [arXiv 2411.05409](https://arxiv.org/abs/2411.05409) — it is "Web Archives Metadata Generation with GPT-4o", about web archive metadata, and the claimed figures are not in the abstract. The direction agrees ("human curated metadata maintains an edge"); the specific percentages do not. **Do not quote until checked against the full text** | [[ai-in-data-processes]] |
| 23.75% → 48.25% | incident root cause: raw telemetry versus fused sources | `benchmark` | independent measurement | [[ai-in-data-processes]] |
| −60…−80% | "fewer false positives" when generating data quality rules | `vendor` | vendor blogs only, no independent data | [[ai-in-data-processes]] |
| 19% slower while believing they were 20% faster | a controlled measurement of developer productivity | `benchmark` | [METR, 2025-07-10](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), [arXiv 2507.09089](https://arxiv.org/abs/2507.09089) · **verified 2026-08-29**. Caveats: 16 developers, 246 tasks, early-2025 tooling; **METR itself labels the result historical** and published new data in February 2026. A counter-RCT reports a 21% speed-up - the divergence is attributed to task complexity | [[ai-in-data-processes]], [[ai-time-saving-trap]] |

## Context and the context layer

| Value | Claim | Tag | Source | Atom |
|---|---|---|---|---|
| 18 models | quality degrades as input grows, long before the window fills; **the decline is continuous, not a cliff** | `benchmark` | [Chroma, Context Rot](https://www.trychroma.com/research/context-rot) · **verified 2026-08-29** | [[context-layer-market]] |
| 200K / 50K | a model with a 200K window shows noticeable degradation already at 50K | `benchmark` | same source · verified 2026-08-29 | [[context-layer-market]] |
| **40-50% of the window** | the threshold past which F1 collapses from 0.55 to 0.3 - **a share of the window, not an absolute token count** | `benchmark` | [arXiv 2601.15300](https://arxiv.org/abs/2601.15300), Qwen2.5-7B · **verified 2026-08-29** | [[context-layer-market]] |
| +38% | "SQL accuracy uplift" across 174 queries | `vendor` | Atlan, its own measurement and methodology | [[context-layer-market]] |
| ~90% | "agent accuracy" | `vendor` | a DataHub release, methodology not published | [[context-layer-market]] |
| 87% | "descriptions no worse than a human's" | `vendor` | Atlan; independent checking finds three times as many errors | [[context-layer-market]] |
| 82% / 61% / 57% / 87% / 88% | survey percentages about context platforms | `disputed` | the survey was commissioned by the seller; internally contradictory: 88% "the platform exists" and 87% "the data is not ready" | [[context-layer-market]] |
| 77% | "of teams believe RAG alone is not enough" | `disputed` | the same survey | [[context-layer-market]] |
| 0.25–1 FTE | platform engineer load for an open-source solution | `author-estimate` | a total cost of ownership estimate | [[context-layer-market]] |
| ~$50K+ / $150–500K / ~$198K | the order of annual pricing for commercial platforms | `vendor` | public vendor price indications | [[context-layer-market]] |
| threefold / threefold / an order of magnitude | the effect of governed context: tokens, agent steps, response time | `measured` | internal measurement, anonymized - calibrate from your own baseline | [[context-governance]] |
| under an hour per week | the verify-gate time budget for a domain's BI partner | `measured` | internal practice, anonymized | [[context-governance]] |

## The domain knowledge base and AI readiness

| Value | Claim | Tag | Source | Atom |
|---|---|---|---|---|
| a little over threefold | the rise in auto-answer accuracy after connecting a populated knowledge base | `measured` | internal measurement, anonymized | [[domain-knowledge-base]] |
| dozens of questions | the starting size of a domain golden set | `author-estimate` | launch practice | [[domain-knowledge-base]] |
| ~11 criteria | formal completeness of the domain knowledge base | `measured` | an internal metric | [[domain-knowledge-base]], [[ai-ready-domain-score]] |
| ≥70% / <5% | the target verified share and the acceptable false-accept rate | `author-estimate` | operating-model target thresholds | [[context-layer-market]] |

## Gartner and market forecasts

| Value | Claim | Tag | Source | Atom |
|---|---|---|---|---|
| 40% | of agentic AI projects will be cancelled by end of 2027 | `vendor` | [Gartner, press release 2025-06-25](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027) · **verified 2026-08-29**. Based on a poll of 3.412 webinar attendees, January 2025; an analyst forecast, not a measurement | [[ai-in-bi-approaches]] |
| +80% / −60% | GenAI accuracy and cost when semantics is prioritized, by 2027 | `vendor` | Gartner | [[ai-in-bi-approaches]] |
| 50% | of agent failures by 2030 due to insufficient runtime-enforcement governance | `vendor` | Gartner | [[ai-in-bi-approaches]] |
| 7.9 / 10 | Data Quality and Data Security top the 2026 priorities | `benchmark` | BARC, practitioner survey | [[ai-in-bi-approaches]] |

## The 2026 field sample (n=12)

The whole group is `measured`, with a caveat: **self-reported, and the sample is biased** (participants of a strategy course). Not industry statistics.

| Value | Claim | Atom |
|---|---|---|
| 20% – 90% | adoption spread: share of target users opening BI at least monthly | [[participants-2026-benchmark]] |
| 3 – 100 | warehouse team size, median ~12 | [[participants-2026-benchmark]] |
| 3 – 400 | number of BI solution builders, median ~10 | [[participants-2026-benchmark]] |
| 0 – 11 | data governance team size, median 2; **in 4 of 12 companies there is none at all** | [[participants-2026-benchmark]] |
| 0 из 12 | companies with a fully mature semantic layer | [[participants-2026-benchmark]] |
| 20% – 90% | subjective estimate of the ad-hoc share that could go to AI; median ~70-80% | [[participants-2026-benchmark]] |
| 4 из 10 | share of companies naming semantics and metrics as the main pain | [[pain-fronts-2026]] |
| 4 из 10 | the same for data culture and for speed/resources | [[pain-fronts-2026]] |
| 15–25% | estimated ceiling of queries an assistant can close - **at odds with the 70-80% above** | [[insight-management]] |

**A conflict worth holding in mind.** The participants' subjective estimate (70-80%) and the practical ceiling (15-25%) differ fourfold. Both rows are kept deliberately: the divergence is the content. The most honest phrasing in the sample explains the gap - "the high estimate reflects the fact that the basic data need is not yet met".

## Operational reference points

| Value | Claim | Tag | Source | Atom |
|---|---|---|---|---|
| 5 + 5 | how many performance metrics to take: primary and secondary | `author-estimate` | the method's selection rule | [[bi-project-metrics]] |
| 0–4 | the Health Check factor scale | `benchmark` | the canonical method | `question-bank.md` |
| +1 level per year | the honest default for target maturity growth | `author-estimate` | the anti-optimism rule | `review-gates.md` |
| 3 weeks | the horizon of a new analyst's onboarding plan | `author-estimate` | the method's template | [[onboarding-plan]] |
| 3+ / 2+ | experts per critical / ordinary domain | `author-estimate` | the competency backup strategy | [[bi-competency-matrix]] |
| 20% | the share of catalog objects worth curating | `author-estimate` | the "do not boil the ocean" rule | [[data-catalog-pitfalls]] |
| 1 quarter | target duration of a core-layer deep dive in a domain | `measured` | internal practice | [[core-layer-project]] |
| 2 из 4 | minimum conditions to move from MVP to a governance programme | `author-estimate` | the launch rule | [[dg-launch-path]] |
| 50–60% | the industry norm for compute utilization | `benchmark` | an industry reference point | [[infra-billing]] |
| half the norm | observed utilization in the worked case | `measured` | internal measurement, anonymized | [[infra-billing]] |

---

## What has been checked against primary sources

The 2026-08-29 pass covered eight load-bearing figures. Four discrepancies, all now reflected in the tables above:

| What the base said | What the check produced |
|---|---|
| Spider 2.0: "36% vs 86%" | **10.1% vs 86.6%** for GPT-4o; the paper's headline comparison is 21.3% vs 91.2% for o1-preview. The old figure was a transcription error from a slide |
| Context rot: "it falls in a step" | Chroma records **continuous** decline. The "cliff" comes from a different paper, and its threshold is **a share of the window (40-50%)**, not an absolute 51-64K tokens |
| Descriptions: 19.6% vs 6.3%, tagged `benchmark` | The cited arXiv paper is about web archive metadata and the figures are not in the abstract. Downgraded to `disputed`, **must not be quoted** |
| METR 19% / 20%, with no caveats | Confirmed, but substantial caveats were added: n=16, early-2025 tooling, the authors label the result historical, and a counter-RCT points the other way |

Подтвердились без правок: Gartner 40% (с уточнением, что это прогноз на опросе, а не замер), Chroma «18 models» и «200K окно, деградация на 50K».

**The rule this produces.** The `benchmark` tag is applied only after opening the primary source, never on the strength of what a slide said. Until then the figure lives as `author-estimate` - which is more honest than a `benchmark` that later fails to hold up in somebody else's presentation.

## How to maintain it

The registry is not generated - it is maintained by hand whenever an atom with a figure is added. Completeness check: if an atom carries a number that is absent here, it cannot be quoted in an artifact. Duplicates are not collapsed: the same number from two sources stays two rows, because their tags may differ.
