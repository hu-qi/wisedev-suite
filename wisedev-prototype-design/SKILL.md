---
name: wisedev-prototype-design
description: recommend contrasting prototype design directions, generate theme token packages, and critique visual outputs for chinese enterprise-facing prototypes. use when the user needs design direction, visual style comparison, color schemes, prototype themes, or design review before or after vue prototype generation.
---

# 目标

在 `wisedev-orchestrator` 已判断进入原型相关阶段后，用本 Skill 补上“设计前置层”。

输出不是最终 Vue 代码，而是：
- 3 套差异化设计方向
- 可传递给下游原型阶段的设计系统产物
- 页面级布局约束与视觉说明
- 对现有原型草稿的设计评审与快速修复建议

# 适用时机

- 用户要求“推荐设计方向 / 视觉风格 / 配色方案 / 原型主题”
- 已有需求规格、设计文档或 OpenAPI，想先收敛原型视觉策略
- Vue 原型已生成，但需要设计评审和 Quick Wins

# 核心原则

1. 约束设计哲学，而不是只列形式元素。
2. 默认给出 3 套有区分度的方向，避免“都差不多”。
3. 输出要能被下游消费，必须同时兼顾 AI 可读性与脚本可消费性。
4. 设计评审要指出问题，也要给出可执行修复值。
5. 默认适配中文政企 / 国企业务演示语境，但允许在此基础上做克制的差异化。

# 输入前提

理想输入至少包含以下之一：
- 需求规格说明书
- 设计文档
- OpenAPI 契约
- 原型页面草稿 / 截图 / Vue 代码骨架

如果上游材料不足，允许基于“业务目标 + 目标受众 + 演示场景”先给方向草案，但必须明确写出假设。

# 标准工作流

## Phase 1：重述设计任务

用 100-180 字重述：
- 谁看
- 要传达什么
- 适合什么演示场景
- 为什么此时需要设计方向而不是直接出代码

以“基于这个理解，我为你准备了 3 个设计方向”结尾。

## Phase 2：推荐 3 套设计方向

默认建议 3 个方向，并尽量满足：
- 气质上有明显区分
- 每个方向都要说明为什么适合当前业务
- 每个方向都要产出可执行的主题包，不只写概念词
- 避免出现“同一风格小修小改后当作多套方案”的伪对比

每个方向至少包含：
- `direction_name`
- `theme_id`
- `design_philosophy`
- `why_fit`
- `tone_keywords`
- `color_roles`
- `type_system`
- `component_traits`
- `page_guidelines`
- `risks`

可参考的流派池：
- `enterprise_order`：秩序、可信、编辑式信息组织，适合正式汇报
- `data_command`：控制台、信号感、行动导向，适合调度/监管
- `minimal_refined`：克制、留白、精致，适合高级简报
- `experimental_system`：更强结构张力和视觉记忆点，适合创新方案展示
- `modern_east`：温润、节制、东方当代感，适合差异化表达

在 WiseDev 里，默认可从中收敛为 3 个优先方向：
- `stable_enterprise`：稳健、专业、低风险，适合领导汇报
- `data_command`：更强看板感和控制台感，适合调度/监管/中台
- `modern_east`：克制但有辨识度，适合需要高级感和差异化的方案

若任务明确要求更先锋或更极简，可把其中一个方向替换为：
- `minimal_refined`
- `experimental_system`

## Phase 3：生成主题包

必须输出至少 1 套推荐主题包，可同时附带 3 套完整包。

主产物与辅助产物的关系如下：
- `DESIGN.md`：主交付，供 AI 工具与人协同阅读
- `theme.json`：辅助交付，供脚本、模板和原型初始化流程稳定消费

每套主题包至少包含：
- 基础颜色 token
- 字体与字号层级
- 圆角、阴影、边框
- 布局密度
- Hero、KPI 卡、列表、详情、表单、时间轴的样式约束
- 图标与插图建议
- 禁区说明

推荐输出：
- 1 份 `DESIGN.md`
- 1 份 `theme.json`

其中：
- `DESIGN.md` 负责表达设计哲学、规范、组件模式、Do/Don't
- `theme.json` 负责表达结构化 token 与脚本必需字段

`theme.json` 格式优先参考 `templates/theme-schema.json`。

若用户尚未做选择，可优先输出：
- 3 套方向摘要
- 1 套主推主题包
- 另外 2 套的轻量主题说明

若用户已明确要比较，也可输出 3 套完整主题包。

## Phase 4：页面级设计约束

对原型常见页面给出规则：
- Dashboard
- List
- Detail
- Form
- Workflow / Timeline

每页写清：
- 信息层级
- 栅格建议
- 强调区与留白区
- 组件优先级

## Phase 5：设计评审

当用户已有页面草稿或代码时，输出设计评审报告。

评分维度：
1. 哲学一致性
2. 视觉层级
3. 细节执行
4. 功能服务性
5. 区分度

必须给出：
- 总体评分
- Keep
- Fix
- Quick Wins


# 下游交接要求

交给 `wisedev-vue-mock-prototype` 时，至少传递：
- 选定的 `theme_id`
- `DESIGN.md`
- `theme.json`
- 页面级设计约束
- 禁区与可替代方案

# 输出边界

- 本 Skill 不直接替代 `wisedev-vue-mock-prototype` 写完整工程代码。
- 本 Skill 不生成生产级视觉规范系统。
- 不要为了“有设计感”牺牲业务信息密度与政企语境可接受性。

# 可用资源

- `references/design-directions-guide.md`
- `references/critique-guide.md`
- `references/example-library.md`
- `scripts/render_design_md.py`
- `examples/design-md/`
- `templates/DESIGN.md`
- `templates/design-directions.md`
- `templates/design-critique.md`
- `templates/theme-schema.json`
- `assets/themes/enterprise-calm.json`
- `assets/themes/data-command.json`
- `assets/themes/modern-east.json`
