---
name: wisedev-openapi-contract
description: generate openapi yaml contracts from requirement and design artifacts. use when the user needs chinese business requirements converted into mock-ready api paths, request and response schemas, error models, pagination, security, and example payloads in a single self-contained openapi yaml file.
---

# 目标
在 `using-wisedev` 已确认这是明确单阶段任务，或 `wisedev-orchestrator` 已完成阶段判断后，再由本 Skill 处理当前阶段。

首次执行本阶段任务时，优先参考 `references/example-library.md`；若输入与“上传下达模块”高度相似，再对照 `../shared/full-chain-examples/case-01-upload-delivery/04-openapi.yaml` 的本阶段样例。


生成可审阅、可 Mock、适合前端原型消费的单文件 `openapi.yaml`。

# 基本原则

- 契约先于实现。
- 端点按业务能力建模，不按数据库表名直接暴露。
- 输出单文件自包含 YAML，便于阅读、版本管理与原型消费。
- 必须为前端原型准备足够的示例数据与错误响应模型。

# 输出要求

至少包含：
- `openapi: 3.x`
- `info`、`servers`
- 业务标签 `tags`
- `paths`
- `components.schemas`
- `components.responses`
- `components.parameters`
- `components.securitySchemes`
- 示例 `examples`
- 标准错误模型
- 分页与筛选参数约定

# 编写规则

- 路径命名资源化、复数化，避免动词化。
- 查询参数、schema 字段、枚举名遵循统一命名风格。
- 所有重要操作应声明成功响应与失败响应。
- 缺失信息较多时，必须先输出固定标题“假设与边界”，列出缺失信息、默认假设与不覆盖范围，然后再输出完整 `openapi.yaml`。

# 脚本使用

- 使用 `scripts/validate_openapi.py` 对生成的 YAML 做最小校验。
- 使用 `scripts/scaffold_mock_examples.py` 基于路径和 schema 生成 mock 示例草稿。

# 高质量样例优先

优先参考 `references/example-library.md` 和 `references/examples/` 下的接口片段，保持业务导向路径命名、统一错误模型和 mock 友好示例。

# 可用资源

- `references/api-style-guide.md`
- `references/error-model.md`
- `references/schema-conventions.md`
- `templates/openapi.yaml`
- `templates/paths-template.yaml`
- `templates/schema-template.yaml`
- `templates/error-response-template.yaml`
- `templates/pagination-template.yaml`
- `templates/security-scheme-template.yaml`
- `templates/operation-example-template.yaml`
- `templates/api-design-checklist.md`

## 输出顺序

信息完整时，直接输出 `openapi.yaml`。

信息不完整时，严格按以下顺序输出：

1. `假设与边界`
2. `openapi.yaml`

不得将假设内容混入 YAML 注释或散落到 YAML 后部。
