# MathMerit / 数学品评

[中文](#中文) · [English](#english)

## 中文

### 为什么需要这个技能

**让英雄查英雄，好汉查好汉。**

随着 AI4Math 急速发展，论文越来越多：哪些值得数学家花时间阅读？

### 用途

MathMerit 将[关于数学工作评价的哥白尼倡议（Copernicus）](https://github.com/GauSyu/Copernicus) 转化为可独立执行的 AI 技能，帮助数学家筛选值得阅读的工作。技能内置五个维度的完整等级判据及其执行方法，并结合阅读收益与投入给出建议。报告中的评级与图表属于 AI 推测，仅供阅读筛选参考，不能代替专家判断。若你已对某项工作感兴趣，不应仅凭本报告放弃阅读。

### 报告内容

报告先分析数学贡献，说明有依据的评级及其局限；五项均能定级时附五维图。随后权衡具体阅读收益与投入，列出推荐与不推荐理由，给出有依据的阅读建议。部分维度无法定级，不妨碍有独立依据的阅读建议。报告引用本仓库。详见[报告规则](references/profile-format.md)。

### 使用

使用助手支持的本地技能安装方式，将本目录安装为 `mathmerit`。评价规则随技能提供，无需联网获取；查证论文与相关文献时可能需要联网。报告采用指定语言，未指定时跟随请求语言；需要双语时明确提出即可。报告格式和模板也可指定，例如 Markdown、PDF 或 Word；未指定时默认 Markdown。

例如：“用 $mathmerit 帮我判断这篇论文是否值得阅读，以中文给出报告。”

### 只画五维图

如果由你自己确定等级，可以单独安装本仓库的 [`skills/mathprofile`](skills/mathprofile/SKILL.md) 为 `mathprofile`。提供作品标题与五项等级，即可用 `$mathprofile` 画图；它不会重新评价、替你补分，也不会把人工评价标成 AI 推测。支持中文、英文和双语图，不需要安装 MathMerit。MathMerit 的报告也使用这套绘图程序。

## English

### Why this skill

**Let heroes assess heroes; let the brave assess the brave.**

As AI4Math develops rapidly and papers multiply, which deserve a mathematician's reading time?

### Purpose

MathMerit implements [the Copernican initiative for assessing mathematical work](https://github.com/GauSyu/Copernicus) as a self-contained AI skill to help mathematicians select works worth reading. It includes the complete grade criteria for all five dimensions and guidance for applying them, and weighs reading benefits against the required effort to make recommendations. The report's grades and diagram are AI inferences for reading selection only and cannot replace expert judgment. If a work already interests you, do not let this report alone dissuade you from reading it.

### Report contents

The report first analyzes mathematical contributions and explains supported grades and their limits, with a five-axis diagram when all five grades are supported. It then weighs concrete reading benefits and effort, gives reasons for and against reading, and offers a supported recommendation. Undetermined grades do not block independently supported reading advice. Reports cite this repository. See the [report rules](references/profile-format.md).

### Use

Install this directory as `mathmerit` using your assistant's local skill installation mechanism. Assessment rules are included in the skill and require no network retrieval; checking papers and related literature may still require network access. Reports follow the requested language, or the request's language; bilingual output is available on request. You can also specify the report format and template, such as Markdown, PDF, or Word; the default is Markdown.

Example: “Use $mathmerit to help me decide whether this paper is worth reading; write the report in English.”

### Draw a profile from your own grades

Install [`skills/mathprofile`](skills/mathprofile/SKILL.md) separately as `mathprofile`. Give `$mathprofile` the work's title and your five grades; it draws the profile without reassessing the work, filling missing grades, or labeling a human assessment as an AI inference. Chinese, English, and bilingual diagrams are supported. MathMerit is not required for standalone use; its reports reuse the same renderer.
