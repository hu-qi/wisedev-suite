# Theme 接入说明

## 目标

当上游 `wisedev-prototype-design` 已经选定 theme package 时，`wisedev-vue-mock-prototype` 不应再次自由定义视觉体系，而应把 theme package 接入到可运行原型中。

## 推荐目录

```text
src/
  theme/
    tokens.ts
    theme.css
```

## 最低接入要求

- `themeId` 在应用根节点可见
- `theme.css` 提供页面、布局、卡片、Hero、表单等基础变量
- 布局模板和页面模板优先使用 CSS 变量
- 颜色、圆角、阴影、间距不要散落在多个页面中重复硬编码

## 推荐做法

1. 将上游 theme package 转写为 `tokens.ts`
2. 将关键 token 映射为 CSS 自定义属性
3. 在 `main.ts` 中统一引入 `theme.css`
4. 页面模板只消费变量和语义类名

## 脚本接入

初始化原型时，可直接使用：

```bash
python3 scripts/init_vue_prototype.py prototype-app ../wisedev-prototype-design/assets/themes/modern-east.json
```

若未传入 theme JSON，脚本会生成默认的 `stable_enterprise` 主题骨架。

若要在 OpenAPI 脚手架阶段一并传递 theme 信息，可使用：

```bash
python3 scripts/scaffold_from_openapi.py openapi.yaml ../wisedev-prototype-design/assets/themes/modern-east.json
```

输出中的 `theme` 字段会显式标明建议使用的 `themeId` 与目标文件位置。

若希望直接生成模块骨架，可追加：

```bash
python3 scripts/scaffold_from_openapi.py openapi.yaml ../wisedev-prototype-design/assets/themes/modern-east.json --write prototype-app
```

脚本会在 `prototype-app/src/modules/*` 下生成：
- `views/*.vue`
- `store/index.ts`
- `mock/*.ts`
- `types/index.ts`
- `src/router/index.ts` 路由草稿

## 不推荐做法

- 在每个页面单独写一套配色
- 页面直接复制上游 JSON 再手工拆值
- 不经 theme 体系直接在组件里硬编码品牌色
