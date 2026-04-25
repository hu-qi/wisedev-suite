# Bundle Review And Smoke Test

## 目的
本清单用于在 `huqi/team-aware` 分支上做 bundle 级人工 review 和 smoke test，确认 team-aware 改造没有破坏原有 WiseDev skills 的独立使用方式。

## 一、人工 Review 清单

### A. 控制层 Review
检查以下文件：
- `using-wisedev/SKILL.md`
- `wisedev-orchestrator/SKILL.md`

确认：
1. team-aware 被描述为增强分支，而不是唯一模式
2. 非 team 场景的原有入口判断和阶段路由没有被删除
3. 没有把 `AgentTeam/` 写成必需目录
4. 没有把 reviewer / leader 规则设成所有场景的强制前置

### B. 子 Skill Review
检查以下文件：
- `wisedev-meeting-to-spec/SKILL.md`
- `wisedev-requirement-spec/SKILL.md`
- `wisedev-design-doc/SKILL.md`
- `wisedev-openapi-contract/SKILL.md`
- `wisedev-prototype-design/SKILL.md`
- `wisedev-vue-mock-prototype/SKILL.md`

确认：
1. 仍保留单阶段主目标与主输出
2. team-aware 规则被描述为轻量增强
3. 没有强制要求共享工件必须存在
4. 没有把原 skill 改成只能由 leader 派工后才能执行
5. 角色边界描述清楚，但没有让 skill 失去独立产出能力

### C. AgentTeam 设计包 Review
检查：
- `AgentTeam/` 下的所有文件

确认：
1. 文档之间术语一致
2. 模板之间没有明显冲突
3. `team-config.example.yaml` 与角色说明书一致
4. changelog、路线图、兼容规则之间口径一致

## 二、Smoke Test 场景

### Scenario 1: 非 team 单阶段需求梳理
输入：一段会议纪要
触发：`using-wisedev`
预期：
1. 可以直接进入 `wisedev-meeting-to-spec` 或经 orchestrator 做原有判断
2. 不要求必须存在共享工件
3. 不要求 reviewer 前置
4. 能产出正常需求梳理结果

### Scenario 2: 非 team 单阶段需求规格
输入：明确需求简报
触发：`wisedev-requirement-spec`
预期：
1. 仍可直接输出正式 SRS
2. 不被 team 规则阻塞
3. 不强制要求 `AgentTeam/` 目录

### Scenario 3: 非 team 单阶段设计文档
输入：稳定需求规格
触发：`wisedev-design-doc`
预期：
1. 仍可直接输出设计文档
2. 不要求共享工件或 reviewer
3. 保持原有设计文档结构

### Scenario 4: 非 team OpenAPI 契约
输入：稳定需求和设计输入
触发：`wisedev-openapi-contract`
预期：
1. 仍可直接输出 `openapi.yaml`
2. 不要求 leader / reviewer
3. 对缺失信息仍按原有“假设与边界 + YAML”顺序输出

### Scenario 5: 非 team Vue 原型
输入：设计与 OpenAPI
触发：`wisedev-vue-mock-prototype`
预期：
1. 仍可直接输出 Vue 原型方案与代码骨架
2. 不要求 team 共享工件存在
3. 若缺失 `DESIGN.md` / `theme.json`，仍按原规则处理

### Scenario 6: team 上下文中的阶段派工
输入：显式团队协作上下文 + 跨阶段任务
触发：`using-wisedev` -> `wisedev-orchestrator`
预期：
1. 优先进入控制层
2. 优先体现角色、共享工件、边界与阶段推进逻辑
3. 不直接越过 leader 走到下游产出型 skill

### Scenario 7: team 上下文中的单阶段执行
输入：显式团队协作上下文 + 已明确单阶段任务
预期：
1. skill 能识别角色边界
2. 若有共享工件路径，会优先回写共享工件
3. 若没有共享工件路径，仍可按原主路径输出

## 三、通过标准
只有当以下条件同时满足时，认为 smoke test 通过：
1. 原 skill 的独立使用方式仍然成立
2. team-aware 规则能在团队上下文中体现作用
3. 没有出现“必须有 AgentTeam 才能用原 skill”的情况
4. 没有出现“所有场景都被 reviewer / leader 规则拖重”的情况

## 四、建议记录方式
对每个场景记录：
- 输入描述
- 实际命中的 skill / 路由
- 是否符合预期
- 发现的问题
- 是否需要回改

## 五、建议结论格式
- Result: `<pass / conditional-pass / fail>`
- Findings:
  1. 
  2. 
- Follow-up:
  1. 
  2. 
