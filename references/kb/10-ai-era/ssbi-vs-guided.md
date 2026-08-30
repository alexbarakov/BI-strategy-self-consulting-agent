---
id: ssbi-vs-guided
title: The two meanings of self-service BI, and why the term guided BI is needed
type: pattern
source: "Course \"BI+AI strategy 26\", Day 3"
confidence: author estimate
blocks: [3, 4.3]
---

The method's key terminological fork: **two different scenarios live inside people's heads under "self-service BI"**, and conflating them is the source of most failures.

## Case 1 - teach casual users to build reports themselves

The team tries to teach business professionals to drag data into BI using templates and certified sources instead of exporting to Excel and drawing charts in PowerPoint.

- This is often **self-deception, egged on by vendors** to grow sales
- Uptake of the "explorer" scenario is close to zero and rarely justifies itself
- Pushing NLP inside BI tools as the main hope also turned out badly
- LLM-based solutions remove some of the UX constraints on natural-language querying; there is a substantial breakthrough in acceptance of the concept, but solving the basic problems of data assistant chatbots - **trust, data quality, security** - will take years

The scenario matters for adoption, but **it is not self-service. The proposed term is guided BI**: maximizing the usefulness of ready reports and sources.

## Case 2 - give power users inside the business teams the tools

The team gives analysts inside business teams access to tools so they can build reports for their own department.

- This is **actual self-service BI**: a federated model with distributed analysts on shared infrastructure
- They are joined into a BI community and follow the content management practices controlled by the BI team
- The constraints: content quality and the absence of a single version of the truth
- **It proves its worth in large enterprises** (hello, data mesh)

## Two patterns in how BI leaders position themselves

- **A dominant centralized report factory (the classic):** "We build reports on request, we have a large backlog, self-service is a secondary concern, we do something about it but there is no response from the business at scale."
- **Dominant self-service BI:** "We rolled out SSBI, recorded a course, hand out entitlements, keep the server updated, consult, monitor traffic - people use it, everything is fine."

Both produce **insufficient penetration of BI into the business**, for different reasons.

| What centralized lacks | What self-service lacks |
|---|---|
| low subject-matter expertise · the barrier between requester and developer · a bottleneck and a fight over priorities · shadow BI · self-service flare-ups that fade | low cross-functional usage · the truth multiplies · content chaos · poor reports added on top of poor data · security risks · "we have no time, it is hard, we have forgotten how again" |

## The method's conclusion

**Self-service will not replace centralized analytics, and without self-service, centralized will not reach a single version of the truth.** They should not be set against each other, but the synergy takes effort: at some point the cost of pushing any one metric further becomes prohibitive, and getting the most out of it means combining drivers and finding empirically the point where further investment stops making sense.

Links: [[ssbi-failure-causes]] · [[ssbi-workflow]] · [[user-classification]] · [[selfservice-practices]] · [[centralized-practices]]
