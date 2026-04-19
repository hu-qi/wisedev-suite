---
name: wisedev-requirement-spec
description: write structured chinese requirement specifications from rough needs, clarified requirement briefs, transcripts, or mixed materials. use when the user needs a formal markdown requirement document with scope, actors, scenarios, functional requirements, non-functional requirements, acceptance criteria, and traceable identifiers in a government or enterprise documentation style.
---

# 目标
在 `using-wisedev` 已确认这是明确单阶段任务，或 `wisedev-orchestrator` 已完成阶段判断后，再由本 Skill 处理当前阶段。

首次执行本阶段任务时，优先参考 `references/example-library.md`；若输入与“上传下达模块”高度相似，再对照 `../shared/full-chain-examples/case-01-upload-delivery/02-requirement-spec.md` 的本阶段样例。


输出正式、可评审、可追踪的《需求规格说明书》。

# 输入前提

优先使用以下任一输入：
- 已整理的需求简报
- 会议纪要转需求梳理结果
- 用户直接给出的结构化业务需求

# 文风要求

- 偏政企 / 国企正式文档风格。
- 避免互联网产品口语化表达。
- 使用“应支持 / 应具备 / 应满足 / 系统应能够”等表述。

# 必须包含的章节

1. 文档概述
2. 项目背景与建设目标
3. 角色与参与方
4. 业务场景
5. 范围界定
6. 功能需求
7. 非功能需求
8. 业务规则
9. 验收标准
10. 风险与待定事项
11. 术语表

# 写作规则

- 所有关键需求必须分配稳定编号，如 `FR-001`、`NFR-001`。
- 每一项功能需求应可被测试验证。
- 对优先级不明确的要求，默认不做强行排序，但可用“核心 / 重要 / 可选”分组。
- 需要时补充“范围外事项”，避免范围蔓延。

# 高质量样例优先

优先参考 `references/example-library.md` 和 `references/examples/` 下的案例，沿用其中的编号方式、正式文风和验收标准粒度。

# 可用资源

- `references/requirement-principles.md`
- `references/scope-rules.md`
- `templates/srs-template.md`
- `templates/acceptance-criteria.md`
- `templates/glossary.md`
- `templates/functional-requirement.md`
- `templates/nonfunctional-requirement.md`
- `templates/risk-and-issues.md`
- `templates/business-scenario.md`
- `templates/project-overview.md`