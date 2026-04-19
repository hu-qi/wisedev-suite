<template>
  <div class="info-strip">
    <div>
      <div class="info-strip-label">{{ label }}</div>
      <div class="info-strip-value">{{ value }}</div>
    </div>
    <div v-if="extra" class="info-strip-extra">{{ extra }}</div>
  </div>
</template>

<script setup lang="ts">
defineProps<{ label: string; value: string; extra?: string }>()
</script>
