---
id: bi-competency-matrix
title: The BI competency matrix 2026 - three parts of the assessment, L1-L3, grades
type: method
source: "Course \"BI+AI strategy 26\", Day 9 - internal practice"
confidence: verifiable (an internal document)
origin: "an internal case walked through on the course; the numeric thresholds are anonymized - calibrate from your own baseline"
blocks: [6]
---

A matrix rewritten for the AI era. The key difference from the classics: **LLM competence is built into every level of every competency rather than split out as a separate skill**.

## Three parts of the assessment - each with its own rhythm

| Part | Rhythm | Content |
|---|---|---|
| **4 soft competencies** | every six months | analysing user needs · managing expectations and planning · a product approach to reports and data · knowledge sharing and developing the BI role |
| **4+1 hard competencies** | once per level | ETL · SQL/DWH · the BI tool · data visualization · **Python, optional** |
| **The BI project** | annually | one project defended, against three criteria |

The differing rhythms are a deliberate detail: hard skills are not re-confirmed, soft skills are revisited regularly, the project is annual.

## Four grade levels

- **Junior** - performs decomposed tasks under the team lead's supervision; marts, flows and dashboards to the standards
- **Middle** - runs work independently within the unit; analyses needs, designs data models, **develops objects as products**; plans several sprints ahead and handles requester communication themselves
- **Senior** - **generates work at their own level inside the domain**; owns the production layer of reports and marts and is answerable for its SLA; plans a quarter and gives commitments to requesters; takes part in hiring technical sections and in onboarding
- **Lead (IC track)** - leadership across several verticals or the whole company; cross-domain data products, BI partnership, self-service, standards. The alternative is the managerial track, team lead BI

## Hard skills: three depth levels with the LLM built in

> What is critical is **the ability to get the right result with any tool - the LLM included**.

- **L1 execution** - I get a correct result and understand what is written. Including understanding LLM-generated code and being able to explain it line by line.
- **L2 design** - I make justified architectural decisions and pick the best approach among alternatives. **I can justify the LLM's proposed solution or replace it.**
- **L3 systematicity** - a complex system runs in production: reused, documented, covered by tests. **I validate and review the LLM's output and embed it into the system.**

L3 in any competency means defending a project before a jury. A level once reached is not re-confirmed.

**What the competencies contain.** ETL: the data model and the storage schema; L2 is an optimal model with an example of optimization, L3 is a core data layer in production with reuse and tests. SQL/DWH: optimal queries on large data with the database engine in mind; L2 is optimization with a measurable before and after, L3 is highly complex code plus reviewing colleagues' SQL. The BI tool: L1 is charts, parameters, datasets; L2 is cross-filtering, drill-down, navigation; L3 is a system of dashboards as an application plus a contribution to the product itself. Visualization: L1 is no basic mistakes, L2 is mock-ups and a justified choice, L3 is influence on the quality of decisions and a contribution to the data visualization culture.

## Grades are distinguished by the number of L3s; the minimums are nearly flat

The L1/L2 minimums for middle, senior and lead barely differ - **the grade is determined by how many competencies sit at L3**: a senior needs more of them than a middle, and for a lead the threshold may not be set at all and is decided in calibration. Python is not part of the minimum at any grade.

This is an important construction: it stops people "growing" on breadth alone and requires genuine depth in at least one place.

## The BI project: annual, with value as the key criterion

Three criteria:
1. **Value** - what changed because of the project, **not the volume of work**: from "users got the data" (junior) to influencing the function's strategy (lead)
2. **Formalization** - who did the work of defining the problem: from "the task arrived fully formed" to "I identified the problem myself across several domains"
3. **Engineering complexity** - how deliberate the chosen solution was and how robust: from standard patterns to changing the domain's architecture

The result is the average across criteria **with value weighted highest**. Pre-review: junior and middle by their own team lead, senior by one designated BI team lead, lead by three.

## Promotion: you perform at the new level first

**You cannot skip a grade.** Every step requires: the soft and hard skills of the new level per the matrix · a completed BI project at the new level · at least one review with a positive result in the current role, plus confirmation at calibration.

Senior to lead: at least two of the four soft competencies confirmed through a functional project, accepted by the head of BI. Senior to team lead: a justification of the role, decided by the domain and unit heads together with the head of BI, and **an acting role before promotion is mandatory**.

## Team lead BI - six competency blocks

Developing processes and tools · leadership per the corporate model · managing resources and projects (a quarterly roadmap; at the junior management level a significant share of time goes on leading applied projects hands-on) · managing the team (hiring, technical sections, SMART goals, retaining key people) · developing the BI function · **assessing effect - the influence of key projects on metrics computed correctly, before and after, not an activity report**.

What separates M2 from M1: **being the driver of the BI strategy project** (rather than a significant contributor) and **a mandatory successor in the team**.

## The calibration cycle - it starts 6 weeks before the defence

1. **Continuously - observation:** record examples of competencies for the pitch, give feedback on artifacts **while there is still time to fix things**
2. **4-6 weeks out - gathering the evidence:** the BI project template with feedback, a self-assessment against the matrix, a pre-review of the project and of hard L3
3. **1-2 weeks out - the check:** the matrix is filled in, the artifacts are in place, the jury's L3 verdict is recorded, the pitch is ready
4. **Calibration - the defence:** a 3-minute pitch -> the group reads -> questions and a vote
5. **Afterwards - the outcome:** do not communicate results until HR says so, meet the employee, give development feedback

Promotion is discussed in advance, one or two quarters ahead; before nomination, blockers are checked.

## The competency backup strategy

**At least three experts on critical domains and at least two on the rest**, plus regular recording of knowledge-sharing sessions. This is the only working answer to the risk of "the domain rests on one person".

Links: [[bi-hiring-ai-era]] · [[bi-org-structure]] · [[onboarding-plan]] · [[bi-community-management]]
