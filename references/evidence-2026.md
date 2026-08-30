# Evidence 2026: what is verifiable, what the vendor measured, what nobody knows

The grounding file for **competent and honest recommendations**. Everything below comes from public sources with links. Its job is to stop the skill from retelling marketing as fact.

## Evidence discipline (always applied)

Tag every figure in the strategy with one of three levels:

| Level | What it is | How to present it |
|---|---|---|
| **Verifiable** | peer-reviewed work, a reproducible benchmark, an independent measurement | safe to rely on; add the link |
| **Vendor-measured** | a vendor benchmark on their own data, a case study, a commissioned survey | present as "claimed", with the measurer named alongside |
| **No data** | no independent research exists | say exactly that; propose measuring it yourself |

The rule: **"no data" ≠ "does not work".** It is an invitation to measure, not a verdict.

The second rule: **the effect of AI cannot be measured by the team's self-assessment** (see METR below).

---

## 1. The perception gap — the single most important fact for a kill-gate

- A randomized trial: 16 experienced developers, 246 real tasks in projects they had worked on for about five years. They expected a 24% speed-up and, after the work, estimated their own speed-up at 20%. The measurement showed them **19% slower** — [METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), [arXiv:2507.09089](https://arxiv.org/abs/2507.09089).
  The authors' own caveats: a small sample, a wide confidence interval, and conditions hostile to AI (mature code, high standards). In a [2026 update](https://metr.org/blog/2026-02-24-uplift-update/) on newer tools the same group showed a speed-up of roughly 18%, and new participants about 4%. **The durable finding is not the sign of the effect but the divergence between self-assessment and measurement.**
- [DORA 2025](https://dora.dev/insights/balancing-ai-tensions/) (~5,000 respondents): 90% use AI, more than 80% believe they are more productive, and **around 30% do not trust the generated code**. Higher adoption correlates with both faster delivery **and greater instability**. AI is an amplifier: it gives speed to a mature pipeline and more chaos to a chaotic one.

**How to use this in the strategy:** in the metrics section, a prohibition on measuring effect by survey; in the kill-gate, a requirement to measure against a golden set.

---

## 2. Where AI actually works in data processes

The pattern: **the closer a task is to "understand the meaning", the better the result; the closer to "provide a guarantee", the worse.** What wins is routing rather than replacement — a deterministic layer on the bulk, the model on the disputed cases.

### Works

| Process | Figure | Caveat |
|---|---|---|
| Classifying PII and confidential content | regex 52.7% → model 95.0% across 1,000 documents; on "confidential" regex scores 0% ([arXiv 2605.20368](https://arxiv.org/pdf/2605.20368)) | regex is roughly 28,000× faster at comparable accuracy on structured fields; ported to another domain, open de-identifiers miss over 50% |
| Entity resolution and deduplication | blocking 35.5% → with an LLM judge 95.4% precision at $0.04 per dataset | you cannot tune the precision/recall threshold to the task; the hybrid wins — the model only on disputed pairs |
| Schema matching during integration | LLM 88.7% against COMA 56.2% and CUPID 51.3% ([GRAM](https://arxiv.org/pdf/2406.01876)) | on simple schemas the classics are no worse and cheaper ([LLMatch](https://arxiv.org/pdf/2507.10897)) |
| Parsing complex tables and scans | 90.2% against 64.6% for a classical engine | on fixed forms ordinary OCR reaches 99% and costs less; parser quality varies enormously ([arXiv 2603.18652](https://arxiv.org/html/2603.18652)) |

### Works only under verification

| Process | Figure | Condition |
|---|---|---|
| Translating SQL between dialects | 76.2% raw → 86.7% with feedback from execution errors ([RISE](https://arxiv.org/pdf/2601.05579)) | an executable comparison of results is mandatory ([Horizon, VLDB](https://www.vldb.org/pvldb/vol18/p5259-emani.pdf)) |
| Descriptions and metadata | 19.6% problematic descriptions from the model against 6.3% from a human ([arXiv 2411.05409](https://arxiv.org/pdf/2411.05409)) | the metric is the share accepted by a steward without edits, not description coverage |
| Pipeline code | speed up, stability down (DORA) | the bottleneck moves into review and testing |

### Overrated or unproven

| Process | What is known |
|---|---|
| Incident root cause | raw telemetry gives 23.75% accuracy, fused sources 48.25% ([arXiv 2602.08804](https://arxiv.org/html/2602.08804v1)); a large controlled study is titled ["Stalled, Biased, and Confused"](https://arxiv.org/html/2601.22208v1); on real telemetry accuracy is [effectively capped](https://arxiv.org/html/2607.13548). **Return ranked evidence, not a verdict.** The limit is not model size but the dependency graph and component taxonomy |
| Generating data quality rules | no independent research exists; "60–80% fewer false positives" appears only in vendor blogs. Measure your own false-positive rate in shadow mode for two weeks |
| Cleaning and synthesizing tabular data | the model [optimizes textual coherence rather than statistics](https://arxiv.org/html/2505.02659); [no method produces an indistinguishable dataset](https://arxiv.org/pdf/2410.03411). Accumulate synthetic data, **do not replace** real data with it |

---

## 3. Context rot — why "give the agent more context" does not work

Answer quality degrades as the supplied text grows, **long before the window is full**.

- 18 models, eight input lengths: degradation at every step, not only near the limit. A model with a 200K window loses noticeable accuracy already at 50K — [Chroma](https://www.trychroma.com/research/context-rot).
- A positional effect: accuracy drops by more than 30% when the needed passage sits in the middle of the context.
- The decline is not smooth: accuracy holds to roughly 51K tokens and then falls by almost half by 64K — [arXiv 2601.15300](https://arxiv.org/pdf/2601.15300).
- Distractors — passages that look right but are not — and a mismatch between the question's wording and the source amplify the effect.
- "Needle in a haystack" tests **understate** the problem: real tasks require synthesis.

**Consequences for context architecture:** serve on request rather than pre-loading; filter out the similar-but-wrong; a bigger window does not remove the need to select.

---

## 4. Data management trends in the AI era

1. **The catalog became a control point rather than a search surface.** One format won, and the dependency moved to the catalog: it resolves names, arbitrates commits, holds permissions and issues short-lived keys to engines. The REST specification standardizes the protocol but **not permissions, masking or lineage** — policies do not transfer between catalogs. The practice: pick one catalog as the governance boundary ([state of catalogs](https://amdatalakehouse.substack.com/p/the-state-of-apache-iceberg-catalogs)).
2. **The agent is a new identity.** The vulnerability formula: private access + untrusted input + an external output channel. In the MCPTox benchmark the most resilient model refused a poisoned tool in under 3% of cases. Static roles are not enough: an agent needs its own identity, narrow short-lived keys, an allowlist of tools, and runtime behaviour monitoring.
3. **The unit of governance became the document fragment.** Permissions from databases and buckets do not travel into vector space; they must be checked **before** retrieval. The same pipeline scores 85–92% on governed data and 45–60% on an ungoverned corpus.
4. **Deletion broke.** Vector stores do soft deletes; deleted vectors are [physically recoverable by reading the index around the API](https://arxiv.org/html/2606.18497). The question to ask a vendor: does the vector remain in the index between the deletion request and the next rebuild?
5. **Answer provenance is not covered by any standard.** Column-level lineage is mature, but the chain "prompt → retrieved chunks → answer" is outside the standard and needs custom extensions ([survey of agent provenance](https://arxiv.org/pdf/2606.04990)).
6. **Contracts: the specification was won, the enforcement was not.** [ODCS](https://bitol.io/) became the de facto standard, but the typical failure is contracts written and wired to nothing. The cheap working layer is a CI gate; the expensive one is a check at the broker. And it is an [organizational problem](https://www.dataengineeringweekly.com/p/data-contracts-a-missed-opportunity), not a technical one.
7. **The economics are not where people look.** 90% of queries from paying customers scan under 100 MB; independently, [more than 99% of users never scan over 1 TB at once](https://motherduck.com/blog/redshift-files-hunt-for-big-data/). The bill grows from unused objects and scheduled recomputation, not from the volume of analysis.

---

## 5. The context layer ("LLM wiki")

### Reference architecture — five layers plus a loop

1. **Sources** — the warehouse, query logs, BI usage, documents, threads, code.
2. **Collection** — connectors, lineage down to columns, mining query history, parsing documents into chunks, event-driven synchronization.
3. **Knowledge assembly** — deduplication, model-written descriptions with a human gate, glossary and metric definitions, "question → SQL" pairs, traps, golden-set questions.
4. **Storage** — a metadata and context graph, the semantic layer, chunk vectors with ACLs, node status, freshness TTL, a reference to the original.
5. **Serving** — MCP: the agent pulls, the permissions are the same as for people, the permission check happens before retrieval, and only what is relevant is returned.
6. **The loop** — the agent writes back what it could not find; demand sets the priority for descriptions; golden-set questions catch breakage after a definition changes; a failed test removes the "verified" status.

### The knowledge atom — mandatory node fields

provenance · status (inferred → candidate → verified → deprecated) · a reference to the source of truth (the formula is never copied) · freshness TTL · the source object with its certification and health score · owner, tests, serving statistics.

This closes the four root problems of a raw knowledge base: where the fact came from, whether it was verified or inferred, whether it has gone stale, and whether it is a copy of a definition that has since diverged. **Trust is inherited from the source object** rather than invented anew.

### The market, as of 2026

- **Atlan** — positioned as a context layer; an enterprise graph, an ontology, a context studio, storage in an open format, MCP/A2A/OSI protocols, bidirectional memory.
- **DataHub** — coming from the open catalog side: the metadata graph grew into a context graph, event-driven sync, six MCP tools, the agent pulls, the same access policies, an open core.
- **Collibra, Alation** — heavy governance platforms; both have MCP, both take long to implement and cost a lot.
- **Secoda → Atlassian** (December 2025), **Select Star → Snowflake** (November 2025) — acquired; the question is whether their roadmaps survive.
- **OpenMetadata** — MCP built in by default, the same authorization engine; the cost moves from licence into maintenance hours.
- **Native platform catalogs** — strong inside their own perimeter.

Having MCP has stopped being a differentiator. The differences moved into storage architecture, permission portability and total cost of ownership.

### Protocols

- **MCP** — carries context, does not produce it.
- **A2A** — how agents negotiate with one another.
- **OSI → Apache Ossie** — a format for exchanging metric definitions, "USB-C for semantics" rather than a new semantic layer; moved to the Apache Software Foundation in 2026.

**Solved by none of them:** permission portability between catalogs, and end-to-end answer provenance.

---

## 6. Next-gen reports: a third format beside the dashboard

**Three formats by purpose:** dashboard (monitoring, read-only, long-lived) → data app (data entry, a scenario, an action) → notebook (one-off investigation).

**Three build approaches** — a different dimension, since each covers several formats:
- **Reactive notebooks** — recomputation by dependency, no hidden state; some store as ordinary code and are reviewed in git. The price: Python skill and your own runtime.
- **Code-first frameworks** — full control of the interface, and a static build from SQL and markup is cheap to host. The price: authorization, permissions, deployment and writes remain yours.
- **Warehouse-native** — permissions inherited from the warehouse and applied at query level, writes go into warehouse tables, metric definitions come from the catalog. The price: you build from the vendor's blocks.

**The sobering figure:** out of 1.45 million notebooks on GitHub only **24% ran without errors and 4% reproduced their own result** ([Pimentel et al., MSR 2019](https://leomurta.github.io/papers/pimentel2019a.pdf)). A notebook without reactivity is a draft, not a report.

**The real dividing line** is not "dashboard or app" but two questions: **does the artifact write back**, and **who applies the permissions**. For a strategy, the data app is a fourth delivery channel beside centralized, self-service and agentic — and it needs its own owner, certification and health score.

---

## 7. Certification: the object passport versus artifact behaviour

Two different questions that are often confused:

| | Passport (governance) | Tests (behaviour) |
|---|---|---|
| What the certificate is | owner + health + description + usage | passing automated tests in the pipeline |
| How it is checked | rules over metadata and logs, covering all content | the test executes: before/after comparison, reconciliation with the source, a performance measurement |
| Trigger | an event or the calendar | every release and platform update |
| Answers the question | "is somebody watching this object?" | "do the numbers reconcile and did anything break?" |

The passport scales across all content but is blind to substantive errors; tests catch regressions and divergence from the source but are expensive per object. **The working combination is a passport everywhere and tests on the critical core.** For AI answers it is the same pair: the health score as a source filter and the golden set as the test.

---

## How to use this in the sections of a strategy

- **Landscape** — a map of "where AI works in our processes" instead of general words about automation.
- **Operating model** — the data app as a fourth channel; the agent as a separate identity.
- **Data processes** — permissions at fragment level, deletion of derivatives, contracts through a CI gate.
- **Content processes** — certification along two dimensions: passport and tests.
- **Technology** — the context layer on top of the triad; the catalog as the governance boundary; serving on request against context rot.
- **Operations** — a prohibition on measuring effect by self-assessment; measurement against a golden set.
- **Plan** — a kill-gate with a threshold derived from your own data, never from somebody else's benchmark.
