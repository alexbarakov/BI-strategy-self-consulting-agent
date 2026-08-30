---
id: ssbi-failure-causes
title: Why self-service BI fails, and where it is ineffective in principle
type: pattern
source: "Course \"BI+AI strategy 26\", Day 3"
confidence: author estimate
blocks: [3, 4.3]
---

## Causes of failure: the user's problems

1. A shortage of basic competence in working with data
2. A shortage of the specific competence to build reports
3. A shortage of the competence to build "good-looking" reports
4. Users slide back to isolated shadow BI solutions
5. They keep going to IT to ask for edits
6. They create too much content, most of it out of date
7. They stop using self-service after the training and forget the skills
8. It takes too long - they are not willing to step away from their main job

## Causes of failure: problems with the product or service

1. It is hard to learn which data sources are available
2. It is hard to pick the right source out of many similar ones
3. It is hard to understand the data, the field names and their values
4. Adding fields and modifying a source needs IT support
5. Report and source quality is opaque, causing problems when reusing somebody else's report
6. It is opaque who owns a report and who is answerable for the data in it
7. A shortage of formal training - both induction and regular courses

**An observation:** the list of product problems matches almost word for word the list of what an AI agent is missing. That is also the argument for why investment in semantics and metadata pays back twice.

## Four segments where self-service is ineffective by its nature

| Segment | Why |
|---|---|
| **Company-wide reporting for top management** | there is no cross-check: a department does not put its report past the others before sending it upwards, so the data gets disputed and contradicts other reports |
| **Cross-role unified reporting** | cross-data reports are difficult; "nobody has time for anybody else" - a data owner has no interest in sharing a report outwards, since that means taking other groups' requirements on board, plus approvals and support |
| **Reports for functions that cannot or will not build a BI practice** | they cannot be left without a service; besides, a BI analyst working alone inside a function burns out quickly and does not grow |
| **Reports on especially confidential data** | the data has to be sliced against a role-based entitlement model, which an individual department finds hard and uninteresting to build |

Plus the general cause: **a shortage of BI skill and a stylistic free-for-all** - departments differ in level and in formats, and find it hard to sync them.

## The fight over a single version of the truth - the mechanics

The business inevitably creates analytics centres inside functional units, which serve their own requester and have an interest in autonomy. **Business logic gets monopolized inside the units**: the analysts and the requester decide for themselves how to calculate an indicator, where to store it and how to visualize it.

> Three lines of business will calculate staff turnover three different ways and produce three reports. The HR department may hold a fourth logic and a report that the business lines will dispute. That kicks off a chain of number reconciliations and unsettles the entire management team.

**What centralized BI should do:** identify the data owner -> facilitate the discussion and agree a shared logic everyone can live with -> fix it in the glossary -> ensure collection and validation, build a report that takes everyone's requirements into account and is more convenient than the alternatives -> **make sure the alternatives are deleted**.

That last step is usually skipped, which is why the conflict comes back.

## The fine line of usefulness

- BI will tend to want everyone inside its own dashboards - "it is simpler that way"
- Push data-illiterate users into a complex, awkward self-service and "you get more new problems with them than without"
- **"Abandoned" content means you grew reports where nobody is ready to maintain them**

Links: [[ssbi-vs-guided]] · [[ssbi-workflow]] · [[bi-adoption-barriers]] · [[content-mgmt-processes]]
