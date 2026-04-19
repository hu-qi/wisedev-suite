# API 风格指引

## 借鉴原则
- 采用 API First 思路，先定义契约、后谈实现。
- 输出单文件自包含 YAML，便于审阅与版本管理。
- 资源路径使用复数名词，避免动词化。
- 分页、错误响应、安全方案和示例都应统一。

## 默认命名建议
- path: kebab-case
- query 参数: snake_case
- schema / property: camelCase 或 snake_case 二选一；同一份规范内保持一致
- 枚举值: UPPER_SNAKE_CASE
