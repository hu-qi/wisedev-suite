# 高质量样例库：原型设计方向

## 样例 1：已有 OpenAPI，先做设计方向

### 输入前提
- 已有 `openapi.yaml`
- 已知主要页面类型：Dashboard、List、Detail、Form

### 推荐输出顺序
1. 设计任务重述
2. 3 套方向
3. 推荐方向
4. 主题包 JSON
5. 页面级约束
6. 交接给 `wisedev-vue-mock-prototype`

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
