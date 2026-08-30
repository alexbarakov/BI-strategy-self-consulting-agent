---
id: data-team-pain-points
title: The pain points of data teams - BI/self-service and data management
type: pattern
source: "Course \"BI+AI strategy 26\", Day 6"
confidence: verifiable
blocks: [1, 4.1]
---

A catalog of pain points for [[painpoints-analysis]], split across two teams. Its value is that it is a ready interview checklist: a pain is either recognized or explicitly absent.

## The pain of a BI / self-service / data team

| Pain | The substance |
|---|---|
| **Access to data** | data groups often have no access to the data of other departments and domains; enormous time goes into coordinating answers and finding the right people. Even where access exists, a lot of time goes into identifying and locating the data |
| **Coordination with business teams** | understanding what a request really means · business validation · handling "similar" requests from different users · differing readings of the logic over the same data · the difficulty of explaining the logic underneath legacy data products |
| **Documentation** | limited time and resource make it impossible to respond promptly to requests to document models and data provenance - the overall quality of the information assets suffers |
| **Impact analysis** | a small change to an attribute can break another department or report, and the team may not even know, because the problem has not surfaced yet. The classic example: changing a field's length takes minutes but triggers an error in a downstream application |
| **Too many datasets** | data spreads across too many datasets; finding and maintaining them becomes a problem, and knowledge about the objects is smeared across teams |
| **The database does not scale** | queries get more complex and take hours or days to run |
| **Files are too big** | large files are expensive to store and awkward to handle; even limitless disks fill up without clean-up processes |

## The pain of a data management team

| Pain | The substance |
|---|---|
| **Protecting personal and confidential information** | coordination with systems, owners and users; lawyers regularly ask where the PII is and how it is protected, and each time it is a hard problem · the processes for clarifying entitlements are often opaque · obfuscation takes a lot of effort |
| **Managing data quality** | organizations often do not know how to manage it; it calls for complex organizational constructions, in place of which a conceptual system develops "in the hands" of individual experts |
| **No common standards** | without shared definitions of business terms it is impossible to develop shared data standards |
| **Transparency of data provenance** | users have no access to lineage; building it is a technical problem with an asterisk on it |
| **Data availability** | owners try to make data available but, because of PII and confidentiality, cannot share it properly in the lake |
| **General compliance** | GDPR, CCPA, HIPAA and their equivalents; **companies over-insure and limit everything indiscriminately, just in case** |
| **Identifying PII** | inventorying every PII element; as data moves from applications to the lake, from the warehouse to reports, tracking gets harder |
| **Documenting data lineage** | GDPR and BCBS 239 require full lineage; the knowledge sits inside the code, so you end up reading source - months of work |
| **The right to be forgotten** | data is spread across systems and is hard to delete or even extract; **most organizations simply ignore the requirement and stay exposed to an audit** |

## How this ties to AI

The first column of the data teams' pain is almost word for word the map of tasks where AI delivers a measurable win (PII classification, deduplication, schema matching, document parsing, recovering lineage from code). The second is the area where AI gives only a draft to be checked. The split and the figures: `evidence-2026.md` §2 and [[ai-in-data-processes]].

Links: [[painpoints-analysis]] · [[data-mgmt-processes]] · [[ai-in-data-processes]] · [[data-catalog-pitfalls]]
