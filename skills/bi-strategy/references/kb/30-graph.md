---
id: graph-visual
title: Визуальный граф тем
type: meta
purpose: та же информация, что в 30-graph.yaml, в виде схем; GitHub рендерит Mermaid нативно
---

# Визуальный граф тем

Рендер `30-graph.yaml`. **Сплошные стрелки** — курируемые типизированные связи из секции `relations`. **Пунктир** — связи, выведенные из содержания и живущие в атомах как `[[wiki-ссылки]]`.

Полный ненаправленный граф — 66 узлов и 283 ребра, изолированных нет; ниже он разложен на читаемые виды, потому что одна схема на 66 узлов нечитаема.

## 1. Кластеры и как они опираются друг на друга

```mermaid
flowchart TB
  VAL["Ценность и зрелость<br/>8 атомов"]
  DEM["Спрос и домены<br/>5"]
  DEL["Модели поставки<br/>11"]
  CON["Контент и доверие<br/>6"]
  DAT["Данные и фундамент<br/>10"]
  AI["AI-фундамент<br/>14"]
  PEO["Люди и команда<br/>6"]
  PRG["Программа и управление<br/>4"]
  FLD["Полевые данные<br/>2"]

  FLD -.->|калибрует| VAL
  FLD -.->|калибрует| DEM
  VAL -->|диагноз задаёт приоритет| DEM
  DEM -->|скоуп проекта| DEL
  DEM -->|домены и критичность| DAT
  DEL -->|что публикуем| CON
  DAT -->|core и семантика| AI
  CON -->|доля потребления на доверенном| AI
  DEL -->|роли и компетенции| PEO
  AI -->|роли гейтов| PEO
  PRG -->|спайн и план| VAL
  PRG -->|спайн и план| DAT
  PEO -->|кто исполняет| PRG

  style AI fill:#e8f7f9,stroke:#2fb9ca
  style PRG fill:#f7f7f7,stroke:#808080
  style FLD fill:#fff8e6,stroke:#d9a441
```

## 2. Цепочка зависимостей — линия защиты бюджета

Порядок, который нельзя переставить. Инициатива, стоящая за непройденным звеном, даёт ноль, а не уменьшенный эффект.

```mermaid
flowchart LR
  A["Сертифицированное ядро<br/>core-layer-project"] --> B["Семантический слой<br/>semantic-layer-evidence"] --> C["Доменный контекст<br/>domain-knowledge-base"] --> D["Точность агента<br/>llm-assistant-architecture"] --> E["Self-service<br/>ssbi-workflow"]

  G1{{"no-semantic-without-core"}} -.-> B
  G2{{"no-assistant-without-foundation"}} -.-> D
  G3{{"no-selfservice-without-governance"}} -.-> E
```

## 3. AI-фундамент — главный кластер

```mermaid
flowchart TB
  subgraph risk["Из чего всё выводится"]
    PBW["plausible-but-wrong<br/>правдоподобно неверный ответ"]
    DUG["data-utility-gap<br/>6 условий utility"]
  end

  subgraph triad["Триада пререквизитов"]
    CORE["core-layer-project"]
    SEM["semantic-layer-evidence"]
    DKB["domain-knowledge-base"]
  end

  subgraph run["Исполнение и управление"]
    ARCH["llm-assistant-architecture<br/>5 слоёв · 7 шагов · контуры A–E"]
    CG["context-governance<br/>Context Unit · trust-плоскость"]
    CLM["context-layer-market<br/>рынок и что доказано"]
  end

  subgraph meas["Замер"]
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
  ARCH -->|feeds очередь моделирования| SEM
  PBW -->|motivates метку доверия| ARCH
  SCORE -->|measures| CORE
  SCORE -->|measures| DKB
  TRAP -.->|constrains| SCORE
  AID -.->|маршрутизация вместо замены| ARCH

  style triad fill:#e8f7f9,stroke:#2fb9ca
  style risk fill:#fdeaea,stroke:#c96
```

