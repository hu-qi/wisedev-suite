---
name: wisedev-vue-mock-prototype
description: generate vue-based frontend prototype plans and code scaffolds with local mock services from chinese requirement, design, and openapi artifacts. use when the user needs a modern vue 3 plus vite plus typescript plus pinia plus router prototype, with realistic mock data, workflow states, and local run instructions for complex enterprise business demonstrations.
---

# 目标
在 `using-wisedev` 已确认这是明确单阶段任务，或 `wisedev-orchestrator` 已完成阶段判断后，再由本 Skill 处理当前阶段。

首次使用时，优先参考 `references/example-library.md`，并对照 `../shared/full-chain-examples/case-01-upload-delivery/05-vue-mock-prototype.md` 与 `06-vue-prototype-code/`。


输出一套可本地运行、可演示复杂流程、可与 OpenAPI 契约对齐的 Vue 原型方案与代码骨架。

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

# 脚本使用

- `scripts/init_vue_prototype.py`：初始化原型骨架目录和基础文件。
- `scripts/check_prototype_structure.py`：检查目录、路由、mock、页面、运行说明是否齐全。
- `scripts/scaffold_from_openapi.py`：根据 OpenAPI tags 和 paths 生成 mock 模块与 route 草稿。

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