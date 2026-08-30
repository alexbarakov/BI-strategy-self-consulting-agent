[[index|← BI+AI Strategy]] · 🏢 Severnaya

# 02. Streams of change

## Order and freeze

**Stack-rank:** S1 Trusted data → S5 Separating sensitive data → S2 Metric layer → S4 Platform migration → S3 Governed self-service.

We cut right to left. S5 sits second not by importance but because permissions cannot be opened without it: it blocks S3.

> **Why S1 comes before S2.** The first draft put the metric layer first. Review found a priority error: a metric layer on top of a contractor delivery model speeds up nothing — definitions get agreed and the data mart still takes three weeks. In-house engineering capability first, semantics on top of it second.

Freeze list — [[05-Risks#Freeze list]].

---

## S1 · Trusted data

**Description.** Our own layer of data marts for sales and stock: key entities described, refreshed on schedule, each with an owner and quality checks. Development moves from contractor tickets to an in-house engineer; the contractor stays on legacy support.

**Justification.** Closes [[01-Context#P2 · Data marts via the contractor]] — the company's most expensive pain: every data mart costs weeks and contract money. Addresses the forced-migration trend: a described model survives a platform switch, an undescribed one is rewritten. Without this stream the other four are unreachable: S2 has nothing to describe, S3 nothing to open, S4 nothing to move.

**Boundaries.** Out of scope: HR marts, financial reporting, logistics contractor data. Sales and stock only — the two entities that give the most reuse.

**Owner:** Head of IT. **Initiatives:** tagged `S1` in [[03-Initiatives]].

---

## S2 · Metric layer

**Description.** One definition per metric for the whole company, fixed in code and in the glossary rather than in the SQL of individual reports. We start with three disputed ones: average basket, stock turnover, margin.

**Justification.** Closes [[01-Context#P1 · Metrics disagree]] and removes the precondition behind [[01-Context#P3 · No data owners]]: agreeing a definition requires somebody who confirms it. Addresses the accuracy trend — the semantic layer is what an assistant needs to avoid returning a plausible wrong answer.

**Boundaries.** Out of scope: migrating every existing report onto the new definitions. Old reports live until their planned rework; new ones are built on the layer only.

**Owner:** Head of BI. **Depends on:** S1.

---

## S3 · Governed self-service

**Description.** Category analysts work on certified sources themselves, under a clear rule about what may be published and what goes to review.

**Justification.** Closes [[01-Context#P5 · Analyst skill varies widely]] and removes the load that keeps reproducing [[01-Context#P2 · Data marts via the contractor]]. Addresses the observation that self-service opened to everyone at once adds untangled content on top of untangled data.

**Boundaries.** We open one category at a time, not all at once. Out of scope: building reports for executives — that stays centralized.

**Owner:** Head of BI. **Depends on:** S1, S5.

---

## S4 · Platform migration

**Description.** Move to the domestic BI platform without rewriting logic: the described model first, the migration second.

**Justification.** Addresses the vendor-exit trend, which for us is already reality. The stream is justified not by the migration itself — it will happen regardless — but by its **order**: migrating after S1 moves a model, migrating before S1 moves a mess.

**Boundaries.** Platform choice is out of scope; it was made outside this strategy. Only sequencing and acceptance are in scope.

**Owner:** Head of IT. **Depends on:** S1.

---

## S5 · Separating sensitive data

**Description.** Loyalty programme personal data is separated from sales marts at the model and permission level. A category analyst sees segment behaviour but not individual identifiers.

**Justification.** Closes [[01-Context#P6 · Personal data inside sales marts]]. It did not exist in the first draft and appeared after the traceability check: the problem was named in the context and covered by no stream. Addresses the regulatory trend. **Blocks S3** — self-service cannot be opened before the separation is done.

**Boundaries.** Out of scope: revising consents and the legal side of the loyalty programme.

**Owner:** Compliance with IT. **Depends on:** S1.

---

## Traceability

| Problem | Covered by | Comment |
|---|---|---|
| P1 · metrics disagree | S2 | |
| P2 · data marts via contractor | S1 | most expensive, hence the first stream |
| P3 · no data owners | S2 | the owner is appointed as a precondition, not as a separate stream |
| P4 · usage not measured | S1 | the baseline measurement is in the first 90 days |
| P5 · analyst skill varies | S3 | |
| P6 · personal data in sales marts | S5 | added after the traceability check |
| Mobile access | — | deliberately uncovered, no demand |
| Demand forecasting | — | deliberately uncovered until a core layer exists |
