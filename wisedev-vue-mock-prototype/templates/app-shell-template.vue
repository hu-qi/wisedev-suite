<template>
  <div class="app-shell" :data-theme="themeId">
    <RouterView />
  </div>
</template>

<script setup lang="ts">
const themeId = 'stable_enterprise'
</script>
