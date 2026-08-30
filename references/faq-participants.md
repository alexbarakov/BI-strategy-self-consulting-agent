# A base of participant questions, answered from the knowledge base

The questions people actually ask on the "Building a BI+AI strategy" course, with answers grounded in `references/kb/`. Every answer points at atoms - the detailed evidence and its reliability level live there.

## Provenance of the questions

| Mark | Where it comes from |
|---|---|
| **◆ real** | the pre-course participant survey (n=12, July-August 2026) and the Day 1 interactive (n=10, companies A-J) - phrased from their own words |
| **◇ from the floor** | a question the author put on a slide for group discussion - that is, knowingly contentious |
| **○ potential** | constructed from the knowledge base: a place where strategies usually break, which the participant has not yet asked about |

**How to use this.** The answers are deliberately short and take a position - they are prompts for discussion, not final verdicts. The numeric thresholds in the case atoms are anonymized: transplant the mechanics, set the thresholds from your own baseline.

---

## 1. BI problems, trends, the structure of a strategy

**◇ Can you live without a BI strategy?**
You can, and the method admits it outright: nobody will die, and there is a year of work queued up anyway. The argument is not about the document but about the format: two two-day workshops a year with business stakeholders, where the team makes decisions on processes, roles and tools. The underrated side effect is that it is the best instrument of professional motivation for the team and the reason key experts stay. → [[bi-strategy-purpose]]

**◇ Can you write a strategy with GenAI?**
You can write a draft; you cannot make the decisions. The course's principle: AI generates the draft, a human checks it. In practice that means an LLM is good at assembling a long list of use cases with RICE scoring and at rewriting phrasing, but the choice of "what we freeze first" and "who owns it" stays human. The check is to put the result through the judge stage. → [[bi-strategy-purpose]], `review-gates.md`

**○ Where do you start if there has never been a strategy?**
With the guide's first sheet, not with the target picture: pain points across the four role groups, then grouping them and naming candidate initiatives. The order of the sheets is the order of the work - each one rests on the last. → [[guide-structure]], [[painpoints-analysis]]

**◆ We have no single strategy: IT does not drive the processes and the business does not know how. Who should be the driver?**
That is a diagnosis from the "who drives it" column in the landscape inventory - the exercise's most useful column. It exposes disciplines that formally exist but that nobody runs. The answer to "who" follows from where BI sits: in an IT-centric model nobody will become the driver; in a business-centric one the function appears together with a CDO or CAO. → [[bi-adoption-stats]], [[bi-org-structure]]

**○ How do we know our BI project actually delivers?**
Start with the unpleasant number: 88% of reports die within three months, 10% live on minimal traffic, 2% deliver a stable result. Median dashboard life is about 50 days, three times longer where practices are mature. If the team cannot say where its 2% is, then the metrics "reports with falling traffic" and "users who came once" simply do not exist. → [[bi-value-illusion]], [[bi-project-metrics]]

**○ Will AI devalue the BI function?**
The method names two symmetrical illusions: "it is all over, GenAI will replace everything shortly" and "GenAI is just hype, nothing can beat us". Both get in the way. The facts sit in between: an agent is a data consumer too, but without intuition, and it needs all six utility conditions at once. Which is why governance, data quality and semantics do not wither - they matter more. → [[bi-value-illusion]], [[data-utility-gap]]

**◆ We are doing import substitution and rolling out AI at the same time. How do we not tear ourselves apart?**
These are two projects with different gates, and combining them into one stream is a reliable way to complete neither. The choice of an AI approach in the Russian perimeter is determined not by a feature ranking but by the combination of features, jurisdiction and geopolitics: the personal data law, the critical infrastructure law, the FSTEC requirements, the sanctions risk of a foreign LLM. On-prem plus a domestic model removes the sanctions risk but closes off some scenarios. → [[ai-in-bi-approaches]], [[bi-tool-selection]]

---

## 2. Vision, the supply and demand of analytics

**◇ Why do I need the global picture - I am just a BI manager who administers the server and builds reports on request?**
The method answers in one line: you cannot meet needs you do not know about. The supply-demand matrix is the definition of the project's scope, and without it priorities get set by whoever asks loudest. → [[info-supply-demand]]

**◇ How do you set priorities?**
Two working mechanics. The simple scoring one: the report is needed by three roles `+3`, a CxO is among the requesters `+2`, the requester has no resource of their own `+2`, the automation effect is 2 FTE `+1`. The formal one: RICE = Reach x Impact x Confidence / Effort. The second is more honest but requires a confidence figure, which most people set from intuition - and that has to be flagged. → [[info-supply-demand]]

**○ How many domains do we have to cover to close most of the cases?**
20-40% of domains cover 60-85% of the use cases. Hence the working order: a long list of cases -> prioritization -> which data they need -> which data products follow. It is also the argument against trying to "describe all the domains first". → [[info-supply-demand]], [[data-domains-classification]]

**◆ The business does not understand what data the company holds or why it should be managed. Where do we start?**
Not with governance but with the domain classification and the question "how much would we lose if this data were deleted". Classifying into strategic / critical / cross-functional / local turns an abstract conversation into a conversation about damage. Then comes the data owner who signs off, kept separate from the stewards who run it. → [[data-domains-classification]], [[pain-fronts-2026]]

