# The diagnostic question bank

Real wording from the **BI Project Health Check** (72 factors, 9 categories) plus the course's **AI-readiness overlay** and pointers to the D&A Planner questionnaire worksheets. Use it as the source of interview questions — do not invent your own.

Every factor is scored **0–4**: 0 No · 1 Planned · 2 In progress / partially · 3 Completed, needs improvement · 4 Fully completed and optimized. The participant gives a **current score and a one-year target**.

How to use it by mode:
- **Light:** after the eight context questions, ask for a **self-assessment across the nine categories** (one 0–4 score per category, anchored on its lead question) plus **five AI-readiness scores**. That is enough for an honest scorecard.
- **Full:** run the factors one by one as a grid, then average by category and by the seven solution categories.

---

## 1. Connection with business (business alignment / data culture)
- 1.1 Is there a register of analytical use cases, ranked by business value?
- 1.2 Are reports embedded into regular business processes and the decision cadence?
- 1.3 Are BI initiatives aligned with strategic and operational business goals?
- 1.4 Are business leaders engaged with BI and promoting a data culture?
- 1.5 Are the target audience personas clearly defined and classified?
- 1.6 Is a business metric tree defined and standardized?

## 2. Adoption and satisfaction (user engagement)
- 2.1 Are there tools for monitoring report usage ("BI for BI")?
- 2.2 Do you assess BI tool adoption regularly?
- 2.3 Is the share of monthly active users above 50% for the key roles?
- 2.4 Is adoption part of the BI team's goals?
- 2.5 Are there regular user satisfaction surveys?
- 2.6 Is there a framework for collecting end-user feedback?
- 2.7 Is there an onboarding process for new users, with recommendations?

## 3. BI content management (processes and standards)
- 3.1 Are acceptance criteria defined and agreed with the business?
- 3.2 Is there a documented requirements-gathering framework?
- 3.3 Does every report release or update pass a quality checklist?
- 3.4 Is there a process for documenting reports (sources, metadata, logic)?
- 3.5 Are recommended reports marked or certified by business owners?
- 3.6 Are there regular report reviews with the data owners?
- 3.7 Are reports integrated with the corporate glossary?
- 3.8 Is there a procedure for archiving stale or unused reports?
- 3.9 Is report load time tracked against a threshold?
- 3.10 Is there a performance improvement workflow and a content health SLA?
- 3.11 Is there a visual style guide for dashboards?

## 4. Self-service BI delivery (model balance, community)
- 4.1 Are the centralized and self-service models harmonized?
- 4.2 Is there a mechanism keeping methodology and tooling consistent across self-service authors?
- 4.3 Is there a portal or communication channel for self-service?
- 4.4 Is there a process for handing over and reviewing content between authors?
- 4.5 Is there a BI champions programme?
- 4.6 Are there structured learning paths?
- 4.7 Are there community activities: meetups, demo days, knowledge sharing?
- 4.8 Is there regular training and mentoring for self-service users?

## 5. Guided BI service delivery (support, UX)
- 5.1 Are there teams supporting BI users?
- 5.2 Is there regular training to raise skills?
- 5.4 Does the BI team run joint data analysis sessions with the business?
- 5.5 Do users have data access and can they work independently?
- 5.6 Are reports optimized for mobile and tablet?
- 5.7 Is usability testing run with real users?
- 5.8 Is user behaviour analysed to improve the UX?
- 5.9 Is there a BI portal with better navigation on top of the default one?

## 6. BI platform governance (tools and automation) — the core of the AI foundation
- 6.1 **Semantic layer** — a centralized layer for reporting?
- 6.2 **Metric store** (dbt metrics or similar) for metric consistency?
- 6.3 A solution for automatic insight generation and delivery?
- 6.4 CI/CD in the BI and data engineering workflow?
- 6.5 Self-service ETL for power users?
- 6.6 BI system performance monitoring?
- 6.7 Tooling and a process for regular query optimization?
- 6.8 A reliable process for upgrading the BI platform?
- 6.9 Integration between BI and the data catalog?
- 6.10 Automation of bulk report distribution?

## 7. Data quality management (processes and standards)
- 7.1 Do reports refresh automatically on schedule?
- 7.2 Are there automated checks for accuracy, completeness and consistency?
- 7.3 Is there a **layer of certified sources** for domains and metrics?
- 7.4 Are certified sources documented (fields, descriptions)?
- 7.5 Are data changes tracked through lineage?
- 7.6 Is data freshness transparent in reports (extract time, delays)?

## 8. BI security and compliance (processes and standards)
- 8.1 Role-based access control?
- 8.2 Automated role assignment by rules?
- 8.3 An access request workflow with automated approval?
- 8.4 Integration with the corporate directory?
- 8.5 Regular access security audits?
- 8.6 Compliance (GDPR / HIPAA / local data protection law)?
- 8.7 Regular assessment of data usage risk?
- 8.8 A disaster recovery plan, written and tested?

## 9. Project management (processes and standards / skills)
- 9.1 A prioritization system for BI projects?
- 9.2 Tasks tracked in a tracker?
- 9.3 Agile practice (Kanban or Scrum with sprints and retrospectives)?
- 9.4 A competency matrix for the BI team?
- 9.5 A list of the team's operational KPIs (adoption, satisfaction and so on)?
- 9.6 Are the team's annual goals aligned with the D&A strategy?
- 9.7 A long-term strategic plan for BI?
- 9.8 Standardized hiring and onboarding for BI specialists?

---

## The AI-readiness overlay (a tenth category, the course layer)

Score these on the same 0–4 scale:
- **AI-1 Semantic coverage** — the share of key metrics with an unambiguous definition in the semantic layer or metric store.
- **AI-2 Trusted core** — the share of queries and reports on a certified core layer; ownership, SLA and data quality checks on the marts.
- **AI-3 Domain context** — the completeness of the domain knowledge base: objects, glossary, FAQ, "question → SQL" examples, eval cases.
- **AI-4 Process readiness** for "AI drafts — humans validate" — a verify gate, kill-gates, eval infrastructure.
- **AI-5 Agentic infrastructure** — MCP access to services, a skill registry, judge gates and guardrails, observability and tracing.

Plus two behavioural questions from the course, answered as fact rather than on a scale:
- What was tried with AI/LLM in analytics, and **what survived to production**?
- What **share of ad-hoc** could plausibly be closed by AI without an analyst?

---

## Additional Planner questionnaire worksheets (Full mode)

For a deeper AS-IS on processes, use the practices from the D&A Planner (worksheet → what it asks):
- `2.1 Data Mgmt questionnaire` — data source management, data quality, enrichment, security (centralized vs self-governing).
- `2.2 Content Mgmt questionnaire` — the content lifecycle, authorization, validation, promotion.
- `2.3 SelfServ D&A Practices`, `2.4 Centralized D&A Practices` — practice checklists (applicable? / owner / timing).
- `2.5 BI & Around BI Tools` — stack inventory, including GPT-based BI UX and insight generation.
