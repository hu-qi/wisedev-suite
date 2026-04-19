# 错误模型建议

统一错误对象字段：
- code
- message
- details
- traceId
- timestamp

对校验类、权限类、业务冲突类错误，应分别给出不同 code 范围。
