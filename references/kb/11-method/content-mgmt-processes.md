---
id: content-mgmt-processes
title: 2.2 BI content management processes - six processes in two models
type: method
source: "Guide 2.0, sheets \"2.2 Content Mgmt Processes\" and \"2.2 Content Mgmt questionnaire\""
board_ref: "https://miro.com/app/board/o9J_lha8MnM=/?moveToWidget=3458764567544624352"
confidence: verifiable
blocks: [4.2]
---

The mirror of [[data-mgmt-processes]] for content. The same construction: every process is described in both a centralized and a self-governing implementation, each with its pain points and a target approach naming roles and tools.

## The six processes

| Process | Centralized | Self-governing |
|---|---|---|
| **Content management** | building and maintaining content storage environments, navigation for authors and users | keeping your own content relevant, following the design and architecture requirements |
| **Authorization** | formalizing entitlement policies, tooling, and granting access by rule, role and confidentiality | controlling access to your own content within the organization's rules |
| **Content validation** | defining the correct validation process, validating content | validating your own content, helping check trustworthiness |
| **Content promotion** | the promotion process, promoting centralized and cross-functional reports | promoting your own validated content into the centralized environment through the process |
| **Content certification** | the certification process, working with authors on cross-functional reports | certifying your own trusted content and separating it from untrusted content in the same environment |
| **Content utilization** | measuring report usage by department and role, audit tooling | measuring the usage of your own content |

## The questionnaire is the most useful part

**Content management.** Is content shared company-wide or within roles · what isolates sensitive content (sites, folders, projects) · are folders organized on an organizational, functional or hybrid principle · **are the sandbox, production and archive separated** · the naming convention for reports and folders · is it a practice to publish several copies of one report with different filters · are there descriptions and tags · is there a style guide and a report architecture guide · **is there a maximum acceptable report load time and a procedure for when it is exceeded** · how content ownership is handed over when someone leaves.

**Authorization.** The minimal role for AD/LDAP sync · are the All Users group's rights on the default project set to None · are explicit Denies needed · have groups been created for the authoring and viewing capability sets of each project · have effective permissions been checked on a sample of users · are permissions locked on the parent project · have service accounts been created for published data sources.

**Content validation.** Who takes part · which quality criteria apply in production (completeness, reliability, security, timeliness) and do all production reports meet them · are previous versions replaced · are the data and calculations correct · how architecturally sound is the report · does it follow the visual style guide · does it load in a reasonable time · do the actions behave sensibly · does the dashboard stay valid under different filters (all / none / a single value).

**Content promotion.** Who takes part · is there a checklist of criteria · which communication channels · which events count as news hooks.

**Content certification.** Do authors and users know the process exists · who is responsible for setting the flag · what the criteria are · have all criteria been met · are all fields filled in (about yourself, certification notes, tags).

**Content utilization.** How much traffic reports need · what counts as stale content and how often it is deleted · how much indirect usage there is (alerts and subscriptions) · are subscriptions delivered on time · what the target audience size is and whether the actual one matches · how traffic behaves week over week, month over month, quarter over quarter, and what drives it · visit frequency per user by group, role and report · which cohorts stand out by first-visit date · which BI usage patterns exist and how they change.

## The tie to certification in the AI era

The question "what are the certification criteria" is where the classical method diverges from the "certification through tests" approach. The difference and the trade-off are in `evidence-2026.md` §7.

Links: [[data-mgmt-processes]] · [[centralized-practices]] · [[bi-project-metrics]] · [[guide-structure]]
