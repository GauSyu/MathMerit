# MathMerit

[中文](README.zh-CN.md)

## Why this project

**Let heroes assess heroes; let the brave assess the brave.**

As AI4Math develops rapidly and papers multiply, which deserve a mathematician's reading time? This project develops and advocates a method for evaluating mathematical contributions from first principles, with an automated skill to help mathematicians find papers worth reading.

## First principle

> **Mathematical contributions serve the mathematical community's knowledge and understanding of mathematical objects, structures, and questions.**

## The method

[Copernicus](Copernicus.en.md) presents the method for the mathematical community to use, discuss, and revise: guiding principles, five dimensions, named grades, and a five-axis diagram. Grades and diagrams belong to the method itself, supporting human assessment as well as AI-assisted implementation. A [Chinese edition](Copernicus.md) is also available.

| Dimension | Guiding question |
|---|---|
| Knowledge | What is established, and which grounds are strengthened? |
| Understanding | Which questions are clarified, and which relationships or mechanisms are revealed? |
| Methods | Which tasks become feasible, and which costs fall? |
| Exposition | Which obstacles to understanding, checking, and use are removed? |
| Significance | Why do these improvements matter? |

The five-axis diagram displays distinct contributions through named grades. Grades are not added, and area does not measure overall value. Contributions need evidence, significance calls for human judgment, and lasting influence is tested by history.

## The skill

[MathMerit](SKILL.md) automates the method. Provide a mathematical text and version to an AI assistant to obtain a reasoned assessment, a filled diagram, and reading advice under the [operating rules](references/profile-format.md).

Install this directory as `mathmerit` using your assistant's local skill installation mechanism. The English method, instructions, and diagram template support English use without consulting the Chinese edition; no separate language package is needed. Output follows your requested language, or the language of your request. Bilingual output is available on request.

Example: “Use $mathmerit to assess this paper in English.”
