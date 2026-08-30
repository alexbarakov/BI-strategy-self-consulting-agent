---
id: failure-catalog
title: Failure catalog — how BI and AI initiatives actually die
type: index
purpose: the entry point for "something is wrong with us"; symptom → mechanism → the atom holding the evidence
confidence: mixed — each entry names the atom carrying its evidence level
---

# Failure catalog

75 named ways to fail a BI project or an AI initiative, grouped into seven families. Not a risk taxonomy: every entry is an observed mechanism with a symptom you recognise it by, and an atom where the substance lives.

**How to use it.** Start with the triage table: find your symptom, go to the family, read the mechanism. If the symptom is not there, that is itself a finding — either you are looking in the wrong place, or you have a rare case worth writing down.

**Reading rule.** A failure in this list is not a verdict on an initiative; it is a description of how it breaks when a specific defence is missing. The defence is named after the `→` in each entry.

---

## Symptom triage

| Symptom | Look at |
|---|---|
| We build reports and almost nobody uses them | **A** — value and demand |
| We cannot state our adoption percentage | **A2**, **G6** |
| The business argues about numbers, everyone has their own truth | **D5**, **C6** |
| Production is full of junk with no owners | **B** — content and trust |
| Users cannot find the report they need | **B6**, **B7** |
| We opened self-service and it got worse | **C** — delivery model |
| Analysts route around the rules | **D1** |
| We deployed a catalog and it is empty | **D7** |
| The AI pilot worked beautifully and lies in production | **E1**, **E2** |
| We filled the knowledge base and accuracy did not move | **E5** |
| We cannot prove the effect of AI | **E8**, **A6** |
| People do not grow, a domain rests on one person | **F** — people and team |
| The strategy is written and nothing changed | **G** — programme management |
| Governance is declared but absent | **G3**, **G4** |

---

## A. Value and demand

**A1. Reports die faster than they pay off.** 88% of reports do not survive three months — the process changes, the business shifts focus, the driver leaves. 10% live on minimal traffic, 2% deliver a stable result. → Metrics for "reports with falling traffic" and "users who came once and never returned"; without them a team cannot tell its 2% from its 88%. [[bi-value-illusion]]

**A2. Adoption is not counted, therefore not managed.** The team quotes an absolute number of users instead of a share of the target audience. → A pair of metrics: target-group engagement rate and target audience match rate; the first without the second misleads — high traffic can come from people the report was never for. [[content-promotion-monitoring]], [[participants-2026-benchmark]]

**A3. Build it and they will come.** The platform, the marts and the lake exist; the use cases do not. → An information supply-demand matrix before the build, not after. [[bi-strategy-purpose]], [[info-supply-demand]]

**A4. The data team is isolated.** It works apart from the business without understanding its tasks; the projects come out irrelevant. → Regular status meetings with the domain owner, personal sessions with top users. [[bi-strategy-purpose]], [[centralized-practices]]

**A5. Eternal pilots.** Many experiments, not one scaled. → A kill-gate with a threshold on your own data: a pilot either passes the gate or closes on a named criterion. [[bi-strategy-purpose]], `review-gates.md`

**A6. The leader's own illusion about the project's value.** There is not enough cynicism to assess the real value; people routinely hide that they do not use the reports themselves, assuming everyone else does. → Measurement instead of feeling; a claim to be the best BI project must be backed by traffic. [[bi-value-illusion]], [[centralized-bi-brand]]

**A7. BI in a non-selling function: there is nothing to show the effect with.** → Metrics that do not require revenue: the share of meetings where reports are used, the volume and cost of manual work automated, coverage of the information demand. [[bi-project-metrics]]

**A8. Analytics stops at "what happened".** Dashboards show the data but do not explain why a KPI moved; testing a hypothesis is expensive and there is no structured approach to root cause. → The diagnostic layer as its own investment, not a side effect of dashboards. [[maturity-models]]

---

## B. Content and trust

**B1. The report dies with its author.** Someone leaves and ownership is never transferred. → A handover procedure as a mandatory part of the process rather than goodwill. [[content-hygiene-loop]]

**B2. A policy instead of a mechanism.** Rules for keeping production clean were written and nothing changed. → Three mechanisms at once: automated monitoring with digests, a content bot on a schedule, and a social format. The point of the clean-up day is the habit, not the one-off tidying. [[content-hygiene-loop]]

**B3. Certifying everything.** The process chokes and the mark loses meaning. → A two-tier scheme: automated certification on machine-checkable signs across a wide set, and certification of data and methodology only for the most-viewed. [[content-certification]]

