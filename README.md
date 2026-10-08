# MathMerit / 数学品评

[中文](#中文) · [English](#english)

## 中文

### 为什么需要这个技能

**让英雄查英雄，好汉查好汉。**

随着 AI4Math 急速发展，论文越来越多：哪些值得数学家花时间阅读？读过之后，又怎样查证、讨论和修订我们对数学贡献的判断？

### 用途

MathMerit 支持以人的认识为中心的人机协作数学评价：帮助人们借助 AI 辨析数学成果的贡献，决定读什么、怎样读，并在需要时继续查证、讨论和修订评价。AI 阅读筛选本身就是一种直接实用的人机协作评价；人的参与较浅时，可以止于阅读建议，参与深入时，则沿着同一份材料继续共同评价，无须更换产品或完成规定阶段。

技能采用[哥白尼倡议（Copernicus）](https://github.com/GauSyu/Copernicus)的原则及其五维判据方案。知识、理解、方法、表达辨析贡献所在，数学意义判断贡献的分量；等级不能相加。技能内置完整判据与执行方法，阅读建议另依具体收益与必要投入作出。采用的来源快照与规则修订见[版本依据](references/source-revision.md)。

AI 可以独立交付有根据的分析和阅读建议，不以人工审查为前置门槛。人在任何具体判断中都可补充材料、核对比较、提出阅读经验或质疑理由。报告说明实际参与和核查范围；人的身份、赞同或 AI 的确信都不能替代理由。

### 输出与接续

完整的阅读筛选报告分析贡献，说明等级的根据、证据与局限，五项均有依据时可附五轴图；随后权衡阅读收益与投入，给出阅读建议。保留四档建议：强烈推荐、值得一看、谨慎阅读、不值一提；部分维度无法定级，不妨碍有独立依据的阅读建议。未知不能填成最低等级。

局部追问可以只检查一个比较或修订一条判断，无须重做全套报告。新证据改变哪些判断、还有什么分歧，都在相应位置说明，保留其他仍然成立的发现。图名依实际用途与参与情况选择，归属与核查范围写在正文中；图形面积不代表价值。详见[评价与报告规则](references/profile-format.md)。

### 使用

使用助手支持的本地技能安装方式，将本目录安装为 `mathmerit`。评价规则随技能提供，无需联网获取；查证论文与相关文献时可能需要联网，并遵循已有的本地文献规则。报告采用指定语言，未指定时跟随请求语言；需要双语时明确提出即可。报告格式和模板也可指定，例如 Markdown、PDF 或 Word；未指定时默认 Markdown。

例如：

- “用 $mathmerit 帮我判断这篇论文是否值得阅读，以中文给出报告。”
- “用 $mathmerit 检查这项贡献判断：前作定理 3.2 是否已经覆盖这里的假设？只更新受影响的结论。”
- “用 $mathmerit 继续讨论表达评价：我读过这一节，认为这个例子帮助解释了构造；请结合原文检查我的理由。”

### 只画五维图

如果由你自己确定等级，可以单独安装本仓库的 [`skills/mathprofile`](skills/mathprofile/SKILL.md) 为 `mathprofile`。提供作品标题与五项等级，即可用 `$mathprofile` 画图；它不会重新评价、替你补分，也不会把人工评价标成 AI 推测。支持中文、英文和双语图，不需要安装 MathMerit。MathMerit 的报告也使用这套绘图程序。

## English

### Why this skill

**Let heroes assess heroes; let the brave assess the brave.**

As AI4Math develops rapidly and papers multiply, which deserve a mathematician's reading time? After reading, how can we check, discuss, and revise our judgments of their contributions?

### Purpose

MathMerit supports human-centered mathematical assessment with AI: it helps people examine contributions, decide what and how to read, and continue checking, discussing, and revising an assessment when useful. AI reading selection is itself a practical form of human–AI assessment. With limited human participation, useful reading advice can be the endpoint; deeper participation continues the same work without a separate product or mandatory stages.

The skill applies the principles of [Copernicus](https://github.com/GauSyu/Copernicus) through its five-dimensional scheme. Knowledge, Understanding, Methods, and Exposition distinguish contributions; Significance judges their weight. Grades do not form a total score. The complete criteria and application guidance are bundled; reading recommendations separately weigh concrete benefits against necessary effort. See the [source and rules revision](references/source-revision.md).

AI can deliver supported analysis and reading advice without prior human review. People can join at any particular judgment by supplying material, checking comparisons, contributing reading experience, or challenging reasons. Reports describe actual participation and checking scope; neither human identity or agreement nor AI confidence replaces reasons.

### Outputs and continuation

A complete reading-selection report analyzes contributions, with grades, evidence, reasons, and limits, and may include a five-axis diagram when all five grades are supported. It then weighs reading benefits and effort to recommend one of four levels: Strongly Recommended, Worth a Look, Read with Caution, or Not Worth Reading. Undetermined contribution grades do not block independently supported reading advice; unknown is not the lowest grade.

A focused follow-up can check one comparison or revise one judgment without repeating a complete report. Explain which judgments change with new evidence and which disagreements remain, preserving independent findings. Choose the diagram context for the actual purpose and participation; describe attribution and checking scope in the text. Diagram area does not measure value. See the [assessment and reporting rules](references/profile-format.md).

### Use

Install this directory as `mathmerit` using your assistant's local skill installation mechanism. Assessment rules require no network retrieval; checking papers and related literature may still require network access and follows applicable local literature rules. Reports follow the requested language, or the request's language; bilingual output is available on request. You can also specify the report format and template, such as Markdown, PDF, or Word; the default is Markdown.

Examples:

- “Use $mathmerit to help me decide whether this paper is worth reading; write the report in English.”
- “Use $mathmerit to check this contribution claim: does prior Theorem 3.2 already cover these hypotheses? Update only the affected conclusions.”
- “Use $mathmerit to continue the exposition assessment: I read this section and found the example helpful in explaining the construction; check my reasons against the text.”

### Draw a profile from your own grades

Install [`skills/mathprofile`](skills/mathprofile/SKILL.md) separately as `mathprofile`. Give `$mathprofile` the work's title and your five grades; it draws the profile without reassessing the work, filling missing grades, or labeling a human assessment as an AI inference. Chinese, English, and bilingual diagrams are supported. MathMerit is not required for standalone use; its reports reuse the same renderer.
