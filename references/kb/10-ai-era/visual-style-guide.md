---
id: visual-style-guide
title: The visual style guide - a three-layer structure and how it takes root
type: method
source: "Course \"BI+AI strategy 26\", the \"Content management\" session"
confidence: verifiable
blocks: [4.2, 6]
---

## Framing the question

Why do we need pixel-perfect reporting and a fight over shade combinations, padding pixels and the appropriateness of chart types? Can a developer with no aptitude be taught high-class design - **probably not**. Hence the question: is a designer in the BI team overkill or salvation? In such a setup their main duties are **design audit, coaching, design polishing and live design**.

## The three layers of a style guide - each with its own audience and implementation

| Layer | Content | Purpose | Where it lives |
|---|---|---|---|
| **1. The BI report template** | a preformatted set of starting compositions with padding, fonts and navigation elements already set | the author uses it as a starting point -> time saved, universal parameters standardized | in the BI tool |
| **2. The visual vocabulary** | 10-15 core visualization types with target implementations, hints and know-how | "take it apart and build one like it" -> training authors, standardizing how charts look | in the BI tool |
| **3. The corporate visualization textbook** | hundreds of pages: colour, perception patterns, dashboard composition, sketching, checklists | give knowledge to those who want it -> deep training for BI champions | **not in the BI tool** - Miro, a deck |

The separation matters: mixing the layers is the standard reason a style guide goes unused. The template has to be two clicks from development; the textbook does not.

## The goals of a design guide

Build more genuinely good reports - comprehensible to the user and pleasing to the manager's eye · unify the visual code and raise clarity and intuitiveness · raise the visualization culture and **the intolerance of visual slop** · make working with BI reports more enjoyable.

## How it takes root - rollout practice

1. Develop it jointly with the warehouse/BI team, hand it to colleagues to grow and maintain
2. Run training for the analysts
3. Use it for every report the centralized team builds
4. **Redesign into the template as a service** - run consultations, help people redesign
5. A series of masterclasses to keep it developing

The course's short formula: "redesign into the template as a service · training, training, training".

## The dashboard-building algorithm

1. Define the goals and the audience -> 2. Sketch it -> 3. Build it -> 4. Make it interactive -> 5. Add instructions and hints -> 6. **Remove everything superfluous** -> 7. Apply the best visual techniques to the final version.

The questions for step 1: why are you creating this dashboard · who is the audience (an executive, operational management or analysts) · do entitlements need to be separated inside the dashboard.

## Three types of dashboard

| Type | Characteristics |
|---|---|
| **Strategic** | a fast overview of the state, focused on high-level indicators, simple |
| **Operational** | monitoring processes and metrics across cuts, comparisons and trends; more information, longer to take in; clear, well-worn scenarios; a broader audience |
| **Analytical** | needs additional context, non-obvious scenarios, harder to take in, deeper in capability, highly interactive, many filters |

## The rules stated explicitly

**Padding:** external - at least 12px at the bottom and the sides, none needed at the top; between semantic containers - at least 10px; the filter area reads as a separate container.

**Colour:** the visualization background is always white · "grey is the most important colour in data visualization" · if a chart needs more than seven colours, change the chart type or group the categories · light colours for small values, dark for large · one colour per identical variable, shades for subtypes · with a red-amber-green palette, make sure green and red mean good and bad respectively · bright accent colours only for the data that needs to stand out.

Links: [[content-mgmt-processes]] · [[rules-and-standards]] · [[content-hygiene-loop]] · [[centralized-practices]]
