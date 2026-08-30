---
id: access-automation
title: Automating entitlement management - five pieces of the puzzle
type: method
source: "Course \"BI+AI strategy 26\", the \"Content management\" session, part 2"
confidence: verifiable
blocks: [4.1, 6]
---

> Access is a monster that eats the team's resource and its motivation. **Investment in automating it pays back 100%.**

The method calls this "a really important topic for developing the BI function" and lays out honestly what can be automated and what cannot.

## The five pieces and how automatable they are

| # | Piece | Automation |
|---|---|---|
| 1 | Issuing licences | **yes** |
| 2 | Identifying an employee's role | **yes** |
| 3 | The role-based entitlement matrix | **no** - hand-crafted and signed off, only |
| 4 | Attaching access to BI spaces and reports | **barely** |
| 5 | Rights to part of the data inside a report (RLS) | **yes and no** |

## 1. Licences

The problems: how to let 3,000 users into a system on 1,000 licences · how to eliminate manual key issuance entirely · how to keep developers' extended licences under control.

The solution is three automatic rules: **an automatic check of entitlement to a key · automatic granting when someone moves onto the server · automatic reclamation of the key after X days without a login**. Plus reclaiming extended licences from those who do not use them; consider a virtual machine or a farm.

## 2. Identifying the role

A one-off superhuman effort to derive the rules, plus ongoing maintenance of the group-formation logic.

**Signs the logic has drifted:** daily anomalies in group sizes · a rise in service-desk requests. Both go on automatic monitoring.

## 3. The entitlement matrix - the part that cannot be automated

The thing you have to extract from management (the data owners) with a real effort, structure into the form of a governing document and **get signed off**.

> **The matrix is the mandate to hand out role-based access on its basis without further approvals.**

That is where the payback lies: a matrix agreed once removes the stream of individual approvals. It is built on top of [[info-supply-demand]] - you take the demand matrix and add access levels to it. Format details in [[access-matrix]].

## 4. Attaching access

Automates poorly, so you work through rules instead:
- **no per-person (non-AD-group) access on production reports**
- maximum inheritance of access from the levels above (folder, project, site, space)
- automation of the audit operations

## Questions for self-assessment

Manual entitlements versus AD group sync, is there SSO · what the licence management process, quotas and rules are · are there groups covering the level of available functions (viewing, web editing, publishing, administration) · what the inheritance model from parent spaces looks like · **is there an instruction for the BI champion and the self-service lead with simple guidance on what matters and what to avoid when administering entitlements**.

Links: [[access-matrix]] · [[info-supply-demand]] · [[content-mgmt-processes]] · [[ssbi-workflow]]
