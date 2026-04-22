# WiseDev Skills Suite

一套面向“需求梳理 → 需求规格 → 概要/详细设计 → OpenAPI 契约 → 原型设计方向 → Vue + Mock 原型”的阶段化 Skills 方案。

说明：真正的 AI Agent 控制面位于 `using-wisedev/` 与 `wisedev-orchestrator/`，README 仅用于辅助理解，不作为主要行为规约入口。

## 设计目标

- 以中文业务场景为主，输出风格适配政企 / 国企项目文档。
- 以文档分析与产物生成为主，不依赖项目仓库、研发平台、MCP 或工作项系统。
- 通过总控 Skill 保证不同 AI 工具、多轮对话中的阶段一致性与产物一致性。
- 通过模板、检查清单、脚本和示例，减少模型自由发挥造成的漂移。

## 目录说明

- `using-wisedev/`：元 Skill，先判断是否应启用 WiseDev，并执行显式入口映射。
- `wisedev-orchestrator/`：总控 Skill，负责阶段判断、上下文标准化、路由与交接。
- `wisedev-meeting-to-spec/`：会议纪要/录音转写/混合材料 → 需求梳理。
- `wisedev-requirement-spec/`：需求规格说明书。
- `wisedev-design-doc/`：概要设计、详细设计。
- `wisedev-openapi-contract/`：OpenAPI YAML、Mock 示例、接口设计检查清单。
- `wisedev-prototype-design/`：原型设计方向、主题 token 包、设计评审。
- `wisedev-vue-mock-prototype/`：Vue 3 + Vite + TypeScript + Pinia + Router + 本地 Mock 原型。
- `shared/`：跨阶段通用模板与检查清单。

## 安装建议

推荐以 **bundle 安装** 的方式使用整个 `wisedev-suite`，而不是把每个 Skill 目录拆开单独安装。

原因：
- 多个 Skill 会共同引用 `shared/` 下的模板、检查清单和完整链路样例
- `case-01-upload-delivery` 等样例并不属于单一 Skill，而是整套方法论的公共参考
- `wisedev-prototype-design` 与 `wisedev-vue-mock-prototype` 之间存在显式交接关系，需要完整目录结构才能稳定工作

如果只安装单个 Skill 目录，`../shared/...` 这类共享资源路径很容易失效。

## 方法论来源

这套方案借鉴了分阶段技能编排的思路：先通过提问和澄清收敛需求，再输出可审阅的中间产物，再将中间产物交给下一个阶段继续处理。该分阶段 workflow 与 Superpowers 的“先规格化、再计划化、再分技能执行”的模式一致。

## 完整链路样例

本套件已内置 `shared/full-chain-examples/`，其中 `case-01-upload-delivery` 提供从源输入到 Vue + mock 原型的完整样例链路，可作为总控 Skill 与子 Skill 的统一参考。

## 推荐新链路

当任务目标是“高保真、可演示、风格更稳定的原型”时，推荐按下面顺序推进：

1. `wisedev-openapi-contract` 形成稳定契约
2. `wisedev-prototype-design` 产出设计方向与 theme package
3. `wisedev-vue-mock-prototype/scripts/scaffold_from_openapi.py` 生成模块、路由与 theme 接入草稿
4. `wisedev-vue-mock-prototype/scripts/init_vue_prototype.py` 初始化带 theme 的 Vue 原型骨架

如需一个现成示范，可直接参考：
- `shared/full-chain-examples/case-01-upload-delivery/12-theme-prototype-workflow.md`

## 实现关注点

如果使用者关心这套 Skill 的实现方式，应优先查看：

- `suite-architecture.md`：查看总控与子 Skill 的职责边界、阶段链路与交接规则。
- `shared/full-chain-examples/case-01-upload-delivery/`：查看完整链路如何从源输入逐步落到规格、设计、契约与原型。
- `wisedev-openapi-contract/scripts/` 与 `wisedev-vue-mock-prototype/scripts/`：查看当前已提供的自动化脚本范围。
- `wisedev-prototype-design/`：查看设计方向、theme package 与评审模板如何约束下游原型。
