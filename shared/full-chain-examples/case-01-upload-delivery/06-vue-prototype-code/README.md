# case-01 Vue 原型代码骨架样例

本目录提供“上传下达模块”标杆样例的可运行 Vue 3 原型骨架，目标是：

- 能本地安装并启动
- 展示多角色切换
- 覆盖首页看板、调度指令、周报、协助申请、会议通知、审计摘要等核心页面
- 使用本地 mock 数据，不依赖真实后端

## 启动方式

```bash
npm install
npm run dev
```

## 验证方式

```bash
npm run build
```

## 说明

- 这是演示型原型骨架，不追求生产级实现。
- 页面与字段命名与 `04-openapi.yaml` 和 `05-vue-mock-prototype.md` 保持尽量一致。
- Mock 数据集中放在 `src/services/mock/datasets/`。
