import { defineStore } from 'pinia'

export const useFeatureStore = defineStore('feature', {
  state: () => ({
    loading: false,
    items: [] as Array<Record<string, unknown>>,
    selectedId: '' as string,
  }),
  actions: {
    async load() {
      this.loading = true
      try {
        this.items = []
      } finally {
        this.loading = false
      }
    },
  },
})
