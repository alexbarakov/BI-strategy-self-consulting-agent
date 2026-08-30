---
id: graph-visual
title: Visual theme graph
type: meta
purpose: the same information as 30-graph.yaml, drawn; GitHub renders Mermaid natively
---

# Visual theme graph

Rendered from `30-graph.yaml`. **Solid arrows** are the curated typed relations from the `relations` section. **Dotted arrows** are relations inferred from the content, living in the atoms as ordinary Obsidian wiki-links.

The full undirected graph has 66 nodes and 283 edges with no isolates. It is broken into readable views below, because a single diagram of 66 nodes is unreadable.

## 1. Clusters and how they rest on one another

```mermaid
flowchart TB
  VAL["Value and maturity<br/>8 atoms"]
  DEM["Demand and domains<br/>5"]
  DEL["Delivery models<br/>11"]
  CON["Content and trust<br/>6"]
  DAT["Data and foundation<br/>10"]
  AI["AI foundation<br/>14"]
  PEO["People and team<br/>6"]
  PRG["Programme and management<br/>4"]
  FLD["Field data<br/>2"]

  FLD -.->|calibrates| VAL
  FLD -.->|calibrates| DEM
  VAL -->|diagnosis sets priority| DEM
  DEM -->|project scope| DEL
  DEM -->|domains and criticality| DAT
  DEL -->|what we publish| CON
  DAT -->|core and semantics| AI
  CON -->|share of consumption on trusted| AI
  DEL -->|roles and competencies| PEO
  AI -->|gate roles| PEO
  PRG -->|spine and plan| VAL
  PRG -->|spine and plan| DAT
  PEO -->|who executes| PRG

  style AI fill:#e8f7f9,stroke:#2fb9ca
  style PRG fill:#f7f7f7,stroke:#808080
  style FLD fill:#fff8e6,stroke:#d9a441
```

## 2. The dependency chain — the budget-defence line

An order that cannot be rearranged. An initiative standing behind an unpassed link yields zero, not a reduced effect.

```mermaid
flowchart LR
  A["Certified core<br/>core-layer-project"] --> B["Semantic layer<br/>semantic-layer-evidence"] --> C["Domain context<br/>domain-knowledge-base"] --> D["Agent accuracy<br/>llm-assistant-architecture"] --> E["Self-service<br/>ssbi-workflow"]

  G1{{"no-semantic-without-core"}} -.-> B
  G2{{"no-assistant-without-foundation"}} -.-> D
  G3{{"no-selfservice-without-governance"}} -.-> E
```

## 3. The AI foundation — the principal cluster

```mermaid
flowchart TB
  subgraph risk["What it all follows from"]
    PBW["plausible-but-wrong<br/>the plausible wrong answer"]
    DUG["data-utility-gap<br/>the six utility conditions"]
  end

  subgraph triad["The prerequisite triad"]
    CORE["core-layer-project"]
    SEM["semantic-layer-evidence"]
    DKB["domain-knowledge-base"]
  end

  subgraph run["Execution and control"]
    ARCH["llm-assistant-architecture<br/>5 layers · 7 steps · loops A-E"]
    CG["context-governance<br/>Context Unit · trust plane"]
    CLM["context-layer-market<br/>the market and what is proven"]
  end

  subgraph meas["Measurement"]
    SCORE["ai-ready-domain-score"]
    TRAP["ai-time-saving-trap"]
    AID["ai-in-data-processes"]
  end

  PBW -->|motivates| TRIADN["ai-triad-prerequisites"]
  DUG -->|motivates| TRIADN
  TRIADN --> CORE
  CORE -->|prerequisite| SEM
  SEM -->|prerequisite| DKB
  TRIADN -->|enables| ARCH
  CG -->|governs| DKB
  CLM -->|implements| CG
  ARCH -->|feeds modelling queue| SEM
  PBW -->|motivates the trust label| ARCH
  SCORE -->|measures| CORE
  SCORE -->|measures| DKB
  TRAP -.->|constrains| SCORE
  AID -.->|routing instead of replacement| ARCH

  style triad fill:#e8f7f9,stroke:#2fb9ca
  style risk fill:#fdeaea,stroke:#c96
```

