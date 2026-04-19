import { defineStore } from 'pinia'

export type ScenarioCode = 'happy_path' | 'delayed_tasks' | 'returned_for_revision' | 'cross_department_coordination' | 'closed_archive'

const STORAGE_KEY = 'case01-scenario'

const labels: Record<ScenarioCode, string> = {
  happy_path: '标准推进',
  delayed_tasks: '滞后待办',
  returned_for_revision: '退回补正',
  cross_department_coordination: '横向协同中',
  closed_archive: '已办结归档',
}

const readStored = (): ScenarioCode => {
  if (typeof window === 'undefined') return 'happy_path'
  const value = window.localStorage.getItem(STORAGE_KEY)
  return (value as ScenarioCode) || 'happy_path'
}

export const useScenarioStore = defineStore('scenario', {
  state: () => ({ code: readStored() as ScenarioCode }),
  getters: {
    scenarioLabel: (state) => labels[state.code],
    scenarios: () => Object.entries(labels).map(([value, label]) => ({ value: value as ScenarioCode, label })),
  },
  actions: {
    setScenario(code: ScenarioCode) {
      this.code = code
      if (typeof window !== 'undefined') {
        window.localStorage.setItem(STORAGE_KEY, code)
      }
    },
  },
})
