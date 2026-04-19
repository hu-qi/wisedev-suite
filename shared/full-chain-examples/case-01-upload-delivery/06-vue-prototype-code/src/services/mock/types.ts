export type DispatchOrderStatus = 'DRAFT' | 'PUBLISHED' | 'ACKNOWLEDGED' | 'IN_PROGRESS' | 'OVERDUE' | 'COMPLETED'
export type ReportStatus = 'DRAFT' | 'SUBMITTED' | 'RETURNED' | 'RESUBMITTED' | 'ARCHIVED'
export type AssistStatus = 'PENDING' | 'ACCEPTED' | 'IN_PROGRESS' | 'COMPLETED'

export interface DashboardSummary {
  pendingAck: number
  overdue: number
  weeklyRate: string
  openAssists: number
  risks: Array<{ id: string; title: string; level: string; link: string }>
}

export interface DispatchOrder {
  id: string
  title: string
  securityLevel: string
  targetGroupCount: number
  dueAt: string
  status: DispatchOrderStatus
  updatedAt: string
  content: string
  actions: string[]
  timeline: Array<{ at: string; actor: string; action: string; note: string }>
}

export interface GroupReport {
  id: string
  title: string
  period: string
  status: ReportStatus
  groupName: string
  updatedAt: string
  content: string
  returnComment?: string
  versions: Array<{ version: string; at: string; operator: string; note: string }>
}

export interface AssistRequest {
  id: string
  title: string
  requester: string
  targetDepartment: string
  status: AssistStatus
  updatedAt: string
  content: string
  timeline: Array<{ at: string; actor: string; action: string; note: string }>
}

export interface MeetingNotice {
  id: string
  title: string
  startAt: string
  confirmStatus: string
  content: string
}

export interface AuditLog {
  id: string
  module: string
  action: string
  actor: string
  at: string
  summary: string
}
