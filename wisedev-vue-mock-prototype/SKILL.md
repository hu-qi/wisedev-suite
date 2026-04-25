---
name: wisedev-vue-mock-prototype
description: generate vue-based frontend prototype plans and code scaffolds with local mock services from chinese requirement, design, and openapi artifacts. use when the user needs a modern vue 3 plus vite plus typescript plus pinia plus router prototype, with realistic mock data, workflow states, and local run instructions for complex enterprise business demonstrations.
---

# 目标
在 `using-wisedev` 已确认这是明确单阶段任务，或 `wisedev-orchestrator` 已完成阶段判断后，再由本 Skill 处理当前阶段。

首次使用时，优先参考 `references/example-library.md`，并对照 `../shared/full-chain-examples/case-01-upload-delivery/05-vue-mock-prototype.md` 与 `06-vue-prototype-code/`。默认应先由 `wisedev-prototype-design` 提供 `DESIGN.md` 与 `theme.json`，再由本 Skill 消费其 token、布局约束与页面气质说明。


输出一套可本地运行、可演示复杂流程、可与 OpenAPI 契约对齐的 Vue 原型方案与代码骨架。

# 兼容原则

1. 本 Skill 必须继续兼容原有单阶段、独立输出 Vue + Mock 原型的使用方式。
2. team-aware 能力仅作为增强分支，不替换当前“直接输出原型方案与代码骨架”的主路径。
3. 若未检测到 team 协作上下文，沿用原有技术栈、脚本和输出范围。
4. 不得因为 team-aware 规则而强制依赖 leader、reviewer、共享工件或 `AgentTeam/` 目录。

# Team-aware 轻量规则

若处于 team 协作上下文，则增加以下轻量规则：
1. 默认将本 Skill 视作 `frontend_engineer` 的阶段执行能力。
2. 若已提供共享工件路径，应优先基于已验收的契约与设计约束输出，并尽量回写：
   - `prototype/`
   - `mock/`
   - `prototype-readme.md`
   - `stage-handoff.md`
3. 若发现上游设计、契约或需求之间存在明显冲突，应先显式反馈问题，不要自行重定义业务范围。
4. 本 Skill 不应替代 `wisedev-prototype-design` 做完整设计哲学收敛；若缺少 `DESIGN.md` / `theme.json`，应明确标注“跳过设计前置层”的假设。
5. 在 team 场景中，优先保证下游演示原型可消费共享工件，而不是只追求聊天输出好看。

# 默认技术栈

- Vue 3
- Vite
- TypeScript
- Vue Router
- Pinia
- 本地 Mock Service Layer（默认 `src/mock/`）
- 可选接入 MSW 思路，但默认保持轻量本地可运行

# 输出范围

必须至少包含：
- 项目结构建议
- `package.json` 草稿
- 路由表
- 页面清单
- 功能模块清单
- Store / 状态结构建议
- Mock 模块拆分方案
- Theme / 样式 token 接入方案
- 核心页面代码样板
- 场景化 mock 数据
- 本地运行说明
- 演示 walkthrough

# 设计规则

- 以“业务功能模块”组织目录，而不是只按页面堆砌。
- mock 接口命名与 OpenAPI 保持一致。
- mock 数据必须覆盖：成功、空态、处理中、驳回、部分完成、超时等关键演示场景。
- 页面命名、路由命名、模块命名必须稳定，避免 `Page1`、`TempView` 之类名称。
- 目标是“演示型可运行原型”，不是生产级 UI 完整实现。
- 若存在多套设计方向，必须先明确当前选用的 theme id，再开始落代码。
- 若上游提供 theme package，应通过 `src/theme/` 统一接入，避免把颜色、圆角、阴影散落在各页面中硬编码。
- 若未提供 `DESIGN.md` / `theme.json`，必须明确写出当前是在“跳过设计前置层”的假设下生成原型。
- 在 team 场景中，不要通过前端实现去偷偷修正需求或接口定义。

# 脚本使用

- `scripts/init_vue_prototype.py`：初始化原型骨架目录和基础文件。
- `scripts/init_vue_prototype.py <target> [theme-json]`：初始化原型骨架目录；若提供 `wisedev-prototype-design` 生成的主题包 JSON，则同步生成 `src/theme/`。
- `scripts/check_prototype_structure.py`：检查目录、路由、mock、页面、运行说明是否齐全。
- `scripts/scaffold_from_openapi.py <openapi.yaml> [theme-json] [--write target]`：根据 OpenAPI tags 和 paths 生成 mock 模块、route 草稿、theme 接入提示；必要时直接写出 `src/modules/*` 骨架。

# 高质量样例优先

优先参考 `references/example-library.md` 和 `references/examples/` 下的页面映射、场景矩阵与运行方式，确保原型输出更稳定、更接近可演示状态。

# 可用资源

- `references/vue-project-conventions.md`
- `references/mock-service-patterns.md`
- `references/page-module-guidelines.md`
- `templates/package-json-template.md`
- `templates/vite-config-template.ts`
- `templates/tsconfig-template.json`
- `templates/router-template.ts`
- `templates/store-template.ts`
- `templates/theme-tokens-template.ts`
- `templates/theme-css-template.css`
- `templates/app-shell-template.vue`
- `templates/layout-template.vue`
- `templates/list-page-template.vue`
- `templates/detail-page-template.vue`
- `templates/form-page-template.vue`
- `templates/dashboard-page-template.vue`
- `templates/workflow-page-template.vue`
- `templates/mock-module-template.ts`
- `templates/mock-dataset-template.json`
- `templates/mock-scenario-matrix.md`
- `templates/local-run-readme.md`
- `templates/prototype-walkthrough.md`
- `templates/page-inventory.md`
- `templates/ui-module-map.md`
- `../AgentTeam/shared/templates/decision-log.md`
- `../AgentTeam/shared/templates/stage-handoff.md`
