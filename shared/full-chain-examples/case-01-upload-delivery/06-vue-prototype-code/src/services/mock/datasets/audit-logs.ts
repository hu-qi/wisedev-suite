import type { AuditLog } from '../types'

export const auditLogs: AuditLog[] = [
  { id: 'AL-001', module: '调度指令', action: '催办', actor: '巡办管理员', at: '2026-04-17 08:46', summary: '对 DO-2026-003 发起催办提醒' },
  { id: 'AL-002', module: '周报', action: '退回', actor: '巡办管理员', at: '2026-04-17 11:00', summary: '将 GR-2026-002 退回补充附件目录' },
  { id: 'AL-003', module: '协助申请', action: '转办', actor: '巡办管理员', at: '2026-04-15 16:30', summary: '将 AR-2026-001 转办至纪检部门' },
]
