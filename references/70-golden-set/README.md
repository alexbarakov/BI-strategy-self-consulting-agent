# The skill's golden set

A regression set: after edits to `references/kb/`, `SKILL.md` or `strategy-template.md`, run it and confirm quality has not dropped.

It is built by the rules the skill itself preaches: the set is frozen before the changes and is not rephrased to match what the agent found; some items are blind; verify is tied to eval.

## Three tiers - they measure different things

| Tier | What it measures | How it is scored | Items |
|---|---|---|---|
| **1 · retrieval** | did the agent find the right knowledge base atoms | deterministically, with no LLM | 101 |
| **2 · answer quality** | did it say what was needed and **not say what is forbidden** | an LLM judge against a rubric, plus the hard rule | 32 |
| **3 · honest refusal** | can it decline to answer | an LLM judge against a rubric | 10 |

Tier 1 is cheap and runs on every change. Tiers 2 and 3 run before a skill release.

**Tier 3 is mandatory.** Without it the set measures only completeness and rewards confident invention - exactly the `plausible but wrong` the whole architecture in the knowledge base exists to guard against.

## The field that makes this worth doing

`must_not` holds the specific wrong answers the knowledge base explicitly refutes: "saved hours are the effect", "we certify everything", "we build the triad in parallel", "the share of certified objects as a metric", "we cut the juniors".

**The hard rule: a match against `must_not` overrides the judge's verdict.** An answer containing a forbidden claim gets "wrong" regardless of how many `must_contain` items it covered. That is the defence against elegant answers where the correct sits next to the harmful.

## End-to-end runs

`e2e-01-severnaya.md` and its successors test assembly rather than recall: an invented company, a full FORM run, honest application of the gates, and a section on "what the run said about the skill itself". The cases are chosen to be **awkward**: a convenient case shows nothing.

Every run leaves two artifacts: the report `e2e-NN-<company>.md` and the strategy itself in the folder `e2e-NN-<company>/` - an eight-page wiki plus `strategy.html`, built by `build-html.py` (no dependencies, opens from disk and on a phone).

The value of a run is in its last section. Findings about the document get fixed in the document; findings about the base go into `kb/60-roadmap.md`.

## How to run it

1. Put the questions from the sets to an agent carrying the skill and collect the answers into `answers.jsonl`:

```json
{"id": "gs1-001", "cited_atoms": ["bi-strategy-purpose"], "answer": "text"}
{"id": "gs2-01", "cited_atoms": ["ai-triad-prerequisites"], "answer": "text", "verdict": "correct_with_a_decision"}
```

2. For tiers 2 and 3, set `verdict` with an LLM judge: the judge gets the question, the answer, `must_contain`, `must_not` and the list of verdicts. The judge does not see the knowledge base - only the rubric.

3. Compute the score:

```bash
python3 score.py answers.jsonl
```

`cited_atoms` holds the identifiers of the atoms the agent cited. If the skill does not emit references, tier 1 cannot be measured - and that is a finding in itself: without provenance you cannot tell knowledge from guessing.

## Metrics

- **Tier 1:** the share of questions hit in full on atoms, and atom recall
- **Tier 2:** the share of `correct_with_a_decision` (primary), plus the same together with `correct_without_a_decision` (secondary)
- **Tier 3:** the share of `refusal_with_a_continuation`; a bare "I don't know" without stating what is missing counts half

Target thresholds are deliberately not set in the sets. They are set from the first measurement: run it, record the baseline, and from then on watch that it does not fall. A threshold taken from somebody else's set is useless.

## Statuses and the blind portion

Every item carries `status: needs_review` - the answers in `../faq-participants.md` the set is built from are a synthesis over the knowledge base, not truth confirmed by the author. **Only `confirmed` counts** - the same mechanic as for domain knowledge base objects.

Items with `blind: true` are not used while refining the skill, only at measurement time. Otherwise the set turns into a specification to fit to.

## A known limitation

The tier 1 questions are taken from the FAQ verbatim, which means they are phrased **in the knowledge base's language**. Such a set partly tests wording overlap rather than understanding. The tier 2 and 3 questions are rephrased in the participant's language specifically to counter this.

The proper fix is to add paraphrases of each question to tier 1 and measure retrieval on those. That is work worth doing before the set starts being treated as an assessment.

## Files

| File | Maintenance |
|---|---|
| `goldenset-tier1.yaml` | **generated** from `../faq-participants.md` - do not edit by hand |
| `goldenset-tier2.yaml` | by hand |
| `goldenset-tier3.yaml` | by hand |
| `build.py` | rebuilds tier 1 after edits to the FAQ |
| `score.py` | aggregates a run, with no external dependencies |

The order when editing the knowledge base: fix the atom -> fix the answer in the FAQ -> `python3 build.py` -> run it -> compare against the baseline.
