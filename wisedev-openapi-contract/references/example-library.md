# 高质量样例库：OpenAPI 契约

## 样例 1：调度指令查询接口

### 业务意图
前端需要列表页、筛选条件、状态标识和催办按钮。

### 稳定输出特征
- 路径围绕业务对象，而不是数据库表
- 查询参数命名统一
- 响应中包含列表项、分页信息和状态字段
- Example 覆盖正常与空列表场景

### 示例片段
```yaml
/delivery/dispatch-orders:
  get:
    tags: [DispatchOrder]
    summary: 查询调度指令列表
    parameters:
      - name: keyword
        in: query
        schema:
          type: string
      - name: status
        in: query
        schema:
          type: string
          enum: [PUBLISHED, SIGNED, IN_PROGRESS, FEEDBACKED, OVERDUE]
      - $ref: '#/components/parameters/PageNo'
      - $ref: '#/components/parameters/PageSize'
```

## 样例 2：创建协助申请接口

### 业务意图
巡组向巡办发起协助申请，后续需流转状态与反馈结果。

### 推荐输出特征
- `requestBody` 字段名使用业务语义
- 响应返回申请编号、状态、创建时间
- 错误码体现字段校验和权限不足

### 示例片段
```yaml
/delivery/assist-requests:
  post:
    tags: [AssistRequest]
    summary: 发起协助申请
    requestBody:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/AssistRequestCreateCommand'
```

## 样例 3：错误模型

### 推荐统一错误响应
```yaml
ErrorResponse:
  type: object
  required: [code, message, traceId]
  properties:
    code:
      type: string
    message:
      type: string
    traceId:
      type: string
    details:
      type: array
      items:
        $ref: '#/components/schemas/ErrorDetail'
```

## 完整链路样例映射

- 参考 `shared/full-chain-examples/case-01-upload-delivery/03-design-doc.md` 与 `04-openapi.yaml`。
- 当前 Skill 应围绕设计模块、状态与对象来定义接口契约，并服务于 mock 与原型。


## 输出顺序约束

当需求或设计信息不完整时，必须先输出：

```md
## 假设与边界
- 缺失信息：
- 默认假设：
- 不覆盖范围：
```

然后再输出完整的 `openapi.yaml`。不要把假设混写在 YAML 注释里，也不要放在 YAML 后部。
