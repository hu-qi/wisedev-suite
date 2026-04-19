<template>
  <div class="empty-state">
    <div class="empty-state-icon">{{ icon }}</div>
    <div class="empty-state-title">{{ title }}</div>
    <div class="empty-state-desc">{{ description }}</div>
  </div>
</template>

<script setup lang="ts">
defineProps<{ title: string; description: string; icon?: string }>()
</script>
