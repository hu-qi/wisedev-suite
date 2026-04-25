# AgentTeam 接入计划

## 目标
将现有 `wisedev-suite` 从“总控 Skill + 子 Skill 的阶段化编排”逐步演进为“长期协作、多角色产品交付团队”。

## 阶段 1：规范准备
- 固定角色说明书
- 固定共享工件目录
- 固定派工 / 审查 / 验收模板
- 形成 team 配置草案

当前已完成的输入包括：
- `ROLE_SPEC.md`
- `team-config.example.yaml`
- `shared-workspace-layout.md`
- `shared/templates/*`

## 阶段 2：Skill 映射
- 确定每个角色对应的 skills
- 明确 leader / reviewer 的职责边界
- 确定哪些 skills 需要 team-aware 改造

参考：
- `SKILL_MAPPING.md`

## 阶段 3：Prompt 与模板对齐
- 为 `using-wisedev` 增加 team-aware 入口判断
- 为 `wisedev-orchestrator` 增加 leader 派工 / 验收逻辑
- 为各子 skill 增加共享工件写入约束
- 为 reviewer 增加问题导向审查规范

## 阶段 4：运行时接入
- 在真实 AgentTeam runtime 中挂载角色
- 将共享工件目录接入成员 workspace
- 让 leader/成员/reviewer 围绕共享工件推进
- 验证任务分派、审查、交接的闭环

## 阶段 5：持续优化
- 评估是否增加更多角色
- 评估是否开放局部并行
- 评估是否把更多模板和脚本纳入 team 工作流

## 第一批建议接入角色
1. `team_leader`
2. `product_analyst`
3. `solution_architect`
4. `api_designer`
5. `ux_designer`
6. `frontend_engineer`
7. `reviewer`

## 第一批成功标准
1. team leader 能稳定派工
2. 成员能将输出回写共享工件
3. reviewer 能基于共享工件发现问题
4. leader 能基于 reviewer 结论做推进决策
5. 下游阶段不再主要依赖聊天记忆推进
