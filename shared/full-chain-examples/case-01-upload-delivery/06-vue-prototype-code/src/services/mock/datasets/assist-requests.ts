import type { AssistRequest } from '../types'

export const assistRequests: AssistRequest[] = [
  {
    id: 'AR-2026-001',
    title: '提请纪检部门协助核查专项资金问题',
    requester: '第二巡视组',
    targetDepartment: '纪检部门',
    status: 'IN_PROGRESS',
    updatedAt: '2026-04-17 08:30',
    content: '请协助核查 2025 年度专项资金拨付与验收资料一致性。',
    timeline: [
      { at: '2026-04-15 14:00', actor: '第二巡视组', action: '发起申请', note: '已提交协助申请表' },
      { at: '2026-04-15 16:30', actor: '巡办管理员', action: '转办', note: '已转办至纪检部门' },
      { at: '2026-04-16 09:00', actor: '纪检联络员', action: '接收', note: '已安排内部核查' },
    ],
  },
]
