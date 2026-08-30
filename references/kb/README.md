# KB — the skill's knowledge base

An atomic knowledge base: **one file = one topic**, linked with Obsidian wiki-links, with a machine-readable graph in `30-graph.yaml`.

Sources broken down into atoms:
- **BI Strategy & Tactics Guide 2.0** (Google Sheets, Data Nature) — the canonical method, 22 worksheets
- **The Miro board `o9J_lha8MnM=`** — the frames "BI Strategy Guide 2.0" (a mirror of the spreadsheet) and "BI Project Innovation Map" (a catalog of directions)
- **The «BI+AI Strategy 2026» course** — nine sessions, in the PDF form they were delivered
- **The pre-course participant survey** — 12 BI projects, July–August 2026

## Structure

Folder numbering is shared with the companion repository [DG Strategy](https://github.com/alexbarakov/DG-strategy-self-consulting-agent): the same number means the same role in both.

| Folder / file | Contents | Files |
|---|---|---|
| `10-ai-era/` | the contemporary layer: concepts, cases and practices from the nine course sessions | 44 |
| `11-method/` | the canonical method: the spine of the guide and each of its worksheets as an atom | 19 |
| `20-catalog/` | the raw catalog of directions (BI Project Innovation Map) | 1 |
| `30-graph.yaml` | the machine-readable graph: strategy block → atoms, key evidence, worked cases | — |
| `30-graph.md` | the visual graph — 10 Mermaid diagrams, rendered natively on GitHub | — |
| `31-field/` | field data: the participant benchmark and the map of pain fronts | 2 |
| `50-failure-catalog.md` | 75 named failures in 7 families, with symptom triage | — |
| `51-numbers.md` | the numbers registry, with reliability tags and verification dates | — |
| `60-roadmap.md` | what the base still lacks and in what order to fix it — driven by findings, not wishes | — |

## Frontmatter conventions

```yaml
id:          # kebab-case, matches the filename
title:       # the heading
type:        # method | pattern | evidence | case | benchmark | catalog | metric
source:      # the primary source
confidence:  # verifiable | vendor-measured | no data | author estimate | mixed
origin:      # optional: marks a worked case whose numeric thresholds are anonymized
blocks:      # which strategy blocks it belongs to (1, 2, 3, 4.1, 4.2, 4.3, 5, 6, 7)
```

## Rules for the agent

1. **Entry point is `30-graph.yaml`**: given a strategy block number, it lists the relevant atoms.
2. **Cite an atom rather than paraphrasing the whole base** — the files are cut one topic apiece precisely so they can be quoted precisely.
3. **Carry the `confidence` label with the figure.** A number tagged as vendor-measured does not become a fact when it moves into an artifact.
4. **Atoms with an `origin` field are worked cases with anonymized thresholds.** The mechanics transfer; thresholds are set from your own baseline. Phrasings such as "roughly threefold" or "about two thirds" are deliberate: what matters is the order of the effect, not somebody else's exact number.
5. **The KB is a source, not an output template.** The artifact is assembled per `strategy-requirements.md`; the KB grounds it.