**◆ The business will not take responsibility for metric methodology. What do we do?**
This is the most frequent pain in the sample, and persuasion does not fix it. The mechanic from the method: centralized BI identifies the data owner -> facilitates agreement on a shared logic -> fixes it in the glossary -> builds a report more convenient than the alternatives -> **and makes sure the alternatives get deleted**. That last step is usually skipped, which is why the conflict comes back. → [[ssbi-failure-causes]], [[glossary-vs-dictionary]]

**○ How do we gather information needs if the business does not come to us?**
Six channels, not one: interviews with executives and with the analysts of each line, an analysis of the current reports (spreadsheets and slides included), an analysis of the company's strategy and its metrics, surveys, your own analysis of operational processes for slack, and market benchmarking. Plus an LLM to assemble the long list of cases, with a human reading it through afterwards. → [[info-supply-demand]]

**○ How do we classify users so it does not stay a spreadsheet?**
In two passes. Identify - find everyone who uses data and reports; classify - split them into casual (data customers and explorers) and power (analysts and data scientists). The practical output the whole thing exists for is **auto-populated AD groups for granting rights** to self-service tools, not the typology itself. → [[user-classification]]

**○ How do we record the status of critical data so that it is a decision, not a report?**
With a domain scorecard: business criticality, master source coverage, the key marts, the quality status and **plans for the quarter**. Separately, a master data source registry (not to be confused with MDM): selecting the marts best suited to the domain, cutting duplicates, focusing ownership and monitoring on those alone. This is the sheet that answers the question "what is the agent allowed to answer on". → [[critical-data-status]]

---

## 3. Assessment and maturity

**◇ Who last assessed their BI system, when, and how?**
Two formats by effort: light - usage statistics plus a survey inside the team, about a week; extended - the same plus six or more interviews and a request for the standards, up to six weeks. Nine assessment areas: the link to the business, adoption and satisfaction, content management, self-service delivery, guided delivery, platform governance, data quality, security, project management. → [[maturity-models]], `diagnostic.md`

**○ We are stuck - we seem to have everything, but maturity does not grow. Why?**
The TDWI model puts a **chasm** between the early and the established level, and that is where most stop. What blocks the crossing: not enough flexibility in the tooling, mental fragmentation and a shortage of trust, tools inadequate to the tasks, political infighting. None of these is fixed by buying software. → [[maturity-models]]

**○ We have plenty of dashboards but decisions do not change. Where is the gap?**
The diagnostic analytics gap: companies get stuck on "what happened" and never reach "why". The causes run along four axes - people (analysts do not understand the business, the business cannot use the tools), tools (a dashboard is not built for finding causes), processes (no structured approach to root cause), culture (settling for surface-level conclusions). This is also the clearest place to apply AI. → [[maturity-models]], [[ai-cases-in-prod]]

**◆ How do we compute adoption if we have no number?**
If a participant cannot name a percentage, that is a finding for the diagnostic block, not a gap in the questionnaire. The sample spread runs from 20% to 90%, and some respondents give an absolute user count instead of a percentage, which is a diagnosis in itself. A useful pair of metrics: the target group's engagement rate and the target audience match rate - the first without the second deceives. → [[participants-2026-benchmark]], [[content-promotion-monitoring]]

**○ How do we measure AI readiness rather than merely declare it?**
A composite score per domain in two parts: the formal completeness of the domain knowledge base (about a dozen binary criteria) plus four non-knowledge-base criteria - are the three roles named, the share of healthy metrics, the share of dashboard **views** landing on certified content, the share of **queries** hitting certified marts. The key property: it measures the share of consumption, not the share of coverage - the latter can be inflated by certifying dead content. → [[ai-ready-domain-score]]

**◆ We have no semantic layer, no catalog and no labelling - is that normal?**
Statistically, yes. Not one company in the sample has a fully mature semantic layer: half have none or none planned, a third have one under development. In four companies of twelve there is no governance team at all. That is not an excuse but a calibration: you have not fallen behind, you are in the main group. → [[participants-2026-benchmark]]

---

## 4. Governance: self-service, guided, agentic

**◇ Does self-service BI actually work?**
Two different scenarios live under the term, and conflating them is the source of most failures. Teaching casual users to build reports themselves is a scenario with near-zero uptake, which the method suggests calling **guided BI**. Giving power users inside business teams the tools is what self-service actually is, and it proves its worth in large companies. → [[ssbi-vs-guided]]

**◆ We gave everyone development access with no criteria and now have to sort it out. How?**
Not by taking access away but by building the missing link - the right-to-left workflow: `propose -> prototype -> promote`. A popular self-service report goes to the governance committee as a **prototype** of a new cross-functional report; the committee checks the indicators and definitions and the BI team prepares the mass version. Without the reverse direction a good report stays local forever and production silts up. → [[ssbi-workflow]], [[content-certification]]