**B4. Certifying dead content.** The share of certified objects rises; the benefit does not. → Measure the share of *consumption* (views and queries), not the share of coverage. [[ai-ready-domain-score]], [[content-certification]]

**B5. Copies of one report with different filters.** Authors multiply versions and the single version of truth is lost. → The check exists in the content management questionnaire, plus environment separation with automatic permission expiry in the sandbox. [[content-mgmt-processes]], [[content-catalog-ux]]

**B6. There is a health score and no findability.** The rating is computed and the user still asks in chat. → A report catalog plus a role-oriented workspace; otherwise the score stays an invisible back-end rating. [[content-catalog-ux]]

**B7. Search in the BI portal scares off the casual user.** Too many functions, an unfamiliar interface, no descriptions or grouping. → A dedicated navigation interface, or catalog integration into corporate search. [[content-catalog-ux]]

**B8. The style guide is published and unused.** → Three layers with different addresses: the template and the visual vocabulary inside the tool, the textbook outside it. Plus "redesign into the template" offered as a service. [[visual-style-guide]]

**B9. The author has no interest in others using their report.** Promotion then works through no channel. → The question is asked before promotion; if the answer is no, the report does not go cross-functional. [[content-promotion-monitoring]]

**B10. Production reports run on sandboxes.** Production is built on layers nobody maintains. → Environment separation and a source check in the validation checklist. [[content-mgmt-processes]], [[pain-fronts-2026]]

---

## C. Delivery model

**C1. Self-service as self-deception.** Casual users are taught to assemble reports from templates; adoption is close to zero. → Separate the terms: this is guided BI, and it is measured by the usefulness of finished content, not by the number of authors. [[ssbi-vs-guided]]

**C2. The report factory dominates.** A large backlog, self-service is "secondary", and there is no response from the business. → Insufficient BI penetration: the requester-developer barrier, a bottleneck, shadow BI. [[ssbi-vs-guided]]

**C3. Self-service dominates.** Permissions granted, a course recorded, traffic monitored — "everything is fine". → The same insufficient penetration, arriving instead through multiplied truths, content chaos and security risk. [[ssbi-vs-guided]]

**C4. The analyst's tool handed to a data consumer.** The person is frightened by the menus and calls a local analyst instead. → Map roles to tools; the reverse mistake works the same way. [[ssbi-workflow]]

**C5. No way back from self-service into production.** A good local report stays local forever and production fills with duplicates. → The `propose → prototype → promote` workflow with a governance committee. [[ssbi-workflow]]

**C6. Business logic monopolised inside departments.** Three lines of business compute attrition three ways, HR has a fourth. → Central BI names the data owner, facilitates agreement, fixes it in the glossary, builds something more convenient than the alternatives, **and enforces their removal**. The last step is usually skipped, which is why the conflict returns. [[ssbi-failure-causes]]

**C7. Self-service where it cannot work.** Company-wide executive reporting, cross-role unified reporting, functions that cannot or will not grow a BI practice, and reports on highly confidential data. → These four segments stay centralized at any maturity. [[ssbi-failure-causes]]

**C8. Abandoned content.** Reports were grown where there is nobody to maintain them. → Check not only "can they build it" but "can they maintain it". [[ssbi-failure-causes]]

**C9. One head over both the report factory and self-service.** One block eats the other. → Separate heads: the models have different goals. [[bi-org-structure]]

**C10. Users do not know the sources exist.** It is hard to learn what is available, to pick the right one among lookalikes, to understand field names. → This is also the list of what an agent lacks — which makes the investment pay twice. [[ssbi-failure-causes]]

---

## D. Data and foundation

**D1. The rule costs more than routing around it.** Long lead times on data marts push analysts into more accessible data, breaking the rules. → Governance initiatives and speed initiatives run as a pair, not in sequence. [[pain-fronts-2026]], [[dg-launch-path]]

**D2. A permission matrix with no implementation mechanism.** A beautiful table, permissions still granted by hand. → Next to the visibility scope, the specific visibility table or directory filter. A matrix without a mechanism is a declaration. [[access-matrix]]

**D3. A permission matrix with no review date.** It goes stale silently. → The last review date is a mandatory field. [[access-matrix]]

**D4. Trying to automate what cannot be automated.** People attempt to derive the role matrix from data. → It is extracted from the owners and signed off; in return it becomes the mandate to grant permissions without further approvals. [[access-automation]]

**D5. No master data sources.** Marts duplicate, ownership is smeared, and the agent has nothing to stand on. → A master source register: the marts best suited to a domain, duplicates reduced, checks focused only on them. [[critical-data-status]]

