# Case-01 Mock 场景切换机制

## 1. 目的
用统一命名的场景切换来稳定演示复杂业务，不让不同 AI 工具自由发散业务状态。

## 2. 统一场景
- `happy_path`：标准推进，主要事项按时推进。
- `delayed_tasks`：存在逾期与催办场景。
- `returned_for_revision`：周报、报表出现退回补正。
- `cross_department_coordination`：横向协同处于处理中。
- `closed_archive`：事项已办结归档，适合展示审计闭环。

## 3. 切换位置
- 首页看板右上角
- 全局布局头部

## 4. 切换效果
场景切换后，以下数据应同步变化：
- 首页指标
- 风险事项
- 调度指令状态与时间轴
- 周报状态与退回意见
- 协助申请状态与时间轴
- 审计摘要中的最新动作

## 5. 演示要求
- 默认场景使用 `happy_path`
- 演示逾期时切到 `delayed_tasks`
- 演示退回补正时切到 `returned_for_revision`
- 演示横向协同时切到 `cross_department_coordination`
- 演示全流程闭环时切到 `closed_archive`
