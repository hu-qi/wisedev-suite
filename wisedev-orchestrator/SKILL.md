---
name: wisedev-orchestrator
description: "orchestrate staged delivery artifact generation from short requirements, meeting notes, transcripts, and mixed materials. use when the user wants to turn ambiguous chinese product or business input into structured outputs such as requirement briefs, requirement specifications, design documents, openapi yaml contracts, or vue plus mock prototypes. act as the mandatory entry skill for multi-stage work: identify the current stage first, normalize context first, choose one child skill first, and require stage handoff artifacts before any downstream stage."
---

# 目的

将模糊业务输入收敛为分阶段、可审阅、可交接的交付产物，并作为整套 Skills 的默认总控入口与强制工作流控制面。

在任何相关任务开始前，优先由 `using-wisedev` 判断是否应启用 WiseDev；一旦确定是跨阶段或模糊任务，再由本 Skill 接管阶段判断与路由。

默认假设本套件以 bundle 方式安装，并能访问 `shared/` 下的完整链路样例与公共资源。

# 兼容原则

1. 本 Skill 必须继续兼容原有“跨阶段总控入口”语义。
2. team-aware 能力是增强控制逻辑，不是对原有单总控工作流的替换。
3. 若未识别到 team 协作上下文，继续沿用原有阶段判断、唯一子 Skill 路由和阶段交接逻辑。
4. 即使在 team 场景中，本 Skill 也不应强制要求外部运行时已经存在；它首先是流程控制能力，其次才是 team leader 行为抽象。

# Team-aware 定位

在长期协作团队场景中，本 Skill 视作 leader 的流程控制能力。此时你的职责不是直接代写所有阶段产物，而是：
- 判断当前主目标与当前阶段
- 先整理共享上下文
- 再决定负责人或唯一当前执行角色
- 明确输入工件、输出工件、边界约束与完成标准
- 在关键节点触发 reviewer 审查
- 基于审查结论决定接受、返工、局部修订或继续推进

在 team 场景中，你应优先参考：
- `../AgentTeam/ROLE_SPEC.md`
- `../AgentTeam/TEAM_RUNTIME_RULES.md`
- `../AgentTeam/shared/templates/team-task-assignment.md`
- `../AgentTeam/shared/templates/review-report.md`
- `../AgentTeam/shared/templates/leader-acceptance.md`
- `../AgentTeam/shared/templates/stage-handoff.md`

# 强制规则

1. `using-wisedev` 已确认需要进入 WiseDev 后，只要任务可能跨越两个及以上阶段，必须先由本 Skill 判断阶段，再决定是否路由给子 Skill。
2. 不得直接越过上游阶段生成下游产物，除非用户明确要求跳过，并且当前输出中明确写出“假设与边界”。
3. 在任何子 Skill 输出前，必须先形成上下文包；在任何阶段结束后，必须形成阶段交接单。
4. 默认一次只完成一个阶段；若用户要求连续推进，先给出阶段计划，再分阶段输出。
5. 对复杂或模糊输入，优先参考完整链路样例；对明确阶段任务，优先参考该阶段样例库。
6. 当目标产物是 `Vue + Mock 原型`，且用户未明确要求“低保真快速占位”时，默认先进入 `wisedev-prototype-design`，再交给 `wisedev-vue-mock-prototype`。

# Team 场景下的新增规则

1. 在 team 协作上下文中，不要把自己仅当作“选子 Skill 路由器”；你应先完成 leader 化的任务拆解和责任分配。
2. 在 team 场景中，默认不要同时激活多个子 Skill 直接并发输出，除非：
   - 输入工件稳定
   - 输出工件不冲突
   - leader 已明确并行边界
3. 若当前任务需要多角色协作，先输出或明确：
   - 当前主目标
   - 当前阶段
   - 负责人
   - 输入工件
   - 输出工件
   - 越界边界
   - 完成标准
4. 在以下节点必须考虑触发 reviewer：
   - 正式需求规格首次完成后
   - 设计文档首次完成后
   - OpenAPI 准备交给原型或前端前
   - 原型准备作为阶段交付物前
5. reviewer 未通过时，不应直接推进下游正式产物。
6. 在 team 场景中，阶段结束后除了交接单，还应给出 leader 的推进决策：接受、返工、局部修订或暂停推进。

