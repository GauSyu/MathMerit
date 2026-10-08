---
name: mathprofile
description: Draw a five-axis mathematical contribution profile from grades already supplied by a person or an assessment. Use for drawing only, without assessing a work or choosing its grades.
---

# MathProfile

Turn five supplied contribution grades into a diagram. The grades belong to the supplied assessment; drawing them neither verifies nor endorses them. Accept a person's choices directly without requiring an AI assessment or a MathMerit report.

## Input

Obtain the work's title, one grade for each of Significance, Knowledge, Understanding, Methods, and Exposition, and the output language. Follow the request's language; support Chinese, English, or requested bilingual output. [grades.json](references/grades.json) contains the complete ordered names for each axis in both languages. These are named ordinal grades, not numeric scores.

Keep supplied grades unchanged. Ask about missing, ambiguous, or conflicting values. Do not infer grades from a paper, interpolate a missing value, or use the lowest grade for an unassessed axis. If the user supplies numbers, clarify their mapping to these named grades before drawing. If they want help evaluating the work, treat that as a separate assessment request.

## Draw

Use [render_profile.py](scripts/render_profile.py), which needs only Python 3. Write an input JSON in the authorized output location, then run:

```sh
python3 /path/to/mathprofile/scripts/render_profile.py input.json output.svg
```

Resolve the script relative to this installed skill; the repository is not needed at runtime. Use an available Python runtime (on the owner's Mac, `/opt/homebrew/bin/python3.13 -B`). A minimal input is:

```json
{
  "title": "Title of the work",
  "language": "en",
  "grades": {
    "significance": "A Worthwhile Contribution",
    "knowledge": "A Step Forward",
    "understanding": "Fresh Insight",
    "methods": "No Improvement",
    "exposition": "The Structure Made Clear"
  }
}
```

`language` accepts `zh`, `en`, or `bilingual`; grade values may use either language's exact name. Optional `context` is `contribution` by default, producing the neutral title **Mathematical contribution profile / 数学贡献五维图**. Use `ai-reading-selection` only when the supplied assessment explicitly calls for that identity, as MathMerit does. AI assistance in drawing a person's grades does not make the assessment AI-generated. Attribution and evaluation status belong in the accompanying text; do not invent them.

The renderer rejects incomplete or invalid grades before creating output, and refuses to replace an existing file unless `--overwrite` is deliberately supplied for an authorized revision. A validation error calls for correcting the input, not changing the grade to make it fit.

## Check and deliver

Compare all five displayed grade names with the supplied choices. The axes run clockwise from the top: Significance, Knowledge, Understanding, Methods, Exposition. Each axis has four grades: the lowest is at the shared origin, and the other three occupy successive rings. The diagram includes the ordered names for interpreting each axis. The positions show order only; neither distances nor area measure contribution, and no total score is computed.

Keep zero-radius markers at the origin. All-lowest profiles are a point, and some profiles form lines; these are valid complete profiles. The renderer retains all five coordinates in the contour even when they coincide.

Render and inspect the SVG for clipping and overlap when a renderer is available. Deliver the SVG and display a preview when supported, with a brief note that it follows the supplied grades. Do not add a reading recommendation or an assessment of the work.
