<template>
  <PageHeader title="首页看板" subtitle="围绕指令签收、周报填报、横向协同和审计追踪展示整体运行态势。">
    <select :value="session.role" @change="onRoleChange(($event.target as HTMLSelectElement).value)">
      <option v-for="item in session.roles" :key="item.value" :value="item.value">{{ item.label }}</option>
    </select>
    <span class="meta-pill">当前场景：{{ scenario.scenarioLabel }}</span>
  </PageHeader>

  <div class="hero-banner">
    <div class="hero-panel">
      <div class="hero-title">巡办与巡组双向信息传递一体化看板</div>
      <div class="hero-desc">
        当前原型通过统一的调度、上报、协同和审计视图，展示上传下达模块在不同业务场景下的运行状态。
        适合做方案评审、领导演示和后续开发分工讨论。
      </div>
      <div class="hero-metrics">
        <span class="hero-chip">待签收 {{ data.pendingAck }}</span>
        <span class="hero-chip">逾期 {{ data.overdue }}</span>
        <span class="hero-chip">周报提交率 {{ data.weeklyRate }}</span>
        <span class="hero-chip">协助申请未结 {{ data.openAssists }}</span>
      </div>
    </div>
    <div class="hero-panel">
      <div class="section-head">
        <div>
          <h2>演示建议</h2>
          <div class="section-subtitle">先看风险，再下钻到对应业务页面。</div>
        </div>
      </div>
      <div class="info-strip">
        <div>
          <div class="info-strip-label">建议路径</div>
          <div class="info-strip-value">看板 → 调度指令 → 周报 → 协助申请 → 审计摘要</div>
        </div>
      </div>
      <div class="info-strip">
        <div>
          <div class="info-strip-label">适合讲解对象</div>
          <div class="info-strip-value">巡办、巡组、横向协同部门、项目评审组</div>
        </div>
      </div>
    </div>
  </div>

  <div class="card-grid">
    <KpiCard label="待签收数量" :value="data.pendingAck" hint="待巡组签收调度或材料" icon="📨" tone="primary" trend="较昨日 -1" />
    <KpiCard label="逾期事项" :value="data.overdue" hint="需催办与升级预警" icon="⏰" tone="danger" trend="高优先级" />
    <KpiCard label="周报提交率" :value="data.weeklyRate" hint="巡组填报完成度" icon="📝" tone="success" trend="目标 ≥ 90%" />
    <KpiCard label="协助申请未结" :value="data.openAssists" hint="横向协同处理中" icon="🤝" tone="warning" trend="跨部门关注" />
  </div>

  <div class="dual-column">
    <div class="section">
      <div class="section-head">
        <div>
          <h2>最近风险事项</h2>
          <div class="section-subtitle">用于快速下钻到重点事项详情。</div>
        </div>
      </div>
      <div class="table-wrap">
        <table class="table">
          <thead>
            <tr><th>风险编号</th><th>事项</th><th>等级</th><th>去向</th></tr>
          </thead>
          <tbody>
            <tr v-for="item in data.risks" :key="item.id">
              <td>{{ item.id }}</td>
              <td>
                <div class="table-title">{{ item.title }}</div>
                <div class="table-desc">根据当前场景自动收敛至相关页面。</div>
              </td>
              <td><StatusBadge :label="item.level" :variant="item.level === '高' ? 'danger' : 'warning'" /></td>
              <td><RouterLink class="link-button" :to="item.link">查看详情</RouterLink></td>
            </tr>
            <tr v-if="data.risks.length === 0">
              <td colspan="4">
                <EmptyState icon="✅" title="当前场景无风险项" description="可用于演示已办结归档场景下的闭环效果。" />
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div>
      <div class="notice-panel warning" v-if="data.overdue > 0">
        <div class="notice-title">逾期预警提示</div>
        <div class="notice-desc">当前存在 {{ data.overdue }} 个逾期事项，建议从“调度指令”进入查看催办与升级预警流程。</div>
      </div>
      <div class="notice-panel info">
        <div class="notice-title">角色视角提示</div>
        <div class="notice-desc">
          巡办侧适合从“总览与催办”切入，巡组侧适合从“周报填报与反馈”切入，横向协同部门适合从“协助申请详情”切入。
        </div>
      </div>
      <InfoStrip label="当前角色" :value="session.roleLabel" extra="可以在页面右上角或左侧切换角色。" />
      <InfoStrip label="演示场景" :value="scenario.scenarioLabel" extra="切换场景后会同步刷新 mock 数据。" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { repository } from '@/services/api/repository'
import { useSessionStore, type RoleCode } from '@/stores/session'
import { useScenarioStore } from '@/stores/scenario'
import KpiCard from '@/components/common/KpiCard.vue'
import StatusBadge from '@/components/common/StatusBadge.vue'
import PageHeader from '@/components/common/PageHeader.vue'
import InfoStrip from '@/components/common/InfoStrip.vue'
import EmptyState from '@/components/common/EmptyState.vue'

const session = useSessionStore()
const scenario = useScenarioStore()
const data = repository.getDashboard()
const onRoleChange = (role: string) => session.setRole(role as RoleCode)
</script>
