# 高质量样例库：Vue + Mock 原型

## 样例 1：复杂业务原型的最小可跑交付

### 输入前提
已有需求规格或 OpenAPI 契约，需要输出一个可本地运行、可演示主要流程的 Vue 原型。

### 稳定输出顺序
1. 项目结构
2. 页面清单
3. 路由定义
4. mock 场景矩阵
5. 代表性代码文件
6. 运行说明

### 推荐页面清单
- 首页看板
- 调度指令列表页
- 调度指令详情页
- 材料传递页
- 组上报页
- 协助申请页
- 催办预警页

## 样例 2：页面模板选型

### 列表型场景
适合使用 `list-page-template.vue`
- 查询条件 + 表格 + 状态标签 + 行操作

### 详情型场景
适合使用 `detail-page-template.vue`
- 基本信息 + 时间线 + 附件区 + 操作区

### 流程型场景
适合使用 `workflow-page-template.vue`
- 阶段条 + 操作记录 + 状态切换 + 备注

## 样例 3：Mock 场景矩阵写法

### 推荐场景
- happy-path：完整成功流程
- delayed-feedback：部分事项逾期未反馈
- permission-limited：只读角色访问
- mixed-status：列表中混合多种状态

### 稳定输出片段
```md
| 场景 | 角色 | 页面 | 数据特点 | 目的 |
| --- | --- | --- | --- | --- |
| happy-path | 巡办管理员 | 调度指令列表 | 全部字段齐全 | 演示正常链路 |
| delayed-feedback | 巡办管理员 | 催办预警页 | 含逾期标记 | 演示督办能力 |
```

## 完整链路样例映射

- 参考 `shared/full-chain-examples/case-01-upload-delivery/04-openapi.yaml` 与 `05-vue-mock-prototype.md`。
- 当前 Skill 负责把契约映射到页面、路由、mock 场景与演示路径。


## 标杆案例补充
- `shared/full-chain-examples/case-01-upload-delivery/06-vue-prototype-code/`：与 `05-vue-mock-prototype.md` 配套的可运行 Vue 原型代码骨架。


## 标杆原型补充
当任务需要稳定复刻原型时，优先对照 `shared/full-chain-examples/case-01-upload-delivery/06-vue-prototype-code/` 与 `07` 到 `11` 号文件，保持页面骨架、演示口径和 mock 场景一致。
