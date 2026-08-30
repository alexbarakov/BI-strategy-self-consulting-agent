---
id: content-hygiene-loop
title: Content hygiene - automated monitoring, a content bot and a BI clean-up day
type: pattern
source: "Course \"BI+AI strategy 26\", the \"Content management\" session"
confidence: verifiable
blocks: [4.2, 6]
---

Three mechanisms for keeping production clean - automatic, bot-driven and social.

## 1. Automated monitoring

Monitoring the connections between reports and database tables - hunting legacy and duplicates · removing departed users from the server · removing manual entitlements and all-users entitlements on production reports · finding reports suspected of architectural inefficiency (more than X connections, extract build duration, responsiveness) · reports that are candidates for archiving (no users, no updates) · reports in production with no description.

The output: **regular digests, alerts and shame-lists sent to the authors**.

## 2. The BI content management bot

A tool that runs many checks over a report at once.

**Per report:** extract size against a threshold · performance against a threshold and against previous values, clicking through the filters · links to documentation, yes/no · a data freshness timestamp, yes/no · use of the style guide template (icons, links, fonts) · layout quality (fixed size, containers) · use of colours from the brand range · use of certified sources versus inefficient custom SQL · problems with field naming · whether the report name follows the standards · problems with calculations (the number of level-of-detail expressions and their cascading) · entitlements set up correctly with specific groups · whether the required tags have been added.

**Per folder and project:** the production folder holds all the required attributes (description, domain, security role) · the DEV folder holds no reports older than a month · the archive folder holds no live refresh schedules or subscriptions.

The bot sends notifications to the creator with a call to action, shows problem statistics to the BI server administrator, and runs on a schedule from the admin console.

The natural extension in the AI era: generating a readme from a "Fill with AI" button, with a template and a preview, on top of which a human reads through.

## 3. The BI clean-up day - the social mechanism

An online event or marathon lasting from four hours to several days, once a quarter or twice a year. Two scales: inside the BI team, and company-wide for all BI champions and authors.

**Promotion:** a reminder of why it matters, prizes for participants, a competitive element, a link to the process description.

**What people do:** check their own content against the checklist - data quality, freshness, refreshability · inefficient queries, connections to the wrong sources · naming, metadata, links · moving content between environments, archiving · removing manual entitlements · **peer review of other people's reports, bug testing**.

> **The goal is not to do everything but to build the habit.**

The clean-up day also serves as the point of annual re-confirmation of certification ([[content-certification]]).

## The feedback circuit

A feedback tool on every interface, including the reports themselves, feeding **a CSAT dashboard cut by factor** with a trend on a 30-day rolling window. The factors satisfaction is measured across: overall · navigation · speed · documentation · data update · data accuracy · visualization · download availability · training · support and updates · report turnaround.

That cut immediately shows **which factor specifically is dragging CSAT down**, instead of a general "users are unhappy".

## When the author leaves

The method asks directly: what happens after a report's author leaves - content ownership is handed over, or nothing happens, meaning the report dies? The method says the second option out loud, because it is the actual answer for most, and one of the reasons behind the 88% mortality in [[bi-value-illusion]].

Links: [[content-certification]] · [[content-mgmt-processes]] · [[bi-value-illusion]] · [[content-catalog-ux]]
