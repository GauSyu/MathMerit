# MathMerit

[中文](README.zh.md)

## Why this skill

**Let heroes assess heroes; let the brave assess the brave.**

As AI4Math develops rapidly and papers multiply, which deserve a mathematician's reading time? MathMerit is an AI skill for helping human mathematicians select works worth reading.

## The report

The reading-selection report gives a recommendation with reasons for and against reading, supported by provisional five-dimensional grades, specific evidence, and an AI reading-selection diagram. It identifies the limits of the inferences, the model used, and this repository. Its grades must not be used as judgments of mathematical quality. See the [report rules](references/profile-format.md).

## Basis and scope

[Copernicus](https://github.com/GauSyu/Copernicus) is an independent, human-facing proposal for evaluating mathematical contributions. MathMerit draws on its five dimensions and grade criteria; the two projects maintain different purposes, reports, and diagram templates. MathMerit's diagram displays AI inferences for reading selection, not a Copernicus contribution assessment.

A fixed copy of the proposal is bundled in [English](references/copernicus/Copernicus.en.md) and [Chinese](references/copernicus/Copernicus.zh.md), with its source commit and file hashes in [source.json](references/copernicus/source.json). These are imported reference copies, not a second place to edit the proposal. Update the proposal in Copernicus, then deliberately refresh and check the skill's dependency. Reading recommendations remain specific to MathMerit.

## Use

Install this directory as `mathmerit` using your assistant's local skill installation mechanism. The skill is self-contained: English use needs no Chinese reading, separate checkout, or network fetch of Copernicus. Reports follow the requested language, or the request's language; bilingual output is available on request.

Example: “Use $mathmerit to help me decide whether this paper is worth reading; write the reading-selection report in English.”
