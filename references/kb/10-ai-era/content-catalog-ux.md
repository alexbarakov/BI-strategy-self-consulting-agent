---
id: content-catalog-ux
title: Findability of content - the report catalog, the workplace and navigation
type: pattern
source: "Course \"BI+AI strategy 26\", the \"Content management\" session"
confidence: verifiable
blocks: [4.2, 4.3]
---

**Content management is findability too, not only quality.** A health score helps with ranking, but the user needs to find the right thing easily. Under the Jevons paradox, findability is the first thing to go.

## The real user questions the interface has to answer

**Power user, an author:** where do I publish my report · where do I see which reports are built on table X · where do I see who uses my report · how do I set up entitlements · who has access to my report · I want to start building reports, where do I go.

**Casual user, a consumer:** I am looking for a dashboard, how do I find it and get access · how do I work out what the report is about and who to go to with questions · where can I read about the report and what it is built on · I need analytics on metric X, which valid reports exist · I have a question about a report, who do I ask · when was the report last refreshed.

An **ideal report catalog portal interface** has to answer all of these.

## Two ways to implement navigation

| Out of the box - the BI portal | Separate - custom-built, or a section of the corporate portal |
|---|---|
| a tree of folders / projects / collections | can combine several BI interfaces into one the user already knows |
| the discomfort of yet another unfamiliar interface that mass casual users have to be trained on | expensive, worth it with a large number of casual users; more context in a compact form |

An intermediate option is **integrating the report catalog into the corporate Google-like search application**.

## Separating the environments

Organizational (departments/teams) · functional (data domains) · and the lifecycle: **personal folder -> sandbox -> production -> certified report -> archive**.

A practice the course flags as successful: in project sandboxes you may keep any reports and grant access to any employee, **but the entitlements are deleted automatically after a week**. A mechanism, not a policy.

## The analytical workplace

A role-oriented set of recommended content, not a dumping ground. The workplace card holds: a description of the role · how access is granted (AD groups) · how entitlements are sliced · the focus areas of data and analytics · a table of reports with statuses.

**Report statuses in a workplace:** AVAILABLE (ready to use) · AVAILABLE with limitations (suboptimal design, significant assumptions in the logic) · IN PROGRESS · PLANNED. "Available with limitations" is an important honest category that is usually missing.

Plus: an executive sponsor, a working group, support buttons (need training / the report I need does not exist / no access / another question).

The evolution of the implementation: **from Confluence to a built-in interface** in the data catalog, with quick search, take a tour, dashboards and access, dashboard traffic, get help.

## Report descriptions and tags

A description is an end-to-end process of creating and managing a semantic layer of metadata about reports: which questions it answers · how to use it · which metrics are presented · the specifics of data collection and refresh · **the data quality assumptions** · the backlog of development work · ownership · availability and row-level security.

Tags are needed for: categorization through attribution (data domain, workplace, certification by the function) · **search optimization** · key metrics and terms that do not appear in the title.

## The conclusion

Findability is half of content management. The catalog plus a role-specific workplace turn the health score into a real choice for the user **and for the agent**, rather than an invisible back-end rating.

Links: [[content-mgmt-processes]] · [[content-certification]] · [[content-hygiene-loop]] · [[centralized-practices]]
