[[index|← BI+AI Strategy]] · 🏢 Severnaya

# 05. Risks

| Risk | Likelihood / impact | Mitigation | Owner | Trigger |
|---|---|---|---|---|
| **The engineer is not hired** — the strategy stays a work plan for the contractor | high / critical | strategy gate: without the hire by March, S2–S4 are postponed and the strategy is re-assembled rather than executed half-way | sponsor | 1 March, the role is not filled |
| **The contractor is a single point of failure** | medium / high | the register describes objects so that someone other than the author can maintain them; knowledge transfer written into the contract | Head of IT | ticket turnaround doubles, or a key contractor person leaves |
| **The platform migration consumes the year** | high / high | migration does not start on objects outside the register; description first, move second | Head of IT | the migration plan contains objects absent from the register |
| **No domain owner** — nobody to confirm S2 | medium / critical for S2 | the stream stops explicitly instead of being agreed "de facto" | Head of BI | 1 April, no name |
| **Governance declared without resource** | medium / high | we do not create a DG function; the rules live inside S1 and S5 as part of the engineer's and compliance's work | Head of BI | a policy appears with no one to execute it |
| **A domain rests on one person** | medium / high | a second person in the sales perimeter from year two; knowledge transfer recorded from day one | Head of IT | the sole holder of the knowledge goes on leave and work stops |
| **Priority changes after November** | medium / high | the freeze list is published in advance; cuts follow it rather than negotiation | sponsor | budget cut, or the sponsor changes |
| **Self-service opened before personal data is separated** | low / critical | S5 is declared blocking for S3 in [[02-Streams]] | Compliance | an access request from a category arrives before S5 completes |

## Freeze list

Published in advance. If a third of the resource is lost, we freeze top-down:

1. **S3 · Governed self-service** — first. It only pays off after S1, and without resource S1 will not finish. Frozen entirely, not reduced to "a pilot in one category".
2. **S4 · Platform migration** — in scope of our timeline, not cancelled: the migration is external. What freezes is our acceptance work beyond the minimum.
3. **S2 · Metric layer** — reduced to three agreed definitions without moving them into code.

**Never frozen, under any cut:** S1 in the part covering the register and data contracts, and S5 in full. The first because without it a cut nullifies everything else; the second because it is a regulatory requirement, not an improvement.

> **Honesty check for this list.** If the budget cut arrives and the list turns out to be uncomfortable, it was written correctly. A list everyone agrees with in advance has usually cut nothing.
