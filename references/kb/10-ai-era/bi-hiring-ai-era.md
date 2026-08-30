---
id: bi-hiring-ai-era
title: Hiring into BI in the AI era - grade discovery and what to do about the vanishing juniors
type: method
source: "Course \"BI+AI strategy 26\", Day 9 - internal practice"
confidence: verifiable (an internal process)
origin: "an internal case walked through on the course; the numeric thresholds are anonymized - calibrate from your own baseline"
blocks: [6, 7]
---

## What has changed in a BI developer's work

- **AI-first: the LLM is in the daily cycle** - from SQL to marts and documentation. A developer's value is getting a correct result with any tool while **keeping quality under control**.
- **The bottleneck is review and requirements.** Code gets written faster; what decides the outcome is the quality of review, requirements analysis and an understanding of value. The hiring focus shifts from "can they build it by hand" to **"will they review the result"**.
- **The SQL skill profile has shifted.** Writing by hand from scratch is no longer the main case. What dominates is reading other people's code, debugging, reviewing LLM output and defending decisions in conversation.
- **The competency matrix has already been rewritten for AI while hiring stayed the same** - the process tests hard skills "in words" and cannot see AI at all. The new concept exists to close that gap.

## Five principles of the new hiring concept

1. **Grade discovery** - one process with rising difficulty. **The grade is determined by the ceiling at which the candidate starts to flounder, not by the CV.**
2. **A 1:1 tie to the matrix** - each interview block closes specific competencies; **there are no blocks "for a general impression"**.
3. **Hard skills through practice, soft skills through a case** - ETL and visualization through artifacts produced in the moment; the product mindset through observation in a case, not through questioning.
4. **AI-first with quality control** - the LLM is allowed on the technical tasks, because that is the real working mode. **The stop signals are refusing the LLM and trusting its output blindly** - equally bad.
5. **A pool of interviewers plus a scorecard** - rubrics for each block, with divergences calibrated; the AI harness removes the routine of recording. **The recommendation is min(hard, soft)** - confirming a grade requires a result in both halves, which protects against both inflation and deflation.

*The AI harness:* interview recording and transcription, automatic task checking, an LLM agent that produces conclusions against the matrix competencies.

## The funnel

HR screening -> **the technical session (new)** -> **the case section (new, roughly half again as long as the technical session)** -> the final with the hiring manager -> culture fit, unchanged. Both new sections fit inside the overall limit on the technical part that was set before the redesign - that was a design constraint, not a consequence.

The grade is unknown at entry; the process determines it. All candidates take one route, with difficulty rising inside the sections. **The final word on grade rests with the hiring manager; the technical sections give grounds, not a verdict.**

## An honest coverage map - what the process tests reliably and what it does not

| Competency | Where it is tested | Reliability |
|---|---|---|
| SQL/DWH | technical session: 3 tasks plus an oral debrief | reliable at L1-L2, a signal at L3 |
| ETL | the case, phase 2 - the data model | reliable at L1-L2; L3 via portfolio |
| The BI tool | the case - design patterns, not the UI | **a signal at L1-L2 only** |
| Visualization | a dashboard critique, a mock-up in the case if there was time | reliable at L1-L2 |
| Python | **not tested - a risk zone on timing** | not tested |
| Soft skills and BI project | the case (observation) plus a behavioural block | observation |
| LLM competence | the debrief plus the behavioural block | a signal at L1-L3 |

Publishing the process's limitations alongside it is rare and a sign of maturity: "knowledge sharing" is not tested at entry, being non-critical for hiring, and the AI-first mindset is monitored through behavioural questions.

## What still matters more than technical skill

> Engagement, intrinsic motivation, a willingness to do business analysis of data and to produce design that is not embarrassing on day one are **slightly more important than technical skills**. A BI product can be learned; SQL can be built up.

The classic set of blocks: a projective interview (soft skills and business sense) · a practical task on a BI product **even if the candidate does not know it** (motivation, the ability to get up to speed fast, basic design skill) · a technical interview on SQL.

## A risk worth naming out loud: the battle of the agents

> The candidate carpet-bombs with generated CVs, while the recruiter scores with agents.
> The employee generates a report and artifacts for the performance review, while managers run the review through agents.

Both loops hollow the process out from either end. Hence the requirement for artifacts produced in the moment and an oral debrief.

## The vanishing junior-to-middle tier - and what to do instead of cutting

Compressing factory teams down to two or three people creates not only a saving but a **staffing risk** that has to be managed deliberately.

**The risk if left alone:** the entry route into the profession disappears for juniors and middles · in three to five years there is nobody to grow into senior · **hollowing out - an agent operator on intellectual load all day with no pauses**.

**What to do instead:** move juniors into business data engineer and domain curator roles rather than letting them go · grow them **through reviewing AI outputs** rather than through routine · **deliberately keep some routine as ballast** · retrain them on semantics, the domain knowledge base and agent development.

> Compressing teams is not only about cutting; it is about a new growth trajectory: the agent takes the routine and people move towards meaning, the domain and oversight of quality.

This is the strongest candidate for a strategy's change management section: it answers the question HR and the team will ask, and turns a cut into a retraining.

Links: [[bi-competency-matrix]] · [[bi-org-structure]] · [[ai-in-data-processes]] · [[action-plan]]
