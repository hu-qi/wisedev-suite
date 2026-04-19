import type { DispatchOrder } from '../types'

export const dispatchOrders: DispatchOrder[] = [
  {
    id: 'DO-2026-001',
    title: '关于第一轮谈话提纲复核的调度通知',
    securityLevel: '机密',
    targetGroupCount: 4,
    dueAt: '2026-04-21 18:00',
    status: 'IN_PROGRESS',
    updatedAt: '2026-04-17 09:20',
    content: '请各巡视组在规定时间内完成谈话提纲复核，并提交阶段反馈。',
    actions: ['催办', '关闭事项'],
    timeline: [
      { at: '2026-04-15 09:00', actor: '巡办管理员', action: '发布', note: '已向 4 个巡视组下发调度通知' },
      { at: '2026-04-15 10:30', actor: '第一巡视组', action: '签收', note: '已签收并安排责任人' },
      { at: '2026-04-16 16:20', actor: '第二巡视组', action: '阶段反馈', note: '已完成 60%，待补充材料' },
    ],
  },
  {
    id: 'DO-2026-003',
    title: '内部通报材料限时签收',
    securityLevel: '绝密',
    targetGroupCount: 3,
    dueAt: '2026-04-16 12:00',
    status: 'OVERDUE',
    updatedAt: '2026-04-17 08:45',
    content: '请各组限时签收专项通报材料，签收后方可查看附件。',
    actions: ['催办', '再次提醒'],
    timeline: [
      { at: '2026-04-15 08:00', actor: '巡办管理员', action: '发布', note: '专项材料已加密投递' },
      { at: '2026-04-16 12:01', actor: '系统', action: '逾期预警', note: '第二巡视组尚未完成签收' },
    ],
  },
]
