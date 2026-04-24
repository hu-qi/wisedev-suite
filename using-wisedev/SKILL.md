---
name: using-wisedev
description: enforce wisedev workflow discipline before product-delivery tasks. use when the user asks for requirement clarification, requirement specifications, design documents, openapi yaml contracts, vue plus mock prototypes, or any request that may cross stages. require the assistant to check the wisedev skill suite first, route multi-stage tasks through wisedev-orchestrator first, and map clear single-stage requests to the correct wisedev child skill.
---

# 目的

作为 WiseDev 套件的元 Skill，在任何需求、设计、契约、原型类任务开始前，先约束代理检查是否应启用 WiseDev 工作流。

默认假设本套件以 bundle 方式安装，并可访问 `shared/` 下的共享模板与完整链路样例。

# 兼容原则

1. 本 Skill 必须继续兼容原有单技能、单阶段、非 team 场景的使用方式。
2. team-aware 能力是增强分支，不是唯一分支。
3. 若未检测到 team 协作上下文，沿用原有 WiseDev 入口判断和子 Skill 路由逻辑。
4. 不得因为启用 team-aware 规则而让原本可直接处理的单阶段任务无故变重、变慢或强依赖额外目录。

# Team-aware 识别规则

当运行环境显式表现出以下任一特征时，可视为 team 协作上下文：
- 当前任务已明确由长期协作团队接管
- 上下文中存在 leader / reviewer / shared artifacts / handoff 等团队协作约束
- 任务要求围绕共享工件进行角色分工、审查、验收或阶段推进

若已识别为 team 协作上下文，则增加以下规则：
1. 不直接把多阶段任务绑定到某个子 Skill，优先交由 `wisedev-orchestrator` 作为 leader 控制层判断负责人。
2. 即使是明确单阶段任务，也要先判断：这是应该由当前团队中的某个角色接手，还是仍可作为独立子 Skill 直接执行。
3. 在 team 场景中，本 Skill 的职责从“选择子 Skill”升级为“决定是否进入团队协作控制面”。
4. 不要在 team 场景中绕过 leader 直接把跨阶段任务交给下游产出型 Skill。

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
- 已识别为 team 协作上下文，且任务需要 leader 判断负责人、共享工件或审查闭环

# Team 场景下的控制策略

在 team 场景中，请按以下顺序执行：
1. 先判断当前请求是否应进入长期协作团队控制面。
2. 再判断该任务更适合作为：
   - leader 的阶段判断任务
   - 某个团队角色的阶段执行任务
   - reviewer 的审查任务
3. 若需要团队分工、共享工件、审查、交接或多角色协作，优先交给 `wisedev-orchestrator`。
4. 仅当当前请求在 team 上下文中仍然是“明确、单阶段、边界清晰、可独立完成”的任务时，才直接进入对应子 Skill。

# 执行顺序

1. 先判断：这是单阶段任务还是跨阶段任务。
2. 再判断：输入是否满足单阶段最低前提。
3. 再判断：当前是否处于 team 协作上下文。
4. 若不满足单阶段前提，立即交给 `wisedev-orchestrator`。
5. 若满足单阶段前提但处于 team 上下文，优先让 `wisedev-orchestrator` 判断是否需要 leader 分配角色。
6. 若满足单阶段前提且不处于 team 上下文，选择唯一最合适的子 Skill。
7. 优先参考 `references/entry-mapping.md` 与 `references/activation-rules.md`。

# 样例优先级

- 跨阶段、复杂、模糊任务：优先看 `../shared/full-chain-examples/case-01-upload-delivery/README.md`，然后交给 `wisedev-orchestrator`。
- 明确单阶段任务：优先看目标子 Skill 的 `references/example-library.md`。
- Team 协作任务：优先参考 `../AgentTeam/` 下的角色、模板、运行规则，再交给 `wisedev-orchestrator` 控制推进。

# 可用资源

- `references/activation-rules.md`
- `references/entry-mapping.md`
- `../AgentTeam/COMPATIBILITY_GUIDELINES.md`
- `../AgentTeam/TEAM_RUNTIME_RULES.md`
- `../AgentTeam/ROLE_SPEC.md`
