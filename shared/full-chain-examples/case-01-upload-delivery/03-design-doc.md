# 概要设计与详细设计（高保真标杆样例）

## 1. 设计目标
围绕“下发、上报、协同、督办”四大业务主线，建立统一的模块边界、状态模型、权限规则、交互约束和接口契约映射，为 OpenAPI 与 Vue + mock 原型提供稳定输入。

## 2. 设计原则
1. **契约先行**：模块设计必须可映射到明确 API 标签与请求响应模型。
2. **状态清晰**：关键业务对象必须具备清晰且可解释的状态流转。
3. **留痕一致**：不同模块的审计字段保持统一口径。
4. **原型可演示**：设计输出需支撑本地可运行原型，而不是仅停留于抽象描述。
5. **首期可落地**：首期对真实加密、网关通知等能力以占位方式表达。

## 3. 总体架构
### 3.1 逻辑架构分层
- **展示层**：Vue 页面、布局、路由、角色切换与 mock 演示入口。
- **应用层**：调度、材料、会议、上报、协助、看板等业务模块服务。
- **契约层**：OpenAPI 定义、错误模型、分页与筛选模型。
- **数据层**：业务对象模型、状态字典、审计日志、mock 数据集。

### 3.2 模块划分
| 模块编号 | 模块名称 | 核心职责 | 主要对象 |
|---|---|---|---|
| MOD-DISPATCH | 调度指令管理 | 指令创建、发布、签收、反馈、催办 | DispatchOrder |
| MOD-MATERIAL | 材料传递管理 | 附件挂载、定向传递、回执、下载留痕 | DispatchMaterial |
| MOD-MEETING | 会议协同管理 | 会议通知、参会确认、纪要查看 | MeetingNotice |
| MOD-REPORT | 组上报管理 | 周报、问题报表、版本链、退回重提 | GroupReport |
| MOD-ASSIST | 协助申请管理 | 申请发起、巡办受理、转办、部门反馈 | AssistRequest |
| MOD-BOARD | 看板与预警 | 统计汇总、筛选跳转、逾期预警 | DashboardCard |
| MOD-AUDIT | 审计留痕 | 统一动作留痕、动作摘要展示 | AuditLog |

## 4. 核心业务对象设计
### 4.1 DispatchOrder
**职责**：承载巡办向巡组下发的调度任务。

**关键字段**
- `id`
- `orderNo`
- `title`
- `content`
- `secrecyLevel`
- `dueAt`
- `feedbackRequired`
- `status`
- `recipientGroupIds[]`
- `feedbackSummary`
- `attachments[]`
- `latestActionAt`

**子对象**
- `DispatchRecipientStatus`：记录每个巡组的签收/反馈状态。
- `DispatchFeedback`：记录阶段反馈和办结反馈。

### 4.2 DispatchMaterial
**职责**：承载定向传递的专项材料。

**关键字段**
- `id`
- `dispatchOrderId`
- `fileName`
- `secrecyLevel`
- `downloadAllowed`
- `downloadCount`
- `receiptStatus`

### 4.3 MeetingNotice
**职责**：承载会议通知与确认。

**关键字段**
- `id`
- `subject`
- `meetingAt`
- `locationOrLink`
- `participants[]`
- `confirmationStatusSummary`
- `minutesAttachment`

### 4.4 GroupReport
**职责**：承载周报或问题报表。

**关键字段**
- `id`
- `reportType`
- `groupId`
- `period`
- `title`
- `content`
- `attachments[]`
- `status`
- `version`
- `returnedReason`

### 4.5 AssistRequest
**职责**：承载巡组向巡办提出的协助申请及后续转办过程。

**关键字段**
- `id`
- `requestNo`
- `subject`
- `supportType`
- `requestingGroupId`
- `coordinatorDeptId`
- `dueAt`
- `status`
- `resultSummary`
- `timeline[]`

### 4.6 AuditLog
**职责**：统一记录关键动作。

**关键字段**
- `id`
- `entityType`
- `entityId`
- `actionType`
- `actorId`
- `actorRole`
- `occurredAt`
- `result`
- `remarks`

## 5. 状态模型设计
### 5.1 调度指令状态机
主链路：
`草稿 -> 已发布 -> 已签收 -> 办理中 -> 已反馈 -> 已关闭`

异常分支：
- `已发布 -> 已撤回`
- `办理中 -> 已逾期`
- `已逾期 -> 已反馈`
- `已反馈 -> 已关闭`

**状态说明**
- `已发布`：巡办已发出，但目标对象尚未签收。
- `已签收`：巡组已签收，尚未提交阶段反馈。
- `办理中`：已有阶段反馈或已开始处理。
- `已逾期`：超过截止时间且未达到反馈要求。
- `已关闭`：巡办确认闭环完成。

### 5.2 周报/问题报表状态机
`草稿 -> 已提交 -> 已退回 -> 已重提 -> 已归档`

### 5.3 协助申请状态机
`草稿 -> 已提交 -> 巡办处理中 -> 已转办 -> 部门处理中 -> 已反馈 -> 已关闭`

### 5.4 会议通知确认状态
`待确认 -> 已确认参加/请假/待定 -> 已结束`

## 6. 权限模型
### 6.1 权限矩阵
| 动作 | 巡办管理员 | 巡组组长 | 巡组成员 | 协同部门联络员 | 系统管理员 |
|---|---|---|---|---|---|
| 创建调度指令 | Y | N | N | N | N |
| 发布/撤回调度指令 | Y | N | N | N | N |
| 签收调度指令 | N | Y | Y* | N | N |
| 提交反馈 | N | Y | Y* | N | N |
| 传递专项材料 | Y | N | N | N | N |
| 创建会议通知 | Y | N | N | N | N |
| 提交周报 | N | Y | Y* | N | N |
| 退回周报 | Y | N | N | N | N |
| 发起协助申请 | N | Y | Y* | N | N |
| 转办协助申请 | Y | N | N | N | N |
| 反馈协同结果 | N | N | N | Y | N |
| 查看审计日志 | Y | N | N | N | Y |

