# Compatibility Guidelines

## 目的
本文件用于约束 WiseDev Suite 在引入 team-aware 能力时，尽量不破坏原有 skill 的独立使用方式。

核心原则：
- 不把原 skill 强制改造成 team-only skill
- 不让 team 运行时约束破坏单阶段、单技能、非 team 场景的可用性
- 优先改控制层，谨慎改产出层

## 一、总体策略

不是“把原 skill 改造成 team skill”，而是：

1. 保留原 skill 的主语义
2. 给原 skill 增加 team 场景下的增强分支
3. 将 team 协作规则尽量收口在控制层
4. 让共享工件、reviewer、leader 派工成为可增强能力，而不是硬依赖

## 二、低风险改造区

以下区域适合优先改造：

### 1. `AgentTeam/`
- 风险等级：低
- 原因：新增设计资料、模板、规范，不影响原 skill 行为
- 建议：可以持续扩展

### 2. `using-wisedev/SKILL.md`
- 风险等级：低
- 原因：它本来就是入口判断层
- 适合增加：
  - team-aware 入口识别
  - “在 team 场景下由 leader 决定负责人”的规则
  - 不改变原有单阶段 / 跨阶段判断能力

### 3. `wisedev-orchestrator/SKILL.md`
- 风险等级：低到中
- 原因：它本来就是流程控制层
- 适合增加：
  - leader 派工规则
  - 共享工件输入 / 输出约束
  - reviewer 触发与 leader 验收规则
  - 阶段交接强化

## 三、中风险改造区

以下 skills 可以增加 team-aware 规则，但应尽量保持原主流程不变：

### 1. `wisedev-meeting-to-spec/SKILL.md`
- 风险等级：中
- 可加内容：
  - 若存在共享工件，则优先回写 `context-package.md` / `requirement-brief.md`
  - 若运行在 team 角色上下文中，遵守角色边界
- 不建议改动：
  - 其当前“单阶段直接输出需求梳理稿”的核心能力

### 2. `wisedev-design-doc/SKILL.md`
- 风险等级：中
- 可加内容：
  - 明确引用上游需求工件
  - 检测不稳定输入时回推而非私改
- 不建议改动：
  - 其当前单阶段正式设计输出逻辑

### 3. `wisedev-prototype-design/SKILL.md`
- 风险等级：中
- 可加内容：
  - 明确以已验收需求 / 契约为输入
  - 引导输出到共享工件
- 不建议改动：
  - 原有设计方向输出主路径

## 四、高风险改造区

以下 skills 是“产出型核心 skill”，一旦硬改，很容易破坏原有使用方式：

### 1. `wisedev-requirement-spec/SKILL.md`
- 风险等级：高
- 风险原因：
  - 当前直接面向正式需求规格输出
  - 很适合作为单独使用 skill
- 高风险改法：
  - 强制依赖 team 共享工件才能工作
  - 强制 reviewer 或 leader 前置
  - 强制派工后才能输出
- 建议：
  - 仅增加“若存在共享工件则写回”的兼容规则
  - 保留独立输出 SRS 的能力

### 2. `wisedev-openapi-contract/SKILL.md`
- 风险等级：高
- 风险原因：
  - 当前单阶段目标非常明确：直接输出 `openapi.yaml`
- 高风险改法：
  - 改成必须依赖 team runtime
  - 改成必须先走 leader / reviewer 才能工作
- 建议：
  - 只补充“team 场景下引用共享工件”的规则
  - 不破坏独立 OpenAPI 产出路径

### 3. `wisedev-vue-mock-prototype/SKILL.md`
- 风险等级：高
- 风险原因：
  - 当前是完整的原型产出型 skill
  - 很多用户会希望独立使用它
- 高风险改法：
  - 将其绑定成必须有设计前置层、必须有 team 共享工件、必须 reviewer 通过后才能产出
- 建议：
  - 保留原有独立使用能力
  - team 下只增强“引用共享工件”“遵守角色边界”“反馈上游问题”三类规则

## 五、兼容改造原则

### 原则 1：默认行为不变
原 skill 在非 team 场景中的默认行为应保持不变。

### 原则 2：team 是增强分支，不是唯一分支
推荐写法：
- 如果检测到 team 协作上下文，则启用共享工件 / 角色边界 / 审查约束
- 否则保持原有单 skill 工作流

### 原则 3：控制层强感知，子 skill 轻感知
- `using-wisedev`、`wisedev-orchestrator` 可以强感知 team
- 子 skill 只需要最小程度感知 team

### 原则 4：共享工件应可选增强
共享工件应当是“可用则用”，不是“没有就失败”。

### 原则 5：reviewer 规则不要直接替代子 skill 主流程
reviewer 应由 leader / orchestrator 触发，而不是让每个子 skill 默认等待 reviewer。

### 原则 6：不要在子 skill 中硬编码 `AgentTeam/` 为必需目录
否则 bundle 外、局部安装、单 skill 使用场景都会受影响。

## 六、建议的改造顺序

### 第一步：改控制层
1. `using-wisedev/SKILL.md`
2. `wisedev-orchestrator/SKILL.md`

### 第二步：对子 skill 做最小 team-aware 增强
建议只加：
1. 若存在共享工件，则优先写回
2. 若在 team 角色上下文，则遵守角色边界
3. 若发现上游输入不稳定，则显式回推 open questions / decision log

### 第三步：逐个验证原 skill 是否仍可独立使用
每改一个 skill，都要验证：
1. 脱离 team 还能不能像以前一样用
2. 是否仍能完成原本的单阶段产物输出
3. 是否没有被共享工件或 reviewer 规则绑死

## 七、建议新增验证清单

每次改 skill 后，至少检查：
1. 单阶段直出能力是否仍在
2. 不依赖 `AgentTeam/` 是否仍可工作
3. 文档没有把 team 模式写成唯一模式
4. team-aware 规则是增强项，不是强制项

## 八、一句话准则

保留原 skill 的独立可用性，在控制层外包一层长期协作团队能力，而不是把所有 skill 硬改成 team-only。