## 4. The method spine — the order of work through the guide

```mermaid
flowchart LR
  subgraph asis["AS-IS · section 1"]
    P["painpoints-analysis"] --> DD["data-domains-classification"] --> UC["user-classification"] --> ISD["info-supply-demand"] --> ADO["bi-adoption-stats"]
  end
  subgraph tobe["TO-BE · section 2"]
    DMP["data-mgmt-processes"] --> CDS["critical-data-status"]
    CMP["content-mgmt-processes"]
    SSP["selfservice-practices"]
    CP["centralized-practices"]
    TL["bi-toolset-landscape"]
  end
  subgraph ops["Operations · section 3"]
    AM["access-matrix"] --> RM["regular-meetings"] --> RS["rules-and-standards"] --> ON["onboarding-plan"] --> MET["bi-project-metrics"]
  end
  ADO --> DMP
  ADO --> CMP
  ISD -->|feeds| AM
  ops --> AP["action-plan · section 4"] --> VIS["vision-statement · section 5"]
  P -->|feeds| AP
  GS["guide-structure<br/>the spine, 25 links - the largest hub"] -.-> asis
  GS -.-> tobe
  GS -.-> ops
```

## 5. Content: from publication to an agent's trust

```mermaid
flowchart LR
  CMP["content-mgmt-processes<br/>6 processes x 2 models"] --> CERT["content-certification<br/>3 certification models"]
  CMP --> HYG["content-hygiene-loop<br/>auto-monitoring · bot · clean-up day"]
  CERT --> UX["content-catalog-ux<br/>findability and the workspace"]
  UX -->|completes| CERT
  HYG -->|addresses| ILL["bi-value-illusion<br/>88% / 10% / 2%"]
  PROM["content-promotion-monitoring<br/>engagement x match rate"] --> MET["bi-project-metrics"]
  VSG["visual-style-guide<br/>the guide's 3 layers"] -.-> CMP
  CERT -->|share of consumption| SCORE["ai-ready-domain-score"]
  ILL -->|motivates| MET
```

## 6. Delivery models

```mermaid
flowchart TB
  SVG["ssbi-vs-guided<br/>the two meanings of self-service"] -->|explains| SFC["ssbi-failure-causes<br/>8 + 7 causes · 4 segments"]
  SVG --> WF["ssbi-workflow<br/>curate→create→consume<br/>propose→prototype→promote"]
  UC["user-classification"] -->|prerequisite| WF
  WF -->|feeds| CERT["content-certification"]
  SSP["selfservice-practices<br/>29 entries"] --- COM["bi-community-management"]
  CP["centralized-practices<br/>15 practices"] --- BRAND["centralized-bi-brand<br/>a premium service"]
  PLAT["unified-bi-platform<br/>3 layers as one product"] -->|contains| NG["nextgen-report-formats<br/>dashboard · data app · notebook"]
  TOOL["bi-tool-selection<br/>the market and the questionnaire"] -.-> PLAT
  INS["insight-management<br/>direct · indirect · delegated"] -.-> CP
```

## 7. Data, governance and economics

```mermaid
flowchart TB
  DD["data-domains-classification"] -->|prerequisite| CDS["critical-data-status<br/>master source register"]
  DD -->|prerequisite| AM["access-matrix"]
  AM -->|implements| AA["access-automation<br/>5 pieces of the puzzle"]
  CDS -->|prerequisite| CORE["core-layer-project"]
  DGL["dg-launch-path<br/>common sense -> MVP -> programme"] -->|sequences| DMP["data-mgmt-processes"]
  CAT["data-catalog-pitfalls<br/>ghost town · golden path"] -->|feeds| DKB["domain-knowledge-base"]
  BILL["infra-billing<br/>the reader pays for reads"] -->|funds| CORE
  PAIN["data-team-pain-points<br/>7 + 9 pains"] -.->|maps-onto| AID["ai-in-data-processes"]
  GLO["glossary-vs-dictionary"] -.-> CAT
```

