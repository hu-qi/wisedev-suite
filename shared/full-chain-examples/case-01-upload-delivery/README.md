# Case-01 上传下达模块标杆样例

本案例用于演示“上传下达模块”从原始需求输入到会议梳理、需求规格、设计文档、OpenAPI 契约、Vue + mock 原型，再到演示脚本和场景切换机制的完整闭环。

在当前版本中，本案例还可用于演示新的“原型设计方向 → theme package → Vue 原型骨架”链路。

## 目录说明
- `00-source-input.md`：原始输入
- `01-meeting-to-spec.md`：会议纪要/转写整理结果
- `02-requirement-spec.md`：需求规格说明书样例
- `03-design-doc.md`：概要与详细设计样例
- `04-openapi.yaml`：契约样例
- `05-vue-mock-prototype.md`：原型设计说明
- `06-vue-prototype-code/`：可本地运行的 Vue 原型代码骨架
- `07-demo-script.md`：标准演示脚本
- `08-role-based-walkthrough.md`：角色化走查脚本
- `09-screen-spec.md`：页面截图约定
- `10-page-wireframe-rules.md`：页面线框与布局规则
- `11-mock-scenario-switch.md`：mock 场景切换机制
- `12-theme-prototype-workflow.md`：theme package 驱动的原型脚手架示例

## 当前标杆包能力
- 文档链路已覆盖从需求梳理到原型说明的完整闭环。
- `06-vue-prototype-code/` 已提升为更高保真的演示原型，并实际通过 `npm run build`。
- 场景切换机制、页面截图约定和演示脚本已经接入，适合做跨模型复刻与方案演示。

## 推荐阅读顺序
1. 先看 `00` 到 `05`，理解业务与产物如何逐层收敛。
2. 再看 `06-vue-prototype-code/`，理解如何将契约和原型说明落成可运行骨架。
3. 最后看 `07` 到 `11`，理解如何让不同 AI 工具稳定复刻同一条演示链路。
4. 如需验证新的主题化原型链路，再看 `12-theme-prototype-workflow.md`。

## 关键价值
- 用完整链路样例稳定总控与子 Skill 的阶段判断。
- 用页面约定和场景切换机制稳定不同模型生成的原型结构。
- 用演示脚本稳定业务讲述路径，减少“今天能讲、明天讲偏”的问题。
- 用更高保真的页面与交互提升方案评审和业务汇报时的演示质量。
