---
id: bi-routine-calendar
title: The BI team's routine calendar - what gets checked daily, weekly and quarterly
type: method
source: "Course \"BI+AI strategy 26\", Day 9"
confidence: verifiable
blocks: [6]
---

An operational checklist with an explicit definition of done for each activity. Its value is that it is **a ready-made list of what ought to be checked at all** - most teams find holes in it.

## Daily (morning)

| Activity | Definition of done |
|---|---|
| Check the extracts and the freshness of master sources | every source refreshed successfully |
| Check that subscriptions are correct | every subscription delivered successfully |
| Check your own subscription to the key reports | **the refresh date in the report is today** |
| Check the service-desk board: new assigned tickets and their priority, raise a Jira issue if needed | comments added to assigned tickets, status current |
| Plan and review the day's tasks | the day's plan is set |
| Daily BI meeting (Tue, Wed, Fri) | open questions have been talked through |

Subscribing yourself to the key reports is the cheapest way to catch "the data did not refresh" before the user does.

## Weekly

Create or check the warehouse tasks for the next sprint (Friday EOD) · create tasks when a requester comes directly: into the active sprint for a bug fix, into refinement for everything else.

## Fortnightly

Check "reports in the workspace": tags assigning a role and a domain - **DoD: every report is assigned to a domain and a role, and the section of reports without a role is empty** · check unassigned tasks in your domain · estimate new tasks in refinement · check unclosed sprint tasks · **split large tasks into stories that fit inside one sprint**.

## Quarterly or on demand

| Check | Target threshold |
|---|---|
| Extract build duration | **under 20 minutes**, with a shame-list report of the offenders |
| Report performance | no anomalies in query duration |
| **Report adoption** | **adoption is visible: 30% of the focus audience** |

Those three quarterly checks are effectively the minimum SLA the team gives itself. The 30%-of-focus-audience threshold is a realistic bar, not 100%.

Links: [[bi-org-structure]] · [[regular-meetings]] · [[content-promotion-monitoring]] · [[bi-project-metrics]]
