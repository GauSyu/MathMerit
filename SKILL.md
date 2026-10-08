---
name: mathmerit
description: "Help mathematicians select mathematical works or interdependent series worth reading, applying its built-in implementation of Copernicus to contribution analysis and evidence-based reading recommendations."
---

# MathMerit

MathMerit implements Copernicus as a self-contained skill to help human mathematicians decide whether a work merits their reading time. Apply its built-in contribution criteria, then weigh reading benefits and costs. The reading-selection purpose does not change contribution-grade thresholds. Reports are AI inferences, not assessments of mathematical quality or substitutes for expert judgment.

## Apply the built-in rules

Read [profile-format.md](references/profile-format.md) before assessing. It contains the principles, complete bilingual criteria for all five contribution dimensions, execution guidance, reading levels, report format, and drawing requirements. These bundled rules govern the assessment; no retrieval of Copernicus is required. Literature searches may still be needed to establish the work's contribution. For an eligible diagram, use the separate [MathProfile skill](skills/mathprofile/SKILL.md) and its bundled renderer; pass the finalized grades without re-assessment.

Use the requested language, otherwise the request's language, defaulting to English when unspecified. Produce bilingual output only on request. Apply the choice to the report, status labels, and diagram; use the grade names in the built-in tables.

## Assess and report

1. **Define the work.** Establish versions and the bounded unit, including interdependent series, under [Unit of assessment](references/profile-format.md#unit-of-assessment).
2. **Compare with its own time.** Assess contribution at the time using [Historical comparison](references/profile-format.md#historical-comparison); keep later influence separate. Broad context comes first; timestamps alone do not establish discovery order.
3. **Check the grounds.** Use [Evidence gaps and output decisions](references/profile-format.md#evidence-gaps-and-output-decisions) throughout the assessment. Distinguish checking status, evidence gaps, and unreliable inferences; determine separately which grades, advice, and diagram the evidence supports.
4. **Grade actual gains.** Apply [Grades and judgment provenance](references/profile-format.md#grades-and-judgment-provenance): common rules first, then dimension-specific checks. Attribute gains to the work, support every promotion, distinguish result advances from method advances, and judge exposition for human readers. Supported low grades across all dimensions are normal.
5. **Weigh the reading value.** Apply [Reading recommendation](references/profile-format.md#reading-recommendation). Unknown benefits cannot justify advice; documented defects must enter the balance. Do not adjust contribution grades to fit the recommendation.
6. **Compose, check, and deliver.** Follow [Report](references/profile-format.md#report) for the requested output format and template (Markdown by default), presentation order, scope and status labels, and the MathMerit source link. Use [Five-axis grid](references/profile-format.md#five-axis-grid) for eligible diagrams and consistency checks. Save in the task's authorized location, link the report, display the diagram when eligible, and preserve source originals.
