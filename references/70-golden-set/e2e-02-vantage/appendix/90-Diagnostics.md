[[index]] · Appendix · Diagnostics

# 🩺 Diagnostics

Self-assessment on the Health Check 0–4 scale (0 no · 1 planned · 2 partially · 3 done, needs improvement · 4 optimized), plus the AI-readiness overlay. Bands: Beginning 0–1 · Learning 1–2 · Developing 2–3 · Mastering 3–4.

**Phases of work:** 🔎 AS-IS = frame blocks 1–2 · 🛠️ TO-BE = 3–6 · 🚀 Transformation = 7.

## The profile

| | Category | Score | Band | What it means here |
|---|---|---|---|---|
| 🟢 | 4 · Self-service delivery | 3.0 | Developing | 40 analysts embedded in squads with real tooling. The company's genuine strength |
| 🟢 | 9 · Project management | 3.0 | Developing | strong agile practice; the work gets planned and shipped |
| 🟡 | 1 · Connection with business | 2.5 | Developing | use cases are registered inside squads; no metric tree, business impact untracked |
| 🟡 | 8 · Security and compliance | 2.5 | Developing | good RBAC from engineering — but the assistant sits outside it (P5) |
| 🟡 | 2 · Adoption and satisfaction | 2.0 | Developing | dashboards measured; assistant measured by calls, which flatters |
| 🟡 | 7 · Data quality management | 2.0 | Developing | contracts on 3 domains of 11 |
| 🔴 | 3 · BI content management | 1.5 | Learning | 912 dashboards, no owner field, no archiving |
| 🔴 | 5 · Guided delivery / support | 1.5 | Learning | no support path for casual users — the assistant became the support, badly |
| 🔴 | 6 · BI platform governance | 1.5 | Learning | **no semantic layer, no metric store.** CI/CD is strong, meaning is absent |
| 🔴 | **AI readiness (overlay)** | **1.4** | Learning | see the breakdown below |

## The AI-readiness overlay

| Component | Score | Note |
|---|---|---|
| Semantic coverage | 0.5 | of the twelve board metrics, none has a single definition |
| Trusted core | 2.0 | 3 domains of 11 |
| Domain context | 1.0 | the assistant's few-shots are the only context, and they are unowned |
| Process readiness for "AI drafts — humans validate" | 1.0 | no verify gate, no eval, no golden set |
| Agentic infrastructure | 2.5 | MCP, tracing and CI exist — engineering's strength again |
| **Average** | **1.4** | |

> The `ai-ready-domain-score` from the knowledge base could not be computed for this company: its first part needs a domain knowledge base, which does not exist. Stated as a target for later rather than dressed up as a current-state number. This is a limitation of the instrument, recorded in the run report.

## The systemic skew

Cut across the solution categories, the picture is unusual and it is the diagnosis:

**Tools and automation: high. Processes and standards: low. Data culture: mixed.**

The company can build anything and agrees on nothing. Almost every standard recommendation aimed at the opposite skew — buy a tool, hire engineers, modernize the platform — would be spent here on something that is already strong.

## The chain breaks

```
core → semantic → context → AI accuracy → self-service
  ●       ✗          ✗          skipped        ●
```

1. **Core → semantic, total.** 3 domains certified; no semantic layer at all.
2. **The few-shots became the de facto semantic layer.** Editable, unversioned, unowned — and it is what the model reasons from. The most expensive break, because it looks like a solution.
3. **The AI accuracy link was skipped rather than broken.** The launch happened ahead of both preceding links, and it cannot be undone. Everything in this strategy is the retroactive form of a gate that was never applied.

## The channel triangle

Self-service dominant · agentic launched early · **centralized effectively absent, and deliberately so**.

The textbook answer here — build centralized reporting to reach a single version of the truth — is not available: there is no factory team and there will not be one. The single version of the truth has to be reached through definitions rather than through a team, which is why S1 carries the weight that a report factory would carry elsewhere.

**Agentic maturity:** claimed at managed autonomy, measured at interoperability. Tools are connected; nothing checks the answers.

---

→ [[index]] · [[01-Context]] · [[appendix/91-Analysis-frame|Analysis frame]]
