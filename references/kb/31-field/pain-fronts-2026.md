---
id: pain-fronts-2026
title: Three fronts of BI project pain - a 2026 field cut
type: benchmark
source: "The Day 1 interactive of the \"BI+AI strategy 26\" course, n=10 companies (A-J); consistent with the pre-course survey, n=12"
confidence: verifiable (participant self-report)
blocks: [1, 2]
---

Free-form answers to "what problems do you feel in your company when rolling out and developing BI" collapse into three fronts. The plot is the same throughout: **without a single metric methodology and a data culture, an AI foundation does not get built**.

## Front 1. The semantic layer and metrics - 4 of 10

> "And yes, the metrics are calculated differently."
> "Metrics are not reused from the metric catalog; they are recalculated from scratch each time."
> "There is no semantic layer, no data catalog, no readiness for AI - no semantics and no labelling."

## Front 2. The data culture - 4 of 10

> "The business does not understand what data the company holds or why it should be managed."
> "A low culture of working with data."
> "The business does not take responsibility for metric methodology."

## Front 3. Speed and resources - 4 of 10

> "High time to market on marts - analysts work with whatever data is easier to reach, breaking the rules."
> "We cannot keep up with what the business wants."
> "A small BI headcount against a wish to put everything in order."

## Adjacent, named less often

**Content hygiene and technical debt.** "Walls of code in the data sources"; "production-grade reports creeping into the sandboxes"; "junk reports in production"; "scattered reports across different BI tools, legacy in QlikView and Qlik Sense".

**The value and positioning of BI.** "BI in a non-revenue unit - you cannot compute the effect on the business"; "the business does not buy the value of data roles: DataOps, stewards, QA".

**One-offs, but sharp.** Cross-domain data availability · import substitution simultaneously with rolling out AI · no single strategy while developers on the same grade differ widely in skill · access, performance and migrations between BI platforms · self-service development by business users with no criteria ("we gave everyone access, now we have to sort it out").

## How to use it

1. **As a calibration of priority.** If a participant's pain does not fall into any of the three fronts, it is worth asking whether it really is the most expensive pain or merely the most recent.
2. **As an argument against skipping ahead.** The three fronts are exactly the first three links of the chain `core -> semantic -> context -> AI accuracy -> self-service`. A company whose metrics and culture hurt physically cannot start with an agent.
3. **As workshop material.** Anonymous quotes take away a participant's sense that their problem is unique and speed up a [[painpoints-analysis]] session considerably.

## Separately: a causal chain named by a participant

> "High time to market on marts -> analysts work with whatever data is easier to reach -> breaking the rules."

This is the best short argument against governance-first without investing in speed: **a rule that costs more than going around it will not be followed**. In a strategy it follows that governance initiatives and time-to-market initiatives have to move as a pair, not in sequence.

Links: [[participants-2026-benchmark]] · [[painpoints-analysis]] · [[bi-value-illusion]] · [[info-supply-demand]]
