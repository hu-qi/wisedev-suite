# Mock 服务模式

优先使用“本地 mock 模块 + fetch 包装层”的简单方式，保证复制出来即可运行。

每个业务域建议至少包括：
- handlers
- dataset
- scenario switch
- delay / error simulation
