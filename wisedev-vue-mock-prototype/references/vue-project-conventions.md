# Vue 原型项目约定

## 推荐技术栈
- Vue 3 + Vite + TypeScript
- Vue Router
- Pinia
- `src/modules/` 按业务模块组织
- `src/mock/` 放本地 mock handler 和 dataset

## 目录组织原则
- 以功能模块优先
- 页面与组件分层
- 可共享的组件进入 `src/components/`
- 与 API 契约直接相关的类型进入 `src/types/`
