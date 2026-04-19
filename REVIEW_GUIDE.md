# 审阅说明

建议按以下顺序审阅：

## 一、总控层
- `wisedev-orchestrator/SKILL.md`
- `wisedev-orchestrator/references/`
- `wisedev-orchestrator/templates/`

重点关注：
- 是否既有顾问式引导，又有足够强的阶段控制。
- 是否能清楚识别“当前阶段应该做什么、不应该做什么”。

## 二、需求与设计层
- `wisedev-meeting-to-spec/`
- `wisedev-requirement-spec/`
- `wisedev-design-doc/`

重点关注：
- 文风是否符合政企 / 国企正式文档。
- 模板是否足够覆盖常见项目章节。
- 缺失信息时是否会显式列出假设和未决问题。

## 三、契约与原型层
- `wisedev-openapi-contract/`
- `wisedev-vue-mock-prototype/`

重点关注：
- OpenAPI 模板是否足够约束接口命名、错误模型、分页、安全、示例。
- Vue 原型模板是否足够覆盖复杂业务演示、路由、状态、Mock 场景与本地运行。
- scripts 是否真能提升稳定性，而不是仅做占位。

## 四、共享资源
- `shared/`

重点关注：
- 追踪矩阵、术语表、审阅清单是否有助于跨阶段一致性。

## 完整链路样例

本套件已内置 `shared/full-chain-examples/`，其中 `case-01-upload-delivery` 提供从源输入到 Vue + mock 原型的完整样例链路，可作为总控 Skill 与子 Skill 的统一参考。


## 发布前整理（已执行）

- 已清理历史旧命名痕迹，仅保留 `wisedev-*`。
- 已删除无意义空目录，保留真实使用的 `scripts/` 与 `assets/`。
- 已将样例导航调整为 AI Agent 优先视角。
- 已统一 OpenAPI 在信息不完整时的输出顺序：先“假设与边界”，再 `openapi.yaml`。
