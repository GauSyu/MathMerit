---
name: mathmerit
description: "Help mathematicians select mathematical works or interdependent series worth reading, using Copernicus to produce a provisional five-axis report and a reasoned reading recommendation."
---

# MathMerit

Help human mathematicians decide whether a work merits their reading time. Copernicus is a proposal for human evaluation; this skill uses it only for AI-assisted reading selection. Open each report with the short scope line specified in the format reference. Copernicus governs the grade criteria; reading selection governs their presentation and the recommendation, not different promotion thresholds.

Read the bundled [English criterion snapshot](references/copernicus/Copernicus.en.md) or its [Chinese edition](references/copernicus/Copernicus.zh.md), as needed for the report's language. [Copernicus](https://github.com/GauSyu/Copernicus) is the independently maintained proposal; [source.json](references/copernicus/source.json) identifies the imported commit and file hashes. Use this pinned copy consistently for a report, rather than silently substituting the latest upstream text. Its dimensions and grade criteria inform the AI inferences; MathMerit owns the reading-selection rules and its distinct diagram. Use [profile-format.md](references/profile-format.md) for execution and reporting, and MathMerit's [profile-grid.svg](assets/profile-grid.svg) for drawing. Obtain missing criteria before grading; do not substitute remembered or superseded scales.

Use the language requested by the user; otherwise follow the request’s language, defaulting to English when unspecified. Produce bilingual output only when requested. Apply this choice to the report, status, and all diagram text.

## Assess the contribution

Assess **Contribution at the time**, whether the work is recent or historical. Reconstruct the community's context at each assessed item's appearance. Any separately requested assessment of **Subsequent influence** stays outside the five grades.

**Assess the whole contribution.** Establish the unit before grading. When companion works jointly supply the definitions, arguments, methods, or exposition needed for a contribution, assess the bounded series together. Identify the included works and versions; shared authorship or topic alone does not make a series. Give one set of five grades and one diagram for the whole, explaining each part’s role without adding, averaging, or taking the maximum of per-paper grades. Follow the scope rules in the format reference.

**Compare with its own time.** Begin with the broad research context and substantive precedents. Investigate precise chronology only when it could materially change the assessment, especially amid dense bursts of related AI-generated work. Public timestamps alone establish neither discovery order nor dependence; preserve uncertain precedence without withholding supported judgments. Follow the comparison procedure in the format reference.

**Distinguish the gains.** Assess Knowledge, Understanding, Methods, and Exposition under their respective criteria. Distinguish gains in conclusions or grounds, concepts or relationships, operational capability, and access to understanding, checking, or use. The same material may support several dimensions, but each needs its own gain. Solving a problem does not by itself establish a Methods advance; identify the change in method and resulting capability separately from the new result. Do not infer contribution from the work's genre, authorship, or terminology. Actual uptake is not required.

**Attribute only the added contribution.** Separate inherited results, tools, routes, and connections from what this work establishes, adapts, or invents. A problem’s importance, successful execution, arduous search, or elaborate verification does not by itself justify a high grade or a claim of originality. Ground any claimed significance in the specific change this work makes; keep anticipated effects separate.

**Judge expression for human readers.** Assess how emphasis, organization, and appropriate detail guide the intended readers’ thought. Ground the judgment in passages and materials, not explanations you supply yourself. Neither exhaustive detail nor little need for reconstruction establishes good exposition; apply the reader-based checks in the format reference.

**Grade the gain; explain the grounds.** For every move to a higher named grade, identify the dimension-specific gain, its evidence, and why the lower grade understates it under Copernicus. Strong adjectives or success in another dimension do not supply that basis. Low grades across all five dimensions are a normal, complete outcome; do not raise any grade to balance the profile, justify a recommendation, or reward effort. Give reasoned provisional judgments without requiring complete correctness certification. Name key dependencies for conditional judgments; an identified error or missing argument restricts dependent claims, while surviving gains remain assessable. If grounds are insufficient for any dimension, withhold the entire assessment: report only the missing grounds, with no grades, evaluative reading advice, or diagram. Provisional or conditional wording cannot substitute for missing grounds. Incomplete correctness checking alone does not trigger this stop. A finding of no improvement concerns only the specified dimension. Assess independent corroboration under Knowledge when it strengthens grounds; retain material gains and costs not captured by the grades.

**Expose the limits of AI judgment.** Present AI-assigned grades as provisional inferences. Identify the specific inference AI cannot reliably settle and apply the reference’s warning there; neither a dimension name nor confidence of tone establishes reliability. Labels do not excuse missing grounds or lower the contribution grade.

**Give reasons for significance.** Assess Significance separately from the four contribution grades. Use a clear attributed human judgment when supplied; preserve its scope and reasons. Otherwise supply an AI provisional judgment under the same criteria. Do not convert that judgment into community endorsement.

**Label the whole assessment.** After the opening purpose notice, include **Assessment status: Not evaluated by the mathematical community** unless community evaluation of this assessment is documented, using the report’s language (see the format reference for the required wording). Keep status, attribution, and checking notes outside the image. One person's opinion is not community evaluation.

## Present the judgment

**Show the profile; preserve the reasons.** Once all five dimensions have supported grades, deliver a concise reading-selection report led by the recommendation and its benefits and costs. Use the five-dimensional analysis and SVG to explain the judgment, in the selected language or languages. From the top clockwise: **Significance, Knowledge, Understanding, Methods, Exposition**. Take grade names from the corresponding language edition of Copernicus; English labels stand on their own rather than translating the Chinese labels afresh. Derive the report’s grade labels, diagram labels, and marker positions from one final grade record. Do not reassess or raise grades while drawing. Check agreement with the supporting reasoning before delivery. Never add grades, measure area, or infer an overall ranking.

**Recommend for human readers.** Give reasons for and against reading, then select exactly one of the four recommendation levels in the reference. Weigh concrete mathematical benefits against prerequisites, exposition, and the effort required to locate and check the contribution. Neither diagram size nor an unreliable high grade decides the recommendation. Provide reading entry points only where warranted by that recommendation. Sign the report with the actual model identity and cite the MathMerit repository. Keep future expectations distinct from realized contributions; leave long-term influence to history.

Save in the task's authorized location, link the report, display the grid, and preserve source originals.