**D6. The core layer started from the most painful marts.** Expensive, slow, and the project stalls on the first hard case without showing value. → Start from the most reused cross-domain entities; presentation layer first, technical layer second. [[core-layer-project]]

**D7. A ghost-town catalog.** Deployed, with no descriptions. → Automate metadata harvesting as far as possible, capture documentation in the flow of work including CI checks, and curate the top 20%. [[data-catalog-pitfalls]]

**D8. A fragmented golden path.** Discussions, the knowledge base and querying are duplicated across the catalog, the wiki and the messenger. → Choose one path and switch the duplicates off. The catalog's built-in messenger is self-deception. [[data-catalog-pitfalls]]

**D9. A long tail of unused marts.** Costs grow faster than the organic load, and there is no incentive to optimize because nobody sees the cost. → Billing as a transparency metric for unit economics; the reader pays for reads, the owner for storage. [[infra-billing]]

**D10. A metric tree that will never exist.** Attempting a strict hierarchy ends in a stretch or in a stall. → Build links and levels, not a tree. [[glossary-vs-dictionary]]

**D11. Glossary and data dictionary in one place.** Both break. → Different artifacts with different owners; the term reaches the user at the moment of reading, not in a separate system. [[glossary-vs-dictionary]]

**D12. Data governance stopped by a budget refusal.** → The refusal is a normal branch of the route: common-sense governance inside teams via small quick wins, then a restart through an MVP. To move to a programme you need at least two of four conditions. Governance started from below survives the budget cycle. [[dg-launch-path]]

**D13. Owner and curator roles in domains never took hold.** They were assigned and nobody started. → A role without a time budget and without being built into the process is a line on a slide. [[dg-launch-path]], [[context-governance]]

---

## E. AI and context

**E1. The plausible wrong answer.** Syntactically valid SQL, the wrong metric, the wrong period. It damages trust more than an honest "I don't know"; the user goes back to Excel. → "I cannot" as a designed outcome, a trust label and provenance in every answer, a clarifying question when there are two readings. [[plausible-but-wrong]]

**E2. A demo on a toy schema carried into production.** A small space and obvious joins create false confidence. → Measure on your own schema and your own golden set before deciding to deploy. [[plausible-but-wrong]], [[semantic-layer-evidence]]

**E3. The assistant ahead of the foundation.** Launched before semantic coverage and a certified core exist. → The `no-assistant-without-foundation` kill-gate; check the order of initiatives separately from their value. [[ai-triad-prerequisites]], [[bi-toolset-landscape]]

**E4. Building the triad in parallel.** A reliable way to finish none of it. → One layer at a time, with an eval before and after, starting from the domain's most expensive pain. [[ai-triad-prerequisites]]

**E5. Filling equated with quality.** Many objects, accuracy unchanged. → Filling ≠ trust ≠ effect: three different metrics. Only confirmed objects count, and generated ones only after review. [[domain-knowledge-base]], [[context-governance]]

**E6. More context into the prompt.** Quality degrades as input grows, continuously and long before the window fills; the separate threshold effect is measured as a share of the window (40-50%), not as an absolute token count. → Serve only what is relevant; apply the permission filter before retrieval, not after. [[context-layer-market]]

**E7. The verify gate became a bottleneck.** The curator drowns in the queue. → The gate carries an explicit weekly time budget; exceeding it is fixed by the platform, not by the person. The gate's load is a platform health metric. [[context-governance]]

**E8. The effect of AI measured by self-assessment.** In a controlled study developers were 19% slower while convinced they were 20% faster. → Only measurement against a golden set with a baseline fixed beforehand. [[ai-in-data-processes]], [[ai-time-saving-trap]]

**E9. Hours saved taken for effect.** The freed time dissolves into small things. → A named reallocation decision, and the person who makes it, is a mandatory part of an AI initiative. [[ai-time-saving-trap]]

**E10. Growth in agent calls taken for success.** → Growth in calls without growth in successfully completed tasks does not count as a result; the calls may be retries. [[ai-accelerator]]

**E11. Replacing the process instead of routing.** AI is placed where a guarantee is required. → The deterministic layer on the bulk, the model on the disputed cases. [[ai-in-data-processes]]

**E12. Governance theatre around context.** Context is assembled, the accuracy gain is not significant, and trust in the whole AI agenda falls. → The kill-gate: no significant gain, stop. [[context-layer-market]]

**E13. A vendor figure quoted as fact.** → The evidence level travels with the number; what you buy is architecture, not the claimed percentages. [[context-layer-market]], [[semantic-layer-evidence]]

