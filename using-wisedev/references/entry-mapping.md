# WiseDev 显式入口映射

本文件用于让代理在单阶段、明确请求中快速选择正确的 WiseDev 子 Skill。

## 一、输入归类

### 会议与讨论材料
关键词示例：
- 会议纪要
- 录音转写
- 需求梳理
- 讨论材料

目标子 Skill：`wisedev-meeting-to-spec`

### 需求规格文档
关键词示例：
- 需求规格说明书
- SRS
- 正式需求文档
- 验收标准

目标子 Skill：`wisedev-requirement-spec`

### 设计文档
关键词示例：
- 概要设计
- 详细设计
- 模块设计
- 状态机
- 数据模型

目标子 Skill：`wisedev-design-doc`

### API 契约
关键词示例：
- openapi
- 接口契约
- api yaml
- mock-ready api

目标子 Skill：`wisedev-openapi-contract`

### Vue 原型
关键词示例：
- vue 原型
- 前端原型
- mock 原型
- 演示型前端

目标子 Skill：`wisedev-vue-mock-prototype`

## 二、回退到总控的优先级

如果一个请求同时命中多个入口，或虽然命中单个入口但上游产物明显缺失，则不要直接进入子 Skill，应先转给 `wisedev-orchestrator`。
