# MathMerit

[中文](README.zh.md)

## Why this project

**Let heroes assess heroes; let the brave assess the brave.**

As AI4Math develops rapidly and papers multiply, which deserve a mathematician's reading time? This repository hosts two distinct contributions:

- **Copernicus — a proposal for the mathematical community.** Explore and advocate a method for evaluating mathematical contributions from first principles.
- **MathMerit — an AI reading-selection skill.** Help mathematicians select works worth reading, drawing on Copernicus while making the limits of AI judgment explicit.

Copernicus stands on its own for human use; MathMerit uses its criteria. They are maintained together so the skill follows the method, while their purposes and deliverables remain distinct.

## First principle

> **Mathematical contributions serve the mathematical community's knowledge and understanding of mathematical objects, structures, and questions.**

## Copernicus: the proposal

[Copernicus](Copernicus.en.md) presents the method for the mathematical community to use, discuss, and revise: guiding principles, five dimensions, named grades, and a five-axis diagram. Grades and diagrams belong to the method itself, supporting human assessment as well as AI-assisted implementation. A [Chinese edition](Copernicus.zh.md) is also available.

| Dimension | Guiding question |
|---|---|
| Knowledge | What is established, and which grounds are strengthened? |
| Understanding | Which questions are clarified, and which relationships or mechanisms are revealed? |
| Methods | Which tasks become feasible, and which costs fall? |
| Exposition | Which obstacles to understanding, checking, and use are removed? |
| Significance | Why do these improvements matter? |

The five-axis diagram displays distinct contributions through named grades. Grades are not added, and area does not measure overall value. Contributions need evidence, significance calls for human judgment, and lasting influence is tested by history.

## MathMerit: the AI skill

[MathMerit](SKILL.md) produces a reading-selection report for human mathematicians: provisional five-dimensional grades and reasons, a five-axis diagram, explicit limits of AI judgment, reasons for and against reading, and one overall reading recommendation. The report identifies the model used and cites this repository. Its purpose is to help readers decide where to spend attention; it does not certify mathematical merit. See the [report and recommendation rules](references/profile-format.md).

Install this directory as `mathmerit` using your assistant's local skill installation mechanism. The English method, instructions, and diagram template support English use without consulting the Chinese edition; no separate language package is needed. Output follows your requested language, or the language of your request. Bilingual output is available on request.

Example: “Use $mathmerit to assess this paper in English.”
