<template>
  <span class="badge" :class="resolvedVariant">{{ resolvedLabel }}</span>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{ label: string; variant?: 'warning' | 'success' | 'info' | 'danger' | 'neutral' }>()

const labelMappings: Record<string, { text: string; variant: 'warning' | 'success' | 'info' | 'danger' | 'neutral' }> = {
  OVERDUE: { text: '逾期', variant: 'danger' },
  IN_PROGRESS: { text: '办理中', variant: 'info' },
  COMPLETED: { text: '已办结', variant: 'success' },
  SUBMITTED: { text: '已提交', variant: 'success' },
  RETURNED: { text: '已退回', variant: 'warning' },
  RESUBMITTED: { text: '已重提', variant: 'info' },
  ACCEPTED: { text: '已受理', variant: 'info' },
  PENDING: { text: '待受理', variant: 'warning' },
}

const resolvedLabel = computed(() => labelMappings[props.label]?.text || props.label)
const resolvedVariant = computed(() => props.variant || labelMappings[props.label]?.variant || 'neutral')
</script>
