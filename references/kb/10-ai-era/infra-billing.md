---
id: infra-billing
title: Billing the analytics infrastructure - from a common pot to an addressed bill
type: case
source: "Course \"BI+AI strategy 26\", Day 6 - internal practice"
confidence: verifiable (internal measurements)
origin: "an internal case walked through on the course; the numeric thresholds are anonymized - calibrate from your own baseline"
blocks: [5, 6, 7]
---

A topic absent from the classical guide that is fast becoming mandatory: **the economics of the analytics platform as an object of management**.

## The problem

In investment cases and in product teams' P&L, the cost of analytics infrastructure **does not appear at all**. Without transparency there is no incentive to optimize either - the growth comes not only from organic demand but from a long tail of unused marts and dead-end computations nobody reads.

The platform orders hardware for all of analytics out of one pot; there is no cost allocation by domain.

The measured symptoms in the case walked through: analytics infrastructure cost growing at **twice the target rate** · compute utilization roughly **half the industry norm** (the norm being around 50-60%) · a substantial rise in server prices over the year.

The first two metrics are worth measuring at home before any conversation about billing: without them the topic does not sell, and with them it sells itself.

## The target scheme - self-service ordering by the product teams

| Element | Content |
|---|---|
| **Quota isolation** | a quota at unit level: one team overrunning does not block another |
| **A service catalog** | mart, dataset, ETL source, ad-hoc, metric, ML feature - each with a tariff |
| **Tracking** | dashboards of current and historical consumption per domain |
| **Ordering by the team** | the tech lead places the order, with the analyst as a partner justifying the drivers |

> This is **not invoicing**: turning consumption into money is needed as a transparency metric for unit economics. But the teams place their next hardware order themselves.

The framing matters politically: billing presented as "now you pay" meets resistance; presented as "now you can see and decide", it works.

## Who pays for what - the central rule

- **Reads are paid by the reader.** Any SELECT against a mart is tariffed under the initiator's account and drawn from the reading vertical's quota, **even when the mart belongs to a horizontal team**.
- **Writes and storage are paid by the owner.** The owning team spends quota only on the regular recomputation and the disk space; it does not pay for other people's reads.
- **Unattributed usage is shared proportionally.** Objects with no owner and shared platform resources are allocated to technical clusters and then distributed across verticals by actual consumption.

This split removes the main objection from the owners of shared marts: otherwise the platform team pays for the whole company's traffic.

## The assumptions to know about when a number looks odd

- **A single compute price** - the cost of a query does not depend on the server generation; average utilization across the cluster is used
- **Load smoothing** - consumption is averaged over a period so that rare heavy computations do not spike the quotas
- **Overheads are included** - the price includes target utilization (headroom for resilience) and a replication factor
- **Service type priority** - a query may carry the markers of several systems but lands in the first matching type; the ordering matters

Publishing the assumptions alongside the numbers is a mandatory part of the mechanism. Without it, the first disputed bill collapses trust in the whole model.

## The tie to strategy

Billing is the missing link between core-layer initiatives and the conversation with the business: without it, the savings from reusing marts stay unobservable. See the business goals in [[core-layer-project]].

Links: [[core-layer-project]] · [[bi-project-metrics]] · [[data-mgmt-processes]]
