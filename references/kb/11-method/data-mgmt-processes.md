---
id: data-mgmt-processes
title: 2.1 Data management processes - six processes in two models
type: method
source: "Guide 2.0, sheets \"2.1 Data Mgmt processes\" and \"2.1 Data Mgmt questionnaire\""
board_ref: "https://miro.com/app/board/o9J_lha8MnM=/?moveToWidget=3458764567476311802"
confidence: verifiable
blocks: [4.1]
---

The core of the data TO-BE. The method's key construction: **every process is described twice** - how it is implemented in the centralized model and how in the self-governing one. This operationalizes the dichotomy rather than leaving it as an abstract choice of "we are for self-service".

## The six processes

| Process | Centralized | Self-governing |
|---|---|---|
| **Data source management** | managing and granting access to sources, developing and enforcing policies and procedures | defining, using, evolving and managing data objects and models for analysis |
| **Data quality** | defining the validation process and building trust, designing and applying cleansing rules | applying cleansing rules to your own data |
| **Enrichment & preparation** | defining the ETL process and tooling, preparing sources | using ready sources and applying ETL rules to your own tables |
| **Data security** | security configuration and access control for models, audit | complying with corporate policies and external regulation |
| **Metadata management** | metadata management policy, maintaining metadata for key models, rolling out the data catalog | describing and maintaining the metadata of your own objects |
| **Monitoring & management** | monitoring and auditing usage, compliance control, tool selection | monitoring the metrics of your own sources in centralized tooling |

For each process the sheet requires: **pain points -> a target approach in two or three sentences naming the roles and the tools**.

## The questionnaire - 40+ questions that test whether the process actually exists

- **Data source management** - which sources are key and for which departments · who the steward and owner are · which connection types are allowed (live, extract, embedded, published) · standards for joining in the BI model (a wide consolidated model is more convenient but slower than a normalized one) · the naming convention.
- **Data quality** - the processes ensuring accuracy, completeness, reliability and freshness · is there a checklist · who validates the data before it becomes available · can a business user report a problem to the data owner.
- **Enrichment & preparation** - centralized or self-service · which ETL tools serve which levels of data literacy (enterprise / light / self-service ETL) · what may be done inside the BI system and what outside it (joins, blends, incremental loads, complex scripts) · which source combinations are the most valuable · what keeps the source refresh and the report refresh in sync.
- **Data security** - how data is classified by sensitivity · what the access request process looks like · which visibility levels are in use (database, schema, table, rows, columns) · whether the protection meets legal and regulatory requirements.
- **Metadata management** - what source curation looks like · how you can tell a source is fit for analysis, what its assumptions and problems are · requirements for naming, field formats, hiding duplicates, descriptions · is there a metadata checklist and how it is wired into validation, promotion and certification.
- **Monitoring & management** - how successful the loads are and which errors occur · are there duplicate sources · which schedules are available · how subscriptions, mailings and alerts work · how many self-service users there are and how many come in from mobile · how many sources are used, by whom, and why they fall out of use · the process for removing stale sources · load and performance (CPU, RAM, network, cache hit ratio, latency, active sessions).

## How to read this in the AI era

The questionnaire's questions are the same list as what the agent is missing. "How you can tell a source is fit for analysis and what its assumptions are" is exactly the context whose absence turns text-to-SQL into guesswork.

Links: [[guide-structure]] · [[critical-data-status]] · [[content-mgmt-processes]] · [[data-domains-classification]] · [[access-matrix]]
