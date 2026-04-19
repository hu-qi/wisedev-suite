import type { GroupReport } from '../types'

export const groupReports: GroupReport[] = [
  {
    id: 'GR-2026-001',
    title: '第一巡视组第 16 周周报',
    period: '2026-W16',
    status: 'SUBMITTED',
    groupName: '第一巡视组',
    updatedAt: '2026-04-17 10:10',
    content: '本周已完成谈话 8 人次，发现问题线索 2 项。',
    versions: [
      { version: 'v1', at: '2026-04-17 09:40', operator: '第一巡视组', note: '首次提交' },
    ],
  },
  {
    id: 'GR-2026-002',
    title: '第三巡视组第 16 周问题报表',
    period: '2026-W16',
    status: 'RETURNED',
    groupName: '第三巡视组',
    updatedAt: '2026-04-17 11:00',
    content: '发现主要问题 4 项，涉及采购审批流程。',
    returnComment: '请补充问题分类和附件目录。',
    versions: [
      { version: 'v1', at: '2026-04-16 17:10', operator: '第三巡视组', note: '首次提交' },
      { version: 'v1-return', at: '2026-04-17 11:00', operator: '巡办管理员', note: '退回补充' },
    ],
  },
]
