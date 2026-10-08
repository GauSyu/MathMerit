# MathMerit

[中文](README.zh.md)

## Why this skill

**Let heroes assess heroes; let the brave assess the brave.**

As AI4Math develops rapidly and papers multiply, which deserve a mathematician's reading time? MathMerit is an AI skill for helping human mathematicians select works worth reading.

## The report

The reading-selection report gives a recommendation with reasons for and against reading, supported by provisional five-dimensional grades, specific evidence, and an AI reading-selection diagram. It identifies the limits of the inferences, the model used, and this repository. Its grades must not be used as judgments of mathematical quality. See the [report rules](references/profile-format.md).

## Basis and scope

[Copernicus](https://github.com/GauSyu/Copernicus) is an independent, human-facing proposal for evaluating mathematical contributions. MathMerit draws on its five dimensions and grade criteria; the two projects maintain different purposes, reports, and diagram templates. MathMerit's diagram displays AI inferences for reading selection, not a Copernicus contribution assessment.

Each assessment retrieves the latest [English](https://github.com/GauSyu/Copernicus/blob/main/Copernicus.en.md) or [Chinese](https://github.com/GauSyu/Copernicus/blob/main/Copernicus.zh.md) proposal from Copernicus and records the exact commit used. MathMerit keeps no copy of the proposal. Reading recommendations remain specific to MathMerit.

## Use

Install this directory as `mathmerit` using your assistant's local skill installation mechanism. Assessments require network access to retrieve the current Copernicus criteria; English use needs only the English edition, with no separate checkout. Reports follow the requested language, or the request's language; bilingual output is available on request.

Example: “Use $mathmerit to help me decide whether this paper is worth reading; write the reading-selection report in English.”
