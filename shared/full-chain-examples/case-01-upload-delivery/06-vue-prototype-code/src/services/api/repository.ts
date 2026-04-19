import { getScenarioBundle, type ScenarioCode } from '@/services/mock/scenarios'

const readScenario = (): ScenarioCode => {
  if (typeof window === 'undefined') return 'happy_path'
  return (window.localStorage.getItem('case01-scenario') as ScenarioCode) || 'happy_path'
}

const bundle = () => getScenarioBundle(readScenario())

export const repository = {
  getDashboard: () => bundle().dashboard,
  listDispatchOrders: () => bundle().dispatchOrders,
  getDispatchOrder: (id: string) => bundle().dispatchOrders.find((item) => item.id === id),
  listReports: () => bundle().groupReports,
  getReport: (id: string) => bundle().groupReports.find((item) => item.id === id),
  listAssists: () => bundle().assistRequests,
  getAssist: (id: string) => bundle().assistRequests.find((item) => item.id === id),
  listMeetings: () => bundle().meetings,
  getMeeting: (id: string) => bundle().meetings.find((item) => item.id === id),
  listAuditLogs: () => bundle().auditLogs,
}
