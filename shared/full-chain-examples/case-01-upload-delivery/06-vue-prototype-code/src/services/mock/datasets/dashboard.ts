import type { DashboardSummary } from '../types'

export const dashboardSummary: DashboardSummary = {
  pendingAck: 3,
  overdue: 2,
  weeklyRate: '83%',
  openAssists: 4,
  risks: [
    { id: 'R-001', title: '第二巡视组专项材料签收逾期', level: '高', link: '/dispatch-orders/DO-2026-003' },
    { id: 'R-002', title: '第三巡视组周报被退回待重提', level: '中', link: '/group-reports/GR-2026-002' },
    { id: 'R-003', title: '纪检协助申请处理超过 48 小时', level: '高', link: '/assist-requests/AR-2026-001' },
  ],
}