**○ Where is self-service ineffective in principle?**
Four segments: company-wide reporting for top management (no cross-check), cross-role unified reporting (the domain owner has no interest in sharing), reports for functions that cannot or will not grow a BI practice, and reports on especially confidential data (complex role-based slicing). Those four segments stay centralized at any maturity level. → [[ssbi-failure-causes]]

**○ We gave users a tool and they do not use it. What is wrong?**
Most likely you gave the wrong tool to the wrong role. The main mistake is handing data consumers the analysts' tools: they take fright at the number of buttons and phone the local analyst. The role-to-tool mapping: consumers get ready reports, explorers get templates, published sources and light data wrangling, analysts get data preparation plus visual discovery, scientists get code. → [[ssbi-workflow]]

**◆ A small headcount against a wish to put everything in order. What comes first?**
Rehearse the cut before it happens: answer the question "if we lose a third of the resource, what dies first" and publish the answer. The freeze order is set by the stack rank: governance -> trusted data -> AI readiness -> BI content -> self-service, cutting right to left. A deliberate refusal to improve something is a strategic decision that has to be recorded. → `review-gates.md`, [[action-plan]]

**○ Centralized BI and self-service conflict. How do we reconcile them?**
The method's formula: self-service will not replace the centralized approach, and without self-service the centralized approach will not reach a single version of the truth. Both patterns of dominance produce the same result - insufficient penetration of BI into the business - for different reasons. The practical conclusion: separate heads for the reporting factory and the self-service office, or one block eats the other. → [[ssbi-vs-guided]], [[bi-org-structure]]

**○ Which community practices do we take if we have little resource?**
Not all of them - the catalog of 29 entries (16 tools, 7 event types, 6 support types) is filled in across "applicable · driver · timing", and **an entry with no named driver equals an entry marked not applicable**. Pick three to five and name an owner. Cheap with a proven effect: regular open consultations run by the competence centre for analysts noticeably raise the quality of what they build themselves. → [[selfservice-practices]]

**○ What should centralized BI be able to do besides building reports?**
A catalog of 15 practices, the last two of which are AI's point of entry into the classical method: **a navigation assistant** (explains terms and recommends a report for a request) and **a data assistant** (gives metric values and describes deviations). Both are described as ordinary team services with their own owner and SLA rather than as a separate AI initiative. → [[centralized-practices]]

**○ What makes people use our data product, and what gets in the way?**
It makes them: the data is unique outside it, the logic is hard to reproduce yourself, it is easy to find, the quality is predictable, it is documented, and it saves their own team's resource. It gets in the way: no trust in the owner, cases of not being told about changes, missing fields, infrequent refresh, awkward tools and **simply not knowing it exists**. This is gathered through a standing circuit rather than a one-off audit: customer development interviews, surveys, access statistics. → [[bi-adoption-barriers]]

---

## 5. Content management: certification, hygiene, findability

**◇ Report certification - a sensible topic or over-engineering?**
Over-engineering if you certify everything. The construction that works is two-tier: **automatic** certification on machine-checkable signs (metadata filled in, a heading naming the owner, documentation present, objects in production folders, the report is fast) - applied to everything except sandboxes and personal folders; **data certification** on methodology, ETL, metrics and reconciliation - only for the most-viewed reports or on request. → [[content-certification]]

**◇ What happens after a report's author leaves?**
Two honest options: ownership is handed over, or nothing happens - meaning the report dies. The method says the second out loud, because it is the actual answer for most and one of the causes behind the 88% mortality. "How is ownership handed over when someone leaves" is a separate item in the content management questionnaire. → [[content-hygiene-loop]], [[bi-value-illusion]]

**◆ Reports with no owner keep appearing. How do we stop it?**
With three mechanisms at once, because none works alone. Automated monitoring - reports with no owner, no description and no updates go into digests and shame-lists. The content bot - scheduled checks with a notification to the creator. The BI clean-up day - a quarterly marathon where everyone cleans their own content against a checklist; the goal is not to do everything but **to build the habit**. → [[content-hygiene-loop]]

**◇ How do you separate the content environments?**
The lifecycle: personal folder -> sandbox -> production -> certified -> archive, with an organizational or functional folder principle on top. The most elegant practice from the course: in project sandboxes you may keep anything and grant access to anyone, **but the entitlements are removed automatically after a week**. A mechanism instead of a policy. → [[content-catalog-ux]]

**◆ Junk reports in production, walls of code in the data sources, production-grade reports creeping into the sandboxes. Where do we start?**
With automatic archiving on the "no users, no updates" signal - the only category where the decision needs no approvals. Then separating the environments and setting an acceptable load time with a procedure for when it is exceeded. The order matters: remove the dead first, then fix the living. → [[content-hygiene-loop]], [[content-mgmt-processes]]

**○ We built a health score and users still cannot find what they need. Why?**
Because content management is findability too, not only quality. A health score ranks, but the user needs to **find**. A report catalog plus a role-oriented analytical workplace turn the score into a real choice for the user and for the agent rather than an invisible back-end rating. → [[content-catalog-ux]]

