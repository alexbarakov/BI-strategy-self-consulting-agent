[[index]] · Initiatives

# 🗺️ Section 3. Projects and initiatives

**A** = output, what was built. **O** = outcome, what changed. Year 1 is concrete; years 2–3 are indicative and marked so. `<•>` is a placeholder held open until a baseline exists — see [[04-Goals]].

| Initiative | Streams | Owner | Year 1 | Year 2 *(indicative)* | Year 3 *(indicative)* | Metric | Kill-gate | Depends on |
|---|---|---|---|---|---|---|---|---|
| **I1 · Golden set of 60 questions from real logs** | S4 | Head of Analytics | **A:** 60 questions with verified answers<br>**O:** the assistant's accuracy is known for the first time | A: extended to 120 | — | G1 accuracy | — measurement, not a bet | — |
| **I2 · Restate the public commitment** | S4 | CPO + Head of Analytics | **A:** the metric behind "50% by 2027" restated as verified-correct share, agreed before the board review<br>**O:** the board is given a number that survives its first question | O: reported quarterly on the new unit | — | G2 | if the CPO declines, the strategy is rebuilt around the old unit and this is recorded as an accepted risk | I1 |
| **I3 · Twelve metric definitions in code** | S1 | Head of Data Platform | **A:** 12 definitions, one owner each, in dbt with tests<br>**O:** competing definitions for the twelve drop from 3 to 1 | A: next 20 metrics<br>O: `<•>` | O: `<•>` | G3 | if fewer than 8 of 12 are agreed within 5 months, the scope narrows to the 4 board metrics rather than slipping | metric owners from the sponsor |
| **I4 · Named metric owners** | S1 | Head of Analytics | **A:** 2 owners at 20%, with a weekly decision slot<br>**O:** definition disputes are closed in the slot rather than in the board week | A: 4 owners | — | G4 gate load | if the slot regularly overruns its budget, the platform is what gets fixed, not the person | sponsor decision |
| **I5 · Perimeter and refusal for the assistant** | S3 | Assistant PM | **A:** perimeter 1 published; refusal plus routing outside it; provenance on every in-perimeter answer<br>**O:** confidently wrong answers inside the perimeter fall to `<•>` | A: perimeter 2 after S2<br>O: `<•>` | O: `<•>` | G5, G6 | **if accuracy inside the perimeter is under 85% on the golden set two months after narrowing, the perimeter shrinks further rather than the threshold moving** | I1, I3 |
| **I6 · Own identity for the assistant** | S3 | Data Platform lead | **A:** the service account replaced by a per-user identity with an audit trail<br>**O:** an access review can answer who read what | — | — | G7 | — a compliance precondition, not a bet | — |
| **I7 · Trusted core, domains 4–6** | S2 | Data Platform lead | **A:** domain 4 certified<br>**O:** share of queries on certified objects rises from `<•>` | A: domains 5–6 | O: `<•>` | G8 | — | — |
| **I8 · Owner field and auto-archiving** | S5 | Data Platform lead | **A:** the field is mandatory; dashboards with no users and no updates are archived<br>**O:** live dashboards become countable | — | — | G9 | — | — |

## Deliberately not in the portfolio

- **A data catalog.** It entered the first draft and was removed at gate 0: no problem in section 1 stands behind it. Reconsidered when there is something worth cataloguing.
- **A semantic layer for all metrics.** Twelve first; the rest is a year-2 conversation.
- **A certification programme for 912 dashboards.** Ranked last and frozen first — see [[02-Streams]].
- **A data literacy programme.** Forty analysts already have the skills; what they lack is a definition to work from.

## The first 90 days

| # | What | Owner | Check date |
|---|---|---|---|
| 1 | Build the golden set from logs and measure the assistant's real accuracy | Head of Analytics | day 30 |
| 2 | Agree the restated commitment with the CPO **before** any engineering starts | CPO | day 20 |
| 3 | Fix the first 4 of 12 definitions — the ones that reach the board | Head of Data Platform | day 60 |
| 4 | Publish perimeter 1 and turn refusal on outside it | Assistant PM | day 75 |
| 5 | Reconcile the assistant against the certified source for those 4 metrics | metric owners | day 90 |

**Explicitly not in the first 90 days:** the trusted core beyond domain 4, dashboard hygiene, anything touching finance data. Item 2 is first in sequence and cheapest in effort, and it is the one the whole plan rests on.

## The cost of narrowing — the number that has to be said out loud

From eight months of logs, questions currently answered by the assistant split as: `<•>`% inside perimeter 1 · `<•>`% outside it. `[requires clarification]` — the log analysis in I1 closes this by day 30.

Whatever the split is, the questions outside the perimeter do not vanish: they route to a named analyst with a stated turnaround. Until that number exists, "we are narrowing the assistant" is not a proposal anyone can accept. The number is produced first and the narrowing is announced second.

---

→ [[index]] · [[02-Streams]] · [[04-Goals]]
