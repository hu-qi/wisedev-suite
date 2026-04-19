# Schema 约定

- 列表响应使用 `items + page` 结构。
- 对同一资源，读写模型尽量共享，但可通过 `readOnly` / `writeOnly` 区分。
- 重要字段要带 `description` 与 `example`。
