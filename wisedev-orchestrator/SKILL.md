---
name: wisedev-orchestrator
description: "orchestrate staged delivery artifact generation from short requirements, meeting notes, transcripts, and mixed materials. use when the user wants to turn ambiguous chinese product or business input into structured outputs such as requirement briefs, requirement specifications, design documents, openapi yaml contracts, or vue plus mock prototypes. act as the mandatory entry skill for multi-stage work: identify the current stage first, normalize context first, choose one child skill first, and require stage handoff artifacts before any downstream stage."
---

# 目的

将模糊业务输入收敛为分阶段、可审阅、可交接的交付产物，并作为整套 Skills 的默认总控入口与强制工作流控制面。

在任何相关任务开始前，优先由 `using-wisedev` 判断是否应启用 WiseDev；一旦确定是跨阶段或模糊任务，再由本 Skill 接管阶段判断与路由。

# 强制规则

1. `using-wisedev` 已确认需要进入 WiseDev 后，只要任务可能跨越两个及以上阶段，必须先由本 Skill 判断阶段，再决定是否路由给子 Skill。
2. 不得直接越过上游阶段生成下游产物，除非用户明确要求跳过，并且当前输出中明确写出“假设与边界”。
3. 在任何子 Skill 输出前，必须先形成上下文包；在任何阶段结束后，必须形成阶段交接单。
4. 默认一次只完成一个阶段；若用户要求连续推进，先给出阶段计划，再分阶段输出。
5. 对复杂或模糊输入，优先参考完整链路样例；对明确阶段任务，优先参考该阶段样例库。

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
- Vue + Mock 原型
- 跨阶段连续交付包

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

## 步骤 5：选择唯一子 Skill
- 会议纪要、转写、讨论材料 → `wisedev-meeting-to-spec`
- 正式需求规格说明书 → `wisedev-requirement-spec`
- 概要设计或详细设计 → `wisedev-design-doc`
- 接口契约、Mock-ready OpenAPI → `wisedev-openapi-contract`
- 演示型前端原型与 mock 服务 → `wisedev-vue-mock-prototype`

## 步骤 6：输出阶段性交付物
输出必须是当前阶段的正式草稿，而不是下一阶段的半成品摘要。

## 步骤 7：生成阶段交接单
阶段结束前，必须生成 `templates/stage-handoff.md`，写清：
- 稳定输入
- 追踪键
- 假设与限制
- 下游目标
- 不应越界的内容

# 样例优先级规则

1. 复杂模糊输入：先参考 `../shared/full-chain-examples/case-01-upload-delivery/README.md` 与对应阶段文件。
2. 明确阶段任务：优先参考 `references/example-library.md`。
3. 输入与已有案例高度相似时：复用样例的阶段判断、输出顺序、章节粒度与交接方式，但不要照抄业务内容。

# 输出规则

- 中文业务叙述优先，语气偏正式、审慎、适合政企项目文档。
- 工程标识、文件路径、路由、schema 名称使用英文。
- 对缺失信息不要硬编；要明确列为“工作假设”或“待确认事项”。
- 需求、设计、API、原型之间必须保留追踪关系。
- 当用户要求跨阶段连续产出时，先给阶段计划，再分段输出，避免把所有产物一次性混在一起。

# 实现控制面

本 Skill 默认在 `using-wisedev` 完成激活判断后生效。

优先读取以下资源作为工作流控制面，而不是把 README 当成主要入口：
- `references/meta-workflow.md`
- `references/workflow.md`
- `references/routing-rules.md`
- `references/output-contract.md`
- `references/example-library.md`