**E14. Expecting AI to close most of the ad-hoc.** Participants estimate 70–80%; the practical ceiling is far lower. A high estimate of potential usually signals low maturity of demand. → Count per domain, not on average. [[participants-2026-benchmark]], [[insight-management]]

**E15. Projects duplicating one another by job to be done.** A wave of initiatives breeds overlaps. → Pre-review and merge projects before they start; focus on polishing the mass scenarios rather than generating new ones. [[ai-accelerator]]

---

## F. People and team

**F1. Grade by breadth.** Knows a bit of everything, therefore senior. → The grade is determined by the number of competencies at the top level; breadth does not carry you up. [[bi-competency-matrix]]

**F2. A domain resting on one person.** → At least three experts on critical domains, two on the rest; a successor as a mandatory requirement for a team lead. [[bi-competency-matrix]]

**F3. The matrix was rewritten for AI, hiring was not.** The process tests hard skills by conversation and does not see AI at all. → Interview blocks mapped one-to-one onto the matrix; LLM allowed on technical tasks, with two stop signals — refusing it, and trusting its output blindly. [[bi-hiring-ai-era]]

**F4. The battle of agents.** The candidate mass-produces generated CVs while the recruiter scores with an agent; the employee generates review artifacts while managers run them through an agent. → Artifacts produced in the moment, plus a spoken debrief. [[bi-hiring-ai-era]]

**F5. The junior and mid tier erodes.** Teams shrink, the entry into the profession disappears, and in a few years there is nobody to grow seniors from. → Move juniors into domain curator roles, grow them through reviewing AI output, and deliberately keep some routine for grounding. [[bi-hiring-ai-era]]

**F6. A champions programme with no benefits column.** There are company goals and no answer to "what is in it for the champion". → Symmetry between goals and benefits; plus four preconditions before launch, including an executive sponsor. [[bi-community-management]]

**F7. Belts, badges and awards mixed together.** All three lose their meaning. → The belt is about competence, the badge about engagement, the award about recognition. [[bi-community-management]]

**F8. Nothing to put in the onboarding plan.** The self-learning track is empty. → That is not an onboarding problem but a diagnosis: the standards documents do not exist. [[onboarding-plan]], [[rules-and-standards]]

**F9. A premium service promised to everyone.** The queue is perceived as a defect. → Centralized BI by definition cannot be available to all; the queue is the design, and the answer lies in prioritization. [[centralized-bi-brand]]

---

## G. Strategy and programme management

**G1. A strategy built around the current technology.** It is organised around a platform rather than the business's tasks; the platform changes and the strategy collapses. → The spine runs from needs; tools live on their own worksheet. [[bi-strategy-purpose]], [[bi-tool-selection]]

**G2. An initiative with no owner.** A line in a plan, not a change. → An owner, a metric and a kill-gate for every initiative. [[action-plan]]

**G3. Governance lives only in the text of the strategy.** Exactly one recurring meeting holds it; if that meeting does not happen, governance does not exist. → A monthly governance status as a mandatory slot. [[regular-meetings]]

**G4. Declared but not resourced.** Roles named without time, goals set without capacity, policies written without an owner. → Do not average it into a single score: flag the dimension `[declared, not resourced]` and move it into the gap list. `review-gates.md`

**G5. Target maturity at 3–4 across every category.** A symptom of an unread diagnosis. → Plus one level per year as the honest default; a larger shift requires a named reason. `review-gates.md`

**G6. An inspiring number instead of a measurement.** A gap in the vision is filled with a nice figure; it will outlive the strategy and be quoted for a year. → `[requires clarification]` until it is measured. [[vision-statement]]

**G7. A polite judge.** The review happened and the draft did not change. → A pass with no visible change means the judge was polite rather than useful. `review-gates.md`

**G8. The cut was never rehearsed.** The first budget review fails everything at once, everywhere. → A published freeze list: what dies if a third of the resource goes. [[action-plan]], `review-gates.md`

**G9. Pains collected only from your own team.** The strategy answers the most interesting pain rather than the most expensive one. → Four role groups in the pain exercise, and a candidate initiative against each group. [[painpoints-analysis]]

**G10. Overrating the tool.** Choosing a platform eats a year while the data and the context stay as they were. → Data, context and AI work as one product; the tool is not the main lever. [[unified-bi-platform]]

---

## What this catalog does not cover

Failures specific to regulated industries (breaching data residency, auditing access to personal data, honouring a deletion request) and failures during a forced platform migration are only touched on. The knowledge base does not yet hold enough substance for separate entries. If such a case appears, it deserves to be written down rather than forced into the nearest existing line.
