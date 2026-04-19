# Vue + Mock 原型样例（高保真标杆样例）

## 1. 原型目标
基于 Vue 3 + Vite + TypeScript + Vue Router + Pinia 构建一个可本地运行的演示型原型，用于向业务、产品、设计与研发多角色展示上传下达模块的核心业务闭环、状态变化、权限差异与看板视角。

## 2. 技术约束
- Node.js 18+
- Vite 5+
- Vue 3
- TypeScript
- Vue Router
- Pinia
- 本地 mock 模块，默认不依赖真实后端
- 支持从 `04-openapi.yaml` 衍生 route/mock 草稿
- 本轮标杆样例已经过 `npm run build` 验证

## 3. 原型展示目标
### 3.1 展示重点
1. 巡办下发调度指令到巡组签收反馈的闭环。
2. 周报/问题报表从草稿、提交、退回到重提的状态变化。
3. 协助申请跨部门流转的时间轴。
4. 首页看板的预警与跳转能力。
5. 多角色视角下操作按钮和页面文案的差异。
6. 多场景切换下指标卡、详情页、审计摘要的联动。
7. 更接近正式汇报的视觉层级、信息卡片和详情分区。

### 3.2 不追求内容
- 不实现真实鉴权。
- 不实现真实文件上传。
- 不实现真实图表引擎。
- 不做像素级 UI 设计稿，优先保证业务表达与演示稳定性。

## 4. 当前高保真增强点
- 首页增加 Hero 区、KPI 卡片、演示建议和风险下钻。
- 列表页增加筛选区、数量提示、风险提示和更清晰的信息密度层次。
- 详情页增加进度条、信息条、动作区和更清晰的时间轴。
- 周报创建页增加分步标签页、校验提示和模板填充动作。
- 左侧导航增加角色与场景双切换，并对演示路径给出显式提示。

## 5. 目录结构建议
```text
src/
  main.ts
  App.vue
  layouts/
    ConsoleLayout.vue
  router/
    index.ts
  stores/
    session.ts
    scenario.ts
  services/
    api/
      repository.ts
    mock/
      scenarios.ts
      datasets/
        dashboard.ts
        dispatch-orders.ts
        group-reports.ts
        assist-requests.ts
        meetings.ts
        audit-logs.ts
      types.ts
  views/
    DashboardView.vue
    DispatchOrderListView.vue
    DispatchOrderDetailView.vue
    GroupReportListView.vue
    GroupReportCreateView.vue
    GroupReportDetailView.vue
    AssistRequestListView.vue
    AssistRequestDetailView.vue
    MeetingListView.vue
    MeetingDetailView.vue
    AuditLogView.vue
  components/
    common/
      PageHeader.vue
      StatusBadge.vue
      KpiCard.vue
      InfoStrip.vue
      EmptyState.vue
  styles/
    main.css
```

## 6. 页面清单
| 页面 | 路由 | 核心角色 | 页面目标 | 关键增强 |
|---|---|---|---|---|
| 首页看板 | /dashboard | 巡办管理员 | 汇总查看待签收、逾期、周报提交率、协助未结 | Hero、KPI 卡片、风险表、演示提示 |
| 调度指令列表 | /dispatch-orders | 巡办/巡组 | 按状态筛选、查看是否逾期、进入详情 | 筛选区、密级筛选、逾期提示 |
| 调度指令详情 | /dispatch-orders/:id | 巡办/巡组 | 查看正文、时间轴、执行进度 | 进度条、焦点说明、动作区 |
| 周报列表 | /group-reports | 巡办/巡组 | 查看上报记录、状态、版本 | 筛选区、退回提示 |
| 周报新建 | /group-reports/new | 巡组 | 填报、保存草稿、提交 | 标签页、模板填充、校验提示 |
| 周报详情 | /group-reports/:id | 巡办/巡组 | 查看版本链、退回意见 | Hero 区、退回提示、版本时间轴 |
| 协助申请列表 | /assist-requests | 巡办/巡组 | 查看申请状态和协同部门 | 未结数量提示 |
| 协助申请详情 | /assist-requests/:id | 巡办/协同部门/巡组 | 展示转办时间轴和处理结果 | 流转时间轴、动作区 |
| 会议通知列表 | /meetings | 巡办/巡组 | 查看通知与确认状态 | 更清晰的信息列表 |
| 会议通知详情 | /meetings/:id | 巡办/巡组 | 查看通知正文、确认情况 | 详情信息卡 |
| 审计摘要页 | /audit-logs | 巡办/系统管理员 | 查看关键动作摘要 | 审计动作标签 |

## 7. 角色与权限呈现
### 7.1 角色切换入口
- 左侧导航和首页右上角均可切换角色。
- 预置角色：巡办管理员、巡组组长、协同部门联络员。
- 切换角色后主要影响默认讲解视角、页面文案和演示建议。

### 7.2 差异化展示规则
- 巡办管理员可见：发布、撤回、催办、转办、查看看板、查看审计摘要。
- 巡组组长可见：签收、提交反馈、提交周报、发起协助申请。
- 协同部门联络员可见：查看转办详情、提交处理反馈。

## 8. 场景与数据联动
- 支持 `happy_path`、`delayed_tasks`、`returned_for_revision`、`cross_department_coordination`、`closed_archive` 五类场景。
- 切换场景后影响首页指标、风险事项、调度详情时间轴、周报退回意见、协助申请流转与审计摘要。
- 当前为了简单直接，场景切换后通过刷新页面载入新的 mock bundle。

## 9. 页面级高保真要求
### 9.1 首页看板 `/dashboard`
- 顶部必须有标题、角色切换、场景提示。
- 中部必须有 Hero 区和 4 张 KPI 卡片。
- 底部必须有风险事项区和演示提示区。

### 9.2 调度指令详情 `/dispatch-orders/:id`
- 必须有 Hero 区、进度条、基础信息区、时间轴区、说明区。
- 动作按钮要与状态形成呼应，例如逾期场景下能体现催办感。

### 9.3 周报新建页 `/group-reports/new`
- 必须分为基础信息、问题与附件、提交预览三个页签。
- 必须存在至少一个显式校验提示。

## 10. 后续可继续增强的方向
- 引入更真实的图表组件与附件侧栏。
- 实现不刷新页面的场景切换。
- 增加角色差异下按钮权限控制。
- 引入更细的页面截图样式约定与默认插图资源。
