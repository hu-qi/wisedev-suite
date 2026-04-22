---
name: using-wisedev
description: enforce wisedev workflow discipline before product-delivery tasks. use when the user asks for requirement clarification, requirement specifications, design documents, openapi yaml contracts, vue plus mock prototypes, or any request that may cross stages. require the assistant to check the wisedev skill suite first, route multi-stage tasks through wisedev-orchestrator first, and map clear single-stage requests to the correct wisedev child skill.
---

# 目的

作为 WiseDev 套件的元 Skill，在任何需求、设计、契约、原型类任务开始前，先约束代理检查是否应启用 WiseDev 工作流。

默认假设本套件以 bundle 方式安装，并可访问 `shared/` 下的共享模板与完整链路样例。

# 强制规则

1. 只要任务涉及以下任一内容，先检查是否应启用 WiseDev：
   - 会议纪要 / 录音转写 / 混合讨论材料的需求梳理
   - 需求规格说明书
   - 概要设计 / 详细设计
   - OpenAPI YAML
   - 原型设计方向 / 配色方案 / 视觉风格 / 设计评审
   - Vue + Mock 原型
   - 从一个阶段推进到另一个阶段的连续交付
2. 只要任务可能跨越两个及以上阶段，必须先交给 `wisedev-orchestrator`。
3. 只有当用户请求明确处于单一阶段，并且输入材料已经满足该阶段最低前提时，才允许直接进入对应子 Skill。
4. 不要把根 README、REVIEW_GUIDE 或人工审阅说明当成主要控制面；优先读取 Skill 本体和 `references/` 中的规则文件。
5. 这些规则是默认强制行为，不是可选建议。

# 显式入口映射

当用户请求与下列表述高度一致时，可直接映射到对应子 Skill；否则优先交给 `wisedev-orchestrator`：

- “梳理会议纪要 / 录音转写 / 讨论材料 / 需求梳理” → `wisedev-meeting-to-spec`
- “写需求规格说明书 / 输出 SRS / 细化需求规格” → `wisedev-requirement-spec`
- “写概要设计 / 详细设计 / 模块设计 / 状态机 / 数据模型” → `wisedev-design-doc`
- “生成 OpenAPI / 接口契约 / mock-ready openapi yaml” → `wisedev-openapi-contract`
- “推荐原型设计方向 / 设计风格 / 配色方案 / 设计评审” → `wisedev-prototype-design`
- “做 Vue 原型 / 前端 mock 原型 / 演示型原型” → `wisedev-vue-mock-prototype`

## 默认回退策略

出现以下任一情况时，不直接映射子 Skill，必须转交 `wisedev-orchestrator`：
- 输入起点不清楚
- 目标产物不止一个
- 上游产物明显缺失
- 用户同时要求“梳理 + 规格 + 设计 + API + 原型”中的两个及以上
- 输入材料中混有会议纪要、设计片段、接口片段等多种来源

# 执行顺序

1. 先判断：这是单阶段任务还是跨阶段任务。
2. 再判断：输入是否满足单阶段最低前提。
3. 若不满足，立即交给 `wisedev-orchestrator`。
4. 若满足，选择唯一最合适的子 Skill。
5. 优先参考 `references/entry-mapping.md` 与 `references/activation-rules.md`。

# 样例优先级

- 跨阶段、复杂、模糊任务：优先看 `../shared/full-chain-examples/case-01-upload-delivery/README.md`，然后交给 `wisedev-orchestrator`。
- 明确单阶段任务：优先看目标子 Skill 的 `references/example-library.md`。

# 可用资源

- `references/activation-rules.md`
- `references/entry-mapping.md`
