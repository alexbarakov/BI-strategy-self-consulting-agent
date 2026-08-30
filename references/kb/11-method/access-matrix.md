---
id: access-matrix
title: 3.1 The access matrix by role and domain
type: method
source: "Guide 2.0, sheet \"3. Access Matrix\""
confidence: verifiable
blocks: [4.1, 6]
---

A matrix of access rules for reports and data: **rows are domains and subdomains, columns are roles**, and each cell holds not a yes/no but a **visibility scope**.

## The vocabulary of visibility scopes

`COMPANY-WIDE` · `LOB` (line of business) · `FBU` (functional business unit) · `LM` (line manager - their own reports) · `Chapter` · `Account` · `Person` · `Offering` · `x` (no access) - plus phrasings such as "within their area of responsibility" and "by budget ownership".

The telling detail in a real example: next to the visibility scope sits the **implementation mechanism** - a specific visibility table or AD filter (`dbo.BU_VISIBILITY_LOGINS_WITHOUT_FULL`, `LoginString_FBU_owners_delegates in FBU_VISIBILITY_LOGINS_UNIFIED`, `oebs.VisibilityFromOracle`, `User filters based on AD group`). A matrix without a mechanism is a declaration; a matrix with one is working row-level security.

## What the header records

For every source: system · domain · **Data Owner (sign off)** · Business Data Steward · R&A Data Steward · data type (regular / sensitive) · level of detail · **date of last review**.

For every role: role group · role · the AD groups it is assembled from.

## The rule

The matrix is filled in from the domain, not from the report. On a first pass it is acceptable to take **one role or one domain** - the method allows this explicitly. The last-review date is mandatory: an access matrix without one goes stale silently.

In the AI perimeter this gains the requirement from `evidence-2026.md` §4.2: an agent is not "a service account with admin rights" but a separate identity with narrow keys and an audit trail.

Links: [[data-domains-classification]] · [[data-mgmt-processes]] · [[user-classification]] · [[rules-and-standards]]