## 4. Спайн метода — порядок работы с гайдом

```mermaid
flowchart LR
  subgraph asis["AS-IS · раздел 1"]
    P["painpoints-analysis"] --> DD["data-domains-classification"] --> UC["user-classification"] --> ISD["info-supply-demand"] --> ADO["bi-adoption-stats"]
  end
  subgraph tobe["TO-BE · раздел 2"]
    DMP["data-mgmt-processes"] --> CDS["critical-data-status"]
    CMP["content-mgmt-processes"]
    SSP["selfservice-practices"]
    CP["centralized-practices"]
    TL["bi-toolset-landscape"]
  end
  subgraph ops["Операционка · раздел 3"]
    AM["access-matrix"] --> RM["regular-meetings"] --> RS["rules-and-standards"] --> ON["onboarding-plan"] --> MET["bi-project-metrics"]
  end
  ADO --> DMP
  ADO --> CMP
  ISD -->|feeds| AM
  ops --> AP["action-plan · раздел 4"] --> VIS["vision-statement · раздел 5"]
  P -->|feeds| AP
  GS["guide-structure<br/>спайн, 25 связей — крупнейший хаб"] -.-> asis
  GS -.-> tobe
  GS -.-> ops
```

## 5. Контент: от публикации до доверия агента

```mermaid
flowchart LR
  CMP["content-mgmt-processes<br/>6 процессов × 2 модели"] --> CERT["content-certification<br/>3 модели сертификации"]
  CMP --> HYG["content-hygiene-loop<br/>автомониторинг · бот · субботник"]
  CERT --> UX["content-catalog-ux<br/>находимость и АРМ"]
  UX -->|completes| CERT
  HYG -->|addresses| ILL["bi-value-illusion<br/>88% / 10% / 2%"]
  PROM["content-promotion-monitoring<br/>engagement × match rate"] --> MET["bi-project-metrics"]
  VSG["visual-style-guide<br/>3 слоя гайда"] -.-> CMP
  CERT -->|доля потребления| SCORE["ai-ready-domain-score"]
  ILL -->|motivates| MET
```

## 6. Модели поставки

```mermaid
flowchart TB
  SVG["ssbi-vs-guided<br/>два смысла self-service"] -->|explains| SFC["ssbi-failure-causes<br/>8 + 7 причин · 4 сегмента"]
  SVG --> WF["ssbi-workflow<br/>curate→create→consume<br/>propose→prototype→promote"]
  UC["user-classification"] -->|prerequisite| WF
  WF -->|feeds| CERT["content-certification"]
  SSP["selfservice-practices<br/>29 позиций"] --- COM["bi-community-management"]
  CP["centralized-practices<br/>15 практик"] --- BRAND["centralized-bi-brand<br/>премиальный сервис"]
  PLAT["unified-bi-platform<br/>3 слоя как один продукт"] -->|contains| NG["nextgen-report-formats<br/>дашборд · data app · ноутбук"]
  TOOL["bi-tool-selection<br/>рынок РФ и опросник"] -.-> PLAT
  INS["insight-management<br/>прямое · косвенное · делегированное"] -.-> CP
```

## 7. Данные, governance и экономика

```mermaid
flowchart TB
  DD["data-domains-classification"] -->|prerequisite| CDS["critical-data-status<br/>MDS-реестр"]
  DD -->|prerequisite| AM["access-matrix"]
  AM -->|implements| AA["access-automation<br/>5 элементов пазла"]
  CDS -->|prerequisite| CORE["core-layer-project"]
  DGL["dg-launch-path<br/>common sense → MVP → программа"] -->|sequences| DMP["data-mgmt-processes"]
  CAT["data-catalog-pitfalls<br/>ghost town · золотой путь"] -->|feeds| DKB["domain-knowledge-base"]
  BILL["infra-billing<br/>читающий платит за чтение"] -->|funds| CORE
  PAIN["data-team-pain-points<br/>7 + 9 болей"] -.->|maps-onto| AID["ai-in-data-processes"]
  GLO["glossary-vs-dictionary"] -.-> CAT
```

