# Case-01 Theme Prototype Workflow

本文档用于演示新的原型链路如何将“设计方向”显式传递给 Vue 原型阶段，而不是在原型落地时重新自由发挥。

## 1. 目标

通过一个可复用的示范流程，说明以下三件事：

1. `wisedev-prototype-design` 先给出设计方向与 theme package
2. `wisedev-vue-mock-prototype` 在 OpenAPI 脚手架阶段保留 theme 信息
3. 初始化 Vue 原型骨架时，直接把选定 theme 写入 `src/theme/`

## 2. 推荐输入

- 业务上下文：`00-source-input.md`
- 规格与设计：`02-requirement-spec.md`、`03-design-doc.md`
- 契约：`04-openapi.yaml`
- 原型说明：`05-vue-mock-prototype.md`

## 3. 推荐主题化链路

### 步骤 A：先选设计方向

由 `wisedev-prototype-design` 输出：
- 3 套方向建议
- 选定的 `themeId`
- 对应 theme package JSON

本案例推荐用于演示差异化方案时，可选择：
- `stable_enterprise`
- `data_command`
- `modern_east`

## 4. 步骤 B：从 OpenAPI 生成脚手架草稿

示例命令：

```bash
PYTHONPATH=/tmp/wisedev-pyyaml python3 wisedev-vue-mock-prototype/scripts/scaffold_from_openapi.py \
  shared/full-chain-examples/case-01-upload-delivery/04-openapi.yaml \
  wisedev-prototype-design/assets/themes/modern-east.json
```

预期输出至少包含：
- `modules`
- `routes`
- `mockHandlers`
- `theme`
- `moduleScaffold`

其中 `theme` 段会显式标明：
- 推荐使用的 `themeId`
- theme 来源
- 目标文件：`src/theme/tokens.ts`、`src/theme/theme.css`

如需直接生成模块目录草稿，可追加 `--write`：

```bash
PYTHONPATH=/tmp/wisedev-pyyaml python3 wisedev-vue-mock-prototype/scripts/scaffold_from_openapi.py \
  shared/full-chain-examples/case-01-upload-delivery/04-openapi.yaml \
  wisedev-prototype-design/assets/themes/modern-east.json \
  --write /private/tmp/wisedev-case01-modern
```

## 5. 步骤 C：初始化带主题的原型骨架

示例命令：

```bash
python3 wisedev-vue-mock-prototype/scripts/init_vue_prototype.py \
  /private/tmp/wisedev-case01-modern \
  wisedev-prototype-design/assets/themes/modern-east.json
```

预期结果：
- `src/theme/tokens.ts` 已写入选定 theme
- `src/theme/theme.css` 已生成 CSS 变量
- `src/App.vue` 上的 `data-theme` 与选定 `themeId` 一致

## 6. 推荐验证点

- `tokens.ts` 中的颜色、圆角、字体是否来自选定 theme
- `theme.css` 是否映射了基础 CSS 变量
- `App.vue` 是否带有正确的 `data-theme`
- `moduleScaffold` 是否能作为后续 `src/modules/*` 落地的参考

## 7. 对当前 Case-01 的意义

这个新链路不会替代 `05-vue-mock-prototype.md` 与 `06-vue-prototype-code/`，而是补上一层显式的设计约束传递：

- 以前：OpenAPI → 原型骨架
- 现在：设计方向 → OpenAPI 脚手架提示 → theme 化原型骨架

这样做的价值是：
- 页面视觉不再完全依赖模型临场发挥
- 原型更容易在不同模型间保持一致气质
- 方案评审时可以清楚区分“业务结构问题”和“视觉方向问题”
