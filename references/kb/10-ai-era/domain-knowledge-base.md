---
id: domain-knowledge-base
title: The domain knowledge base - what is in it, how to populate it, how to measure it
type: method
source: "Course \"BI+AI strategy 26\", Day 7 - internal practice"
confidence: verifiable (internal measurements)
origin: "an internal case walked through on the course; the numeric thresholds are anonymized - calibrate from your own baseline"
blocks: [4.3, 5, 6]
---

**The domain knowledge base as a skill: the agent answers from the domain, not from the model's memory.**

## Why - a diagnosis of what causes wrong answers

The causes of an agent's inventions come down to one block: **a shortage of knowledge about domain specifics** - the rules for using objects in a use case, the assumptions, the accepted interpretations, the links between objects and business processes.

A bigger model does not cure this; only external knowledge does.

## The population roadmap

0. **Agree the boundary of responsibility with the head of analytics** - a domain or a subdomain, an internal decision
1. **Choose a pack** - packs already exist by domain and subdomain; if the tree needs changing, take it to the shared domain channel; if there is no pack, a separate skill creates one
2. **Install your pack for yourself and the team** - install the knowledge base skill, run the onboarding, and from there the agent explains what to do
3. **Populate through real work and the enrichment skill** - start with **a small golden set (dozens of questions, not hundreds)**, the FAQ and the objects, then work down the list; have the agent review whatever gets loaded during bulk enrichment
4. **Watch the formal completeness dashboard** - work towards the full set of criteria, drawing the team in
5. *(beyond the goal)* **Understand and improve quality** together with the specialist team

## Two quality signals

- **Signal 1 - the accuracy of the duty bot in the channel**, the best proxy for knowledge base quality. In the case walked through, connecting a populated knowledge base raised average auto-answer accuracy **a little over threefold** - from a level at which the bot was unusable to the level of a working tool.
- **Signal 2 - your own golden set.** An internal benchmark for the domain; when you add new knowledge it makes sense to extend the question list right away. It shows whether the agent answers your own typical questions correctly.

This is the strongest argument for investing in context: **the delta comes from knowledge, not from the model** - the model is the same in both measurements. Your own effect size has to be measured on your own golden set, before and after.

## Skill enrichment - all you decide is what to throw in

Enrichment takes free-form input, classifies the entity family itself (FAQ / glossary / text2sql / object / lineage) and routes it to the right adding skill.

| Trigger | What you hand the agent |
|---|---|
| The agent failed and you prompted it | "run everything I had to prompt you with through enrichment" |
| A useful wiki page | the link or the page ID |
| A recurring question in a channel | a link to the thread - the skill extracts the question, the answer and the artifacts itself |
| A colleague sent shared SQL | the SQL itself plus one sentence on "what it counts" |
| You learned a table dependency X -> Y | one sentence of plain text |

**Merging into your own domain needs no approvals - but do read the PR with your own eyes.**

**What we do not take:** PII, tokens, `.env`, one-off SQL, sandbox tables, whole large research pieces.

The entry barrier matters here: the "one sentence" bar is what separates a knowledge base that gets populated from one that does not.

## The object lifecycle and the metric

Statuses:
- **needs_review** - a candidate, unverified knowledge
- **master_system_autosync** - the object came from a master system or an automatic trusted source (the catalog, the metric registry, BI); counted as verified
- **confirmed** - the domain owner has confirmed it is valid
- **archived** - deleted or obsolete

> **The team lead's metric: only `confirmed` and `master_system_autosync` count.** Generated objects count only after review.

This is the key defence against gaming: without it, bulk auto-generation instantly "closes" completeness while adding no knowledge. A useful habit is to ask the agent regularly which objects are currently in `needs_review`.

## Formal completeness

Computed as a composite per domain from roughly a dozen binary criteria, and it forms the first part of [[ai-ready-domain-score]]. The knowledge object types completeness is checked across: FAQ · objects · glossary · documentation · lineage · SQL · eval cases · metrics (technical and business name) · skills · eval coverage.

Also tracked: the contribution of teams and team leads, the number of contributors, commits and knowledge items in the period, and a ranking of contributors.

Links: [[ai-triad-prerequisites]] · [[ai-ready-domain-score]] · [[context-governance]] · [[llm-assistant-architecture]]
