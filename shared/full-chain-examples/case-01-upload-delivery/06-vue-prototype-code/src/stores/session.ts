import { defineStore } from 'pinia'

export type RoleCode = 'office_admin' | 'group_leader' | 'department_liaison'

const STORAGE_KEY = 'case01-role'

const roleLabels: Record<RoleCode, string> = {
  office_admin: '巡办管理员',
  group_leader: '巡组组长',
  department_liaison: '协同部门联络员',
}

const readStored = (): RoleCode => {
  if (typeof window === 'undefined') return 'office_admin'
  return (window.localStorage.getItem(STORAGE_KEY) as RoleCode) || 'office_admin'
}

export const useSessionStore = defineStore('session', {
  state: () => ({ role: readStored() as RoleCode }),
  getters: {
    roleLabel: (state) => roleLabels[state.role],
    roles: () => Object.entries(roleLabels).map(([value, label]) => ({ value: value as RoleCode, label })),
  },
  actions: {
    setRole(role: RoleCode) {
      this.role = role
      if (typeof window !== 'undefined') {
        window.localStorage.setItem(STORAGE_KEY, role)
      }
    },
  },
})