**◇ A designer in the BI team - overkill or salvation?**
Salvation, if their duties are design audit, coaching, polishing and live design rather than drawing dashboards. Teaching high-class design to a developer with no aptitude is probably not on. A style guide works only in three layers: the report template inside the tool, the visual vocabulary there too, and the corporate textbook **outside the BI tool**. Mixing the layers is the standard reason the guide goes unused. → [[visual-style-guide]]

**◇ How does a design guide take root with you?**
The course's short formula: "redesign into the template as a service" plus training. Develop it jointly, hand it over for maintenance, train people, use it for every centralized report, help with redesigns on request. A guide that is merely published never takes root. → [[visual-style-guide]]

**○ How do we know a report's promotion worked?**
Through traffic analysis after the release and a cohort analysis by first-visit date. And one question asked before the promotion that settles more than the channels do: **does the author want other people to use their report, and are they willing to take other people's requirements on board?** If not, no amount of mailing will help. → [[content-promotion-monitoring]]

---

## 6. Data management and data governance

**◆ High time to market on marts - analysts go around the rules. What comes first, speeding up or tightening up?**
Both at once. A rule that costs more than going around it will not be followed - that is the shortest argument against governance-first without investing in speed. In a strategy, governance initiatives and time-to-market initiatives have to move as a pair, not in sequence. → [[pain-fronts-2026]], [[dg-launch-path]]

**○ We were refused the data governance budget. Is the direction dead?**
No, it is a standard branch of the route. Until it is obvious whether formal governance is needed, **common-sense governance** runs at the level of individual teams - small quick-win projects measured in weeks. A budget refusal means continuing on that branch and restarting through an MVP later. Governance started from the bottom survives the budget cycle. → [[dg-launch-path]]

**○ When do we move from the MVP to a programme?**
The condition is stated explicitly: at least **2 of 4** - interest from other domain owners, a domain owner willing to take part in the MVP, support at COO/CTO/CFO/CEO level, support from the ML/warehouse/product analytics teams. Fewer than two means it is early. → [[dg-launch-path]]

**◆ Cross-domain data availability is our main pain. How do we solve it?**
Through an access matrix built from the domain rather than from the report, with a mandatory implementation mechanism in each cell. A matrix that does not name the visibility table or the AD filter is a declaration. And crucially: an agreed matrix is **the mandate to hand out role-based access without further approvals**, which is what the whole exercise is for. → [[access-matrix]], [[access-automation]]

**○ What in entitlement management genuinely automates?**
Licences, yes (automatic entitlement checks, automatic granting on entry, automatic reclamation after N idle days). Role identification, yes, with a one-off major effort plus maintenance of the group logic. **The role matrix, no** - it has to be pulled out of the data owners and signed off. Attaching access, barely - you work through rules instead: no per-person entitlements in production, maximum inheritance from above. → [[access-automation]]

**◇ When is it time to roll out a data catalog?**
When the aggregate efficiency loss of the power users exceeds the cost of the solution - and the method suggests **measuring that with an experiment** rather than deciding by feel. The formula for the measurement: time to value = delivery date minus committed date. → [[data-catalog-pitfalls]]

**○ We rolled out a catalog and it is empty. Now what?**
Three antidotes to the ghost town: automate metadata extraction as far as possible (domain and stewards can be computed algorithmically), enter documentation **in the flow of work** - up to and including CI/CD checks that break the build - and curate the top 20% of most-queried objects instead of trying to boil the ocean. → [[data-catalog-pitfalls]]

