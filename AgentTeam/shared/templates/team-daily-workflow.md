# Team Daily Workflow

## Purpose
用于长期协作团队的日常推进，确保每次工作都围绕共享工件、责任分工和可审查交付展开。

## Step 1: Leader Confirms Main Goal
Leader 先确认本轮主目标：
- 当前主目标：`<一句话目标>`
- 当前阶段：`<阶段>`
- 当前阻塞点：`<阻塞点>`
- 本轮优先级：`<高 / 中 / 低>`

## Step 2: Check Stable Inputs
在派工前先确认哪些共享工件已稳定：
- `<工件1>`
- `<工件2>`
- `<工件3>`

如果输入不稳定：
1. 不进入下游正式交付
2. 先派工修复上游工件
3. 必要时补“假设 / 待确认事项”

## Step 3: Leader Assigns Tasks
Leader 使用 `team-task-assignment.md` 给成员派工，明确：
- 负责人
- 输入工件
- 输出工件
- 边界约束
- 完成标准

## Step 4: Members Update Shared Artifacts
成员执行任务时必须：
1. 基于已验收输入开展工作
2. 将正式结论写入共享工件
3. 不在消息里形成唯一事实来源
4. 不越界修改他人职责范围内的结论

## Step 5: Reviewer Checks Deliverables
当某项输出达到阶段完成条件后，提交 reviewer：
- 审查对象：`<工件路径>`
- 审查重点：
  - 一致性
  - 完整性
  - 越界
  - 追踪关系
  - 风险显式化

Reviewer 使用 `review-report.md` 输出结论。

## Step 6: Leader Makes Acceptance Decision
Leader 基于 reviewer 报告做推进决策：
- 接受
- 局部修订
- 返工
- 暂停推进

Leader 使用 `leader-acceptance.md` 沉淀决策。

## Step 7: Update Handoff
每个阶段或里程碑结束后，更新：
- `stage-handoff.md`
- `decision-log.md`
- 必要的 `open-questions.md`

## Daily Rules
1. 共享工件优先于聊天记忆
2. reviewer 未通过，不默认推进下游
3. 可以局部并行，但必须明确负责人和依赖
4. 不确定信息必须写成假设或待确认项
5. 每轮结束时要有明确“下一步责任人”

## End-of-Round Summary
每轮收尾时至少记录：
- 本轮完成了什么
- 更新了哪些工件
- 哪些问题还未解决
- 下一轮由谁推进什么
