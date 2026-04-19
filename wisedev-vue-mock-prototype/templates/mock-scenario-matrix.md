# Mock 场景矩阵

| 场景 | 说明 | 适用页面 | 关键状态 | 是否必须 |
| --- | --- | --- | --- | --- |
| happy_path | 主流程成功 | 列表、详情、提交流程 | COMPLETED | 是 |
| pending_review | 待审核 | 详情、审批页 | PENDING | 是 |
| partial_completion | 部分完成 | 看板、列表 | PARTIAL | 是 |
| rejected | 被退回 | 详情、流程页 | REJECTED | 建议 |
| timeout_retry | 请求超时 / 重试 | 表单页 | RETRYING | 建议 |
