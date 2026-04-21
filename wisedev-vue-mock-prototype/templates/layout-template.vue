<template>
  <div class="layout-shell">
    <aside class="layout-sidebar">导航区</aside>
    <main class="layout-main">
      <slot />
    </main>
  </div>
</template>

<style scoped>
.layout-shell {
  display: grid;
  grid-template-columns: var(--layout-sidebar-width, 220px) minmax(0, 1fr);
  min-height: 100vh;
  background: var(--color-bg-canvas, #f5f7fa);
  color: var(--color-text-primary, #1f2937);
}

.layout-sidebar {
  padding: 24px 20px;
  border-right: 1px solid var(--color-border, #d7dee7);
  background: var(--color-bg-surface, #ffffff);
}

.layout-main {
  padding: 24px;
}
</style>