## 8. People and programme management

```mermaid
flowchart LR
  ORG["bi-org-structure<br/>IT-centric <-> business-centric<br/>D&amp;A Council"] -->|staffs| MTX["bi-competency-matrix<br/>L1-L3 · LLM inside each level"]
  MTX -->|aligns| HIRE["bi-hiring-ai-era<br/>Grade Discovery · min(hard, soft)"]
  ORG --> CAL["bi-routine-calendar<br/>day · sprint · quarter"]
  CAL -->|operates| HYG["content-hygiene-loop"]
  COM["bi-community-management<br/>champions · belts"] -->|operates| SSP["selfservice-practices"]
  ON["onboarding-plan"] -.->|standards audit| RS["rules-and-standards"]
  RM["regular-meetings<br/>governance held by one slot"] -->|operates| AP["action-plan"]
  ACC["ai-accelerator"] -.-> COM
```

## 9. The "something is wrong with us" entry

The families from `50-failure-catalog.md` and where they lead.

```mermaid
flowchart LR
  S(["Symptom"]) --> A["A · Value and demand<br/>8 failures"]
  S --> B["B · Content and trust<br/>10"]
  S --> C["C · Delivery model<br/>10"]
  S --> D["D · Data and foundation<br/>13"]
  S --> E["E · AI and context<br/>15"]
  S --> F["F · People<br/>9"]
  S --> G["G · Programme management<br/>10"]

  A --> ILL["bi-value-illusion"]
  B --> HYG["content-hygiene-loop"]
  C --> SVG["ssbi-vs-guided"]
  D --> DGL["dg-launch-path"]
  E --> PBW["plausible-but-wrong"]
  F --> MTX["bi-competency-matrix"]
  G --> AP["action-plan"]
```

## 10. Diagnostics, calibration and the market frame

Nine nodes that do not fit the earlier diagrams: they feed the input rather than sit on the chain.

```mermaid
flowchart TB
  subgraph field["Field calibration"]
    PB["participants-2026-benchmark<br/>12 projects, n=12"]
    PF["pain-fronts-2026<br/>3 pain fronts"]
  end
  subgraph diag["Diagnostics"]
    MM["maturity-models<br/>TDWI · the chasm · diagnostic gap"]
    BAB["bi-adoption-barriers<br/>44 factors"]
    BSP["bi-strategy-purpose<br/>6 typical strategy errors"]
  end
  subgraph market["Market frame"]
    AIB["ai-in-bi-approaches<br/>4 approaches · 6 layers · regulatory perimeter"]
    AAW["ai-adoption-waves<br/>4 adoption waves"]
    ACP["ai-cases-in-prod<br/>2 production cases"]
  end
  IM["innovation-map<br/>catalog of directions<br/>as a completeness checklist"]

  PF -->|calibrates| PP["painpoints-analysis"]
  PB -->|calibrates| MM
  MM -->|precedes| SCORE["ai-ready-domain-score"]
  BAB -.-> ADO["bi-adoption-stats"]
  BSP -.-> AP["action-plan"]
  AIB -.->|approach choice| TL["bi-toolset-landscape"]
  AAW -->|sequences| ACC["ai-accelerator"]
  ACP -->|demonstrates| TRAP["ai-time-saving-trap"]
  IM -->|feeds| AP

  style field fill:#fff8e6,stroke:#d9a441
```

---

**How to read the assembly order.** Field data calibrates expectations → the value and maturity diagnosis sets the priority → demand defines the scope → domains and criticality set the foundation → the triad is built one layer at a time with an eval before and after → content and self-service go on top of a finished foundation rather than alongside it → people and regular management keep it all alive beyond a quarter.
