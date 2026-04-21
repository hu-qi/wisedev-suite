# Suite Architecture

## 元控制层

- `using-wisedev`：元 Skill，负责激活判断与显式入口映射。
- `wisedev-orchestrator`：总控 Skill，负责阶段判断、上下文包、唯一子 Skill 路由、阶段交接。

# 套件架构说明

## 0. 架构定位

本套件采用“总控 Skill + 子 Skill”的阶段化结构。

- `wisedev-orchestrator` 负责阶段判断、上下文标准化、路由和交接控制。
- 子 Skill 负责单一阶段的正式产物输出。
- `templates/`、`references/example-library.md`、`shared/full-chain-examples/` 共同约束输出稳定性。

实现上，真正的控制面在 `wisedev-orchestrator/SKILL.md` 与其 `references/meta-workflow.md`，而不是根 README。

## 1. 核心原则

1. 顾问式引导优先：先澄清、再归纳、后产出。
2. 严格阶段化：默认只做当前阶段，不默认跨阶段一口气输出到底。
3. 产物驱动交接：每一阶段都必须形成可审阅的文档或代码草稿。
4. 追踪键一致：需求编号、模块编号、API 标签、页面模块名之间保持映射。
5. 中文业务表达 + 英文工程标识：文档模板中文化，代码与 OpenAPI 结构英文为主。

## 2. 阶段链路

### 阶段 A：输入归一化
由 `wisedev-orchestrator` 完成：
- 识别输入类型：口头需求、会议纪要、录音转写、混合材料、局部设计等。
- 形成 `上下文包`：背景、角色、场景、范围、约束、假设、未决问题。

### 阶段 B：需求梳理
由 `wisedev-meeting-to-spec` 完成：
- 从讨论材料中提炼事实、需求点、业务规则、风险和遗留问题。

### 阶段 C：需求规格说明书
由 `wisedev-requirement-spec` 完成：
- 形成正式的需求规格说明书、范围定义、功能点、验收标准。

### 阶段 D：概要/详细设计
由 `wisedev-design-doc` 完成：
- 形成模块分解、角色权限、流程、状态机、数据对象和异常处理设计。

### 阶段 E：API 契约
由 `wisedev-openapi-contract` 完成：
- 输出单文件 `openapi.yaml`、Mock 示例、接口检查清单。

### 阶段 F：原型设计方向
由 `wisedev-prototype-design` 完成：
- 输出 3 套可对比的设计方向，而不是直接跳进单一视觉方案。
- 形成可落地的主题 token、布局约束、页面气质说明和适用场景。
- 对后续原型草图或代码成品给出设计评审与 Quick Wins。

### 阶段 G：Vue + Mock 原型
由 `wisedev-vue-mock-prototype` 完成：
- 输出可本地运行的 Vue 原型骨架、路由、页面模块、mock 服务、演示说明。

## 3. 推荐使用节奏

- 第一次对话：只做输入归一化 + 阶段判断。
- 第二次对话：产出当前阶段的正式草稿。
- 第三次对话：根据审阅意见修订。
- 第四次对话：交接给下一阶段 Skill。