`Y*` 表示具备组内授权的成员。

### 6.2 角色切换策略
原型中提供角色切换入口，用于同一套 mock 数据在不同角色视角下展示不同按钮、列表与明细。

## 7. 关键流程设计
### 7.1 调度指令下发与反馈流程
1. 巡办管理员创建指令草稿。
2. 系统校验标题、截止时间、目标巡组和反馈要求。
3. 发布成功后为每个目标巡组生成待办。
4. 巡组登录后在列表页查看待办并签收。
5. 巡组在详情页补充阶段反馈或办结反馈。
6. 巡办在详情页与看板中查看状态变化；对逾期项发起催办。
7. 完成后巡办将事项关闭。

### 7.2 周报提报与退回重提流程
1. 巡组进入周报新建页。
2. 选择报表类型与周期，填写正文和附件。
3. 可保存草稿；提交后生成版本 1。
4. 巡办审阅后可退回并填写退回意见。
5. 巡组修改并重提，系统生成版本 2，并保留旧版本只读展示。

### 7.3 协助申请流转流程
1. 巡组创建协助申请并提交。
2. 巡办在待办中受理，选择协同部门并转办。
3. 协同部门联络员更新处理进度。
4. 协同部门提交结果反馈。
5. 巡办确认结果，申请关闭；巡组可查看全链路记录。

### 7.4 首页看板进入列表流程
1. 巡办打开首页看板。
2. 点击“逾期事项”卡片。
3. 系统跳转调度列表并带入 `status=OVERDUE` 条件。
4. 用户查看逾期明细并进一步催办。

## 8. 页面与组件设计约束
### 8.1 页面分类
- 列表页：支持筛选、分页、状态徽标、快捷操作。
- 详情页：支持基础信息区、正文附件区、状态时间轴区、操作区。
- 表单页：支持保存草稿、提交、校验错误提示。
- 看板页：支持卡片指标、趋势区块、快捷入口。

### 8.2 复用组件
- `StatusBadge`
- `TimelinePanel`
- `AttachmentList`
- `AuditSummaryCard`
- `FilterToolbar`
- `RoleSwitcher`

### 8.3 交互约束
- 关键状态使用统一色系：正常、预警、逾期、关闭。
- 所有详情页底部保留“最近动作摘要”。
- 原型中重要按钮需有显式业务名称，如“签收指令”“提交反馈”“转办协同”。

## 9. API 设计映射
| 设计模块 | API 标签 | 关键路径 |
|---|---|---|
| MOD-DISPATCH | dispatchOrders | `/dispatch-orders`, `/dispatch-orders/{orderId}/receive`, `/dispatch-orders/{orderId}/feedback` |
| MOD-MATERIAL | dispatchMaterials | `/dispatch-materials`, `/dispatch-materials/{materialId}/receipt` |
| MOD-MEETING | meetings | `/meetings`, `/meetings/{meetingId}/confirm` |
| MOD-REPORT | groupReports | `/group-reports`, `/group-reports/{reportId}/resubmit` |
| MOD-ASSIST | assistRequests | `/assist-requests`, `/assist-requests/{requestId}/forward`, `/assist-requests/{requestId}/feedback` |
| MOD-BOARD | dashboards | `/dashboards/overview` |
| MOD-AUDIT | auditLogs | `/audit-logs` |

## 10. 异常与补偿设计
### 10.1 调度指令异常
- 若已发布指令目标配置错误，则通过“撤回 + 重发”补偿，不直接修改已发记录。
- 若反馈附件上传失败，则保留反馈草稿并提示重新上传。

### 10.2 周报异常
- 若退回意见为空，则不允许执行退回。
- 若模板版本变更，则新建版本时保留版本标识。

### 10.3 协助申请异常
- 若协同部门超过时限未反馈，则进入预警状态，并允许巡办再次催办。
- 若转办部门错误，需补偿为“追回并重新转办”，保留追回记录。

## 11. 审计与安全设计
### 11.1 统一留痕口径
统一使用以下字段：
- `actorId`
- `actorRole`
- `actionType`
- `entityType`
- `entityId`
- `occurredAt`
- `result`
- `remarks`

### 11.2 涉密展示策略
- 原型阶段通过图标和标签体现密级。
- 详情页显示“下载行为留痕”提示。
- 附件列表中区分“可查看”和“受限”两类状态。

## 12. 原型映射
| 功能需求 | 页面路由 | 关键组件 | 主要 mock 数据 |
|---|---|---|---|
| FR-001/FR-002 | `/dispatch-orders`, `/dispatch-orders/:id` | FilterToolbar, StatusBadge, TimelinePanel | dispatchOrders, dispatchFeedbacks |
| FR-003 | `/dispatch-orders/:id` | AttachmentList, AuditSummaryCard | dispatchMaterials |
| FR-004 | `/meetings`, `/meetings/:id` | StatusBadge, AttachmentList | meetings |
| FR-005 | `/group-reports`, `/group-reports/new`, `/group-reports/:id` | FormSection, VersionList | groupReports |
| FR-006 | `/assist-requests`, `/assist-requests/:id` | TimelinePanel, StatusBadge | assistRequests |
| FR-007 | `/dashboard` | DashboardCard, QuickEntry | dashboardOverview |
| FR-008 | `/audit-logs` | AuditSummaryCard, FilterToolbar | auditLogs |
