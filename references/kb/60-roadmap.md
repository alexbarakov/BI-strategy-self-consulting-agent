---
id: roadmap
title: What the knowledge base lacks, and in what order to fix it
type: meta
source: findings from assembling the base and from checking its figures against primary sources, 2026-08-29
---

# Knowledge base roadmap

This file exists because the base was tested rather than admired. The principle matches the companion's: **an honest gap beats a padded chapter.** Nothing on this list can be closed by generating plausible text — that would destroy the one property the base was assembled for.

## A. Checking the substance — the most urgent

**A1. Verify the remaining figures against primary sources.** The 2026-08-29 pass covered eight load-bearing quantities out of roughly ninety and produced **four discrepancies out of eight** — half. The extrapolation is obvious: the rest of the registry is unverified and must not be treated as verified. Order of work: everything tagged `benchmark` first, because that tag promises reproducibility.

**A2. Close or drop the 19.6% / 6.3% line.** The cited arXiv paper turned out to be about web archive metadata. Either find the real source of the figures or delete the line. It is tagged `disputed` and must not be quoted; the two atoms that cite it now carry the same flag, so what remains is the decision on the line itself — find the source or delete it.

**A3. Separate two different claims about long context — done.** Chroma records continuous degradation; the critical-threshold paper records a collapse after 40–50% of the window. The atom used to merge them into a single "it falls in a step"; `context-layer-market`, `50-failure-catalog` E6, `course-knowledge` and golden set item gs2-05 now state both separately. Kept here as a record of why the distinction matters: the first implies "always serve less", the second implies "watch the share of the window".

**A4. Mark verification dates inside the atoms.** The registry now carries verification dates; the atoms do not. While a figure's status differs between the atom and the registry, the agent will take whichever is closer.

## B. Completeness of the base

**B0. The base is skewed toward a large technology company.** The end-to-end run in `70-golden-set/e2e-01-severnaya.md` on a pharmacy chain showed that the frame comes out correct, but the thresholds and practices suggested come from the perimeter of a large technology company with its own engineering. The fix is not new atoms but caveats about the limits of applicability on the existing ones, starting with the field benchmark.

**B1. Session transcripts.** Real participant questions were reconstructed from written sources: the pre-course survey, the session-one interactive and the questions the author put on slides. Live questions have a different shape — "but our case is a bit special" — and those special cases are the most valuable material. Not currently available.

**B2. The Innovation Map is only partly extracted.** The major directions are captured, the nested detail is not. The frame holds 471 elements.

**B3. Regulated industries and forced migrations.** In the failure catalog these appear only in passing: breaching data residency, auditing access to personal data, honouring a deletion request, missing a migration deadline. There is not enough substance yet for separate entries.

**B4. The economic model.** The base does not answer "how much money is this". A decision was taken not to build a twin of the companion's economics skill: BI has different metrics and different specifics. The question stays open in another form — which lines of effect are defensible for BI at all.

**B5. The contractor delivery model.** The whole base assumes an in-house engineering team. A company whose marts are built by a contractor on request is a common case with different economics, different lead times and a different principal risk — a single point of failure. There is no atom and no line in the failure catalog.

## C. Evaluation

**C1. Paraphrases for tier 1 of the golden set.** The questions are taken from the FAQ verbatim and are phrased in the base's own language, so they partly test string overlap rather than understanding. Tiers 2 and 3 were deliberately reworded; tier 1 was not.

**C2. A golden set for end-to-end assembly.** Done — `70-golden-set/e2e-01-severnaya.md`. Worth extending with a second and third company so that a single case does not become the specification.

**C3. Deterministic checks on the base itself.** Dangling links, atoms without a `confidence` field, atoms missing from the graph, counter mismatches in the README — all currently checked by hand. The companion solves this in its `evals/`.

**C4. Reviewing the golden set.** Every item is `status: needs_review`, because the FAQ answers are a synthesis from the base rather than truth confirmed by the author. Only `confirmed` items count, so formally the count is zero.

## Order

A1 and A2 come first: an unverified figure tagged `benchmark` is more dangerous than a missing one, because it will be quoted in a budget defence. Then C3, as the cheapest. B and C1–C2 as material and time appear.
