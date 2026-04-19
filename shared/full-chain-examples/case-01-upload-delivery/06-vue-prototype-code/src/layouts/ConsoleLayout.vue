<template>
  <div class="app-shell">
    <aside class="sidebar">
      <h1>上传下达模块</h1>
      <div class="sidebar-subtitle">Case-01 标杆样例 · 高保真演示原型</div>

      <div class="sidebar-panel">
        <label class="sidebar-label">演示场景</label>
        <select :value="scenario.code" @change="onScenarioChange(($event.target as HTMLSelectElement).value)">
          <option v-for="item in scenario.scenarios" :key="item.value" :value="item.value">{{ item.label }}</option>
        </select>
      </div>

      <div class="sidebar-panel">
        <label class="sidebar-label">演示角色</label>
        <select :value="session.role" @change="onRoleChange(($event.target as HTMLSelectElement).value)">
          <option v-for="item in session.roles" :key="item.value" :value="item.value">{{ item.label }}</option>
        </select>
      </div>

      <div class="sidebar-panel sidebar-tip">
        当前场景：{{ scenario.scenarioLabel }}<br />
        当前角色：{{ session.roleLabel }}<br />
        建议先从首页看板进入，再沿“调度指令 → 周报 → 协助申请”完成演示。
      </div>

      <div class="nav-section-title">核心业务链路</div>
      <RouterLink class="nav-link" to="/dashboard"><span>首页看板</span><span class="nav-badge">总览</span></RouterLink>
      <RouterLink class="nav-link" to="/dispatch-orders"><span>调度指令</span><span class="nav-badge">流程</span></RouterLink>
      <RouterLink class="nav-link" to="/group-reports"><span>周报上报</span><span class="nav-badge">填报</span></RouterLink>
      <RouterLink class="nav-link" to="/assist-requests"><span>协助申请</span><span class="nav-badge">协同</span></RouterLink>
      <RouterLink class="nav-link" to="/meetings"><span>会议通知</span><span class="nav-badge">同步</span></RouterLink>
      <RouterLink class="nav-link" to="/audit-logs"><span>审计摘要</span><span class="nav-badge">追溯</span></RouterLink>
    </aside>
    <main class="main">
      <div class="page-shell">
        <RouterView />
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { useScenarioStore, type ScenarioCode } from '@/stores/scenario'
import { useSessionStore, type RoleCode } from '@/stores/session'

const scenario = useScenarioStore()
const session = useSessionStore()

const onScenarioChange = (value: string) => {
  scenario.setScenario(value as ScenarioCode)
  window.location.reload()
}

const onRoleChange = (value: string) => {
  session.setRole(value as RoleCode)
}
</script>
