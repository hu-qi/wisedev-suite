<template>
  <div class="kpi-card" :class="tone">
    <div class="kpi-head">
      <div>
        <div class="kpi-label">{{ label }}</div>
        <div class="kpi-value">{{ value }}</div>
      </div>
      <div class="kpi-icon">{{ icon }}</div>
    </div>
    <div class="kpi-foot">
      <span>{{ hint }}</span>
      <span v-if="trend" class="kpi-trend">{{ trend }}</span>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  label: string
  value: string | number
  hint: string
  icon?: string
  trend?: string
  tone?: 'neutral' | 'primary' | 'warning' | 'success' | 'danger'
}>()
</script>
