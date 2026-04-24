# Implementation Tasks

## 目标
本文件用于将 `AgentTeam/` 下的设计资料转化为可执行的工程任务清单，帮助 WiseDev Suite 从现有“总控 Skill + 子 Skill”模式逐步演进到“长期协作、多角色产品交付团队”。

## 阶段 1：规范固化

### Task 1.1 建立 AgentTeam 设计入口
- 目标：将 `AgentTeam/` 作为团队模式设计入口固定下来
- 当前状态：已完成
- 产出：
  - `README.md`
  - `ROLE_SPEC.md`
  - `TEAM_ADOPTION_PLAN.md`
  - `TEAM_RUNTIME_RULES.md`

### Task 1.2 固定共享模板
- 目标：让团队协作模板成为稳定规范
- 当前状态：已完成
- 产出：
  - `shared/templates/team-task-assignment.md`
  - `shared/templates/review-report.md`
  - `shared/templates/leader-acceptance.md`
  - `shared/templates/team-daily-workflow.md`
  - `shared/templates/context-package.md`
  - `shared/templates/stage-handoff.md`
  - `shared/templates/decision-log.md`

## 阶段 2：Skill 对齐改造

### Task 2.1 为 `using-wisedev` 增加 team-aware 入口判断
- 目标：在 team 运行时不仅判断是否启用 WiseDev，还要判断更适合哪个角色接手
- 建议动作：
  1. 增加 team 模式说明
  2. 增加“由 leader 决定负责人”的规则
  3. 保持单阶段和跨阶段任务判断能力

### Task 2.2 将 `wisedev-orchestrator` 重构为 leader 控制能力
- 目标：让 orchestrator 更适合作为 team leader 的流程控制能力
- 建议动作：
  1. 增加派工规则
  2. 增加输入工件 / 输出工件约束
  3. 增加 reviewer 触发条件
  4. 增加 leader 验收决策要求

### Task 2.3 为子 skill 增加共享工件写入约束
- 目标：让子 skill 的正式产出落到共享工件，而不是仅停留在对话中
- 建议动作：
  1. 在 `wisedev-meeting-to-spec` 中引入 `context-package.md` / `requirement-brief.md`
  2. 在 `wisedev-requirement-spec` 中引入 `requirement-spec.md`
  3. 在 `wisedev-design-doc` 中引入 `design-doc.md`
  4. 在 `wisedev-openapi-contract` 中引入 `openapi.yaml`
  5. 在 `wisedev-prototype-design` 中引入 `prototype-plan.md` / `ux-rules.md`
  6. 在 `wisedev-vue-mock-prototype` 中引入前端原型输出目录约束

### Task 2.4 为 reviewer 增加问题导向审查规范
- 目标：让 reviewer 成为独立角色，而不是弱化的附属检查器
- 建议动作：
  1. 引入 `review-report.md`
  2. 明确必须检查一致性 / 完整性 / 越界 / 追踪关系
  3. 明确 reviewer 不直接重写主产物

## 阶段 3：共享工件接入

### Task 3.1 定义 team 工作区目录
- 目标：为 team 提供统一共享工件目录
- 建议动作：
  1. 将 `shared-workspace-layout.md` 转为实际目录约束
  2. 确定默认工作区结构
  3. 确定各角色的共享读写边界

### Task 3.2 建立共享工件初始化机制
- 目标：在 team 首次启动时生成基础工件
- 建议动作：
  1. 初始化 `context-package.md`
  2. 初始化 `decision-log.md`
  3. 初始化 `stage-handoff.md`
  4. 初始化 review 目录

### Task 3.3 定义共享工件更新策略
- 目标：明确工件何时创建、何时更新、何时回审
- 建议动作：
  1. 工件更新时打标主要负责人
  2. 关键工件变更时触发 reviewer
  3. 关键决策变更时更新 decision log

## 阶段 4：Team 配置与角色接入

### Task 4.1 固化第一版 team 配置
- 目标：从 `team-config.example.yaml` 产出真实可运行配置
- 建议动作：
  1. 确定第一批角色是否全部启用
  2. 确定 skills 列表是否需要精简
  3. 确定 persona 是否需要更贴合实际业务风格

### Task 4.2 接入第一批长期角色
- 目标：让核心角色先进入实际 team runtime
- 建议角色：
  1. `team_leader`
  2. `product_analyst`
  3. `solution_architect`
  4. `api_designer`
  5. `ux_designer`
  6. `frontend_engineer`
  7. `reviewer`

### Task 4.3 控制第一版并行度
- 目标：避免第一版 team 运行时过度并行
- 建议动作：
  1. 主线串行
  2. 局部并行
  3. reviewer 强介入
  4. leader 强验收

## 阶段 5：试点运行

### Task 5.1 选择试点链路
- 目标：用一个小范围场景验证 team 模式
- 建议试点：
  - 需求规格 -> API 契约 -> Vue 原型

### Task 5.2 观察关键指标
- 目标：评估 team 模式是否比现有 orchestrator 更有效
- 观察项：
  1. 是否真的减少跨阶段漂移
  2. 共享工件是否成为唯一正式事实来源
  3. reviewer 是否真的拦住低质量推进
  4. leader 是否没有吞并所有工作

### Task 5.3 记录问题与回调
- 目标：形成下一轮改造输入
- 建议动作：
  1. 记录角色边界问题
  2. 记录共享工件不清晰点
  3. 记录并行冲突场景
  4. 记录最需要补强的模板或规则

## 第一批推荐优先级

### P0
1. `using-wisedev` team-aware 改造
2. `wisedev-orchestrator` leader 化改造
3. 子 skill 共享工件写入约束
4. reviewer 审查规范接入

### P1
1. 共享工件初始化机制
2. 第一版 team 配置接入
3. 试点链路运行

### P2
1. 更细粒度角色优化
2. 更高并行度支持
3. 更多自动化脚本与模板协作

## 完成标准
当以下条件同时满足时，可认为第一版 AgentTeam 接入成功：
1. leader 能稳定派工
2. 成员能把正式输出写入共享工件
3. reviewer 能基于工件做审查
4. leader 能基于 reviewer 结论做推进决策
5. 下游推进不再主要依赖聊天记忆