## 8. Люди и управление программой

```mermaid
flowchart LR
  ORG["bi-org-structure<br/>IT-centric ↔ business-centric<br/>D&A Council"] -->|staffs| MTX["bi-competency-matrix<br/>L1–L3 · LLM внутри уровня"]
  MTX -->|aligns| HIRE["bi-hiring-ai-era<br/>Grade Discovery · min(hard,soft)"]
  ORG --> CAL["bi-routine-calendar<br/>день · спринт · квартал"]
  CAL -->|operates| HYG["content-hygiene-loop"]
  COM["bi-community-management<br/>чемпионы · пояса"] -->|operates| SSP["selfservice-practices"]
  ON["onboarding-plan"] -.->|аудит стандартов| RS["rules-and-standards"]
  RM["regular-meetings<br/>governance держит один слот"] -->|operates| AP["action-plan"]
  ACC["ai-accelerator"] -.-> COM
```

## 9. Вход «у нас что-то не так»

Семейства из `50-failure-catalog.md` и куда они ведут.

```mermaid
flowchart LR
  S(["Симптом"]) --> A["A · Ценность и спрос<br/>8 провалов"]
  S --> B["B · Контент и доверие<br/>10"]
  S --> C["C · Модель поставки<br/>10"]
  S --> D["D · Данные и фундамент<br/>13"]
  S --> E["E · AI и контекст<br/>15"]
  S --> F["F · Люди<br/>9"]
  S --> G["G · Управление программой<br/>10"]

  A --> ILL["bi-value-illusion"]
  B --> HYG["content-hygiene-loop"]
  C --> SVG["ssbi-vs-guided"]
  D --> DGL["dg-launch-path"]
  E --> PBW["plausible-but-wrong"]
  F --> MTX["bi-competency-matrix"]
  G --> AP["action-plan"]
```

## 10. Диагностика, калибровка и рыночная рамка

Девять узлов, которые не ложатся в предыдущие схемы: они питают вход, а не строятся по цепочке.

```mermaid
flowchart TB
  subgraph field["Полевая калибровка"]
    PB["participants-2026-benchmark<br/>12 проектов, n=12"]
    PF["pain-fronts-2026<br/>3 фронта болей"]
  end
  subgraph diag["Диагностика"]
    MM["maturity-models<br/>TDWI · пропасть · diagnostic gap"]
    BAB["bi-adoption-barriers<br/>44 фактора"]
    BSP["bi-strategy-purpose<br/>6 типовых ошибок стратегии"]
  end
  subgraph market["Рыночная рамка"]
    AIB["ai-in-bi-approaches<br/>4 подхода · 6 слоёв · контур РФ"]
    AAW["ai-adoption-waves<br/>4 волны внедрения"]
    ACP["ai-cases-in-prod<br/>2 продовых кейса"]
  end
  IM["innovation-map<br/>каталог направлений<br/>как чеклист полноты"]

  PF -->|calibrates| PP["painpoints-analysis"]
  PB -->|calibrates| MM
  MM -->|precedes| SCORE["ai-ready-domain-score"]
  BAB -.-> ADO["bi-adoption-stats"]
  BSP -.-> AP["action-plan"]
  AIB -.->|выбор подхода| TL["bi-toolset-landscape"]
  AAW -->|sequences| ACC["ai-accelerator"]
  ACP -->|demonstrates| TRAP["ai-time-saving-trap"]
  IM -->|feeds| AP

  style field fill:#fff8e6,stroke:#d9a441
```

---

**Как читать порядок сборки стратегии.** Полевые данные калибруют ожидания → диагностика ценности и зрелости даёт приоритет → спрос определяет скоуп → домены и критичность задают фундамент → триада строится по одному слою за раз с eval до и после → контент и self-service идут поверх готового фундамента, а не параллельно ему → люди и регулярный менеджмент удерживают всё это дольше квартала.