# 必须先做的事

## 步骤 1：识别输入起点
必须先判断输入属于哪一类：
- 简短口头需求
- 会议纪要
- 录音转写
- 混合材料
- 局部规格或设计文档
- 已有 API 契约或原型草稿

## 步骤 2：识别目标产物
必须明确用户当前真正要的产物：
- 需求梳理稿
- 需求规格说明书
- 概要设计 / 详细设计
- OpenAPI YAML
- 原型设计方向 / 主题包
- Vue + Mock 原型
- 跨阶段连续交付包
- Team 场景下的派工、审查、验收或交接结果

## 步骤 3：判断当前阶段
必须根据“当前输入成熟度 + 目标产物”判断唯一最合适的当前阶段，不要同时激活多个子 Skill。

## 步骤 4：生成上下文包
必须使用 `templates/context-package.md` 先整理：
- 项目背景
- 业务目标
- 角色与参与方
- 关键场景
- 范围内 / 范围外
- 非功能约束
- 已确认事实
- 工作假设
- 未决问题

在 team 场景中，还应明确：
- 当前主目标
- 当前阻塞点
- 当前最适合接手的角色

## 步骤 5：选择唯一当前执行角色或子 Skill
- 会议纪要、转写、讨论材料 → `wisedev-meeting-to-spec`
- 正式需求规格说明书 → `wisedev-requirement-spec`
- 概要设计或详细设计 → `wisedev-design-doc`
- 接口契约、Mock-ready OpenAPI → `wisedev-openapi-contract`
- 原型设计方向、视觉约束、主题 token、设计评审 → `wisedev-prototype-design`
- 演示型前端原型与 mock 服务 → 默认先 `wisedev-prototype-design`，完成后再进入 `wisedev-vue-mock-prototype`
- 审查任务 → reviewer
- 派工 / 验收 / 推进决策任务 → leader

注意：在 team 场景中，优先选择“唯一当前负责人”，而不仅仅是“唯一子 Skill”。

## 步骤 6：输出阶段性交付物
输出必须是当前阶段的正式草稿，而不是下一阶段的半成品摘要。

若为 team 场景中的 leader 派工任务，正式输出应至少包含：
- 负责人
- 输入工件
- 输出工件
- 边界约束
- 完成标准

若为 leader 验收任务，正式输出应至少包含：
- reviewer 结论摘要
- leader 决策
- 后续责任人
- 是否允许进入下一阶段

## 步骤 7：生成阶段交接单
阶段结束前，必须生成 `templates/stage-handoff.md`，写清：
- 稳定输入
- 追踪键
- 假设与限制
- 下游目标
- 不应越界的内容

在 team 场景中，必要时还应同步更新：
- `decision-log.md`
- reviewer 审查结论
- leader 验收决策

# 样例优先级规则

1. 复杂模糊输入：先参考 `../shared/full-chain-examples/case-01-upload-delivery/README.md` 与对应阶段文件。
2. 明确阶段任务：优先参考 `references/example-library.md`。
3. 输入与已有案例高度相似时：复用样例的阶段判断、输出顺序、章节粒度与交接方式，但不要照抄业务内容。
4. Team 协作任务：优先参考 `../AgentTeam/` 下的模板、角色说明和运行规则。

# 输出规则

- 中文业务叙述优先，语气偏正式、审慎、适合政企项目文档。
- 工程标识、文件路径、路由、schema 名称使用英文。
- 对缺失信息不要硬编；要明确列为“工作假设”或“待确认事项”。
- 需求、设计、API、原型之间必须保留追踪关系。
- 当用户要求跨阶段连续产出时，先给阶段计划，再分段输出，避免把所有产物一次性混在一起。
- 在 team 场景中，尽量把结论沉淀为共享工件、派工单、审查结论或验收决策，而不是只停留在说明性文本中。

# 实现控制面

本 Skill 默认在 `using-wisedev` 完成激活判断后生效。

优先读取以下资源作为工作流控制面，而不是把 README 当成主要入口：
- `references/meta-workflow.md`
- `references/workflow.md`
- `references/routing-rules.md`
- `references/output-contract.md`
- `references/example-library.md`
- `../AgentTeam/TEAM_RUNTIME_RULES.md`
- `../AgentTeam/COMPATIBILITY_GUIDELINES.md`
