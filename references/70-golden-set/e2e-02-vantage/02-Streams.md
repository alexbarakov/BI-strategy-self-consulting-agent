[[index]] · Streams

# 🧭 Section 2. Streams of change

## The stack-rank and the freeze order

Priority runs governance → trusted data → AI readiness → BI content → self-service. Cut right to left.

| # | Stream | Rank | Frozen |
|---|---|---|---|
| **S4** | Honest measurement of the assistant | AI readiness, but **first in time** | never — it is what makes the commitment defensible |
| **S1** | One definition per commercial metric | governance + trusted data | never |
| **S3** | A guaranteed perimeter for the assistant | AI readiness | perimeter 1 never; expansion beyond it freezes second |
| **S2** | Extending the trusted core to 6 domains | trusted data | domains 5–6 freeze third |
| **S5** | Dashboard hygiene | BI content | **freezes first** |

S4 sits ahead of S1 in time although it ranks lower: the board review is in four months and the semantic layer will not be finished by then. What can be finished by then is an honest number and a restated commitment. This ordering came out of the judge stage — see the rework log in [`e2e-02-vantage.md`](../e2e-02-vantage.md).

---

## S1 · One definition per commercial metric

**Description.** Twelve metrics that reach the board get exactly one definition, expressed in code, with a named owner. Everything else keeps its current life until the twelve are done.

**Justification.** Closes [[01-Context#P1 · Three competing definitions of the twelve commercial metrics]] and answers [[01-Context#T1 · Text-to-SQL on a real enterprise schema is around 40%, and a semantic layer moves it to 85–95%]]. Chosen over a full semantic-layer programme because twelve metrics can be finished inside the horizon and a full layer cannot.

**Boundaries.** Not a semantic layer for all metrics. Not a metric store purchase. **Not the unification of country-level variance:** where a country computes differently for regulatory or commercial reasons, we standardize the *description of the difference*, not the number.

**Owner.** Head of Data Platform. **Dependencies.** Two metric owners at 20% from commerce and ops — part of the ask to the sponsor.

---

## S2 · Extending the trusted core to six domains

**Description.** From 3 certified domains to 6, chosen by reuse rather than by pain: the entities that the most queries touch.

**Justification.** Closes [[01-Context#The chain breaks|the core half of chain break 1]] and is the precondition for widening the assistant's perimeter beyond domain 1.

**Boundaries.** Not the remaining five domains this horizon. Not a rebuild of the three that already exist.

**Owner.** Data Platform lead. **Dependencies.** None outbound; S3's expansion depends on it.

---

## S3 · A guaranteed perimeter for the assistant

**Description.** The assistant stops answering everything. Inside the perimeter — the twelve metrics on certified sources — it answers with provenance and a trust marker. Outside it, it refuses and routes to an analyst with a stated turnaround. It also gets its own identity instead of the shared service account.

**Justification.** Closes [[01-Context#P2 · The assistant answers questions it cannot answer correctly]] and [[01-Context#P5 · The assistant runs under a service account with warehouse-wide read]]; addresses [[01-Context#T2 · The character of the error changes with a semantic layer]] and [[01-Context#T3 · An agent is a new class of identity]].

**Boundaries.** Not a switch-off, and not a rebuild. Not finance data this year.

> ⚠️ Narrowing will be read as a rollback. The number that answers it is in [[03-Initiatives]]: how many of today's questions fall outside perimeter 1, and where they go instead.

**Owner.** Assistant PM. **Dependencies.** S1 for the definitions, S4 for the evidence that narrowing helped.

---

## S4 · Honest measurement of the assistant

**Description.** A golden set built from real logs, an accuracy baseline, provenance on every answer, and a reporting unit that is not call volume. The public commitment is restated in that unit before the board review.

**Justification.** Closes [[01-Context#P4 · The assistant's success is measured by call volume]]. This is the stream that makes every other one defensible: without a baseline, no claim about improvement can be made in four months.

**Boundaries.** Not an eval platform purchase. Sixty questions, not six hundred.

**Owner.** Head of Analytics. **Dependencies.** Requires the CPO's agreement to restate the number — the first item in the ask to the sponsor.

---

## S5 · Dashboard hygiene

**Description.** An owner field made mandatory, and automatic archiving of dashboards with no users and no updates. Nothing else.

**Justification.** Partially closes [[01-Context#P6 · 912 dashboards, no owner field and no archiving]]. Ranked last deliberately: 912 dashboards are a real problem and not this year's most expensive one.

**Boundaries.** No certification programme. No health score. No review of the surviving dashboards.

**Owner.** Data Platform lead. **Dependencies.** None. **Freezes first.**

---

## Traceability

| Problem | Covered by |
|---|---|
| P1 · Three competing definitions | S1 |
| P2 · The assistant answers what it cannot | S3, S4 |
| P3 · Parallel spreadsheets | S1 + S3 indirectly — the outcome metric is in [[04-Goals]] |
| P4 · Measured by call volume | S4 |
| P5 · Shared service account | S3 |
| P6 · 912 dashboards | S5, partially |
| P7 · Governance at 0.5 FTE with no mandate | **not covered by a stream** |

**P7 is left uncovered deliberately, and this is the document's least comfortable line.** Headcount is frozen, so a governance function cannot be staffed this year. Instead of declaring one and not resourcing it, the mandate is attached to the twelve metrics: their owners are named individually and their decisions are binding for those twelve only. That is narrower than governance and it is real. The wider question returns when the hiring freeze lifts.

Bottom-up: every stream references a named problem. No orphan streams.

---

→ [[index]] · [[01-Context]] · [[03-Initiatives]]
