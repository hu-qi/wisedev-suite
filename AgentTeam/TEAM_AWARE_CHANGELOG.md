# Team-Aware Changelog

## 目的
本文件记录 `huqi/team-aware` 分支中已完成的 team-aware 改造内容、兼容策略和后续待办，帮助后续 review、验证和合并时快速理解这条分支做了什么。

## 一、改造目标
本轮改造的目标不是把 `wisedev-suite` 变成 team-only 套件，而是：
1. 保留原有单技能、单阶段使用方式
2. 为长期协作团队场景增加兼容的 team-aware 分支
3. 将团队协作能力优先收口到控制层
4. 让子 skill 在 team 场景中更守纪律、更适合共享工件协作

## 二、已新增的 AgentTeam 设计包
新增目录：`AgentTeam/`

主要新增内容：
- `README.md`
- `ROLE_SPEC.md`
- `SKILL_MAPPING.md`
- `TEAM_ADOPTION_PLAN.md`
- `TEAM_RUNTIME_RULES.md`
- `IMPLEMENTATION_TASKS.md`
- `COMPATIBILITY_GUIDELINES.md`
- `leader-persona.md`
- `reviewer-persona.md`
- `shared-workspace-layout.md`
- `team-config.example.yaml`
- `shared/templates/*`

这些文件提供了：
- 团队角色说明
- 共享工件目录规范
- 派工 / 审查 / 验收 / 交接模板
- team 接入路线图
- 兼容改造原则

## 三、已完成的 Skill 改造

### 1. 控制层 Skills
已修改：
- `using-wisedev/SKILL.md`
- `wisedev-orchestrator/SKILL.md`

改造内容：
- 增加 team-aware 识别规则
- 增加 team 上下文下的控制层逻辑
- 增加 leader 化派工 / 验收 / 审查意识
- 将 `AgentTeam/` 下的规范文档接入为控制面参考资源

### 2. 中风险子 Skills
已修改：
- `wisedev-meeting-to-spec/SKILL.md`
- `wisedev-design-doc/SKILL.md`
- `wisedev-prototype-design/SKILL.md`

改造内容：
- 增加兼容原则
- 增加轻量 team-aware 规则
- 增加共享工件回写优先级
- 增加角色边界说明
- 增加上游不稳定时的回推规则

### 3. 高风险产出型 Skills
已修改：
- `wisedev-requirement-spec/SKILL.md`
- `wisedev-openapi-contract/SKILL.md`
- `wisedev-vue-mock-prototype/SKILL.md`

改造内容：
- 增加兼容原则
- 增加轻量 team-aware 规则
- 增加共享工件回写意识
- 增加角色边界说明
- 明确在 team 场景中不要私自定案或越界修正上游结论

## 四、兼容策略
本轮改造采用以下兼容策略：

1. 原 skill 默认语义不变
- 单阶段任务仍可直接调用原 skill
- 非 team 场景不应被强制拉入长期团队协作规则

2. team-aware 仅是增强分支
- 当检测到 leader / reviewer / shared artifacts / handoff 等上下文时，启用 team-aware 规则
- 否则沿用原工作流

3. 控制层强感知，子 skill 轻感知
- `using-wisedev` 与 `wisedev-orchestrator` 强感知 team
- 子 skill 只补共享工件、角色边界与回推能力

4. 不强制依赖 `AgentTeam/`
- 文档中增加对 `AgentTeam/` 资源的引用
- 但不将其写成“没有就失败”的必需依赖

## 五、已形成的阶段性结果
到当前为止，这条分支已经完成：
1. AgentTeam 设计基础设施
2. 控制层 team-aware 改造
3. 中风险子 skill 的轻量兼容增强
4. 高风险产出型 skill 的轻量兼容增强

可以认为：
- 第一轮 team-aware 规则接入已完成
- 套件已具备“在团队场景下更守纪律”的能力
- 原 skill 独立使用方式原则上仍应可保留

## 六、当前尚未完成的内容
以下内容仍未落实到真实运行层：

1. 尚未验证所有 skill 在非 team 场景下的回归行为
2. 尚未将这些规则真正接入 AgentTeam runtime
3. 尚未做共享工件初始化与目录自动化
4. 尚未定义 team 模式下的真实文件写入实现策略
5. 尚未做 reviewer 驱动的自动闭环验证

## 七、建议的下一步

### 短期建议
1. 做一轮人工 review，检查各 skill 的兼容写法是否足够稳
2. 做一次 bundle 级 smoke test，确认原 skill 仍可单独使用
3. 评估是否需要为关键 skill 增加“team-aware 示例”

### 中期建议
1. 将 `AgentTeam/shared/templates/` 与现有 skill 模板体系建立更明确的引用关系
2. 在真实 team runtime 中试点：
   - `team_leader`
   - `product_analyst`
   - `api_designer`
   - `frontend_engineer`
   - `reviewer`
3. 验证共享工件是否能真正成为唯一正式事实来源

## 八、对应提交
当前已形成两个主要提交：

1. `bfe7617`
- `Add AgentTeam design package and team-aware control layer`

2. `c267469`
- `Add team-aware compatibility to output skills`

## 九、一句话总结
本分支完成的是“兼容式 team-aware 改造第一阶段”：

保留原 skill 的独立可用性，在控制层外包一层长期协作团队能力，并让子 skill 在 team 场景中更适合共享工件、角色边界和审查闭环。
