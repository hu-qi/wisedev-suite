---
name: wisedev-design-doc
description: generate chinese high-level and detailed design documents from requirement specifications, requirement briefs, or structured business input. use when the user needs architecture decomposition, module boundaries, role permissions, workflows, state transitions, data entities, interfaces, and exception handling documented in markdown in a formal enterprise style.
---

# 目标
在 `using-wisedev` 已确认这是明确单阶段任务，或 `wisedev-orchestrator` 已完成阶段判断后，再由本 Skill 处理当前阶段。

首次执行本阶段任务时，优先参考 `references/example-library.md`；若输入与“上传下达模块”高度相似，再对照 `../shared/full-chain-examples/case-01-upload-delivery/03-design-doc.md` 的本阶段样例。


将需求规格或需求简报转化为概要设计、详细设计，输出结构清晰、边界明确、便于后续 API 与原型工作的设计文档。

# 兼容原则

1. 本 Skill 必须继续兼容原有单阶段设计文档输出能力。
2. team-aware 能力仅用于补充共享工件与角色边界，不替换原有设计输出主流程。
3. 若未检测到 team 协作上下文，沿用原有设计文档产出逻辑。
4. 不应因为 team-aware 规则而强制要求 reviewer、leader 或共享工件必须预先存在。

# Team-aware 轻量规则

若处于 team 协作上下文，则增加以下轻量规则：
1. 默认将本 Skill 视作 `solution_architect` 的阶段执行能力。
2. 若已提供共享工件路径，应优先基于已验收需求工件输出设计，并尽量回写：
   - `design-doc.md`
   - `decision-log.md`
   - `stage-handoff.md`
3. 若需求仍存在关键不稳定点，应显式指出“待确认事项”或回推给 leader / reviewer，而不是私自修正业务目标。
4. 本 Skill 不应越界输出正式 OpenAPI 或前端原型实现。
5. 设计中的关键决策、方案取舍、风险与假设，建议显式沉淀到共享工件，而不是只写在正文叙述里。

# 模式

- 概要设计
- 详细设计
- 概设 + 详设组合包

# 必须覆盖的内容

- 设计目标与范围
- 总体架构与模块划分
- 角色与权限模型
- 关键业务流程
- 状态流转
- 数据模型
- 接口边界
- 异常处理与补偿策略
- 安全、审计、日志
- 对需求编号的追踪关系

# 规则

- 对需求规格中的每一项核心需求，至少在设计中找到对应模块或流程承接。
- 在没有指定技术栈时，设计描述优先保持实现中立。
- 当设计中存在多种方案时，应先列默认方案，再列备选方案和取舍原因。
- 在 team 场景中，若关键设计结论依赖未稳定的需求前提，必须显式标注，不得静默定案。

# 高质量样例优先

优先参考 `references/example-library.md` 中的模块拆分、状态机、异常处理写法；设计文档要与样例保持同等粒度和正式程度。

# 可用资源

- `references/design-patterns.md`
- `references/permissions-and-states.md`
- `references/exception-handling.md`
- `templates/hld-template.md`
- `templates/lld-template.md`
- `templates/module-design.md`
- `templates/state-machine.md`
- `templates/data-model.md`
- `templates/permission-model.md`
- `templates/sequence-flow.md`
- `templates/audit-log.md`
- `../AgentTeam/shared/templates/decision-log.md`
- `../AgentTeam/shared/templates/stage-handoff.md`