**○ We have a catalog but nobody uses it - it competes with the wiki and the messenger.**
That is fragmentation of the golden path. The antidote is to choose one path deliberately and **switch off the duplicating functions**. Three classic points: discussions (do not believe in the catalog's built-in messenger - that is self-deception), the knowledge base (pick one and integrate it into the other), running queries. → [[data-catalog-pitfalls]]

**◆ How do we sell the business the value of data roles - DataOps, stewards, QA?**
Not through the importance of the roles but through money and through AI readiness. Billing turns infrastructure consumption into the domain's unit economics and makes the cost of the long tail of unused marts visible. The core layer is packaged so that the same work covers two goals: analyst speed and the domain's readiness for AI. → [[infra-billing]], [[core-layer-project]]

**○ Which marts do we start the core layer with?**
Not the most painful ones - they are expensive and slow, and the project stalls on the first hard case without having shown value. Start with the most **reused** cross-domain entities (customer, listing, deal): maximum reuse per unit of effort. Presentation layer first, technical second. The health score suggests candidates before any manual selection. → [[core-layer-project]]

**○ Where does AI genuinely help in data management, and where does it not?**
There is one regularity: the closer the task is to "make sense of meaning" the better, the closer to "give a guarantee" the worse. It works for: PII classification, deduplication, schema matching on hard cases, parsing complex tables. Only under verification: SQL translation between dialects, descriptions and metadata, pipeline code. Unproven: incident root cause, generating data quality rules. The rule: the deterministic layer takes the bulk volume, the model takes the disputed cases. → [[ai-in-data-processes]]

**○ How do we describe data management processes without it being a retelling of DAMA?**
Each process is described **twice** - how it is implemented in the centralized model and how in the self-governing one. Six processes: sources, quality, enrichment and preparation, security, metadata, monitoring. For each: the pain points and a target approach in two or three sentences with roles and tools. A questionnaire of 40+ questions tests whether the process actually exists rather than merely being named. → [[data-mgmt-processes]]

**○ Is our pain unique?**
Probably not. A ready interview checklist: seven pains of a BI/self-service team (access to data, coordination with the business, documentation, impact analysis, too many datasets, the database does not scale, files are too big) and nine pains of data management (PII, quality, no common standards, lineage, availability, compliance, identifying PII, documenting lineage, the right to be forgotten). The first list matches almost word for word the map of tasks where AI gives a measurable win. → [[data-team-pain-points]]

---

## 7. The AI foundation: semantics, core, context

**◆ What AI work actually survives to production for people?**
By the sample, what works **on top of an existing structure**: MCP for analysing and building dashboards, ad-hoc as a chatbot scenario, automatic presentations with LLM summarization, personalized HTML reports, internal skills for gathering requirements and prototyping. What does not survive is anything that required the model to reconstruct the semantics itself: text-to-SQL prototypes, RAG over metrics, automatic A/B summaries. → [[participants-2026-benchmark]]

**◆ What percentage of ad-hoc can genuinely go to AI?**
Participants' subjective estimates run 20-90%, with a median around 70-80%. The most honest formulation in the sample: "70%, but that high estimate reflects the fact that the basic data need is not yet met." That is, a high estimate of the potential often means low maturity of demand. The course's ceiling estimate is more modest - 15-25% of queries. → [[participants-2026-benchmark]], [[insight-management]]

**○ Why does a text-to-SQL demo work while production lies?**
The demo runs on a toy schema: a small space, obvious joins. In production the agent guesses and produces **plausible but wrong** - syntactically valid SQL, but the wrong metric, the wrong period, the wrong cut. And that is more dangerous than an error: one plausible wrong answer damages trust more than an honest "I don't know", and after that the user goes back to Excel. → [[plausible-but-wrong]]

**○ Where do we start the triad - semantics, core or the knowledge base?**
With the layer that closes the domain's most expensive pain, and **one at a time with an eval before and after**. Metric consistency hurts - start with the semantic layer. Finding data and joining it hurts - start with the core layer. The agent does not understand the domain - start with the domain knowledge base, which gives the fastest accuracy gain. Building all three at once is a reliable way to finish none. → [[ai-triad-prerequisites]]

**◆ Should we put the source systems, not just the warehouse, into the semantic layer right now?**
No, not if there is still no stable contract beneath the core layer: the `no-semantic-without-core` kill-gate has not been passed. The separation settles the question: the core layer is "what from", always materialized; the semantic layer is "what to compute", materializing nothing; the engine is "how to serve", on the fly by default. Sources get connected once the core layer already covers the key entities. → [[unified-bi-platform]], [[ai-triad-prerequisites]]

**○ How much does a semantic layer really raise accuracy?**
Paired measurements where only the presence of semantics changes: on a corporate schema of 199 tables, threefold; on hard questions not one is solved on the raw schema, and about 39% with semantics; on a real warehouse with 2,730+ columns, half again. Three conclusions: the dirtier the schema the bigger the effect; **the model barely matters** - reasoning effort does not change accuracy once the layer exists; and the nature of the error changes - the layer answers "I can't" while SQL generation lies silently. → [[semantic-layer-evidence]]

**○ Text-to-SQL or text-to-semantic?**
The complexity has moved out of defining metrics and into executing them. An agent that writes SQL every time works out afresh where the data is, how to join it, what the grain is and which formula applies - every query is a new attempt to guess. An agent that asks the runtime for a metric gets the same answer to the same question. Security and row-level security move there too: **entitlements are applied while the query is assembled, not as a filter afterwards**. → [[semantic-layer-evidence]]

**○ What actually has to be in an LLM assistant's architecture so that it does not lie?**
Five layers and seven runtime steps, four of which are critical: the role and the domain arrive **with the question**, not afterwards; on two readings, ask a clarifying question rather than guess; the route is chosen on the "covered by semantics or not" criterion; and the answer carries the number, a trust marker and provenance. Plus "I can't" as a valid answer. → [[llm-assistant-architecture]]

**○ We populated the knowledge base. Why did accuracy not rise?**
Because population is not trust is not effect - three different metrics. Only objects with `confirmed` status, or those arriving from a trusted master system, should count; generated content counts **only after review**. Without that rule, bulk auto-generation instantly "closes" completeness while adding no knowledge. → [[domain-knowledge-base]], [[context-governance]]

**○ Is more context better?**
No. Context rot: quality degrades as input grows, independently verified across 18 models. Hence the serving rule: MCP returns **only what is relevant**, and the ACL filter is applied before the search rather than after. → [[context-layer-market]]

**○ Who should verify the context, and will that not become a bottleneck?**
It will, if the gate has no time budget. The construction that works: the BI partner holds the domain's verify gate with an explicit weekly budget, and if the queue eats more than that, **the platform gets fixed, not the person**. The gate's load becomes a platform health metric. And the curator does not write context - they judge the machine's draft. → [[context-governance]], [[context-layer-market]]

**○ How do we know when to stop a context initiative?**
The kill-gate is stated plainly: if the accuracy gain from context is not significant, stop. Useless context knocks down trust in the whole AI agenda. The measurement is on your own golden set, before and after the context is supplied; verify is tied to eval, and you cannot mark as verified something that lowers accuracy. → [[context-layer-market]]

---

## 8. Tools and the platform

**◇ Who ran into which rollout problems?**
The fork after 2022 comes down to three strategies: re-implement, look for workarounds, build your own. The method's practical conclusion: despite the existence of supply workarounds, the risks are usually rated too high for further investment - and that consideration matters more than a feature comparison. → [[bi-tool-selection]]

**○ How do we compare BI systems without arguing forever?**
With a weighted questionnaire: the working group sets each factor's weight from the business requirements (1-3), and the tool is scored from the pilot results (1-5). Otherwise the comparison turns into an argument about whose favourite tool is better. In 2026 the factor list has to include AI functionality, built-in governance features and row-level security. → [[bi-tool-selection]]

**○ The dashboard is no longer the only format. What else is there?**
Three formats by purpose: the **dashboard** (monitoring, read-only, long-lived, a mass audience), the **data app** (data entry, a scenario, an action, read-write, calls an agent), the **notebook** (a one-off investigation, a single author, short-lived). The approaches to building them are a different dimension: reactive notebooks, code-first frameworks, warehouse-native. The key question in choosing is not "which framework" but **who is answerable for entitlements and writes**. → [[nextgen-report-formats]]

**○ Buy a context platform or build our own?**
What is worth buying is the **architecture**, not the claimed percentages: where the context sits, whose entitlements apply, whether you can take the data out. Every loud effect figure is a vendor's internal benchmark on its own data. The cost trap with open-source solutions: the licence is zero but it costs 0.25-1 FTE of a platform engineer; with commercial ones the price is driven by the number of connected sources, not seats. → [[context-layer-market]]

**○ Everyone has MCP - so what distinguishes the solutions?**
Having MCP has stopped being a differentiator. The differences moved into the architecture of context storage, entitlement inheritance and total cost of ownership. And no standard covers two things: **portability of entitlements** (row-level security from one catalog does not apply when reading through another - which is why people pick ONE catalog as the governance boundary) and **the provenance of an answer** (the chain "prompt -> retrieved chunks -> answer"). → [[context-layer-market]]

**○ How do we measure the quality of agent infrastructure while there are no accuracy metrics?**
By the MCP server's error rate. It is measurable, controllable and does not require judging "answer quality". A useful detail: collect the statistics separately per tool and per error cause - then you can see that half of what remains is timeouts, and that they are cured architecturally (return a task number instead of waiting) rather than by improving prompts. → [[unified-bi-platform]]

**○ Are a glossary and a data dictionary the same thing?**
No, and trying to keep them in one place usually breaks both. A glossary is business terms and definitions. A data dictionary is metadata about objects: types, sizes, constraints, relations, a column's purpose, whether it is PII. The delivery mechanic that works: the master glossary in the governance platform, terms highlighted right inside the wiki text, and a ticket to the steward raised from the highlight. The term reaches the user **at the moment of reading**. → [[glossary-vs-dictionary]]

**○ We need a metric tree. Where do we start?**
By accepting that a properly hierarchical tree is not going to happen. Metrics are connected as a network, not a tree; attempting a strict hierarchy ends either in a stretch or in the work stalling. What is worth building is relations and levels. → [[glossary-vs-dictionary]]

**○ How do we assess promising directions around BI rather than only the tool itself?**
With the sheet of 16 directions, cut across "value/applicability · consumers · technical solution · owner · cost". The list was drawn up before the agentic wave, but its first two entries - GPT-based UX and insight generation - are exactly where the market moved. A practical move: fill in the sheet as it stands, then **separately check the ordering** - whether an AI entry sits above its own link in the chain. → [[bi-toolset-landscape]]

**○ Which stage of AI adoption are we at and what comes next?**
Four observable waves: enthusiasm with local agents and spontaneous MCP servers (1-2 months) -> ordering: a gateway, an agreement with security, a skill hub (2-4 months) -> platformization: an MCP hub, JTBD registries, a domain knowledge base, champions (4-6 months) -> productization: agents inside the BI products, text-to-semantic, a semantic layer. You cannot skip a wave; you can get stuck in one. → [[ai-adoption-waves]]

---

## 9. The team, the roles, the profession

**◇ Do you have a BI community?**
The test is not whether a chat exists but whether you land in people's motives. Why anyone would want self-service: to get a report on time and fix it quickly · **to raise their standing in the team and with management** · to master a tool and grow their market value · for fun · to change the kind of work they do · to socialize · their manager made them. That last motive is named honestly - that part of the audience is not worth trying to retain. → [[bi-community-management]]

**○ We want a champions programme. What is needed before the launch?**
Four preconditions: a strategic plan for the community already exists (the programme does not replace onboarding), a dedicated programme lead for the whole cycle, an established communication platform, an executive sponsor. And a mandatory symmetry: next to the company's goals there has to be a column of **the champion's benefits** - networking, influence on change, access to roadmaps, public recognition. Without the second column the programme does not live. → [[bi-community-management]]

**○ Champions burn out and the programme fades. Is that curable?**
Organizationally, no. The method names two problems directly: keeping the temperature up (it needs people with conviction and internal drive) and capacity. Both come down to specific people. What helps is separating three mechanisms: belts are about competence, badges about engagement, awards about recognition. Mixing them devalues all three. → [[bi-community-management]]

**◆ Developers on the same grade have wildly different skill sets. How do we level them?**
With a matrix where the grade is determined not by breadth but by **the number of L3 competencies**: the L1/L2 minimums for middle, senior and lead barely differ. That stops people "growing" on breadth and requires genuine depth in at least one place. Three assessment parts on different rhythms: soft skills every six months, hard skills once per level, the BI project annually. → [[bi-competency-matrix]]

**◆ Some people are stuck at junior and have not grown for years. What do we do?**
Look at how promotion is constructed: you cannot skip a grade, and **you perform at the new level first** and receive it afterwards. If somebody goes years without assembling either the soft skills of the next level or a BI project at that level, that is not a motivation problem but the absence of a decision. What helps is that the matrix has an explicit annual artifact (the project) that shows movement or its absence. → [[bi-competency-matrix]]

**○ How do we build the LLM into the competency matrix?**
Not as a separate skill but **inside every level of every competency**. L1 - I understand generated code and can explain it line by line. L2 - I can justify the model's proposed solution or replace it. L3 - I validate and review the model's output and embed it into the system. The criterion is phrased as "the ability to get the right result with any tool". → [[bi-competency-matrix]]

**○ We rewrote the matrix for AI but hiring stayed the same. How do we fix it?**
With five principles. Grade discovery - the grade comes from the ceiling at which the candidate starts to flounder, not from the CV. A 1:1 tie to the matrix - no blocks "for a general impression". Hard skills through artifacts made in the moment, soft skills through observation in a case. **The LLM is allowed on the technical tasks**, and the stop signals are symmetrical: refusing the LLM and trusting its output blindly are equally bad. The recommendation is min(hard, soft). → [[bi-hiring-ai-era]]

**○ What matters more at the door - SQL or motivation?**
The course's phrasing: engagement, intrinsic motivation, a willingness to do business analysis of data and to produce design that is not embarrassing are slightly more important than technical skills. A BI product can be learned; SQL can be built up. The SQL skill profile has shifted too: what dominates is reading other people's code, debugging, reviewing the model's output and defending a decision in conversation. → [[bi-hiring-ai-era]]

**◇ Retain seniors, train juniors or take on interns?**
The question got sharper because factory teams have been compressed to two or three people. The risk if left alone: the entry route into the profession disappears, in three to five years there is nobody to grow into senior, and an agent operator is on intellectual load all day with no pauses. What to do instead of cutting: move juniors into domain curator roles, grow them **through reviewing AI outputs**, deliberately keep some routine as ballast, retrain them on semantics and agent development. → [[bi-hiring-ai-era]]

**○ How do we avoid a domain that rests on one person?**
A backup strategy: at least three experts on critical domains and at least two on the rest, plus regular recording of knowledge-sharing sessions. At the M2 team lead level, a successor in the team is mandatory. → [[bi-competency-matrix]]

**◇ What are the values of a centralized BI team?**
The author's version: we are a premium service and the company pays serious money for it · ours is the best project in the country, **but that has to be borne out by real traffic and the level of automation** · we are the best BI people in the company and everyone has to live up to that. The second statement has a defence against self-deception built in - the claim is obliged to be backed by a measurement. → [[centralized-bi-brand]]

**◆ BI in a non-revenue unit: the effect on the business cannot be computed. What do we do?**
Through a service catalog with SLAs and through metrics that do not require revenue: the share of meetings where BI reports are used, the volume and cost of manual operations automated, the share of analytical tasks still solved by hand, coverage of information demand by role and domain. Plus the positioning: a premium service **cannot be available to everyone**, and a queue is part of the design rather than a defect. → [[bi-project-metrics]], [[centralized-bi-brand]]

**○ Which meetings are genuinely needed, and which can we skip?**
Three external (an executive committee monthly or quarterly, a working committee fortnightly, a BI-to-warehouse sync fortnightly) and four internal. The key observation: **exactly one format on the list holds governance up** - the monthly BI governance status. If it is not held, governance lives only in the text of the strategy. → [[regular-meetings]]

**○ Why is a newcomer's onboarding plan in the strategy?**
Because how fast a new analyst becomes productive is a direct multiplier on everything planned. And because it is the most honest audit of your own standards: if there is nothing to put on the self-learning track, the documents on your standards list do not exist. The format is deliberately concrete - three weeks day by day, four tracks: access and software, self-learning, meetings, tasks. → [[onboarding-plan]], [[rules-and-standards]]

---

## 10. Efficiency and metrics

**○ How many metrics do we take?**
Five primary and five secondary, and no more - the selection rule is hard and deliberate. Four groups: engagement, quality of service, process quality, business impact. If what you need is not in the catalog, write your own. → [[bi-project-metrics]]

**○ We saved analysts hours with AI. Is that the effect?**
No, that is a trap metric. A person's time saved does not equal a gain for the company: for most people the freed time dissolves into small things. The gain appears only with an explicit reallocation of the resource. The practical requirement: every AI initiative has to name **the decision about where the freed time goes, and who makes it**. → [[ai-time-saving-trap]]

**○ How do we measure AI's effect honestly at all?**
With three techniques from the cases walked through: a baseline-versus-after measurement on UAT (without "how long this used to take", any percentage saving is meaningless), a separate LLM judge for explanation quality, and a golden dataset for metric-resolution accuracy. Plus a ban confirmed by controlled measurement: **do not measure the effect by the team's self-assessment** - developers turned out to be 19% slower while convinced they had become 20% faster. → [[ai-cases-in-prod]], [[ai-in-data-processes]]

**○ Is a rise in agent calls a success?**
No. The rule from the loyalty programme: **a rise in call volume with no rise in successful tasks does not count as a result**. The next level of assessment is the share of successfully completed AI jobs-to-be-done and the number of task-hours AI successfully covers. → [[ai-accelerator]]

**○ Which metrics do we put on top as the platform's annual shop window?**
The composition matters more than the values: two metrics about redistributing labour (the share of tasks solved without an analyst, the share of analysts' time spent on investigation), one about AI adoption, one about the speed of creating an artifact, one about satisfaction. None is measured by self-assessment. → [[unified-bi-platform]]

**○ What do we check regularly so things do not drift?**
The routine calendar: daily - the extracts, the subscriptions, your own subscription to the key reports (the refresh date is today), the service-desk board; fortnightly - whether every report is assigned to a domain and a role, and splitting large tasks; quarterly - extract duration against the threshold, report performance, **adoption against the target share of the focus audience**. → [[bi-routine-calendar]]

---

## 11. The action plan and rollout

**○ What makes an initiative in a plan different from a line in a plan?**
An owner, a metric and a kill-gate. The method requires an area, an initiative and dates; on top of that the skill requires a named owner, a way of measuring and a stopping condition for every initiative. **An initiative with no owner is a line in a plan, not a change.** → [[action-plan]]

**○ How do we set target maturity without drawing fours across the board?**
Levels 3-4 in every category is not a goal but a symptom of an unread diagnostic. The honest default is **plus one level a year**; a bigger shift requires a named reason: dedicated capacity, an already funded platform change, a regulatory deadline. For each category, name the ceiling and mark where "enough" sits. → `review-gates.md`

**○ What goes into the "what the strategy does not do" section?**
Which capabilities stay as they are and which initiatives are deliberately absent in this horizon - with the reason. A deliberately excluded stream with a gate that will open it later is a stronger artifact than a stream included "because it is a trend". It is also the honest answer to "so where is our AI".→ `review-gates.md`, [[innovation-map]]

**○ How do we check the strategy will not fall apart on the first question?**
Run it through the judge stage across seven dimensions: priority, order, feasibility, complexity, concreteness, defensibility, honesty about risk. The output is 5-8 findings with a severity and an exact quotation, plus a verdict line of "I would / would not sign, because". A pass with no visible change to the draft means the judge was polite rather than useful. → `review-gates.md`

**○ How do we drive AI adoption without herding people onto courses?**
With a format between a hackathon and a course: several weeks to work things through alongside the day job, mentors, pitches, assessment by three parties. The main lesson learned is that **completion to production is far higher where support existed**, technical and methodological. And the next focus shifts from generating new ideas to polishing a limited set of mass scenarios. → [[ai-accelerator]]

**○ How do we close a conversation about AI with the business when the foundation is not there yet?**
With the dependency chain and one kill-gate. `core -> semantic -> context -> AI accuracy -> self-service`; there is no AI assistant without semantic coverage of the target domains and a certified core. Plus the argument from the evidence: text-to-SQL on real enterprise schemas is around 40%, and 85-95% with a semantic layer - **and the difference comes from knowledge, not from the model**. → [[ai-triad-prerequisites]], [[semantic-layer-evidence]]

**○ How do we write a vision that is not just words?**
The method's template deliberately leaves blanks where numbers go: how many users we serve, what share of headcount that is, by what percentage and by what date we grow. **The blanks are filled with measured numbers or left marked "data missing" until they are measured.** An inspiring number dropped in to plug a hole will outlive the strategy and be quoted for a year. The shape of a goal has four mandatory fields: description, KPIs, outcomes, timing. → [[vision-statement]]

---

## What is not in this base

Transcripts of the live sessions are not available in the current perimeter, so the "real" questions were reconstructed from written sources: the pre-course survey, the Day 1 interactive and the questions the author put on slides. The wordings are reconstructions of the sense rather than verbatim participant quotes.

If access to the transcripts appears, the base is worth rebuilding: live questions have a different structure - they are more often about "but our case is a special one", and those special cases are the most valuable material for the next version.
