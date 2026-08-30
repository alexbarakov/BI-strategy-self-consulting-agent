[[../index|← BI+AI Strategy]] · appendix

# 90. Maturity diagnostics

Scale 0–4: 0 none · 1 planned · 2 partial · 3 done, needs improvement · 4 complete and optimized.

| Level | Categories | What it means |
|---|---|---|
| 🔴 **1** | Data management · Data quality · Governance and ownership | The function does not exist: no roles, no processes, no tooling. The break is at the first link of the chain |
| 🟡 **2** | BI content management · Project management · Security and access | Processes exist de facto but are undocumented; security is handled at the platform level, not at the model level |
| 🟡 **2** | Connection with the business | Stakeholders exist and are active, but requirements arrive as report tickets rather than as questions |
| 🔴 **1** | Adoption and satisfaction | Not measured |
| 🔴 **1** | Self-service delivery | Some analysts have access, there are no rules |
| 🟡 **2** | Guided delivery | Executive reports are produced centrally and reliably — the only thing that works as a process |

**Average level: 1.5.** No strong categories.

## AI readiness

| Dimension | Score | Comment |
|---|---|---|
| Semantic coverage | 0 | no layer |
| Certified core | 0 | marts are built per task |
| Domain context | 0 | does not exist as a class |
| Process readiness for "AI drafts — humans validate" | 1 | report review exists but is informal |
| Answer-quality measurement | 0 | no golden set |

## Breaks in the chain

`core → semantics → context → AI accuracy → self-service`

The break is at the **first link**. Two expensive consequences: every data mart costs weeks and money, and there is nothing to build a metric layer on. Everything right of the first link is unreachable while it stays open — hence the stream order in [[../02-Streams]].
