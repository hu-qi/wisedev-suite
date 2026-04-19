import { dashboardSummary } from './datasets/dashboard'
import { dispatchOrders } from './datasets/dispatch-orders'
import { groupReports } from './datasets/group-reports'
import { assistRequests } from './datasets/assist-requests'
import { meetings } from './datasets/meetings'
import { auditLogs } from './datasets/audit-logs'
import type { AssistRequest, AuditLog, DashboardSummary, DispatchOrder, GroupReport, MeetingNotice } from './types'

export type ScenarioCode = 'happy_path' | 'delayed_tasks' | 'returned_for_revision' | 'cross_department_coordination' | 'closed_archive'

export type ScenarioBundle = {
  dashboard: DashboardSummary
  dispatchOrders: DispatchOrder[]
  groupReports: GroupReport[]
  assistRequests: AssistRequest[]
  meetings: MeetingNotice[]
  auditLogs: AuditLog[]
}

const clone = <T>(data: T): T => JSON.parse(JSON.stringify(data)) as T

const baseBundle = (): ScenarioBundle => ({
  dashboard: clone(dashboardSummary),
  dispatchOrders: clone(dispatchOrders),
  groupReports: clone(groupReports),
  assistRequests: clone(assistRequests),
  meetings: clone(meetings),
  auditLogs: clone(auditLogs),
})

const applyDelayedTasks = (bundle: ScenarioBundle) => {
  bundle.dashboard.pendingAck = 5
  bundle.dashboard.overdue = 4
  bundle.dashboard.weeklyRate = '76%'
  bundle.dispatchOrders[0].status = 'OVERDUE'
  bundle.dispatchOrders[0].actions = ['催办', '升级预警']
  bundle.dispatchOrders[0].timeline.push({ at: '2026-04-17 14:20', actor: '系统', action: '催办提醒', note: '因超过计划节点自动提醒' })
  bundle.auditLogs.unshift({ id: 'AL-NEW-001', module: '调度指令', action: '升级预警', actor: '系统', at: '2026-04-17 14:20', summary: '对 DO-2026-001 触发升级预警' })
}

const applyReturnedForRevision = (bundle: ScenarioBundle) => {
  bundle.dashboard.weeklyRate = '68%'
  bundle.groupReports[0].status = 'RETURNED'
  bundle.groupReports[0].returnComment = '请补充问题分类、责任单位与附件目录。'
  bundle.groupReports[0].versions.push({ version: 'v1-return', at: '2026-04-17 16:00', operator: '巡办管理员', note: '退回补正' })
  bundle.auditLogs.unshift({ id: 'AL-NEW-002', module: '周报', action: '退回', actor: '巡办管理员', at: '2026-04-17 16:00', summary: '将 GR-2026-001 退回补充问题分类和附件目录' })
}

const applyCoordination = (bundle: ScenarioBundle) => {
  bundle.dashboard.openAssists = 6
  bundle.assistRequests[0].status = 'IN_PROGRESS'
  bundle.assistRequests[0].timeline.push({ at: '2026-04-17 10:40', actor: '组织部门联络员', action: '补充协同', note: '同步调取干部任职资料' })
  bundle.meetings[0].confirmStatus = '已确认 9/9'
  bundle.auditLogs.unshift({ id: 'AL-NEW-003', module: '协助申请', action: '联合协同', actor: '巡办管理员', at: '2026-04-17 10:45', summary: '纪检、组织、职能部门进入联合协同处理' })
}

const applyClosedArchive = (bundle: ScenarioBundle) => {
  bundle.dashboard.pendingAck = 0
  bundle.dashboard.overdue = 0
  bundle.dashboard.weeklyRate = '100%'
  bundle.dashboard.openAssists = 0
  bundle.dashboard.risks = []
  for (const item of bundle.dispatchOrders) {
    item.status = 'COMPLETED'
    item.actions = ['查看归档']
    item.timeline.push({ at: '2026-04-20 18:00', actor: '巡办管理员', action: '办结归档', note: '归档完成，可供追溯' })
  }
  for (const item of bundle.groupReports) {
    item.status = 'SUBMITTED'
    item.returnComment = undefined
  }
  bundle.assistRequests[0].status = 'COMPLETED'
  bundle.assistRequests[0].timeline.push({ at: '2026-04-19 17:30', actor: '纪检联络员', action: '反馈完成', note: '结果已回传巡办与巡组' })
  bundle.auditLogs.unshift({ id: 'AL-NEW-004', module: '全流程', action: '归档', actor: '系统', at: '2026-04-20 18:10', summary: '上传下达模块 Case-01 场景已全部归档' })
}

export const getScenarioBundle = (scenario: ScenarioCode): ScenarioBundle => {
  const bundle = baseBundle()
  if (scenario === 'delayed_tasks') applyDelayedTasks(bundle)
  if (scenario === 'returned_for_revision') applyReturnedForRevision(bundle)
  if (scenario === 'cross_department_coordination') applyCoordination(bundle)
  if (scenario === 'closed_archive') applyClosedArchive(bundle)
  return bundle
}
