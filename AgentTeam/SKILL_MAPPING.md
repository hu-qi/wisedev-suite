# AgentTeam 与 WiseDev Skills 映射说明

## 目标
本文件用于说明 `AgentTeam/` 下的长期协作团队设计，如何与现有 `wisedev-*` skills 对接。

目标不是替换现有 skills，而是：
1. 保留现有阶段化技能资产
2. 将技能资产映射到长期角色
3. 让 team leader、成员、reviewer 能围绕共享工件协作

## 一、角色与 Skills 映射

### 1. Team Leader
- 主要技能：
  - `using-wisedev`
  - `wisedev-orchestrator`
- 作用：
  - 判断是否进入 WiseDev 工作流
  - 识别当前阶段
  - 生成上下文包任务
  - 指派阶段任务
  - 决定何时进入 reviewer 审查
  - 输出阶段交接决策

### 2. Product Analyst
- 主要技能：
  - `using-wisedev`
  - `wisedev-meeting-to-spec`
  - `wisedev-requirement-spec`
- 作用：
  - 从原始输入提炼需求事实
  - 维护上下文包
  - 输出需求梳理与需求规格说明书

### 3. Solution Architect
- 主要技能：
  - `wisedev-design-doc`
- 作用：
  - 输出概要设计 / 详细设计
  - 维护架构与模块边界
  - 向 API 与原型阶段提供结构约束

### 4. API Designer
- 主要技能：
  - `wisedev-openapi-contract`
- 作用：
  - 产出 OpenAPI YAML
  - 维护接口契约、Mock 示例与 API 检查清单

### 5. UX Designer
- 主要技能：
  - `wisedev-prototype-design`
- 作用：
  - 输出原型方向、信息架构、设计规则、主题 token

### 6. Frontend Engineer
- 主要技能：
  - `wisedev-vue-mock-prototype`
  - `wisedev-prototype-design`
- 作用：
  - 基于 API 契约和设计约束落地 Vue + Mock 原型

### 7. Reviewer
- 主要技能：
  - `using-wisedev`
  - `shared`
- 作用：
  - 不负责主产物创作
  - 负责检查共享工件间的一致性、完整性、越界与追踪关系

## 二、推荐的模板引用关系

### Leader 相关
以下能力建议显式引用：
- `shared/templates/team-task-assignment.md`
- `shared/templates/leader-acceptance.md`
- `shared/templates/team-daily-workflow.md`
- `shared/templates/stage-handoff.md`

### Product Analyst 相关
以下能力建议显式引用：
- `shared/templates/context-package.md`
- `shared/templates/decision-log.md`
- `shared/templates/stage-handoff.md`

### Solution Architect 相关
以下能力建议显式引用：
- `shared/templates/decision-log.md`
- `shared/templates/stage-handoff.md`

### API Designer 相关
以下能力建议显式引用：
- `shared/templates/decision-log.md`
- `shared/templates/stage-handoff.md`

### UX Designer / Frontend Engineer 相关
以下能力建议显式引用：
- `shared/templates/decision-log.md`
- `shared/templates/stage-handoff.md`

### Reviewer 相关
以下能力建议显式引用：
- `shared/templates/review-report.md`
- `shared/templates/leader-acceptance.md`
- `shared/templates/decision-log.md`

## 三、哪些 Skills 需要调整提示词

### 1. `using-wisedev`
建议新增 team 感知规则：
- 当运行环境为 team 协作模式时，不只判断“是否启用 WiseDev”，还要判断当前请求更适合哪个团队角色处理。
- 当任务需要阶段推进时，优先交由 team leader 决定负责人，而不是直接将任务绑定到某个子 skill。

### 2. `wisedev-orchestrator`
建议从“唯一总控 skill”调整为“leader 的流程控制能力”。
需要补充：
- 如何基于共享工件派工
- 如何定义输入工件 / 输出工件
- 如何请求 reviewer 审查
- 如何在局部并行时控制边界

### 3. `wisedev-meeting-to-spec`
建议补充：
- 输出不是停留在聊天文本，而是要回写 `context-package.md`、`requirement-brief.md` 等共享工件
- 不能越界产出设计 / API / 原型

### 4. `wisedev-requirement-spec`
建议补充：
- 输出需对齐共享工件中的稳定事实
- 变更关键需求范围时，要更新 decision log 或 open questions

### 5. `wisedev-design-doc`
建议补充：
- 所有设计结论都要明确其来源于哪一版需求工件
- 若发现需求存在不稳定点，应显式回推而非私自修正

### 6. `wisedev-openapi-contract`
建议补充：
- 接口契约必须标明其依赖的需求与设计输入版本
- 若关键字段来自假设，必须显式标记

### 7. `wisedev-prototype-design`
建议补充：
- 原型方向必须引用已验收需求与契约
- 不擅自创造新的业务范围

### 8. `wisedev-vue-mock-prototype`
建议补充：
- 代码与 mock 结构必须围绕共享工件推进
- 如发现 API/设计问题，应反馈给 leader 或 reviewer，而不是自行重定业务规则

## 四、建议新增的 Team 协作约束

1. 每个角色的正式输出都必须落到共享工件，而不是仅出现在回复文本中。
2. leader 派工时必须显式给出：
   - 负责人
   - 输入工件
   - 输出工件
   - 越界边界
   - 完成标准
3. reviewer 的反馈必须引用具体工件。
4. 任意成员发现上游不稳定时，应中止越级推进，并回写 open questions / decision log。
5. team 模式下，skills 不应默认把“当前回复”当作最终交付，而应优先更新共享工件。

## 五、建议下一步

1. 为关键 skills 增加 team-aware 规则说明
2. 为 leader / reviewer 增加对模板的显式引用
3. 在后续实现中，把 `AgentTeam/shared/templates/` 作为 team 运行时的规范输入
