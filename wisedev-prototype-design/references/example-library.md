# 高质量样例库：原型设计方向

## 样例 1：已有 OpenAPI，先做设计方向

### 输入前提
- 已有 `openapi.yaml`
- 已知主要页面类型：Dashboard、List、Detail、Form

### 推荐输出顺序
1. 设计任务重述
2. 3 套方向
3. 推荐方向
4. `DESIGN.md`
5. `theme.json`
6. 页面级约束
7. 交接给 `wisedev-vue-mock-prototype`

## 样例 2：已有 Vue 原型，做设计评审

### 输入前提
- 已有页面截图或 Vue 代码骨架

### 推荐输出顺序
1. 当前采用的设计气质判断
2. 总体评分
3. Keep
4. Fix
5. Quick Wins

## 样例 3：政企项目默认建议

若用户没有明确偏好，可默认推荐：
- 主推：`stable_enterprise`
- 备选：`data_command`
- 差异化：`modern_east`

推荐理由：
- 既符合政企接受度，又保留一定演示辨识度

## 样例 4：双产物建议

默认建议：
- 对人和 AI：交付 `DESIGN.md`
- 对脚本和脚手架：保留 `theme.json`

不建议当前阶段直接删除 `theme.json`，因为 `wisedev-vue-mock-prototype/scripts/` 仍依赖结构化字段。

## 样例 5：内置 DESIGN.md 样例

当前仓库已提供 3 份由内置 theme 自动导出的 `DESIGN.md` 样例：
- `examples/design-md/enterprise-calm-DESIGN.md`
- `examples/design-md/data-command-DESIGN.md`
- `examples/design-md/modern-east-DESIGN.md`

可用于：
- 校验 `theme.json -> DESIGN.md` 的导出质量
- 作为后续新增主题的参考格式
- 给 AI 工具直接提供可读的设计系统输入
