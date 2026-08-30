---
id: plausible-but-wrong
title: The plausible-but-wrong answer - the central risk of AI analytics
type: pattern
source: "Course \"BI+AI strategy 26\", Day 7"
confidence: verifiable
blocks: [2, 5]
---

**More dangerous than an error is a plausible wrong answer.**

- A demo on a toy schema always works: a small space, obvious joins.
- In production the agent guesses and produces **plausible but wrong**: syntactically valid SQL, but the wrong metric, the wrong period, the wrong cut.

## The mechanics of trust collapse

`A plausible wrong answer -> trust falls -> back to Excel`

One plausible wrong answer damages trust more than an honest "I don't know". Metric consistency built over years is lost, and **trust is the BI function's most expensive asset**.

## Three design consequences

1. **"I can't" is a valid answer.** The assistant must be able to refuse, and the refusal must be designed as a normal scenario rather than a failure.
2. **A clarifying question is cheaper than a wrong answer.** If there are two readings, put the question back to the user; measurement shows the difference between the no-clarification and the clarification modes to be fundamental.
3. **A trust marker and provenance are mandatory in the answer** - which measure, which query, as of what date. See the runtime in [[llm-assistant-architecture]].

## The risk the whole architecture exists for

> The query ran without an error and returned a wrong number - silently, with no signal.

Offline and online validation, the golden set and the trust plane are all derived from this one risk. Everything else is implementation detail.

Links: [[ai-triad-prerequisites]] · [[llm-assistant-architecture]] · [[context-governance]] · [[data-utility-gap]]
