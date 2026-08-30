# BI+AI Strategy — Vantage Mobility

> Fictional company · three-year horizon · draft 1.1, after the gates · 2026-08-30
> ⚠️ A demonstration artifact of the skill. Figures are placeholders `<•>`; baselines are marked `[requires clarification]`.

## Where we are going

Within three years the twelve metrics the board is graded on mean one thing across the company, and the AI assistant answers on them with a guarantee — or refuses and says who to ask. Not more answers than today. Answers that can be quoted.

The assistant is not the project. It is already live, already paid for and already promised to the market. The project is giving it something true to answer from, and giving the company a way to tell whether it does.

## Which problems we are closing

| Problem | Who it hits | → |
|---|---|---|
| Three competing definitions of the twelve board metrics | commerce, analysts | [[01-Context#P1 · Three competing definitions of the twelve commercial metrics]] |
| The assistant answers questions it cannot answer correctly | ops, casual users | [[01-Context#P2 · The assistant answers questions it cannot answer correctly]] |
| Ops leads keep parallel spreadsheets | ops | [[01-Context#P3 · Ops leads keep parallel spreadsheets]] |
| The assistant's success is measured by call volume | the sponsor, the board | [[01-Context#P4 · The assistant's success is measured by call volume]] |
| It reads the whole warehouse under one service account | security | [[01-Context#P5 · The assistant runs under a service account with warehouse-wide read]] |

## Streams of change

| Stream | In one line | Owner |
|---|---|---|
| **S4 · Honest measurement** | a real accuracy number, and a public commitment restated in a unit that survives a question | Head of Analytics |
| **S1 · One definition per metric** | twelve metrics defined once, in code, with named owners | Head of Data Platform |
| **S3 · A guaranteed perimeter** | the assistant answers with provenance inside it and refuses outside it | Assistant PM |
| **S2 · Trusted core** | from three certified domains to six, chosen by reuse | Data Platform lead |
| **S5 · Dashboard hygiene** | an owner field and auto-archiving; nothing more | Data Platform lead |

→ in detail: [[02-Streams]]

## What we deliberately do not do

- **We do not switch the assistant off, and we do not rebuild it.** It works, it is used, and the failure is not in the model — it is in what the model reads from.
- **We do not unify country-level metric variance.** Where a country computes differently for regulatory or commercial reasons, we standardize the description of the difference, not the number. Erasing it would replace three wrong answers with one.
- **We do not build a data catalog this year.** It entered the first draft and was removed at gate 0: no problem behind it.
- **We do not declare a governance function.** One person at half-time with no mandate is not governance, and naming it would be the "declared, not resourced" pattern. The mandate is attached to twelve metrics instead. See the uncovered problem P7 in [[02-Streams]].
- **We do not touch 912 dashboards** beyond an owner field and auto-archiving.

## What we need from the sponsor

Three decisions, and the first one blocks the rest.

1. **Agree to restate the public commitment** before the board pack is drafted — from "50% of ad-hoc handled by AI" to a share that is verified correct. This is a conversation with the CPO, not a budget line, and it is worth more than either of the others.
2. **Two metric owners at 20% of their time**, named individually, from commerce and ops. Not a team — two people with a weekly decision slot.
3. **Authority to narrow the assistant's perimeter** without a squad veto, for the twelve metrics only.

Nothing here asks for headcount. The freeze is taken as given.

## First step and the cost of inaction

**90 days:** measure the assistant's real accuracy on a 60-question golden set built from live logs · agree the restated commitment · fix the first four definitions · publish perimeter 1 and turn refusal on · reconcile the assistant against the certified source. Detail in [[03-Initiatives]].

**The cost of doing nothing** is not that the assistant stays as it is. It is that in four months the board is shown a number that falls apart under its first question, and the ops shadow spreadsheets quietly become the system of record. The second is harder to reverse than the first.

## Navigation

[[00-Company-profile|Company profile]] · [[01-Context]] · [[02-Streams]] · [[03-Initiatives]] · [[04-Goals]] · [[05-Risks]] · [[appendix/90-Diagnostics|Diagnostics]] · [[appendix/91-Analysis-frame|Analysis frame]]
