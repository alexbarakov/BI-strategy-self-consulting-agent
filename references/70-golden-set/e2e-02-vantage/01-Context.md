[[index]] · Context

# 🌍 Section 1. Context

## 1.1 External context — trends

Six trends. Each carries the line "what follows from it for us"; a trend without one would be deleted.

### T1 · Text-to-SQL on a real enterprise schema is around 40%, and a semantic layer moves it to 85–95%
`benchmark` — paired measurements, one model, one question set, only the presence of semantics changes ([Spider 2.0](https://spider2-sql.github.io/); details in `kb/51-numbers.md`).

**For us:** our assistant has been running for eight months on a schema with no semantic layer at all. We have never measured which side of that range we are on. Until we do, every discussion about the assistant is a discussion about opinions.

### T2 · The character of the error changes with a semantic layer
`benchmark` — on a question it does not cover, a layer answers "I can't"; raw SQL generation returns a confidently wrong number in silence.

**For us:** our assistant has no refusal path. It answers every question, including the ones it should not. That is the mechanism behind the parallel spreadsheets, not a training problem.

### T3 · An agent is a new class of identity
`author-estimate`, consistent with the 2026 governance material — private access plus untrusted input plus an outbound channel is exploitable.

**For us:** the assistant reads the whole warehouse under one service account. Access reviews currently see one account, not 400 users.

### T4 · The market shifted from data catalogs to context platforms
`vendor` in its framing (measured by the sellers), `benchmark` in the underlying finding: quality degrades as input grows, long before the window fills.

**For us:** we do not have a catalog, and we should not buy a context platform to compensate for the absence of definitions. The order is definitions first, delivery of them second.

### T5 · Gartner: 40% of agentic AI projects will be cancelled by end of 2027
`vendor` — an analyst forecast built on a poll of 3,412 webinar attendees, not a measurement. Named causes: cost, unclear value, weak risk control.

**For us:** not grounds for an initiative, and not quotable as fact. Useful only as the register in which the board will ask its question in four months: what is this costing and what does it return.

### T6 · Compressed factory teams and the thinning junior tier
`author-estimate` — the routine moves to agents and the entry route into the profession narrows.

**For us:** inverted. We never had a factory team, so nothing compresses. What we do have is 40 analysts whose squads now expect them to review the assistant's output — a skill nobody has assessed them on.

---

## 1.2 Internal context — problems

Collected across four role groups. Each carries a symptom, evidence and a cost of inaction.

### P1 · Three competing definitions of the twelve commercial metrics
**Group:** analysts in squads, commerce.
**Symptom:** "active subscriptions" resolves differently in dbt, in the BI tool's layer and in the assistant's few-shot examples.
**Evidence:** `measured` — found by hand during the interview: three definitions, differing on paused subscriptions and on the last day of the month.
**Cost of inaction:** every number that reaches the board has to be reconciled by hand first. The reconciliation is currently done by two people in the week before each board meeting.

### P2 · The assistant answers questions it cannot answer correctly
**Group:** casual users, ops.
**Symptom:** no perimeter, no refusal, no provenance in the answer.
**Evidence:** `measured` — 31% of ad-hoc questions start in the assistant; accuracy has never been measured.
**Cost of inaction:** trust is spent down at an unknown rate on an unknown denominator. By the time it is visibly gone, it is not recoverable within a planning horizon.

### P3 · Ops leads keep parallel spreadsheets
**Group:** casual users.
**Symptom:** the shadow file is treated as the real number for weekly operations.
**Evidence:** `author-estimate` — reported in the interview by two of four ops leads; not counted. `[requires clarification]` — an audit of shared drives would close it.
**Cost of inaction:** the shadow file quietly becomes the system of record, and the warehouse becomes the place where numbers are argued with rather than taken from.

### P4 · The assistant's success is measured by call volume
**Group:** the central team, the sponsor.
**Symptom:** the growth chart shown at the investor day was a call chart.
**Evidence:** `measured` — 31% is a share of questions started, not of questions answered correctly.
**Cost of inaction:** the public commitment is stated in a unit that cannot be defended. A rise in calls with no rise in solved tasks is not a result, and the board will find that out in one question.

### P5 · The assistant runs under a service account with warehouse-wide read
**Group:** the data management team, security.
**Symptom:** entitlements are applied around the assistant, not inside its queries.
**Evidence:** `measured` — one account, one grant.
**Cost of inaction:** an access review cannot answer who read what. The first regulated-data question stops the assistant entirely, and that stop is not on our schedule.

### P6 · 912 dashboards, no owner field and no archiving
**Group:** the central team.
**Symptom:** nobody can say which of them are alive.
**Evidence:** `measured` — 912 objects; usage per object is not tracked.
**Cost of inaction:** the assistant is being asked to navigate a corpus that we ourselves cannot rank. Deliberately left mostly uncovered this year — see the traceability table in [[02-Streams]].

### P7 · Data governance is one person at half-time with no mandate
**Group:** the data management team.
**Symptom:** no policy is signed, and no decision can be made stick across squads.
**Evidence:** `measured` — 0.5 FTE, no signed document.
**Cost of inaction:** every definition agreed in one squad is re-litigated in the next. This is the reason P1 regenerates after each fix.

---

## Maturity scorecard

The full profile is in [[appendix/90-Diagnostics|Diagnostics]]. The short read: **tooling is strong and meaning is absent.**

| Strong (≥3) | Middle (2–2.5) | Weak (≤2) |
|---|---|---|
| Self-service delivery · project management | connection with business · adoption · data quality · security | content management · guided delivery · **platform governance** · **AI readiness (1.4)** |

The skew is systemic and it is not the usual one: this company has the tools and the engineers, and it lacks the layer that says what the numbers mean. A second BI tool would change nothing here.

---

## The chain breaks

`core → semantic → context → AI accuracy → self-service`

**Break 1 — between core and semantic, and it is total.** The core layer exists for 3 domains of 11; the semantic layer does not exist at all. Nothing is defined once.

**Break 2 — the assistant's few-shot examples became the de facto semantic layer.** They are editable, unversioned, unowned, and they are what the model actually reasons from. This is the most expensive break, because it looks like a solution.

**Break 3 — the AI accuracy link was skipped, not broken.** The assistant was launched ahead of both preceding links. The `no-assistant-without-foundation` gate would have stopped this launch; it was never applied, and the launch cannot now be undone.

## Position in the channel triangle

Self-service dominant, agentic launched prematurely, **centralized effectively absent**. The company never had a report factory and is not going to build one. The usual advice — grow centralized reporting to reach a single version of the truth — does not apply and would be rejected in a week.

Agentic maturity: the sponsor believes it is at managed autonomy. Measured against the stages, it is at interoperability with no evals — the tools are connected and nothing checks the answers.

---

→ [[index]] · [[02-Streams]] · [[appendix/90-Diagnostics|Diagnostics]]
