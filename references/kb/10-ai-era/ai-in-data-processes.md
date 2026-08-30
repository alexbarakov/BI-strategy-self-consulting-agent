---
id: ai-in-data-processes
title: Where AI actually works in data management - routing, not replacement
type: evidence
source: "Course \"BI+AI strategy 26\", Day 6; expanded in references/evidence-2026.md §2"
confidence: mixed - the level is stated per row
blocks: [2, 4.1, 5]
---

The one regularity the method considers dependable:

> The closer the task is to "make sense of meaning", the better the result. The closer it is to "give a guarantee", the worse. **What wins is not replacing the process but routing it.**

## Works - the model sees meaning where a rule is blind

| Task | Measurement | Comment |
|---|---|---|
| **PII and confidentiality classification** | 52.7% -> 95.0% | regex versus the model on 1,000 documents; in the "confidential" category regex scores exactly 0% |
| **Entity matching, deduplication** | 35.5% -> 95.4% precision | cheap blocking plus the LLM only on disputed pairs; ~$0.04 per dataset |
| **Schema matching during integration** | 88.7% versus 51-56% | against COMA and CUPID; **the win exists only on complex schemas** - on simple ones the classics are no worse |
| **Parsing complex tables and scans** | 90.2% versus 64.6% | variable layout; **on fixed forms ordinary OCR reaches up to 99% and costs less** |

## Works only under verification - do not accept the result without an executable check

| Task | Measurement | Comment |
|---|---|---|
| **SQL translation between dialects** | 76% -> 87% | raw translation versus translation with feedback from execution errors |
| **Descriptions and metadata** | 19.6% versus 6.3% error rate - `disputed`, **do not quote** | model versus human; the cited source did not survive the 2026-08-29 check (see `51-numbers.md`). The direction holds - a human-curated description keeps an edge - but the percentages are unconfirmed. Measure the share a steward accepts without edits |
| **Pipeline code** | speed up, stability down | DORA-2025: AI amplifies a mature pipeline and chaos alike - the bottleneck moves into review |

## Overrated or unproven - the figures are vendor-supplied or absent

| Task | Measurement | Comment |
|---|---|---|
| **Incident root cause** | 23.75% -> 48.25% | raw telemetry versus fused sources; **hand over ranked evidence, not a verdict** |
| **Generating data quality rules** | no independent data | "60-80% fewer false positives" appears only in vendor blogs; measure your own false-positive rate in shadow mode for two weeks |

## The routing rule

**The deterministic layer takes the bulk volume, the model takes the disputed cases.** And do not measure the effect by the team's self-assessment: in a controlled measurement developers turned out to be **19% slower while convinced they had become 20% faster**.

The same rule explains the economics: an LLM on the disputed 5% of pairs, with cheap blocking on the rest, delivers both the accuracy and a cost of $0.04 per dataset.

Links: [[data-team-pain-points]] · [[ai-time-saving-trap]] · [[data-catalog-pitfalls]] · [[ai-in-bi-approaches]]
