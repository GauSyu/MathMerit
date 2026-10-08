# MathMerit

[中文](README.zh.md)

## Why this skill

**Let heroes assess heroes; let the brave assess the brave.**

As AI4Math develops rapidly and papers multiply, which deserve a mathematician's reading time?

## Purpose

MathMerit is an AI skill that helps mathematicians select works worth reading. It uses the five dimensions and grade criteria of [Copernicus](https://github.com/GauSyu/Copernicus) to analyze mathematical contributions, and weighs reading benefits against the required effort to make recommendations. The report's grades and diagram are AI inferences for reading selection only, not assessments of mathematical quality.

## Report contents

The report first presents provisional five-dimensional grades, specific evidence, and an AI reading-selection diagram, then weighs reading benefits and effort, gives reasons for and against reading, and concludes with a recommendation. It identifies the limits of the inferences, the model used, and this repository. Its grades must not be used as judgments of mathematical quality. See the [report rules](references/profile-format.md).

## Use

Install this directory as `mathmerit` using your assistant's local skill installation mechanism. Assessments require network access to retrieve the current Copernicus criteria; English use needs only the English edition, with no separate checkout. Reports follow the requested language, or the request's language; bilingual output is available on request.

Example: “Use $mathmerit to help me decide whether this paper is worth reading; write the report in English.”
