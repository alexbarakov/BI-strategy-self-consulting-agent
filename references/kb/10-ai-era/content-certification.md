---
id: content-certification
title: Certifying BI content - three models and their shades
type: pattern
source: "Course \"BI+AI strategy 26\", the \"Content management\" session"
confidence: verifiable (descriptions of company practice)
blocks: [4.2]
---

The course puts the question directly: **a sensible topic or over-engineering?** - and answers that certification has shades, and the model is chosen to fit the management model.

## Model A. Certification in decentralized self-service

All reports split into "good" (certified) and "bad", and the team believes the good ones solve the business's problem faster. Certification happens in the review every report goes through on the way to production. It is essentially like code review, but less standardized.

**Formal criteria:** a description and a comprehensible name are present · entitlements are set correctly · the formatting standards are used.
**Expert criteria:** convenience and UX · correctness of the calculations · how well the "code" in the BI tool is written.

### A two-tier implementation

**1. Automatic BI certification** - 5 machine checks: metadata for the landing page is filled in · there is a heading naming the owner · there is documentation of at least 300 characters · the report and its objects are in production folders · the report runs fast.

**2. Data certification** - only for key reports or on request, across 5 parameters: **data sources · ETL · methodology · metrics (calculation and reconciliation) · docs**. A simplified version checks only data sources, ETL and docs - **the metric calculation methodology is not checked in it**, which is stated honestly.

### The operational answers the method considers mandatory

- **Do all reports go through?** The automatic one, yes, except sandboxes, self-service and personal folders. Data check tickets are raised only for the most-viewed.
- **What happens if you fail?** A banner appears everywhere saying "this report failed certification", naming exactly what is wrong.
- **What do those who pass get?** An achievement, plus a report ranking owners that is taken into account in performance review.
- **Will the BI development team help?** Yes, in hard cases, but the first port of call is your own team's BI analyst.
- **How is it re-confirmed?** Once a year, as part of the clean-up day.

## Model B. Certification in a centralized report factory

A process of marking reports **recommended by the business function responsible for the data area**, plus quality control over data and logic freshness for whatever has been marked.

The badge "Recommended by \<function name\>" means the department has confirmed the data and the logic are right and takes part in the regular review.

**What for:** the user finds a trustworthy report among many and saves time; they avoid reports whose logic is stale or that are no longer refreshed. **Without bureaucracy:** only cross-functional reports with potential use by several roles get certified; everything is recorded on the report cards in the wiki; certification is part of building the analytical workplace; marked reports are checked in semi-annual audits.

**Four roles in the responsibility matrix:** the business stakeholder (final decisions on business logic, prioritization) · the data steward (developing and checking the business logic, requirements, UAT) · the report developer (sources, development, design, testing, documentation) · the controller (starting, moderating and finalizing the communications, updating the wiki artifacts).

**The stages:** a one-off marking on inclusion in the workplace -> building a new cross-functional report or upgrading an existing one -> release and promotion into the target roles -> support -> **regular reviews every six months** across all the workplace's reports.

## Model C. Hybrid - a report stewardship programme

Responsibility for supporting analytical solutions is shared with the requester's representatives: **the business stakeholder · the data steward · the R&A report owner**. Certification confirms the dashboard has been verified both by R&A and by the corporate function, and that the data can be trusted for decisions.

The boundary with self-service is simple: **if the business is willing and able to build and maintain a cross-functional report**, it develops and maintains it, and the centralized team helps take another part of the business's requirements into account and includes it in the workplace. **If it is unwilling or unable**, development and support sit with the centralized team and the business participates as the requester.

A separate scenario transition: a report built for one team, on going beyond that team, passes a check for overlap with existing reporting, a joint decision on ownership and, where needed, **a transfer of ownership to the centralized team**, with design and architecture optimization, a logic review, visibility configuration and prepared descriptions.

## The tie to the AI era

Certification stops being only a human trust signal: **a content health score becomes a trust signal for the agent**. Hence the metric from [[ai-ready-domain-score]] - the share of views and queries landing on healthy, certified content. The alternative approach of "certification through tests instead of a passport", and its trade-off, is in `evidence-2026.md` §7.

Links: [[content-mgmt-processes]] · [[content-hygiene-loop]] · [[ai-ready-domain-score]] · [[content-catalog-ux]]
