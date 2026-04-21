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

## 主题接入约定
- 若上游存在 `wisedev-prototype-design` 产出的 theme package，统一放入 `src/theme/`
- 推荐至少包含：
  - `src/theme/tokens.ts`：主题 token 对象或默认主题导出
  - `src/theme/theme.css`：映射到 CSS 变量
- 页面、布局、公共组件优先消费 CSS 变量，不直接硬编码视觉值
- 允许页面有少量场景化覆盖，但不得绕开 theme 体系重写整页视觉
