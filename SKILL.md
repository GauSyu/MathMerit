---
name: mathmerit
description: "Help mathematicians select mathematical works or interdependent series worth reading, using Copernicus for supported contribution grades and evidence-based reading recommendations."
---

# MathMerit

Help human mathematicians decide whether a work merits their reading time. Use Copernicus for contribution grades and MathMerit's reading criteria for recommendations. The reading-selection purpose does not change contribution-grade thresholds. Reports are AI inferences, not assessments of mathematical quality or substitutes for expert judgment.

## Load the criteria

At each assessment's start, resolve the current `main` commit of [Copernicus](https://github.com/GauSyu/Copernicus) through `GET https://api.github.com/repos/GauSyu/Copernicus/commits/main` (field `sha`). Read `https://raw.githubusercontent.com/GauSyu/Copernicus/<sha>/Copernicus.en.md` or `Copernicus.zh.md` for the report's language; bilingual reports use both at the same commit. Record that SHA and commit-specific links and use that version throughout. Keep no proposal copies in this repository; never substitute stale text or memory. Upstream dimensions and grade criteria govern any grade-specific guidance here. A retrieval failure or incompatible change blocks affected grading or drawing, not independently supported reading advice; disclose the limitation.

Read [profile-format.md](references/profile-format.md) before assessing. It contains the execution rules, reading levels, report format, and drawing requirements; use it throughout. Use [profile-grid.svg](assets/profile-grid.svg) when the report qualifies for a diagram.

Use the requested language, otherwise the request's language, defaulting to English when unspecified. Produce bilingual output only on request. Apply the choice to the report, status labels, and diagram; take grade names from the corresponding Copernicus edition.

## Assess and report

1. **Define the work.** Establish versions and the bounded unit, including interdependent series, under [Unit of assessment](references/profile-format.md#unit-of-assessment).
2. **Compare with its own time.** Assess contribution at the time using [Historical comparison](references/profile-format.md#historical-comparison); keep later influence separate. Broad context comes first; timestamps alone do not establish discovery order.
3. **Check the grounds.** Use [Evidence gaps and output decisions](references/profile-format.md#evidence-gaps-and-output-decisions) throughout the assessment. Distinguish checking status, evidence gaps, and unreliable inferences; determine separately which grades, advice, and diagram the evidence supports.
4. **Grade actual gains.** Apply [Grades and judgment provenance](references/profile-format.md#grades-and-judgment-provenance): common rules first, then dimension-specific checks. Attribute gains to the work, support every promotion, distinguish result advances from method advances, and judge exposition for human readers. Supported low grades across all dimensions are normal.
5. **Weigh the reading value.** Apply [Reading recommendation](references/profile-format.md#reading-recommendation). Unknown benefits cannot justify advice; documented defects must enter the balance. Do not adjust contribution grades to fit the recommendation.
6. **Compose, check, and deliver.** Follow [Report](references/profile-format.md#report) for presentation order, scope and status labels, and the model signature with repository link. Use [Five-axis grid](references/profile-format.md#five-axis-grid) for eligible diagrams and consistency checks. Save in the task's authorized location, link the report, display the diagram when eligible, and preserve source originals.
