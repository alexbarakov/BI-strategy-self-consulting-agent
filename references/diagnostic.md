# The maturity diagnosis model

Based on the **BI Project Health Check** (the Data Nature method / Alex Barakov), extended with the course's **AI-readiness overlay**. Reference file: `BI Project Health Check.xlsx`.

## The scale (0–4)

The base scale, used for most factors:

| Score | Meaning |
|---|---|
| 0 | No |
| 1 | Planned |
| 2 | In progress / partially |
| 3 | Completed, but needs improvement |
| 4 | Fully completed and optimized |

Special scales on the same 0–4 range: **applicability** (not applicable → highly applicable), **user count** (≤50 / ≤150 / ≤500 / 500+), **business dependency** (high / moderate / low), **disruption likelihood** (very likely / somewhat / unlikely).

For each factor the participant gives a current score **and a one-year target**. The gap (target − current) is the priority.

## Maturity bands

The category average maps to a band: **Beginning (0–1) · Learning (1–2) · Developing (2–3) · Mastering (3–4)**.

## Visualizing maturity (mandatory)

In the diagnostics page, insert a **maturity bar chart by theme** (as in the Data & Analytics Maturity Tool): horizontal 0–4 bars across the nine categories plus AI readiness, with the Beginning / Learning / Developing / Mastering zones marked. Generate it with `references/make-maturity-svg.py` (put the participant's self-assessment into `SCORES`) → `assets/maturity.svg`, and embed it. Add a "phases of work" block: 🔎 AS-IS = blocks 1–2, 🛠️ TO-BE = 3–6, 🚀 Transformation = 7.

## The nine Health Check categories and their factors

1. **Connection with business** (6): registering analytical use cases; integration into business processes; aligning BI goals with business goals; defining the target audience roles; structuring business metrics (the metric tree); tracking business impact.
2. **Adoption and satisfaction** (7): BI usage monitoring ("BI for BI"); adoption measurement; business engagement (>50% active); satisfaction surveys; feedback collection; onboarding new users.
3. **BI content management** (12): acceptance criteria; a documented development process; a testing and release checklist; report documentation; content certification with the business; glossary integration; archiving; tracking and improving load times; a style guide; a content health SLA.
4. **Self-service BI delivery** (8): balance of the operating model (central + self-service); consistency of methodology and tooling; a portal or communication channel; content handover and review; a BI champions programme; learning paths; community development; training and mentoring.
5. **Guided BI service delivery** (8): user support; training; joint data analysis sessions; data availability and explorability; mobile optimization; usability testing; UX behaviour analysis; improving BI portal navigation.
6. **BI platform governance** (10): **semantic layer**; **metric store**; insight management; CI/CD; self-service ETL; performance monitoring; query optimization; a platform upgrade process; data catalog integration; subscription automation.
7. **Data quality management** (6): automated report refresh; data validation; certified sources; source documentation; lineage change tracking; transparency of data freshness.
8. **BI security and compliance** (8): role-based access; automated role identification; an access request workflow; directory integration; security audits; compliance (GDPR/HIPAA); risk assessment; disaster recovery.
9. **Project management** (8): a prioritization system; task tracking; agile practice (Kanban/Scrum); a competency matrix; operational KPIs; team goal setting; a long-term BI strategic plan; standardized hiring.

An extended block (D&A and data governance maturity, ~83 factors) is used in Full mode: data sharing and democratization; **data governance** (sponsorship, stewardship, budget, policies, classification, metadata, catalog, roadmap); data quality management; data security; **data architecture** (architecture reviews, scalability, integrated governance, modern and cloud, real time, **AI/ML**, **data mesh**, **data contracts**); strategic leadership (D&A vision, executive involvement, investment, data literacy, ethics).

## Seven solution categories (a cross-cut)

Every factor is tagged with one of: **Business alignment · Data culture · Processes and standards · User engagement · Skills and training · Tools and automation · Efficiency monitoring**. A second scorecard computes maturity along this cut, which is useful for spotting a systemic skew — strong tooling with weak user engagement, for instance.

## The AI-readiness overlay (the course layer)

On top of the Health Check, score AI readiness 0–4 using the same bands. Treat it as a tenth category:

- **Semantic coverage** — the share of key metrics with an unambiguous definition in the semantic layer or metric store.
- **Trusted core** — the share of queries and reports running on a certified core layer; whether ownership, SLA and data quality checks exist on the marts.
- **Domain context** — the completeness of the domain knowledge base: objects, glossary, FAQ, "question → SQL" examples, eval cases.
- **Process readiness** for "AI drafts — humans validate": is there a verify gate, are there kill-gates, is there eval infrastructure.
- **Agentic infrastructure** — MCP access to services, a skill registry, judge gates and guardrails, observability and tracing.

### Additional 2026 factors (ask these in Full mode)

- **Context layer** — is there one place the agent takes meaning from, or is context reassembled for every case.
- **Governance boundary** — one catalog as the source of permissions, or permissions spread across several systems.
- **Agent identity** — does the agent have its own credentials, narrow keys and an audit trail, or does it operate under a person's account.
- **Permissions on unstructured content** — do ACLs reach document fragments and vectors; are they checked before retrieval or after.
- **Deleting derivatives** — can a deletion request actually be fulfilled, including vectors and derived knowledge nodes.
- **Answer provenance** — can the chain "prompt → retrieved chunks → answer" be reconstructed.
- **Data apps as a channel** — do analytical applications have an owner, certification and a health score, or do they live outside the perimeter.

## Diagnosing the dependency chain (the key output)

Walk the chain and find where it snaps first:

```
core layer → certified metrics (semantic) → domain context
          → AI accuracy → self-service
```

The rule: **an AI feature cannot be placed ahead of its link.** On dirty data it returns plausible garbage and destroys trust. Name the two or three most expensive breaks — they become priority number one in the action plan.

## How the diagnosis feeds the strategy

- Weak **categories** (Beginning / Learning) → TO-BE initiatives in the corresponding Planner blocks and in the action plan.
- A skew across **solution categories** → a systemic recommendation (for example, "the tools are there and adoption is not → work on user engagement, not on another tool").
- **The chain break** → the order of the stack-rank (Governance → Trusted Data → AI readiness → BI Content → Self-service).
- The participant's **one-year targets** → measurable goals in the vision.
